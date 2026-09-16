Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 5: The polynomial hierarchy and alternations, Section 5.3: Alternating Turing Machines.

## Definition

> [!definition] Class $\Pi$TIME
> For every $i \in \mathbb{N}$, we define $\Pi_i \mathsf{TIME}(T(n))$ to be the set of [[Language]] accepted by a $T(n)$-time [[Alternating Turing Machine]] $M$ whose initial state is labeled "$\forall$" and on which every input and on every (directed) path from the starting configuration in the configuration graph, $M$ can alternate at most $i - 1$ times from states with one label to states with other label.
