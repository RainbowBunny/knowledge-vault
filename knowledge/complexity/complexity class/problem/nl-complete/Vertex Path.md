Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 1: The computational model —and why it doesn’t matter, Section 1.6: The Class P.
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.3: NL Completeness; Section 4.3.2: NL = coNL.

## Definition

> [!definition] Vertex Path
> Reference Name: $\mathsf{PATH}$
> 
> ---
> Input:
> - $G$: Graph.
> - $s, t$: Two vertices in the graph.
> 
> ---
> Output: Decide if s is connected to t in G.
> 
> ---
> Certificate: A path from $s$ to $t$.

## Property

> [!theorem]
> Complete for:: [[Class NL]] under [[Log-space Reducibility]].
> 
> ---
> $\mathsf{PATH}$ is $\mathsf{NL}\mbox{-}\mathsf{complete}$.

> [!theorem] Immerman-Szelepcsényi Theorem
> Requires:: [[Language|Complement Language]], [[Class NL]]
> 
> ---
> $\overline{\mathsf{PATH}} \in \mathsf{NL}$.

