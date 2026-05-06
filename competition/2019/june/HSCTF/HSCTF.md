---
type: ctf
event: HSCTF
date: 2026-01-02T11:00
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


