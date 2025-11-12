# Multi-stage build for Cortex MCP Server
FROM python:3.11-slim as builder

WORKDIR /app

# Install build dependencies
RUN pip install --no-cache-dir build

# Copy project files
COPY pyproject.toml .
COPY README.md .
COPY server/ server/
COPY codegen/ codegen/
COPY specs/ specs/

# Generate tools from OpenAPI specs
RUN pip install --no-cache-dir pyyaml && \
    python -m codegen.generator

# Build the package
RUN python -m build

# Runtime stage
FROM python:3.11-slim

WORKDIR /app

# Copy the wheel from builder
COPY --from=builder /app/dist/*.whl /tmp/

# Install the package
RUN pip install --no-cache-dir /tmp/*.whl && \
    rm -rf /tmp/*.whl

# Copy server code and generated tools
COPY --from=builder /app/server/ /app/server/

# Run the server
CMD ["python", "-m", "server.main"]
