"""Tests for the MCP server."""

from pathlib import Path

from server import generated_xsiam_tools as xsiam
from server import generated_xsoar_tools as xsoar
from server import main as server_main


def test_generated_files_exist():
    """Generated registry files should exist."""
    server_dir = Path(__file__).parent.parent / "server"
    assert (server_dir / "generated_xsiam_tools.py").exists()
    assert (server_dir / "generated_xsoar_tools.py").exists()


def test_registries_non_empty():
    """Generated registries should not be empty."""
    assert xsiam.TOOL_HANDLERS and xsiam.TOOL_SCHEMAS
    assert xsoar.TOOL_HANDLERS and xsoar.TOOL_SCHEMAS


def test_server_merges_registries():
    """Server merge should expose combined tool count."""
    handlers, schemas, descs = server_main._merge_registries()
    assert len(handlers) > 0
    assert set(handlers.keys()) == set(schemas.keys()) == set(descs.keys())
