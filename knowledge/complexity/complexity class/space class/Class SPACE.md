Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.1: Definition of Space-bounded Computation.

## Definition

> [!definition] Class PSPACE
> Let $S: \mathbb{N} \rightarrow \mathbb{N}$ and $\mathcal{L} \subseteq \{0, 1\}^*$. We say that $\mathcal{L} \in \mathsf{SPACE}(s(n))$ if there is a constant $c$ and a [[Turing Machine]] $M$ deciding $\mathcal{L}$ such at most $c \cdot s(n)$ locations on $M$'s work tapes (excluding the input tape) are ever visited by $M$'s head during its computation on every input of length $n$.