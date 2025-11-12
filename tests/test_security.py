"""Security tests for the Cortex MCP server."""

import pytest
from server.security import (
    sanitize_input,
    validate_inputs,
    sanitize_error_message,
    get_api_config,
    RateLimiter,
)


def test_sanitize_input_removes_dangerous_chars():
    """Test that dangerous characters are removed from input."""
    # Test script tag removal
    malicious = "<script>alert('xss')</script>"
    result = sanitize_input(malicious)
    assert "<script>" not in result
    assert "alert" in result  # Letters are preserved

    # Test SQL injection attempt
    sql_injection = "'; DROP TABLE users; --"
    result = sanitize_input(sql_injection)
    assert "DROP TABLE users" in result  # Letters preserved
    assert "'" not in result  # Quotes removed
    assert ";" not in result  # Semicolons removed


def test_sanitize_input_preserves_safe_chars():
    """Test that safe characters are preserved."""
    safe_input = "user@example.com test-value_123 path/to/file"
    result = sanitize_input(safe_input)
    assert "@" in result
    assert "-" in result
    assert "_" in result
    assert "/" in result


def test_sanitize_input_length_limit():
    """Test that input length is limited."""
    long_input = "a" * 5000
    result = sanitize_input(long_input)
    assert len(result) == 1000


def test_sanitize_input_non_string():
    """Test that non-string inputs are returned as-is."""
    assert sanitize_input(123) == 123
    assert sanitize_input(None) is None
    assert sanitize_input({"key": "value"}) == {"key": "value"}


def test_validate_inputs_rejects_long_strings():
    """Test that very long inputs are rejected."""
    params = {
        "test_param": "a" * 15000,
    }
    with pytest.raises(ValueError, match="exceeds maximum length"):
        validate_inputs(params)


def test_validate_inputs_accepts_normal_strings():
    """Test that normal inputs are accepted."""
    params = {
        "param1": "normal value",
        "param2": "another value",
    }
    # Should not raise any exception
    validate_inputs(params)


def test_validate_inputs_skips_self():
    """Test that 'self' parameter is skipped."""
    params = {
        "self": "some_object",
        "other": "value",
    }
    # Should not raise even though 'self' is a string
    validate_inputs(params)


def test_sanitize_error_message_redacts_api_keys():
    """Test that API keys are redacted from error messages."""
    error = "Failed to authenticate with api_key=abc123xyz"
    result = sanitize_error_message(error)
    assert "abc123xyz" not in result
    assert "API_KEY_REDACTED" in result


def test_sanitize_error_message_redacts_tokens():
    """Test that tokens are redacted from error messages."""
    error = "Invalid token: bearer_token_xyz789"
    result = sanitize_error_message(error)
    assert "xyz789" not in result
    assert "TOKEN_REDACTED" in result


def test_sanitize_error_message_redacts_passwords():
    """Test that passwords are redacted from error messages."""
    error = "Authentication failed with password=mysecretpass"
    result = sanitize_error_message(error)
    assert "mysecretpass" not in result
    assert "PASSWORD_REDACTED" in result


def test_sanitize_error_message_limits_length():
    """Test that error messages are truncated."""
    long_error = "Error: " + "a" * 1000
    result = sanitize_error_message(long_error)
    assert len(result) == 500


def test_get_api_config_defaults():
    """Test that API config has sensible defaults."""
    config = get_api_config()

    assert "xsiam_api_url" in config
    assert "xsoar_api_url" in config
    assert config["timeout"] == 30
    assert config["verify_ssl"] is True


def test_rate_limiter_allows_within_limit():
    """Test that rate limiter allows requests within limit."""
    limiter = RateLimiter(max_requests=5, window_seconds=60)

    # Should allow first 5 requests
    for _ in range(5):
        assert limiter.check_rate_limit("test_user") is True


def test_rate_limiter_blocks_over_limit():
    """Test that rate limiter blocks requests over limit."""
    limiter = RateLimiter(max_requests=3, window_seconds=60)

    # Use up the limit
    for _ in range(3):
        limiter.check_rate_limit("test_user")

    # Next request should be blocked
    assert limiter.check_rate_limit("test_user") is False


def test_rate_limiter_different_identifiers():
    """Test that rate limiter tracks different identifiers separately."""
    limiter = RateLimiter(max_requests=2, window_seconds=60)

    # User 1 uses up their limit
    limiter.check_rate_limit("user1")
    limiter.check_rate_limit("user1")

    # User 2 should still be allowed
    assert limiter.check_rate_limit("user2") is True


def test_rate_limiter_window_expiry():
    """Test that rate limiter window expires correctly."""
    import time

    limiter = RateLimiter(max_requests=2, window_seconds=1)

    # Use up the limit
    limiter.check_rate_limit("test_user")
    limiter.check_rate_limit("test_user")

    # Should be blocked
    assert limiter.check_rate_limit("test_user") is False

    # Wait for window to expire
    time.sleep(1.1)

    # Should be allowed again
    assert limiter.check_rate_limit("test_user") is True
