Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 1.2: First examples and special classes of rings.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — §16.1 Rings; §16.2 Integral Domains and Fields (read at the mirror https://judsonbooks.org/aata-files/aata-html/; item numbers as there).

## Definition

> [!definition] Parameters
> - [[Commutative Ring]]: Import $R$.
> - $a$: an element of $R$.
> - $b$: an element of $R$.

> [!definition] Integral Domain
> Extends:: [[Commutative Ring]].
>
> ---
> An **integral domain** is a nonzero [[Commutative Ring]] $R$ (with $1$) such that
> $$\forall a, b \in R: ab = 0 \implies a = 0 \lor b = 0$$
>
> `[Alu III.1.2]` `[Jud §16.1]`

## Property

> [!proposition] Finite integral domains are fields — a finite commutative ring is an integral domain iff it is a field
> Assume $R$ is a finite [[Commutative Ring]]; then $R$ is an integral domain if and only if it is a [[Field]].
>
> `[Alu III.1.2]` `[Jud Thm 16.2.5]` (every finite integral domain is a field)

## Related

### Descendants
- [[Principal Ideal Domain]] — every [[Ideal]] is principal.

### Siblings
- [[Field]] — every field is an integral domain; for finite rings the converse holds.
- [[Boolean Ring]] — the only Boolean integral domain is $\mathbb Z/2\mathbb Z$.
