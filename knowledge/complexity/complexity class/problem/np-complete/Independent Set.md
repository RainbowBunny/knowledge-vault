Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 0: Notational conventions, Section 0.1: Decision Problems/Languages.
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.1: The Class NP; Section 2.4: The Web of Reductions.

## Definition

> [!definition] Independent Set
> $\mathsf{INDSET} = \{\langle G, k \rangle \; | \; \exists S \subseteq V(G) \; \text{s.t.} |S| \geq k \land \forall u, v \in S, (u, v) \notin E(G)\}.$

## Property

> [!theorem]
> Requires:: [[Class NP]]
> 
> ---
> $\mathsf{INDSET} \in \mathsf{NP}$.
> 
> ---
> The polynomial-time verifier $M$: 
> - On input $\langle G, k \rangle, w$ where $G$ is a graph, $k$ is the number of vertices and $w$ is the $k$ vertices forming the independent set in $G$ which is the witness:
> 	1. Checks there is no edges between each pair of vertices in $w$.

> [!theorem]
> [[Hardness and Completeness|Complete]] for:: [[Class NP]] under [[Polynomial-time Karp Reducibility]]
> 
> ---
> $\mathsf{INDSET} \in \mathsf{NP}\mbox{-}\mathsf{complete}$
> 
> ---
> $\mathsf{3SAT} \leq_p \mathsf{INDSET}$