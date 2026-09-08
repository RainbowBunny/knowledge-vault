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

