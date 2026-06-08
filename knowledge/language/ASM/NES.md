---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-11-23T19:57
---
`PPU_STATUS`:
- Address: `$2002`
- Layout:

| Bit | Meaning                            |
| --- | ---------------------------------- |
| 7   | VBlank flag (1 when VBlank starts) |
| 6   | Sprite 0 hit                       |
| 5   | Sprite overflow                    |
| 4-0 | Misc internal PPU flags            |
