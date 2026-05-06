---
type: challenge
event: csaw qual
name: brainfun
category: forensics
note: "[[Steganography#PNG]]"
solved: ✅
---


```python
from PIL import Image
im = Image.open('brainfun.png')
pixels = []
for row in xrange(32):
    pixel_row = []
    for column in xrange(32):
        pixel_row.append(im.getpixel((16*column,16*row)))
    pixels.append(pixel_row)

rgb = 4096*[0] # 16^3 because each of R, G, and B have 16 possible values
for row in pixels:
    for (r,g,b,a) in row:
		index = 16*r+g+b/16
		rbg[index] = chr(a)
```

