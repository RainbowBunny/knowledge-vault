---
type: challenge
event: february
name: El Diablo
category: rev
note:
solved: ✅
---
First, because of `upx`, we find that the binary is packed by `upx`.
After packing, we find that there is a suspicious call in `main` that did not get disassembly by IDA: 

```
text:00000000000031D3                 call    sub_3851
```

Now, we want to understand the structure of the vm:





| **Offset**    | **Purpose**                                                  |
| ------------- | ------------------------------------------------------------ |
| `0x00 - 0x9F` | **General Purpose Registers** (10 registers x 16 bytes each) |
| `0xA0`        | **Program Counter (PC)**                                     |
| `0xA8`        | **Bytecode Buffer Pointer**                                  |
| `0xB0`        | **Bytecode Size**                                            |
| `0x18C4`      | **VM State / Execution Flag**                                |

| **Offset**  | **Size**   | **Purpose**                                     |
| ----------- | ---------- | ----------------------------------------------- |
| `0x00`      | 160 bytes  | **Registers** (10 regs × 16 bytes)              |
| `Reg + 0x0` | 8 bytes    | Registers data                                  |
| `Reg + 0x8` | 4 bytes    | Type tag (0 = Integer, 1 = Pointer)             |
| `Reg + 0xC` | 4 bytes    | Padding                                         |
| `0xA0`      | 2 bytes    | **Internal State/Flags**                        |
| `0xA4`      | 4 bytes    | **Program Counter (PC)**                        |
| `0xA8`      | 8 bytes    | **Pointer to Bytecode Buffer**                  |
| `0xB0`      | 4 bytes    | **Bytecode Size**                               |
| `0xB8`      | 8 bytes    | Error fall back<br>Susge?                       |
| `0xC0`      | 2048 bytes | **Opcode Dispatch Table** (256 slots × 8 bytes) |
| `0x8C0`     |            | Stack                                           |
| `0x18C0`    | 4 bytes    | Stack size                                      |
| `0x18C4`    | 2 bytes    | **Running Flag** (Set to 1 earlier)             |


| Opcode | Name                     | Parameters                                                            | Description                                 |
| ------ | ------------------------ | --------------------------------------------------------------------- | ------------------------------------------- |
| `0x00` | `halt`                   |                                                                       | Set `flag` to `0`                           |
| `0x01` | `load_int_32`            | `1 byte register R1`<br>`2 bytes number`                              | `R1 = number`                               |
| `0x02` | `print_hex`              | `1 byte register`                                                     |                                             |
| `0x03` | `convert_int_to_string`  | `1 byte register`                                                     |                                             |
| `0x04` | `generate_random`        | `1 byte register R1`                                                  | `R1 = rand()`                               |
| `0x10` | `jump_address`           | `2 bytes address`                                                     |                                             |
| `0x12` | `jump_if_zero`           | `2 bytes address`                                                     | Check `flag = 0`                            |
| `0x11` | `jump_if_not_zero`       | `2 bytes address`                                                     | Check `flag != 0`                           |
| `0x21` | `add`                    | `3 registers R1, R2, R3`                                              | `R1 = R2 + R3`<br>Update `flag = (R1 == 0)` |
| `0x27` | `and`                    | `3 registers R1, R2, R3`                                              | `R1 = R2 & R3`<br>Update `flag = (R1 == 0)` |
| `0x22` | `sub`                    | `3 registers R1, R2, R3`                                              | `R1 = R2 - R3`<br>Update `flag = (R1 == 0)` |
| `0x23` | `mul`                    | `3 registers R1, R2, R3`                                              | `R1 = R2 * R3`<br>Update `flag = (R1 == 0)` |
| `0x24` | `div`                    | `3 registers R1, R2, R3`                                              | `R1 = R2 / R3`<br>Update `flag = (R1 == 0)` |
| `0x20` | `xor`                    | `3 registers R1, R2, R3`                                              | `R1 = R2 ^ R3`<br>Update `flag = (R1 == 0)` |
| `0x28` | `or`                     | `3 registers R1, R2, R3`                                              | `R1 = R2 \| R3`                             |
| `0x25` | `inc`                    | `1 register R1`                                                       | `R1++`<br>Update `flag = (R1 == 0)`         |
| `0x26` | `dec`                    | `1 register R1`                                                       | `R1--`<br>Update `flag = (R1 == 0)`         |
| `0x30` | `load_string_literal`    | `1 register R1`<br>`2 bytes for string length l`<br>`string length l` | `R1 = string`                               |
| `0x31` | `print_string`           | `1 register R1`                                                       |                                             |
| `0x32` | `add_string`             | `3 registers R1, R2, R3`                                              | `R1 = R2 + R3`                              |
| `0x33` | `system`                 | `1 register R1`                                                       | Run `system R1`                             |
| `0x34` | `string_to_int`          | `1 register R1`                                                       |                                             |
| `0x40` | `string_compare`         | `2 registers R1, R2`                                                  | `flag = (R1 == R2)`                         |
| `0x41` | `compare_int_literal`    | `1 register`<br>`2 bytes number`                                      | `flag = (R1 == number)`                     |
| `0x42` | `compare_string_literal` | `1 register R1`<br>`2 bytes string length l`<br>`string length l`     | `flag = (R1 == l)`                          |
| `0x43` | `is_string`              | `1 register R1`                                                       | `flag = (R1 is string)`                     |
| `0x44` | `is_int`                 | `1 register R1`                                                       | `flag = (R1 is integer)`                    |
| `0x50` | `nop`                    |                                                                       |                                             |
| `0x51` | `set`                    | `2 registers R1, R2`                                                  | `R1 = R2`                                   |
| `0x60` | `load_register`          | `2 registers R1, R2`                                                  | `R1 = [R2]`                                 |
| `0x61` | `write_register`         | `2 registers R1, R2`                                                  | `[R2] = R1`                                 |
| `0x62` | `buf_copy`               | `3 registers R1, R2, R3`                                              | Copy `R3` bytes from `[R2]` to `[R1]`       |
| `0x70` | `push`                   | `1 register R1`                                                       |                                             |
| `0x71` | `pop`                    | `1 register R1`                                                       | `R1 = pop(stack)`                           |
| `0x72` | `ret`                    |                                                                       | `PC = pop(stack)`                           |
| `0x73` | `call`                   | `2 bytes address`                                                     | push `PC + 1`<br>`PC = address`             |
| `0x82` | `get_liscense`           | `2 registers R1, R2`                                                  | `R1 = LISCENSE[R2]`                         |
| `0x84` | `print_flag`             | `1 register R1`                                                       | `putchar(R1)`                               |

`DAT_0010c290 = 0xA62373A7702931C7` generated by the debug detection part.
`DAT_0010c2a0` is created by `generate_c2a0`.