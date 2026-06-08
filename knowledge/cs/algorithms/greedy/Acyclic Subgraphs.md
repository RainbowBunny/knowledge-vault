## Acyclic Subgraphs

> [!definition] Incidence Matrix
> The **incidence matrix** for an undirected graph $G = (V, E)$ is a $|V| \times |E|$ matrix $M$ such that $M_{ve} = 1$ if edge $e$ is incident on vertex $v$, and $M_{ve} = 0$ otherwise. 
> The **incidence matrix** for an directed graph $G = (V, E)$ with no self-loops is a $|V| \times |E|$ matrix $M$ such that $M_{ve} = -1$ if edge $e$ leaves vertex $v$, $M_{ve} = 1$ if edge $e$ enters vertex $v$, and $M_{ve} = 0$ otherwise.

> [!proposition]
> Consider the incidence matrix for an undirected graph $G = (V, E)$. A set of columns of $M$ is linearly independent over $\mathbb F_2$ if and only if the corresponding set of edges is acyclic.

> [!proposition]
> Consider the incidence matrix for a directed graph $G = (V, E)$ with no self-loops, then if a set of columns of $M$ is linearly independent, then the corresponding set of edges does not contain a directed cycle.
