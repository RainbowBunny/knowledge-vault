---
type: ctf
event: <% tp.file.title %>
date: 2026-02-14T08:05
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


