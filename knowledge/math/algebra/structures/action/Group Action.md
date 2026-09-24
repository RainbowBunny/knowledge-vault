Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter II: Groups, first encounter, Section 9.1: Actions; Section 9.2: Actions on sets; Section 9.3: Transitive actions and the category G-Set.

## Definition

> [!definition] Group Action
> An **action** of a [[Group]] $G$ on an object $A$ of a [[Category]] $\mathsf{C}$ is a [[Homomorphism]]
> $$\sigma: G \rightarrow \mathsf{Aut}_\mathsf{C}(A).$$

> [!definition] Faithful
> An action of a [[Group]] $G$ on an object $A$ of a [[Category]] $\mathsf{C}$ is **faithful** (or **effective**) if the corresponding $\sigma: G \rightarrow \mathsf{Aut}_\mathsf{C}(A)$ is an [[Injection]].

> [!definition] Action on Set
> An **action** of a [[Group]] $G$ on a [[Set]] $A$ is a [[Function]]
> $$\rho: G \times A \rightarrow A$$
> such that:
> - $\forall a \in A: \rho(e_G, a) = a$.
> - $(\forall g, h \in G), (\forall a \in A): \rho(gh, a) = \rho(g, \rho(h, a))$.
> Usually, we can just remove $\rho$ and have a simpler [[Associativity]] operation:
> $$(\forall g, h \in G), (\forall a \in A): (gh) a = g (ha).$$

> [!definition] Orbit
> The **orbit** of $a \in A$ under an action of a [[Group]] $G$ is the [[Set]]
> $$O_G(a) = \{ga \mid g \in G\}.$$

> [!definition] Stabilizer
> The **stabilizer** [[Subgroup]] of $a$ consists of the elements of $G$ which fix $a$:
> $$\mathsf{Stab}_G(a) = \{g \in G \mid ga = a\}$$

## Property

> [!theorem]
> Every [[Group]] acts faithfully on some set. That is, every group may be realized as a [[Subgroup]] of a [[Symmetric Group]].
> 
> ---
> [[Group Action on Group|Left Multiplication]].

### Stabilizer

> [!proposition]
> Every [[Transitivity]] left-action of $G$ on a nonempty [[Set]] $A$ is [[Morphism|Isomorphic]] to the left-multiplication of $G$ on $G/H$, for $H$ = the stabilizer of any $a \in A$.
> 
> ---
> $H = \mathsf{Stab}_G(a)$
> $\varphi: G/H \rightarrow A,\quad gH \mapsto ga$

> [!corollary]
> Requires:: [[Quotient Group]].
> 
> ---
> If $O$ is an orbit of the action of a finite [[Group]] $G$ on a [[Set]] $A$, then $O$ is a finite set and
> $$|O| \mid |G|.$$
> 
> ---
> $|O| \cdot |\mathsf{Stab}_G(a)| = |G|$.

> [!proposition]
> Suppose a [[Group]] $G$ acts on a [[Set]] $A$, and let $a \in A, g \in G, b = ga$. Then
> $$\mathsf{Stab}_G(b) = g \mathsf{Stab}_G(a) g^{-1}$$



