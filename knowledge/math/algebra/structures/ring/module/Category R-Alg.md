Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 5.2: The category R-Mod.
- `[Las]` — _Modules over Rings and Algebras: Basics_, lecture notes on C. Lassueur's teaching page (RPTU Kaiserslautern-Landau; rings unital and associative): https://agag-lassueur.math.rptu.de/~lassueur/en/teaching/SumSchools/IKIU22/IKIU22/YAC21_ModAndAlgs.pdf

## Definition

> [!definition] Parameters
> - $R$: a [[Commutative Ring]].

> [!definition] Category $R \mbox{-} \mathsf{Alg}$
> Instantiates:: [[Category]].
>
> ---
> The category $R \mbox{-} \mathsf{Alg}$ consists of
> - $\mathsf{Obj}(R \mbox{-} \mathsf{Alg})$: the class of all [[R-algebra|$R$-algebras]] $\alpha: R \rightarrow S$, with the $R$-module structure $r \cdot s = \alpha(r) s$.
> - For $R$-algebras $S, T$, $\mathsf{Hom}_{R \mbox{-} \mathsf{Alg}}(S, T)$: the maps $\varphi: S \rightarrow T$ that are both a [[Ring Homomorphism]] and a homomorphism of $R$-modules.
>
> `[Las Def F.1(b)]`

## Property

> [!proposition] Morphisms over $R$ — a ring homomorphism is a morphism iff it commutes with the structure maps
> For $R$-algebras $\alpha: R \rightarrow S$ and $\beta: R \rightarrow T$, a [[Ring Homomorphism]] $\varphi: S \rightarrow T$ is a morphism of $R \mbox{-} \mathsf{Alg}$ if and only if
> $$\varphi \circ \alpha = \beta.$$
>
> ---
> $\varphi(r \cdot s) = \varphi(\alpha(r)) \varphi(s)$ and $r \cdot \varphi(s) = \beta(r) \varphi(s)$; these agree for all $s$ iff they agree at $s = 1_S$.
>
> `[Las Def F.1(b)]` with $r \cdot s = \alpha(r) s$

## Related

### Siblings
- [[Category R-Mod]] — forget the multiplication
- [[Coslice Category]] — by the proposition, $R \mbox{-} \mathsf{Alg}$ is the full subcategory of the coslice $R / \mathsf{Ring}$ on the $\alpha$ with central image
- [[Category Ring]] — rings and ring homomorphisms

### Prerequisites
- [[R-algebra]] — the objects
- [[Category]] — the structure instantiated
