Reference:
- [[Book Reference|Introduction to the Theory of Computation]]: - Chapter 3: The Church-Turing Thesis, Section 3.2: Variants of Turing Machines.

## Definition

> [!definition] Multitape Turing Machine
> Generalizes:: [[Turing Machine]].
> 
> ---
> - $k$: The number of tapes.
> - The rule 4 is now $\delta: Q \times \Gamma^k \rightarrow Q \times \Gamma^k \times \{L, R, S\}^k$.

## Property

> [!theorem]
> Every multitape Turing machine has an equivalent single-tape Turing machine.
> 
> ---
> To be completed.

> [!corollary]
> A [[Language]] is [[Recognizable Language|Turing-recognizable]] if and only if some multitape Turing machine recognizes it.