# Incidents & Investigations

This section documents 17 XSOAR tools related to incidents & investigations.

---

### `xsoar_close_incidents_batch`

Closes an incidents batch To update incident custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip To get the actual key name you can also go to Cortex XSOAR CLI and run /incident_add and look for the key that you would like to update

**Parameters:** None

**Returns:** List[types.TextContent]: IncidentSearchResponseWrapper

---

### `xsoar_create_incident`

Create or update incident according to JSON structure. To update incident custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip To get the actual key name you can also go to Cortex XSOAR CLI and run /incident_add and look for the key that you would like to update Use the 'createInvestigation\: true' to start the investigation process automatically. (by running a playbook based on incident type.)

**Parameters:** None

**Returns:** List[types.TextContent]: IncidentWrapper

---

### `xsoar_create_incident_json`

Create single incident from raw JSON, builds incident according to default mapping

**Parameters:** None

**Returns:** List[types.TextContent]: Created

---

### `xsoar_create_incidents_batch`

Update a batch of incidents. To update incident custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip To get the actual key name you can also go to Cortex XSOAR CLI and run /incident_add and look for the key that you would like to update

**Parameters:** None

**Returns:** List[types.TextContent]:

---

### `xsoar_create_or_update_incident_type`

API to create new Incident Type

**Parameters:** None

**Returns:** List[types.TextContent]: IncidentType

---

### `xsoar_delete_incidents_batch`

Deletes an incidents batch

**Parameters:** None

**Returns:** List[types.TextContent]: IncidentSearchResponseWrapper

---

### `xsoar_export_incidents_to_csv_batch`

Exports an incidents batch to CSV file (returns file ID)

**Parameters:** None

**Returns:** List[types.TextContent]: csv file name

---

### `xsoar_import_incident_fields`

Import an incident field to Cortex XSOAR

**Parameters:** None

**Returns:** List[types.TextContent]: The saved incident field

---

### `xsoar_import_incident_types_handler`

Import an incident type to Cortex XSOAR.

**Parameters:** None

**Returns:** List[types.TextContent]: The saved incident type

---

### `xsoar_incident_as_csv`

Get an incident CSV file that was exported, by ID

**Parameters:**

- id (str): CSV file to fetch (returned from batch export to csv call) (required)

**Returns:** List[types.TextContent]: Return Csv file

---

### `xsoar_incident_file_upload`

Add file attachement to an incidents

**Parameters:**

- id (str): Incident id to update (required)

**Returns:** List[types.TextContent]: IncidentWrapper

---

### `xsoar_incidents_fields_by_incident_type`

Get all incident fields associated with incident type

**Parameters:**

- type (str): the name (case sensitive) of the incident type (required)

**Returns:** List[types.TextContent]: Returns a list of incident fields associated with the incident type

---

### `xsoar_investigation_add_entries_sync`

API to create an entry (markdown format) in existing investigation Body example: {"investigationId":"1234","data":"entry content…"}

**Parameters:** None

**Returns:** List[types.TextContent]: An array of the children entries of the executed entry.

---

### `xsoar_investigation_add_entry_handler`

API to create an entry (markdown format) in existing investigation Body example: {"investigationId":"1234","data":"entry content…"}

**Parameters:** None

**Returns:** List[types.TextContent]: Entry

---

### `xsoar_investigation_add_formatted_entry_handler`

API to create a formatted entry (table/json/text/markdown/html) in existing investigation Body example: {"investigationId":"1234","format":"table/json/text/markdown/html","contents":"entry content…"}

**Parameters:** None

**Returns:** List[types.TextContent]: Entry

---

### `xsoar_search_incidents`

Search incidents across all indices. You can filter by multiple options. **Note:** You cannot paginate results in a multi-tenant environment.

**Parameters:** None

**Returns:** List[types.TextContent]: incidentSearchResponse

---

### `xsoar_search_investigations`

This will search investigations across all indices You can filter by multiple options

**Parameters:** None

**Returns:** List[types.TextContent]: investigationSearchResponse

---

