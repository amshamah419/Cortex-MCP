# Cortex-MCP

An MCP (Model Context Protocol) server that auto-generates tools from OpenAPI specifications for XSIAM/XSOAR APIs.

## Overview

This project provides a Python MCP server that dynamically generates tools from OpenAPI specifications. Instead of manually defining tools, you simply add OpenAPI spec files to the `specs/` directory, run the code generator, and the tools are automatically created with proper snake_case naming conventions.

## Features

- **Auto-generation**: Reads `specs/*.yaml` and generates `server/generated_*_tools.py` files
- **Snake_case naming**: Automatically converts camelCase operation IDs to snake_case tool names
- **No runtime overhead**: Tools are pre-generated, not loaded at runtime from Swagger
- **Type hints**: Generated code includes proper Python type hints
- **Docker support**: Containerized deployment with multi-stage builds
- **CI/CD**: GitHub Actions workflow for automated testing, formatting, and deployment

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

## Installation

### Local Development

1. Clone the repository:
```bash
git clone https://github.com/amshamah419/Cortex-MCP.git
cd Cortex-MCP
```

2. Install dependencies:
```bash
pip install -e ".[dev]"
```

3. Generate tools from OpenAPI specs:
```bash
python -m codegen.generator
```

4. Run the server:
```bash
python -m server.main
```

### Docker

Build and run using Docker:

```bash
# Build the image
docker build -t cortex-mcp .

# Run the container
docker run -i cortex-mcp
```

## Usage

### Adding New API Specifications

1. Add your OpenAPI specification to the `specs/` directory:
```bash
cp your-api-spec.yaml specs/
```

2. Regenerate the tools:
```bash
python -m codegen.generator
```

3. The generator will create `server/generated_your-api-spec_tools.py` with all tools

### Tool Naming Convention

The generator automatically converts OpenAPI operation IDs to snake_case:

- `listIncidents` → `list_incidents`
- `createIncident` → `create_incident`  
- `executePlaybook` → `execute_playbook`
- `searchIndicators` → `search_indicators`

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

## Development

### Running Tests

```bash
pytest tests/ -v
```

### Code Formatting

```bash
black codegen/ server/ tests/
```

### Linting

```bash
ruff check codegen/ server/ tests/
```

### Type Checking

```bash
mypy codegen/ server/
```

## CI/CD Pipeline

The GitHub Actions workflow automatically:

1. **Generates tools** from OpenAPI specs
2. **Formats code** with Black
3. **Lints code** with Ruff
4. **Runs tests** with pytest
5. **Commits generated tools** (on main branch)
6. **Builds and pushes Docker image** to GitHub Container Registry

The workflow runs on:
- Push to `main` branch
- Pull requests
- Manual trigger via workflow_dispatch

## API Specifications

### XSIAM

The XSIAM spec (`specs/xsiam.yaml`) includes tools for:
- `list_incidents`: List security incidents
- `create_incident`: Create a new incident
- `get_incident`: Get incident details
- `update_incident`: Update an incident
- `list_alerts`: List security alerts

### XSOAR

The XSOAR spec (`specs/xsoar.yaml`) includes tools for:
- `list_playbooks`: List available playbooks
- `execute_playbook`: Execute a playbook
- `list_investigations`: List investigations
- `create_investigation`: Create a new investigation
- `search_indicators`: Search for IOCs

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add or modify OpenAPI specs in `specs/`
4. Run the generator to create tools
5. Add tests for new functionality
6. Submit a pull request

## License

MIT License - see LICENSE file for details

## Architecture

### Code Generation Flow

```
specs/*.yaml → codegen/generator.py → server/generated_*_tools.py → server/main.py
```

1. OpenAPI specs define the API operations
2. Generator parses specs and creates Python functions
3. Server dynamically imports generated modules
4. Tools are registered with the MCP server

### No Runtime Swagger

Unlike some MCP servers that load Swagger/OpenAPI specs at runtime, this project pre-generates all tools. This approach:

- Eliminates runtime parsing overhead
- Provides better type safety
- Enables IDE autocomplete
- Simplifies debugging
- Allows code review of generated tools

## Requirements

- Python 3.10+
- Dependencies listed in `pyproject.toml`
- Docker (optional, for containerized deployment)

## Troubleshooting

### No generated tools found

If you see "Warning: No generated tool files found", run:
```bash
python -m codegen.generator
```

### Import errors

Ensure all dependencies are installed:
```bash
pip install -e ".[dev]"
```

### Docker build fails

Check that all files are present:
```bash
ls -la specs/ codegen/ server/
```

## Support

For issues and questions:
- Open an issue on GitHub
- Check existing issues for solutions
- Review the code generation output in `server/generated_*_tools.py`