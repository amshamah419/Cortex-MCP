# Indicators

This section documents 12 XSOAR tools related to indicators.

---

### `xsoar_create_feed_indicators_json`

Create indicators from raw JSON (similar to ingesting from a feed). Builds indicators according to the specified feed classifier, or uses the default one if not specified. Indicator properties (all optional except for value): **value** (string, required) | **type** (string) | **score** (number, 0-3, default `0`, where `0` means None, `1` Good, `2` Suspicious, and `3` Bad) | **sourceBrand** (string, default `"External"`) | **sourceInstance** (string, default `"External"`) | **reliability** (string, one of `"A - Completely reliable"`, `"B - Usually reliable"`, `"C - Fairly reliable"`, `"D - Not usually reliable"`, `"E - Unreliable"`, `"F - Reliability cannot be judged"`) | **expirationPolicy** (string, one of `"never"`, `"interval"`, `"indicatorType"`) | **expirationInterval** (number, in minutes)

**Parameters:** None

**Returns:** List[types.TextContent]: Indicators created

---

### `xsoar_delete_indicators_batch`

Batch whitelist or delete indicators entities In order to delete indicators and not whitelist, set doNotWhitelist boolean field to true

**Parameters:** None

**Returns:** List[types.TextContent]: UpdateResponse

---

### `xsoar_export_indicators_to_csv_batch`

Exports an indicators batch to CSV file (returns file ID)

**Parameters:** None

**Returns:** List[types.TextContent]: csv file name

---

### `xsoar_export_indicators_to_stix_batch`

Exports an indicators batch to STIX file (returns file ID)

**Parameters:** None

**Returns:** List[types.TextContent]: STIX file name

---

### `xsoar_indicator_whitelist`

Whitelists or deletes an indicator entity In order to delete an indicator and not whitelist, set doNotWhitelist boolean field to true

**Parameters:** None

**Returns:** List[types.TextContent]: UpdateResponse

---

### `xsoar_indicators_as_csv`

Get an indicators CSV file that was exported, by ID

**Parameters:**

- id (str): CSV file to fetch (returned from batch export to csv call) (required)

**Returns:** List[types.TextContent]: Return Csv file

---

### `xsoar_indicators_as_stix`

Get an indicators STIX V2 file that was exported, by ID

**Parameters:**

- id (str): STIX V2 file to fetch (returned from batch export to STIX call) (required)

**Returns:** List[types.TextContent]: Return STIX V2 file

---

### `xsoar_indicators_create`

Create an indicator entity To update indicator custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip

**Parameters:** None

**Returns:** List[types.TextContent]: IocObject

---

### `xsoar_indicators_create_batch`

Create indicators from a file

**Parameters:** None

**Returns:** List[types.TextContent]: IocObjects

---

### `xsoar_indicators_edit`

Edit an indicator entity To update indicator custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip

**Parameters:** None

**Returns:** List[types.TextContent]: IocObject

---

### `xsoar_indicators_search`

Search indicators by filter

**Parameters:** None

**Returns:** List[types.TextContent]: indicatorResult

---

### `xsoar_indicators_timeline_delete`

Delete indicators timeline by filter

**Parameters:** None

**Returns:** List[types.TextContent]: IndicatorEditBulkResponse

---

