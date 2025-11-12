"""Tests for the code generator."""

import tempfile
from pathlib import Path

import yaml

from codegen.generator import (
    generate_tools_file,
    to_snake_case,
    get_parameter_type,
    generate_parameter_schema,
)


def test_to_snake_case():
    """Test snake_case conversion."""
    assert to_snake_case("listIncidents") == "list_incidents"
    assert to_snake_case("createIncident") == "create_incident"
    assert to_snake_case("getIncidentID") == "get_incident_id"
    assert to_snake_case("executePlaybook") == "execute_playbook"


def test_get_parameter_type():
    """Test parameter type mapping."""
    assert get_parameter_type({"type": "string"}) == "str"
    assert get_parameter_type({"type": "integer"}) == "int"
    assert get_parameter_type({"type": "number"}) == "float"
    assert get_parameter_type({"type": "boolean"}) == "bool"
    assert get_parameter_type({"type": "array"}) == "List[Any]"
    assert get_parameter_type({"type": "object"}) == "Dict[str, Any]"


def test_generate_parameter_schema():
    """Test parameter schema generation."""
    parameters = [
        {
            "name": "limit",
            "in": "query",
            "required": False,
            "schema": {"type": "integer"},
            "description": "Maximum number of results",
        },
        {
            "name": "status",
            "in": "query",
            "required": True,
            "schema": {"type": "string"},
            "description": "Filter by status",
        },
    ]

    param_defs, schema_props = generate_parameter_schema(parameters)

    assert len(param_defs) == 2
    # Required params come first now
    assert "status: str," in param_defs[0]
    assert "limit: int | None = None," in param_defs[1]

    assert len(schema_props) == 2
    assert '"limit"' in schema_props[0] or '"limit"' in schema_props[1]
    assert '"status"' in schema_props[0] or '"status"' in schema_props[1]


def test_generate_tools_file():
    """Test generating a tools file from a spec."""
    # Create a minimal OpenAPI spec
    spec = {
        "openapi": "3.0.0",
        "info": {"title": "Test API", "version": "1.0.0"},
        "servers": [{"url": "https://api.test.com"}],
        "paths": {
            "/items": {
                "get": {
                    "operationId": "listItems",
                    "summary": "List items",
                    "description": "Get all items",
                    "parameters": [
                        {
                            "name": "limit",
                            "in": "query",
                            "required": False,
                            "schema": {"type": "integer"},
                            "description": "Max items",
                        }
                    ],
                    "responses": {"200": {"description": "Success"}},
                }
            }
        },
    }

    with tempfile.TemporaryDirectory() as tmpdir:
        spec_path = Path(tmpdir) / "test.yaml"
        output_dir = Path(tmpdir) / "output"
        output_dir.mkdir()

        # Write the spec
        with open(spec_path, "w") as f:
            yaml.dump(spec, f)

        # Generate the tools file
        generate_tools_file(spec_path, output_dir)

        # Check the output file exists
        output_file = output_dir / "generated_test_tools.py"
        assert output_file.exists()

        # Check the content
        content = output_file.read_text()
        assert "def list_items" in content
        assert "limit: int | None = None" in content
        assert "async def list_items" in content
        assert "@server.call_tool()" in content
