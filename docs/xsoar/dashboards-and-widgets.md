# Dashboards & Widgets

This section documents 11 XSOAR tools related to dashboards & widgets.

---

### `xsoar_all_widgets`

Get all widgets

**Parameters:** None

**Returns:** List[types.TextContent]: Return all the widgets in the system.

---

### `xsoar_delete_widget`

Remove a given widget Id from the system.

**Parameters:**

- id (str): Widget id to remove (returned from widget save or widgets get) (required)

**Returns:** List[types.TextContent]: widget deleted

---

### `xsoar_get_stats_for_dashboard`

Get a given dashboard statistics result.

**Parameters:** None

**Returns:** List[types.TextContent]: Return an array of stats results for each widget cell in dashboard.

---

### `xsoar_get_stats_for_dashboard_old_format`

Get a given dashboard statistics result. Deprecated - use "/v2/statistics/dashboards/query

**Parameters:** None

**Returns:** List[types.TextContent]: Return an array of stats results for each widget cell in dashboard.

---

### `xsoar_get_stats_for_widget`

Get the statistics for the specified widget. **Note:** This endpoint has many return types depending on the widget type and data. Each 200X represents a 200 OK request of specific widget type and data.

**Parameters:** None

**Returns:** List[types.TextContent]: Response differ according to the widget type
-  Incident data type of a "table" or "list" widget returns incidentSearchResponse
total:
type: integer
data:
type: array
items:
"$ref": "#/definitions/Incident"
- Indicators data type of a "table" or "list" widget returns IoCsResponse
total:
type: integer
data:
type: array
items:
"$ref": "#/definitions/IocObject"
- Number widget returns a simple number
type: integer
- Trend widget returns a trend object
"$ref": "#/definitions/StatsTrendsResponse"
- Text widget returns a text object, describing the final text and the placeholders values.
"$ref": "#/definitions/StatsTextResponse"
- Line chart widget or Column chart widget returns StatsResponseWithReferenceLine
"$ref": "#/definitions/StatsResponseWithReferenceLine"
- A chart data array by groups. When requesting a date, the key is the date string, according to the specified time frame. Empty groups (dates) are also returned.
type: array
items:
"$ref": "#/definitions/Group"

---

### `xsoar_get_stats_for_widget_old_format`

Get a given widget object statistics result. Note: This route has many return types based on the widget type and data. Each 200X represent a 200 OK request of specific widget type and data Deprecated - use "/v2/statistics/widgets/query

**Parameters:** None

**Returns:** List[types.TextContent]: Response differ according to the widget type
-  Incident data type of a "table" or "list" widget returns incidentSearchResponse
total:
type: integer
data:
type: array
items:
"$ref": "#/definitions/Incident"
- Indicators data type of a "table" or "list" widget returns IoCsResponse
total:
type: integer
data:
type: array
items:
"$ref": "#/definitions/IocObject"
- Number widget returns a simple number
type: integer
- Trend widget returns a trend object
"$ref": "#/definitions/StatsTrendsResponse"
- Text widget returns a text object, describing the final text and the placeholders values.
"$ref": "#/definitions/StatsTextResponse"
- A chart data array by groups. When requesting a date, the key is the date string, according to the specified time frame. Empty groups (dates) are also returned.
type: array
items:
"$ref": "#/definitions/Group"

---

### `xsoar_get_widget`

Get a widget object by a given ID.

**Parameters:**

- id (str): The ID of widget to get. (required)

**Returns:** List[types.TextContent]: Return the widget if found.

---

### `xsoar_import_dashboard`

Import a dashboard to Cortex XSOAR

**Parameters:** None

**Returns:** List[types.TextContent]: The saved dashboard

---

### `xsoar_import_widget`

Import a widget to the system, ignoring ID or version, used to import new widgets.

**Parameters:** None

**Returns:** List[types.TextContent]: The saved widget

---

### `xsoar_reset_roi_widget`

Reset ROI widget

**Parameters:** None

**Returns:** List[types.TextContent]: ROI widget has been reset

---

### `xsoar_save_widget`

Add or update a given widget based on Id.

**Parameters:** None

**Returns:** List[types.TextContent]: The saved widget newest version.

---

