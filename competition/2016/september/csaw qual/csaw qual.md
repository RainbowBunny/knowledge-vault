---
type: ctf
event: csaw qual
date: 2025-12-05T18:52
---


```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


