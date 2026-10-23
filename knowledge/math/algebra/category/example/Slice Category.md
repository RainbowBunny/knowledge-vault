Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter I: Preliminaries: Set theory and categories, Section 3.2: Examples.
- `[Rie]` — E. Riehl, _Category Theory in Context_ (2016): https://math.jhu.edu/~eriehl/context.pdf — Exercise 1.1.iii (read at the mirror https://www.math.ucla.edu/~mopie/context.pdf).

## Definition

> [!definition] Parameters
> - $\mathsf C$: a [[Category]].
> - $A$: an object of $\mathsf C$.

> [!definition] Slice Category
> Instantiates:: [[Category]].
>
> ---
> Let $\mathsf{C}$ be a [[Category]], and let $A \in \mathsf{Obj}(\mathsf{C})$, we define the slice category $\mathsf{C}_A$ consists of:
> - $\mathsf{Obj}(\mathsf{C}_A)$: All [[Morphism]] from any object to $A$.
> - For $\varphi_1 \in \mathsf{Hom}_\mathsf{C}(Z_1, A)$ and $\varphi_2 \in \mathsf{Hom}_\mathsf{C}(Z_2, A)$, define $\mathsf{Hom}_{\mathsf{C}_A}(\varphi_1, \varphi_2)$ is the set of $\sigma \in \mathsf{Hom}_\mathsf{C}(Z_1, Z_2)$ such that this diagram
> $$\begin{CD}
> Z_1 @>\sigma>> Z_2 \\
> @V\varphi_1VV @VV\varphi_2V \\
> A @= A
> \end{CD}$$
> commutes, i.e. $\varphi_2 \circ \sigma = \varphi_1$.
>
> `[Alu I.3.2]` `[Rie Exer 1.1.iii]`

> [!remark] Notation
> `[Rie Exer 1.1.iii]` writes $\mathsf C/A$ and calls it the slice category of $\mathsf C$ *over* $A$.

## Related

### Siblings
- [[Coslice Category]] — the dual: objects are morphisms *out of* $A$.
