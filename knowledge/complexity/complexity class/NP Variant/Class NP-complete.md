Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.2: Reducibility and NP-completeness.

## Definition

> [!definition] Class NP-complete
> Requires:: [[Polynomial-time Karp Reducibility]]
> 
> ---
> A [[Language]] $\mathcal{L} \in \mathsf{NP}\mbox{-}\mathsf{complete}$ if:
> $$\mathcal{L} \in \mathsf{NP} \land \forall \mathcal{L'} \in \mathsf{NP}: \mathcal{L} \leq_p \mathcal{L}'$$

## Member


> [!example] Members of NP-Complete
> - $\text{CLIQUE} = \{\langle G, k \rangle \mid G \text{ is an undirected graph with a } k\text{-clique}\}$
> - $\text{VERTEX-COVER} = \{\langle G, k \rangle \mid G \text{ is an undirected graph with a } k\text{-node vertex cover}\}$
> - $\text{HAMPATH} = \{\langle G, s, t \rangle \mid G \text{ is a directed graph with a Hamiltonian path from } s \text{ to } t\}$
> - $\text{UHAMPATH} = \{\langle G, s, t \rangle \mid G \text{ is an undirected graph with a Hamiltonian path from } s \text{ to } t\}$
> - [[Subset-Sum Problem|SUBSET-SUM]]
