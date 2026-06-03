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

