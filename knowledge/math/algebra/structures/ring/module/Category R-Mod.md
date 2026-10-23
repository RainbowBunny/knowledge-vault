Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and modules, Section 5.2: The category R-Mod.
- `[Las]` — _Modules over Rings and Algebras: Basics_, lecture notes on C. Lassueur's teaching page (RPTU Kaiserslautern-Landau; rings unital and associative): https://agag-lassueur.math.rptu.de/~lassueur/en/teaching/SumSchools/IKIU22/IKIU22/YAC21_ModAndAlgs.pdf

## Definition

> [!definition] Parameters
> - $R$: a [[Ring]].

> [!definition] Category $R \mbox{-} \mathsf{Mod}$
> Instantiates:: [[Category]].
>
> ---
> The category $R \mbox{-} \mathsf{Mod}$ consists of
> - $\mathsf{Obj}(R \mbox{-} \mathsf{Mod})$: the class of all left [[R-Module|$R$-modules]].
> - For $R$-modules $M, N$, $\mathsf{Hom}_{R \mbox{-} \mathsf{Mod}}(M, N)$: the set of $R$-module homomorphisms, i.e. [[Group Homomorphism|group homomorphisms]] $\varphi: (M, +) \rightarrow (N, +)$ with
> $$(\forall r \in R)(\forall m \in M): \varphi(rm) = r \varphi(m).$$
>
> `[Alu III.5.2]` `[Las Not A.4, Def A.3]`

## Property

> [!proposition] $\mathbb Z$-modules are abelian groups — $\mathbb{Z} \mbox{-} \mathsf{Mod}$ is equivalent to $\mathsf{Ab}$
> Requires:: [[Category Abelian]].
>
> ---
> $\mathbb{Z} \mbox{-} \mathsf{Mod}$ is equivalent to $\mathsf{Ab}$: every abelian group is a $\mathbb Z$-module in exactly one way (see [[Abelian Group]]), and conversely.
>
> `[Alu III.5.2]` `[Las Rem A.5(b)]`

## Related

### Siblings
- [[Category Abelian]] — the case $R = \mathbb Z$
- [[Category R-Alg]] — the objects also carry a compatible ring multiplication
- [[Category Ring]] — rings and ring homomorphisms

### Prerequisites
- [[R-Module]] — the objects
- [[Category]] — the structure instantiated
