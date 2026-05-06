---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-11-26T19:45
---
## Data Types

For an instruction, we have:
- `s`: signed
- `h`: half words
- `b`: bytes

```
                           00000000 : byte
                  00000000 00000000 : half word
00000000 00000000 00000000 00000000 : word
```

## ARM Registers

Register lists:

| Registers | Alias | Purpose                                |
| --------- | ----- | -------------------------------------- |
| `R0-R6`   | -     | General purpose                        |
| `R7`      | -     | Holds Syscall Number                   |
| `R8-R10`  | -     | General purpose                        |
| `R11`     | `FP`  | Frame Pointer                          |
| `R12`     | `IP`  | Intra Procedural Call                  |
| `R13`     | `SP`  | Stack Pointer                          |
| `R14`     | `LR`  | Link Register                          |
| `R15`     | `PC`  | Program Counter                        |
| `CPSR`    | -     | Current Program Status Register (Flag) |

Register `CPSR`:

| Flag                                  | Bit   | Description                                                                                                               |
| ------------------------------------- | ----- | ------------------------------------------------------------------------------------------------------------------------- |
| `N` (Negative)                        | 31    | Enabled if result of the instruction yields a negative number                                                             |
| `Z` (Zero)                            | 30    | Enabled if result of the instruction yields a zero value                                                                  |
| `C` (Carry)                           | 29    | Enabled if result of the instruction yields a value that requires a 33rd bit to be fully represented                      |
| `V` (Overflow)                        | 28    | Enabled if result of the instruction yields a value that cannot be represented in 32 bit two’s complement                 |
| `Q` (Underflow)                       | 27    | Saturation / sticky overflow flag — used in saturating arithmetic / DSP / SIMD instructions                               |
| `J` (Jazelle)                         | 24    | Third execution state that allows some ARM processors to execute Java bytecode in hardware                                |
| `GE` (Greater than or Equal for SIMD) | 19-16 | Compare flag for parallel computation                                                                                     |
| `E` (Endianness)                      | 9     | ARM can operate either in little endian, or big endian. This bit is set to 0 for little endian, or 1 for big endian mode. |
| `A` (Abort disable)                   | 8     | Imprecise data abort disable                                                                                              |
| `I` (IRQ disable)                     | 7     | Mask/disable standard interrupts                                                                                          |
| `F` (FIQ disable)                     | 6     | Mask/disable fast interrupts                                                                                              |
| `T` (Thumb)                           | 5     | This bit is set if you are in Thumb state and is disabled when you are in ARM state.                                      |
| `M` (privilege mode)                  | 4-0   | These bits specify the current privilege mode (USR, SVC, etc.).                                                           |

## ARM & Thumb

Thumb is another instructions set that have a `.w` suffix.

Template of operation:

```
MNEMONIC{S}{condition} {Rd}, Operand1, Operand2
```

Explaination:

| Component     | Meaning                                                                                               |
| ------------- | ----------------------------------------------------------------------------------------------------- |
| `NMEMONIC`    | Short name (mnemonic) of the instruction                                                              |
| `{S}`         | An optional suffix. If S is specified, the condition flags are updated on the result of the operation |
| `{condition}` | Condition that is needed to be met in order for the instruction to be executed                        |
| `{Rd}`        | Register (destination) for storing the result of the instruction                                      |
| `Operand1`    | First operand. Either a register or an immediate value                                                |
| `Operand2`    | Second (flexible) operand. Can be an immediate value (number) or a register with an optional shift    |

Most common instruction:

| Instruction | Description                   |
| ----------- | ----------------------------- |
| `MOV`       | Move data                     |
| `MVN`       | Move and negate               |
| `ADD`       | Addition                      |
| `SUB`       | Subtraction                   |
| `MUL`       | Multiplication                |
| `LSL`       | Logical Shift Left            |
| `LSR`       | Logical Shift Right           |
| `ASR`       | Arithmetic Shift Right        |
| `ROR`       | Rotate Right                  |
| `CMP`       | Compare                       |
| `AND`       | Bitwise AND                   |
| `ORR`       | Bitwise OR                    |
| `EOR`       | Bitwise XOR                   |
| `LDR`       | Load                          |
| `STR`       | Store                         |
| `LDM`       | Load Multiple                 |
| `STM`       | Store Multiple                |
| `PUSH`      | Push on Stack                 |
| `POP`       | Pop off Stack                 |
| `B`         | Branch                        |
| `BL`        | Branch with Link              |
| `BX`        | Branch and eXchange           |
| `BLX`       | Branch with Link and eXchange |
| `SWI/SVC`   | System Call                   |
