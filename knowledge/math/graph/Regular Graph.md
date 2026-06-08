
## Regular Graph


## Strongly Regular Graph

> [!definition] Strongly Regular Graph
> A **strongly regular graph (SRG)** is a **[[#Regular Graph]]** $G = (V, E)$ with $v$ vertices and **degree** $k$ such that for some some given integers $\lambda, \mu \geq 0$
> - Every two adjacent vertices have $\lambda$ common neighbors, and 
> - Every two non-adjacent vertices have $\mu$ common neighbours.
> 
> Denoted: $\text{srg}(v, k, \lambda, \mu)$.

> [!proposition] Algebraic Properties 
> - Relationship between parameters:
> $$(v - k - 1) \mu = k (k - \lambda - 1)$$
> - Adjacency matrix equation:
> $$\begin{gather}
> AJ = JA = kJ \\
> A^2 = kI + \lambda A + \mu (J - I - A)
> \end{gather}$$

> [!example] Steiner Graphs

> [!example] Latin Square Graphs

> [!theorem]
> Let $\Gamma$ be a primitive strongly regular graph with smallest eigenvalue $-m$, where $m$ is a positive integer. Then $\mu \leq m^3 (2m - 3)$.
> Known example: $m = 2$ and $m = 3$.

> [!theorem] Neumaier

> [!theorem] Improved Bound by Koolean

> [!remark]
> Improve from $\lambda = O(m^2 \mu)$ to $\lambda = O(m \mu)$.

> [!remark] Open Question
> If I have an $OA(n, t)$ $\mathcal O$ with $t$ close to $n$, can I extend $\mathcal O$ to an $OA(n, n + 1)$.
> $$\rightarrow n - t \leq O(n^{\frac{1}{3}})$$


