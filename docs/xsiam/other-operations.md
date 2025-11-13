# Other Operations

This section documents 78 XSIAM tools related to other operations.

---

### `xsiam_allowlist`

Add files which do not exist in the allow or block lists to an allow list. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_asm_management_remove_asm_data_v1`

Remove certificates, domains (paid-level domains and subdomains), and IPv4 address ranges from your inventory. Remove up to 500 certificates, domains, or IP ranges per request. Removed assets appear the Asset Uploads/Removals table with the status **Removed**. Within 24 hours of submitting your request, assets are removed from the inventory. Within a few days, related incidents, alerts, and services are also removed. You cannot remove an asset that was uploaded in a previous upload request. When you remove a paid-level domain, related subdomains are also removed. When you remove an IPv4 range, the individual IPv4 addresses in that range are also removed. Required role: Instance Admin Required license: **Cortex XSIAM Premium** or **Cortex XSIAM with ASM add-on**

**Parameters:**

- authorization (str): {api-key} (required)
- x_xdr_auth_id (str): {api-key-id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_asm_management_upload_asm_data_v1`

Upload domains (paid-level domains (PLD) and subdomains) and IPv4 address ranges. You can upload up to 500 IP address ranges or domains in each request. You must have **Instance Administrator** permissions to run this endpoint. Required license: **Cortex XSIAM Premium** or  Cortex XSIAM with ASM add-on

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assets_bulk_update_vulnerability_tests_v1`

Enable or disable vulnerability tests.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assets_get_asset_internet_exposure_v1`

Get Internet exposure asset details according to the asset ID. You can send up to 20 IDs. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assets_get_assets_internet_exposure_v1`

Get a list of all your Internet exposure filtered by business units, externally detected providers, externally inferred CVEs, mac addresses, names, IP addresses, whether it has an XDR agent, whether it has active external services, and type. The maximum result limit is 500 assets. Note: You can send a request to retrieve either all or filtered results. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary returns all results. (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assets_get_external_service_v1`

Get service details according to the service ID. You can send up to 20 IDs. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise**, **Cortex XSIAM Enterprise Plus** or **Cortex XSIAM Premium**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assets_get_external_services_v1`

Get a complete or filtered list of all your external services. The maximum result limit is 500. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise**, **Cortex XSIAM Enterprise Plus** or **Cortex XSIAM Premium**

**Parameters:**

- authorization (str): api-key (required)
- x_xdr_auth_id (str): api-key-id (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assets_get_external_website_v1`

Get details about specific websites based on website IDs. You can submit up to 20 website IDs. Required license: **Cortex XSIAM Premium** or  Cortex XSIAM with ASM Add-on

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assets_get_external_websites_last_external_assessment_v1`

Gets the time and status of the last update of websites data in Cortex. A status of "true" indicates the websites data update was successful.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): An empty dictionary returns the time and status of the last websites assessment. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assets_get_external_websites_v1`

Get a complete or filtered list of your public-facing websites. Required license: **Cortex XSIAM Premium** or  Cortex XSIAM with ASM Add-on

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary returns all results. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assets_get_vulnerability_tests_v1`

Get a complete or filtered list of vulnerability tests. Results include details about each test, including the number of services confirmed vulnerable.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_assign`

Assign one or more tags to one or more endpoints. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_authentication_settings_create_v1`

Create authentication settings for IdP SSO or metadata URL. You must include either the `metadata_url` field or all of the following fields: `idp_sso_url`, `idp_issuer`, and `idp_certificate`. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_authentication_settings_delete_v1`

Delete all authentication settings for the specified domain. **Note: ** The first configuration on the tenant is the default configuration and cannot be deleted. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_authentication_settings_get_metadata_v1`

Get the metadata for all IdPs. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_authentication_settings_get_settings_v1`

Get all the authentication settings for every configured domain in the tenant. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_authentication_settings_update_v1`

Update existing authentication settings. To update the default domain, include empty value for both `current_domain_value` and `new_domain_value`. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_blocklist`

Add files which do not exist in the allow or block lists to a block list. You can view the block list in the UI at **Incident Response** > **Action Center** > **Block List**. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_correlations_delete_v1`

Delete correlation rules selected by filter. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_correlations_get_v1`

