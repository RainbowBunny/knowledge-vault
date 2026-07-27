## Basic Definition

> [!definition] Category
> A **category** $\mathcal C$ consists of
> - A class $\text{Obj}(\mathcal C)$ of objects of the category; and
> - For every two objects $A, B$ of $C$, a set $\text{Hom}_{\mathcal C}(A, B)$ of morphisms, with the properties listed below.
> 1. For every object $A$ of $\mathcal C$, there exists (at least) one [[Morphisms]] $1_A \in \text{Hom}_{\mathcal C}(A, A)$, the 'identity' on $A$.
> 2. One can decompose morphisms: two morphisms $f \in \text{Hom}_{\mathcal C}(A, B)$ and $g \in \text{Hom}_{\mathcal C}(B, C)$ determine a morphism $gf \in \text{Hom}_{\mathcal C}(A, C)$. That is, for every triple of objects $A, B, C$ of $\mathcal C$ there is a function (of sets)
> $$\text{Hom}_{\mathcal C}(A, B) \times \text{Hom}_{\mathcal C}(B, C) \rightarrow \text{Hom}_{\mathcal C}(A, C)$$
> and the image of the pair $(f, g)$ is denoted $gf$.
> 3. This 'composition law' is associative: if $f \in \text{Hom}_{\mathcal C}(A, B), g \in \text{Hom}_{\mathcal C}(B, C)$, and $h \in \text{Hom}_{\mathcal C}(C, D)$, then
> $$(hg)f = h(gf)$$
> 4. The identity morphisms are identities with respect to composition: that is, for all $f \in \text{Hom}_{\mathcal C}(A, B)$ we have 
> $$f1_A = f, \quad 1_Bf = f$$

> [!remark]
> $f \in \text{Hom}_{\mathcal C}(A, B)$ is the same as $f: A \rightarrow B$.

### Opposite Category

> [!definition] Opposite Category
> Let $\mathcal C$ be a category. Consider a structure $\mathcal C^{op}$ with
> - $\text{Obj}(\mathcal C^{op}) = \text{Obj}(C)$.
> - For $A, B$ objects of $\mathcal C^{op}, \text{Hom}_{\mathcal C^{op}}(A, B) = \text{Hom}_{\mathcal C}(B, A)$.

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


