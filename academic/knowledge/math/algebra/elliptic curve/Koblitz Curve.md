## Koblitz Curve

> [!definition] Koblitz Curve
> A **Koblitz curve** is an elliptic curve defined over $\mathbb F_2$ by an equation of the form $$E_a : Y^2 + XY = X^3 + aX + 1$$ with $a \in \{0, 1\}$. The discriminant of $E_a$ is $\Delta = 1$.

> [!example]
> For **Koblitz curve** $E_0$ over $\mathbb F_2$ is $\{(1, 0), (0, 1), (1, 1), \mathcal O\}$, we have the Frobenius map $\tau$ for $E(\mathbb F_{2^k})$ satisfies the equation $\tau^2 + \tau + 2$. The equation has root $\{\frac{-1 + \sqrt{-7}}{2}, \frac{-1 - \sqrt{-7}}{2}\}$, and we have $$E_0(\mathbb F_{2^k}) = 2^k + 1 - (\frac{-1 + \sqrt{-7}}{2})^k - (\frac{-1 - \sqrt{-7}}{2})^k$$

> [!algorithm] $\tau$-adic Expansion with $\tau^2 = -2 - \tau$
> **Input**
> - A positive integer $n$
> - An element $\tau$ satisfying $\tau^2 = -2 = \tau$
>
> **Output**
> - Coefficients $v_i \in \{-1,0,1\}$ such that
>   $$n = v_0 + v_1 \tau + v_2 \tau^2 + \cdots + v_\ell \tau^\ell$$
>
> ---
>
> 1. Set $n_0 = n$, $n_1 = 0$, and $i = 0$.
>
> 2. While $n_0 \neq 0$ or $n_1 \neq 0$, do:
>
>    2.1 If $n_0$ is odd, then:
>    $$v_i = 2 - \bigl((n_0 - 2n_1) \bmod 4\bigr)$$
>    $$n_0 = n_0 - v_i$$
>
>   2.2 Else:
>    $$v_i = 0$$
>
>   2.3 Set:
>    $$i = i + 1$$
>
>   2.4 Update:
>    $$(n_0, n_1) = \left(n_1 - \tfrac{1}{2} n_0,\; -\tfrac{1}{2} n_0\right)$$
>
> 3. Output the coefficients $v_0, v_1, \ldots, v_\ell$.
> ---
> 
> **Properties**
> 1. At most one-third of the coefficients $v_i$ are nonzero.
> 2. The length satisfies $\ell \le \log(n)$.
