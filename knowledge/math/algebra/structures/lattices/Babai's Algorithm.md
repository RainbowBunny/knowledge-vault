## Babai's Algorithm

> [!algorithm] Babai’s Closest Vertex Algorithm
> **Input:**  
> - A lattice $L \subset \mathbb{R}^n$ with basis $(v_1, v_2, \ldots, v_n)$  
> - A target vector $w \in \mathbb{R}^n$
>
> **Output:**  
> A lattice vector $v \in L$ approximating the closest lattice vector to $w$
>
> ---
>
> 1. Express the target vector in the basis:
>    $$w = t_1 v_1 + t_2 v_2 + \cdots + t_n v_n,$$
>    where $t_1, t_2, \ldots, t_n \in \mathbb{R}$.
>
> 2. For each $i = 1, 2, \ldots, n$, set:
>    $$a_i \gets \lfloor t_i \rceil,$$
>    where $\lfloor \cdot \rceil$ denotes rounding to the nearest integer.
>
> 3. Return the lattice vector:
>    $$v \gets a_1 v_1 + a_2 v_2 + \cdots + a_n v_n.$$
