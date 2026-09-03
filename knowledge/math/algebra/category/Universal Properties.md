## Definition

> [!definition] Universal Property
> Object $X$ is universal with respect to the following property: For any $Y$ such that ..., there exists a unique morphism $Y \rightarrow X$ such that...

### Initial Objects

> [!definition] Initial Objects
> Let $\mathcal C$ be a category. We say that an object $I$ of $\mathcal C$ is **initial** in $\mathcal C$ if for every object $A$ of $\mathcal C$ there exists exactly one morphism $I \rightarrow A$ in $\mathcal C$:
> $$\forall A \in \text{Obj}(\mathcal C): \quad \text{Hom}_{\mathcal C}(I, A) \text{ is a singleton.}$$

> [!proposition]
> Let $\mathcal C$ be a category, If $I_1, I_2$ are both initial objects in $\mathcal C$, then $I_1 \cong I_2$.

### Final Objects

> [!definition] Final Objects
> Let $\mathcal C$ be a category. We say that an object $F$ of $\mathcal C$ is **final** in $\mathcal C$ if for every object $A$ of $\mathcal C$ there exists exactly one morphism $A \rightarrow F$ in $\mathcal C$:
> $$\forall A \in \text{Obj}(\mathcal C): \quad \text{Hom}_{\mathcal C}(A, F) \text{ is a singleton}$$

> [!proposition]
> Let $\mathcal C$ be a category, If $F_1, F_2$ are both final objects in $\mathcal C$, then $F_1 \cong F_2$.

## Example

### Quotients

> [!example] Quotients
> Let $\sim$ be an equivalence relation defined on a set $A$. Then:
> "The quotient $A / \sim$ is universal with respect to the property of mapping $A$ to a set in such a way that equivalent elements have the same image."

> [!proposition]
> Denoting by $\pi$ the [[Function#Canonical Projection|Canonical Projection]], the pair $(\pi, A/\sim)$ is an initial object of this category.

### Products

> [!example] Products
> Let $A, B$ be sets, and consider the product $A \times B$, with the two [[Function#Natural Projection|Natural Projection]] $\pi_A, \pi_B$. Then for every set $Z$ and morphisms $f_A \in \mathsf{Hom}_{\mathcal C}(Z, A), f_B \in \mathsf{Hom}_{\mathcal{C}}(Z, B)$, there exists a unique morphism $\sigma \in \mathsf{Hom}_{\mathcal{C}}(Z, A \times B)$:
> $$\sigma(z) = (f_A(z), f_B(z)).$$
> 


$$\begin{CD}
@. Z @.\\
@. @VV{\sigma}V @.\\
A @<{\pi_A}<< A\times B @>{\pi_B}>> B
\end{CD}$$
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