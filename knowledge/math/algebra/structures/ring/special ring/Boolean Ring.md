Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and Modules, Exercise 3.15.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — Exercises 16.7.28, 16.7.37 (read at the mirror https://judsonbooks.org/aata-files/aata-html/; item numbers as there).
- `[WP]` — Wikipedia, _Boolean ring_: https://en.wikipedia.org/wiki/Boolean_ring (read 2026-10-20).

## Definition

> [!definition] Parameters
> - [[Ring]]: Import $(R, +, *)$.

> [!definition] Boolean Ring
> Extends:: [[Ring]].
>
> ---
> A **Boolean ring** is a ring $(R, +, *)$ in which
> - $*$ is [[Idempotence]] on $R$: $a * a = a$ for every $a \in R$.
>
> `[Alu III Ex 3.15]` `[Jud Ex 16.7.28]` `[WP]`

## Property

> [!theorem] Boolean Ring is Commutative Ring — every Boolean ring is commutative
> Every Boolean ring is a [[Commutative Ring]].
>
> `[Alu III Ex 3.15]` `[Jud Ex 16.7.28]` `[WP]`

> [!theorem] Characteristic of Boolean Ring — a nonzero Boolean ring has characteristic $2$
> Every nonzero Boolean ring has [[Ring#Characteristic|characteristic]] $2$.
>
> `[Alu III Ex 3.15]` `[WP]` ($a + a = 0$ for all $a$)

> [!corollary] Boolean integral domain — a Boolean integral domain is $\mathbb Z / 2\mathbb Z$
> Let $R$ be a Boolean [[Integral Domain]].
> - $R$ has no zero divisors and $a(a - 1) = 0$ for every $a$, so $R = \{0, 1\}$.
> - $R$ is nonzero, so $0 \neq 1$.
> - Hence $R \cong \mathbb{Z} / 2 \mathbb{Z}$.
>
> `[Alu III Ex 3.15]` `[Jud Ex 16.7.37]` (the only idempotents of an integral domain are $0$ and $1$)

## Related

### Instantiations
- [[Power Set Ring]] — $(\mathcal P(S), \Delta, \cap)$.

### Siblings
- [[Commutative Ring]] — a Boolean ring is commutative by the theorem above, not by an axiom.
- [[Integral Domain]] — the only Boolean integral domain is $\mathbb Z/2\mathbb Z$.

### Prerequisites
- [[Ring]], [[Idempotence]].
