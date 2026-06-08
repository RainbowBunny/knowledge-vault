---
parent: "[[Fleeting MOC]]"
tags:
- 🪴weedy
date: 2025-11-23T08:43
---
## Registers

**Registers**

| **Register**         | Size (bit) | Purpose                                                                                                                                                                                                                                                                                                                                          |
| -------------------- | ---------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Accumulator (A)      | 8          | Used to perform calculations on data.  <br>Most instructions can operate directly on the accumulator instead of spending CPU cycles to access memory.                                                                                                                                                                                            |
| X register (X)       | 8          | Used as an index in some addressing modes.                                                                                                                                                                                                                                                                                                       |
| Y register (Y)       | 8          | Used as an index in some addressing modes.                                                                                                                                                                                                                                                                                                       |
| Program Counter (PC) | 16         | Points to the address of the next instruction to be executed.                                                                                                                                                                                                                                                                                    |
| Stack Pointer (S)    | 8          |                                                                                                                                                                                                                                                                                                                                                  |
| Status (P)           | 8          | Each bit represents a status flag.<br><br>Flags indicate the state of the CPU, or information about the result of the previous instruction. PHP and PLP can save/restore P from the stack. Various instructions can directly set or clear bits in P: SEC, CLC, SEI, CLI, SED, CLD, CLV.  <br>See the table below for a description of each flag. |

**Status Flags**:

| Bit | Symbol | Name              | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| --- | ------ | ----------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 7   | `N`    | Negative          | Set if the result was negative, i.e. bit 7 of the result was set.  <br><br>`BIT`: Set to bit 7 of the input.<br><br>NOTE: Compare (CMP, CPX, CPY) instructions work by subtracting, but not keeping the result.                                                                                                                                                                                                                                                                       |
| 6   | `V`    | Overflow          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 5   | -      | (Unused)          | Always set                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| 4   | `B`    | Break             | Set if an interrupt request has been triggered by a `BRK` instruction                                                                                                                                                                                                                                                                                                                                                                                                                 |
| 3   | `D`    | Decimal           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 2   | `I`    | Interrupt Disable | Disables IRQ interrupts while set. NMIs and RESETs are not affected.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 1   | `Z`    | Zero              | `Compare`: Set if the register's value is equal to the input value.<br><br>`BIT`: Set if the result of logically ANDing the accumulator with the input results in 0.<br><br>Otherwise: Set if result was zero.<br><br>NOTE: Compare (CMP, CPX, CPY) instructions work by subtracting, but not keeping the result.                                                                                                                                                                     |
| 0   | `C`    | Carry             | Carry/Borrow flag used in math and rotate operations<br><br>Arithmetic: Set if an unsigned overflow occurred during addition or subtraction, i.e. the result is less than the initial value (or equal to the initial value, if the carry flag was set going in)<br><br>Compare: Set if register's value is greater than or equal to the input value<br><br>Shifting: Set to the value of the eliminated bit of the input, i.e. bit 7 when shifting left, or bit 0 when shifting right |
## Memory Addressing Modes


| Mode     | Name                              | Explaination                                                                                                                                                                                                                                                                                                                   |
| -------- | --------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `A`      | Accumulator                       | The Accumulator is implied as the operand, so no address needs to be specified.                                                                                                                                                                                                                                                |
| `i`      | Implied                           | The operand is implied, so it does not need to be specified.                                                                                                                                                                                                                                                                   |
| `#`      | Immediate                         | The operand is used directly to perform the computation.                                                                                                                                                                                                                                                                       |
| `a`      | Absolute                          | A full 16-bit address is specified and the byte at that address is used to perform the computation.                                                                                                                                                                                                                            |
| `zp`     | Zero Page                         | A single byte specifies an address in the first page of memory (`$00xx`), also known as the zero page, and the byte at that address is used to perform the computation.                                                                                                                                                        |
| `r`      | Relative                          | The offset specified is added to the current address stored in the Program Counter (PC). Offsets can range from -128 to +127.                                                                                                                                                                                                  |
| `(a)`    | Absolute Indirect                 | The little-endian two-byte value stored at the specified address is used to perform the computation. Only used by the `JMP` instruction.                                                                                                                                                                                       |
| `a,x`    | Absolute Indexed with X           | The value in `X` is added to the specified address for a sum address. The value at the sum address is used to perform the computation.                                                                                                                                                                                         |
| `a,y`    | Absolute Indexed with Y           | The value in `Y` is added to the specified address for a sum address. The value at the sum address is used to perform the computation.                                                                                                                                                                                         |
| `zp,x`   | Zero Page Indexed with X          | The value in `X` is added to the specified zero page address for a sum address. The value at the sum address is used to perform the computation.                                                                                                                                                                               |
| `zp,y`   | Zero Page Indexed with Y          | The value in `Y` is added to the specified zero page address for a sum address. The value at the sum address is used to perform the computation.                                                                                                                                                                               |
| `(zp,x)` | Zero Page Indexed Indirect        | The value in `X` is added to the specified zero page address for a sum address. The little-endian address stored at the two-byte pair of sum address (LSB) and sum address plus one (MSB) is loaded and the value at that address is used to perform the computation.                                                          |
| `(zp),y` | Zero Page Indirect Indexed with Y | The value in `Y` is added to the address at the little-endian address stored at the two-byte pair of the specified address (LSB) and the specified address plus one (MSB). The value at the sum address is used to perform the computation. Indeed addressing mode actually repeats exactly the Accumulator register's digits. |
## Instruction

### Load and Store

