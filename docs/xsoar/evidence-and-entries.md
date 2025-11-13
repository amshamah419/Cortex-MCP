# Evidence & Entries

This section documents 6 XSOAR tools related to evidence & entries.

---

### `xsoar_delete_evidence_op`

Delete an evidence entity

**Parameters:** None

**Returns:** List[types.TextContent]: Deleted evidence ID

---

### `xsoar_entry_export_artifact`

Export an entry artifact

**Parameters:** None

**Returns:** List[types.TextContent]: created file name

---

### `xsoar_save_evidence`

Save an evidence entity To update evidence custom fields you should lowercase them and remove all spaces. For example: Scan IP -> scanip

**Parameters:** None

**Returns:** List[types.TextContent]: The new / updated Evidence

---

### `xsoar_search_evidence`

Search for an evidence entutiy by filter

**Parameters:** None

**Returns:** List[types.TextContent]: EvidencesSearchResponse

---

### `xsoar_update_entry_note`

API to mark entry as note, can be used also to remove the note Body example: {"id":1\@1234","version":"-1","investigationId":"1234","data":"true/false"}

**Parameters:** None

**Returns:** List[types.TextContent]: Entry

---

### `xsoar_update_entry_tags_op`

API to set entry tags Body example: {"id":"1\@1234","version":"-1","investigationId":"1234","tags":["tag1","tag2"]"}

**Parameters:** None

**Returns:** List[types.TextContent]: Entry

---

