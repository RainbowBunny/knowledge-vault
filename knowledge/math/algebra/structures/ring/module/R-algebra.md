Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 5.2: The category R-Mod.
- `[Las]` — _Modules over Rings and Algebras: Basics_, lecture notes on C. Lassueur's teaching page (RPTU Kaiserslautern-Landau; rings unital and associative): https://agag-lassueur.math.rptu.de/~lassueur/en/teaching/SumSchools/IKIU22/IKIU22/YAC21_ModAndAlgs.pdf

## Definition

> [!definition] Parameters
> - $R$: a [[Commutative Ring]].
> - $S$: a [[Ring]].
> - $\alpha: R \rightarrow S$: a [[Ring Homomorphism]].

> [!definition] R-algebra
> Extends:: [[Ring Homomorphism]].
> Requires:: [[Ring Center]].
>
> ---
> Let $R$ be a [[Commutative Ring]]. An $R \mbox{-} \mathsf{algebra}$ is a [[Ring Homomorphism]] $\alpha: R \rightarrow S$ such that $\alpha(R)$ is contained in the [[Ring Center|center]] of $S$.
>
> `[Alu III.5.2]`

> [!remark] Equivalent form — a ring that is an $R$-module
> `[Las Def F.1(a)]` defines an $R$-algebra as a ring $S$ with a left [[R-Module|$R$-module]] structure on $(S, +)$ compatible with the multiplication:
> $$\forall r \in R,\ \forall a, b \in S: r \cdot (ab) = (r \cdot a) b = a (r \cdot b).$$
> The two forms correspond by
> - from $\alpha$: $r \cdot s = \alpha(r) s$;
> - back: $\alpha(r) = r \cdot 1_S$.

## Related

### Instantiations
- [[Polynomial Ring]] — $R \to R[x]$, $r \mapsto$ the constant polynomial $r$
- [[Matrix Ring]] — $r \mapsto r I_n$
- [[Group Algebra]] — $R[G]$

### Constructions
- [[Category R-Alg]] — $R$-algebras and their homomorphisms

### Siblings
- [[R-Module]] — an $R$-algebra is an $R$-module with a compatible multiplication
- [[Algebra Structure]] — division algebras over $\mathbb R$; the octonions there are not associative, so they are not $\mathbb R$-algebras in this sense

### Prerequisites
- [[Commutative Ring]] — the base ring $R$
- [[Ring Center]] — where $\alpha(R)$ must land
