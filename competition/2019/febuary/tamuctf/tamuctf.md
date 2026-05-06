---
type: ctf
event: tamuctf
date: 2025-12-05T10:01
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


