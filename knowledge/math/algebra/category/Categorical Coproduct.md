Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter I: Preliminaries: Set theory and categories, Section 5.1: Initial and final objects; Section 5.5: Coproducts.
- `[nLab]` — nLab, _coproduct_: https://ncatlab.org/nlab/show/coproduct

## Definition

> [!definition] Parameters
> - $\mathsf C$: a [[Category]].
> - $A, B$: objects of $\mathsf C$.

> [!definition] Categorical Coproduct
> Requires:: [[Universal Property]].
>
> ---
> Let $A, B$ be objects of a [[Category]] $\mathsf{C}$. A **coproduct** $A \amalg B$ of $A$ and $B$ will be an object $C$, endowed with two morphisms
> - $\iota_A: A \to C$,
> - $\iota_B: B \to C$,
>
> satisfying the following universal property: for all objects $Z$ and morphisms
> $$\begin{CD}
> A @>f_A>> Z \\
> @.   @|\\
> B @>>f_B> Z
> \end{CD}$$
> there exists a unique morphism $\sigma: A \amalg B \rightarrow Z$ such that the diagram
> $$\begin{CD}
> Z @= Z @= Z\\
> @A{f_A}AA @AA{\sigma}A @AA{f_B}A\\
> A @>>{\iota_A}> A \amalg B @<<{\iota_B}< B
> \end{CD}$$
> commutes. `[Alu I.5.5]` `[nLab]`

> [!remark]
> $\iota_A, \iota_B$ are called coprojections, or sometimes injections or inclusions; in a general category they need not be [[Morphism#Monomorphism|monomorphisms]]. `[nLab]`

## Example

- [[Category Set]] — in $\mathsf{Set}$ the coproduct is the disjoint union. `[nLab]`

## Related

### Siblings
- [[Categorical Product]] — the dual notion: the same universal property with every arrow reversed.
- [[Natural Injection]] — a function; $\iota_A, \iota_B$ are morphisms of $\mathsf C$ and need not be injective.

### Prerequisites
- [[Universal Property]] — the form the definition takes.
