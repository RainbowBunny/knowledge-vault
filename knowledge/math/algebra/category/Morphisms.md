## Basic Definition

### Endomorphism

> [!definition] Endomorphism
> A morphism of an object $A$ of a category $\mathcal C$ to itself is called an **endomorphism**; $\text{Hom}_{\mathcal C}(A)$ is denoted $\text{End}_{\mathcal C}(A)$.

### Isomorphisms

> [!definition] Isomorphism
> Let $\mathcal C$ be a category. A morphism $f \in \text{Hom}_{\mathcal C}(A, B)$ is an **isomorphism** if it has a (two-sided) inverse under composition: that is, if $\exists g \in \text{Hom}_{\mathcal C}(B, A)$ such that 
> $$gf = 1_A, \quad fg = 1_B.$$

> [!proposition]
> The inverse of an isomorphism is unique.

> [!proposition]
> We denote inverse by $f^{-1}$.
> - Each identify $1_A$ is an isomorphism and is its own inverse.
> - If $f$ is an isomorphism, then $f^{-1}$ is an isomorphism and further $(f^{-1})^{-1} = f$.
> - If $f \in \text{Hom}_{\mathcal C}(A, B), g \in \text{Hom}_{\mathcal C}(B, C)$ are isomorphisms, then the composition $gf$ is an isomorphism and $(gf)^{-1} = f^{-1} g^{-1}$.

> [!corollary]
> Isomorphism is an equivalence relation. If two objects $A, B$ are isomorphic, one writes $A \cong B$.

### Automorphism

> [!definition] Automorphism
> An **automorphism** of an object $A$ of a category $\mathcal C$ is an isomorphism from $A$ to itself. The set of automorphisms of $A$ is denoted $\text{Aut}_{\mathcal C}(A)$; it is a subset of $\text{End}_{\mathcal C}(A)$.

> [!proposition]
> - The composition of two elements $f, g \in \text{Aut}_{\mathcal C}(A)$ is an element $gf \in \text{Aut}_{\mathcal C}(A)$.
> - Composition is associative.
> - $\text{Aut}_{\mathcal C}(A)$ contains the element $1_A$, which is an identity for composition.
> - Every element $f \in \text{Aut}_{\mathcal C}(A)$ has an inverse $f^{-1} \in \text{Aut}_{\mathcal C}(A)$.

### Monomorphisms

> [!definition] Monomorphism
> Let $\mathcal C$ be a category. A morphism $f \in \text{Hom}_{\mathcal C}(A, B)$ is a **monomorphism** if the following holds:
> - For all object $Z$ of $\mathcal C$ and all morphisms $\alpha', \alpha'' \in \text{Hom}_{\mathcal C}(Z, A)$,
> $$f \circ \alpha' = f \circ \alpha'' \Longrightarrow \alpha' = \alpha''.$$

### Epimorphisms

> [!definition] Epimorphisms
> Let $\mathcal C$ be a category. A morphism $f \in \text{Hom}_{\mathcal C}(A, B)$ is an **epimorphism** if the following holds:
> - For all object $Z$ of $\mathcal C$ and all morphisms $\beta', \beta'' \in \text{Hom}_{\mathcal C}(B, Z)$:
> $$\beta' \circ f = \beta'' \circ f \Longrightarrow \beta' = \beta''.$$
