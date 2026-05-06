---
type: challenge
event: glacier
name: csprw
category: crypto
note: Linear feedback shift register (LFSR)-like construction
solved: ✅
---
```python
#!/usr/bin/env python3
from pwn import *
from z3 import *

# context.log_level = 'debug'

def solve():
    # r = process(['python3', 'challenge'])
    r = remote('challs.glacierctf.com', 13375)

    r.recvuntil(b"new-comer goodies.\n")

    s = Solver()
    state = BitVec('state', 64)

    # We need to keep track of the state as it evolves
    current_state = state

    TAGS = ["crypto", "misc", "pwn", "rev", "web"]
    # We will play "crypto" (index 0) for the first 100 rounds

    my_move_idx = 0
    my_move_str = TAGS[my_move_idx]

    print("Collecting 100 samples...")
    for i in range(100):
        r.recvuntil(b": ")
        r.sendline(my_move_str.encode())

        res = r.recvline().strip().decode()

        # current_state & 0xf
        val = current_state & 0xf
        # We need to be careful with modulo in Z3.
        # URem is unsigned remainder.
        comp_choice = URem(val, 5)

        if res == "tie":
            # Computer chose same as us: 0
            s.add(comp_choice == 0)
        elif res == "win":
            # We won. We played 0.
            # 0 beats 1 and 3.
            s.add(Or(comp_choice == 1, comp_choice == 3))
        elif res == "lose":
            # We lost. We played 0.
            # 0 loses to 2 and 4.
            s.add(Or(comp_choice == 2, comp_choice == 4))
        else:
            print(f"Unexpected result: {res}")
            return

        # Update state 4 times
        for _ in range(4):
            bit = (current_state ^ LShR(current_state, 3) ^ LShR(current_state, 7)) & 1
            current_state = LShR(current_state, 1) | (bit << 63)

    print("Solving for state...")
    if s.check() == sat:
        print("SAT!")
        m = s.model()
        init_state = m[state].as_long()
        print(f"Initial state: {init_state}")

    else:
        print("UNSAT")
        return

    # Reconstruct the state evolution to get to the current point
    curr = init_state
    # Fast forward 100 rounds
    for i in range(100):
        # yield state & 0xf (we don't need this value now)
        for _ in range(4):
            bit = (curr ^ (curr >> 3) ^ (curr >> 7)) & 1
            curr = (curr >> 1) | (bit << 63)

    print("Predicting next 200 rounds...")
    for i in range(200):
        # Predict computer move
        val = curr & 0xf
        comp_choice = val % 5
        # We need to beat comp_choice
        # If comp_choice is C, we need P such that P beats C.
        # P = (C - 1) % 5 works.
        my_win_idx = (comp_choice - 1) % 5
        my_win_str = TAGS[my_win_idx]
        r.recvuntil(b": ")
        r.sendline(my_win_str.encode())
        res = r.recvline().strip().decode()

        # print(f"Round {i+1}: Played {my_win_str} vs {TAGS[comp_choice]} -> {res}")
        if res != "win":
            print(f"Failed at round {i+1}. Expected win, got {res}")
            # return

        # Update state
        for _ in range(4):
            bit = (curr ^ (curr >> 3) ^ (curr >> 7)) & 1
            curr = (curr >> 1) | (bit << 63)

    # Get flag

    print(r.recvall().decode())

if __name__ == "__main__":
    solve()
```

