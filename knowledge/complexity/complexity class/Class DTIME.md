Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 1: The computational model —and why it doesn’t matter, Section 1.6: The Class P.

## Definition

> [!definition] The class DTIME
> Let $T: \mathbb{N} \rightarrow \mathbb{N}$ be some function. A [[Language]] $L$ is in $\mathsf{DTIME}(T(n))$ iff there is a [[Turing Machine]] that runs in time $c \cdot T(n)$ for some constants $c > 0$ and decides ([[Language]]) $L$.

> [!remark]
> The $\mathsf{D}$ in $\mathsf{DTIME}$ refers to "deterministic".