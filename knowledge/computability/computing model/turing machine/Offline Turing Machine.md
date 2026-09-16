Reference:
- [[Book Reference|Introduction to the Theory of Computation]]: - Chapter 1: The computational model—and why it doesn’t matter, Section 1.2: The Turing Machine.

## Definition

> [!definition] Offline Turing Machine
> Extends:: [[Multitape Turing Machine]]
> 
> ---
> - Tape 1 is the input tape (read-only), thus the **transition function** is $\delta: Q \times \Gamma^k \rightarrow Q \times \Gamma^{k - 1} \times \{L, R, S\}^k$.
> - Tape 2-$k$ is the working tape.
> - Tape $k$ is also the output tape, thus, instead of having $q_\mathsf{accept}, q_\mathsf{reject}$, now there is only one $q_\mathsf{halt}$.
