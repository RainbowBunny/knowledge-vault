## Formulation

> [!definition] Discrete Logarithm Language
> Let $\mathcal L_\text{DLog}(\mathbb G, g)$ denote, for a cyclic group $(\mathbb G, \cdots)$ with a generator $g$, the following language:
> $$\mathcal L_\text{DLog}(\mathbb G, g) = \{h \in \mathbb G \; | \; \exists x \in \mathbb Z, g^x = h\}.$$

## Diffie-Hellman Decision Problem

> [!definition] Diffie-Hellman Decision Problem
> Let $p$ be a prime and let $g$ be an integer. The **Diffie-Hellman Decision Problem** is as follow:
> Suppose that you are given three numbers $A$, $B$, and $C$, and suppose that $A$ and $B$ are equal to $$A \equiv g^a \pmod p \quad \text{and} \quad B \equiv g^b \pmod p,$$ but that you do not necessarily know the values of the exponents $a$ and $b$. Determine whether $C$ is equal to $g^{ab} \pmod p$.

## Complexity Bound for DLP

> [!proposition] Trivial Bound for DLP
> Let $G$ be a group and let $g \in G$ be an element of order $N$. (Recall that this means that $g^N = e$ and that no smaller positive power of $g$ is equal to the identity element $e$.) Then the discrete logarithm problem $$g^x = h$$ can be solved in $\mathcal O (N)$ steps, where each step consists of multiplication by $g$.

