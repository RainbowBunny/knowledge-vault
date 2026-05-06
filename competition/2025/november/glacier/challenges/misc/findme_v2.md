---
type: challenge
event: glacier
name: findme_v2
category: misc
note: "[[findme_v2#PDF]]"
solved: ✅
---
The target stream is at `0xad46`.
We can find hidden stream by `Cyberchef > Scan for Embedded Files`
Find the length of the stream:
```
0000ad10: 3133 3020 3020 6f62 6a0a 3c3c 2f46 696c  130 0 obj.<</Fil
0000ad20: 7465 722f 466c 6174 6544 6563 6f64 652f  ter/FlateDecode/
0000ad30: 4c65 6e67 7468 2034 3935 3930 3e3e 0a73  Length 49590>>.s
```

```python
data = open("chall.pdf", "rb").read()[0xad46 : 0xad46 + 49590]
open("s_0xad46.zlib", "wb").write(data)
```
Then
```bash
zlib-flate -uncompress < s_0xad46.zlib > out.png
```
