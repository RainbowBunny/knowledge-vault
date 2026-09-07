## Definition

> [!definition] Group Homomorphisms
> Let $(G, \star_G)$ and $(H, \star_H)$ be groups. A function $\phi: G \rightarrow H$ is called a **(groups) homomorphism** if it satisfies $$\phi(g_1 \star_G g_2) = \phi(g_1) \star_H \phi(g_2) \; \forall g_1, g_2 \in G.$$

### Group Isomorphisms

> [!definition] Isomorphisms
> - See [[Morphism#Isomorphisms|Isomorphisms]].

> [!proposition]
> Let $\phi: G \rightarrow H$ be a group homomorphism. Then $\phi$ is an isomorphism of groups if and only if it is a bijection.

> [!definition] Isomorphic
> Two groups $G, H$ are **isomorphic** if there is a bijective group homomorphism $G \rightarrow H$.

> [!proposition]
> Let $\phi: G \rightarrow H$ be an isomorphism
> - $(\forall g \in G): |\phi(g)| = |g|$;
> - $G$ is commutative if and only if $H$ is commutative.

### Monomorphisms

> [!definition] Group Monomorphism
> - See [[Morphism#Monomorphisms|Monomorphism]].

> [!proposition]
> The following are equivalent:
> - $\phi$ is a monomorphism;
> - $\text{ker} \; \phi = \{e_G\}$;
> - $\phi: G \rightarrow G'$ is injective (as a set-function).

## Property

### Inverse

> [!proposition]
> Let $e_G$ be the identity element of $G$, let $e_H$ be the identity element of $H$, and let $g \in G$. Then $$\phi(e_G) = e_H \quad \text{and} \quad \phi(g^{-1}) = \phi(g)^{-1}.$$

### Order

> [!proposition]
> Let $\phi: G \rightarrow H$ be a group homomorphism, and let $g \in G$ be an element of finite order. Then $|\phi(g)|$ divides $|g|$.

## Example

> [!example]
> Each of the following maps is a group homomorphism
> 1. The map $\phi : \mathbb Z \rightarrow Z / N \mathbb Z$ that sends $a \in \mathbb Z$ to $a \mod N$ in $\mathbb Z / N \mathbb Z$.
> 2. The map $\phi : \mathbb R^* \rightarrow GL_2(\mathbb R)$ defined by $\phi(a) = \begin{pmatrix}a & 0 \\ 0 & a^{-1}\end{pmatrix}.$
