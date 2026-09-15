Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.1: The Class NP.

## Definition

> [!definition] Linear Programming
> Input:
> - $n$: Number of variables ($u_1, \dots, u_n \in \mathbb{Q}$).
> - $m$: Number of linear inequalities.
> - $a_{i, j}, b_i \in \mathbb{Q}$: Coefficient for inequalities: 
> $$\forall i \in [m], \sum_{i = 1}^n a_{i, j} u_j \leq b_i$$ 
> 
> ---
> Output: Decides if there is such assignment $u_1, \dots, u_n$.
> 
> ---
> Certificate: The assignment.
