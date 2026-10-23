Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (Springer), chapter on elliptic curves, incl. Exercise 5.19: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[LMFDB]` — The LMFDB Collaboration, _Discriminant of an elliptic curve_ (knowl ec.discriminant): https://lmfdb.org/knowledge/show/ec.discriminant
- `[Gal12]` — S. D. Galbraith, _Mathematics of Public Key Cryptography_ (CUP 2012), Chapter 9 Elliptic Curves (eq. (9.1), (9.2), (9.11), Cor 9.10.9): https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch9.pdf

## Definition

> [!definition] Parameters
> - $K$: a [[Field]] of any characteristic.
> - $a_1, a_2, a_3, a_4, a_6 \in K$: the coefficients.
> - $b_2, b_4, b_6, b_8$: auxiliary quantities, defined below.
> - $\Delta$: the discriminant.
> - $\mathcal O$: the point at infinity.

> [!definition] Generalized Elliptic Curve
> Generalizes:: [[Elliptic Curve]].
>
> ---
> An **elliptic curve** $E$ is the set of solutions to a **generalized** Weierstrass equation $$E: Y^2 + a_1 XY + a_3 Y = X^3 + a_2 X^2 + a_4 X + a_6$$ together with an extra point $\mathcal O$. The coefficients $a_1, \dots, a_6$ are required to satisfy $\Delta \neq 0$, where the **discriminant** $\Delta$ is defined in terms of certain quantities $b_2, b_4, b_6, b_8$ as follows:
> $$b_2 = a_1^2 + 4a_2$$
> $$b_4 = 2a_4 + a_1 a_3$$
> $$b_6 = a_3^2 + 4a_6$$
> $$b_8 = a_1^2 a_6 + 4 a_2 a_6 - a_1 a_3 a_4 + a_2 a_3^2 - a_4^2$$
> $$\Delta = -b_2^2 b_8 - 8b_4^3 - 27b_6^2 + 9 b_2 b_4 b_6.$$
>
> `[HPS]` `[LMFDB]` `[Gal12 (9.1)]`

### Point Addition

> [!algorithm] Exercise 5.19: Point Addition on a Generalized Weierstrass Curve
> - $P_3 \leftarrow \mathsf{Add}(P_1, P_2)$: Deterministic point addition.
>     - **Input**: an elliptic curve $$E : Y^2 + a_1 X Y + a_3 Y = X^3 + a_2 X^2 + a_4 X + a_6$$ and two points $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$ on $E$.
>     - **Output**: the sum $P_3 = P_1 + P_2$.
>     - **Steps**:
>         1. (**Check for the point at infinity**) If both
>             - $x_1 = x_2$
>             - $y_1 + y_2 + a_1 x_2 + a_3 = 0$
>
>             then $$P_1 + P_2 = \mathcal{O}.$$
>         2. (**Compute $\lambda$ and $\nu$**) If $x_1 \neq x_2$, define $$\lambda = \frac{y_2 - y_1}{x_2 - x_1},$$ $$\nu = \frac{y_1 x_2 - y_2 x_1}{x_2 - x_1}.$$
>         3. If $x_1 = x_2$, define $$\lambda = \frac{3x_1^2 + 2a_2 x_1 + a_4 - a_1 y_1}{2y_1 + a_1 x_1 + a_3},$$ $$\nu = \frac{-x_1^3 + a_4 x_1 + 2a_6 - a_3 y_1}{2y_1 + a_1 x_1 + a_3}.$$
>         4. (**Compute the sum**) Set $$x_3 = \lambda^2 + a_1 \lambda - a_2 - x_1 - x_2,$$ $$y_3 = -(\lambda + a_1) x_3 - \nu - a_3.$$
>         5. Output $$P_3 = (x_3, y_3).$$
>
> `[HPS Ex 5.19]` `[Gal12 (9.2)]` — [Gal12] writes $y_3 = -\lambda(x_3 - x_1) - y_1 - a_1 x_3 - a_3$, the same value since $\nu = y_1 - \lambda x_1$.

### Frobenius Map

> [!definition] Parameters
> - $p$: a [[Prime]].
> - $k \geq 1$: an integer.

> [!definition] p-power Frobenius map
> The (p-power) Frobenius map $\tau$ is the map from the field $\mathbb F_{p^k}$ to itself defined by the simple rule
> $$\tau: \mathbb F_{p^k} \rightarrow \mathbb F_{p^k},$$
> $$\tau(\alpha) = \alpha^p.$$
>
> `[HPS]`

> [!proposition] Property of p-power Frobenius map — $\tau$ preserves addition and multiplication
> The map preserves addition and multiplication:
> $$\tau(\alpha + \beta) = \tau(\alpha) + \tau(\beta)$$
> $$\tau(\alpha \cdot \beta) = \tau(\alpha) \cdot \tau(\beta)$$
>
> `[HPS]`

## Property

> [!theorem] Point counts over extensions — $\#E(\mathbb F_{p^k}) = p^k + 1 - \alpha^k - \beta^k$, and Frobenius satisfies $\tau^2 - t\tau + p = 0$
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $$t = p + 1 - \# E(\mathbb F_p).$$
> 1. Let $\alpha$ and $\beta$ be the complex roots of the quadratic polynomial $Z^2 - tZ + p$. Then $|\alpha| = |\beta| = \sqrt{p}$, and for every $k \geq 1$ we have $$\# E(\mathbb F_{p^k}) = p^k + 1 - \alpha^k - \beta^k.$$
> 2. Let $$\tau: E(\mathbb F_{p^k}) \rightarrow E(\mathbb F_{p^k}),$$ $$(x, y) \rightarrow (x^p, y^p),$$ be the Frobenius map. Then for every point $Q \in E(\mathbb F_{p^k})$ we have $$\tau^2(Q) - t \tau(Q) + p \cdot Q = 0,$$ where $\tau^2(Q)$ denotes the composition $\tau(\tau(Q))$.
>
> `[HPS]` `[Gal12 (9.11), Cor 9.10.9]`

## Related

### Descendants
- [[Koblitz Curve]] — $a_1 = 1$, $a_2 = a$, $a_3 = a_4 = 0$, $a_6 = 1$ over $\mathbb F_2$

### Siblings
- [[Elliptic Curve]] — the short form $a_1 = a_2 = a_3 = 0$, enough in characteristic $\neq 2, 3$
- [[Elliptic Curves over Finite Fields]] — Hasse's bound, the case $k = 1$ of the point count
