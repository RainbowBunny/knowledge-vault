## The Weil Pairing over Fields of Prime Power Order

### Embedding degree

> [!definition] Embedding degree
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $m \geq 1$ be an integer with $p \nmid m$. The **embedding degree** of $E$ with respect to $m$ is the smallest value of $k$ such that $$E(\mathbb F_{p^k})[m] \cong \mathbb Z / m \mathbb Z \times \mathbb Z / m \mathbb Z.$$

> [!proposition]
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $\ell \neq p$ be a prime. Assume that $E(\mathbb F_p)$ contains a point of order $\ell$. Then the embedding degree of $E$ with respect to $\ell$ is given by one of the following cases:
> 1. The embedding degree of $E$ is $1$. (This cannot happen if $\ell > \sqrt{p} + 1$)
> 2. $p \equiv 1 \pmod \ell$ and the embedding degree is $\ell$.
> 3. $p \not\equiv 1 \pmod \ell$ and the embedding degree is the smallest value of $k \leq 2$ such that $$p^k \equiv 1 \pmod \ell.$$

### Distortion Maps and a Modified Weil Pairing

> [!definition] Distortion Map
> Let $\ell \geq 3$ be a prime, let $E$ be an elliptic curve, let $P \in E[\ell]$ be a point of order $\ell$, and let $\phi: E \rightarrow E$ be a map from $E$ to itself. We say that $\phi$ is a $\ell$-**distorsion map** for $P$ if it has the following two properties:
> 1. $\phi(n P) = n \phi(P) \quad \forall n \geq 1.$
> 2. The number $e_{\ell}(P, \phi(P))$ is a primitive $l^{\text{th}}$ root of unity. This means that $$e_{\ell}(P, \phi(P))^r = 1 \qquad \text{if and only if} \qquad r \text{ is a multiple of } \ell.$$

> [!proposition]
> Let $E$ be an elliptic curve, let $\ell \geq 3$ be a prime, and view $E[\ell] = \mathbb Z / \ell \mathbb Z \times \mathbb Z / \ell \mathbb Z$ as a 2-dimensional vector space over the field $\mathbb Z / \ell \mathbb Z$. Let $P, Q \in E[\ell]$. Then the following are equivalent:
> 1. $P$ and $Q$ form a basis for the vector space $E[\ell]$.
> 2. $P \neq \mathcal O$ and $Q$ is not a multiple of $P$.
> 3. $e_{\ell}(P, Q)$ is a primitive $l^{\text{th}}$ root of unity.
> 4. $e_{\ell}(P, Q) \neq 1$.

> [!definition] Modified Weil Pairing
> Let $E$ be an elliptic curve, let $P \in E[\ell]$, and let $\phi$ be an $\ell$-distortion map for $P$. The modified Weil pairing $\hat e_\ell$ on $E[\ell]$ (relative to $\phi$) is defined $$\hat e_\ell(Q, Q') = e_{\ell}(Q, \phi(Q')).$$

> [!proposition]
> Let $E$ be an elliptic curve, let $P \in E[\ell]$, let $\phi$ be an $\ell$-distorsion map for $P$, and let $\hat e_l$ be the modified Weil pairing relative to $\phi$. Let $Q$ and $Q'$ be multiples of $P$. Then $$\hat e_\ell(Q, Q') = 1 \quad \text{if and only if} \quad Q = \mathcal O \text{ or } Q' = \mathcal O.$$

### A distortion map on $y^2 = x^3 + x$

> [!proposition]
> Let $E$ be the elliptic curve $$E: y^2 = x^3 + x$$ over a field $K$ and suppose that $K$ has an element $\alpha \in K$ satisfying $\alpha^2 = -1$. Define a map $\phi$ by $$\phi(x, y) = (-x, \alpha y) \quad \text{and} \quad \phi(\mathcal O) = \mathcal O.$$
> 1. Let $P \in E(K)$. Then $\phi(P) \in E(K)$, so $\phi$ is a map from $E(K)$ to itself.
> 2. The map $\phi$ respects the addition law on $E$, $$\phi(P_1 + P_2) = \phi(P_1) + \phi(P_2) \quad \forall P_1, P_2 \in E(K).$$
> In particular, $\phi(nP) = n\phi(P) \forall P \in E(K) \text{ and all } n \geq 1.$

> [!proposition] 
> Fix the following quantities
> - A prime $p$ satisfying $p \equiv 3 \pmod 4$.
> - The elliptic curve $E: y^2 = x^3 + x$.
> - An element $\alpha \in \mathbb F_{p^2}$ satisfying $\alpha^2 = -1$.
> - The map $\phi(x, y) = (-x, \alpha y)$.
> - A prime $\ell \geq 3$ such that there exists a nonzero point $P \in E(\mathbb F_p)[\ell]$.
> 
> Then $\phi$ is an $l$-distortion map for $P$, i.e., the quantity $$\hat e_{\ell}(P, P) = e_{\ell}(P, \phi (P))$$ is a primitive $\ell^{\text{th}}$ root of unity.
