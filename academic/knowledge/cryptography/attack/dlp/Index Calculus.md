## The Index Calculus Method

> [!algorithm] Index Calculus Method for the Discrete Logarithm Problem
> **Input:** A finite cyclic group $G = \langle g \rangle$ of order $N$,
> and an element $h \in G$  
> **Output:** An integer $x$ such that $g^x = h$
>
> ---
>
> ### Phase 1: Factor Base Selection
>
> 1. Choose a factor base
>    $$\mathcal{B} = \{p_1, p_2, \ldots, p_m\} \subset G$$
>    consisting of “small” elements.
>
> ---
>
> ### Phase 2: Relation Collection
>
> 2. Repeat until sufficiently many independent relations are obtained:
>
>    2.1. Choose a random integer $k$ with $0 \le k < N$.
>
>    2.2. Compute:
>    $$g^k \in G.$$
>
>    2.3. If $g^k$ factors completely over the factor base,
>    $$g^k = \prod_{j=1}^m p_j^{e_{j}},$$
>    record the relation:
>    $$k \equiv \sum_{j=1}^m e_{j} \log_g(p_j) \pmod N.$$
>
> ---
>
> ### Phase 3: Linear Algebra
>
> 3. Solve the resulting system of linear equations modulo $N$ to
>    determine $\log_g(p_j)$ for each $p_j \in \mathcal{B}$.
>
> ---
>
> ### Phase 4: Individual Logarithm
>
> 4. Find an integer $k'$ such that:
>    $$h \cdot g^{k'}$$
>    factors completely over the factor base:
>    $$h \cdot g^{k'} = \prod_{j=1}^m p_j^{e'_j}.$$
>
> 5. Compute:
>    $$x \equiv -k' + \sum_{j=1}^m e'_j \log_g(p_j) \pmod N.$$
>
> 6. Output $x$.

