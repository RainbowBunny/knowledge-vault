Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 1: The computational model —and why it doesn’t matter, Section 1.6: The Class P.
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 3: Diagonalization, Section 3.1: Time Hierarchy Theorem.

## Definition

> [!definition] Class Deterministic TIME
> Let $T: \mathbb{N} \rightarrow \mathbb{N}$ be some function. A [[Language]] $L$ is in $\mathsf{DTIME}(T(n))$ iff there is an [[Offline Turing Machine|Turing Machine]] that runs in time $c \cdot T(n)$ for some constants $c > 0$ and decides ([[Language]]) $L$.

> [!remark]
> The $\mathsf{D}$ in $\mathsf{DTIME}$ refers to "deterministic".

## Property

> [!theorem] Time Hierarchy Theorem
> If $f, g$ are [[Computable Function|Time-Constructible Function]] satisfying $f(n) \log f(n) = o(g(n))$, then
> $$\mathsf{DTIME}(f(n)) \subsetneq \mathsf{DTIME}(g(n))$$
