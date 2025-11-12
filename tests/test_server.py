"""Tests for the MCP server."""

from pathlib import Path


def test_generated_files_exist():
    """Test that generated tool files exist."""
    server_dir = Path(__file__).parent.parent / "server"

    # Check for generated files
    xsiam_tools = server_dir / "generated_xsiam_tools.py"
    xsoar_tools = server_dir / "generated_xsoar_tools.py"

    assert xsiam_tools.exists(), "XSIAM tools file should exist"
    assert xsoar_tools.exists(), "XSOAR tools file should exist"


def test_generated_files_content():
    """Test that generated files have expected content."""
    server_dir = Path(__file__).parent.parent / "server"

    # Check XSIAM tools - HTTP verb prefix should be removed
    xsiam_content = (server_dir / "generated_xsiam_tools.py").read_text()
    assert "def start_xql_query" in xsiam_content
    assert "def get_incidents" in xsiam_content
    assert "def update_incident" in xsiam_content
    assert "@server.call_tool()" in xsiam_content

    # Check XSOAR tools
    xsoar_content = (server_dir / "generated_xsoar_tools.py").read_text()
    assert "def save_or_update_script" in xsoar_content
    assert "def get_automation_scripts" in xsoar_content
    assert "def investigation_add_entry_handler" in xsoar_content
    assert "@server.call_tool()" in xsoar_content


def test_snake_case_naming():
    """Test that generated functions use snake_case."""
    server_dir = Path(__file__).parent.parent / "server"

    xsiam_content = (server_dir / "generated_xsiam_tools.py").read_text()

    # Verify snake_case is used (not camelCase)
    assert "start_xql_query" in xsiam_content
    assert "get_incidents" in xsiam_content
    # Should not have camelCase versions
    assert "postStartXqlQuery" not in xsiam_content
    assert "postGetIncidents" not in xsiam_content
    # Should not have post_ prefix anymore (that's the whole point of this fix)
    assert "post_start_xql_query" not in xsiam_content
    assert "post_get_incidents" not in xsiam_content
    # Check header parameter conversion
    assert "x_xdr_auth_id" in xsiam_content  # Converted from x-xdr-auth-id
