Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter I: Preliminaries: Set theory and categories, Section 3.2: Examples.

## Definition

> [!definition] Slice Category
> Let $\mathsf{C}$ be a [[Category]], and let $A \in \mathsf{Obj}(\mathsf{C})$, we define the slice category $\mathsf{C}_A$ consists of:
> - $\mathsf{Obj}(\mathsf{C}_A)$: All [[Morphism]] from any object to $A$.
> - For $\varphi_1 \in \mathsf{Hom}_\mathsf{C}(Z_1, A)$ and $\varphi_2 \in \mathsf{Hom}_\mathsf{C}(Z_2, A)$, define $\mathsf{Hom}_{\mathsf{C}_A}(\varphi_1, \varphi_2)$ is the set of $\sigma$ such that this diagram
> $$\begin{CD}
> Z_1 @>\sigma>> Z_2 \\
> @V\varphi_1VV @VV\varphi_2V \\
> A @= A
> \end{CD}$$
> commutes.
