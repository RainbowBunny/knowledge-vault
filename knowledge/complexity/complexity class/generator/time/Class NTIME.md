Reference:
-  [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.1.2: Nondeterministic Turing Machines.
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 3: Diagonalization, Section 3.2: Non-deterministic Time Hierarchy Theorem.

## Definition

> [!definition] Class Nondeterministic TIME
> For every function $T: \mathbb{N} \rightarrow \mathbb{N}$ and [[Language]] $\mathcal{L} \subseteq \{0, 1\}^*$, we say that $\mathcal{L} \in \mathsf{NTIME}(T(n))$ if there is a constant $c > 0$ and a $c \cdot T(n)$-time nondeterministic [[Oracle Turing Machine|Turing Machine]] $M$ such that: 
> $$\forall x \in \{0, 1\}^*: x \in \mathcal{L} \iff M(x) = 1.$$

## Property

> [!theorem] Non-deterministic Time Hierarchy Theorem
> If $f, g$ are [[Computable Function|Time-constructible Function]] satisfying $f(n + 1) = o(g(n))$, then
> $$\mathsf{NTIME}(f(n)) \subseteq \mathsf{NTIME}(g(n))$$

