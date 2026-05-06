---
type: ctf
event: LilacCTF
date: 2026-01-25T22:19
---


```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


