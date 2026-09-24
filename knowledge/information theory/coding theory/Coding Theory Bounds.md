## Bounds in coding theory

### The Main Coding Theory Problem

> [!definition] Relative Minimum Distance
> For a $q$-ary code $\mathcal C$ with parameters $(n, M, d)$, the **relative minimum distance** of $\mathcal C$ is defined to be $\delta(\mathcal C) = (d - 1) / n$

> [!definition] Optimal code
> For a given code alphabet $A$ of size $q$ (with $q > 1$) and given values of $n$ and $d$, let $A_q(n, d)$ denote the largest possible size $M$ for which there exists an $(n, M, d)$-code over $A$. Thus, $$A_q(n, d) = \max \{M : \text{there exists an } (n, M, d)\text{-code over } A\}.$$ Any $(n, M, d)$-code $\mathcal C$ that has the maximum size, that is, for which $M = A_q(n, d)$, is called an **optimal code**.

> [!definition] Optimal Weighted Code
> Define $A_q(n, d, w)$ to be the maximum number of codewords in a constant weight $(n, M)$ code over $\mathbb F_q$ of length $n$ and minimum distance at least $d$ whose codewords have weight $w$. Obviously, $A_q(n, d, w) \leq A_q(n, d)$.

> [!definition] Main Coding Theory Problem
> The problem of determining the values of $A_q(n, d)$ is sometimes known as the **main coding theory problem**.

> [!definition] Linear Codes Version
> For a given prime power $q$ and given values of $n$ and $d$, let $B_q(n, d)$ denote the largest possible size $q^k$ for which there exists an $[n, k, d]$-code over $\mathbb F_q$. Thus, $$B_q(n, d) = \max\{q^k : \text{there exists an } [n, k, d]\text{-code over } \mathbb F_q\}.$$

> [!theorem]
> Let $q \geq 2$ be a prime power. Then
> 1. $B_q(n, d) \leq A_q(n, d) \leq q^n$ for all $1 \leq d \leq n$;
> 2. $B_q(n, 1) = A_q(n, 1) = q^n$;
> 3. $B_q(n, n) = A_q(n, n) = q$.

