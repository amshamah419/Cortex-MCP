# Response Actions

This section documents 3 XSIAM tools related to response actions.

---

### `xsiam_abort_scan`

Cancel the scan of selected endpoints. A scan can only be aborted if the selected endpoints are in **Pending** or in **Progress** status. When filtering by multiple fields: - Response is concatenated using AND condition (OR is not supported). - Offset is the zero-based number of endpoints from the start of the result set. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_scan`

Run a scan on selected endpoints. - Response is concatenated using AND condition (OR is not supported). - Offset is the zero-based number of incidents from the start of the result set. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_unisolate`

Reverse the isolation of one or more endpoints in single request. Note: You can only send a request with either `endpoint_id` to unisolate one endpoint or with filters to unisolate more than one endpoint. An error is raised if you try to use both `endpoint_id` and the filters. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

