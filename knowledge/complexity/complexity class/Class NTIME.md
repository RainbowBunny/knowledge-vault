## Definition

> [!definition] Class NTIME
> For every function $T: \mathbb{N} \rightarrow \mathbb{N}$ and [[Language]] $\mathcal{L} \subseteq \{0, 1\}^*$, we say that $\mathcal{L} \in \mathsf{NTIME}(T(n))$ if there is a constant $c > 0$ and a $c \cdot T(n)$-time [[Non-deterministic Turing Machine]] $M$ such that: 
> $$\forall x \in \{0, 1\}^*: x \in \mathcal{L} \iff M(x) = 1.$$
