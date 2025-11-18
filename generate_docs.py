#!/usr/bin/env python3
"""
Generate user-facing documentation for all MCP tools.
Organizes tools by category into markdown files in the docs/ directory.
Supports registry-based tools and unified tools.
"""

import re
import ast
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import defaultdict


def extract_tool_info_from_registry(filepath: Path) -> List[Dict[str, Any]]:
    """Extract tool information from registry-based generated file."""
    content = filepath.read_text()
    
    tools = []
    
    # Extract TOOL_DESCRIPTIONS dictionary
    desc_pattern = r'TOOL_DESCRIPTIONS\[([^\]]+)\]\s*=\s*([^\n]+)'
    descriptions = {}
    for match in re.finditer(desc_pattern, content):
        tool_name = match.group(1).strip('"\'')
        desc = match.group(2).strip('"\'')
        descriptions[tool_name] = desc
    
    # Extract TOOL_SCHEMAS to identify unified tools
    schema_pattern = r'TOOL_SCHEMAS\[([^\]]+)\]\s*=\s*([A-Z_]+_INPUT_SCHEMA)'
    schemas = {}
    for match in re.finditer(schema_pattern, content):
        tool_name = match.group(1).strip('"\'')
        schema_type = match.group(2)
        schemas[tool_name] = schema_type
    
    # Get all tool names from TOOL_HANDLERS
    handler_pattern = r'TOOL_HANDLERS\[([^\]]+)\]\s*=\s*'
    for match in re.finditer(handler_pattern, content):
        tool_name = match.group(1).strip('"\'')
        description = descriptions.get(tool_name, "No description available")
        is_unified = schemas.get(tool_name) == "UNIFIED_INPUT_SCHEMA"
        
        # Extract parameters from schema
        params = []
        if is_unified:
            params.append("platform (str): Platform to use - 'xsoar' or 'xsiam' (required for unified tools)")
        params.append("path (Dict[str, Any]): Path parameters (optional)")
        params.append("query (Dict[str, Any]): Query parameters (optional)")
        params.append("headers (Dict[str, Any]): HTTP headers (optional)")
        params.append("body (Any): Request body (optional)")
        
        tools.append({
            'name': tool_name,
            'params': ', '.join(params),
            'description': description,
            'args': '\n'.join(f"- {p}" for p in params),
            'returns': 'List[types.TextContent]: API response',
            'is_unified': is_unified
        })
    
    return tools


