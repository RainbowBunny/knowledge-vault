
## Syntax

`wire [n:0]`: Bus width `n + 1` bits, `0 -> n`.
`reg [n:0] array [0:LEN-1]`: Create an array of 5 bit (`LEN` entries of `n + 1` bits)
`posedge CLK`: Trigger on rising edge of clock. (Every clock tick)
`posedge RST`: Trigger immediately when reset goes high. (immediately when reset is pressed)
`<width>'<base><value>`: Literal, `<base>` can be `b, h, d`.


## Run

[iverilog](https://github.com/steveicarus/iverilog)

`iverilog -o sim *.v`
`vvp sim`
`gtkwave dump.vcd`