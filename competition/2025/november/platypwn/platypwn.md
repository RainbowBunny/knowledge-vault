---
type: ctf
event: platypwn
date: 2025-12-22T23:24
---




```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


