#!/usr/bin/env python3
"""
Code generator that reads OpenAPI specs and generates MCP tools.
Reads specs/*.yaml and specs/*.json and writes server/generated_*_tools.py with snake_case tool names.
"""

import json
import re
from pathlib import Path
from typing import Any, Dict, List

import yaml


def strip_http_verb_prefix(name: str, http_method: str = "") -> str:
    """
    Strip HTTP verb prefix from operation ID if it matches the actual HTTP method.

    For example:
        postStartXqlQuery (POST) -> StartXqlQuery
        getIncidents (GET) -> Incidents
        getAutomationScripts (POST) -> getAutomationScripts (no change, doesn't match method)

    Args:
        name: The operation ID to process
        http_method: The actual HTTP method for this operation (get, post, put, patch, delete)

    Returns:
        The name with HTTP verb prefix stripped if it matches the method
    """
    if not http_method:
        return name

    # Normalize the HTTP method to lowercase
    http_method = http_method.lower()

    # Check if name starts with the HTTP method (case-insensitive)
    if name.lower().startswith(http_method):
        # Check if there's a character after the method
        method_len = len(http_method)
        if len(name) > method_len:
            # Get the character after the method
            next_char = name[method_len]
            # Strip the method if the next character is uppercase, underscore, or hyphen
            # This ensures we don't strip "get" from "getter" but do strip from "getItems"
            if next_char.isupper() or next_char in ["_", "-"]:
                # Return the name without the method prefix
                return name[method_len:]

    return name


def clean_public_api_name(name: str) -> str:
    """
    Clean up public_api names by removing the public_api prefix and moving version to end.

    For example:
        public_api-v1-alerts-get_alerts -> alerts-get_alerts-v1
        -public_api-v1-alerts-get_alerts -> alerts-get_alerts-v1 (leading hyphen handled)
        public_api-v2-alerts-get_alerts_multi_events -> alerts-get_alerts_multi_events-v2

    Args:
        name: The name to clean (with hyphens, before snake_case conversion)

    Returns:
        The cleaned name with version moved to end
    """
    # Remove leading hyphens or underscores
    name = name.lstrip("-_")

    # Check if this is a public_api name
    if not name.startswith("public_api-"):
        return name

    # Remove public_api- prefix
    name = name[len("public_api-") :]

    # Extract version (v1, v2, etc.) if present
    version_match = re.match(r"^(v\d+)-(.*)", name)
    if version_match:
        version = version_match.group(1)
        rest = version_match.group(2)
        # Move version to the end
        return f"{rest}-{version}"

    return name


def to_snake_case(name: str, http_method: str = "") -> str:
    """
    Convert camelCase or PascalCase to snake_case and handle hyphens.

    Args:
        name: The name to convert
        http_method: Optional HTTP method to strip as prefix if it matches

    Returns:
        The name converted to snake_case
    """
    # Strip HTTP verb prefix if it matches the method
    name = strip_http_verb_prefix(name, http_method)
    # Clean up public_api names before converting to snake_case
    name = clean_public_api_name(name)
    # Replace hyphens with underscores first
    name = name.replace("-", "_")
    # Remove angle brackets and other special characters that aren't valid in Python identifiers
    name = re.sub(r"[<>]", "", name)
    # Insert underscore before uppercase letters and convert to lowercase
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def clean_description(description: str) -> str:
    """Clean and escape description text for use in Python strings."""
    if not description:
        return ""
    # Replace newlines with spaces
    description = description.replace("\n", " ").replace("\r", " ")
    # Replace multiple spaces with single space
    description = re.sub(r"\s+", " ", description)
    # Escape quotes
    description = description.replace('"', '\\"')
    # Trim
    return description.strip()


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

    # Handle case where type might be a list or None (e.g., enum fields without explicit type)
    if isinstance(param_type, list):
        # If type is a list, use the first non-null type
        param_type = next((t for t in param_type if t != "null"), "string")
    elif param_type is None or param_type == "":
        # If no type specified but has enum, it's likely a string
        if "enum" in param_schema:
            param_type = "string"
        else:
            param_type = "string"

    return type_mapping.get(param_type, "Any")


