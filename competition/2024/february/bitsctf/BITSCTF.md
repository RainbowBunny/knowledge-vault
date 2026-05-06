---
type: ctf
event: BITSCTF
date: 2026-02-16T17:19
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```



