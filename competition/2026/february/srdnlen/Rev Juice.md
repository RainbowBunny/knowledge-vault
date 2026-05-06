---
type: challenge
event: <% tp.user.grandparent(tp) %>
name: <% tp.file.title %>
category: <% tp.file.folder(0) %>
note:
solved: ❌✅
---



```
[ YOU ]
  │
  ▼
[ selector ] ──► ENABLE bits (which product is active)
  │
  ├──► SELECT (which product index)
  └──► CANCEL_OUT
        │
        ▼
[ money_manager ] ──► COINS_INSERTED
        │
        ▼
[ multiplexer ] ──► COST_SELECTED, RESULT_SELECTED
        │
        ▼
[ product modules ]
```