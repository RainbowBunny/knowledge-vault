## Bounds in coding theory

### The Main Coding Theory Problem

> [!definition] Relative Minimum Distance
> For a $q$-ary code $C$ with parameters $(n, M, d)$, the **relative minimum distance** of $C$ is defined to be $\delta(C) = (d - 1) / n$

> [!definition] Optimal code
> For a given code alphabet $A$ of size $q$ (with $q > 1$) and given values of $n$ and $d$, let $A_q(n, d)$ denote the largest possible size $M$ for which there exists an $(n, M, d)$-code over $A$. Thus, $$A_q(n, d) = \max \{M : \text{there exists an } (n, M, d)\text{-code over } A\}.$$ Any $(n, M, d)$-code $C$ that has the maximum size, that is, for which $M = A_q(n, d)$, is called an **optimal code**.

> [!definition] Main Coding Theory Problem
> The problem of determining the values of $A_q(n, d)$ is sometimes known as the **main coding theory problem**.

> [!definition] Linear Codes Version
> For a given prime power $q$ and given values of $n$ and $d$, let $B_q(n, d)$ denote the largest possible size $q^k$ for which there exists an $[n, k, d]$-code over $\mathbb F_q$. Thus, $$B_q(n, d) = \max\{q^k : \text{there exists an } [n, k, d]\text{-code over } \mathbb F_q\}.$$

> [!theorem]
> Let $q \geq 2$ be a prime power. Then
> 1. $B_q(n, d) \leq A_q(n, d) \leq q^n$ for all $1 \leq d \leq n$;
> 2. $B_q(n, 1) = A_q(n, 1) = q^n$;
> 3. $B_q(n, n) = A_q(n, n) = q$.

> [!definition] Extended Code
> For any code $C$ over $\mathbb F_q$, the **extended code** of $C$, denoted by $\overline{C}$, is defined to be $$\overline{C} = \{(c_1, \dots, c_n, - \sum_{i = 1}^n c_i) : (c_1, \dots, c_n) \in C\}.$$ When $q = 2$, the extra coordinate is called the **parity-check** coordinate.

> [!theorem]
> If $C$ is an $(n, M, d)$-code over $\mathbb F_q$, then $\overline{C}$ is an $(n + 1, M, d')$-code over $\mathbb F_q$, with $d \leq d' \leq d + 1$. If $C$ is linear, then so is $\overline{C}$. Moreover, when $C$ is linear, $$\begin{pmatrix}H & 0 \\ \textbf{1} & 1\end{pmatrix}$$ is a parity-check matrix of $\overline{C}$ if $H$ is a parity-check matrix of $C$.

> [!theorem]
> Suppose $d$ is odd.
> 1. Then a binary $(n, M, d)$-code exists if and only if a binary $(n + 1, M, d + 1)$-code exists. Therefore, if $d$ is odd, $A_2(n + 1, d + 1) = A_2(n, d)$.
> 2. Similarly, a binary $[n, k, d]$-linear code exists if and only if a binary $[n + 1, k, d + 1]$-linear code exists, so $B_2(n + 1, d + 1) = B_2(n, d)$.

### Lower Bounds

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

### Hamming Bound and Perfect Codes



### Reed-Muller Codes

> [!definition] First Order Reed-Muller codes
> The **(first order) Reed-Muller codes** $\mathcal R(1, m)$ are binary codes defined, for all integers $m \geq 1$, recursively as follows:
> 1. $\mathcal R(1, 1) = \mathbb F_2^2 = \{00, 01, 10, 11\}$;
> 2. For $m \geq 1$, $$\mathcal R(1, m + 1) = \{(u, u): u \in \mathcal R(1, m)\} \cup \{(u, u + 1): u \in \mathcal R(1, m)\}.$$

> [!proposition]
> For $m \geq 1$, the Reed-Muller code $\mathcal R(1, m)$ is a binary $[2^m, m + 1, 2^{m - 1}]$-linear code, in which every codeword except $0$ and $1$ has weight $2^{m - 1}$.

> [!proposition]
> 1. A generator matrix of $\mathcal R(1, 1)$ is $$\begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}$$
> 2. If $G_m$ is a generator matrix for $\mathcal R(1, m)$, then a generator matrix for $\mathcal R(1, m + 1)$ is $$G_{m + 1} = \begin{pmatrix}G_m & G_m \\ 0\cdots 0 & 1\cdots 1\end{pmatrix}$$

> [!proposition]
> The dual code $\mathcal R(1, m)^{\perp}$ is (equivalent to) the extended binary Hamming code $\overline{\text{Ham}(m, 2)}$.

> [!definition] $r$-th order Reed-Muller codes
> 1. The zeroth order Reed-Muller codes $\mathcal R(0, m)$, for $m \geq 0$, are defined to be the repetitions codes $\{0, 1\}$ of length $2^m$.
> 2. For any $r \geq 2$, the $r$th order Reed-Muller codes $\mathcal R(r, m)$ are defined, for $m \geq r - 1$, recursively by $$\mathcal R(r, m + 1) = \begin{cases}\mathbb F_2^{2^r} &\text{ if } m = r - 1 \\ \{(u, u + v) : u \in \mathcal R(r, m), v \in \mathcal R(r - 1, m)\} &\text{ if } m > r - 1\end{cases}$$

> [!proposition]
> $\mathcal R(r, m)$ is a linear code with parameter $[2^m, \sum_{i = 0}^r \binom{m}{i}, 2^{m - r}]$

### First-order Reed-Muller codes



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

