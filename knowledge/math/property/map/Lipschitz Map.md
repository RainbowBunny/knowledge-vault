Reference:
- `[Hut]` — J. E. Hutchinson, _Fractals and self-similarity_, Indiana Univ. Math. J. 30 (1981): https://maths-people.anu.edu.au/~john/Assets/Research%20Papers/fractals_self-similarity.pdf

## Definition

> [!definition] Parameters
> - $(X, d)$: a [[Metric Space]]. $F: X \to X$.

> [!definition] Lipschitz Map
> ### Scope
> A map $F: X \to X$ on a metric space.
>
> ---
> ### Property
> The **Lipschitz constant** of $F$ is
> $$\mathrm{Lip}\, F = \sup_{x \neq y} \frac{d(F(x), F(y))}{d(x, y)}.$$
> If $\mathrm{Lip}\, F = \lambda$, then $d(F(x), F(y)) \leq \lambda\, d(x, y)$ for all $x, y$, and $\lambda$ is the least such constant. $F$ is **Lipschitz** if $\mathrm{Lip}\, F < \infty$. `[Hut 2.2]`

> [!remark] Between two spaces
> The same formula, with $d_Y(F(x), F(y))$ in the numerator, defines $\mathrm{Lip}\, F$ for $F: X \to Y$.

## Property

| $\mathrm{Lip}\, F$ | name | where |
| --- | --- | --- |
| $< 1$ | contraction `[Hut 2.2]` | [[Contraction]] |
| $\leq 1$ | 1-Lipschitz | [[Calculus Functions#Lipschitz-1 Function]]; the test functions of Hutchinson's metric on measures `[Hut 4.3(1)]`, see [[Iterated Function System]] |

## Related

### Descendants
- [[Contraction]]

### Prerequisites
- [[Metric Space]]
