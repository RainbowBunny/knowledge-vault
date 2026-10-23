Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 4.3: Prime and maximal ideals; Exercise 4.14.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ (numbering as on the LibreTexts / AIM mirrors).

## Definition

> [!definition] Parameters
> - $R$: a [[Commutative Ring]].
> - $I \neq (1)$: an [[Ideal]] of $R$.

> [!definition] Prime Ideal
> Extends:: [[Ideal]].
>
> ---
> Let $I \neq (1)$ be an [[Ideal]] of a [[Commutative Ring]] $R$. $I$ is a **prime ideal** if $R/I$ (the [[Quotient Ring]]) is an [[Integral Domain]].
>
> `[Alu III.4.3]`

## Property

> [!proposition] Prime criterion — $ab \in I$ forces $a \in I$ or $b \in I$
> Let $I \neq (1)$ be an [[Ideal]] of a [[Commutative Ring]] $R$:
> - $I$ is prime if and only if:
> $$\forall a, b \in R: ab \in I \implies (a \in I \lor b \in I).$$
>
> `[Alu III.4.3]` `[Jud Prop 16.38]` — Judson takes this condition as the definition.

> [!proposition] Finite quotient — prime and maximal coincide when $R/I$ is finite
> Let $I$ be an [[Ideal]] of a [[Commutative Ring]] $R$. If $R / I$ is finite, then $I$ is prime if and only if it is a [[Maximal Ideal]].
>
> `[Alu III.4 Ex 4.14]` `[Jud Thm 16.16]` (a finite integral domain is a field)

> [!proposition] Prime equals maximal in a PID — for nonzero ideals
> Let $R$ be a [[Principal Ideal Domain]], and let $I$ be a nonzero [[Ideal]] in $R$. Then $I$ is prime if and only if it is maximal.
>
> `[Alu III.4.3]` `[cf. Jud Thm 18.12]`

## Example

> [!example] Prime ideals of $\mathbb Z$
> - The nonzero prime ideals of $\mathbb Z$ are the ideals $p\mathbb Z$, $p$ prime. `[Jud Ex 16.39]`
> - $(0)$ is prime but not maximal: $\mathbb Z/(0) \cong \mathbb Z$ is an integral domain, not a field.

## Related

### Siblings
- [[Maximal Ideal]] — $R/I$ a [[Field]]; every maximal ideal is prime

### Prerequisites
- [[Quotient Ring]] — $R/I$
- [[Integral Domain]] — what $R/I$ must be
