"""Tests for the current code generator implementation."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
from types import ModuleType

import pytest

from codegen.generator import (
    COMMON_INPUT_SCHEMA,
    UNIFIED_INPUT_SCHEMA,
    find_operation_in_spec,
    generate_platform_tools_file,
    generate_unified_tools_file,
    load_whitelist,
    to_snake_case,
)


def _load_module(path: Path) -> ModuleType:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    assert spec.loader  # for mypy
    spec.loader.exec_module(module)
    return module


def test_to_snake_case_handles_mixed_names():
    """Ensure camelCase and symbols are normalized."""
    assert to_snake_case("ListIncidents") == "list_incidents"
    assert to_snake_case("create-Widget/Item") == "create_widget_item"
    assert to_snake_case("HTTPResponse2XX") == "http_response2_xx"


def test_find_operation_in_spec_matches_route_and_method():
    """find_operation_in_spec should locate the correct route/method pair."""
    spec = {
        "paths": {
            "/items": {
                "get": {"operationId": "listItems", "summary": "List", "description": "List items"}
            }
        }
    }

    op = find_operation_in_spec(spec, "/items", "GET")
    assert op is not None
    assert op["operationId"] == "listItems"
    assert op["method"] == "GET"


def test_find_operation_in_spec_returns_none_for_missing_route():
    """Non-existent paths should return None."""
    spec = {"paths": {"/items": {"get": {"operationId": "listItems"}}}}
    assert find_operation_in_spec(spec, "/missing", "GET") is None


def test_generate_platform_tools_file_builds_registry(tmp_path: Path):
    """Platform-specific generator should emit MCP registry files."""
    spec = {
        "openapi": "3.0.0",
        "paths": {
            "/items": {
                "get": {
                    "operationId": "listItems",
                    "summary": "List items",
                    "description": "Return all items",
                }
            }
        },
    }

    spec_path = tmp_path / "spec.json"
    spec_path.write_text(json.dumps(spec))
    output_dir = tmp_path / "out"
    output_dir.mkdir()

    whitelist = {
        "xsiam": {
            "list_items": {
                "route": "/items",
                "method": "GET",
                "operationId": "listItems",
                "description": "Return all items",
            }
        }
    }

    generate_platform_tools_file(spec_path, output_dir, whitelist, "xsiam")
    generated_path = output_dir / "generated_xsiam_tools.py"
    assert generated_path.exists()

    module = _load_module(generated_path)
    tool_name = "xsiam_list_items"
    assert tool_name in module.TOOL_HANDLERS
    assert module.TOOL_SCHEMAS[tool_name] == COMMON_INPUT_SCHEMA
    assert module.TOOL_DESCRIPTIONS[tool_name] == "Return all items"


def test_generate_unified_tools_file_builds_registry(tmp_path: Path):
    """Unified generator should create platform-aware handlers."""
    whitelist = {
        "unified": {
            "get_incidents": {
                "description": "Fetch incidents from a platform",
                "xsoar": {"route": "/incidents/search", "method": "POST"},
                "xsiam": {"route": "/public_api/v1/incidents/get_incidents", "method": "POST"},
            }
        }
    }

    output_dir = tmp_path / "out"
    output_dir.mkdir()

    generate_unified_tools_file(whitelist, {}, {}, output_dir)
    generated_path = output_dir / "generated_unified_tools.py"
    assert generated_path.exists()

    module = _load_module(generated_path)
    tool_name = "get_incidents"
    assert tool_name in module.TOOL_HANDLERS
    assert module.TOOL_SCHEMAS[tool_name] == UNIFIED_INPUT_SCHEMA
    assert module.TOOL_DESCRIPTIONS[tool_name] == "Fetch incidents from a platform"


def test_load_whitelist_reads_json(tmp_path: Path):
    """Whitelist loader should parse JSON config."""
    whitelist_path = tmp_path / "whitelist.json"
    data = {"xsoar": {"tool": {"route": "/test", "method": "GET"}}}
    whitelist_path.write_text(json.dumps(data))

    loaded = load_whitelist(whitelist_path)
    assert loaded == data
