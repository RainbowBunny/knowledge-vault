Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter I: Preliminaries: Set theory and categories, Section 5.1: Initial and final objects; Section 5.5: Coproducts.

## Definition

> [!definition] Categorical Coproduct
> Let $A, B$ be objects of a [[Category]] $\mathsf{C}$. A **coproduct** $A \amalg B$ of $A$ and $B$ will be an object $C$, endowed with two [[Natural Injection]] $\iota_A, \iota_B$.

## Property

> [!proposition] Universal Property
> For all objects $Z$ and morphisms 
> $$\begin{CD}
A @>f_A>> Z \\
@.   @|\\
B @>>f_B> Z
\end{CD}$$
> there exists a unique morphism $\sigma: A \amalg B \rightarrow Z$ such that the diagram
> $$\begin{CD}
Z @= Z @= Z\\
@A{f_A}AA @AA{\sigma}A @AA{f_B}A\\
A @>>{\iota_A}> A \amalg B @<<{\iota_B}< B
\end{CD}$$
> commutes.
