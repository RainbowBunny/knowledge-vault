## Definition

> [!definition] Category
> A **category** $\mathcal{C}$ consists of:
> - A collection of Object $\mathsf{Obj}(\mathcal{C})$.
> - A collection of [[Morphism]] (arrow) $\mathsf{Hom}_{\mathcal{C}}(A, B)$ for each pair of objects $A, B$.
> - An [[Associativity|Associative]], [[Identity Element]] binary operation $\circ$ between Morphism called composition.

> [!remark]
> $f \in \text{Hom}_{\mathcal C}(A, B)$ is the same as $f: A \rightarrow B$.



## Property



## Example

### Equivalence Category

> [!example] Equivalence Category
> Suppose $S$ is a set and $\sim$ is a relation on $S$ satisfying the reflexive and transitive properties. Then we can encode this data into a category:
> - **Objects**: The elements of $S$.
> - **Morphisms**: If $a, b$ are objects (that is, if $a, b \in S$), then let $\text{Hom}(a, b)$ be the set consisting of the element $(a, b) \in S \times S$ if $a \sim b$, and let $\text{Hom}(a, b) = \emptyset$ otherwise.

### Small Category

> [!example] Small Category
> Let $S$ be a set. Define category $\hat {\mathcal S}$ by setting
> - $\text{Obj}(\hat {\mathcal S}) = \mathcal P(S)$, the power set $S$.
> - For $A, B$ objects of $\hat {\mathcal S}$, let $\text{Hom}_{\hat {\mathcal S}}(A, B)$ be the pair $(A, B)$ if $A \subseteq B$, and let $\text{Hom}_{\hat {\mathcal S}}(A, B) = \emptyset$ otherwise.


