---
type: ctf
event: Facebook CTF
date: 2026-01-01T17:28
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


