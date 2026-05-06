---
type: challenge
event: amateurs
name: Easy Bof
category: pwn
note: "[[Binary Exploitation]]"
solved: ❌
---


Source code:

```c
#include <stdio.h>
#include <stdlib.h>

void win() { system("sh"); }

int main() {
  char buf[0x100];
  size_t size;
  
  setbuf(stdout, NULL);
  
  printf("how much would you like to write? ");
  scanf("%ld", &size);
  getchar();
  fgets(buf, size, stdin);
}
```

Target: Call `win` function.

Checksec:

```
    Arch:       amd64-64-little
    RELRO:      Partial RELRO
    Stack:      No canary found
    NX:         NX enabled
    PIE:        No PIE (0x400000)
    Stripped:   No
```

In the assembly code, we can see:

```asm
	PUSH rbp
	MOV rbp, rsp
	SUB rsp, 0x110
```

Additionally, we have the `fgets` function:

```
	MOV rdx, qword ptr [stdin]
	MOV rax, qword ptr [RBP + local_110]
	MOV ecx, eax
	LEA rax, [RBP - 0x100]
	MOV esi, ecx
	MOV rdi, rax
	CALL <EXTERNAL>::fgets
```



