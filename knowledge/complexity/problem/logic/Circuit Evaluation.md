Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 6: Boolean circuits, Section 6.7.2: P-completeness.

## Definition

> [!definition] Circuit Evaluation
> $\mathsf{CIRCUIT} \mbox{-} \mathsf{EVAL}$ denote the [[Language]] consisting of all pairs $\langle C, x \rangle$ where $C$ is an $n$-input single output [[Boolean Circuit]] and $x \in \{0, 1\}^n$ is such that $C(x) = 1$.

## Property

> [!theorem]
> Requires:: [[Hardness and Completeness]]
> Complete for:: [[Class P]] under [[Log-space Reducibility]]
> 
> ---
> $\mathsf{CIRCUIT} \mbox{-} \mathsf{EVAL}$ is $\mathsf{P} \mbox{-} \mathsf{complete}$.