Return a list of correlation rules. You can return all correlation rules or filter results. You can also return extended results with all details included. - The response is concatenated using AND condition (OR is not supported). - The maximum result set size is >100. - Offset is the zero-based number of incidents from the start of the result set. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_correlations_insert_v1`

Insert new Correlation Rules or update existing Correlation Rules. **Note:** The Correlation Rule `id` is tenant specific and can't be used across tenants. Inserting Correlation Rules with the same `id` as an existing Correlation Rule on that tenant will overwrite the existing Correlation Rule. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (List[Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_create`

Create an installation package. This is an async call that returns the distribution ID; it does not mean that the creation succeeded. To confirm the package has been created, check the status of the distribution by running the **Get Distribution Status** API. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_dashboards_delete_v1`

Delete the dashboards retrieved by the Get dashboards API. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_dashboards_get_v1`

Get dashboard details by filtering based on the dashboard name, dashboard ID, time the dashboard was generated, or dashboard source. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_dashboards_insert_v1`

Add or update the dashboards retrieved by the Get dashboards API. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_dataset_define_dataset_v1`

Define an XQL user dataset based on an existing BigQuery table created by the user. **Note:** BigQuery table must be an existing table under public_access_user. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**. These APIs are only applicable from within the XSIAM Notebook environment.

**Parameters:**

- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_dataset_delete_dataset_v1`

Delete an XQL user dataset that was created by the Cortex SDK. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**. These APIs are only applicable from within the XSIAM Notebook environment.

**Parameters:**

- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_dataset_get_created_datasets_v1`

Retrieve a list of all XQL user datasets created using the Cortex SDK. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**. These APIs are only applicable from within the XSIAM Notebook environment.

**Parameters:** None

**Returns:** List[types.TextContent]: OK

---

### `xsiam_delete`

Delete selected endpoints in the Cortex XDR app. You can delete up to 1000 endpoints. Note: Endpoints are deleted from the Cortex XDR app web interface, however they still exist in the database. When filtering by multiple fields: - Response is concatenated using AND condition (OR is not supported). - Maximum result set size is 1000. - Offset is the zero-based number of incidents from the start of the result set. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_distributions_delete_v1`

Delete an agent installation package. The distribution ID is required and can be found in the [Create distributions](https://docs-cortex.paloaltonetworks.com/r/ppPm_R5Omz9LsbjR8gZJbg/NIB~j5teUOLZlFNOhL3dZg) API response or in the **Agent Installations** screen in the Cortex Console. **Note: ** Once you delete an installation package, it prevents new agents using the package, including VDI, from registering. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_entries_get_v1`

