---
type: ctf
event: bitsctf
date: 2026-02-20T22:36
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


