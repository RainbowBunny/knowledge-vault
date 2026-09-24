Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter III: Rings and modules, Section 1.1: Definitions; Section 1.2: First examples and special classes of rings; Section 3.2: Quotients.

## Definition

> [!definition] Ring
> A **ring** is a set $R$ that has two [[Binary Operation]] $+, *$:
> - $(R, +)$ is an [[Abelian Group]]  
> - $(R, *)$ is a [[Monoid]]. 
> - $+$ and $*$ satisfies [[Distributivity]].

### Zero Divisor

> [!lemma] Annihilation
> In a ring $R$:
> $$\forall r \in R: 0 \cdot r = 0 = r \cdot 0$$

> [!definition] Zero Divisor
> An element $a \in R$ is a **left-zero-divisor** if there exist elements $b \neq 0$ in $R$ for which $ab = 0$.
> Similarly, an element $b \in R$ is a **right-zero-divisor** if there exist elements $a \neq 0$ for which $ab = 0$.

> [!proposition]
> In a ring $R, a \in R$ is not a left-(right-)zero-divisor if and only if left (resp., right) multiplication by $a$ is an [[Injection]] on $R$.

### Unit

> [!definition] Unit
> An element $u$ of a ring $R$ is a (two-sided) units iff
> - $\exists v \in R: uv = 1$ (left-unit).
> - $\exists v \in R: vu = 1$ (right-unit).

> [!proposition] Properties of Unit
> In a ring $R$:
> - $u$ is a left- (resp., right-) unit iff left- (resp., right-) multiplication by $u$ is a [[Surjection]] on $R$.
> - If $u$ is a left- (resp., right-) unit, then right- (resp., left-) multiplication by $u$ is an [[Injection]]; that is, $u$ is not a right- (resp., left-) zero-divisor.
> - The inverse of a two-sided unit is unique.
> - Two-sided units form a [[Group]] under multiplication.

### Characteristic

> [!definition] Characteristic
> As $\mathbb{Z}$ is the [[Category Ring|Initial Object]] of category $\mathsf{Ring}$, we have
> $$\exists n \in \mathbb{N}: \ker \varphi = n \mathbb{Z}.$$
> $n$ is called the **characteristic** of $R$.

