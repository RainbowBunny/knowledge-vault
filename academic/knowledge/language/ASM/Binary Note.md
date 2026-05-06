---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-12-10T18:44
---
## GOT

The **GOT (Global Offset Table)** stores _runtime-resolved_ addresses of external functions.
Before resolution:
- GOT entry for `puts` = pointer to resolver stub
After lazy-binding:
- GOT entry for `puts` = real address of `puts` inside libc

## PLT

The **PLT (Procedure Linkage Table)** is a set of small stubs inside the program used to call external library functions _indirectly_.
The PLT stub handles:
1. Lazy binding (first-time resolution)
2. Indirect jump to the real function in libc
3. Jump through the GOT entry


## ASLR



## PIE


## NX


