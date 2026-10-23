Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter I: Preliminaries: Set theory and categories, Exercise 3.1.
- `[Lei]` — T. Leinster, _Basic Category Theory_ (2014), arXiv:1612.09375 — Construction 1.1.9.
- `[Rie]` — E. Riehl, _Category Theory in Context_ (2016): https://math.jhu.edu/~eriehl/context.pdf — Definition 1.2.1; §1.2, the remark after Definition 1.2.7 (read at the mirror https://www.math.ucla.edu/~mopie/context.pdf).

## Definition

> [!definition] Parameters
> - $\mathcal C$: a [[Category]].

> [!definition] Opposite Category
> Instantiates:: [[Category]].
>
> ---
> Let $\mathcal C$ be a [[Category]]. Consider a structure $\mathcal C^{op}$ with
> - $\mathsf{Obj}(\mathcal C^{op}) = \mathsf{Obj}(\mathcal C)$.
> - For $A, B$ objects of $\mathcal C^{op}$: $\mathsf{Hom}_{\mathcal C^{op}}(A, B) = \mathsf{Hom}_{\mathcal C}(B, A)$; write $f^{op} \in \mathsf{Hom}_{\mathcal C^{op}}(A, B)$ for the morphism given by $f \in \mathsf{Hom}_{\mathcal C}(B, A)$.
> - The identity of $A$ in $\mathcal C^{op}$ is $1_A^{op}$.
> - Composition reverses the order: $g^{op} \circ f^{op} = (f \circ g)^{op}$.
>
> `[Alu Exer I.3.1]` `[Lei Constr 1.1.9]` `[Rie Def 1.2.1]`

## Property

> [!proposition] Duality of mono and epi — a monomorphism in $\mathcal C$ is an epimorphism in $\mathcal C^{op}$
> A [[Morphism#Monomorphism|monomorphism]] or [[Morphism#Epimorphism|epimorphism]] in $\mathcal C$ is, respectively, an epimorphism or monomorphism in $\mathcal C^{op}$. `[Rie §1.2]`

## Related

### Siblings
- [[Slice Category]] — another category built from $\mathcal C$, over a fixed object $A$.
- [[Coslice Category]] — another category built from $\mathcal C$, under a fixed object $A$.
