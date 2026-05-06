---
type: challenge
event: glacier
name: awesomeness
category: rev
note:
solved: ❌
---

## Codeblock

### Reset

```asm
  sei                            ; $8000  78
  lda #$00                       ; $8001  A9 00
  sta PPU_CTRL                   ; $8003  8D 00 20
  sta PPU_MASK                   ; $8006  8D 01 20
  sta APU_SND_CHN                ; $8009  8D 15 40
  sta APU_DMC_FREQ               ; $800C  8D 10 40
  lda #$40                       ; $800F  A9 40
  sta APU_FRAME                  ; $8011  8D 17 40
  cld                            ; $8014  D8
  ldx #$FF                       ; $8015  A2 FF
  txs                            ; $8017  9A
  bit PPU_STATUS                 ; $8018  2C 02 20
```

`sei`: SEt Interrupt disable (flag `I = 1`)

```asm
  lda #$00                       ; $8001  A9 00
  sta PPU_CTRL                   ; $8003  8D 00 20
  sta PPU_MASK                   ; $8006  8D 01 20
  sta APU_SND_CHN                ; $8009  8D 15 40
  sta APU_DMC_FREQ               ; $800C  8D 10 40
```

Set `A = 0` then set constant `PPU_CTRL, PPU_MASK, APU_SND_CHN, APU_DMC_FREQ = 0`.

```asm
  lda #$40                       ; $800F  A9 40
  sta APU_FRAME                  ; $8011  8D 17 40
```

Set `A = 40` then set constant `APU_FRAME = 40`

`cld`: CLear Decimal mode (flag `D = 1`)

`ldx #$FF`: `X = 0xFF`.

`txs`: Set stack pointer `SP = 0xFF`

`bit`: 
- `Z = A & PPU_STATUS`
- `V = PPU_STATUS[6]`
- `N = PPU_STATUS[7]`
#### label_801b

```asm
  bit PPU_STATUS                 ; $801B  2C 02 20
  bpl _label_801b                ; $801E  10 FB
  lda #$00                       ; $8020  A9 00
  ldx #$00                       ; $8022  A2 00
```

`bit`: 
- `Z = A & PPU_STATUS`
- `V = PPU_STATUS[6]`
- `N = PPU_STATUS[7]`
`bpl`: Branch if `N = 0` then return to the beginning of the loop so:
```c
while ((PPU_STATUS & 0x01000000) == 0):
	pass
```

Then `A = 0, X = 0.`

#### label_8024

```asm
  sta z:_var_0000_indexed,X      ; $8024  95 00
  sta a:_var_0100_indexed,X      ; $8026  9D 00 01
  sta a:_var_0200_indexed,X      ; $8029  9D 00 02
  sta a:_var_0300_indexed,X      ; $802C  9D 00 03
  sta a:_var_0400_indexed,X      ; $802F  9D 00 04
  sta a:_var_0500_indexed,X      ; $8032  9D 00 05
  sta a:_var_0600_indexed,X      ; $8035  9D 00 06
  sta a:_var_0700_indexed,X      ; $8038  9D 00 07
  inx                            ; $803B  E8
  bne _label_8024                ; $803C  D0 E6
  lda #$FF                       ; $803E  A9 FF
  ldx #$00                       ; $8040  A2 00
```

```asm
  sta z:_var_0000_indexed,X      ; $8024  95 00
  sta a:_var_0100_indexed,X      ; $8026  9D 00 01
  sta a:_var_0200_indexed,X      ; $8029  9D 00 02
  sta a:_var_0300_indexed,X      ; $802C  9D 00 03
  sta a:_var_0400_indexed,X      ; $802F  9D 00 04
  sta a:_var_0500_indexed,X      ; $8032  9D 00 05
  sta a:_var_0600_indexed,X      ; $8035  9D 00 06
  sta a:_var_0700_indexed,X      ; $8038  9D 00 07
```

```c
for (X = 0; ; ) {
	... = 0x00; \\ A = 0x00
	X = (X + 1) & 0xFF; \\ inx
	if (X == 0) { \\ bne
		break;
	}
}
```

Then `A = 0xFF`, `X = 0x00`

→ Clear RAM.

#### label_8042

