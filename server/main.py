#!/usr/bin/env python3
"""
MCP Server for XSIAM/XSOAR with auto-generated tools from OpenAPI specs.
This server dynamically loads generated tool modules.
"""

import asyncio
import importlib.util
import sys
from pathlib import Path

from mcp.server import Server
from mcp.server.stdio import stdio_server


def load_generated_tools(server: Server) -> None:
    """Load all generated tool modules."""
    server_dir = Path(__file__).parent
    tool_files = list(server_dir.glob("generated_*_tools.py"))

    if not tool_files:
        print("Warning: No generated tool files found. Run codegen/generator.py first.")
        return

    for tool_file in tool_files:
        module_name = tool_file.stem
        try:
            # Import the module
            spec = importlib.util.spec_from_file_location(module_name, tool_file)
            if spec and spec.loader:
                module = importlib.util.module_from_spec(spec)
                sys.modules[module_name] = module
                spec.loader.exec_module(module)

                # Set the server instance in the module
                if hasattr(module, "set_server"):
                    module.set_server(server)
                    print(f"Loaded tools from {module_name}")
        except Exception as e:
            print(f"Error loading {module_name}: {e}")


async def run_server() -> None:
    """Run the MCP server."""
    server = Server("cortex-mcp")

    # Load all generated tools
    load_generated_tools(server)

    # Run the server using stdio transport
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options(),
        )


def main() -> None:
    """Main entry point."""
    asyncio.run(run_server())


if __name__ == "__main__":
    main()
