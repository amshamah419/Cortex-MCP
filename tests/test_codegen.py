"""Tests for the code generator."""

import tempfile
from pathlib import Path

import yaml

from codegen.generator import (
    generate_tools_file,
    to_snake_case,
    strip_http_verb_prefix,
    clean_public_api_name,
    get_parameter_type,
    generate_parameter_schema,
)


def test_strip_http_verb_prefix():
    """Test HTTP verb prefix stripping based on HTTP method."""
    # Test POST prefix stripping when method is POST
    assert strip_http_verb_prefix("postStartXqlQuery", "post") == "StartXqlQuery"
    assert strip_http_verb_prefix("postGetQueryResults", "post") == "GetQueryResults"
    assert strip_http_verb_prefix("postUpdateIncident", "post") == "UpdateIncident"

    # Test GET prefix stripping when method is GET
    assert strip_http_verb_prefix("getIncidents", "get") == "Incidents"
    assert strip_http_verb_prefix("getAutomationScripts", "get") == "AutomationScripts"

    # Test PUT prefix stripping when method is PUT
    assert strip_http_verb_prefix("putUpdateUser", "put") == "UpdateUser"

    # Test PATCH prefix stripping when method is PATCH
    assert strip_http_verb_prefix("patchModifyIncident", "patch") == "ModifyIncident"

    # Test DELETE prefix stripping when method is DELETE
    assert strip_http_verb_prefix("deleteRemoveAlert", "delete") == "RemoveAlert"

    # Test with hyphens
    assert (
        strip_http_verb_prefix("post-public_api-v1-alerts-get_alerts", "post")
        == "-public_api-v1-alerts-get_alerts"
    )

    # Test no stripping when prefix doesn't match method
    assert strip_http_verb_prefix("getAutomationScripts", "post") == "getAutomationScripts"
    assert strip_http_verb_prefix("postGetIncidents", "get") == "postGetIncidents"

    # Test no prefix (should remain unchanged)
    assert strip_http_verb_prefix("listIncidents", "post") == "listIncidents"
    assert strip_http_verb_prefix("createIncident", "post") == "createIncident"
    assert strip_http_verb_prefix("executePlaybook", "get") == "executePlaybook"

    # Test edge case: verb as whole word (should not strip)
    assert strip_http_verb_prefix("getter", "get") == "getter"
    assert strip_http_verb_prefix("poster", "post") == "poster"

    # Test without method parameter
    assert strip_http_verb_prefix("postStartXqlQuery", "") == "postStartXqlQuery"
    assert strip_http_verb_prefix("getIncidents", "") == "getIncidents"


def test_clean_public_api_name():
    """Test cleaning public_api names by moving version to end."""
    # Test v1 API
    assert clean_public_api_name("public_api-v1-alerts-get_alerts") == "alerts-get_alerts-v1"

    # Test v2 API
    assert (
        clean_public_api_name("public_api-v2-alerts-get_alerts_multi_events")
        == "alerts-get_alerts_multi_events-v2"
    )

    # Test with leading hyphen (from HTTP verb stripping)
    assert clean_public_api_name("-public_api-v1-alerts-get_alerts") == "alerts-get_alerts-v1"
    assert (
        clean_public_api_name("-public_api-v2-alerts-get_alerts_multi_events")
        == "alerts-get_alerts_multi_events-v2"
    )

    # Test non-public_api names (should remain unchanged)
    assert clean_public_api_name("startXqlQuery") == "startXqlQuery"
    assert clean_public_api_name("getIncidents") == "getIncidents"

    # Test public_api without version (edge case)
    assert clean_public_api_name("public_api-alerts-get_alerts") == "alerts-get_alerts"


def test_to_snake_case():
    """Test snake_case conversion."""
    # Basic conversions without HTTP method
    assert to_snake_case("listIncidents") == "list_incidents"
    assert to_snake_case("createIncident") == "create_incident"
    assert to_snake_case("executePlaybook") == "execute_playbook"

    # Test with HTTP method matching (should strip prefix)
    assert to_snake_case("postStartXqlQuery", "post") == "start_xql_query"
    assert to_snake_case("postGetQueryResults", "post") == "get_query_results"
    assert to_snake_case("getIncidents", "get") == "incidents"
    assert to_snake_case("postUpdateIncident", "post") == "update_incident"
    assert to_snake_case("deleteWidget", "delete") == "widget"

    # Test public_api name cleaning
    assert to_snake_case("public_api-v1-alerts-get_alerts", "post") == "alerts_get_alerts_v1"
    assert (
        to_snake_case("public_api-v2-alerts-get_alerts_multi_events", "post")
        == "alerts_get_alerts_multi_events_v2"
    )

    # Test with HTTP method not matching (should not strip)
    assert to_snake_case("getAutomationScripts", "post") == "get_automation_scripts"
    assert to_snake_case("getIncidentID", "post") == "get_incident_id"


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

        # Check the content - now includes service prefix
        content = output_file.read_text()
        assert "def test_list_items" in content
        assert "limit: int | None = None" in content
        assert "async def test_list_items" in content
        assert "@server.call_tool()" in content
