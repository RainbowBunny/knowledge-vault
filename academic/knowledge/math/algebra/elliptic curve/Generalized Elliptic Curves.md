## Generalized Version of Elliptic Curve

> [!definition] Generalized Elliptic Curve
> An **elliptic curve** $E$ is the set of solutions to a **generalized** Weierstrass equation $$E: Y^2 + a_1 XY + a_3 Y = X^3 + a_2 X^2 + a_4 X + a_6$$ together with an extra point $\mathcal O$. The coefficients $a_1, \dots, a_6$ are required to satisfy $\Delta \neq 0$, where the **discriminant** $\Delta$ is defined in terms of certain quantities $b_2, b_4, b_6, b_8$ as follows: 
> $$b_2 = a_1^2 + 4a_2, \quad b_4 = 2a_4 + a_1 a_3, \quad b_6 = a_3^2 + 4a_6$$
> $$b_8 = a_1^2 a_6 + 4 a_2 a_6 - a_1 a_3 a_$ + a_2 a_3^2 - a_4^2$$ 
> $$\Delta = -b_2^2 b_8 - 8b_4^3 - 27b_6^2 + 9 b_2 b_4 b_6.$$

> [!algorithm] Exercise 5.19: Point Addition on a Generalized Weierstrass Curve
> **Input**
> - An elliptic curve
>   $$
>   E : Y^2 + a_1 X Y + a_3 Y = X^3 + a_2 X^2 + a_4 X + a_6
>   $$
> - Two points $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$ on $E$
>
> **Output**
> - The sum $P_3 = P_1 + P_2$
>
> ---
>
> **Step 1: Check for the Point at Infinity**
> 1. If $x_1 = x_2$ and
>    $$y_1 + y_2 + a_1 x_2 + a_3 = 0,$$
>    then
>    $$P_1 + P_2 = \mathcal{O}.$$
>
> **Step 2: Compute $\lambda$ and $\nu$**
> 2. If $x_1 \neq x_2$, define
>    $$\lambda = \frac{y_2 - y_1}{x_2 - x_1},
>    \qquad
>    \nu = \frac{y_1 x_2 - y_2 x_1}{x_2 - x_1}.$$
>
> 3. If $x_1 = x_2$, define
>    $$\lambda = \frac{3x_1^2 + 2a_2 x_1 + a_4 - a_1 y_1}
>                    {2y_1 + a_1 x_1 + a_3},$$
>    $$\nu = \frac{-x_1^3 + a_4 x_1 + 2a_6 - a_3 y_1}
>               {2y_1 + a_1 x_1 + a_3}.$$
>
> **Step 3: Compute the Sum**
> 1. Set
>    $$x_3 = \lambda^2 + a_1 \lambda - a_2 - x_1 - x_2,$$
>    $$y_3 = -(\lambda + a_1) x_3 - \nu - a_3.$$
>
> 2. Output
>    $$P_3 = (x_3, y_3).$$


> [!definition] p-power Frobenius map
> The (p-power) Frobenius map $\tau$ is the map from the field $\mathbb F_{p^k}$ to itself defined by the simple rule $$\tau: \mathbb F_{p^k} \rightarrow \mathbb F_{p^k}, \quad \tau(\alpha) = \alpha^p.$$

> [!proposition] Property of p-power Frobenius map
> The map preserves addition and multiplication: $$\tau(\alpha + \beta) = \tau(\alpha) + \tau(\beta) \quad \text{and} \quad \tau(\alpha \cdot \beta) = \tau(\alpha) \cdot \tau(\beta)$$

> [!theorem]
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $$t = p + 1 - \# E(\mathbb F_p).$$
> 1. Let $\alpha$ and $\beta$ be the complex roots of the quadratic polynomial $Z^2 - tZ + p$. Then $|\alpha| = |\beta| = \sqrt{p}$, and for every $k \geq 1$ we have $$\# E(\mathbb F_{p^k}) = p^k + 1 - \alpha^k - \beta^k.$$
> 2. Let $$\tau: E(\mathbb F_{p^k}) \rightarrow E(\mathbb F_{p^k}), \qquad (x, y) \rightarrow (x^p, y^p),$$ be the Frobenius map. Then for every point $Q \in E(\mathbb F_{p^k})$ we have $$\tau^2(Q) - t \tau(Q) + p \cdot Q = 0,$$ where $\tau^2(Q)$ denotes the composition $\tau(\tau(Q))$.
