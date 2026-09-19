Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 7: Randomized computation, Section 7.6: Randomized Reductions.

## Definition

> [!definition] Randomized Polynomial Reducibility
> Language $\mathcal{B}$ reduces to language $\mathcal{C}$ under a randomized polynomial time reduction, denoted $\mathcal{B} \leq_r \mathcal{C}$, if there is a [[Probabilistic Turing Machine]] $M$ such that: 
> $$\forall x \in \{0, 1\}^*, \Pr[\mathcal{B}(M(x)) = \mathcal{C}(x)] \geq \frac{2}{3}$$

