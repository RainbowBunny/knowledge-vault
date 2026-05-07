## Discrete Logarithm Problem

> [!definition] Discrete Logarithm Problem 
> Let $g$ be a primitive root for $\mathbb F_p$ and let $h$ be a nonzero element of $\mathbb F_p$. The **Discrete Logarithm Problem (DLP)** is the problem of finding an exponent $x$ such that $$g^x = h \pmod p$$The number $x$ is called the **discrete logarithm** of $h$ to the base $g$ and is denoted by $log_g(h)$.

> [!remark] 
> $log_g$ is a group isomorphism from $\mathbb F_p^*$ to $\mathbb Z / (p - 1)\mathbb Z$:
> 1. $\log_g(h_1 h_2) = \log_g(h_1) + \log_g(h_2) \forall h_1, h_2 \in \mathbb F_p^*$.
> 2. $\log_g(h^n) = n \log_g(h) \forall h \in \mathbb F_p^* \; \text{and} \; n \in \mathbb Z$.

> [!definition] Generalized Discrete Logarithm Problem
> Let $G$ be a group whose group law we denote by the symbol $\star$. The **Discrete Logarithm Problem** for $G$ is to determine, for any two given elements $g$ and $h$ in $G$, an integer $x$ satisfying $$\underbrace {g \star g \star g \star \cdots \star g}_{x \;\text{times}} = h.$$

## Diffie-Hellman Decision Problem

> [!definition] Diffie-Hellman Decision Problem
> Let $p$ be a prime and let $g$ be an integer. The **Diffie-Hellman Decision Problem** is as follow:
> Suppose that you are given three numbers $A$, $B$, and $C$, and suppose that $A$ and $B$ are equal to $$A \equiv g^a \pmod p \quad \text{and} \quad B \equiv g^b \pmod p,$$ but that you do not necessarily know the values of the exponents $a$ and $b$. Determine whether $C$ is equal to $g^{ab} \pmod p$.

## Complexity Bound for DLP

> [!proposition] Trivial Bound for DLP
> Let $G$ be a group and let $g \in G$ be an element of order $N$. (Recall that this means that $g^N = e$ and that no smaller positive power of $g$ is equal to the identity element $e$.) Then the discrete logarithm problem $$g^x = h$$ can be solved in $\mathcal O (N)$ steps, where each step consists of multiplication by $g$.

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

## Elliptic Curve Discrete Logarithm Problem

> [!definition] Elliptic Curve Discrete Logarithm Problem
> Let $E$ be an elliptic curve over the finite field $\mathbb F_p$ and let $P$ and $Q$ be points in $E(\mathbb F_p)$. The **Elliptic Curve Discrete Logarithm Problem (ECDLP)** is the problem of finding an integer $n$ such that $Q = nP$. By analogy with the discrete logarithm problem for $\mathbb F_p^*$, we denote this integer $n$ by $$n = \log_P(Q)$$ and we call $n$ the **elliptic curve logarithm** of $Q$ with respect to $P$.

> [!proposition]
> Let $s$ be the order of point $P$ in the elliptic curve $E(\mathbb F_p)$. We say that the map $\log_P$ defines a **group homomorphism** $$\log_P: E(\mathbb F_p) \rightarrow \mathbb Z/s\mathbb Z$$ 

## MOV Algorithm

> [!definition] Supersingular Elliptic Curves
> Elliptic curves $E$ over $\mathbb F_p$ satisfy $$\# E(\mathbb F_p) = p + 1$$ are called **supersingular elliptic curves** which have embedding degree $k \leq 6$.

> [!algorithm] The MOV Algorithm
> **Input:**  
> - An elliptic curve $E$ over $\mathbb{F}_p$  
> - A point $P \in E(\mathbb{F}_p)$ of prime order $n$
>
> **Output:**  
> An integer $\ell$ such that $P = \ell Q$, reducing the ECDLP to a DLP in a finite field
>
> ---
>
> 1. Compute the number of points:
>    $$N \gets \#E(\mathbb{F}_p).$$
>    This is feasible if the embedding degree $k$ is not too large.
>    Note that $n \mid N$, so any assumption that $E(\mathbb{F}_p)$ has a point of order $n$ is valid.
>
> 2. Choose a random point
>    $$T \in E(\mathbb{F}_{p^k}) \setminus E(\mathbb{F}_p).$$
>
> 3. Compute:
>    $$T' \gets \frac{N}{n} \, T.$$
>    If $T' = \mathcal{O}$, return to Step 2.
>    Otherwise, $T'$ has order $n$.
>
> 4. Compute the Weil pairings:
>    $$\alpha \gets e_n(P, T') \in \mathbb{F}_{p^k}^*, \qquad
>      \beta \gets e_n(Q, T') \in \mathbb{F}_{p^k}^*.$$
>
> 5. Solve the discrete logarithm problem in $\mathbb{F}_{p^k}^*$:
>    Find $\ell$ such that
>    $$\beta = \alpha^{\,\ell}.$$
>    This step can be performed efficiently using index calculus if $k$ is not too large.
>
> 6. Output $\ell$.

## Anomalous

> [!definition] Anomalous
> An elliptic curve $E$ over a finite field $\mathbb F_p$ is called **anomalous** if $\# E(\mathbb F_p) = p$.

## Hyper-Elliptic Curve Discrete Logarithm Problem

> [!definition] Hyperelliptic Curve
> A curve in the form $$y^2 = f(x) = ax^{2n + 2} + ...$$ is a hyperelliptic curve of genus $n$. The group of these curve is **not points**, but the **Jacobian** $J(C)$.

> [!definition] Mumford Representations
> On a genus-2 curve, group element are **reduced divisors** and represented in **Mumford form**: $$(u(x), v(x))$$ where:
> - $u(x)$ is monic and $\deg u(x) \leq 2$ 
> - $v(x)^2 \equiv f(x) \pmod {u(x)}$

> [!remark]
> For some situations, like with hyperelliptic curve, the order of the group might not be available, but we can guess the order of the element $g$ and check: $$\text{order} \cdot g = 1.$$
