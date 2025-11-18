#!/usr/bin/env python3
"""
MCP Server (static) for XSIAM/XSOAR using registry-based generated tools.
"""

from __future__ import annotations

import asyncio
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List

from mcp import types
from mcp.server import Server
from mcp.server.lowlevel.helper_types import ReadResourceContents
from mcp.server.stdio import stdio_server
from pydantic import AnyUrl

from . import generated_xsiam_tools as xsiam
from . import generated_xsoar_tools as xsoar

try:
    from . import generated_unified_tools as unified
except ImportError:
    unified = None


def _log(event: str, **kwargs: Any) -> None:
    # Logging disabled to avoid interfering with MCP protocol (stderr is used for protocol messages)
    # Enable via environment variable if needed: CORTEXSYNAPSE_ENABLE_LOGGING=1
    if os.getenv("CORTEXSYNAPSE_ENABLE_LOGGING", "").lower() in ("1", "true", "yes"):
        try:
            payload = {"event": event, **kwargs}
            print(json.dumps(payload), file=sys.stderr, flush=True)
        except Exception:
            # Best-effort logging
            pass


def _merge_registries() -> tuple[Dict[str, Any], Dict[str, Any], Dict[str, str]]:
    handlers: Dict[str, Any] = {}
    schemas: Dict[str, Any] = {}
    descs: Dict[str, str] = {}

    modules = [xsiam, xsoar]
    if unified:
        modules.append(unified)

    for mod in modules:
        handlers.update(mod.TOOL_HANDLERS)
        schemas.update(mod.TOOL_SCHEMAS)
        descs.update(mod.TOOL_DESCRIPTIONS)

    return handlers, schemas, descs


async def run_server() -> None:
    server = Server("cortexsynapse")

    TOOL_HANDLERS, TOOL_SCHEMAS, TOOL_DESCRIPTIONS = _merge_registries()
    _log("server_start", tools_count=len(TOOL_HANDLERS))

    @server.list_tools()
    async def list_tools_handler() -> List[types.Tool]:
        tools: List[types.Tool] = []
        for name in sorted(TOOL_HANDLERS.keys()):
            tools.append(
                types.Tool(
                    name=name,
                    description=TOOL_DESCRIPTIONS.get(name),
                    inputSchema=TOOL_SCHEMAS.get(name) or {"type": "object", "properties": {}},
                )
            )
        _log("list_tools", count=len(tools))
        return tools

    @server.call_tool()
    async def call_tool_handler(tool_name: str, arguments: Dict[str, Any]):
        _log("call_tool", name=tool_name)
        handler = TOOL_HANDLERS.get(tool_name)
        if not handler:
            return [
                types.TextContent(type="text", text=f"Unknown tool: {tool_name}"),
            ]
        try:
            return await handler(arguments or {})
        except Exception as exc:
            _log("tool_error", name=tool_name, error=str(exc))
            return [types.TextContent(type="text", text=f"ERROR: {exc}")]

    # Resources: expose docs markdown
    DOCS: Dict[str, Path] = {}
    docs_root = Path(__file__).parent.parent / "docs"
    if docs_root.exists():
        for md in docs_root.rglob("*.md"):
            uri = f"cortexsynapse-docs://{md.relative_to(docs_root).as_posix()}"
            DOCS[uri] = md
    _log("resources_ready", resources_count=len(DOCS))

    @server.list_resources()
    async def list_resources_handler() -> List[types.Resource]:
        resources: List[types.Resource] = []
        for uri, path in sorted(DOCS.items()):
            size = path.stat().st_size if path.exists() else None
            resources.append(types.Resource(uri=uri, description=path.name, mimeType="text/markdown", size=size))
        return resources

    @server.read_resource()
    async def read_resource_handler(uri: AnyUrl | str) -> Iterable[ReadResourceContents]:
        path = DOCS.get(str(uri))
        if not path:
            raise ValueError(f"Unknown resource: {uri}")
        text = path.read_text(encoding="utf-8")
        return [ReadResourceContents(content=text, mime_type="text/markdown")]

    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def main() -> None:
    asyncio.run(run_server())


if __name__ == "__main__":
    main()
