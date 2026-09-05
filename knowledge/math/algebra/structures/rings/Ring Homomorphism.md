## Definition

> [!definition] Ring Homomorphism
> Let $R, S$ are rings, a function $\varphi: R \rightarrow S$ is a ring homomorphism if:
> - Addition is preserved:
> $$(\forall a, b \in R): \varphi(a + b) = \varphi(a) + \varphi(b)$$
> - Multiplication is preserved:
> $$(\forall a, b \in R): \varphi(a b) = \varphi(a) \varphi(b)$$
> - Identity is preserved:
> $$\varphi(1_R) = 1_S$$

## Property

### Ring Monomorphism

> [!proposition]
> Let $\varphi: R \rightarrow S$ be a ring homomorphism, the following are equivalent:
> - $\varphi$ is a [[Morphism#Monomorphism|Monomorphism]].
> - $\mathrm{ker} \; \varphi = \{0\}$.
> - $\varphi$ is an [[Injection]].
