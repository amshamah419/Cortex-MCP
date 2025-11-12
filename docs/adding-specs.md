# Adding New API Specifications

This document explains how to add new API specifications to generate MCP tools.

## Quick Start

1. **Add your OpenAPI spec** to the `specs/` directory:
   ```bash
   cp my-api.yaml specs/
   ```

2. **Regenerate tools**:
   ```bash
   python -m codegen.generator
   ```

3. **Test the server**:
   ```bash
   python -m server.main
   ```

## OpenAPI Spec Requirements

Your OpenAPI specification should:

- Use OpenAPI 3.0.0 or later
- Include `operationId` for each operation (will be converted to snake_case)
- Define parameters with proper schemas
- Include descriptions for documentation

## Example Minimal Spec

```yaml
openapi: 3.0.0
info:
  title: My API
  version: 1.0.0
servers:
  - url: https://api.example.com/v1
paths:
  /items:
    get:
      operationId: listItems
      summary: List all items
      parameters:
        - name: limit
          in: query
          schema:
            type: integer
      responses:
        '200':
          description: Success
```

This will generate a tool function:

```python
@server.call_tool()
async def list_items(
    limit: int | None = None,
) -> List[types.TextContent]:
    """List all items"""
    # ... implementation
```

## Operation ID Naming

The generator converts operation IDs to snake_case:

| OpenAPI operationId | Generated function name |
|---------------------|-------------------------|
| `listItems`         | `list_items`            |
| `createUser`        | `create_user`           |
| `getAPIKey`         | `get_api_key`           |
| `executeWorkflow`   | `execute_workflow`      |

## Supported Features

- ✅ Query parameters
- ✅ Path parameters  
- ✅ Request bodies (JSON)
- ✅ GET, POST, PUT, PATCH, DELETE methods
- ✅ Type hints (string, integer, boolean, array, object)
- ✅ Optional vs required parameters

## Testing Your New Tools

After generating tools:

1. Run the tests:
   ```bash
   pytest tests/
   ```

2. Start the server:
   ```bash
   python -m server.main
   ```

3. The server will automatically load your new tools!
