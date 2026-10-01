Reference:
- [[Book Reference|Element of Set Theory]] - Chapter 2: Axioms and Operations, Section: Arbitrary Unions and Intersections.

## Definition

> [!definition] Union Set
> Specializes:: [[Set]].
> Requires:: [[Axiom of Set Theory]].
> 
> ---
> For any sets $a$ and $b$, the **union** $a \cup b$ is the set whose members are those sets belonging either to $a$ or to $b$ (or both).

> [!definition] Arbitrary Union
> For any set $A$, the **union** $\cup A$ of $A$ is the set defined by
> $$\bigcup A = \{x \mid (\exists a \in A) \; x \in a\}.$$

## Property

> [!theorem]
> $A \subseteq B \implies \bigcup A \subseteq \bigcup B$.

> [!theorem]
> $\forall x \in A: x \subseteq B \implies \bigcup A \subseteq B$.

> [!theorem]
> - $\forall A: \bigcup \mathcal{P}(A) = A$.
> - $A \subseteq \mathcal{P}(\bigcup{A})$.


