Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter II: Groups, first encounter, Section 7.2: Quotient Group; Section 7.4: Quotient by normal subgroups; Section 8.5: The index and Lagrange's theorem.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_: https://abstract.ups.edu/aata/ (read in the HTML edition at https://judsonbooks.org/aata-files/aata-html/; result numbers as there).

## Definition

> [!definition] Parameters
> - $G$: a [[Group]].
> - $\sim$: an [[Equivalence Relation]] on $G$.
> - $\pi: G \rightarrow G/_\sim$: the quotient function.

> [!definition] Quotient Group
> Extends:: [[Quotient Relation]].
>
> ---
> For an [[Equivalence Relation]] $\sim$ on a group $G$; given a group $G /_\sim$ and a [[Group Homomorphism]] $\pi: G \rightarrow G /_\sim$ satisfying the appropriate universal property (the first proposition of Property). `[Alu II §7.2]`

> [!definition] Parameters
> - $G$: a [[Group]].
> - $H \trianglelefteq G$: a [[Normal Subgroup]].

> [!definition] Quotient by Normal Subgroup
> Let $H$ be a [[Normal Subgroup]] of a group $G$. The **quotient group of $G$ modulo $H$**, denoted $G/H$, is the group $G/_\sim$ obtained from the relation $\sim$ as in [[Coset]]. `[Alu II §7.4]`
>
> Concretely, $G/H$ is the set of cosets of $H$ with $(aH)(bH) = abH$, a group of order $[G:H]$ `[Jud Thm 10.1.4]`.

### Index

> [!definition] Parameters
> - $G$: a [[Group]].
> - $H \leq G$: a [[Subgroup]], not necessarily normal.
> - $G/H$: the set of left [[Coset|cosets]] $aH$ of $H$.

> [!definition] Index
> The **index** of $H$ in $G$, denoted $[G : H]$, is the number of elements $|G / H|$ of $G/H$, when this is finite, and $\infty$ otherwise. `[Alu II §8.5]` `[Jud §6.1]`

## Property

> [!proposition] When classes multiply — $[a][b] = [ab]$ is a group law iff $\sim$ is compatible with multiplication on both sides
> With notation as above, the operation
> $$[a] \circ [b] = [ab]$$
> defines a group structure on $G/_\sim$ if and only if for all $a, a', g \in G$ with $a \sim a'$:
> - $ga \sim ga'$;
> - $ag \sim a'g$.
>
> In this case the quotient function $\pi: G \rightarrow G/_\sim$ is a [[Group Homomorphism]] and is universal with respect to homomorphisms $\varphi: G \rightarrow G'$ such that $a \sim a' \Longrightarrow \varphi(a) = \varphi(a')$. `[Alu II §7.2]`

> [!theorem] Universal property of the quotient — a homomorphism whose kernel contains $H$ factors uniquely through $G/H$
> Let $H$ be a [[Normal Subgroup]] of a group $G$. Then for every [[Group Homomorphism]] $\varphi: G \rightarrow G'$ such that $H \subseteq \ker \varphi$ there exists a unique group homomorphism $\tilde{\varphi}: G / H \rightarrow G'$ so that the diagram
> $$
> \begin{CD}
> G @>>{\varphi}> G' \\
> @V{\pi}VV @AA{\exists!\tilde{\varphi}}A \\
> G/H @= G/H
> \end{CD}
> $$
> commutes, that is,
> $$\varphi = \tilde{\varphi} \circ \pi.$$
> `[Alu II §7.4]`

### Lagrange's Theorem

> [!lemma] Cosets have the size of $H$ — $h \mapsto gh$ and $h \mapsto hg$ are bijections
> Let $H$ be a [[Subgroup]] of a [[Group]] $G$. Then $\forall g \in G$ the [[Function]]
> $$\begin{align}
> &H \rightarrow gH, \quad h \mapsto gh, \\
> &H \rightarrow Hg, \quad h \mapsto hg
> \end{align}$$
> are [[Bijection]]. `[Alu II §8.5]` `[Jud Prop 6.2.1]`

> [!corollary] Lagrange's theorem — the order of a subgroup divides the order of the group
> If $G$ is a [[Group|Finite Group]] and $H \subseteq G$ is a [[Subgroup]], then
> $$|G| = [G : H] \cdot |H|.$$
> In particular, $|H|$ is a divisor of $|G|$. `[Alu II §8.5]` `[Jud Thm 6.2.2]`

## Related

### Constructions
- [[Subgroup of Quotient Group]] — the subgroups of $G/H$ are the $K/H$ with $H \leq K \leq G$; third isomorphism theorem
- [[Canonical Decomposition]] — with $H = \ker\varphi$, $G/\ker\varphi \cong \varphi(G)$ (First Isomorphism Theorem `[Jud Thm 11.2.1]`)
- [[Group Presentation]] — a group as a quotient $F(A)/R$ of a [[Free Group]]

### Siblings
- [[Quotient Ring]] — the quotient of a ring by an [[Ideal]]

### Prerequisites
- [[Quotient Relation]] — the origin
- [[Normal Subgroup]] — what $H$ must be for $G/H$ to be a group
- [[Coset]] — the elements of $G/H$
