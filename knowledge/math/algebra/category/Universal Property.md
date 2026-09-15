Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter I: Preliminaries: Set theory and categories, Section 5.1: Initial and final objects; Section 5.2: Universal properties.

## Definition

> [!definition] Universal Property
> Object $X$ is universal with respect to the following property: For any $Y$ such that ..., there exists a unique morphism $Y \rightarrow X$ such that...

### Initial Objects

> [!definition] Initial Objects
> Let $\mathcal{C}$ be a category. We say that an object $I$ of $\mathcal{C}$ is **initial** in $\mathcal{C}$ if for every object $A$ of $\mathcal{C}$ there exists exactly one morphism $I \rightarrow A$ in $\mathcal{C}$:
> $$\forall A \in \mathsf{Obj}(\mathcal{C}): \quad \mathsf{Hom}_{\mathcal{C}}(I, A) \text{ is a singleton.}$$

> [!proposition]
> Let $\mathcal C$ be a category, If $I_1, I_2$ are both initial objects in $\mathcal C$, then $I_1 \cong I_2$.

### Final Objects

> [!definition] Final Objects
> Let $\mathcal{C}$ be a category. We say that an object $F$ of $\mathcal{C}$ is **final** in $\mathcal{C}$ if for every object $A$ of $\mathcal{C}$ there exists exactly one morphism $A \rightarrow F$ in $\mathcal{C}$:
> $$\forall A \in \mathsf{Obj}(\mathcal{C}): \quad \mathsf{Hom}_{\mathcal{C}}(A, F) \text{ is a singleton}$$

> [!proposition]
> Let $\mathcal C$ be a category, If $F_1, F_2$ are both final objects in $\mathcal C$, then $F_1 \cong F_2$.






### Coproducts

> [!example] Coproducts
> Let $A, B$ be objects of a category $\mathcal C$. A coproduct $A \amalg B$ of $A$ and $B$ will be an object of $\mathcal C$, endowed with two morphisms $i_A: A \rightarrow A \amalg B, i_B: B \rightarrow A \amalg B$ and satisfying the following property:
> For all objects $Z$ and morphisms $f_A \in \text{Hom}_{\mathcal C}(A, Z), f_B \in \text{Hom}_{\mathcal C}(B, Z)$, there exists a unique morphism $\sigma : A \amalg B \rightarrow Z$ such that $\sigma i_A = f_A, \sigma i_B = f_B$.

> [!proposition]
> The disjoint union is a coproduct in $\text{Set}$:
> $$\sigma(c) = \begin{cases}
> f_A(a) \quad &\text{if } c = (0, a) \in \{0\} \times A, \\
> f_B(b) \quad &\text{if } c = (1, b) \in \{1\} \times B.
> \end{cases}$$