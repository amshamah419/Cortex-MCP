#!/usr/bin/env python3
"""
Code generator that reads OpenAPI specs and generates MCP tools.
Reads specs/*.yaml and writes server/generated_*_tools.py with snake_case tool names.
"""

import re
from pathlib import Path
from typing import Any, Dict, List

import yaml


def to_snake_case(name: str) -> str:
    """Convert camelCase or PascalCase to snake_case."""
    # Insert underscore before uppercase letters and convert to lowercase
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def get_parameter_type(param_schema: Dict[str, Any]) -> str:
    """Convert OpenAPI type to Python type hint."""
    type_mapping = {
        "string": "str",
        "integer": "int",
        "number": "float",
        "boolean": "bool",
        "array": "List[Any]",
        "object": "Dict[str, Any]",
    }
    param_type = param_schema.get("type", "string")
    return type_mapping.get(param_type, "Any")


def generate_parameter_schema(
    parameters: List[Dict[str, Any]], request_body: Dict[str, Any] | None = None
) -> tuple[List[str], List[str]]:
    """Generate parameter definitions and schema properties."""
    param_defs = []
    schema_props = []

    # Process query and path parameters
    for param in parameters:
        param_name = to_snake_case(param["name"])
        param_type = get_parameter_type(param.get("schema", {}))
        required = param.get("required", False)
        description = param.get("description", "")

        # Add parameter definition
        if required:
            param_defs.append(f"    {param_name}: {param_type},")
        else:
            param_defs.append(f"    {param_name}: {param_type} | None = None,")

        # Add to schema
        schema_props.append(
            f'        "{param_name}": {{"type": "{param_type}", "description": "{description}"}},'
        )

    # Process request body if present
    if request_body:
        content = request_body.get("content", {})
        json_content = content.get("application/json", {})
        body_schema = json_content.get("schema", {})

        if body_schema:
            properties = body_schema.get("properties", {})
            required_props = body_schema.get("required", [])

            for prop_name, prop_schema in properties.items():
                snake_prop = to_snake_case(prop_name)
                prop_type = get_parameter_type(prop_schema)
                prop_desc = prop_schema.get("description", "")
                is_required = prop_name in required_props

                if is_required:
                    param_defs.append(f"    {snake_prop}: {prop_type},")
                else:
                    param_defs.append(f"    {snake_prop}: {prop_type} | None = None,")

                schema_props.append(
                    f'        "{snake_prop}": {{"type": "{prop_type}", "description": "{prop_desc}"}},'
                )

    return param_defs, schema_props


def generate_tool_function(
    operation_id: str,
    method: str,
    path: str,
    operation: Dict[str, Any],
    base_url: str,
) -> str:
    """Generate a single tool function from an OpenAPI operation."""
    tool_name = to_snake_case(operation_id)
    summary = operation.get("summary", "")
    description = operation.get("description", summary)

    # Get parameters
    parameters = operation.get("parameters", [])
    request_body = operation.get("requestBody")

    param_defs, schema_props = generate_parameter_schema(parameters, request_body)

    # Build function signature
    param_str = "\n".join(param_defs) if param_defs else ""

    # Build schema properties
    schema_str = "\n".join(schema_props) if schema_props else ""

    # Build the function
    function_code = f'''
@server.call_tool()
async def {tool_name}(
{param_str}
) -> List[types.TextContent]:
    """
    {description}
    
    Args:
        Tool arguments are defined in the schema below
    
    Returns:
        List of text content with the API response
    """
    # Build request parameters
    params = {{}}
    body = {{}}
    path_params = {{}}
    
'''

    # Add parameter building logic
    for param in parameters:
        param_name = to_snake_case(param["name"])
        original_name = param["name"]
        param_in = param.get("in", "query")

        function_code += f"""    if {param_name} is not None:
"""
        if param_in == "path":
            function_code += f"""        path_params["{original_name}"] = {param_name}
"""
        elif param_in == "query":
            function_code += f"""        params["{original_name}"] = {param_name}
"""

    # Add request body building logic
    if request_body:
        content = request_body.get("content", {})
        json_content = content.get("application/json", {})
        body_schema = json_content.get("schema", {})

        if body_schema:
            properties = body_schema.get("properties", {})
            for prop_name in properties.keys():
                snake_prop = to_snake_case(prop_name)
                function_code += f"""    if {snake_prop} is not None:
        body["{prop_name}"] = {snake_prop}
"""

    # Build the URL with path parameters
    function_code += f"""
    # Build URL
    url = "{base_url}{path}"
    for key, value in path_params.items():
        url = url.replace("{{" + key + "}}", str(value))
    
    # Make the API request
    async with httpx.AsyncClient() as client:
        response = await client.request(
            method="{method.upper()}",
            url=url,
            params=params,
            json=body if body else None,
        )
        response.raise_for_status()
        result = response.json()
    
    return [
        types.TextContent(
            type="text",
            text=f"{{result}}",
        )
    ]


# Schema for {tool_name}
{tool_name}_schema = {{
    "type": "object",
    "properties": {{
{schema_str}
    }},
}}
"""

    return function_code


def generate_tools_file(spec_path: Path, output_dir: Path) -> None:
    """Generate a tools file from an OpenAPI spec."""
    with open(spec_path, "r") as f:
        spec = yaml.safe_load(f)

    # Extract spec name from filename
    spec_name = spec_path.stem
    output_file = output_dir / f"generated_{spec_name}_tools.py"

    # Get base URL
    servers = spec.get("servers", [])
    base_url = servers[0]["url"] if servers else ""

    # File header
    file_content = f'''"""
Auto-generated MCP tools for {spec_name.upper()}.
Generated from OpenAPI specification: {spec_path.name}

DO NOT EDIT THIS FILE MANUALLY - it is auto-generated by codegen/generator.py
"""

from typing import Any, Dict, List

import httpx
from mcp.server import Server
from mcp.types import Tool
from mcp import types

# This will be set by the server initialization
server: Server = None  # type: ignore


def set_server(s: Server) -> None:
    """Set the server instance for tool registration."""
    global server
    server = s

'''

    # Generate tool functions
    paths = spec.get("paths", {})
    for path, path_item in paths.items():
        for method in ["get", "post", "put", "patch", "delete"]:
            if method in path_item:
                operation = path_item[method]
                operation_id = operation.get("operationId")
                if operation_id:
                    tool_code = generate_tool_function(
                        operation_id, method, path, operation, base_url
                    )
                    file_content += tool_code

    # Write the file
    with open(output_file, "w") as f:
        f.write(file_content)

    print(f"Generated {output_file}")


def main() -> None:
    """Main entry point for code generation."""
    # Get project root
    project_root = Path(__file__).parent.parent

    # Input and output directories
    specs_dir = project_root / "specs"
    output_dir = project_root / "server"

    # Create output directory if it doesn't exist
    output_dir.mkdir(exist_ok=True)

    # Process all YAML specs
    spec_files = list(specs_dir.glob("*.yaml")) + list(specs_dir.glob("*.yml"))

    if not spec_files:
        print("No OpenAPI specs found in specs/ directory")
        return

    for spec_file in spec_files:
        print(f"Processing {spec_file.name}...")
        generate_tools_file(spec_file, output_dir)

    print(f"\nGenerated {len(spec_files)} tool files in {output_dir}")


if __name__ == "__main__":
    main()
