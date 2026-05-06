---
parent: "[[Foundational Math for Zero Knowledge Proofs]]"
tags: []
date: 2025-07-09T22:14
---
## Arithmetic Circuits as an alternative to Boolean circuits

Disadvantage of Boolean Circuits: Can be verbose when representing arithmetic operations such as addition or multiplication.

| Boolean Circuit                                                                      | Arithmetic Circuit                                                                                  |
| ------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------- |
| Variables are 0, 1                                                                   | Signals hold numbers                                                                                |
| The only operations are AND, OR, NOT                                                 | The only operations are addition and multiplication                                                 |
| Satisfied when the output is true                                                    | Satisfied when the left hand side equals the right hand side for all equations (there is no output) |
| Witness is an assignment to the Boolean variables that satisfies the Boolean circuit | Witness is an assignment to the signals that satisfies all the equality constraints                 |
