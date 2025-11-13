# Endpoints

This section documents 7 XSIAM tools related to endpoints.

---

### `xsiam_audits_agents_reports_v1`

Get agent event reports. - Response is concatenated using AND condition (OR is not supported). - Maximum result set size is 100. - Offset is the zero-based number of incidents from the start of the result set. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary returns all results. (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_endpoints_file_retrieval_v1`

Retrieve files from selected endpoints. You can retrieve up to 20 files, from no more than 10 endpoints. - Response is concatenated using AND condition (OR is not supported). - Offset is the zero-based number of incidents from the start of the result set. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_endpoints_get_endpoint_v1`

Gets a list of filtered endpoints. - The response is concatenated using AND condition (OR is not supported). - The maximum result set size is 100. - Offset is the zero-based number of endpoints from the start of the result set. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary returns all results. (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_endpoints_isolate_v1`

Isolate one or more endpoints in a single request. Request is limited to 1000 endpoints. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_get_endpoints`

Gets a list of all of your endpoints. The response is concatenated using AND condition (OR is not supported). Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_triage_endpoint_v1`

Initiate forensics triage for the specified agents. - Maximum of 10 concurrent triage actions at a time. - Specified agents must have Forensics License enabled. - Specified agents must be the same OS, Windows or macOS, but not a mixture of both. - Specified configuration must have type "Online = True". Required license: **Cortex XSIAM Premium** or

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_update_agent_name`

Set or modify an Alias field for your endpoints. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: Successful response

---

