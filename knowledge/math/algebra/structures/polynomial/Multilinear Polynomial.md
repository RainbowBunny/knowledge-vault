Reference:
- `[Tha22]` — J. Thaler, _Proofs, Arguments, and Zero-Knowledge_ (2022), §3.5: https://people.cs.georgetown.edu/jthaler/ProofsArgsAndZK.pdf

## Definition

> [!definition] Parameters
> - $\mathbb F$: a [[Field]].
> - $v \geq 1$: the number of variables.
> - $g \in \mathbb F[x_1, \dots, x_v]$: a [[Multivariate Polynomial]].

> [!definition] Multilinear
> Extends:: [[Multivariate Polynomial]].
>
> ---
> A multivariate polynomial $g$ is **multilinear** if the degree of the polynomial in each variable is at most one. `[Tha22 Def 3.4]`

## Property

> [!proposition] Multilinear extension — every $f : \{0, 1\}^v \to \mathbb F$ has exactly one
> Any function $f: \{0, 1\}^v \rightarrow \mathbb F$ has a unique multilinear extension (MLE) over $\mathbb F$ — a multilinear polynomial that agrees with $f$ on $\{0, 1\}^v$ — and we reserve the notation $\tilde f$ for this special extension of $f$. `[Tha22 Fact 3.5]`

> [!lemma] Lagrange formula for the MLE — $\tilde f = \sum_w f(w) \, \chi_w$
> For every $x = (x_1, \dots, x_v) \in \mathbb F^v$,
> $$\tilde f(x) = \sum_{w \in \{0, 1\}^v} f(w) \, \chi_w(x),$$
> where the **multilinear Lagrange basis polynomials** are
> $$\chi_w(x) = \prod_{i = 1}^v \big(x_i w_i + (1 - x_i)(1 - w_i)\big).$$
> `[Tha22 Lemma 3.6]`

## Related

### Siblings
- [[Lagrange Interpolation]] — the univariate analogue: values at $n$ distinct points determine a polynomial of degree $< n$
- [[Multilinearity]] — a map linear in each argument; a multilinear polynomial is only affine in each variable ($1 - x_1$ is multilinear)
