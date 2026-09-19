Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 6: Boolean circuits, Section 6.1: Boolean Circuits and P/poly.

## Definition

> [!definition] Circuit Family
> Let $T: \mathbb{N} \rightarrow \mathbb{N}$ be a [[Function]].
> A $T(n)$**-size circuit family** is a sequence $\{C_n\}_{n \in \mathbb{N}}$ of [[Boolean Circuit]], where $C_n$ has $n$ inputs and a single output, and its size $|C_n| \leq T(n) \; \forall n$.

> [!definition] Representing Circuit Family
> - $\mathsf{SIZE}(n)$: Returns the size $S$ (in binary representation) of the circuit $C_n$.
> - $\mathsf{TYPE}(n, i)$: $i \in [m]$, returns the label of the $i$-th vertex of $C_n$. That is it returns one of $\{\land, \lor, \lnot, \mathsf{NONE}\}$.
> - $\mathsf{Edge}(n, i, j)$: Returns 1 if there is a directed edge in $C_n$ from the $i$-th vertex to the $j$-th vertex.

