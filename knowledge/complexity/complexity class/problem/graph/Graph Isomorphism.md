Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.1: The Class NP.

## Definition

> [!definition] Graph Isomorphism
> Reference Name: $\mathsf{GI}$
> 
> ---
> Input:
> - $M_1, M_2$: $n \times n$ adjacency matrices.
> 
> ---
> Output: Decide if $M_1$ and $M_2$ define the same graph, up to renaming of vertices.
> 
> ---
> Certificate: The permutation $\pi: [n] \rightarrow [n]$ such that $M_2$ is equal $M_1$ after reordering $M_1$'s indices according to $\pi$.

## Property

> [!proposition]
> Member of:: [[Class NP]]
