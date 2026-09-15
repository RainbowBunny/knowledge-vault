Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter I: Preliminaries: Set theory and categories, Section 5.3: Quotients.

## Definition

> [!definition] Quotient Category
> Instantiates:: [[Slice Category]] on [[Equivalence Category]]
> 
> ---
> Let $\sim$ be an [[Equivalence Relation]] on a set $A$.
> Quotient Category consists of
> - Object: $(\varphi, Z)$ where $Z$ is a set and [[Morphism]] $\varphi: A \rightarrow Z$ such that:
> $$a_1 \sim a_2 \implies \varphi(a_1) \sim \varphi(a_2).$$
> - For $(\varphi_1, Z_1)$ and $(\varphi_2, Z_2)$, we define $\sigma$ such that this diagram
> $$\begin{CD}
> Z_1 @>\sigma>> Z_2 \\
> @A\varphi_1AA @AA\varphi_2A \\
> A @= A
> \end{CD}$$
> commutes.

## Property

### Universal Property

> [!proposition]
> Denoting by $\pi$ the [[Canonical Projection]], the pair $(\pi, A/_\sim)$ is an initial object of this category.