def generate_nested_assignments(
    properties: Dict[str, Any],
    target_var: str = "current_obj",
    prefix: str = "",
    indent: str = "    ",
    collision_names: set = None,
) -> List[str]:
    """
    Generate code lines to assign flat parameters to a nested object structure.

    Args:
        properties: The properties dictionary from the schema
        target_var: The variable name to assign to
        prefix: Prefix for parameter names
        indent: Indentation string
        collision_names: Set of names that have collisions and need prefixes

    Returns:
        List of code lines
    """
    if collision_names is None:
        collision_names = set()

    lines = []

    for prop_name, prop_schema in properties.items():
        snake_prop = to_snake_case(prop_name)
        full_param_name = f"{prefix}{snake_prop}" if prefix else snake_prop
        prop_type = prop_schema.get("type")
        nested_properties = prop_schema.get("properties", {})

        # If this is an object with properties, build it recursively
        if prop_type == "object" and nested_properties:
            nested_var = f"{snake_prop}_obj"
            lines.append(f"{indent}# Build {prop_name} nested object")
            lines.append(f"{indent}{nested_var} = {{}}")

            # Recursively generate assignments for nested properties
            nested_lines = generate_nested_assignments(
                nested_properties,
                target_var=nested_var,
                prefix=f"{full_param_name}_",
                indent=indent,
                collision_names=collision_names,
            )
            lines.extend(nested_lines)

            lines.append(f"{indent}if {nested_var}:")
            lines.append(f'{indent}    {target_var}["{prop_name}"] = {nested_var}')
        else:
            # Leaf node - add assignment
            # Use simple name if no collision, otherwise use full path
            param_name = full_param_name if snake_prop in collision_names else snake_prop

            lines.append(f"{indent}if {param_name} is not None:")
            lines.append(f'{indent}    {target_var}["{prop_name}"] = {param_name}')

    return lines


def collect_all_parameter_names(
    properties: Dict[str, Any], prefix: str = ""
) -> Dict[str, List[str]]:
    """
    Collect all parameter names and their paths to detect naming collisions.

    Args:
        properties: The properties dictionary from the schema
        prefix: Current path prefix

    Returns:
        Dictionary mapping simple names to list of full paths
    """
    name_to_paths = {}

    for prop_name, prop_schema in properties.items():
        snake_prop = to_snake_case(prop_name)
        full_path = f"{prefix}{snake_prop}" if prefix else snake_prop
        prop_type = prop_schema.get("type")
        nested_properties = prop_schema.get("properties", {})

        # If this is an object with properties, recurse
        if prop_type == "object" and nested_properties:
            nested_names = collect_all_parameter_names(nested_properties, prefix=f"{full_path}_")
            # Merge nested names into our collection
            for name, paths in nested_names.items():
                if name not in name_to_paths:
                    name_to_paths[name] = []
                name_to_paths[name].extend(paths)
        else:
            # Leaf node - record this name
            if snake_prop not in name_to_paths:
                name_to_paths[snake_prop] = []
            name_to_paths[snake_prop].append(full_path)

    return name_to_paths


