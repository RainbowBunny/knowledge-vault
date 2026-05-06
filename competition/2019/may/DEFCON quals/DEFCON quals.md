---
type: ctf
event: DEFCON quals
date: 2025-12-10T21:43
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


