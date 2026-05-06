---
type: ctf
event: <% tp.file.title %>
date: 2025-12-02T08:49
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```