def categorize_xsiam_tools(tools: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Categorize XSIAM tools by functionality."""
    categories = defaultdict(list)
    
    for tool in tools:
        name = tool['name'].lower()
        
        # Categorize based on tool name
        if 'xql' in name or ('query' in name and 'xql' in tool['description'].lower()):
            category = 'XQL Queries'
        elif 'incident' in name:
            category = 'Incidents'
        elif 'alert' in name:
            category = 'Alerts'
        elif 'endpoint' in name or 'agent' in name:
            category = 'Endpoints'
        elif any(x in name for x in ['host', 'user', 'ip_address', 'ad_group', 'ou_']):
            category = 'Assets & Identity'
        elif 'violation' in name or 'policy' in name:
            category = 'Policy & Compliance'
        elif 'scan' in name or 'isolate' in name or 'unisolate' in name or 'quarantine' in name or 'restore' in name:
            category = 'Response Actions'
        elif 'hash' in name or 'reputation' in name or 'ioc' in name or 'indicator' in name or 'bioc' in name:
            category = 'Threat Intelligence'
        elif 'audit' in name or 'rbac' in name or 'role' in name or 'healthcheck' in name:
            category = 'Administration'
        elif 'playbook' in name:
            category = 'Playbooks'
        elif 'dashboard' in name:
            category = 'Dashboards'
        elif 'script' in name:
            category = 'Scripts'
        else:
            category = 'Other Operations'
        
        categories[category].append(tool)
    
    return dict(categories)


def categorize_xsoar_tools(tools: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Categorize XSOAR tools by functionality."""
    categories = defaultdict(list)
    
    for tool in tools:
        name = tool['name'].lower()
        
        # Categorize based on tool name
        if 'script' in name or 'automation' in name:
            category = 'Automations & Scripts'
        elif 'incident' in name or 'investigation' in name:
            category = 'Incidents & Investigations'
        elif 'playbook' in name:
            category = 'Playbooks'
        elif 'indicator' in name or 'ioc' in name:
            category = 'Indicators'
        elif 'integration' in name:
            category = 'Integrations'
        elif 'entry' in name or 'evidence' in name:
            category = 'Evidence & Entries'
        elif 'user' in name or 'role' in name or 'api_key' in name:
            category = 'User Management'
        elif 'classifier' in name or 'mapper' in name or 'layout' in name or 'content' in name:
            category = 'Content Management'
        elif 'widget' in name or 'dashboard' in name:
            category = 'Dashboards & Widgets'
        elif 'list' in name and 'get_list' in name:
            category = 'Lists'
        else:
            category = 'Other Operations'
        
        categories[category].append(tool)
    
    return dict(categories)


def categorize_unified_tools(tools: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Categorize unified tools."""
    categories = defaultdict(list)
    
    for tool in tools:
        name = tool['name'].lower()
        
        if 'incident' in name:
            category = 'Incidents'
        elif 'script' in name or 'automation' in name:
            category = 'Automations & Scripts'
        elif 'audit' in name:
            category = 'Logs & Audits'
        else:
            category = 'Unified Operations'
        
        categories[category].append(tool)
    
    return dict(categories)


def generate_tool_doc(tool: Dict[str, Any]) -> str:
    """Generate markdown documentation for a single tool."""
    doc = f"### `{tool['name']}`\n\n"
    
    if tool.get('is_unified'):
        doc += "**Unified Tool** - Works with both XSOAR and XSIAM platforms\n\n"
    
    doc += f"{tool['description']}\n\n"
    
    if tool['args'] and tool['args'] != 'No parameters required':
        doc += "**Parameters:**\n\n"
        for arg_line in tool['args'].split('\n'):
            if arg_line.strip():
                doc += f"{arg_line.strip()}\n"
        doc += "\n"
    else:
        doc += "**Parameters:** None\n\n"
    
    if tool['returns']:
        doc += f"**Returns:** {tool['returns']}\n\n"
    
    return doc


def generate_category_doc(category: str, tools: List[Dict[str, Any]], prefix: str) -> str:
    """Generate documentation for a category of tools."""
    doc = f"# {category}\n\n"
    doc += f"This section documents {len(tools)} {prefix.upper()} tools related to {category.lower()}.\n\n"
    doc += "---\n\n"
    
    # Sort tools alphabetically
    sorted_tools = sorted(tools, key=lambda t: t['name'])
    
    for tool in sorted_tools:
        doc += generate_tool_doc(tool)
        doc += "---\n\n"
    
    return doc


def generate_index(xsiam_categories: Dict, xsoar_categories: Dict, unified_categories: Dict) -> str:
    """Generate main index documentation."""
    total_xsiam = sum(len(tools) for tools in xsiam_categories.values())
    total_xsoar = sum(len(tools) for tools in xsoar_categories.values())
    total_unified = sum(len(tools) for tools in unified_categories.values())
    total = total_xsiam + total_xsoar + total_unified
    
    doc = "# Cortex MCP Tools Documentation\n\n"
    doc += "This documentation provides detailed information about all available MCP tools for XSIAM and XSOAR.\n\n"
    doc += f"**Total Tools:** {total}\n\n"
    doc += f"- **Unified Tools:** {total_unified} (work with both platforms)\n"
    doc += f"- **XSIAM Tools:** {total_xsiam}\n"
    doc += f"- **XSOAR Tools:** {total_xsoar}\n\n"
    
    doc += "## 📚 Documentation Structure\n\n"
    doc += "Tools are organized by platform and functionality:\n\n"
    
    if unified_categories:
        doc += "### Unified Tools\n\n"
        doc += "These tools work with both XSOAR and XSIAM platforms. Use the `platform` parameter to specify which platform to use.\n\n"
        for category in sorted(unified_categories.keys()):
            tools = unified_categories[category]
            filename = category.lower().replace(' ', '-').replace('&', 'and')
            doc += f"- **[{category}](unified/{filename}.md)** ({len(tools)} tools)\n"
        doc += "\n"
    
    doc += "### XSIAM Tools\n\n"
    for category in sorted(xsiam_categories.keys()):
        tools = xsiam_categories[category]
        filename = category.lower().replace(' ', '-').replace('&', 'and')
        doc += f"- **[{category}](xsiam/{filename}.md)** ({len(tools)} tools)\n"
    
    doc += "\n### XSOAR Tools\n\n"
    for category in sorted(xsoar_categories.keys()):
        tools = xsoar_categories[category]
        filename = category.lower().replace(' ', '-').replace('&', 'and')
        doc += f"- **[{category}](xsoar/{filename}.md)** ({len(tools)} tools)\n"
    
    doc += "\n## 🚀 Quick Start\n\n"
    doc += "Each tool page includes:\n"
    doc += "- **Description**: What the tool does\n"
    doc += "- **Parameters**: What the tool expects (required/optional)\n"
    doc += "- **Returns**: What the tool returns\n\n"
    
    doc += "## 📖 Using the Tools\n\n"
    doc += "All tools follow the MCP (Model Context Protocol) standard. "
    doc += "They are designed to be used with AI-powered IDEs like Windsurf, Cursor, and Roo Code.\n\n"
    doc += "**Unified Tools**: Tools marked as 'Unified Tool' accept a `platform` parameter ('xsoar' or 'xsiam') "
    doc += "to work with either platform. These tools automatically route to the correct API endpoint based on the platform.\n\n"
    doc += "For setup instructions and examples, see:\n"
    doc += "- [README.md](../README.md) - Setup and configuration\n"
    doc += "- [EXAMPLES.md](../EXAMPLES.md) - Usage examples and workflows\n"
    
    return doc


def main():
    """Generate all documentation."""
    # Create docs structure
    docs_dir = Path('docs')
    docs_dir.mkdir(exist_ok=True)
    
    xsiam_dir = docs_dir / 'xsiam'
    xsoar_dir = docs_dir / 'xsoar'
    unified_dir = docs_dir / 'unified'
    xsiam_dir.mkdir(exist_ok=True)
    xsoar_dir.mkdir(exist_ok=True)
    unified_dir.mkdir(exist_ok=True)
    
    # Extract tool information
    print("Extracting tool information...")
    xsiam_tools = extract_tool_info_from_registry(Path('server/generated_xsiam_tools.py'))
    xsoar_tools = extract_tool_info_from_registry(Path('server/generated_xsoar_tools.py'))
    unified_tools = []
    
    unified_file = Path('server/generated_unified_tools.py')
    if unified_file.exists():
        unified_tools = extract_tool_info_from_registry(unified_file)
    
    print(f"Found {len(xsiam_tools)} XSIAM tools")
    print(f"Found {len(xsoar_tools)} XSOAR tools")
    print(f"Found {len(unified_tools)} unified tools")
    
    # Categorize tools
    print("\nCategorizing tools...")
    xsiam_categories = categorize_xsiam_tools(xsiam_tools)
    xsoar_categories = categorize_xsoar_tools(xsoar_tools)
    unified_categories = categorize_unified_tools(unified_tools) if unified_tools else {}
    
    print(f"\nUnified categories: {len(unified_categories)}")
    for cat, tools in sorted(unified_categories.items()):
        print(f"  - {cat}: {len(tools)} tools")
    
    print(f"\nXSIAM categories: {len(xsiam_categories)}")
    for cat, tools in sorted(xsiam_categories.items()):
        print(f"  - {cat}: {len(tools)} tools")
    
    print(f"\nXSOAR categories: {len(xsoar_categories)}")
    for cat, tools in sorted(xsoar_categories.items()):
        print(f"  - {cat}: {len(tools)} tools")
    
    # Generate documentation files
    print("\nGenerating documentation files...")
    
    # Generate unified docs
    for category, tools in unified_categories.items():
        filename = category.lower().replace(' ', '-').replace('&', 'and')
        filepath = unified_dir / f'{filename}.md'
        content = generate_category_doc(category, tools, 'unified')
        filepath.write_text(content)
        print(f"  Created {filepath}")
    
    # Generate XSIAM docs
    for category, tools in xsiam_categories.items():
        filename = category.lower().replace(' ', '-').replace('&', 'and')
        filepath = xsiam_dir / f'{filename}.md'
        content = generate_category_doc(category, tools, 'xsiam')
        filepath.write_text(content)
        print(f"  Created {filepath}")
    
    # Generate XSOAR docs
    for category, tools in xsoar_categories.items():
        filename = category.lower().replace(' ', '-').replace('&', 'and')
        filepath = xsoar_dir / f'{filename}.md'
        content = generate_category_doc(category, tools, 'xsoar')
        filepath.write_text(content)
        print(f"  Created {filepath}")
    
    # Generate index
    index_content = generate_index(xsiam_categories, xsoar_categories, unified_categories)
    index_path = docs_dir / 'README.md'
    index_path.write_text(index_content)
    print(f"\n  Created {index_path}")
    
    print("\n✅ Documentation generation complete!")


if __name__ == '__main__':
    main()
