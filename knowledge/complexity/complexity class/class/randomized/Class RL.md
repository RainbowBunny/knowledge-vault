Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 7: Randomized computation, Section 7.7: Randomized Space-Bound Computation.

## Definition

> [!definition] Class Randomized Logarithm space
> A [[Language]] $\mathcal{L}$ is in $\mathsf{RL}$ if there is an $O(\log n)$-space [[Probabilistic Turing Machine]] $M$ such that: 
> - If $x \in \mathcal{L}$ then $\Pr[M(x) = 1] \geq \frac{2}{3}$.
> - If $x \notin \mathcal{L}$ then $\Pr[M(x) = 1] = 0$.



