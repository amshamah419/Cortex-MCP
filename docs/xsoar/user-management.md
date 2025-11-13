# User Management

This section documents 2 XSOAR tools related to user management.

---

### `xsoar_logout_user_sessions_handler`

Sign out all sessions of the provided username

**Parameters:**

- username (str): Username to logout (required)

**Returns:** List[types.TextContent]: no content

---

### `xsoar_revoke_user_api_key`

Revoke API Key for user

**Parameters:**

- username (str): The username which the API keys assigned to (required)

**Returns:** List[types.TextContent]: 200 for success

---

