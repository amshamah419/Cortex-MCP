# Security Policy

## Overview

Cortex-MCP takes security seriously. This document outlines our security practices, how to report vulnerabilities, and security guidelines for users.

## Supported Versions

We provide security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Security Features

### 1. Input Validation & Sanitization

All user inputs are validated and sanitized to prevent injection attacks:
- Length limits enforced (max 10,000 characters)
- Special characters filtered
- Script injection patterns detected and blocked

### 2. Rate Limiting

Built-in rate limiting protects against API abuse:
- Default: 100 requests per 60 seconds
- Configurable via environment variables:
  - `RATE_LIMIT_REQUESTS`: Maximum requests (default: 100)
  - `RATE_LIMIT_WINDOW`: Time window in seconds (default: 60)

### 3. Error Message Sanitization

Error messages are sanitized to prevent information leakage:
- API keys redacted
- Tokens redacted
- Passwords redacted
- File paths obscured

### 4. Secure HTTP Client Configuration

The HTTP client includes security controls:
- Configurable timeouts (default: 30 seconds)
- Connection limits to prevent resource exhaustion
- Optional SSL/TLS verification (enabled by default)
- Security headers included in requests

### 5. Non-Root Container Execution

Docker containers run as non-root user (`mcpuser`) with UID 1000 for defense in depth.

### 6. Environment-Based Configuration

Sensitive credentials are never hardcoded:
- API keys loaded from environment variables only
- No credentials in code or configuration files
- Secrets excluded from logs and error messages

## Security Best Practices for Users

### API Credentials Management

**DO:**
- ✅ Store API keys in environment variables
- ✅ Use separate API keys for different environments
- ✅ Rotate API keys regularly
- ✅ Use API keys with minimal required permissions
- ✅ Never commit API keys to version control

**DON'T:**
- ❌ Hardcode API keys in configuration files
- ❌ Share API keys between team members
- ❌ Use production API keys in development
- ❌ Store API keys in plaintext files

### Environment Variables

Configure the server using these environment variables:

**Required:**
```bash
XSIAM_API_URL=https://your-xsiam-instance.com
XSIAM_API_KEY=your-xsiam-api-key
XSIAM_API_KEY_ID=your-xsiam-key-id

XSOAR_API_URL=https://your-xsoar-instance.com
XSOAR_API_KEY=your-xsoar-api-key
```

**Optional Security Settings:**
```bash
# Request timeout in seconds (default: 30)
API_TIMEOUT=30

# Maximum retry attempts (default: 3)
API_MAX_RETRIES=3

# SSL/TLS verification (default: true)
VERIFY_SSL=true

# Rate limiting
RATE_LIMIT_REQUESTS=100
RATE_LIMIT_WINDOW=60
```

### Secure Configuration Example

**For Windsurf/Cursor/Roo Code:**

```json
{
  "mcpServers": {
    "cortex": {
      "command": "docker",
      "args": ["run", "-i", "--read-only", "--security-opt=no-new-privileges", "cortex-mcp"],
      "env": {
        "XSOAR_API_URL": "${XSOAR_API_URL}",
        "XSOAR_API_KEY": "${XSOAR_API_KEY}",
        "XSIAM_API_URL": "${XSIAM_API_URL}",
        "XSIAM_API_KEY": "${XSIAM_API_KEY}",
        "XSIAM_API_KEY_ID": "${XSIAM_API_KEY_ID}",
        "VERIFY_SSL": "true",
        "API_TIMEOUT": "30"
      }
    }
  }
}
```

**Note:** Use environment variable references (e.g., `${XSOAR_API_KEY}`) instead of hardcoding credentials.

### Network Security

**SSL/TLS Verification:**
- SSL verification is enabled by default
- Only disable (`VERIFY_SSL=false`) in development with self-signed certificates
- Always use SSL/TLS verification in production

**API Endpoints:**
- Use HTTPS URLs only
- Verify your XSOAR/XSIAM instances have valid TLS certificates
- Keep your Cortex instances up to date with security patches

### Docker Security

**Run with additional security options:**
```bash
docker run -i \
  --read-only \
  --security-opt=no-new-privileges \
  --cap-drop=ALL \
  cortex-mcp
```

**Explanation:**
- `--read-only`: Makes container filesystem read-only
- `--security-opt=no-new-privileges`: Prevents privilege escalation
- `--cap-drop=ALL`: Drops all Linux capabilities (server doesn't need any)

## Reporting a Vulnerability

If you discover a security vulnerability, please report it responsibly:

1. **Do NOT** open a public GitHub issue
2. Email security details to the repository maintainer
3. Include:
   - Description of the vulnerability
   - Steps to reproduce
   - Potential impact
   - Suggested fix (if available)

We will:
- Acknowledge receipt within 48 hours
- Provide a detailed response within 7 days
- Work on a fix and coordinate disclosure timeline
- Credit you in the security advisory (if desired)

## Security Updates

Security updates will be released as:
- Patch versions for critical vulnerabilities
- Minor versions for security enhancements
- Documented in CHANGELOG and GitHub Security Advisories

## Compliance

This server follows security best practices aligned with:
- OWASP Top 10 security guidelines
- Secure development lifecycle (SDL) principles
- Defense in depth architecture
- Principle of least privilege

## Dependencies

We regularly:
- Monitor dependencies for known vulnerabilities
- Update dependencies when security patches are available
- Run automated security scans in CI/CD pipeline
- Use dependency scanning tools (GitHub Dependabot)

## Audit Trail

The server logs:
- Rate limit violations
- Input validation failures
- API request errors (with sanitized messages)

Logs never contain:
- API keys or tokens
- Passwords or secrets
- Full file paths
- Detailed system information

## Additional Resources

- [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices-quick-reference-guide/)
- [Model Context Protocol Security](https://modelcontextprotocol.io/docs/security)
- [Docker Security Best Practices](https://docs.docker.com/engine/security/)

## Questions?

For security-related questions, please:
1. Check this document first
2. Review the README.md for configuration guidance
3. Contact the maintainer for clarification

Thank you for helping keep Cortex-MCP secure!
