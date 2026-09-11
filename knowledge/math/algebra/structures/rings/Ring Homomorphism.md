Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter III: Rings and modules, Section 2.1: Ring homomorphisms; Section 2.3: Monomorphisms and epimorphisms; Section 3.1: Ideals; Section 3.2: Quotients.

## Definition

> [!definition] Ring Homomorphism
> Let $R, S$ are rings, a function $\varphi: R \rightarrow S$ is a ring homomorphism if:
> - Addition is preserved:
> $$(\forall a, b \in R): \varphi(a + b) = \varphi(a) + \varphi(b)$$
> - Multiplication is preserved:
> $$(\forall a, b \in R): \varphi(a b) = \varphi(a) \varphi(b)$$
> - Identity is preserved:
> $$\varphi(1_R) = 1_S$$

### Kernel

> [!definition] Kernel
> The **kernel** of a homomorphism $\varphi: R \rightarrow S$ of [[Ring]] is
> $$\ker{\varphi} = \{r \in R \mid \varphi(r) = 0\}$$

> [!proposition]
> Let $\varphi: R \rightarrow S$ be any ring homomorphism. Then $\ker{\varphi}$ is an [[Ideal]] of $R$.
> 
> ---
> To be completed.

> [!theorem]
> Let $I$ be a [[Ideal|Two-sided Ideal]] of a [[Ring]] $R$. Then for every ring homomorphism $\varphi: R \rightarrow S$ such that $I \subseteq \ker \varphi$ there exists a unique ring homomorphism $\tilde{\varphi}: R / I \rightarrow S$ such that the diagram:
> $$\begin{CD}
R @>\varphi>> S\\
@| @AA\exists! \tilde{\varphi}A \\
R @>>\pi> S
\end{CD}$$
commutes.

## Property

### Ring Monomorphism

> [!proposition]
> Let $\varphi: R \rightarrow S$ be a ring homomorphism, the following are equivalent:
> - $\varphi$ is a [[Morphism#Monomorphism|Monomorphism]].
> - $\mathrm{ker} \; \varphi = \{0\}$.
> - $\varphi$ is an [[Injection]].
> 
> ---
> To be completed.
