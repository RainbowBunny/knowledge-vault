## The Pohlig–Hellman algorithm

> [!algorithm] Pohlig–Hellman Algorithm
> **Input:** A group $G$, an element $g \in G$ of order
> $$N = q_1^{e_1} q_2^{e_2} \cdots q_t^{e_t},$$
> and an element $h \in G$
>
> **Output:** An integer $x$ such that $g^x = h$
> 
> ---
>
> 1. For each $1 \le i \le t$, do the following:
>
>    1.1. Define:
>    $$g_i \gets g^{N / q_i^{e_i}}, \qquad h_i \gets h^{N / q_i^{e_i}}.$$
>
>    1.2. Observe that $g_i$ has order $q_i^{e_i}$.
>    Use the given algorithm for discrete logarithms in prime-power order groups
>    to solve:
>    $$g_i^{\,y_i} = h_i.$$
>
>    1.3. Let $y_i$ be a solution to the above equation.
>
> 2. Use the Chinese Remainder Theorem to solve the system of congruences:
>    $$\begin{aligned}
>    x &\equiv y_1 \pmod{q_1^{e_1}}, \\
>    x &\equiv y_2 \pmod{q_2^{e_2}}, \\
>    &\ \vdots \\
>    x &\equiv y_t \pmod{q_t^{e_t}}.
>    \end{aligned}$$
>
> 3. Output the solution $x$, which satisfies $g^x = h$.
> 
> **Complexity of the algorithm**: $\mathcal O(\sum_{i = 1}^t S_{q_i^{e_i}} + \log N)$ steps where $S_{q_i^{e_i}}$ is the complexity of solving the DLP problem for $q_i^{e_i}$.

> [!proposition] 
> Let $G$ be a group. Suppose that $q$ is a prime, and suppose that we know an algorithm that takes $S_q$ step to solve the discrete logarithm problem $g^x = h$ in $G$ whenever $g$ has order $q$. Now let $g \in G$ be an element of order $q^e$ with $e \geq 1$. Then we can solve the discrete logarithm problem $$g^x = h \quad \text{in} \; \mathcal O(eS_q) \; \text{steps}.$$

> [!algorithm] Discrete Logarithm for Prime-Power Order Groups
> **Input:**  
> - A group $G$  
> - An element $g \in G$ of order $q^e$, where $q$ is prime and $e \ge 1$  
> - An element $h \in G$
>
> **Output:**  
> An integer $x$ such that $g^x = h$
>
> ---
>
> 1. Write the unknown exponent $x$ in base $q$:
>    $$x = x_0 + x_1 q + x_2 q^2 + \cdots + x_{e-1} q^{e-1},$$
>    where $0 \le x_i < q$.
>
> 2. For $i = 0$ to $e-1$, determine $x_i$ as follows:
>
>    2.1. Compute:
>    $$g_i \gets g^{q^{e-1}},$$
>    which has order $q$.
>
>    2.2. Compute:
>    $$h_i \gets
>    \left(
>      h \cdot g^{-(x_0 + x_1 q + \cdots + x_{i-1} q^{i-1})}
>    \right)^{q^{e-1-i}}.$$
>
>    2.3. Solve the discrete logarithm in the order-$q$ subgroup:
>    $$g_i^{\,x_i} = h_i,$$
>    using the assumed algorithm that runs in $S_q$ steps.
>
> 3. Output:
>    $$x = x_0 + x_1 q + x_2 q^2 + \cdots + x_{e-1} q^{e-1}.$$
> ---
> **Complexity of the algorithm**: $\mathcal O(e S_q)$.

