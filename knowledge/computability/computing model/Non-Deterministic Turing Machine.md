Reference:
- [[Book Reference|Introduction to the Theory of Computation]]: - Chapter 3: The Church-Turing Thesis, Section 3.2: Variants of Turing Machines.

## Definition

> [!definition] Non-Deterministic Turing Machine
> Extends: [[Turing Machine]].
> - The rule 4 is now $\delta: Q \times \Gamma \rightarrow \mathcal{P}(Q \times \Gamma \times \{L, R, S\})$.

## Property

> [!theorem]
> Every nondeterministic Turing machine has an equivalent [[Turing Machine|deterministic Turing machine]].
> 
> ---
> To be completed.

> [!corollary]
> A language is [[Language#Recognizable|Turing-recognizable]] if and only if some non-deterministic Turing machine recognizes it.

> [!corollary]
> A language is [[Language#Decidable|Decidable]] if and only if some non-deterministic Turing machine recognizes it.