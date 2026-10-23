Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (Springer), chapter on elliptic curves: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[Gal12]` — S. D. Galbraith, _Mathematics of Public Key Cryptography_ (CUP 2012), Exercise 9.10.11 (Koblitz curves); §11.3.2 Frobenius expansions (Example 11.3.3, Def 11.3.5, Lemma 11.3.7, Algorithm 8, Exercise 11.3.11): https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch9.pdf · https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch11.pdf

## Definition

> [!definition] Parameters
> - $a \in \{0, 1\}$: the coefficient that selects the curve.

> [!definition] Koblitz Curve
> Extends:: [[Generalized Elliptic Curves]].
>
> ---
> A **Koblitz curve** is an elliptic curve defined over $\mathbb F_2$ by an equation of the form $$E_a : Y^2 + XY = X^3 + aX^2 + 1$$ with $a \in \{0, 1\}$. The discriminant of $E_a$ is $\Delta = 1$.
>
> `[HPS]` `[Gal12 Ex 9.10.11]`

### $\tau$-adic Expansion

> [!algorithm] $\tau$-adic Expansion with $\tau^2 = -2 - \tau$
> - $(v_0, \dots, v_\ell) \leftarrow \mathsf{TauExpand}(n)$: Deterministic $\tau$-adic expansion of an integer.
>     - **Input**: a positive integer $n$; an element $\tau$ satisfying $\tau^2 = -2 - \tau$.
>     - **Output**: coefficients $v_i \in \{-1,0,1\}$ such that $$n = v_0 + v_1 \tau + v_2 \tau^2 + \cdots + v_\ell \tau^\ell$$
>     - **Steps**:
>         1. Set
>             - $n_0 = n$
>             - $n_1 = 0$
>             - $i = 0$
>         2. While $n_0 \neq 0$ or $n_1 \neq 0$, do:
>             1. If $n_0$ is odd, then: $$v_i = 2 - \bigl((n_0 - 2n_1) \bmod 4\bigr)$$ $$n_0 = n_0 - v_i$$
>             2. Else: $$v_i = 0$$
>             3. Set: $$i = i + 1$$
>             4. Update: $$(n_0, n_1) = \left(n_1 - \tfrac{1}{2} n_0,\; -\tfrac{1}{2} n_0\right)$$
>         3. Output the coefficients $v_0, v_1, \ldots, v_\ell$.
>
> `[HPS]` `[Gal12 §11.3.2, Algorithm 8]` — [Gal12] writes the digit as $2 - (n_0 + 2n_1 \bmod 4)$, the same residue since $4n_1 \equiv 0 \pmod 4$.

## Property

> [!proposition] $\tau$-NAF — the expansion has no two adjacent nonzero digits, one-third nonzero digits on average, and length about $2\log_2 n$
> 1. No two consecutive coefficients $v_i, v_{i+1}$ are both nonzero, and on average one-third of the coefficients $v_i$ are nonzero.
> 2. The length is roughly $\ell \approx 2 \log_2 n$.
>
> `[Gal12 Def 11.3.5, Ex 11.3.11, §11.3.2]`

## Example

> [!example]
> For **Koblitz curve** $E_0$ over $\mathbb F_2$ is $\{(1, 0), (0, 1), (1, 1), \mathcal O\}$, we have the Frobenius map $\tau$ for $E(\mathbb F_{2^k})$ satisfies the equation $\tau^2 + \tau + 2 = 0$. The equation has root $\{\frac{-1 + \sqrt{-7}}{2}, \frac{-1 - \sqrt{-7}}{2}\}$, and we have $$\#E_0(\mathbb F_{2^k}) = 2^k + 1 - (\frac{-1 + \sqrt{-7}}{2})^k - (\frac{-1 - \sqrt{-7}}{2})^k$$
>
> `[Gal12 Example 11.3.3]` (Frobenius equation $\tau^2 + (-1)^a \tau + 2 = 0$)

## Related

### Prerequisites
- [[Generalized Elliptic Curves]] — the point-count theorem used in the example

### Siblings
- [[Elliptic Curves over Finite Fields]] — double-and-add, which the $\tau$-adic expansion speeds up by replacing doublings with Frobenius
