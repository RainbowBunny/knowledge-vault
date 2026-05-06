---
type: challenge
event: september
name: kvm
category: rev
note:
solved: ✅
---

**Part 1:** Find `DAT_00302174` to get the run_vm script. After extracting this we have a small binary.

**Part 2:** We can see the small binary have some missing part by random `HALT` operation, to analyze this, we come back to the original challenge ELF and we see that:

```c
if (ioctl(vcpu->fd, KVM_GET_REGS, &regs) < 0) {
      perror("KVM_GET_REGS");
      exit(1);
    }
    if (regs.rax != 0) {
      OBF o = find_OBF(regs.rax);
      regs.rip = o.a;
      if (ioctl(vcpu->fd, KVM_SET_REGS, &regs) < 0) {
        perror("KVM_SET_REGS");
        exit(1);
      }
    } else
      break;
```

So we can understand that before the `HALT` operation, there is a `MOVE rax` operation, so we can understand that this equals a `JUMP` operation (there is a map `RAX -> RIP`). This map can be found by `DAT_003020a0`.

**Part 3:** After recovered the binary, we can see the encryption of the flag and find it.