```
  sta a:_var_0200_indexed,X      ; $8042  9D 00 02
  inx                            ; $8045  E8
  inx                            ; $8046  E8
  inx                            ; $8047  E8
  inx                            ; $8048  E8
  bne _label_8042                ; $8049  D0 F7
```

Similarly, set all bit of the `0200 - 02FF` to `1`.

#### label_804b

```
  bit PPU_STATUS                 ; $804B  2C 02 20
  bpl _label_804b                ; $804E  10 FB
  lda #$88                       ; $8050  A9 88
  sta PPU_CTRL                   ; $8052  8D 00 20
  jmp _label_817f                ; $8055  4C 7F 81
```

`bit`: 
- `Z = A & PPU_STATUS`
- `V = PPU_STATUS[6]`
- `N = PPU_STATUS[7]`
`bpl`: Branch if `N = 0` then return to the beginning of the loop so:
```c
while ((PPU_STATUS & 0x01000000) == 0):
	pass
```

`PPU_CTRL = 0x88`
Then jump to `label_817f`

#### label_817f

`X = 0`

#### label_8181

```asm
  lda a:_data_872f_indexed,X     ; $8181  BD 2F 87
  sta a:_var_0401_indexed,X      ; $8184  9D 01 04
  inx                            ; $8187  E8
  cpx #$20                       ; $8188  E0 20
  bcc _label_8181                ; $818A  90 F5
  jsr _func_8645                 ; $818C  20 45 86
  lda #$02                       ; $818F  A9 02
  sta z:_var_0006                ; $8191  85 06
  lda #$80                       ; $8193  A9 80
  sta z:$09                      ; $8195  85 09
  lda #$78                       ; $8197  A9 78
  sta z:$0A                      ; $8199  85 0A
  jsr _func_855f                 ; $819B  20 5F 85
  jsr _func_80f2                 ; $819E  20 F2 80
```

Maps to
```c
for (x = 0; x < 0x20; x++) {
	_var_0401_indexed[x] = _data_872f_indexed[x];
}
```

