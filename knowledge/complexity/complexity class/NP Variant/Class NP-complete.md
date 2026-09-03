## Definition

> [!definition] Class $\text{NP-complete}$
> A language $\mathcal L$ is in the class $\text{NP-complete}$ if:
> - For all $\mathcal L'$ in $\text{NP}$, there exist a polynomial-time reduction to $\mathcal L$.
> - It is in $\text{NP}$.

## Property

> [!theorem]
> If $B$ is NP-complete and $B \in \text{P}$, then $\text{P} = \text{NP}$.

## Member

> [!theorem] Cook-Levin Theorem
> [[Satisfiability Problem|SAT]] is NP-complete.

> [!example] Members of NP-Complete
> - $\text{CLIQUE} = \{\langle G, k \rangle \mid G \text{ is an undirected graph with a } k\text{-clique}\}$
> - $\text{VERTEX-COVER} = \{\langle G, k \rangle \mid G \text{ is an undirected graph with a } k\text{-node vertex cover}\}$
> - $\text{HAMPATH} = \{\langle G, s, t \rangle \mid G \text{ is a directed graph with a Hamiltonian path from } s \text{ to } t\}$
> - $\text{UHAMPATH} = \{\langle G, s, t \rangle \mid G \text{ is an undirected graph with a Hamiltonian path from } s \text{ to } t\}$
> - [[Subset-Sum Problem|SUBSET-SUM]]
