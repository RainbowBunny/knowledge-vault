Reference:
- [[Book Reference|Introduction to the Theory of Computation]]: - Chapter 3: The Church-Turing Thesis, Section 3.2: Variants of Turing Machines.

## Definition

> [!definition] Turing Machine with Stay Option
> Generalizes:: [[Turing Machine]].
> - The rule 4 is now $\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R, S\}$.

## Property

> [!proposition]
> Turing Machine with Stay Option has an equivalent single-tape Turing machine.
> 
> ---
> The "stay put" feature can be replaced by two transitions: one that moves to the right and the second back to the left.