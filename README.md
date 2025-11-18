# CortexSynapse

[![CI/CD Pipeline](https://github.com/amshamah419/CortexSynapse/actions/workflows/ci-cd.yml/badge.svg)](https://github.com/amshamah419/CortexSynapse/actions/workflows/ci-cd.yml)
[![CodeQL](https://github.com/amshamah419/CortexSynapse/actions/workflows/ci-cd.yml/badge.svg?job=codeql-analysis)](https://github.com/amshamah419/CortexSynapse/security/code-scanning)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Docker](https://img.shields.io/badge/docker-ghcr.io-blue.svg)](https://github.com/amshamah419/CortexSynapse/pkgs/container/cortexsynapse)

A robust MCP (Model Context Protocol) server that enables AI-powered IDEs and agents to interact with live XSOAR/XSIAM instances for development, testing, and automation tasks.

## Overview

CortexSynapse bridges the gap between AI development tools (Windsurf, Roo Code, Cursor, etc.) and Palo Alto Cortex platforms (XSOAR/XSIAM). It provides a containerized MCP server that exposes XSOAR and XSIAM APIs as tools that AI agents can use to help developers build, test, and verify security automation workflows.

**Primary Use Case**: Enable developers to use natural language with AI assistants to perform common XSOAR/XSIAM development tasks such as:
- Creating and testing playbooks
- Managing integrations and automations
- Querying incidents and alerts
- Running XQL queries for threat hunting
- Building and deploying custom content
- Debugging security workflows

## Why CortexSynapse?

As a developer working with XSOAR and XSIAM, you need to frequently interact with these platforms to build, test, and verify security automation. CortexSynapse allows you to:

- **Use AI assistants for XSOAR/XSIAM development** - Tell your AI IDE to "create a playbook for phishing investigation" or "query recent high-severity incidents"
- **Accelerate development workflows** - Build and test automations faster with AI assistance
- **Streamline common tasks** - Use natural language for routine operations like running queries, updating incidents, or testing integrations
- **Integrate with modern AI IDEs** - Works seamlessly with Windsurf, Roo Code, Cursor, and other MCP-compatible tools

## Key Features

- **213 production-ready tools** - Auto-generated from official XSIAM/XSOAR OpenAPI specifications
  - 128 XSIAM tools (XQL queries, incidents, alerts, endpoints, threat intelligence)
  - 85 XSOAR tools (playbooks, investigations, automations, indicators)
  - **[📚 Full Tool Documentation](docs/README.md)** - Comprehensive documentation for all tools organized by category
- **Containerized deployment** - Docker support for easy integration with AI IDE workflows
- **Live API integration** - Connect to your actual XSOAR/XSIAM instances
- **Type-safe operations** - Full Python type hints for reliable AI agent interactions
- **Extensible architecture** - Add custom tools by providing OpenAPI specifications

## Project Structure

```
.
├── specs/                          # OpenAPI specification files
│   ├── xsiam.yaml                 # XSIAM API specification
│   └── xsoar.yaml                 # XSOAR API specification
├── codegen/                        # Code generation scripts
│   ├── __init__.py
│   └── generator.py               # Main generator script
├── server/                         # MCP server implementation
│   ├── __init__.py
│   ├── main.py                    # Server entry point
│   ├── generated_xsiam_tools.py   # Auto-generated XSIAM tools
│   └── generated_xsoar_tools.py   # Auto-generated XSOAR tools
├── tests/                          # Test suite
│   ├── __init__.py
│   ├── test_codegen.py            # Code generator tests
│   └── test_server.py             # Server tests
├── .github/workflows/              # GitHub Actions
│   └── ci-cd.yml                  # CI/CD pipeline
├── Dockerfile                      # Container definition
├── pyproject.toml                  # Python project configuration
└── README.md                       # This file
```

## Security

🔒 CortexSynapse implements enterprise-grade security controls. See [SECURITY.md](SECURITY.md) for detailed security documentation.

**Key Security Features:**
- ✅ Input validation and sanitization
- ✅ Rate limiting (100 requests/60s default)
- ✅ Error message sanitization to prevent information leakage
- ✅ Non-root Docker container execution
- ✅ Configurable SSL/TLS verification
- ✅ Environment-based credential management (no hardcoded secrets)
- ✅ Security headers on all requests
- ✅ Automated security scanning in CI/CD

## Quick Start

### Using with AI IDEs

1. **Build the Docker container**:
```bash
docker build -t cortexsynapse .
```

2. **Set up environment variables** (recommended for security):
```bash
export XSOAR_API_URL="https://your-xsoar-instance.com"
export XSOAR_API_KEY="your-api-key"
export XSIAM_API_URL="https://your-xsiam-instance.com"
export XSIAM_API_KEY="your-xsiam-api-key"
export XSIAM_API_KEY_ID="your-key-id"
```

3. **Configure your AI IDE** to use the MCP server:

**For Windsurf/Cursor/Roo Code:**
Add to your MCP settings (typically in `.windsurf/mcp.json`, `.cursor/mcp.json`, or IDE settings):
```json
{
  "mcpServers": {
    "cortex": {
      "command": "docker",
      "args": [
        "run", 
        "-i", 
        "--read-only",
        "--security-opt=no-new-privileges",
        "cortexsynapse"
      ],
      "env": {
        "XSOAR_API_URL": "${XSOAR_API_URL}",
        "XSOAR_API_KEY": "${XSOAR_API_KEY}",
        "XSIAM_API_URL": "${XSIAM_API_URL}",
        "XSIAM_API_KEY": "${XSIAM_API_KEY}",
        "XSIAM_API_KEY_ID": "${XSIAM_API_KEY_ID}"
      }
    }
  }
}
```

**⚠️ Security Note:** Use environment variable references (`${VAR_NAME}`) instead of hardcoding credentials.

4. **Start using AI assistance** for XSOAR/XSIAM development:
   - "Query all high-severity incidents from the last 24 hours"
   - "Create a new playbook for ransomware response"
   - "Run an XQL query to find suspicious login attempts"
   - "Update incident #12345 to closed status"

### Local Development

For development and testing without Docker:

```bash
# Clone and install
git clone https://github.com/amshamah419/Cortex-MCP.git
cd Cortex-MCP
pip install -e ".[dev]"

# Generate tools from OpenAPI specs (already generated by default)
python -m codegen.generator

# Run the MCP server
python -m server.main
```

## Available Tools

All 70 tools are thoroughly documented with descriptions, parameters, and return values.

**📚 [View Complete Tool Documentation](docs/README.md)**

### Unified Tools (7 tools)

These tools work with both XSOAR and XSIAM platforms. Use the `platform` parameter to specify which platform to use:
- **Incidents**: get, update
- **Automations/Scripts**: get, create/update, import, delete
- **Logs**: get audits

### XSIAM Tools (39 tools)

Organized into categories:
- **[XQL Queries](docs/xsiam/xql-queries.md)** (12 tools) - Execute and manage XQL queries for threat hunting
- **[Incidents](docs/xsiam/incidents.md)** (3 tools) - Query, update, and manage security incidents
- **[Alerts](docs/xsiam/alerts.md)** (8 tools) - Retrieve and manage security alerts
- **[Endpoints](docs/xsiam/endpoints.md)** (7 tools) - Query and manage endpoint information
- **[Response Actions](docs/xsiam/response-actions.md)** (3 tools) - Isolate endpoints and take response actions
- **[Assets & Identity](docs/xsiam/assets-and-identity.md)** (11 tools) - Manage hosts, users, IPs, and AD groups
- **[Threat Intelligence](docs/xsiam/threat-intelligence.md)** (3 tools) - Manage IOCs and reputation data
- **[Policy & Compliance](docs/xsiam/policy-and-compliance.md)** (2 tools) - View policies and violations
- **[Administration](docs/xsiam/administration.md)** (1 tool) - Audit logs and RBAC
- **[Other Operations](docs/xsiam/other-operations.md)** (78 tools) - Additional XSIAM operations

### XSOAR Tools (24 tools)

Organized into categories:
- **[Incidents & Investigations](docs/xsoar/incidents-and-investigations.md)** (17 tools) - Create, update, and manage incidents
- **[Indicators](docs/xsoar/indicators.md)** (12 tools) - Manage threat indicators and IOCs
- **[Dashboards & Widgets](docs/xsoar/dashboards-and-widgets.md)** (11 tools) - Manage dashboards and widgets
- **[Evidence & Entries](docs/xsoar/evidence-and-entries.md)** (6 tools) - Add entries and manage evidence
- **[Automations & Scripts](docs/xsoar/automations-and-scripts.md)** (5 tools) - Create and manage automation scripts
- **[User Management](docs/xsoar/user-management.md)** (2 tools) - Manage API keys and users
- **[Playbooks](docs/xsoar/playbooks.md)** (1 tool) - Manage playbooks
- **[Integrations](docs/xsoar/integrations.md)** (1 tool) - Manage integrations
- **[Content Management](docs/xsoar/content-management.md)** (1 tool) - Import classifiers and mappers
- **[Other Operations](docs/xsoar/other-operations.md)** (29 tools) - Additional XSOAR operations

## Common Development Workflows

### Example 1: Threat Hunting with AI Assistance

**Developer**: "Show me all high-severity incidents from the last week where the source IP is from Russia"

**AI Agent** uses:
1. `xsiam_get_incidents` with filters for severity and date range
2. Parses results and filters by geography
3. Presents findings in natural language

### Example 2: Playbook Development

**Developer**: "Create a test incident to verify my new phishing playbook"

**AI Agent** uses:
1. `xsiam_create_incident` to create a test incident
2. `xsoar_execute_playbook` to run the playbook
3. `xsiam_get_incidents` to verify the outcome

### Example 3: Automation Testing

**Developer**: "Run an XQL query to find failed login attempts and create an incident if there are more than 10"

**AI Agent** uses:
1. `xsiam_start_xql_query` with the appropriate XQL syntax
2. `xsiam_get_query_results` to retrieve results
3. `xsiam_create_incident` if threshold is exceeded

## Extending with Custom Tools

While the server comes with 211 production tools, you can add custom tools by providing additional OpenAPI specifications:

1. Add your OpenAPI spec to `specs/`:
```bash
cp your-custom-api.json specs/
```

2. Regenerate tools:
```bash
python -m codegen.generator
```

3. Rebuild the container:
```bash
docker build -t cortexsynapse .
```

The generator supports both YAML and JSON OpenAPI specifications and automatically converts operation IDs to snake_case function names.

### Example Generated Tool

From an OpenAPI operation:
```yaml
paths:
  /incidents:
    get:
      operationId: listIncidents
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
```

The generator creates:
```python
@server.call_tool()
async def list_incidents(
    limit: int | None = None,
) -> List[types.TextContent]:
    """Retrieve a list of security incidents from XSIAM"""
    # ... implementation
```

## Project Structure

```
.
├── specs/                          # OpenAPI specification files
│   ├── xsiam.json                 # XSIAM API specification (129 endpoints)
│   └── xsoar.json                 # XSOAR API specification (82 endpoints)
├── server/                         # MCP server implementation
│   ├── main.py                    # Server entry point
│   ├── generated_xsiam_tools.py   # Auto-generated XSIAM tools
│   └── generated_xsoar_tools.py   # Auto-generated XSOAR tools
├── codegen/                        # Code generation (for extending tools)
│   └── generator.py               # Tool generator from OpenAPI specs
├── tests/                          # Test suite
├── Dockerfile                      # Container for AI IDE integration
└── pyproject.toml                  # Python dependencies
```

## Architecture

### MCP Server Flow

```
AI IDE/Agent → MCP Protocol → CortexSynapse Server → XSOAR/XSIAM API
     ↑                              ↓
     └──────── Natural Language ←────┘
```

1. Developer asks AI assistant to perform a task
2. AI agent selects appropriate tool(s) from 211 available
3. MCP server executes API calls to live XSOAR/XSIAM instance
4. Results returned to AI agent for processing and presentation

### Code Generation (Optional - For Custom Tools)

For adding custom tools beyond the 211 built-in ones:

```
Custom OpenAPI Spec → generator.py → generated_custom_tools.py → Container Rebuild
```

The default installation includes all XSIAM/XSOAR tools pre-generated, so code generation is only needed when extending the server with custom APIs.

## Technical Details

### Requirements

- Python 3.10+
- Docker (for containerized deployment with AI IDEs)
- Active XSOAR and/or XSIAM instance with API access

### Dependencies

Core runtime dependencies (installed automatically):
- `mcp>=0.1.0` - Model Context Protocol implementation  
- `httpx>=0.25.0` - Async HTTP client for API calls
- `pydantic>=2.0` - Data validation and type hints

Development dependencies (for extending tools):
- `pytest` - Testing framework
- `black` - Code formatting
- `ruff` - Linting

## Troubleshooting

### AI IDE Integration Issues

**MCP server not connecting:**
- Ensure Docker is running
- Check that the container starts successfully: `docker run -i cortexsynapse`
- Verify environment variables are set correctly in your IDE's MCP configuration

**API authentication failures:**
- Confirm your XSOAR/XSIAM API keys are valid
- Check that the API URLs are correct and accessible
- Ensure your API key has appropriate permissions

**Tools not appearing in AI assistant:**
- Restart your AI IDE after updating MCP configuration
- Check IDE logs for MCP connection errors
- Verify the MCP protocol version compatibility

### Development Issues

**No generated tools found:**
```bash
python -m codegen.generator
```

**Import errors:**
```bash
pip install -e ".[dev]"
```

**Docker build fails:**
```bash
# Ensure all required files exist
ls -la specs/ codegen/ server/

# Try building with verbose output
docker build -t cortexsynapse . --progress=plain
```

## Security

Security is a top priority for CortexSynapse. We follow industry best practices to protect your credentials and data.

### Security Features

- **Input Validation**: All inputs are validated and sanitized to prevent injection attacks
- **Rate Limiting**: Protects against API abuse (100 requests/60s default, configurable)
- **Error Sanitization**: Error messages are sanitized to prevent information leakage
- **Secure Credentials**: Environment-based configuration prevents hardcoded secrets
- **Non-Root Execution**: Docker containers run as non-root user for defense in depth
- **SSL/TLS Verification**: Enabled by default with configurable options
- **Security Headers**: All requests include security-focused HTTP headers
- **Automated Scanning**: CI/CD pipeline includes vulnerability and secret scanning

### Security Configuration

Configure security settings via environment variables:

```bash
# Request timeout (default: 30 seconds)
export API_TIMEOUT=30

# SSL/TLS verification (default: true)
export VERIFY_SSL=true

# Rate limiting
export RATE_LIMIT_REQUESTS=100
export RATE_LIMIT_WINDOW=60
```

### Reporting Security Issues

Please report security vulnerabilities responsibly:
- **Do NOT** open public issues for security vulnerabilities
- Contact the repository maintainer directly
- See [SECURITY.md](SECURITY.md) for detailed reporting guidelines

For complete security documentation, see **[SECURITY.md](SECURITY.md)**.

## Contributing

We welcome contributions! This project is focused on enabling AI-assisted XSOAR/XSIAM development.

**Priority areas:**
- Additional tools for common development workflows
- Better error handling and debugging support
- Enhanced integration examples for popular AI IDEs
- Performance optimizations for large-scale deployments
- Security enhancements

**To contribute:**
1. Fork the repository
2. Create a feature branch focused on developer productivity
3. Test with real XSOAR/XSIAM instances
4. Follow security best practices (see SECURITY.md)
5. Submit a pull request with clear use case description

## License

MIT License - see LICENSE file for details

## Support

For questions and issues:
- **GitHub Issues**: Bug reports and feature requests
- **Security Issues**: See [SECURITY.md](SECURITY.md) for reporting guidelines
- **Discussions**: Best practices for AI-assisted XSOAR/XSIAM development
- **Documentation**: Check `docs/` and `EXAMPLES.md` for detailed guides

## Acknowledgments

Built on the Model Context Protocol (MCP) standard for AI-to-tool integration. Designed specifically for Palo Alto Cortex platform developers using modern AI development tools.