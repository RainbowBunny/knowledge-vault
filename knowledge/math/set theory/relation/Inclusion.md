Reference:
- [[Book Reference|Element of Set Theory]] - Chapter 1: Introduction, Section: Baby Set Theory.

## Definition

> [!definition] Inclusion Relation
> A set $A$ is said to be a **subset** of a set $B$ (written $A \subseteq B$):
> $A \subseteq B \iff \forall x \in A: x \in B$.

## Property

> [!proposition] Monotonicity of Inclusion Relation
> Requires:: [[Intersection Set]], [[Union Set]].
> 
> ---
> - $A \subseteq B \implies A \cup C \subseteq B \cup C$.
> - $A \subseteq B \implies A \cap C \subseteq B \cap C$.
> - $A \subseteq B \implies \bigcup A \subseteq \bigcup B$.

> [!proposition] Antimonotone of Inclusion Relation
> Requires:: [[Complement Set]], [[Intersection Set]].
> 
> ---
> - $A \subseteq B \implies C - B \subseteq C - A$.
> - $\emptyset \neq A \subseteq B \implies \bigcap B \subseteq \bigcap A$.
