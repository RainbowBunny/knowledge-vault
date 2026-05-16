## Baby-Step–Giant-Step Algorithm

> [!algorithm] Shanks’s Baby-Step–Giant-Step Algorithm
> **Input:** A group $G$, an element $g \in G$ of order $N \ge 2$, and an element $h \in G$  
> **Output:** An integer $x$ such that $g^x = h$
> 
> ---
>
> 1. Let
>    $$n \gets 1 + \lfloor \sqrt{N} \rfloor,$$
>    so in particular $n > \sqrt{N}$.
>
> 2. Create two lists:
>    - **List 1 (baby steps):**
>      $$g^0, g^1, g^2, \ldots, g^n$$
>    - **List 2 (giant steps):**
>      $$h,\; h g^{-n},\; h g^{-2n},\; h g^{-3n},\; \ldots,\; h g^{-n^2}$$
>
> 3. Find a match between the two lists, that is, find integers $i, j$ such that
>    $$g^i = h g^{-j n}.$$
>
> 4. Output
>    $$x \gets i + j n,$$
>    which satisfies $g^x = h$.
> ---
> **Complexity of the algorithm**: $\mathcal O(\sqrt{N} \cdot \log N)$ steps.

