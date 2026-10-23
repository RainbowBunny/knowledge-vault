Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 4.3: Prime and maximal ideals.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ (numbering as on the LibreTexts / AIM mirrors).

## Definition

> [!definition] Parameters
> - $R$: a [[Commutative Ring]].
> - $I \neq (1)$: an [[Ideal]] of $R$.

> [!definition] Maximal Ideal
> Extends:: [[Ideal]].
>
> ---
> Let $I \neq (1)$ be an [[Ideal]] of a [[Commutative Ring]] $R$. $I$ is a **maximal ideal** if $R/I$ (the [[Quotient Ring]]) is a [[Field]].
>
> `[Alu III.4.3]`

## Property

> [!proposition] Maximality — no ideal lies strictly between $I$ and $R$
> Let $I \neq (1)$ be an [[Ideal]] of a [[Commutative Ring]] $R$:
> - $I$ is maximal if and only if, for every ideal $J$ of $R$:
> $$I \subseteq J \implies (I = J \lor J = R).$$
>
> `[Jud §16.6, Thm 16.35]` — Judson takes this condition as the definition and proves it equivalent to "$R/I$ is a field".

> [!proposition] Maximal ideals are prime
> A maximal ideal is also a [[Prime Ideal]].
>
> `[Jud Cor 16.40]`

## Example

> [!example] $p\mathbb Z$
> For a prime $p$, $p\mathbb Z$ is a maximal ideal of $\mathbb Z$, since $\mathbb Z/p\mathbb Z$ is a field. `[Jud Ex 16.36]`

## Related

### Siblings
- [[Prime Ideal]] — $R/I$ only an [[Integral Domain]]; every maximal ideal is prime, not conversely ($(0) \subset \mathbb Z$)

### Prerequisites
- [[Quotient Ring]] — $R/I$
- [[Field]] — what $R/I$ must be