def expand_nested_properties(
    properties: Dict[str, Any],
    required_props: List[str],
    param_defs_required: List[str],
    param_defs_optional: List[str],
    schema_props: List[str],
    param_info: List[Dict[str, Any]],
    prefix: str = "",
    collision_names: set = None,
) -> None:
    """
    Recursively expand nested object properties into individual parameters.

    Args:
        properties: The properties dictionary from the schema
        required_props: List of required property names
        param_defs_required: List to append required parameter definitions to
        param_defs_optional: List to append optional parameter definitions to
        schema_props: List to append schema property definitions to
        param_info: List to append parameter info dictionaries to
        prefix: Prefix for nested property names (e.g., "update_data_")
        collision_names: Set of names that have collisions and need prefixes
    """
    if collision_names is None:
        collision_names = set()

    for prop_name, prop_schema in properties.items():
        snake_prop = to_snake_case(prop_name)
        full_param_name = f"{prefix}{snake_prop}" if prefix else snake_prop
        prop_type = prop_schema.get("type")
        prop_desc = clean_description(prop_schema.get("description", ""))
        is_required = prop_name in required_props

        # If this is an object with properties, expand it recursively
        # But only if it has defined properties (not a free-form object)
        nested_properties = prop_schema.get("properties", {})
        if prop_type == "object" and nested_properties:
            nested_required = prop_schema.get("required", [])
            expand_nested_properties(
                nested_properties,
                nested_required,
                param_defs_required,
                param_defs_optional,
                schema_props,
                param_info,
                prefix=f"{full_param_name}_",
                collision_names=collision_names,
            )
        else:
            # Leaf node - add as a parameter
            param_type = get_parameter_type(prop_schema)

            # Use simple name if no collision, otherwise use full path
            param_name = full_param_name if snake_prop in collision_names else snake_prop

            if is_required:
                param_defs_required.append(f"    {param_name}: {param_type},")
            else:
                param_defs_optional.append(f"    {param_name}: {param_type} | None = None,")

            schema_props.append(
                f'        "{param_name}": {{"type": "{param_type}", "description": "{prop_desc}"}},'
            )

            param_info.append(
                {
                    "name": param_name,
                    "type": param_type,
                    "required": is_required,
                    "description": prop_desc if prop_desc else "No description provided",
                    "location": "body",
                    "original_name": prop_name,
                    "prefix": prefix,
                    "full_path": full_param_name,
                }
            )


def generate_parameter_schema(
    parameters: List[Dict[str, Any]], request_body: Dict[str, Any] | None = None
) -> tuple[List[str], List[str], List[Dict[str, Any]]]:
    """Generate parameter definitions, schema properties, and parameter info for documentation."""
    required_param_defs = []
    optional_param_defs = []
    schema_props = []
    param_info = []  # For docstring generation

    # Process query, path, and header parameters (skip body/formData - handled differently)
    for param in parameters:
        param_in = param.get("in", "query")
        if param_in in ["body", "formData"]:
            # Body and formData parameters are handled differently
            # For OpenAPI 2.0 compatibility, skip them here
            continue

        param_name = to_snake_case(param["name"])
        param_type = get_parameter_type(param.get("schema", {}))
        required = param.get("required", False)
        description = clean_description(param.get("description", ""))

        # Add parameter definition - separate required from optional
        if required:
            required_param_defs.append(f"    {param_name}: {param_type},")
        else:
            optional_param_defs.append(f"    {param_name}: {param_type} | None = None,")

        # Add to schema
        schema_props.append(
            f'        "{param_name}": {{"type": "{param_type}", "description": "{description}"}},'
        )

        # Add to param_info for docstring
        param_info.append(
            {
                "name": param_name,
                "type": param_type,
                "required": required,
                "description": description if description else "No description provided",
                "location": param_in,
            }
        )

    # Process request body if present
    if request_body:
        content = request_body.get("content", {})
        json_content = content.get("application/json", {})
        body_schema = json_content.get("schema", {})

        if body_schema:
            properties = body_schema.get("properties", {})
            required_props = body_schema.get("required", [])

            # Check if this is a request_data wrapper pattern
            # If there's only one property named "request_data" that is an object,
            # expand its nested properties instead (recursively)
            if (
                len(properties) == 1
                and "request_data" in properties
                and properties["request_data"].get("type") == "object"
            ):
                request_data_schema = properties["request_data"]
                nested_properties = request_data_schema.get("properties", {})
                nested_required = request_data_schema.get("required", [])

                # First, collect all parameter names to detect collisions
                name_to_paths = collect_all_parameter_names(nested_properties, prefix="")

                # Find names that appear more than once (collisions)
                collision_names = {name for name, paths in name_to_paths.items() if len(paths) > 1}

                # Use recursive expansion to handle nested objects
                expand_nested_properties(
                    nested_properties,
                    nested_required,
                    required_param_defs,
                    optional_param_defs,
                    schema_props,
                    param_info,
                    prefix="",
                    collision_names=collision_names,
                )
            else:
                # Regular request body processing (no request_data wrapper)
                for prop_name, prop_schema in properties.items():
                    snake_prop = to_snake_case(prop_name)
                    prop_type = get_parameter_type(prop_schema)
                    prop_desc = clean_description(prop_schema.get("description", ""))
                    is_required = prop_name in required_props

                    if is_required:
                        required_param_defs.append(f"    {snake_prop}: {prop_type},")
                    else:
                        optional_param_defs.append(f"    {snake_prop}: {prop_type} | None = None,")

                    schema_props.append(
                        f'        "{snake_prop}": {{"type": "{prop_type}", "description": "{prop_desc}"}},'
                    )

                    # Add to param_info for docstring
                    param_info.append(
                        {
                            "name": snake_prop,
                            "type": prop_type,
                            "required": is_required,
                            "description": prop_desc if prop_desc else "No description provided",
                            "location": "body",
                        }
                    )

    # Combine required params first, then optional (Python requirement)
    param_defs = required_param_defs + optional_param_defs

    return param_defs, schema_props, param_info


