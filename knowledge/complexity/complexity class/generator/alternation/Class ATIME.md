Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 5: The polynomial hierarchy and alternations, Section 5.3: Alternating Turing Machines.

## Definition

> [!definition] Class Alternative TIME
> A [[Language]] $\mathcal{L} \in \mathsf{ATIME}(T(n))$ if there is a constant $c$ and a $c \cdot T(n)$-time [[Alternating Turing Machine]] $M$ such that for every $x \in \{0, 1\}^*$, $M$ accepts $x$ iff $x \in \mathcal{L}$.