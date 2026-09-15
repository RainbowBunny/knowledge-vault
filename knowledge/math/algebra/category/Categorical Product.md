Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter I: Preliminaries: Set theory and categories, Section 5.1: Initial and final objects; Section 5.4: Products.

## Definition

> [!definition] Categorical Product
> Let $A, B$ be objects of a category $\mathsf{C}$. A product $A \times B$ of $A$ and $B$ will be an object $C$, endowed with two [[Natural Projection]] $\pi_A, \pi_B$.

## Property

> [!proposition] Universal Property
For every set $Z$ and morphisms 
> $$\begin{CD}
A @<f_A<< Z \\
@.   @|\\
B @<<f_B< Z
\end{CD}$$
> there exists a unique morphism $\sigma \in \mathsf{Hom}_{\mathcal{C}}(Z, A \times B)$ such that the diagram
> $$\begin{CD}
Z @= Z @= Z\\
@Vf_AVV @VV{\sigma}V @VVf_BV\\
A @<{\pi_A}<< A\times B @>{\pi_B}>> B
\end{CD}$$
> commutes.



