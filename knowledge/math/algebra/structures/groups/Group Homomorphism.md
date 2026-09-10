Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter II: Groups, first encounter, Section 3.1: Group homomorphism; Section 3.3: Pause for reflection; Section 4.2: Homomorphism and order; Section 4.3: Isomorphisms; Section 6.2: Examples: Kernel and image; Section 6.5: Monomorphisms.

## Definition

> [!definition] Group Homomorphism
> Let $(G, \star_G)$ and $(H, \star_H)$ be groups. A function $\varphi: G \rightarrow H$ is called a **(groups) homomorphism** if it satisfies $$\varphi(g_1 \star_G g_2) = \varphi(g_1) \star_H \varphi(g_2) \; \forall g_1, g_2 \in G.$$

> [!definition] Group Homomorphism (Category Definition)
> The function $\varphi: G \rightarrow H$ defines a **group homomorphism** if this diagram commutes.
> $$\begin{CD} 
G \times G @>\varphi \times \varphi>> H \times H\\ 
@V\star_GVV @VV\star_HV\\ 
A @>>\varphi> B 
\end{CD}$$

### Kernel

> [!definition] Kernel
> The **kernel** of $\varphi: G \rightarrow G'$ is the subset of $G$ consisting of elements mapping to the identity in $G'$:
> $$\ker \varphi = \{g \in G \; | \; \varphi(g) = e_{G'}\} = \varphi^{-1}(e_{G'}).$$

> [!proposition]
> Let $\varphi: G \rightarrow G'$ be a homomorphism. Then the [[Inclusion Function]] $\iota: \ker \varphi \hookrightarrow G$ is [[Universal Property|Final]] in the [[Category]] of group homomorphism $\alpha: K \rightarrow G$ such that $\varphi \circ \alpha$ is the [[Trivial Group]].

### Group Isomorphism

> [!definition] Isomorphisms
> - See [[Morphism|Isomorphisms]].

> [!proposition]
> Let $\varphi: G \rightarrow H$ be a group homomorphism. Then $\varphi$ is an isomorphism of groups if and only if it is a bijection.

> [!definition] Isomorphic
> Two groups $G, H$ are **isomorphic** if there is a bijective group homomorphism $G \rightarrow H$.

> [!proposition]
> Let $\varphi: G \rightarrow H$ be an isomorphism
> - $(\forall g \in G): |\varphi(g)| = |g|$;
> - $G$ is commutative if and only if $H$ is commutative.

### Monomorphisms

> [!definition] Group Monomorphism
> - See [[Morphism|Monomorphism]].

> [!proposition]
> The following are equivalent:
> - $\varphi$ is a monomorphism;
> - $\ker \varphi = \{e_G\}$;
> - $\varphi: G \rightarrow G'$ is injective (as a set-function).

## Property

### Inverse

> [!proposition]
> Let $e_G$ be the identity element of $G$, let $e_H$ be the identity element of $H$, and let $g \in G$. Then $$\varphi(e_G) = e_H \quad \land \quad \varphi(g^{-1}) = \phi(g)^{-1}.$$

### Order

> [!proposition]
> Let $\varphi: G \rightarrow H$ be a group homomorphism, and let $g \in G$ be an element of finite order. Then $|\varphi(g)|$ divides $|g|$.

## Example

> [!example]
> Each of the following maps is a group homomorphism
> 1. The map $\phi : \mathbb Z \rightarrow Z / N \mathbb Z$ that sends $a \in \mathbb Z$ to $a \mod N$ in $\mathbb Z / N \mathbb Z$.
> 2. The map $\phi : \mathbb R^* \rightarrow GL_2(\mathbb R)$ defined by $\phi(a) = \begin{pmatrix}a & 0 \\ 0 & a^{-1}\end{pmatrix}.$
