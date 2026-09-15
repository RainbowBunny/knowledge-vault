Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter I: Preliminaries: Set theory and categories, Exercise 3.7.

## Definition

> [!definition] Coslice Category
> Let $\mathsf{C}$ be a [[Category]], and let $A \in \mathsf{Obj}(\mathsf{C})$, we define the coslice category $\mathsf{C}_A$ consists of:
> - $\mathsf{Obj}(\mathsf{C}_A)$: All [[Morphism]] from $A$ to any object.
> - For $\varphi_1 \in \mathsf{Hom}_\mathsf{C}(A, Z_1)$ and $\varphi_2 \in \mathsf{Hom}_\mathsf{C}(A, Z_2)$, define $\mathsf{Hom}_{\mathsf{C}_A}(\varphi_1, \varphi_2)$ is the set of $\sigma$ such that this diagram
> $$\begin{CD}
> Z_1 @>\sigma>> Z_2 \\
> @A\varphi_1AA @AA\varphi_2A \\
> A @= A
> \end{CD}$$
> commutes.

