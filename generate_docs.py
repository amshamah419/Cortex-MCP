#!/usr/bin/env python3
"""
Generate user-facing documentation for all MCP tools.
Organizes tools by category into markdown files in the docs/ directory.
"""

import re
from pathlib import Path
from typing import Dict, List, Any
from collections import defaultdict


def extract_tool_info(filepath: Path, prefix: str) -> List[Dict[str, Any]]:
    """Extract tool information from generated file."""
    content = filepath.read_text()
    
    # Pattern to match function definitions and their docstrings
    pattern = (
        r'@server\.call_tool\(\)\s+'
        r'async def (' + prefix + r'_\w+)\((.*?)\) -> List\[types\.TextContent\]:\s+'
        r'"""(.*?)"""'
    )
    
    tools = []
    for match in re.finditer(pattern, content, re.DOTALL):
        name = match.group(1)
        params = match.group(2)
        docstring = match.group(3)
        
        # Parse docstring sections
        sections = parse_docstring(docstring)
        
        tools.append({
            'name': name,
            'params': params,
            'description': sections['description'],
            'args': sections['args'],
            'returns': sections['returns'],
        })
    
    return tools


def parse_docstring(docstring: str) -> Dict[str, str]:
    """Parse docstring into sections."""
    lines = docstring.split('\n')
    
    description_lines = []
    args_lines = []
    returns_lines = []
    
    current_section = 'description'
    
    for line in lines:
        line = line.strip()
        
        if line.startswith('Args:'):
            current_section = 'args'
            continue
        elif line.startswith('Returns:'):
            current_section = 'returns'
            continue
        
        if current_section == 'description' and line:
            description_lines.append(line)
        elif current_section == 'args' and line:
            args_lines.append(line)
        elif current_section == 'returns' and line:
            returns_lines.append(line)
    
    return {
        'description': ' '.join(description_lines),
        'args': '\n'.join(args_lines),
        'returns': '\n'.join(returns_lines),
    }


def categorize_xsiam_tools(tools: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
    """Categorize XSIAM tools by functionality."""
    categories = defaultdict(list)
    
    for tool in tools:
        name = tool['name'].lower()
        
        # Categorize based on tool name
        if 'xql' in name or 'query' in name and 'xql' in tool['description'].lower():
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
        elif 'scan' in name or 'isolate' in name or 'unisolate' in name:
            category = 'Response Actions'
        elif 'hash' in name or 'reputation' in name or 'ioc' in name:
            category = 'Threat Intelligence'
        elif 'audit' in name or 'rbac' in name or 'role' in name:
            category = 'Administration'
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
        elif 'classifier' in name or 'mapper' in name or 'layout' in name:
            category = 'Content Management'
        elif 'widget' in name or 'dashboard' in name:
            category = 'Dashboards & Widgets'
        elif 'list' in name and 'get_list' in name:
            category = 'Lists'
        else:
            category = 'Other Operations'
        
        categories[category].append(tool)
    
    return dict(categories)


def generate_tool_doc(tool: Dict[str, Any]) -> str:
    """Generate markdown documentation for a single tool."""
    doc = f"### `{tool['name']}`\n\n"
    doc += f"{tool['description']}\n\n"
    
    if tool['args'] and tool['args'] != 'No parameters required':
        doc += "**Parameters:**\n\n"
        for arg_line in tool['args'].split('\n'):
            if arg_line.strip():
                doc += f"- {arg_line.strip()}\n"
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


def generate_index(xsiam_categories: Dict, xsoar_categories: Dict) -> str:
    """Generate main index documentation."""
    doc = "# Cortex MCP Tools Documentation\n\n"
    doc += "This documentation provides detailed information about all available MCP tools for XSIAM and XSOAR.\n\n"
    doc += f"**Total Tools:** {sum(len(tools) for tools in xsiam_categories.values()) + sum(len(tools) for tools in xsoar_categories.values())}\n\n"
    
    doc += "## 📚 Documentation Structure\n\n"
    doc += "Tools are organized by platform and functionality:\n\n"
    
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
    xsiam_dir.mkdir(exist_ok=True)
    xsoar_dir.mkdir(exist_ok=True)
    
    # Extract tool information
    print("Extracting tool information...")
    xsiam_tools = extract_tool_info(Path('server/generated_xsiam_tools.py'), 'xsiam')
    xsoar_tools = extract_tool_info(Path('server/generated_xsoar_tools.py'), 'xsoar')
    
    print(f"Found {len(xsiam_tools)} XSIAM tools")
    print(f"Found {len(xsoar_tools)} XSOAR tools")
    
    # Categorize tools
    print("\nCategorizing tools...")
    xsiam_categories = categorize_xsiam_tools(xsiam_tools)
    xsoar_categories = categorize_xsoar_tools(xsoar_tools)
    
    print(f"\nXSIAM categories: {len(xsiam_categories)}")
    for cat, tools in sorted(xsiam_categories.items()):
        print(f"  - {cat}: {len(tools)} tools")
    
    print(f"\nXSOAR categories: {len(xsoar_categories)}")
    for cat, tools in sorted(xsoar_categories.items()):
        print(f"  - {cat}: {len(tools)} tools")
    
    # Generate documentation files
    print("\nGenerating documentation files...")
    
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
    index_content = generate_index(xsiam_categories, xsoar_categories)
    index_path = docs_dir / 'README.md'
    index_path.write_text(index_content)
    print(f"\n  Created {index_path}")
    
    print("\n✅ Documentation generation complete!")


if __name__ == '__main__':
    main()
