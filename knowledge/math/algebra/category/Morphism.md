## Definition

> [!definition] Morphism
> A morphism is a map between objects in an abstract [[Category]].

> [!definition] Identity Morphism
> We define the identity morphism $1_A \in \mathsf{Hom}_{\mathcal{C}}(A, A)$ that transform an object to itself.

## Property

### Isomorphism

> [!definition] Isomorphism
> Let $\mathcal C$ be a category. A morphism $f \in \mathsf{Hom}_{\mathcal{C}}(A, B)$ is an **isomorphism** if it has a (two-sided) inverse under composition: that is, if $\exists g \in \mathsf{Hom}_{\mathcal{C}}(B, A)$ such that 
> $$gf = 1_A, \quad fg = 1_B.$$

> [!proposition]
> The inverse of an isomorphism is unique.

> [!proposition]
> We denote inverse by $f^{-1}$.
> - Each identify $1_A$ is an isomorphism and is its own inverse.
> - If $f$ is an isomorphism, then $f^{-1}$ is an isomorphism and further $(f^{-1})^{-1} = f$.
> - If $f \in \mathsf{Hom}_{\mathcal C}(A, B), g \in \mathsf{Hom}_{\mathcal C}(B, C)$ are isomorphisms, then the composition $gf$ is an isomorphism and $(gf)^{-1} = f^{-1} g^{-1}$.

> [!corollary]
> Isomorphism is an equivalence relation. If two objects $A, B$ are isomorphic, one writes $A \cong B$.

### Monomorphism

> [!definition] Monomorphism
> Let $\mathcal C$ be a category. A morphism $f \in \mathsf{Hom}_{\mathcal{C}}(A, B)$ is a **monomorphism** if the following holds:
> - For all object $Z$ of $\mathcal C$ and all morphisms $\alpha', \alpha'' \in \mathsf{Hom}_{\mathcal{C}}(Z, A)$,
> $$f \circ \alpha' = f \circ \alpha'' \Longrightarrow \alpha' = \alpha''.$$

### Epimorphism

> [!definition] Epimorphisms
> Let $\mathcal C$ be a category. A morphism $f \in \mathsf{Hom}_{\mathcal{C}}(A, B)$ is an **epimorphism** if the following holds:
> - For all object $Z$ of $\mathcal C$ and all morphisms $\beta', \beta'' \in \mathsf{Hom}_{\mathcal{C}}(B, Z)$:
> $$\beta' \circ f = \beta'' \circ f \Longrightarrow \beta' = \beta''.$$

## Variant

### Endomorphism

> [!definition] Endomorphism
> A morphism of an object $A$ of a category $\mathcal C$ to itself is called an **endomorphism**; $\mathsf{Hom}_{\mathcal{C}}(A)$ is denoted $\mathsf{End}_{\mathcal{C}}(A)$.

### Automorphism

> [!definition] Automorphism
> An **automorphism** of an object $A$ of a category $\mathcal C$ is an isomorphism from $A$ to itself. The set of automorphisms of $A$ is denoted $\mathsf{Aut}_{\mathcal{C}}(A)$; it is a subset of $\mathsf{End}_{\mathcal{C}}(A)$.

> [!proposition]
> - The composition of two elements $f, g \in \mathsf{Aut}_{\mathcal{C}}(A)$ is an element $gf \in \mathsf{Aut}_{\mathcal{C}}(A)$.
> - Composition is associative.
> - $\mathsf{Aut}_{\mathcal{C}}(A)$ contains the element $1_A$, which is an identity for composition.
> - Every element $f \in \mathsf{Aut}_{\mathcal{C}}(A)$ has an inverse $f^{-1} \in \mathsf{Aut}_{\mathcal{C}}(A)$.
