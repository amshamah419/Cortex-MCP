# Policy & Compliance

This section documents 2 XSIAM tools related to policy & compliance.

---

### `xsiam_get_policy`

Get the policy name for a specific endpoint. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_violations`

Gets a list of device control violations filtered by selected fields. You can retrieve up to 100 violations. When filtering by multiple fields: - Response is concatenated using AND condition (OR is not supported). - Maximum result set size is 100. - Offset is the zero-based number of incidents from the start of the result set. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): An empty object returns all results. (optional)

**Returns:** List[types.TextContent]: Successful response

---

