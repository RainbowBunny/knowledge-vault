Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 7: Randomized computation, Section 7.1: Probabilistic Turing Machines.

## Definition

> [!definition] Class Bounded Polynomial Time
> For $T: \mathbb{N} \rightarrow \mathbb{N}$ and $\mathcal{L} \subseteq \{0, 1\}^*$, we say that a [[Probabilistic Turing Machine]] $M$ decides $\mathcal{L}$ in time $T(n)$ if for every $x \in \{0, 1\}^*$, $M$ halts in $T(|x|)$ steps regardless of its random choices, and $\Pr[M(x) = \mathcal{L}(x)] \geq \frac{2}{3}$.
> 
> We let $\mathsf{BPTIME}(T(n))$ be the class of languages decided by PTMs in $O(T(n))$.

