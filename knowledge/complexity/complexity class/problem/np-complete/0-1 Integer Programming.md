Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.1: The Class NP; Section 2.4: The Web of Reductions.

# Definition

> [!definition] 0/1 Integer Programming
> Reference Name: $0/1 \; \mathsf{IPROG}$
> 
> ---
> Input:
> - $n$: Number of variables ($u_1, \dots, u_n \in \{0, 1\}$).
> - $m$: Number of linear inequalities.
> - $a_{i, j}, b_i \in \mathbb{Q}$: Coefficient for inequalities: 
> $$\forall i \in [m], \sum_{i = 1}^n a_{i, j} u_j \leq b_i$$ 
> 
> ---
> Output: Decides if there is such assignment $u_1, \dots, u_n$.
> 
> ---
> Certificate: The assignment.

## Property

> [!theorem]
> Complete for:: [[Class NP]] under [[Polynomial-time Karp Reducibility]]
> 
> ---
> $0/1 \; \mathsf{IPROG} \in \mathsf{NP}\mbox{-}\mathsf{complete}$
> 
> ---
> $\mathsf{SAT} \leq_p 0/1 \; \mathsf{IPROG}$

