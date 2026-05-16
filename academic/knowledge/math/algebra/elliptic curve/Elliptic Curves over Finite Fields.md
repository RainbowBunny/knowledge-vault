## Elliptic Curves over Finite Fields

> [!definition] Elliptic Curve over $\mathbb F_p$
> An **elliptic curve over** $\mathbb F_p$ is an equation of the form $$E: Y^2 = X^3 + AX + B \qquad \text{with } A, B \in \mathbb F_p \text{ satisfying } 4A^3 + 27B^2 \neq 0,$$ and then we look at the points on $E$ with coordinates in $\mathbb F_p$, which we denote by $$E(\mathbb F_p) = \{(x, y): x, y \in \mathbb F_p \text{ satisfy } y^2 = x^3 + Ax + B\} \cup \{\mathcal O\}.$$

> [!theorem]
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $P$ and $Q$ be points in $E(\mathbb F_p).$
> 1. The elliptic curve addition algorithm applied to $P$ and $Q$ yields a point in $E(\mathbb F_p)$. We denote this point by $P + Q$.
> 2. This addition law makes $E(\mathbb F_p)$ into a [[Algebra Structure#Group|Finite Group]].

> [!theorem] Hasse
> Let $E$ be an elliptic curve over $\mathbb F_p$. Then $$\#(\mathbb F_p) = p + 1 - t_p \quad \text{with } t_p \text{ satisfying } |t_p| \leq 2 \sqrt{p}.$$
> Let $E$ be an elliptic curve over $\mathbb F_{p^k}$. Then $$\#(\mathbb F_{p^k}) = p^k + 1 - t_{p^k} \quad \text{with } t_{p^k} \text{ satisfying } |t_{p^k}| \leq 2p^{k/2}.$$

> [!definition] Trace of Frobenius
> The quantity $$t_p = p + 1 - \#(\mathbb F_p)$$ is called the **trace of Frobenius** for $E / \mathbb F_p$.

> [!algorithm] Double-and-Add Algorithm for Elliptic Curves
> **Input:**  
> A point $P \in E(\mathbb{F}_p)$ and an integer $n \ge 1$
>
> **Output:**  
> The point $nP \in E(\mathbb{F}_p)$
>
> ---
>
> 1. Initialize:
>    $$Q \gets P, \qquad R \gets \mathcal{O}.$$
>
> 2. While $n > 0$, do:
>
>    2.1. If
>    $$n \equiv 1 \pmod 2,$$
>    then set:
>    $$R \gets R + Q.$$
>
>    2.2. Set:
>    $$Q \gets 2Q.$$
>
>    2.3. Set:
>    $$n \gets \lfloor n / 2 \rfloor.$$
>
> 3. Return $R$, which equals $nP$.
> ---
> **Complexity of the algorithm**: $2 \log_2 n$ point operations

> [!remark]
> The fastest known algorithm to solve ECDLP in $E(\mathbb F_p)$ takes approximately $\sqrt{p}$ steps.
