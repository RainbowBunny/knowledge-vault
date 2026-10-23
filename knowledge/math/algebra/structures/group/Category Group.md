Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter II: Groups, first encounter, Section 3.2: $\mathsf{Grp}$: Definition; Section 3.4: Product et al.
- `[Lei]` — T. Leinster, _Basic Category Theory_, arXiv:1612.09375: https://arxiv.org/abs/1612.09375

## Definition

> [!definition] Parameters
> - $G, H$: [[Group|groups]].

> [!definition] Category $\mathsf{Grp}$
> Instantiates:: [[Category]].
>
> ---
> $\mathsf{Grp}$ consists of
> - $\mathsf{Obj}(\mathsf{Grp})$ is the class of all [[Group]].
> - For $G, H$ groups, we define
> $$\mathsf{Hom}_\mathsf{Grp}(G, H)$$
> to be the set of [[Group Homomorphism]] $G \rightarrow H$.
>
> `[Alu II.3.2]` `[Lei Ex 1.1.3(b)]`

## Property

### Universal Property

> [!proposition] Initial and Final Object — the trivial group is both
> [[Trivial Group]] are both [[Universal Property|Initial]] and [[Universal Property|Final]] in $\mathsf{Grp}$. `[Alu II.3]`

### Product

> [!proposition] Product — the direct product is the categorical product
> With operation defined component-wise, $G \times H$ is a [[Categorical Product|Product]] in $\mathsf{Grp}$. `[Alu II.3.4]`

## Related

### Prerequisites
- [[Category]], [[Group Homomorphism]] — the objects and morphisms

### Siblings
- [[Category Abelian]] — the full subcategory of $\mathsf{Grp}$ on the abelian groups `[Lei §1.2]`
- [[Category G-Set]] — the sets with an action of one fixed group
