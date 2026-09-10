Reference:
- [[Book Reference|Introduction to the Theory of Computation]] - Chapter 1: Regular Languages, Exercise 1.24; Exercise 1.25; Exercise 1.26.

## Definition

> [!definition] Finite State Transducer
> Generalizes:: [[Deterministic Finite Automaton]].
> 
> ---
> A Finite State Transducer $\mathsf{FST}$ is a 5-tuple $(Q, \Sigma, \Gamma, \delta, q_0)$:
> - $\Sigma$: Is now the **input alphabet**.
> - $\Gamma$: A finite set called the **output alphabet**.
> - $\delta: Q \times \Sigma \rightarrow Q \times \Gamma$: The transition function now has an output.
> - The set of accepts state $F$ is removed, but we now have an output.
