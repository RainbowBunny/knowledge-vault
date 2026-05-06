---
type: challenge
event: csaw qual
name: evidence.zip
category: forensics
note:
solved: ✅
---
After the signature (`PK\x01\x02`), there are exactly `24` extra bytes inserted before the correct entry data. Looking a little closer, you can see the flag in plaintext broken up across the extra bytes in every entry:
```
00001600: 4101 6761 6c66 ffff ffff ffff ffff 0e00  A.galf.......... => "flag"
00001650: 4101 3368 747b ffff ffff ffff ffff 0e00  A.3ht{.......... => "{th3"
000016A0: ...
```


