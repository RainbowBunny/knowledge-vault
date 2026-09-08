## A Discrete Logarithm Collision Algorithm

> [!algorithm] Randomized Meet-in-the-Middle for Discrete Logarithms
> **Input:**  
> - A group $G$  
> - An element $h \in G$ of order $N$  
> - An element $b \in G$  
>
> **Output:**  
> An integer $x$ such that $h^x = b$, assuming a solution exists
>
> ---
>
> 1. Let
>    $$n \gets \lceil \sqrt{N} \rceil.$$
>
> 2. **Baby-step phase:**  
>    Choose random integers
>    $$y_1, y_2, \ldots, y_n \in \{1, 2, \ldots, N\}.$$
>    For each $i = 1, \ldots, n$, compute and store:
>    $$h^{y_i} \in G.$$
>
> 3. **Giant-step phase:**  
>    Choose random integers
>    $$z_1, z_2, \ldots, z_n \in \{1, 2, \ldots, N\}.$$
>    For each $j = 1, \ldots, n$, compute:
>    $$b \cdot h^{z_j} \in G.$$
>
> 4. **Collision search:**  
>    Look for indices $i, j$ such that
>    $$h^{y_i} = b \cdot h^{z_j}.$$
>
> 5. **Recover the discrete logarithm:**  
>    If a collision is found, output:
>    $$x \gets y_i - z_j \pmod N.$$
>
> ---
>
> **Guarantee:**  
> With high probability, a collision exists after $O(\sqrt{N})$
> group exponentiations, yielding a solution.

