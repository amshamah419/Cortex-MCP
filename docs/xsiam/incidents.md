# Incidents

This section documents 3 XSIAM tools related to incidents.

---

### `xsiam_get_incidents`

Get a list of incidents filtered by a list of incident IDs, modification time, or creation time.  This includes all incident types and severities, including correlation-generated incidents. - The response is concatenated using AND condition (OR is not supported). - The maximum result set size is >100. - Offset is the zero-based number of incidents from the start of the result set. Note: You can send a request to retrieve either **all** or **filtered** results. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary returns all results. (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_incidents_get_incident_extra_data_v1`

Get extra data fields of a specific incident including alerts and key artifacts. - Cortex XDR displays in the APIs response whether a PAN NGFW type alert contains a PCAP triggering packet. Use the **Retrieve PCAP Packet** API to retrieve a list of alert IDs and their associated PCAP data. Note: The API includes a limit rate of 10 API requests per minute. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_update_incident`

Update one or more fields of a specific incident. Missing fields are ignored. **Note**: - `assigned_user_mail` field is validated by Cortex XSIAM to confirm the provided assignee email address belongs to a user that exists in the same Cortex XSIAM tenant. - To unassign an incident pass `none` or `"assigned_user_mail": ""`. - To remove a manually set severity pass `none` or `"manual_severity": ""`.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: Successful response

---

