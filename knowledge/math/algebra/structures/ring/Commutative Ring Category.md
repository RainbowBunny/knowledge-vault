Reference:
- `[Lei]` — T. Leinster, _Basic Category Theory_ (2014), arXiv:1612.09375 — Exercise 0.13; Example 1.2.4(b).

## Definition

> [!definition] Parameters
> - $A = \{a_1, \dots, a_n\}$: a [[Set]] of order $n$.

> [!definition] Commutative Ring Category
> Instantiates:: [[Category]].
>
> ---
> Category $\mathcal{R}_A$:
> - $\mathsf{Obj}(\mathcal{R}_A)$ consists of all pairs $(j, R)$ where $R$ is a [[Commutative Ring]] and
> $$j: A \rightarrow R$$
> is a [[Function]].
> - For two objects $(j_1, R_1)$ and $(j_2, R_2)$, $\mathsf{Hom}_{\mathcal{R}_A}((j_1, R_1), (j_2, R_2))$ is the set of [[Ring Homomorphism]] $\varphi: R_1 \rightarrow R_2$ for which the diagram
> $$\begin{CD}
> R_1 @>\varphi>> R_2 \\
> @Aj_1AA @AAj_2A \\
> A @= A
> \end{CD}$$
> is commutative, that is,
> $$\varphi \circ j_1 = j_2.$$
>
> `[Lei Ex 0.13]` (the case $n = 1$, as a universal property of $\mathbb Z[x]$)

## Property

> [!proposition] Free commutative ring — $(i, \mathbb{Z}[x_1, \dots, x_n])$ is initial in $\mathcal R_A$
> Let $i: A \to \mathbb{Z}[x_1, \dots, x_n]$ be the function $i(a_k) = x_k$. Then $(i, \mathbb{Z}[x_1, \dots, x_n])$ is [[Universal Property|Initial]] in $\mathcal{R}_A$.
>
> `[Lei Ex 1.2.4(b)]` (the free commutative ring on a set $S$ is the polynomial ring over $\mathbb Z$ in commuting variables $x_s$, $s \in S$) `[Lei Ex 0.13]` ($n = 1$)

## Related

### Siblings
- [[Category Ring]] — all rings, no map from $A$; its initial object is $\mathbb Z$, the case $A = \emptyset$ here (restricted to commutative rings).
- [[Coslice Category]] — the same "objects under $A$" shape, but there $A$ is an object of the category itself; here $A$ is a set and $j$ lands in the underlying set of $R$.

### Prerequisites
- [[Commutative Ring]], [[Ring Homomorphism]], [[Polynomial Ring]], [[Multivariate Polynomial]].
