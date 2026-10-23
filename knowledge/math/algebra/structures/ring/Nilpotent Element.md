Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 1.2: First examples and special classes of rings; Exercise 1.6.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — Exercise 16.7.27 (read at the mirror https://judsonbooks.org/aata-files/aata-html/; item numbers as there).

## Definition

> [!definition] Parameters
> - $R$: a [[Ring]].
> - $a$: an element of $R$.
> - $n$: a positive integer.

> [!definition] Nilpotent Element
> An element $a$ of a [[Ring]] $R$ is *nilpotent* if $a^n = 0$ for some positive integer $n$.
>
> `[Alu III.1.2]` `[Jud Ex 16.7.27]`

## Property

> [!proposition] Commuting nilpotents add — if $a, b$ are nilpotent and commute, $a + b$ is nilpotent
> If $a$ and $b$ are nilpotent in $R$ and $ab = ba$, then $a + b$ is also nilpotent.
>
> `[Alu III Ex 1.6]`

> [!proposition] Nilpotents form an ideal — in a commutative ring the nilpotent elements form an ideal
> If $R$ is a [[Commutative Ring]], the set of nilpotent elements of $R$ is an [[Ideal]] of $R$.
>
> `[Jud Ex 16.7.27]`

## Example

> [!example]
> In the [[Matrix Ring]] $M_2(\mathbb R)$, the matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ is nilpotent: its square is $0$.

## Related

### Prerequisites
- [[Ring]], [[Commutative Ring]] (for the ideal of nilpotents).
