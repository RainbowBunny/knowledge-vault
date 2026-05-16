
**Intrinsics**: C/C++ wrapper around special hardware instructions.

## Registers

### Vector Data Registers

|         |                           |
| ------- | ------------------------- |
| `.b`    | signed byte               |
| `.ub`   | unsigned byte             |
| `.h`    | signed halfword           |
| `.uh`   | unsigned halfword         |
| `.w`    | for signed word           |
| `.uw`   | unsigned halfword         |
| `.qf16` | 16-bit HVX floating point |
| `.qf32` | 32-bit HVX floating point |
| `.hf`   | Half precision            |
| `.sf`   | single precision          |


> [!remark]
> HVX coprocessor contains 32 vector registers (V0 -> V31). These registers store operand data for the vector instructions.
> These vector registers can be treated as a vector pair by the operand `V5:4` or reverse order `V4:5`, it must be align so that the hardware can unpack easily.

> [!remark] VRF to GRF transfers
> Transfer values between **vector register file (VRF)** and **general register file (GRF)**, as the vector register should only be used in holding intermediate vector computation results. Thus, these operation will slow down the computation significantly and is advised to use only for debugging. 

| Syntax                    | Behavior                           | Description |
| ------------------------- | ---------------------------------- | ----------- |
| `RD.w = extractw(Vu, Rs)` | `RD = Vu.uw[Rs & 0xF]`             |             |
| `Vx.w = insertw(Rss)`     | `Vx.uw[Rss.w[1] & 0xF] = Rss.w[0]` |             |

### Vector predicate registers

> [!remark]
> These vectors hold the result of vector compare instructions, 1 byte result are stored by 1 bit and thus we have 1 byte = 1 bit, 1 half-word = 2 bits, 1 word = 4 bits.

## Instruction

`Q6`: Version
`Vh`: Vector Half
`R`: Rotate amount after getting the result

|                   |                        |
| ----------------- | ---------------------- |
| `Q6_Vh_vadd_VhVh` |                        |
| `Q6_Vh_vsub_VhVh` |                        |
| `Q6_Vh_vmax_VhVh` |                        |
| `Q6_Vw_vasl_VwR`  | Arithmetic shift left  |
| `Q6_Vw_vlsr_VwVw` | Logical shift right    |
| `Q6_V_vror_VR`    | Rotate                 |
| `Q6_W_vdeal_VVR`  | Concatenate and deal   |
| `Q6_Vh_vdeal_Vh`  | Deal by odd even index |
