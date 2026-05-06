---
type: ctf
event: Insomni'hack teaser
date: 2025-12-24T21:18
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