Get the War Room entries for a specific incident or alert. You can filter by timestamp, ID, and tags. You can also choose which type of entries you want to retrieve (notes, chat, attachments...). The response depends on what type of entry you choose to retrieve.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- id (str): The ID of the incident or alert you want to get the War Room entries of. For an incident ID, prepend \"INCIDENT-\" to the incident ID. For example, if the incident ID is 3, the value of `id` should be `INCIDENT-3`. For alert IDs, just put the ID. For example, if the alert ID is 3, the value of `id` should be `3`. (optional)
- filter (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_entries_insert_v1`

Add an entry to the incident or alert War Room, including data.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- id (str): The ID of the incident or alert for which you want to add a War Room entry. For an incident ID, prepend \"INCIDENT-\" to the incident ID. For example, if the incident ID is 3, the value of `id` should be `INCIDENT-3`. For alert IDs, just put the ID. For example, if the alert ID is 3, the value of `id` should be `3`. (optional)
- data (str): The data you want to add or the command you want to run in the War Room. (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_file_retrieval_details`

View the API required to call in order to download the file retrieved by the **Retrieve File** API request according to the action ID. The response contains a file hash you need to download and then unzip to view: 1. Download the file. <!-- title: "Request Example" --> ``` curl curl -XPOST "https://api-{fqdn}/public_api/v1/download/<api_value>" -H "x-xdr-auth-id:{API_KEY_ID}" -H "Authorization:{API_KEY}" -H 'Content-Type:application/json' --output /tmp/file.zip ``` 2. Unzip the file: `unzip /tmp/file.zip` Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_action_status`

Retrieve the status of the requested actions according to the action ID. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_dist_url`

Get the distribution URL for downloading the installation package. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_quota`

Retrieve the amount of query quota available and used. Note: This endpoint only works on XQL queries initiated by `/public_api/v1/xql/start_xql_query/`. For more information on how to run XQL queries, see [*Running XQL query APIs*](https://cortex-panw.stoplight.io/docs/cortex-xsiam-1/90ay3tlx6l9dh-running-xql-query-ap-is). <!-- theme: info --> > #### Note > > To ensure you don't surpass your quota, Cortex XSIAM allows you to run up to four API queries in parallel. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:** None

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_risk_score_v1`

Retrieve the risk score of a specific user or endpoint in your environment, along with the reason for the score. Required license: **Cortex XSIAM Premium** or **Identity Threat Module**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_get_script_code`

Get the code of a specific script in the script library. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_script_execution_results`

Retrieve the results of a script execution action. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_script_execution_results_files`

Get the files retrieved from a specific endpoint during a script execution. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_script_execution_status`

Retrieve the status of a script execution action. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_script_metadata`

Get the full definitions of a specific script in the scripts library. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_scripts`

Get a list of scripts available in the scripts library. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary returns all results. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_status`

Check the status of the installation package. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_get_triage_presets_v1`

Get all triage preset information including triage name, platform, description, created by, and triage type. Required license: **Cortex XSIAM Premium** or **Forensics add-on**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_get_versions`

Get a list of all the agent versions to use for creating a distribution list. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_healthcheck`

Perform a health check of your Cortex XSIAM environment. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_indicators_delete_v1`

Delete IOCs selected by filter. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_indicators_get_v1`

Get a list of IOCs. You can return all IOCs or filter results. You can also return extended results with all details included. - The response is concatenated using AND condition (OR is not supported). - The maximum result set size is >100. - Offset is the zero-based number of incidents from the start of the result set. UI navigation: **XSIAM** > **Detection & Threat Intel** > **Detection Rules** > **IOC**. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_indicators_insert_v1`

Insert new IOCs or update existing IOCs. **Note:** The IOC `rule_id` is tenant specific and can't be used across tenants. Inserting IOCs with the same `rule_id` as an existing IOC on that tenant will overwrite the existing IOC. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (List[Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_insert_csv`

Upload IOCs in CSV format that you retrieved from external threat intelligence sources. Note: Cortex XDR does not scan historic data, but rather only new incoming data. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (str): The body of this request contains a JSON object with a single field: `request_data`. This field is required. Its value is as string containing two or more comma-separated lines. The first line must contain the CSV header. All subsequent lines must represent IOC data. Each line must include at a minimum the required CSV fields, which are identified below. To help you validate the upload, you can send a separate validate field to view an array of errors with an unsuccessful call. | Field | Description | | ----------- | ----------- | | indicator | (Required) String that identifies the indicator you want to insert into Cortex XDR. | | type | (Required) Keyword identifying the type of indicator. Valid values are: `HASH`, `IP`, `PATH`, `DOMAIN_NAME`, or `FILENAME` | | severity | (Required) Keyword identifying the indicator's severity. Valid values are: `INFO`, `LOW`, `MEDIUM`, `HIGH`, or `CRITICAL` | | expiration_date | Integer representing the indicator's expiration timestamp. This is a Unix epoch timestamp value, in milliseconds. If this indicator has no expiration, use `Never`. If this value is NULL, the indicator receives the indicator's type value with the default expiration date. Valid values are: 7 days, 30 days, 90 days, or 180 days | | comment | Comment string. | | reputation | Keyword representing the indicator's reputation. Valid values are: `GOOD`, `BAD`, `SUSPICIOUS`, or `UNKNOWN` | | reliability | Character representing the indicator's reliability rating. Valid values are A-F. A is the most reliable, F is the least. | | class | String representing the indicator class (for example, \"Malware\") | | vendor.name | String representing the name of the vendor who reported this indicator. | | vendor.reputation | Keyword representing the vendor's reputation. Valid values are: `GOOD`, `BAD`, `SUSPICIOUS`, or `UNKNOWN` | | vendor.reliability | Character representing the vendor's reliability rating. Valid values are A-F. A is the most reliable, F is the least. | (required)
- validate (bool): Indicates whether to return an array of errors in the case of an unsuccessful update indicator API request. (optional)

**Returns:** List[types.TextContent]: SUCCESS

---

### `xsiam_insert_jsons`

Upload IOCs as JSON objects that you retrieved from external threat intelligence sources. Note: Cortex XSIAM does not scan historic data, rather only new incoming data. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (List[Any]): No description provided (required)
- validate (bool): Whether to return an array of errors in the case of an unsuccessful update indicator API request. (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_integrations_syslog_create_v1`

Create a new syslog integration. You must have **View/Edit Alert Notification** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_integrations_syslog_delete_v1`

Delete all the syslog integrations or the ones who match the filter criteria. You must have **View/Edit Alert Notification** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary deletes all syslog servers. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_integrations_syslog_get_v1`

Get a complete or filtered list of syslog servers. You must have **View Alert Notification** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary returns all results. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_integrations_syslog_test_v1`

Tests a syslog integration's validity. You must have **View Alert Notification** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_integrations_syslog_update_v1`

Update the details of the specified syslog integration. You must have **View/Edit Alert Notification** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_management_logs`

Get audit management logs. - Response is concatenated using AND condition (OR is not supported). - Maximum result set size is 100. - Offset is the zero-based number of incidents from the start of the result set.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. An empty dictionary returns all results. (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_playbooks_delete_v1`

Delete a playbook by filtering based on its name or ID. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_playbooks_get_v1`

Get a playbook by filtering based on its name or ID. The playbook's YAML is returned in a ZIP file. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_playbooks_insert_v1`

Add or update a playbook by passing the YAML in a ZIP file. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_quarantine`

Quarantine file on selected endpoints. You can select up to 1000 endpoints. Note: A success response means that the request reached the defined endpoints, however if the file was not found there, no quarantine action will take place. To ensure if the file has been quarantined, check the Cortex XDR Action Center. When filtering by multiple fields: - Response is concatenated using AND condition (OR is not supported). - Maximum result set size is 1000. - Offset is the zero-based number of incidents from the start of the result set.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_remove`

Remove one or more tags from one or more endpoints. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the following API request fields. (optional)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_restore`

Restore a quarantined file on a requested endpoints. When filtering by multiple fields: - Response is concatenated using AND condition (OR is not supported). - Maximum result set size is 100. - Offset is the zero-based number of incidents from the start of the result set. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_run_script`

Initiate a new endpoint script execution action using a script from the script library. The script can be run on up to 1000 endpoints. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_run_snippet_code_script`

Initiate a new endpoint script execution action using provided snippet code. Cortex XDR supports sending your request in Base64. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): A dictionary containing the API request fields. (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_scheduled_queries_delete_v1`

Delete scheduled queries. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (List[Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_scheduled_queries_insert_v1`

Insert new scheduled queries or update existing scheduled queries. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (List[Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_scheduled_queries_list_v1`

Return a list of scheduled queries. You can return all scheduled queries or filter results. You can also return extended results with all details included. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_scripts_delete_v1`

Delete a script by filtering based on its name or ID. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_scripts_get_v1`

Get a script by filtering based on its name or ID. The script's YAML is returned in a ZIP file. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_scripts_insert_v1`

Update or add a script by passing the YAML in a ZIP file. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_status`

Retrieve the quarantine status for specified files. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: Successful response

---

### `xsiam_system_get_tenant_info_v1`

Get your tenant license information. Required license: **Cortex XSIAM Premium** or **Cortex XSIAM Enterprise** or **Cortex XSIAM Enterprise Plus**

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_widgets_delete_v1`

Delete the widgets retrieved by the Get widgets API. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_widgets_get_v1`

Get widget details by filtering based on the widget title and widget creator. **Note:** The endpoint only returns XQL widgets and not predefined widgets. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (Dict[str, Any]): No description provided (required)

**Returns:** List[types.TextContent]: OK

---

### `xsiam_widgets_insert_v1`

Update or add the widgets retrieved by the Get widgets API. You must have **Instance Administrator** permissions to run this endpoint.

**Parameters:**

- authorization (str): {api_key} (required)
- x_xdr_auth_id (str): {api_key_id} (required)
- request_data (List[Any]): No description provided (optional)

**Returns:** List[types.TextContent]: OK

---

