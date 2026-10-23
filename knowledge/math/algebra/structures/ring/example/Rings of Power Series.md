Reference:
- `[WP]` — Wikipedia, _Formal power series_: https://en.wikipedia.org/wiki/Formal_power_series (read 2026-10-20).

## Definition

> [!definition] Parameters
> - $R$: a [[Commutative Ring]].
> - $f = \sum_{n \geq 0} a_n x^n$: a formal power series, $a_n \in R$.
> - $g = \sum_{n \geq 0} b_n x^n$: a formal power series, $b_n \in R$.

> [!definition] Ring of Formal Power Series
> Instantiates:: [[Commutative Ring]].
>
> ---
> The **ring of formal power series** $R[\![x]\!]$ is the set of all sequences $(a_n)_{n \geq 0}$ of elements of $R$, written $\sum_{n \geq 0} a_n x^n$ (a notation, not an infinite sum), with
> - $f + g = \sum_{n \geq 0} (a_n + b_n) x^n$
> - $f g = \sum_{n \geq 0} c_n x^n$, where
>     - $c_n = \sum_{k = 0}^{n} a_k b_{n - k}$
>
> It is a commutative ring with identity $1 = 1 + 0x + 0x^2 + \cdots$.
>
> `[WP]`

## Property

> [!proposition] Units of $R[\![x]\!]$ — $f$ is invertible iff its constant term is
> $f = \sum_{n \geq 0} a_n x^n$ is a [[Ring#Unit|unit]] of $R[\![x]\!]$ if and only if $a_0$ is a unit of $R$.
>
> `[WP]`

## Related

### Siblings
- [[Polynomial Ring]] — $R[x] \subseteq R[\![x]\!]$: the series with finitely many nonzero coefficients.
- [[Monoid Ring]] — $R[x] = R[(\mathbb N, +)]$; dropping the finiteness condition gives $R[\![x]\!]$.

### Prerequisites
- [[Commutative Ring]].
