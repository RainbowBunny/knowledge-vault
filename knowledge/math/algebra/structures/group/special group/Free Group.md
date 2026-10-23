Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter II: Groups, first encounter, Section 5.1: Motivation.
- `[McG24]` — McGovern, Math 504 (University of Washington), Lecture 10-4: _Free groups and the Nielsen–Schreier Theorem_ (2024): https://sites.math.washington.edu/~mcgovern/504%20pdf%202024/504.10-4.pdf
- `[WikFG]` — Wikipedia, _Free group_: https://en.wikipedia.org/wiki/Free_group

## Definition

> [!remark] Motivation
> Given a set $A$, whose elements have no special 'group-theoretic' property, we want to construct the **free group** $F(A)$ containing $A$ 'in the most efficient way' for every set $A$. `[Alu II §5.1]`

> [!definition] Parameters
> - $A$: a [[Set]].
> - $F(A)$: a [[Group]].
> - $j: A \rightarrow F(A)$: a [[Function]].
> - $G$: any [[Group]].
> - $f: A \rightarrow G$: any [[Function]].

> [!definition] Free Group
> Extends:: [[Group]].
> Requires:: [[Universal Property]].
>
> ---
> The **free group** on $A$ is a group $F(A)$ together with a function $j: A \rightarrow F(A)$ such that for every group $G$ and every function $f: A \rightarrow G$ there is a unique [[Group Homomorphism]] $\varphi: F(A) \rightarrow G$ with
> $$\varphi \circ j = f.$$
> `[McG24 Thm 17]` `[WikFG]`
>
> [McG24] constructs $F(S)$ from reduced words over $S$ and proves this property as Theorem 17.

## Property

> [!theorem] Nielsen–Schreier theorem — every subgroup of a free group is free
> Every [[Subgroup]] of a free group is free. `[McG24 Thm 19]`
>
> Finite generation is not needed, and it is not inherited: a free group of rank at least 2 has subgroups of every countable rank `[WikFG]`.

## Related

### Constructions
- [[Group Presentation]] — $G \cong F(A)/R$

### Prerequisites
- [[Universal Property]] — the form of the definition