> [!theorem]
> If $\mathcal C$ is an $(n, M, d)$-code over $\mathbb F_q$, then [[New Codes from Old#Extending Codes|Extended Code]] $\widehat{\mathcal C}$ is an $(n + 1, M, d')$-code over $\mathbb F_q$, with $d \leq d' \leq d + 1$. If $C$ is linear, then so is $\overline{\mathcal C}$. Moreover, when $\mathcal C$ is linear, $$\begin{pmatrix}H & 0 \\ \textbf{1} & 1\end{pmatrix}$$ is a parity-check matrix of $\widehat{\mathcal C}$ if $H$ is a parity-check matrix of $\mathcal C$.

> [!theorem]
> Suppose $d$ is odd.
> 1. Then a binary $(n, M, d)$-code exists if and only if a binary $(n + 1, M, d + 1)$-code exists. Therefore, if $d$ is odd, $A_2(n + 1, d + 1) = A_2(n, d)$.
> 2. Similarly, a binary $[n, k, d]$-linear code exists if and only if a binary $[n + 1, k, d + 1]$-linear code exists, so $B_2(n + 1, d + 1) = B_2(n, d)$.

### Sphere-Covering Lower Bounds

> [!definition] Sphere
> Let $A$ be an alphabet of size $q$, where $q > 1$. For any vector $u \in A^n$ and any integer $r \geq 0$, the **sphere** of radius $r$ and center $u$, denoted $S_A(u, r)$, is the set $\{v \in A^n : d(u, v) \leq r\}$.

> [!definition] 
> For a given integer $q > 1$, a positive integer $n$ and an integer $r \geq 0$, define $V_q^n(r)$ to be $$V_q^n(r) = \begin{cases}\binom{n}{0} + \binom{n}{1} (q - 1) + \cdots + \binom{n}{r} (q - 1)^r &\text{ if } 0 \leq r \leq n\\ q^n & \text{ if } n \leq r\end{cases}$$

> [!lemma]
> For all integers $r \geq 0$, a sphere of radius $r$ in $A^n$ contains exactly $V_q^n(r)$ vectors, where $A$ is an alphabet of size $q > 1$.

> [!theorem] Sphere-covering bound
> For an integer $q > 1$ and integers $n, d$ such that $1 \leq d \leq n$, we have $$\frac{q^n}{V_q^n(d - 1)} = \frac{q^n}{\sum_{i = 0}^{d - 1} \binom{n}{i} (q - 1)^i} \leq A_q(n, d)$$

> [!theorem] Gilbert-Varshamov Bound
> Let $n, k$ and $d$ be integers satisfying $2 \leq d \leq n$ and $1 \leq k \leq n$. If $$\sum_{i = 0}^{d - 2} \binom{n - 1}{i} (q - 1)^i < q^{n - k},$$ then there exists an $[n, k]$ linear code over $\mathbb F_q$ with minimum distance at least $d$.

> [!corollary]
> For a prime power $q > 1$ and integers $n, d$ such that $2 \leq d \leq n$, we have $$B_q(n, d) \geq q^{n - \lceil \log_q (V_q^{n - 1}(d - 2) + 1) \rceil} \geq \frac{q^{n - 1}}{V_q^{n - 1}(d - 2)}$$

### Plotkin Upper Bound

> [!theorem] Plotkin Bound
> Let $\mathcal C$ be an $(n, M, d)$ code over $\mathbb F_q$ such that $rn < d$ where $r = 1 - q^{-1}$. Then,
> $$M \leq \left\lfloor \frac{d}{d - rn} \right\rfloor$$
> In particular,
> $$A_q(n, d) \leq \left\lfloor \frac{d}{d - rn} \right\rfloor,$$
> provided $rn < d$. In the binary case,
> $$A_2(n, d) \leq 2 \left\lfloor \frac{d}{2d - n} \right\rfloor$$
> if $n < 2d$.

> [!corollary]
> The following bounds hold:
> 1. If $d$ is even, $A_2(2d, d) \leq 4d$.
> 2. If $d$ is odd, $A_2(2d, d) \leq 2d + 2$.
> 3. If $d$ is odd, $A_2(2d + 1, d) \leq 4d + 4$.

### Johnson Upper Bounds

> [!theorem]
> If $\mathcal C$ is a constant weight $(n, M, d)$ code with codewords of weight $w$ and if $M > 1$, then $d \leq 2w$.

> [!theorem]
> 1. $A_q(n, d, w) = 1$ if $d > 2w$.
> 2. $A_q(n, 2w, w) \leq \lfloor (n(q - 1) / w) \rfloor$.
> 3. $A_2(n, 2w, w) = \lfloor n / w \rfloor$.
> 4. $A_2(n, 2e - 1, w) = A_2(n, 2e, w)$.

> [!theorem] Restricted Johnson Bound for $A_q(n, d, w)$
> $$A_q(n, d, w) \leq \left\lfloor \frac{nd(q - 1)}{qw^2 - 2(q - 1)nw + nd(q - 1)} \right\rfloor$$
> provided $qw^2 - 2(q - 1)nw + nd(q - 1) > 0$, and
> $$A_2(n, d, w) \leq \left\lfloor \frac{nd}{2w^2 - 2nw + nd} \right\rfloor$$
> provided $2w^2 - 2nw + nd > 0$.

> [!theorem] Unrestricted Johnson Bound for $A_q(n, d, w)$
> 1. If $2w < d$, then $A_q(n, d, w) = 1$.
> 2. If $2w \geq d$ and $d \in \{2e - 1, 2e\}$, then, setting $q^* = q - 1$,
> $$A_q(n, d, w) \leq \left \lfloor \frac{nq^*}{w} \left \lfloor \frac{(n - 1)q^*}{w - 1} \left \lfloor \cdots \left \lfloor \frac{(n - w + e) q^*}{e} \right \rfloor \dots \right \rfloor \right \rfloor \right \rfloor$$
> 3. If $w < e$, then $A_2(n, 2e - 1, w) = A_2(n, 2e, w) = 1$.
> 4. If $w \geq e$, then 
> $$A_2(n, 2e - 1, w) = A_2(n, 2e, w) \leq \left \lfloor \frac{n}{w} \left \lfloor \frac{n - 1}{w - 1} \left \lfloor \cdots \left \lfloor \frac{n - w + e}{e} \right \rfloor \dots \right \rfloor \right \rfloor \right \rfloor$$

> [!theorem] Johnson Bound for $A_q(n, d)$

### Hamming Bound and Perfect Codes


### Singleton Bound and MDS Codes

> [!theorem] Singleton Bound
> For any integer $q > 1$, any positive integer $n$ and any integer $d$ such that $1 \leq d \leq n$, we have $$A_q(n, d) \leq q^{n - d + 1}.$$
> In particular, when $q$ is a prime power, the parameters $[n, k, d]$ of any linear code over $\mathbb F_q$ satisfy $$k + d \leq n + 1.$$

> [!definition] Maximum Distance Separable (MDS) code
> A linear code with parameters $[n, k, d]$ such that $k + d = n + 1$ is called a **maximum distance separable (MDS)** code.

> [!theorem]
> Let $C$ be a linear code over $\mathbb F_q$ with parameters $[n, k, d]$. Let $G, H$ be a generator matrix and a parity-check matrix, respectively, for $C$. Then, the following statements are equivalent:
> 1. $C$ is an MDS code;
> 2. Every set of $n - k$ columns of $H$ is linearly independent;
> 3. Every set of $k$ columns of $G$ is linearly independent;
> 4. $C^{\perp}$ is an MDS code.

## Linear Code

### Quasi-Cyclic Codes

> [!definition] Quasi-Cyclic Codes
> View a vector $c = (c_0, \dots, c_{s - 1})$ of $\mathbb F_2^{sn}$ as $s$ successive blocks ($n$-tuples). An $[sn, k, d]$ linear code $C$ is Quasi-Cyclic (QC) of index $s$ if, for any $c = (c_0, \dots, c_{s - 1}) \in C$, the vector obtained after applying a simultaneous circular shift to every block $c_0, \dots, c_{s - 1}$ is also a codeword. More formally, by considering each block $c_i$ as a polynomial in $\mathcal R = \mathbb F_2[X] / (X^n - 1)$, the code $C$ is QC of index $s$ if for any $c = (c_0, \dots, c_{s - 1}) \in C$ it holds that $(X \cdot c_0, \dots, X \cdot c_{s - 1}) \in C$.

### Systematic Quasi-Cyclic Codes

> [!definition] Systematic Quasi-Cyclic Codes
> A systematic Quasi-Cyclic $[sn, n]$ code of index $s$ (number of blocks) and rate $1/s$ is a quasi-cyclic code with an $(s - 1)n \times sn$ parity-check matrix of the form: $$H = \begin{bmatrix}
> I_n & 0   & \cdots & 0   & A_0    \\
> 0   & I_n &        &     & A_1    \\
>     &     & \ddots &     & \vdots \\
> 0   &     & \cdots & I_n & A_{s - 2} \\    
> \end{bmatrix}$$ where $A_0, \dots, A_{s - 2}$ are circulant $n \times n$ matrices.

