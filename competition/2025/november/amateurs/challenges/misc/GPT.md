---
type: challenge
event: amateurs
name: GPT
category: misc
note: Padding of base64s
solved: ✅
---

Idea: Base64 is a mapping between group of 3 bytes (`8 x 3 = 24` bit) to group of 4 base64 characters (`6 x 4 = 24`).

However, there is a special case where the length of the sequence is not divisible by 3:
- `Length % 3 = 1`: Adds 2 equal characters and has 4 unused bit.
- `Length % 3 = 2`: Adds 1 equal character and has 2 unused bit.

