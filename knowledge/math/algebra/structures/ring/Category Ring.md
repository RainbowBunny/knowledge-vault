Reference:
- `[Lei]` — T. Leinster, _Basic Category Theory_ (2014), arXiv:1612.09375 — Example 0.2; Example 1.1.3(c).
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — §16.3 Ring Homomorphisms and Ideals (read at the mirror https://judsonbooks.org/aata-files/aata-html/; item numbers as there).

## Definition

> [!definition] Parameters
> - $R$: a [[Ring]].
> - $S$: a [[Ring]].

> [!definition] Category $\mathsf{Ring}$
> Instantiates:: [[Category]].
>
> ---
> Category $\mathsf{Ring}$ consists of
> - $\mathsf{Obj}(\mathsf{Ring})$ is the class of all [[Ring]].
> - For $R, S$ rings, we define
> $$\mathsf{Hom}_\mathsf{Ring}(R, S)$$
> to be the set of ring [[Homomorphism]] $R \rightarrow S$ (see [[Ring Homomorphism]]).
>
> `[Lei Ex 1.1.3(c)]`

## Property

### Universal Property

> [!proposition] Initial Object — $\mathbb Z$ is initial in $\mathsf{Ring}$
> The category $\mathsf{Ring}$ has an initial object which is the ring of integers $\mathbb{Z}$ (with the usual operations $+, \cdot$).
> - For every ring $R$ we can define a unique [[Ring Homomorphism]] $\varphi: \mathbb{Z} \rightarrow R$ by
> $$(\forall n \in \mathbb{Z}): \varphi(n) = n \cdot 1_R$$
>
> `[Lei Ex 0.2]`

> [!remark] Uniqueness uses $\varphi(1) = 1$
> `[Lei Ex 0.2]` takes rings with $1$ and homomorphisms that preserve $1$, as [[Ring Homomorphism]] does. With the homomorphisms of `[Jud §16.3]`, which need not preserve $1$, the zero map $\mathbb Z \to R$ is a second homomorphism, and $\mathbb Z$ is not initial.

## Related

### Constructions
- [[Ring#Characteristic|Characteristic]] — the kernel of the map $\mathbb Z \to R$ out of the initial object.

### Siblings
- [[Category Group]] — the same construction for groups; there the [[Trivial Group]] is both initial and final.
- [[Commutative Ring Category]] — commutative rings with a map from a set $A$; its initial object is $\mathbb Z[x_1, \dots, x_n]$.

### Prerequisites
- [[Ring]], [[Ring Homomorphism]].
