Reference:
- [[Book Reference|Element of Set Theory]] - Chapter 2: Axioms and Operations, Section: Algebra of Sets.

## Definition

> [!definition] Basic Operation of Set
> Requires:: [[Union Set]], [[Intersection Set]], [[Complement Set]], [[Inclusion]].
> 
> ---
> - $A \cup B = \{x \mid x \in A \lor x \in B\}$.
> - $A \cap B = \{x \mid x \in A \land x \in B\}$.
> - $A - B = \{x \in A \mid x \notin B\}$.
> - $-A = \{x \in S \mid x \notin A\}$.

## Property

> [!proposition] Commutative Law
> $\cup$ and $\cap$ satisfies [[Commutativity]]:
> - $A \cup B = B \cup A$.
> - $A \cap B = B \cap A$.

> [!proposition] Associative Law
> $\cup$ and $\cap$ satisfies [[Commutativity]]:
> - $A \cup (B \cup C) = (A \cup B) \cup C$.
> - $A \cap (B \cap C) = (A \cap B) \cap C$.

> [!proposition] Distributive Law
> $\cup$ and $\cap$ satisfies [[Distributivity]]:
> - $A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$.
> - $A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$.
> - $A \cup \bigcap R = \bigcap \{A \cup X \mid X \in R\}$ (for $R \neq \emptyset$).
> - $A \cap \bigcup R = \bigcup \{A \cap X \mid X \in R\}$.

> [!proposition] De Morgan's Law
> - $-(A_1 \cup \cdots \cup A_n) = -A_1 \cap \cdots \cap -A_n$.
> - $-(A_1 \cap \cdots \cap A_n) = -A_1 \cup \cdots \cup -A_n$.
> - $-\bigcup A = \bigcap \{-X \mid X \in A\}$.
> - $-\bigcap A = \bigcup \{-X \mid X \in A\}$.

> [!proposition] Identities involving $\emptyset$
> Requires:: [[Empty Set]].
> 
> ---
> - $A \cup \emptyset = A$.
> - $A \cap \emptyset = A$.
> - $A \cap (C - A) = \emptyset$.

> [!proposition] Identities Involving Subset
> Requires:: [[Axiom of Set Theory]].
> 
> ---
> Given $A \subseteq S$.
> - $A \cup S = S$.
> - $A \cap S = S$.
> - $A \cup -A = S$.
> - $A \cap -A = \emptyset$.


