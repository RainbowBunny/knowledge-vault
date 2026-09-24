Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.1: The Class NP.

## Definition

> [!definition] Traveling Salesperson
> Input: 
> - $n$: Number of nodes.
> - $\binom{n}{2}$ numbers $d_{i, j}$: The distances between all pairs of nodes.
> - $k$: The length limit.
> 
> ---
> Output: Decide if there is a closed circuit (i.e., a “salesperson tour”) that visits every node exactly once and has total length at most $k$.
> 
> ---
> Certificate: Sequence of nodes.

## Property

> [!theorem]
> Requires:: [[Hardness and Completeness]]
> Complete for:: [[Class NP]] under [[Polynomial-time Karp Reducibility]]

