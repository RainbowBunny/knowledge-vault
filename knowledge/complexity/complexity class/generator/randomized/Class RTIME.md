Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 7: Randomized computation, Section 7.3: One-Sided and "Zero-Sided" Error: RP, coRP, ZPP.

## Definition

> [!definition] Class Randomized TIME
> $\mathsf{RTIME}(T(n))$ contains every [[Language]] $\mathsf{L}$ for which there is a [[Probabilistic Turing Machine]] $M$ running in $T(n)$ time such that:
> - $x \in \mathcal{L} \implies \Pr[M(x) = 1] \geq \frac{2}{3}$.
> - $x \notin \mathcal{L} \implies \Pr[M(x) = 0] = 0$.

