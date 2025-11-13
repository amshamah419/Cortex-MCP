# Threat Intelligence

This section documents 3 XSIAM tools related to threat intelligence.

---

### `xsiam_bioc_delete_v1`

Delete BIOCs selected by filter. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_bioc_get_v1`

Return a list of BIOCs. You can return all BIOCs or filter results. You can also return extended results with all details included.- The response is concatenated using AND condition (OR is not supported). - The maximum result set size is >100. - Offset is the zero-based number of incidents from the start of the result set. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_bioc_insert_v1`

Insert new BIOCs or update existing BIOCs. **Note:** The BIOC `rule_id` is tenant specific and can't be used across tenants. Inserting BIOCs with the same `rule_id` as an existing BIOC on that tenant will overwrite the existing BIOC. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (List[Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

