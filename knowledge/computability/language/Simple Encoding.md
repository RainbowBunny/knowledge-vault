Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 1: The computational model —and why it doesn’t matter, Section 1.1.1: Representing objects as strings

## Definition

> [!definition] Simple Encoding
> **Simple encoding** can be used to represent general objects (integers, pairs of integers, graphs, vectors, matrices, etc.) as strings of bits.
> For an object $x$, we denote $\llcorner x \lrcorner$ as the binary representation of $x$.

> [!remark] Representing pairs and tuples
> A canonical representation for $\langle x, y \rangle$ can be easily obtained from the representation of $x$ and $y$. A simple idea is that we can use $\{0, 1, \#\}$ and then use the mapping $0 \mapsto 00, 1 \mapsto 11, \# \mapsto 01$ to convert this into a string of bits.
