---
type: ctf
event: csaw qual
date: 2025-12-02T10:17
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


