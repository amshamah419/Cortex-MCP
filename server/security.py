"""
Security utilities for Cortex MCP server.
Provides input validation, rate limiting, and security controls.
"""

import os
import re
import time
from collections import defaultdict
from typing import Any, Dict
from functools import wraps

import httpx


class RateLimiter:
    """Simple rate limiter to prevent API abuse."""

    def __init__(self, max_requests: int = 100, window_seconds: int = 60):
        self.max_requests = max_requests
        self.window_seconds = window_seconds
        self.requests: Dict[str, list] = defaultdict(list)

    def check_rate_limit(self, identifier: str) -> bool:
        """Check if request is within rate limit."""
        now = time.time()
        # Clean old requests outside window
        self.requests[identifier] = [
            req_time
            for req_time in self.requests[identifier]
            if now - req_time < self.window_seconds
        ]

        # Check if limit exceeded
        if len(self.requests[identifier]) >= self.max_requests:
            return False

        # Record this request
        self.requests[identifier].append(now)
        return True


# Global rate limiter instance
_rate_limiter = RateLimiter(
    max_requests=int(os.getenv("RATE_LIMIT_REQUESTS", "100")),
    window_seconds=int(os.getenv("RATE_LIMIT_WINDOW", "60")),
)


def get_rate_limiter() -> RateLimiter:
    """Get the global rate limiter instance."""
    return _rate_limiter


def sanitize_input(value: Any) -> Any:
    """
    Sanitize user input to prevent injection attacks.

    Args:
        value: Input value to sanitize

    Returns:
        Sanitized value
    """
    if isinstance(value, str):
        # Remove potentially dangerous characters while preserving useful ones
        # Allow alphanumeric, spaces, hyphens, underscores, dots, @, commas, colons, slashes
        sanitized = re.sub(r"[^\w\s\-_.@,:/]", "", value)
        # Limit length to prevent DoS
        return sanitized[:1000]
    return value


def validate_inputs(params: Dict[str, Any]) -> None:
    """
    Validate input parameters for security.

    Args:
        params: Dictionary of parameters to validate

    Raises:
        ValueError: If validation fails
    """
    for key, value in params.items():
        if key == "self":  # Skip 'self' from locals()
            continue
        if value is not None and isinstance(value, str):
            # Check for extremely long inputs
            if len(value) > 10000:
                raise ValueError(f"Input parameter '{key}' exceeds maximum length")
            # Check for obvious injection attempts
            if any(pattern in value.lower() for pattern in ["<script", "javascript:", "onerror="]):
                raise ValueError(f"Input parameter '{key}' contains potentially malicious content")


def sanitize_error_message(error: str) -> str:
    """
    Sanitize error messages to prevent information leakage.

    Args:
        error: Error message to sanitize

    Returns:
        Sanitized error message
    """
    # Remove sensitive information patterns
    sanitized = re.sub(r"api[_-]?key[=:]?\s?[\w-]+", "API_KEY_REDACTED", error, flags=re.IGNORECASE)
    sanitized = re.sub(r"token[=:]?\s?[\w-]+", "TOKEN_REDACTED", sanitized, flags=re.IGNORECASE)
    sanitized = re.sub(
        r"password[=:]?\s?[\w-]+", "PASSWORD_REDACTED", sanitized, flags=re.IGNORECASE
    )
    sanitized = re.sub(r"secret[=:]?\s?[\w-]+", "SECRET_REDACTED", sanitized, flags=re.IGNORECASE)
    # Remove file paths that might leak system information
    sanitized = re.sub(r"/[\w/]+/", "/PATH_REDACTED/", sanitized)
    sanitized = re.sub(r"[A-Z]:\\[\w\\]+\\", r"PATH_REDACTED\\", sanitized)
    # Limit error message length
    return sanitized[:500]


def get_api_config() -> Dict[str, Any]:
    """
    Get API configuration from environment variables with secure defaults.

    Returns:
        Dictionary with API configuration
    """
    return {
        "xsiam_api_url": os.getenv("XSIAM_API_URL", "https://api-yourfqdn"),
        "xsoar_api_url": os.getenv("XSOAR_API_URL", "https://your-xsoar-instance.com"),
        "timeout": int(os.getenv("API_TIMEOUT", "30")),
        "max_retries": int(os.getenv("API_MAX_RETRIES", "3")),
        "verify_ssl": os.getenv("VERIFY_SSL", "true").lower() == "true",
    }


def get_http_client() -> httpx.AsyncClient:
    """
    Create a configured HTTP client with security settings.

    Returns:
        Configured httpx.AsyncClient
    """
    config = get_api_config()
    return httpx.AsyncClient(
        timeout=config["timeout"],
        verify=config["verify_ssl"],
        limits=httpx.Limits(max_keepalive_connections=5, max_connections=10),
        headers={
            # Security headers
            "X-Content-Type-Options": "nosniff",
            "X-Frame-Options": "DENY",
            "X-XSS-Protection": "1; mode=block",
        },
    )


def rate_limit(identifier_func=None):
    """
    Decorator to apply rate limiting to functions.

    Args:
        identifier_func: Optional function to extract identifier from args
    """

    def decorator(func):
        @wraps(func)
        async def wrapper(*args, **kwargs):
            # Use a default identifier if none provided
            identifier = "default"
            if identifier_func:
                identifier = identifier_func(*args, **kwargs)

            limiter = get_rate_limiter()
            if not limiter.check_rate_limit(identifier):
                raise Exception("Rate limit exceeded. Please try again later.")

            return await func(*args, **kwargs)

        return wrapper

    return decorator
