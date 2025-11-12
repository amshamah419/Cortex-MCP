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

    # Check XSIAM tools
    xsiam_content = (server_dir / "generated_xsiam_tools.py").read_text()
    assert "def list_incidents" in xsiam_content
    assert "def create_incident" in xsiam_content
    assert "def get_incident" in xsiam_content
    assert "@server.call_tool()" in xsiam_content

    # Check XSOAR tools
    xsoar_content = (server_dir / "generated_xsoar_tools.py").read_text()
    assert "def list_playbooks" in xsoar_content
    assert "def execute_playbook" in xsoar_content
    assert "def list_investigations" in xsoar_content
    assert "@server.call_tool()" in xsoar_content


def test_snake_case_naming():
    """Test that generated functions use snake_case."""
    server_dir = Path(__file__).parent.parent / "server"

    xsiam_content = (server_dir / "generated_xsiam_tools.py").read_text()

    # Verify snake_case is used (not camelCase)
    assert "list_incidents" in xsiam_content
    assert "create_incident" in xsiam_content
    assert "listIncidents" not in xsiam_content  # Should not have camelCase
    assert "createIncident" not in xsiam_content