def generate_tool_function(
    operation_id: str,
    method: str,
    path: str,
    operation: Dict[str, Any],
    base_url: str,
    service_prefix: str = "",
) -> str:
    """Generate a single tool function from an OpenAPI operation."""
    tool_name = to_snake_case(operation_id, method)
    # Prepend service prefix if provided
    if service_prefix:
        tool_name = f"{service_prefix}_{tool_name}"
    summary = operation.get("summary", "")
    description = operation.get("description", summary)

    # Get parameters
    parameters = operation.get("parameters", [])
    request_body = operation.get("requestBody")

    param_defs, schema_props, param_info = generate_parameter_schema(parameters, request_body)

    # Build function signature
    param_str = "\n".join(param_defs) if param_defs else ""

    # Build schema properties
    schema_str = "\n".join(schema_props) if schema_props else ""

    # Build parameter documentation for docstring
    param_doc_lines = []
    if param_info:
        for param in param_info:
            required_str = "(required)" if param["required"] else "(optional)"
            # Format: param_name (type): description [required/optional]
            param_doc_lines.append(
                f"        {param['name']} ({param['type']}): {param['description']} {required_str}"
            )

    param_doc = "\n".join(param_doc_lines) if param_doc_lines else "        No parameters required"

    # Get response information from OpenAPI spec
    responses = operation.get("responses", {})
    success_response = responses.get("200") or responses.get("201") or responses.get("204")
    response_desc = "API response data"
    if success_response:
        response_desc = success_response.get("description", response_desc)

    # Determine which service this is for
    service_env_var = ""
    if service_prefix == "xsiam":
        service_env_var = "XSIAM_API_URL"
    elif service_prefix == "xsoar":
        service_env_var = "XSOAR_API_URL"

    # Build the function
    function_code = f'''
@server.call_tool()
async def {tool_name}(
{param_str}
) -> List[types.TextContent]:
    """
    {description}
    
    Args:
{param_doc}
    
    Returns:
        List[types.TextContent]: {response_desc}
    """
    # Input validation
    validate_inputs(locals())
    
    # Build request parameters
    params = {{}}
    body = {{}}
    path_params = {{}}
    headers = {{}}
    
'''

    # Add parameter building logic
    for param in parameters:
        param_name = to_snake_case(param["name"])
        original_name = param["name"]
        param_in = param.get("in", "query")

        # Skip body and formData parameters - they're handled differently
        if param_in in ["body", "formData"]:
            continue

        function_code += f"""    if {param_name} is not None:
"""
        if param_in == "path":
            function_code += f"""        path_params["{original_name}"] = sanitize_input({param_name})
"""
        elif param_in == "query":
            function_code += f"""        params["{original_name}"] = sanitize_input({param_name})
"""
        elif param_in == "header":
            function_code += f"""        headers["{original_name}"] = sanitize_input({param_name})
"""

    # Add request body building logic
    if request_body:
        content = request_body.get("content", {})
        json_content = content.get("application/json", {})
        body_schema = json_content.get("schema", {})

        if body_schema:
            properties = body_schema.get("properties", {})

            # Check if this is a request_data wrapper pattern
            if (
                len(properties) == 1
                and "request_data" in properties
                and properties["request_data"].get("type") == "object"
            ):
                # Expand request_data properties
                request_data_schema = properties["request_data"]
                nested_properties = request_data_schema.get("properties", {})

                # First, collect all parameter names to detect collisions
                name_to_paths = collect_all_parameter_names(nested_properties, prefix="")

                # Find names that appear more than once (collisions)
                collision_names = {name for name, paths in name_to_paths.items() if len(paths) > 1}

                # Build the request_data object from expanded parameters (recursively)
                function_code += """    # Build request_data object from parameters
    request_data_obj = {}
"""
                # Generate nested assignment code
                assignment_lines = generate_nested_assignments(
                    nested_properties,
                    target_var="request_data_obj",
                    prefix="",
                    indent="    ",
                    collision_names=collision_names,
                )
                function_code += "\n".join(assignment_lines) + "\n"

                function_code += """    if request_data_obj:
        body["request_data"] = request_data_obj
"""
            else:
                # Regular request body processing (no request_data wrapper)
                for prop_name in properties.keys():
                    snake_prop = to_snake_case(prop_name)
                    function_code += f"""    if {snake_prop} is not None:
        body["{prop_name}"] = {snake_prop}
"""

    # Build the URL with path parameters
    url_config_part = ""
    if service_env_var:
        url_config_part = f"""
    # Get base URL from environment
    base_url = get_api_config().get("{service_prefix.lower()}_api_url", "{base_url}")
    url = base_url + "{path}"
"""
    else:
        url_config_part = f"""
    # Build URL
    url = "{base_url}{path}"
"""

    function_code += url_config_part
    function_code += f"""    for key, value in path_params.items():
        url = url.replace("{{" + key + "}}", str(value))
    
    # Make the API request with security controls
    try:
        async with get_http_client() as client:
            response = await client.request(
                method="{method.upper()}",
                url=url,
                params=params,
                headers=headers,
                json=body if body else None,
            )
            response.raise_for_status()
            result = response.json()
    except httpx.HTTPStatusError as e:
        # Sanitize error messages to prevent information leakage
        return [
            types.TextContent(
                type="text",
                text=sanitize_error_message(str(e)),
            )
        ]
    except Exception as e:
        return [
            types.TextContent(
                type="text",
                text=sanitize_error_message(f"Request failed: {{str(e)}}"),
            )
        ]
    
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
    # Load the spec based on file extension
    if spec_path.suffix.lower() in [".json"]:
        with open(spec_path, "r") as f:
            spec = json.load(f)
    elif spec_path.suffix.lower() in [".yaml", ".yml"]:
        with open(spec_path, "r") as f:
            spec = yaml.safe_load(f)
    else:
        print(f"Unsupported file format: {spec_path.suffix}")
        return

    # Extract spec name from filename (without extension)
    spec_name = spec_path.stem
    output_file = output_dir / f"generated_{spec_name}_tools.py"

    # Get base URL
    servers = spec.get("servers", [])
    base_url = servers[0]["url"] if servers else ""

    # First pass: collect all tool names to detect collisions
    tool_names: Dict[str, List[tuple[str, str, str]]] = {}  # name -> [(operation_id, method, path)]
    paths = spec.get("paths", {})
    for path, path_item in paths.items():
        for method in ["get", "post", "put", "patch", "delete"]:
            if method in path_item:
                operation = path_item[method]
                operation_id = operation.get("operationId")
                if operation_id:
                    tool_name = to_snake_case(operation_id, method)
                    if tool_name not in tool_names:
                        tool_names[tool_name] = []
                    tool_names[tool_name].append((operation_id, method, path))

    # Identify collisions - names that appear more than once
    collisions = {name for name, ops in tool_names.items() if len(ops) > 1}

    # File header
    file_content = f'''"""