| Instruction | Briefly                      | Operation | Flag affected |
| ----------- | ---------------------------- | --------- | ------------- |
| LDA         | Load Accumulator with Memory | `A = M`   | `N`, `Z`      |
| LDX         | Load Index X with Memory     | `X = M`   | `N`, `Z`      |
| LDY         | Load Index Y with Memory     | `Y = M`   | `N`, `Z`      |
| STA         | Store Accumulator in Memory  | `M = A`   | None          |
| STX         | Store Index X in Memory      | `M = X`   | None          |
| STY         | Store Index Y in Memory      | `M = Y`   | None          |

### Arithmetic

| Instruction | Briefly                                      | Operation        | Flag affected      |
| ----------- | -------------------------------------------- | ---------------- | ------------------ |
| ADC         | Add Memory to Accumulator with Carry         | `A = A + M + C`  | `N`, `V`, `Z`, `C` |
| SBC         | Subtract Memory from Accumulator with Borrow | `A = A - M - ~C` | `N`,`V`, `Z`, `C`  |

### Increment and Decrement

**Increment Index X by One**: INX 
Flags affected: `N, Z`

| Instruction | Briefly                        | Operation | Flag affected |
| ----------- | ------------------------------ | --------- | ------------- |
| CMP         | Compare Memory and Accumulator | `A - M`   | `N`, `Z`, `C` |
| CPX         | Compare Memory and Index X     | `X - M`   | `N`, `Z`, `C` |
| CPY         | Compare Memory and Index Y     | `Y - M`   | `N`, `Z`, `C` |
### Shift and Rotate

### Logic

| Instruction | Briefly                              | Operation      | Flag affected |
| ----------- | ------------------------------------ | -------------- | ------------- |
| AND         | AND Memory with Accumulator          | `A = (A & M)`  | `N`, `Z`      |
| ORA         | OR Memory with Accumulator           | `A = (A \| M)` | `N`, `Z`      |
| EOR         | Exclusive-OR Memory with Accumulator | `A = (A ^ M)`  | `N`, `Z`      |

### Compare and Test Bit

| Instruction | Briefly                        | Operation | Flag affected |
| ----------- | ------------------------------ | --------- | ------------- |
| CMP         | Compare Memory and Accumulator | `A - M`   | `N`, `Z`, `C` |
| CPX         | Compare Memory and Index X     | `X - M`   | `N`, `Z`, `C` |
| CPY         | Compare Memory and Index Y     | `Y - M`   | `N`, `Z`, `C` |

### Branch

| Instruction | Briefly                   | Check             |
| ----------- | ------------------------- | ----------------- |
| BCC         | Branch on Carry Clear     | Branch if `C = 0` |
| BCS         | Branch on Carry Set       | Branch if `C = 1` |
| BNE         | Branch on Result not Zero | Branch if `Z = 0` |
| BEQ         | Branch on Result Zero     | Branch if `Z = 1` |

### Transfer

| Instruction | Briefly                           | Action  | Flags    |
| ----------- | --------------------------------- | ------- | -------- |
| TAX         | Transfer Accumulator to Index X   | `X = A` | `N`, `Z` |
| TXA         | Transfer Index X to Accumulator   | `A = X` | `N`, `Z` |
| TAY         | Transfer Accumulator to Index Y   | `Y = A` | `N`, `Z` |
| TYA         | Transfer Index Y to Accumulator   | `A = Y` | `N`, `Z` |
| TSX         | Transfer Stack Pointer to Index X | `S = X` | `N`, `Z` |
| TXS         | Transfer Index X to Stack Pointer | `X = S` | None     |

### Stack

| Instruction | Briefly                     | Action        | Flags    |
| ----------- | --------------------------- | ------------- | -------- |
| PHA         | Push Accumulator on Stack   | `S.push(A)`   | None     |
| PLA         | Pull Accumulator from Stack | `A = S.pop()` | `N`, `Z` |

### Subroutines and Jump

| Instruction | Briefly                                    | Action                                                                                                                                                                                                                                                                          | Flags |
| ----------- | ------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| JMP         |                                            |                                                                                                                                                                                                                                                                                 |       |
| JSR         | Jump to New Location Saving Return Address | The address before the next instruction `(PC - 1)` is pushed onto the stack: first the upper byte followed by the lower byte. As the stack grows backwards, the return address is therefore stored as a little-endian number in memory.  <br>`PC` is set to the target address. | None  |
| RTS         | Return from Subroutine                     | Return from a subroutine to the point where it called with `JSR`.<br><br>The return address is popped from the stack (low byte first, then high byte).  <br>The return address is incremented and stored in PC.                                                                 | None  |

### Set and Clear

| Instruction | Briefly                        | Flags |
| ----------- | ------------------------------ | ----- |
| CLC         | Clear Carry Flag               | C = 0 |
| SEC         | Set Carry Flag                 | C = 1 |
| CLD         | Clear Decimal Mode             | D = 0 |
| SED         | Set Decimal Mode               | D = 1 |
| CLI         | Clear Interrupt Disable Status | I = 0 |
| SEI         | Set Interrupt Disable Status   | I = 1 |
| CLV         | Clear Overflow Flag            | V = 0 |

## Miscellaneous

| CPU Addr | Register  | Purpose                           |
| -------- | --------- | --------------------------------- |
| `$2000`  | PPUCTRL   | Enable NMI, pattern table select  |
| `$2001`  | PPUMASK   | Rendering enable                  |
| `$2002`  | PPUSTATUS | Status flags (VBlank, sprite hit) |
| `$2003`  | OAMADDR   | Sprite memory address             |
| `$2004`  | OAMDATA   | Sprite data                       |
| `$2005`  | PPUSCROLL | Scrolling                         |
| `$2006`  | PPUADDR   | VRAM address                      |
| `$2007`  | PPUDATA   | Read/write VRAM                   |