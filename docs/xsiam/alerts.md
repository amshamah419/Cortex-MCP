# Alerts

This section documents 8 XSIAM tools related to alerts.

---

### `xsiam_alerts_get_alerts_multi_events_v2`

Get a list of alerts with multiple events. - The response is concatenated using AND condition (OR is not supported). - The maximum result set size is 100. - Offset is the zero-based number of alerts from the start of the result set. Cortex XDR displays in the API response whether a PAN NGFW type alert contains a PCAP triggering packet. Use the **Retrieve PCAP Packet** API to retrieve a list of alert IDs and their associated PCAP data. Note: You can send a request to retrieve either all or filtered results. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary returns all results. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_alerts_get_alerts_v1`

Get a list of all or filtered alerts.  The alerts listed are what remains after alert exclusions are applied by Cortex XSIAM. - Response is concatenated using AND condition (OR is not supported). - Maximum result set size is 100. - Offset is the zero-based number of alerts from the start of the result set. The response indicates whether an PAN NGFW type alert contains a PCAP triggering packet. Use the Retrieve PCAP Packet API to retrieve a list of alert IDs and their associated PCAP data. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_create_alert`

Create a custom alert. In addition to the mandatory fields (`vendor`, `product`, `severity`, `category`), any field that appears in the alert table can be used. In order to use a field from the alert table, use its lower camel case representation. For example: `Container ID` -> `container_id`. If the field in the alert table contains a hyphen, replace it with underscore, for example: `App - ID` -> `app_id`. The following fields are recommended for creating an alert: - `remote_ip` - `remote_host` - `host_name` - `group_id` - `initiated_by` - `initiator_sha256` - `target_process_sha256` - `cgo_sha256` - `file_sha256` - `os_parent_cmd` - `os_parent_user_name` By using multiple calls of `create_alert`, you can send up to 600 alerts per minute. Required role: **App Service Account** Required licenses: **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_alerts_multi_events`

**Note: ** This endpoint is legacy. Use the [Get Alerts Multi-Events v2](https://cortex-panw.stoplight.io/docs/cortex-xsiam-1/guxcmlw6h3y8v-get-alerts-multi-events-v2) endpoint. Get a list of alerts with multiple events. - Response is concatenated using AND condition (OR is not supported). - Maximum result set size is 100. - Offset is the zero-based number of alerts from the start of the result set. Cortex XDR displays in the APIs response whether an PAN NGFW type alert contains a PCAP triggering packet. Use the Retrieve PCAP Packet API to retrieve a list of alert IDs and their associated PCAP data. Note: You can send a request to retrieve either all or filtered results. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_alerts_pcap`

Retrieve a list of alert IDs and the associated PCAP triggering packets of PAN NGFW type alerts returned when running the **Get Alerts** and **Get Extra Incident Data** APIs. Maximum result set size is 100. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_insert_cef_alerts`

Upload alerts in CEF format from external alert sources. After you map CEF alert fields to Cortex XDR fields, Cortex XDR displays the alerts in related incidents and views. You can send 600 alerts per minute. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_insert_parsed_alerts`

Upload alerts from external alert sources in Cortex XSIAM format. Cortex XSIAM displays alerts that are parsed successfully in related incidents and views. You can send 600 alerts per minute. Each request can contain a maximum of 60 alerts. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_update_alerts`

Update one or more alerts. You can update up to 100 alerts per request. Missing fields are ignored. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): (Required) A dictionary containing the API request fields. An empty dictionary returns all results. (optional)

**Returns:** List[types.TextContent]: Successful response

---

