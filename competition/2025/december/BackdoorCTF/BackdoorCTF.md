---
type: ctf
event: BackdoorCTF
date: 2025-12-06T20:27
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


