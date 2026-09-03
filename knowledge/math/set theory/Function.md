## Definition

> [!definition] Function
> A function is the subset of $A \times B$:
> $$\Gamma_f = \{(a, b) \in A \times B \; | \; b = f(a)\} \subseteq A \times B$$
> That satisfies:
> $$(\forall a \in A) (\exists! b \in B) \quad (a, b) \in \Gamma_f$$

> [!remark]
> Equivalently: a function is a [[Relation]] $\Gamma_f \subseteq A \times B$ that is left-total and functional. The condition $(\forall a)(\exists! b)$ above says exactly that.

> [!theorem]
> Two function $f$ and $g$ are equal if and only if
> 1. $f$ and $g$ have the same domain, and
> 2. $f(x) = g(x)$ for every $x$ in the domain of $f$.

### Domain

> [!definition] Domain
> For a function $f$, the set of all elements $x$ that occur as the first members of pairs $(x, y)$ in $f$ is called the **domain** of $f$ denoted as $\mathsf{dom}(f)$.

### Co-Domain

> [!definition] Co-domain
> For a function $f$, the set of all possible elements $y$ is called the **co-domain** of $f$.

### Range

> [!definition] Range
> The **range** of a function is the set containing all the possible values of $f(x)$ denoted as $\mathsf{ran}(f)$.

### Image

> [!definition] Image
> If $S$ is a subset of $A$, we denote by $f(S)$ the subset of $B$ defined by
> $$f(S) = \{b \in B \; | \; (\exists a \in A) \; b = f(a)\}.$$
> That is, $f(S)$ is the subset of $B$ consisting of all elements that are images of elements of $S$ by the function $f$. $f(A)$ is the **image** of $f$, denoted $\text{im} \; f$.

## Variant

### Partial Function




### Restriction

> [!definition] Restriction
> $f_S$ denotes the 'restriction' of $f$ to the subset $S$: this is the function $S \rightarrow B$ defined by
> $$(\forall s \in S): \quad f|_S(s) = f(s).$$

### Composition

> [!definition] Composition
> Functions may be **composed**: if $f: A \rightarrow B$ and $g: B \rightarrow C$ are functions, then so is the operation $g \circ f$ defined by
> $$(\forall a \in A) \quad (g \circ f)(a) = g(f(a))$$

> [!remark] Commutative Diagram Form of Composition
> $$\begin{CD} 
> A @>f>> B \\ 
> @| @VVgV \\ 
> A @>>{g \circ f}> C 
> \end{CD}$$

> [!remark] Associativity of Composition
> Composition is associative: if $f: A \rightarrow B, g : B \rightarrow C$, and $h: C \rightarrow D$ are functions, then $h \circ (g \circ f) = (h \circ g) \circ f$.

> [!remark] Commutative Diagram Form of Composition
> $$\begin{CD} 
> A @>f>> B @>h \circ g>> D\\ 
> @| @VVgV @|\\ 
> A @>>{g \circ f}> C @>h>> D 
> \end{CD}$$

### Natural Projection

> [!definition] Natural Projection
> Let $A, B$ be sets. Then there are **natural projections** $\pi_A, \pi_B$ defined by:
> $$\pi_A((a, b)) = a, \quad \pi_B((a, b)) = b$$
> for all $(a, b) \in A \times B$. Both of these maps are (clearly) surjective.

### Natural Injections

> [!definition] Natural Injections
> Let $A, B$ be sets. Then there are **natural injections** from $A$ and $B$ to the disjoint union $A \amalg B$ obtained by sending $a \in A$ (resp., $b \in B$) to the corresponding element in the isomorphic copy $A'$ of $A$ (resp., $B'$ of $B$) in $A \amalg B$.

### Canonical Projection

> [!definition] Canonical Projection
> If $\sim$ is an equivalence relation on a set $A$, there is a canonical projection
> $$A \twoheadrightarrow A/_\sim$$
> obtained by sending every $a \in A$ to its equivalence class $[a]_\sim$.

### Canonical Decomposition

> [!definition] Canonical Decomposition
> A canonical decomposition is a function $f: A \rightarrow B$ determines an equivalence relation $\sim$ on $A$ as follows:
> - For all $a', a'' \in A$,
> $$a' \sim a'' \Longleftrightarrow f(a') = f(a'')$$

> [!theorem]
> Let $f: A \rightarrow B$ be any function, and define $\sim$ as above. Then $f$ decomposes as follows:
> $$A \twoheadrightarrow (A/_\sim) \; \substack{\sim \\ \longrightarrow \\ \tilde f} \; \text{im} f \hookrightarrow B$$
> where the first function is the canonical projection, the third function is the inclusion $\text{im} \; f \subseteq B$, and the bijection $\tilde f$ in the middle is defined by
> $$\tilde f([a]_\sim) = f(a)$$
> for all $a \in A$.

## Property

### Inverse

> [!definition] Inverse
> If $f: A \rightarrow B$ is a bijection, then we can define an inverse function:
> $$g: B \rightarrow A$$
> such that $a = g(b) \iff b = f(a)$.
> If $g \circ f = \text{id}_A$, we have a left-inverse.
> If $f \circ g = \text{id}_B$, we have a right-inverse.

> [!proposition]
> Assume $A \neq \emptyset$, and let $f: A \rightarrow B$ be a function. Then,
> 1. $f$ has a left-inverse if and only if it is injective.
> 2. $f$ has a right-inverse if and only if it is surjective.

> [!corollary]
> A function $f: A \rightarrow B$ is a bijection if and only if it has a (two-sided) inverse.

### Monomorphism

> [!definition] Monomorphism
> A function $f: A \rightarrow B$ is a **monomorphism** (or monic) if the following holds:
> - For all sets $Z$ and all functions $\alpha', \alpha'': Z \rightarrow A$
> $$f \circ \alpha' = f \circ \alpha'' \Longrightarrow \alpha' = \alpha''$$

> [!proposition]
> A function is injective if and only if it is a monomorphism.

### Epimorphism

> [!definition] Epimorphism
> A function $f: A \rightarrow B$ is a **epimorphism** if the following holds:
> - For all sets $Z$ and all function $\beta', \beta'': Z \rightarrow B$
> $$\beta' \circ f = \beta'' \circ f \Longrightarrow \beta' = \beta''$$

> [!proposition]
> A function is surjective if and only if it is a epimorphism.






