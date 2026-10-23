Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter I: Preliminaries: Set theory and categories, Section 5.3: Quotients.
- `[Rie]` — E. Riehl, _Category Theory in Context_ (2016): https://math.jhu.edu/~eriehl/context.pdf — Exercise 1.1.iii (read at the mirror https://www.math.ucla.edu/~mopie/context.pdf).
- `[Ter]` — I. Terek, _Equivalence relations, quotients, and examples_ (lecture notes): https://web.williams.edu/Mathematics/it3/texts/quotients.pdf — Theorem 1.

## Definition

> [!definition] Parameters
> - $A$: a [[Set]].
> - $\sim$: an [[Equivalence Relation]] on $A$.

> [!definition] Quotient Category
> Instantiates:: [[Category]].
>
> ---
> Let $\sim$ be an [[Equivalence Relation]] on a set $A$.
> Quotient Category consists of
> - Object: $(\varphi, Z)$ where $Z$ is a set and [[Morphism]] $\varphi: A \rightarrow Z$ such that:
> $$a_1 \sim a_2 \implies \varphi(a_1) = \varphi(a_2).$$
> - For $(\varphi_1, Z_1)$ and $(\varphi_2, Z_2)$, the morphisms are the functions $\sigma: Z_1 \to Z_2$ such that this diagram
> $$\begin{CD}
> Z_1 @>\sigma>> Z_2 \\
> @A\varphi_1AA @AA\varphi_2A \\
> A @= A
> \end{CD}$$
> commutes.
>
> `[Alu I.5.3]` `[Ter Thm 1]`

> [!remark]
> The objects are objects of the [[Coslice Category]] $\mathsf{Set}^A$ (morphisms out of $A$, `[Rie Exer 1.1.iii]`) and the morphisms are exactly those of $\mathsf{Set}^A$: this is the full subcategory of $\mathsf{Set}^A$ on the functions constant on $\sim$-classes.

## Property

### Universal Property

> [!proposition] Quotient as initial object — $(\pi, A/{\sim})$ is initial
> Denoting by $\pi$ the [[Canonical Projection]], the pair $(\pi, A/_\sim)$ is an [[Universal Property|initial object]] of this category. `[Alu I.5.3]` `[Ter Thm 1]`

## Related

### Siblings
- [[Quotient Relation]] — the quotient $A/{\sim}$ whose projection is initial here.

### Prerequisites
- [[Coslice Category]] — the ambient category $\mathsf{Set}^A$.
- [[Canonical Projection]] — the map $\pi: A \to A/{\sim}$.
