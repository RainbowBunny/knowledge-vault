## Scheme

> [!definition] Delsarte Matrix Codes
> ### Parameters
> - $q, m$: Internal axis
> - $n$: Code length
> - $d_r$: Target rank distance
> - $k = n - d_r + 1$
> - $N$: Evaluation point
> - $\mathbb F_q$: Base field
> - $\ohm$: Basis, fixes the matrix view.
> 
> ---
> ### Algorithms
> - [[Rank Metric Codes#Matrix Form|Matrix Form]]: For a message vector $u$,
> $$\mathcal M = \{M(u): u \in \mathbb F_{q^m}^{n - d_r + 1}\}$$
> where elements $M_{i, j}(u), \quad i = 1, 2, \dots, m, \quad j = 1, 2, \dots, n$, of the matrix $M(u)$ are given by
> $$M_{ij}(u) = \text{Tr}(\omega_i \sum_{s = 0}^{n - d_r} u_s v_j^{q^s})$$

