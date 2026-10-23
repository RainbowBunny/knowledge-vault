Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 4.1: Basic Operations.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ (numbering as on the LibreTexts / AIM mirrors).

## Definition

> [!definition] Parameters
> - $R$: an [[Integral Domain]].

> [!definition] Principal Ideal Domain
> Extends:: [[Integral Domain]].
>
> ---
> An integral domain $R$ is a PID ('Principal Ideal Domain') if every [[Ideal]] of $R$ is [[Ideal#Principal Ideal|principal]].
>
> `[Alu III.4.1]` `[Jud §18.2]`

## Property

> [!proposition] PIDs are Noetherian — every ascending chain of ideals stabilises
> Every principal ideal domain is a [[Noetherian Ring]].
>
> `[Jud Lemma 18.14]`

- In a PID a nonzero ideal is prime if and only if it is maximal — see [[Prime Ideal]].

## Example

> [!example] Example of Principal Ideal Domain
> - $\mathbb{Z}$ — every ideal is $n\mathbb Z$. `[Jud Thm 16.25]`

> [!example] A non-PID: $\mathbb Z[x]$
> The ideal $\{5f(x) + xg(x) : f, g \in \mathbb Z[x]\}$ of $\mathbb Z[x]$ is not principal, so $\mathbb Z[x]$ is an integral domain that is not a PID. `[Jud Ex 18.17]`

## Related

### Siblings
- [[Noetherian Ring]] — every ideal finitely generated; a PID is Noetherian

### Prerequisites
- [[Ideal#Principal Ideal]] — the ideal $(a)$
- [[Polynomial Ring]] — $\mathbb Z[x]$, the counterexample
