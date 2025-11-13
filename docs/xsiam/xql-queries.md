# XQL Queries

This section documents 12 XSIAM tools related to xql queries.

---

### `xsiam_get_query_results`

Retrieve results of an executed XQL query API. Note: This endpoint only works on XQL queries initiated by `/public_api/v1/xql/start_xql_query/`. Maximum result set size is 1000. The API does not support pagination, therefore, you can set values to determine the result size limitation and how to wait for the results. To view response with greater than 1000 results you must call **Get XQL query results Stream**. For more information on how to run XQL queries, see [*Running XQL query APIs*](https://cortex-panw.stoplight.io/docs/cortex-xsiam-1/90ay3tlx6l9dh-running-xql-query-ap-is). <!-- theme: info --> > #### Note > > To ensure you don't surpass your quota, Cortex XSIAM allows you to run up to four API queries in parallel. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_query_results_stream`

Retrieve XQL query results with more than 1000 results. Note: This endpoint only works on XQL queries initiated by `/public_api/v1/xql/start_xql_query/`. Response is returned as chunked (Transfer-Encoding: chunked). To retrieve a compressed gzipped response (Content-Encoding: gzip), in your header add Accept-Encoding: gzip. For more information on how to run XQL queries, see [*Running XQL query APIs*](https://cortex-panw.stoplight.io/docs/cortex-xsiam-1/90ay3tlx6l9dh-running-xql-query-ap-is). <!-- theme: info --> > #### Note > > To ensure you don't surpass your quota, Cortex XSIAM allows you to run up to four API queries in parallel. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- accept__encoding (str): For retrieving a compressed gzipped response (optional)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_start_xql_query`

Execute an XQL query. For more information on how to run XQL queries, see [*Running XQL query APIs*](https://cortex-panw.stoplight.io/docs/cortex-xsiam-1/90ay3tlx6l9dh-running-xql-query-ap-is). <!-- theme: info --> > #### Note > > To ensure you don't surpass your quota, Cortex XSIAM allows you to run up to four API queries in parallel. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_xql_add_dataset_v1`

Add a dataset of type `lookup` with the specified name and schema. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_xql_delete_dataset_v1`

Delete a dataset with the specified name. The following dataset types can be deleted: Lookup, Raw, User, Snapshot, and Correlation. You can only delete a dataset with dependencies by setting `force` to TRUE. **Note:** The System dataset and other protected datasets cannot be deleted. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_xql_get_datasets_v1`

Retrieve a list of all the datasets and their properties. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_xql_library_delete`

Delete XQL queries. You can filter by list of query names or by list of query tags. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_xql_library_get`

Retrieve a detailed list of XQL query libraries. You can filter by list of query names or by list of query tags. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_xql_library_insert`

Insert new XQL queries or update existing XQL queries. **Note:** You should use unique `xql_query_name` for each XQL query on a given tenant. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_xql_lookups_add_data_v1`

Add or update data in a lookup dataset. When updating data, any field not specified in the `data` field, but specified on at least one of the rows, will be set to `None`. The `/public_api/xql/lookups/add_data/`  endpoint does not support concurrent edits. Sending concurrent calls to this endpoint can cause data to be unintentionally overwritten or deleted. To allow sufficient time for each API call to complete its operation before initiating another one, assume that 1000 entries can be added per API every 10 seconds. **Note: ** - The maximum size of a lookup dataset is 50 MB. Attemping to exceed this limit will fail. - Requests time out after three minutes. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_xql_lookups_get_data_v1`

Get data from a lookup dataset according to the specified filter fields. All lookup entries matching any of the filter blocks are returned. To match a filter block, a lookup entry must match all the specified fields as if there were an `AND` operator between them. If no filters are specified, return all lookup entries. **Note:** - The maximum number of entries returned is 10,000. - Requests time out after three minutes. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_xql_lookups_remove_data_v1`

Remove data from a dataset based on the specified parameters. If any one of the filter sets are not found, the API does not delete any data. The `/public_api/xql/lookups/remove_data/`  endpoint does not support concurrent edits. Sending concurrent calls to this endpoint can cause data to be unintentionally overwritten or deleted. To allow sufficient time for each API call to complete its operation before initiating another one, assume that 1000 entries can be added per API every 10 seconds. **Note:** - All lookup entries matching any of the filter blocks are deleted. To match a filter block, a lookup entry must match all the specified fields as if there were an `AND` operator between them. - Requests time out after three minutes. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

