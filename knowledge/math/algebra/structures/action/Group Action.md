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

> [!definition] Fixed Point
> $Z$ is the set of **fixed points** of the action:
> $$Z = \{a \in S \mid (\forall g \in G): ga = a\}$$

## Property

> [!theorem]
> Every [[Group]] acts faithfully on some set. That is, every group may be realized as a [[Subgroup]] of a [[Symmetric Group]].
> 
> ---
> [[Group Action on Group|Left Multiplication]].

> [!proposition]
> With $B \subseteq A$ is the set of that has exactly one element for each nontrivial [[Orbit]] of the action. Then,
> $$|A| = |Z| + \sum_{a \in A} |G : G_a|.$$

> [!corollary]
> With $G$ is a [[p-Group]]:
> $$|Z| \equiv |A| \mod p$$


