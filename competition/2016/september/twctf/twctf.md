---
type: ctf
event: twctf
date: 2026-01-02T19:29
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


