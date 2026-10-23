Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 1.1: Definitions; Section 1.2: First examples and special classes of rings; Section 3.2: Quotients.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — §16.1 Rings; §16.2 Integral Domains and Fields; Exercise 16.7.35 (read at the mirror https://judsonbooks.org/aata-files/aata-html/; item numbers as there).

## Definition

> [!definition] Parameters
> - $R$: a [[Set]].
> - $+$: a [[Binary Operation]] on $R$ (addition).
> - $*$: a [[Binary Operation]] on $R$ (multiplication).

> [!definition] Ring
> A **ring** is a set $R$ that has two [[Binary Operation]] $+, *$:
> - $(R, +)$ is an [[Abelian Group]].
> - $(R, *)$ is a [[Monoid]].
> - $+$ and $*$ satisfies [[Distributivity]].
>
> `[Alu III.1.1]`

> [!remark] Convention: a ring has $1$
> In this vault (following `[Alu]`) a ring has a multiplicative identity $1$, since $(R, *)$ is a monoid, and $0 = 1$ is allowed: that is the [[Zero Ring]].
> `[Jud §16.1]` asks only that $*$ be associative. There a *ring with identity* (*unity*) is one with an element $1 \neq 0$ such that $1a = a1 = a$ for all $a$. Statements quoted from `[Jud]` are read with this difference in mind.

## Structure

### Zero Divisor

> [!definition] Parameters
> - $R$: a ring.
> - $a$: an element of $R$.
> - $b$: an element of $R$.

> [!definition] Zero Divisor
> An element $a \in R$ is a **left-zero-divisor** if there exist elements $b \neq 0$ in $R$ for which $ab = 0$.
> Similarly, an element $b \in R$ is a **right-zero-divisor** if there exist elements $a \neq 0$ for which $ab = 0$.
>
> `[Alu III.1.2]`

> [!remark] Zero divisors in `[Jud]`
> `[Jud §16.1]` defines a zero divisor only in a commutative ring, and only for a *nonzero* element $a$. With the definition above, $0$ is a left- and right-zero-divisor in every nonzero ring (take $b = 1$).

> [!proposition] Zero-divisors and injectivity — $a$ is not a left-zero-divisor iff $x \mapsto ax$ is injective
> In a ring $R$, $a \in R$ is not a left-(right-)zero-divisor if and only if left (resp., right) multiplication by $a$ is an [[Injection]] on $R$.
>
> `[Alu III.1.2]`

### Unit

> [!definition] Parameters
> - $R$: a ring.
> - $u$: an element of $R$.
> - $v$: an element of $R$.

> [!definition] Unit
> An element $u$ of a ring $R$ is a (two-sided) unit iff
> - $\exists v \in R: uv = 1$ (left-unit).
> - $\exists v \in R: vu = 1$ (right-unit).
>
> `[Alu III.1.2]` `[Jud §16.1]`

> [!proposition] Properties of units — one-sided units, uniqueness of the inverse, the group of units
> In a ring $R$:
> - $u$ is a left- (resp., right-) unit iff left- (resp., right-) multiplication by $u$ is a [[Surjection]] on $R$.
> - If $u$ is a left- (resp., right-) unit, then right- (resp., left-) multiplication by $u$ is an [[Injection]]; that is, $u$ is not a right- (resp., left-) zero-divisor.
> - The inverse of a two-sided unit is unique.
> - Two-sided units form a [[Group]] under multiplication.
>
> `[Alu III.1.2]` `[Jud Ex 16.7.35]` (the group of units $U(R)$)

### Characteristic

> [!definition] Parameters
> - $R$: a ring.
> - $\varphi: \mathbb Z \to R$: the unique [[Ring Homomorphism]], $\varphi(m) = m \cdot 1_R$.

> [!definition] Characteristic
> As $\mathbb{Z}$ is the [[Category Ring|Initial Object]] of category $\mathsf{Ring}$, we have
> $$\exists n \in \mathbb{N}: \ker \varphi = n \mathbb{Z}.$$
> $n$ is called the **characteristic** of $R$.
>
> `[Alu III]`

> [!remark] The same number as in `[Jud]`
> `[Jud §16.2]` defines the characteristic as the least positive integer $n$ such that $nr = 0$ for all $r \in R$, and $0$ if there is no such integer. For a ring with $1$ this is the additive order of $1$ (`[Jud Lemma 16.2.7]`), which generates $\ker \varphi$: the two definitions agree.

## Property

> [!lemma] Annihilation — $0$ times anything is $0$
> In a ring $R$:
> $$\forall r \in R: 0 \cdot r = 0 = r \cdot 0$$
>
> `[Alu III.1]` `[Jud Prop 16.1.8]`

## Related

### Descendants
- [[Commutative Ring]] — $ab = ba$; below it [[Integral Domain]] and [[Field]].
- [[Division Ring]] — $1 \neq 0$ and every nonzero element is a two-sided unit.
- [[Boolean Ring]] — every element is idempotent.

### Instantiations
- [[Zero Ring]] — the only ring with $0 = 1$.
- [[Matrix Ring]] — $M_n(R)$, not commutative for $n \geq 2$.
- [[Monoid Ring]] — $R[M]$, finite formal sums over a monoid.

### Constructions
- [[Subring]] — a subset whose inclusion is a ring homomorphism.
- [[Ring Center]] — the elements that commute with all of $R$.
- [[Quotient Ring]] — $R/I$ for a two-sided [[Ideal]] $I$.
- [[Ring Homomorphism]] — the maps; with them rings form [[Category Ring|$\mathsf{Ring}$]].

### Properties
- [[Nilpotent Element]] — $a^n = 0$ for some positive integer $n$.

### Prerequisites
- [[Abelian Group]], [[Monoid]], [[Distributivity]].
