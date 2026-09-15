Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.1: Definition of Space-bounded Computation.

## Definition

> [!definition] Class NPSPACE
> Let $S: \mathbb{N} \rightarrow \mathbb{N}$ and $\mathcal{L} \subseteq \{0, 1\}^*$. We say that $\mathcal{L} \in \mathsf{NSPACE}(s(n))$ if there is a constant $c$ and a [[Non-deterministic Turing Machine]] $M$ deciding $\mathcal{L}$ such at most $c \cdot s(n)$ that never uses more than $c \cdot s(n)$ nonblank tape locations on length $n$ inputs, regardless of its non-deterministic choices.