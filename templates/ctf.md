---
type: ctf
event: <% tp.file.title %>
date: {{date:YYYY-MM-DD}}T{{time:HH:mm}}
---

```dataview
TABLE category, note, solved
WHERE contains(file.folder, this.file.folder + "/challenges")
  AND type = "challenge"
SORT category ASC
```