Auto-generated MCP tools for {spec_name.upper()}.
Generated from OpenAPI specification: {spec_path.name}

DO NOT EDIT THIS FILE MANUALLY - it is auto-generated by codegen/generator.py
"""

from typing import Any, Dict, List
import os
import re

import httpx
from mcp.server import Server
from mcp import types

# This will be set by the server initialization
server: Server = None  # type: ignore


def get_api_config() -> Dict[str, str]:
    """Get API configuration from environment variables."""
    return {{
        "xsiam_api_url": os.getenv("XSIAM_API_URL", "https://api-yourfqdn"),
        "xsoar_api_url": os.getenv("XSOAR_API_URL", "https://your-xsoar-instance.com"),
        "timeout": int(os.getenv("API_TIMEOUT", "30")),
        "max_retries": int(os.getenv("API_MAX_RETRIES", "3")),
        "verify_ssl": os.getenv("VERIFY_SSL", "true").lower() == "true",
    }}


def get_http_client() -> httpx.AsyncClient:
    """Create a configured HTTP client with security settings."""
    config = get_api_config()
    return httpx.AsyncClient(
        timeout=config["timeout"],
        verify=config["verify_ssl"],
        limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),
    )


def sanitize_input(value: Any) -> Any:
    """Sanitize user input to prevent injection attacks."""
    if isinstance(value, str):
        # Remove potentially dangerous characters
        # Allow alphanumeric, spaces, hyphens, underscores, and common punctuation
        sanitized = re.sub(r'[^\\w\\s\\-_.@,:/]', '', value)
        # Limit length to prevent DoS
        return sanitized[:1000]
    return value


def validate_inputs(params: Dict[str, Any]) -> None:
    """Validate input parameters."""
    for key, value in params.items():
        if key == "self":  # Skip 'self' from locals()
            continue
        if value is not None and isinstance(value, str):
            # Check for extremely long inputs
            if len(value) > 10000:
                raise ValueError(f"Input parameter '{{key}}' exceeds maximum length")


def sanitize_error_message(error: str) -> str:
    """Sanitize error messages to prevent information leakage."""
    # Remove sensitive information patterns
    sanitized = re.sub(r'api[_-]?key[=:]?[\\s]?[\\w-]+', 'API_KEY_REDACTED', error, flags=re.IGNORECASE)
    sanitized = re.sub(r'token[=:]?[\\s]?[\\w-]+', 'TOKEN_REDACTED', sanitized, flags=re.IGNORECASE)
    sanitized = re.sub(r'password[=:]?[\\s]?[\\w-]+', 'PASSWORD_REDACTED', sanitized, flags=re.IGNORECASE)
    # Limit error message length
    return sanitized[:500]



def set_server(s: Server) -> None:
    """Set the server instance for tool registration."""
    global server
    server = s

'''

    # Generate tool functions
    for path, path_item in paths.items():
        for method in ["get", "post", "put", "patch", "delete"]:
            if method in path_item:
                operation = path_item[method]
                operation_id = operation.get("operationId")
                if operation_id:
                    # Check if this would be a collision
                    tool_name = to_snake_case(operation_id, method)
                    # For collisions, don't pass the method so the HTTP verb prefix is kept
                    method_for_naming = "" if tool_name in collisions else method

                    tool_code = generate_tool_function(
                        operation_id,
                        method_for_naming,
                        path,
                        operation,
                        base_url,
                        spec_name,  # Pass the service name as prefix
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

    # Process all YAML and JSON specs
    spec_files = (
        list(specs_dir.glob("*.yaml"))
        + list(specs_dir.glob("*.yml"))
        + list(specs_dir.glob("*.json"))
    )

    if not spec_files:
        print("No OpenAPI specs found in specs/ directory")
        return

    for spec_file in spec_files:
        print(f"Processing {spec_file.name}...")
        generate_tools_file(spec_file, output_dir)

    print(f"\nGenerated {len(spec_files)} tool files in {output_dir}")


if __name__ == "__main__":
    main()
