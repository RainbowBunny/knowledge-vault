Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 4.2: Quotients of polynomial rings.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — §16.3, §16.4, §17.3 (numbering as in the HTML edition https://judsonbooks.org/aata-files/aata-html/).

## Definition

> [!definition] Parameters
> - $R$: a [[Commutative Ring]] with identity.
> - $f(x) \in R[x]$: a polynomial.

> [!definition] Quotient of Polynomial Ring
> Instantiates:: [[Quotient Ring]].
>
> ---
> The **quotient** of the [[Polynomial Ring]] $R[x]$ by $f(x)$ is the [[Quotient Ring]] $R[x] / (f(x))$ modulo the principal [[Ideal]] $(f(x)) = \{f(x) g(x) : g(x) \in R[x]\}$. Its elements are the cosets $g(x) + (f(x))$, with multiplication
> $$\big(g(x) + (f(x))\big)\big(h(x) + (f(x))\big) = g(x) h(x) + (f(x)).$$
> `[Jud Ex 16.3.5]` `[Jud Thm 16.3.10]` `[Alu III.4.2]`

## Property

> [!theorem] Irreducible modulus — $\mathbb F[x] / (m)$ is a field iff $m$ is irreducible
> Let $\mathbb F$ be a [[Field]] and $m \in \mathbb F[x]$. Then $\mathbb F[x] / (m)$ is a [[Field]] if and only if $m$ is irreducible: $(m)$ is a [[Maximal Ideal]] exactly when $m$ is irreducible, and a quotient by a maximal ideal is a field. `[Jud Thm 17.3.12]` `[Jud Thm 16.4.1]`

Further properties over a field (a unique remainder of degree $< \deg m$ in each class, the units, $|\mathbb F_p[x]/(m)| = p^d$) are in [[Polynomial#Quotient of Polynomial Rings]]; the convolution rings $\mathbb Z[x]/(x^N - 1)$ used by NTRU are in [[Polynomial#Convolution Polynomial Rings]].

## Related

### Prerequisites
- [[Polynomial Ring]] — the ring being divided
- [[Quotient Ring]] — the general construction $R/I$
- [[Ideal]] — $(f)$ is a principal ideal
