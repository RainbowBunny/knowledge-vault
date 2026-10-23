Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 1.2: First examples and special classes of rings; Exercise 1.4.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — §16.1 Rings, Example 16.1.6 (read at the mirror https://judsonbooks.org/aata-files/aata-html/; item numbers as there).
- `[WP]` — Wikipedia, _Matrix ring_: https://en.wikipedia.org/wiki/Matrix_ring (read 2026-10-20).

## Definition

> [!definition] Parameters
> - $R$: a [[Ring]].
> - $n$: a positive integer.
> - $A = (a_{ij})$: an $n \times n$ [[Matrix]] with entries in $R$.
> - $B = (b_{ij})$: an $n \times n$ [[Matrix]] with entries in $R$.

> [!definition] Matrix Ring
> Instantiates:: [[Ring]].
>
> ---
> The **matrix ring** $M_n(R)$ is the set of $n \times n$ matrices with entries in $R$, with
> - entrywise addition: $(A + B)_{ij} = a_{ij} + b_{ij}$
> - matrix multiplication: $(AB)_{ij} = \sum_{k = 1}^{n} a_{ik} b_{kj}$
> - identity the identity matrix $I_n$ ($1$ on the diagonal, $0$ elsewhere).
>
> `[WP]` `[Jud Ex 16.1.6]` (the case $M_2(\mathbb R)$)

## Property

> [!proposition] Noncommutative with zero divisors — $M_n(R)$ for $n \geq 2$ and $R \neq 0$
> For $n \geq 2$ and $R$ not the [[Zero Ring]], $M_n(R)$ is not commutative, and it has zero divisors and nonzero [[Nilpotent Element|nilpotent elements]].
>
> `[WP]` `[Jud Ex 16.1.6]` ($M_2(\mathbb R)$: noncommutative, with zero divisors)

## Related

### Siblings
- [[Matrix Group]] — groups of invertible matrices, inside the units of a matrix ring.

### Prerequisites
- [[Matrix]], [[Ring]].
