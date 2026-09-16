## Definition

> [!definition] Hardness and Completeness
> ### Scope
> A [[Complexity Class]] $\mathsf{C}$, a [[Reductions]] $\leq$.
> 
> ---
> ### Property
> - $\mathcal{L} \in \mathsf{C}\mbox{-}\mathsf{hard} \iff \forall \mathcal{A} \in \mathsf{C}: \mathcal{A} \leq \mathcal{L}$.
> - $\mathcal{L} \in \mathsf{C}\mbox{-}\mathsf{complete} \iff \mathcal{L} \in \mathsf{C}\mbox{-}\mathsf{hard} \land \mathcal{L} \in \mathsf{C}$

## Instantiation

| Completeness    | Reduction                             |
| --------------- | ------------------------------------- |
| NP-complete     | [[Polynomial-time Karp Reducibility]] |
| PSPACE-complete | [[Polynomial-time Karp Reducibility]] |
| NL-complete     | [[Log-space Reducibility]]            |
| P-complete      | [[Log-space Reducibility]]            |
