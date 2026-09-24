## Acyclic Subgraphs

The incidence matrix is defined in [[Graph#Incidence Matrix]] (for undirected graphs, replace $-1$ by $1$: $M_{ve} = 1$ iff $e$ is incident on $v$).

> [!proposition]
> Consider the incidence matrix for an undirected graph $G = (V, E)$. A set of columns of $M$ is linearly independent over $\mathbb F_2$ if and only if the corresponding set of edges is acyclic.

> [!proposition]
> Consider the incidence matrix for a directed graph $G = (V, E)$ with no self-loops, then if a set of columns of $M$ is linearly independent, then the corresponding set of edges does not contain a directed cycle.