Call function [8645](###func_8645)
`_var_0006 = 0x02`
`$0009 = 0x80`
`$000A = 0x78`
Call function [855f](###func_855f) (`A = 0x78`)
Call function [80f2](_func_80f2) (Game loop)

### func_80f2

```
  lda #$01                       ; $80F2  A9 01
  sta z:_var_0002                ; $80F4  85 02
```

#### label_80f6

```
  lda z:_var_0002                ; $80F6  A5 02
  bne _label_80f6                ; $80F8  D0 FC
  rts                            ; $80FA  60
```

`_var_0002 = 0x01`

### func_810b

Parameters: `X, Y`
```asm
  lda PPU_STATUS                 ; $810B  AD 02 20
  tya                            ; $810E  98
  lsr a                          ; $810F  4A
  lsr a                          ; $8110  4A
  lsr a                          ; $8111  4A
  ora #$20                       ; $8112  09 20
  sta PPU_ADDR                   ; $8114  8D 06 20
  tya                            ; $8117  98
  asl a                          ; $8118  0A
  asl a                          ; $8119  0A
  asl a                          ; $811A  0A
  asl a                          ; $811B  0A
  asl a                          ; $811C  0A
  sta z:_var_0007                ; $811D  85 07
  txa                            ; $811F  8A
  ora z:_var_0007                ; $8120  05 07
  sta PPU_ADDR                   ; $8122  8D 06 20
  rts                            ; $8125  60
```

`lda PPU_STATUS`: reset the latch
`PPU_ADDR = (Y >> 3) | 0x20`, `((Y << 5) | X) & 0xFF`

### func_8163

`JOYPAD1 = 0100`
`X = 0x08`

```
_label_816f:
  pha                            ; $816F  48
  lda JOYPAD1                    ; $8170  AD 16 40
  and #$03                       ; $8173  29 03
  cmp #$01                       ; $8175  C9 01
  pla                            ; $8177  68
  ror a                          ; $8178  6A
  dex                            ; $8179  CA
  bne _label_816f                ; $817A  D0 F3
  sta z:_var_0008                ; $817C  85 08
  rts                            ; $817E  60

_label_817f:
  ldx #$00                       ; $817F  A2 00

_label_8181:
  lda a:_data_872f_indexed,X     ; $8181  BD 2F 87
  sta a:_var_0401_indexed,X      ; $8184  9D 01 04
  inx                            ; $8187  E8
  cpx #$20                       ; $8188  E0 20
  bcc _label_8181                ; $818A  90 F5
  jsr _func_8645                 ; $818C  20 45 86
  lda #$02                       ; $818F  A9 02
  sta z:_var_0006                ; $8191  85 06
  lda #$80                       ; $8193  A9 80
  sta z:$09                      ; $8195  85 09
  lda #$78                       ; $8197  A9 78
  sta z:$0A                      ; $8199  85 0A
  jsr _func_855f                 ; $819B  20 5F 85
  jsr _func_80f2                 ; $819E  20 F2 80

_label_81a1:
  lda z:_var_0037                ; $81A1  A5 37
  cmp #$00                       ; $81A3  C9 00
  beq _label_81b1                ; $81A5  F0 0A
  cmp #$02                       ; $81A7  C9 02
  beq _label_81b7                ; $81A9  F0 0C
  jsr _func_83b8                 ; $81AB  20 B8 83
  jmp _label_81a1                ; $81AE  4C A1 81

_label_81b1:
  jsr _func_81bd                 ; $81B1  20 BD 81
  jmp _label_81a1                ; $81B4  4C A1 81

_label_81b7:
  jsr _func_83bc                 ; $81B7  20 BC 83
  jmp _label_81a1                ; $81BA  4C A1 81
```
TBC...
### func_855f

Parameters: `A`
```asm
  lda #$50                       ; $855F  A9 50
  sta a:$0201                    ; $8561  8D 01 02
  lda #$20                       ; $8564  A9 20
  sta a:$0202                    ; $8566  8D 02 02
  lda z:_var_000f                ; $8569  A5 0F
  jsr _func_860d                 ; $856B  20 0D 86
  stx a:_var_0203                ; $856E  8E 03 02
  sty a:_var_0200_indexed        ; $8571  8C 00 02
  lda #$01                       ; $8574  A9 01
  sta a:$0205                    ; $8576  8D 05 02
  lda #$01                       ; $8579  A9 01
  sta a:$0209                    ; $857B  8D 09 02
  stx a:_var_0207                ; $857E  8E 07 02
  stx a:_var_020b                ; $8581  8E 0B 02
  lda #$00                       ; $8584  A9 00
  sta a:$0206                    ; $8586  8D 06 02
  lda #$80                       ; $8589  A9 80
  sta a:$020A                    ; $858B  8D 0A 02
  tya                            ; $858E  98
  sec                            ; $858F  38
  sbc #$08                       ; $8590  E9 08
  sta a:_var_0204                ; $8592  8D 04 02
  tya                            ; $8595  98
  clc                            ; $8596  18
  adc #$08                       ; $8597  69 08
  sta a:_var_0208                ; $8599  8D 08 02
  rts                            ; $859C  60
```

`$0201 = 0x50`
`$0202 = 0x20`
Call function [860d](###func_860d) (`A`)
`_var_0203 = X`
`_var_0200_indexed = Y`
`$0205 = 0x01`
`$0209 = 0x01`
`_var_0207 = X`
`_var_020b = X`
`$0206 = 0x00`
`$020A = 0x80`
`_var_0204 = Y - 0x08`
`_var_0208 = Y + 0x08`
### func_859d

Parameters: `A`
```asm
  ldx #$02                       ; $859D  A2 02
  ldy #$59                       ; $859F  A0 59
  cmp #$00                       ; $85A1  C9 00
```

`X = 0x02, Y = 0x59`

#### label_85a3

```asm
  beq _label_85b3                ; $85A3  F0 0E
  inx                            ; $85A5  E8
  cpx #$1E                       ; $85A6  E0 1E
  bcc _label_85ad                ; $85A8  90 03
  ldx #$02                       ; $85AA  A2 02
  iny                            ; $85AC  C8
```

#### label_85ad

```asm
  sec                            ; $85AD  38
  sbc #$01                       ; $85AE  E9 01
  jmp _label_85a3                ; $85B0  4C A3 85
```

```c
while (A != 0) {
	x++;
	if (x < 0x1E) {	
	
	} else {
		x = 0x02;
		y++;
	}
	A--;
}
```
#### label_85b3

```
  rts                            ; $85B3  60
```


### func_860d

Parameters: `A`
```
  jsr _func_859d                 ; $860D  20 9D 85
  txa                            ; $8610  8A
  asl a                          ; $8611  0A
  asl a                          ; $8612  0A
  asl a                          ; $8613  0A
  tax                            ; $8614  AA
  tya                            ; $8615  98
  asl a                          ; $8616  0A
  asl a                          ; $8617  0A
  asl a                          ; $8618  0A
  tay                            ; $8619  A8
  dey                            ; $861A  88
  rts                            ; $861B  60
```

Call function [859d](func_859d) (`A`)

`X >>= 3`
`Y >>= 3`
`Y--`

### func_8645

```
  lda PPU_STATUS                 ; $8645  AD 02 20
  lda #$28                       ; $8648  A9 28
  sta PPU_ADDR                   ; $864A  8D 06 20
  lda #$00                       ; $864D  A9 00
  sta PPU_ADDR                   ; $864F  8D 06 20
  lda #$00                       ; $8652  A9 00
  ldy #$1E                       ; $8654  A0 1E
```
`PPU_ADDR = 2800`
`lda PPU_STATUS`: reset the latch

```
  lda #$28                       ; $8648  A9 28
  sta PPU_ADDR                   ; $864A  8D 06 20
  lda #$00                       ; $864D  A9 00
  sta PPU_ADDR                   ; $864F  8D 06 20
```

We need two stores action to write `2800` to `PPU_ADDR` (depends on latch).

`Y = 0x1E`
#### label_8656

`X = 0x20`

#### label_8658

```
  sta PPU_DATA                   ; $8658  8D 07 20
  dex                            ; $865B  CA
  bne _label_8658                ; $865C  D0 FA
  dey                            ; $865E  88
  bne _label_8656                ; $865F  D0 F5
  ldx #$40                       ; $8661  A2 40
```

Then the two labels mean:

```c
for (y = 0x1E; y > 0; y--) {
	for (x = 0x20; x > 0; x--) {
		PPU_DATA = 0
	}
}
```

`X = 0x40`

#### label_8663

```asm
  sta PPU_DATA                   ; $8663  8D 07 20
  dex                            ; $8666  CA
  bne _label_8663                ; $8667  D0 FA
  lda #$01                       ; $8669  A9 01
  ldy #$42                       ; $866B  A0 42
```

Maps to:

```c
for (x = 0x40; x > 0; x--) {
	PPU_DATA = 0
}
```

`A = 0x01, Y = 0x42`

#### label_866d

```asm
  pha                            ; $866D  48
  ldx #$08                       ; $866E  A2 08
  jsr _func_810b                 ; $8670  20 0B 81
  pla                            ; $8673  68
  ldx #$08                       ; $8674  A2 08
```

`pha`: Push `0x01` to the stack
`X = 0x08`
Call function [810b](###func_810b) (`X = 0x08, Y = 0x42`)
`pla`: Pop and `A = 0x01`
`X = 0x08`

#### label_8676

```asm
  sta PPU_DATA                   ; $8676  8D 07 20
  eor #$03                       ; $8679  49 03
  inx                            ; $867B  E8
  cpx #$18                       ; $867C  E0 18
  bcc _label_8676                ; $867E  90 F6
  eor #$03                       ; $8680  49 03
  iny                            ; $8682  C8
  cpy #$56                       ; $8683  C0 56
  bcc _label_866d                ; $8685  90 E6
  jsr _func_861c                 ; $8687  20 1C 86
  rts                            ; $868A  60
```

```c
for (y = 0x42; y < 0x56; y++) {
	for (x = 0x08; x < 0x18; x++) {
		PPU_DATA = A;
		A ^= 0x03;
	}
	A ^= 0x03;
}
```

Call function [861c](###func_861c)

### func_861c
```c
0x810b(X = 0x00, Y = 0x56);
for (x = 0; x < 47; x++) {
	PPU_DATA = _data_887e_indexed[x]
}
0x810b(X = 0x02, Y = 0x5B);
PPU_DATA = 44;
_var_0300_indexed = 0x87;
```