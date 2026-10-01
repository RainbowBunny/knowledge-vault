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
