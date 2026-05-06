---
type: challenge
event: amateurs
name: Uwa so Piano
category: misc
note: "[[Steganography#midi|midi]]"
solved: ✅
---


After reading the file, the velocity parameters are the flag.

```python
import re

with open('result.txt', 'r') as file:
    data = file.readlines()

flags = []

for line in data:
    if "velocity" in line and "note_on" in line:
        velocity_match = re.search(r'velocity=(\d+)', line)
        if velocity_match:
            velocity_value = int(velocity_match.group(1))
            flags.append(chr(velocity_value))

print(''.join(flags))
```

