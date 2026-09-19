Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 6: Boolean circuits, Section 6.1: Boolean Circuits and P/poly; Section 6.6: Nonuniform Hierarchy Theorem.

## Definition

> [!definition] Class SIZE
> Requires:: [[Circuit Family]]
> 
> ---
> Let $T: \mathbb{N} \rightarrow \mathbb{N}$ be a function.
> A [[Language]] $\mathcal{L} \in \mathsf{SIZE}(T(n))$ if there exists a $T(n)$-size circuit family $\{C_n\}_{n \in \mathbb{N}}$ such that:
> $$\forall x \in \{0, 1\}^n: x \in \mathcal{L} \iff C_n(x) = 1$$

## Property

> [!theorem] Nonuniform Hierarchy Theorem
> For every function $T, T': \mathbb{N} \rightarrow \mathbb{N}$ with $2^n/n > T'(n) > 10T(n) > n$,
> $$\mathsf{SIZE}(T(n)) \subsetneq \mathsf{SIZE}(T'(n))$$
