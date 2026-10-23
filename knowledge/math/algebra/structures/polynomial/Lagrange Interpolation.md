Reference:
- `[Tha22]` — J. Thaler, _Proofs, Arguments, and Zero-Knowledge_ (2022), §2.4: https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — §17.2 (numbering as in the HTML edition https://judsonbooks.org/aata-files/aata-html/).

## Definition

> [!definition] Parameters
> - $\mathbb F$: a [[Field]].
> - $n \geq 1$: the number of points.
> - $x_0, \dots, x_{n-1} \in \mathbb F$: distinct points.
> - $y_0, \dots, y_{n-1} \in \mathbb F$: the prescribed values.

> [!definition] Lagrange Interpolation
> Requires:: [[Polynomial]].
>
> ---
> The **Lagrange basis polynomials** of the points $x_0, \dots, x_{n-1}$ are
> $$\delta_i(X) = \prod_{\substack{k = 0 \\ k \neq i}}^{n - 1} \frac{X - x_k}{x_i - x_k} \qquad (0 \leq i \leq n - 1),$$
> so that
> - $\delta_i(x_i) = 1$,
> - $\delta_i(x_k) = 0$ for $k \neq i$.
>
> The **Lagrange interpolation polynomial** of the data $(x_i, y_i)$ is
> $$q(X) = \sum_{i = 0}^{n - 1} y_i \, \delta_i(X),$$
> a polynomial of degree at most $n - 1$ with $q(x_i) = y_i$ for every $i$. `[Tha22 §2.4, eqs. (2.3) and (2.8)]`, there over $\mathbb F_p$ with $x_i = i$.

## Property

> [!theorem] Uniqueness of the interpolant — one polynomial of degree $< n$ takes $n$ prescribed values
> $q$ is the only polynomial of degree at most $n - 1$ with $q(x_i) = y_i$ for $i = 0, \dots, n - 1$: the difference of two such polynomials has degree at most $n - 1$ and $n$ distinct roots, so it is $0$. `[Tha22 Lemma 2.3]` `[Jud Cor 17.2.4]`

## Related

### Siblings
- [[Multilinear Polynomial]] — the analogue on $\{0, 1\}^v$, with basis polynomials $\chi_w$
- [[Vanishing Polynomial]] — $\delta_i$ is $Z_S(X) / (X - x_i)$, $S = \{x_0, \dots, x_{n-1}\}$, rescaled to equal $1$ at $x_i$

### Prerequisites
- [[Polynomial]] — see [[Polynomial#Polynomial Interpolation]] for the secret-sharing form (interpolation in the exponent)
