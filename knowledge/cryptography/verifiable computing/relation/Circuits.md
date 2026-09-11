
| Boolean Circuit                                                                      | Arithmetic Circuit                                                                                  |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| Variables are 0, 1                                                                   | Signals hold numbers                                                                                |
| The only operations are AND, OR, NOT                                                 | The only operations are addition and multiplication                                                 |
| Satisfied when the output is true                                                    | Satisfied when the left hand side equals the right hand side for all equations (there is no output) |
| Witness is an assignment to the Boolean variables that satisfies the Boolean circuit | Witness is an assignment to the signals that satisfies all the equality constraints                 |
## Definition

> [!definition] Arithmetic Circuit
> Let $q$ be a prime. An **arithmetic circuit** for $\mathbb Z_q$ is a circuit with four types of gates: addition, multiplication, constant addition, and scalar multiplication.
> - An **addition gate** takes two inputs, $x, y \in \mathbb Z_q$ and produces a single output $z = x + y \in \mathbb Z_q$.
> - A **multiplication gate** takes two inputs, $x, y \in \mathbb Z_q$ and produces a single output $z = x \cdot y \in \mathbb Z_q$.
> - A **constant addition gate** takes one input $x \in \mathbb Z_q$ and produces a single output $z = x + c \in \mathbb Z_q$.
> - A **scalar multiplication gate** takes one input $x \in \mathbb Z_q$ and produces a single output $z = cx \in \mathbb Z_q$, where $c \in \mathbb Z_q$ is a constant associated with the gate.

