Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter II: Groups, first encounter, Section 7.2: Quotient Group; Section 7.4: Quotient by normal subgroups; Section 8.5: The index and Lagrange's theorem.

## Definition

> [!definition] Quotient Group
> For an [[Equivalence Relation]] $\sim$ on a group $G$; given a group $G /_\sim$ and a [[Group Homomorphism]] $\pi: G \rightarrow G /_\sim$ satisfying the appropriate universal property.

> [!definition] Quotient by Normal Subgroup
> Let $H$ be a [[Normal Subgroup]] of a group $G$. The **quotient group of $G$ modulo $H$**, denoted $G/H$, is the group $G/_\sim$ obtained from the relation $\sim$ as in [[Coset]].

### Index

> [!definition] Index
> The **index** of $H$ in $G$, denoted $[G : H]$, is the number of elements $|G / H|$ of $G/H$, when this is finite, and $\infty$ otherwise.

## Property

> [!proposition]
> With notation as above, the operation
> $$[a] \circ [b] = [ab]$$
> defines a group structure on $G/_\sim$ if and only if $\forall a, a', g \in G$
> $$a \sim a' \Longrightarrow ga \sim ga' \land ag \sim ag'.$$
> In this case the quotient function $\pi: G \rightarrow G/_\sim$ is a [[Group Homomorphism]] and is universal with respect to homomorphisms $\varphi: G \rightarrow G'$ such that $a \sim a' \Longrightarrow \varphi(a) = \varphi(a')$.

> [!theorem] Universal property of the quotient
> Let $H$ be a [[Normal Subgroup]] of a group $G$. Then for every [[Group Homomorphism]] $\varphi: G \rightarrow G'$ such that $H \subset \ker \varphi$ there exists a unique group homomorphism $\tilde{\varphi}: G / H \rightarrow G'$ so that the diagram
> $$
> \begin{CD}
> G @>>{\varphi}> G' \\
> @V{\pi}VV @AA{\exists!\tilde{\varphi}}A \\
> G/H @= G/H
> \end{CD}
> $$

### Lagrange's Theorem

> [!lemma]
> Let $H$ be a [[Subgroup]] of a [[Group]] $G$. Then $\forall g \in G$ the [[Function]]
> $$\begin{align}
> &H \rightarrow gH, \quad h \mapsto gh, \\
> &H \rightarrow Hg, \quad h \mapsto hg
> \end{align}$$
> are [[Bijection]].

> [!corollary] Lagrange's Theorem
> If $G$ is a [[Group|Finite Group]] and $H \subseteq G$ is a [[Subgroup]], then $|G| = |G : H| \cdot |H|$. In particular, $|H|$ is a divisor of $|G|$.

