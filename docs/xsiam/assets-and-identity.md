# Assets & Identity

This section documents 11 XSIAM tools related to assets & identity.

---

### `xsiam_assets_get_external_ip_address_range_v1`

Get external IP address range details according to the range IDs. You can send up to 100 IDs. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assets_get_external_ip_address_ranges_v1`

Get a list of all your Internet exposure filtered by business units and organization handles. The maximum result limit is 1000 ranges. Note: You can send a request to retrieve either **all** or **filtered** results. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary returns all results. (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_get_risky_hosts_v1`

Retrieve a list of endpoints with the highest risk score in your environment along with the reason for each score. Required license: **Cortex XSIAM Premium** or **Identity Threat Module**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_get_risky_users_v1`

Retrieve a list of users with the highest risk score in your environment along with the reason affecting each score. Required license: **Cortex XSIAM Premium** or **Identity Threat Module**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_rbac_get_user_group_v1`

Retrieve a list of the current user emails associated with one or more user groups in your environment. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_rbac_get_users_v1`

Retrieve a list of the current users in your environment. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_rbac_set_user_role_v1`

Add or remove one or more users from a role. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_replace_ad_groups`

Replace the featured active directory groups and organizational units listed in your environment. Note: Running this API will delete all existing active directory groups. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_replace_hosts`

Replace the featured hosts listed in your environment. Note: Running this API will delete all existing host names. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_replace_ip_addresses`

Replace the featured IP addresses listed in your environment. Note: Running this API will delete all existing IP addresses. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_replace_users`

Replace the featured users listed in your environment. Note: Running this API will delete all existing user names. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

