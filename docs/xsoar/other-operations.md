# Other Operations

This section documents 29 XSOAR tools related to other operations.

---

### `xsoar_add_ad_hoc_task`

Add an ad-hoc task to a running playbook

**Parameters:**

- investigation_id (str): investigation ID (required)

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_all_reports`

Get all of the reports

**Parameters:** None

**Returns:** List[types.TextContent]: Return array of reports

---

### `xsoar_complete_task`

Complete a task with a file attachment Deprecated - use "/v2/inv-playbook/task/complete"

**Parameters:** None

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_complete_task_v2`

Complete a task with command and multiple file attachments

**Parameters:** None

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_containers`

Gets info on the containers - amount of running, inactive and total containers

**Parameters:** None

**Returns:** List[types.TextContent]: Gets info on the containers - amount of running, inactive and total containers

---

### `xsoar_create_docker_image`

Create an image with a given list of dependencies

**Parameters:** None

**Returns:** List[types.TextContent]: NewDockerImageResult

---

### `xsoar_create_or_update_whitelisted`

Create or update excluded indicators list

**Parameters:** None

**Returns:** List[types.TextContent]: WhitelistedIndicator

---

### `xsoar_delete_ad_hoc_task`

Delete an ad-hoc task from a running playbook

**Parameters:**

- inv_pb_task_id (str): ad-hoc task ID (required)
- investigation_id (str): investigation ID (required)

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_docker_images`

Get list of all available docker image names

**Parameters:** None

**Returns:** List[types.TextContent]: DockerImagesResult

---

### `xsoar_download_file`

Download file from Cortex XSOAR by entry ID

**Parameters:**

- entryid (str): Entry ID (required)

**Returns:** List[types.TextContent]: Return the entry

---

### `xsoar_download_latest_report`

Get the latest report by its ID. **Note:** To get the report, it must be a scheduled report with recipients.

**Parameters:**

- id (str): the ID of the report to get (required)

**Returns:** List[types.TextContent]: Return a report file

---

### `xsoar_edit_ad_hoc_task`

Edit an ad-hoc task in a running playbook

**Parameters:**

- investigation_id (str): investigation ID (required)

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_execute_report`

Execute a new report

**Parameters:**

- request_id (str): the ID to register the request under (required)
- id (str): the ID of the report to get (required)

**Returns:** List[types.TextContent]: Request registered

---

### `xsoar_get_audits`

Get audits by filter

**Parameters:** None

**Returns:** List[types.TextContent]: auditResult

---

### `xsoar_health_handler`

Check if Cortex XSOAR server is available

**Parameters:** None

**Returns:** List[types.TextContent]: OK status

---

### `xsoar_logout_everyone_handler`

Sign out all open users sessions

**Parameters:** None

**Returns:** List[types.TextContent]: no content

---

### `xsoar_logout_myself_handler`

Sign out all my open sessions

**Parameters:** None

**Returns:** List[types.TextContent]: no content

---

### `xsoar_logout_myself_other_sessions_handler`

Sign out all my other open sessions

**Parameters:** None

**Returns:** List[types.TextContent]: no content

---

### `xsoar_report_by_id`

Get a report by its ID

**Parameters:**

- id (str): the ID of the report to get (required)

**Returns:** List[types.TextContent]: Return a report

---

### `xsoar_set_tags_field`

Sets the select values of a specific tags field. The values passed to the route override the existing select values of the field. To reset the select values pass an empty array.

**Parameters:**

- id (str): The machine name of the field prefixed with the type. For example indicator_tags or incident_dbotmirrortags (required)

**Returns:** List[types.TextContent]: empty

---

### `xsoar_simple_complete_task`

Complete a task without a file attachment

**Parameters:** None

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_submit_task_form`

Submit a data collection task with given answers and multiple file attachments

**Parameters:** None

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_task_add_comment`

Add comment to a task

**Parameters:** None

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_task_assign`

Assign a task to an owner

**Parameters:** None

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_task_set_due`

Set the task due date

**Parameters:** None

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_task_un_complete`

Reopen a closed task and change the status to uncomplete

**Parameters:** None

**Returns:** List[types.TextContent]: InvestigationPlaybook

---

### `xsoar_upload_content_packs`

Upload Pack to the Server. Can be used to upload a Pack for an offline scenario or a Pack that hasn't been released.

**Parameters:** None

**Returns:** List[types.TextContent]: The pack was successfully uploaded

---

### `xsoar_upload_report`

Upload a report to Cortex XSOAR

**Parameters:** None

**Returns:** List[types.TextContent]: A list of all the reports in the instance

---

### `xsoar_workers_status_handler`

Get workers status

**Parameters:** None

**Returns:** List[types.TextContent]: Workers status

---

