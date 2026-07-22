## Basic Definition

> [!definition] Groups Homomorphism
> Let $G$ and $H$ be groups. A function $\phi: G \rightarrow H$ is called a **(groups) homomorphism** if it satisfies $$\phi(g_1 \star g_2) = \phi(g_1) \star \phi(g_2) \; \forall g_1, g_2 \in G.$$

> [!proposition]
> Let $e_G$ be the identity element of $G$, let $e_H$ be the identity element of $H$, and let $g \in G$. Then $$\phi(e_G) = e_H \quad \text{and} \quad \phi(g^{-1}) = \phi(g)^{-1}.$$

> [!example]
> Each of the following maps is a group homomorphism
> 1. The map $\phi : \mathbb Z \rightarrow Z / N \mathbb Z$ that sends $a \in \mathbb Z$ to $a \mod N$ in $\mathbb Z / N \mathbb Z$.
> 2. The map $\phi : \mathbb R^* \rightarrow GL_2(\mathbb R)$ defined by $\phi(a) = \begin{pmatrix}a & 0 \\ 0 & a^{-1}\end{pmatrix}.$
