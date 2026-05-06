## Hall's Theorem

**Theorem**: A bipartite graph with sets of vertices $A, B$ has a perfect matching if and only if:
- $|A| = |B|$
- For all $U \subseteq A$: $|N(U)| \ge |U|$ with $N(U)$ is the set of vertices that are adjacent to vertices in $U$.

## Konig Theorem

**Theorem**: The size of a maximum matching in a bipartite graph is equal to the size of a minimum vertex cover of the graph.

## Frobenius-Hall Theorem

**Theorem**: In a bipartite graph with sets of vertices $A, B$, $A$ has a matching into $B$ if and only if for every subset $X$ of $A$, $|X| \leq |\Gamma(X)|$ if $\Gamma(X)$ is the set of neighbors of $X$. 