Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (Springer), chapter on elliptic curves: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[Gal12]` — S. D. Galbraith, _Mathematics of Public Key Cryptography_ (CUP 2012), Chapter 9 Elliptic Curves (Thm 9.10.7): https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch9.pdf

## Definition

> [!definition] Parameters
> - $p \geq 3$: a [[Prime]].
> - $A, B \in \mathbb F_p$: the coefficients.
> - $\mathcal O$: the point at infinity.

> [!definition] Elliptic Curve over $\mathbb F_p$
> Extends:: [[Elliptic Curve]].
>
> ---
> An **elliptic curve over** $\mathbb F_p$ is an equation of the form $$E: Y^2 = X^3 + AX + B$$ with $A, B \in \mathbb F_p$ satisfying $$4A^3 + 27B^2 \neq 0,$$ and then we look at the points on $E$ with coordinates in $\mathbb F_p$, which we denote by $$E(\mathbb F_p) = \{(x, y): x, y \in \mathbb F_p \text{ satisfy } y^2 = x^3 + Ax + B\} \cup \{\mathcal O\}.$$
>
> `[HPS]`

### Trace of Frobenius

> [!definition] Parameters
> - $E$: an elliptic curve over $\mathbb F_p$.

> [!definition] Trace of Frobenius
> The quantity $$t_p = p + 1 - \#E(\mathbb F_p)$$ is called the **trace of Frobenius** for $E / \mathbb F_p$.
>
> `[HPS]` `[Gal12 Thm 9.10.7]`

### Double-and-Add

> [!algorithm] Double-and-Add Algorithm for Elliptic Curves
> - $R \leftarrow \mathsf{DoubleAndAdd}(P, n)$: Deterministic scalar multiplication.
>     - **Input**: a point $P \in E(\mathbb{F}_p)$ and an integer $n \ge 1$.
>     - **Output**: the point $nP \in E(\mathbb{F}_p)$.
>     - **Steps**:
>         1. Initialize: $$Q \gets P,$$ $$R \gets \mathcal{O}.$$
>         2. While $n > 0$, do:
>             1. If $$n \equiv 1 \pmod 2,$$ then set: $$R \gets R + Q.$$
>             2. Set: $$Q \gets 2Q.$$
>             3. Set: $$n \gets \lfloor n / 2 \rfloor.$$
>         3. Return $R$, which equals $nP$.
>
> **Complexity of the algorithm**: $2 \log_2 n$ point operations
>
> `[HPS]`

## Property

> [!theorem] Group law over $\mathbb F_p$ — the addition algorithm stays in $E(\mathbb F_p)$ and makes it a finite group
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $P$ and $Q$ be points in $E(\mathbb F_p).$
> 1. The elliptic curve addition algorithm applied to $P$ and $Q$ yields a point in $E(\mathbb F_p)$. We denote this point by $P + Q$.
> 2. This addition law makes $E(\mathbb F_p)$ into a [[Group|Finite Group]].
>
> `[HPS]`

> [!theorem] Hasse's theorem — $\#E(\mathbb F_q)$ differs from $q + 1$ by at most $2\sqrt q$
> Let $E$ be an elliptic curve over $\mathbb F_p$. Then $$\#E(\mathbb F_p) = p + 1 - t_p,$$ with $t_p$ satisfying $|t_p| \leq 2 \sqrt{p}$.
> Let $E$ be an elliptic curve over $\mathbb F_{p^k}$. Then $$\#E(\mathbb F_{p^k}) = p^k + 1 - t_{p^k},$$ with $t_{p^k}$ satisfying $|t_{p^k}| \leq 2p^{k/2}$.
>
> `[HPS]` `[Gal12 Thm 9.10.7]`

> [!remark]
> The fastest known algorithm to solve ECDLP in $E(\mathbb F_p)$ takes approximately $\sqrt{p}$ steps.

## Related

### Constructions
- [[Weil Pairing over Prime Power Fields]] — embedding degree and distortion maps over $\mathbb F_p$

### Siblings
- [[Generalized Elliptic Curves]] — the Frobenius map and $\#E(\mathbb F_{p^k})$ for all $k$
- [[Koblitz Curve]] — over $\mathbb F_2$, where the short equation above is not available
