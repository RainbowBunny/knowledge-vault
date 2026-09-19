Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.4: The Web of Reductions.

## Definition

> [!definition] Directed Hamiltonian Path
> Reference name: $\mathsf{dHAMPATH}$
> 
> ---
> Input:
> - $G$: Directed graph.
> 
> ---
> Output: Decides if there is a path that visits all vertices exactly once. (Hamiltonian path)
> 
> ---
> Certificate: The Hamiltonian path.

## Property

> [!theorem]
> Complete for:: [[Class NP]] under [[Polynomial-time Karp Reducibility]]
> 
> ---
> $\mathsf{dHAMPATH}$ is $\mathsf{NP}\mbox{-}\mathsf{complete}$.
> 
> ---
> $G \in \mathsf{dHAMPATH} \iff \varphi \in \mathsf{SAT}$

