Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter II: Groups, first encounter, Section 7.2: Quotient Group; Section 7.4: Quotient by normal subgroups.

## Definition

> [!definition] Quotient Group
> For an [[Equivalence Relation]] $\sim$ on a group $G$; given a group $G /_\sim$ and a group homomorphism $\pi: G \rightarrow G /_\sim$ satisfying the appropriate universal property.

> [!definition] Quotient by Normal Subgroup
> Let $H$ be a [[Normal Subgroup]] of a group $G$. The **quotient group of $G$ modulo $H$**, denoted $G/H$, is the group $G/_\sim$ obtained from the relation $\sim$ as in [[Coset]].

## Property

> [!proposition]
> With notation as above, the operation
> $$[a] \circ [b] = [ab]$$
> defines a group structure on $G/_\sim$ if and only if $\forall a, a', g \in G$
> $$a \sim a' \Longrightarrow ga \sim ga' \land ag \sim ag'.$$
> In this case the quotient function $\pi: G \rightarrow G/_\sim$ is a homomorphism and is universal with respect to homomorphisms $\varphi: G \rightarrow G'$ such that $a \sim a' \Longrightarrow \varphi(a) = \varphi(a')$.


