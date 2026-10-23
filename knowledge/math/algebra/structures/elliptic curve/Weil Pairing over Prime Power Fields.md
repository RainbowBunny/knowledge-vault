Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (Springer), chapter on elliptic curves, the Weil pairing over fields of prime power order: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[Gal12]` — S. D. Galbraith, _Mathematics of Public Key Cryptography_ (CUP 2012), Chapter 26 Pairings on elliptic curves (Def 26.3.7, Thm 26.4.1, Def 26.6.4): https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch26.pdf
- `[GPS06]` — S. D. Galbraith, K. G. Paterson, N. P. Smart, _Pairings for Cryptographers_, ePrint 2006/165, §2 (pairing types): https://eprint.iacr.org/2006/165.pdf

## Definition

### Embedding degree

> [!definition] Parameters
> - $p$: a [[Prime]].
> - $E$: an elliptic curve over $\mathbb F_p$.
> - $m \geq 1$: an integer with $p \nmid m$.

> [!definition] Embedding degree
> Requires:: [[Elliptic Curves over Finite Fields]].
>
> ---
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $m \geq 1$ be an integer with $p \nmid m$. The **embedding degree** of $E$ with respect to $m$ is the smallest $k \geq 1$ such that $$m \mid p^k - 1,$$ so that $\mathbb F_{p^k}^*$ contains the $m$-th roots of unity.
>
> [HPS] instead calls embedding degree the smallest value of $k$ such that $$E(\mathbb F_{p^k})[m] \cong \mathbb Z / m \mathbb Z \times \mathbb Z / m \mathbb Z,$$ the degree of the field over which the whole $m$-torsion is defined. For a prime $m = \ell$ with $\ell \nmid p - 1$ the two agree (Balasubramanian–Koblitz); for $\ell \mid p - 1$ they can differ (case 2 of [[#Field of definition of the $\ell$-torsion]]).
>
> `[Gal12 Def 26.3.7, Thm 26.4.1]` `[HPS]`

### Distortion Maps and a Modified Weil Pairing

> [!definition] Parameters
> - $\ell \geq 3$: a [[Prime]].
> - $E$: an elliptic curve.
> - $P \in E[\ell]$: a point of order $\ell$.
> - $\phi: E \rightarrow E$: a map from $E$ to itself.
> - $e_\ell$: the [[Bilinear Pairings#Weil pairing|Weil pairing]] on $E[\ell]$.

> [!definition] Distortion Map
> Requires:: [[Bilinear Pairings]].
>
> ---
> Let $\ell \geq 3$ be a prime, let $E$ be an elliptic curve, let $P \in E[\ell]$ be a point of order $\ell$, and let $\phi: E \rightarrow E$ be a map from $E$ to itself. We say that $\phi$ is a $\ell$-**distortion map** for $P$ if it has the following two properties:
> 1. $\phi(n P) = n \phi(P) \quad \forall n \geq 1.$
> 2. The number $e_{\ell}(P, \phi(P))$ is a primitive $l^{\text{th}}$ root of unity. This means that $$e_{\ell}(P, \phi(P))^r = 1 \qquad \text{if and only if} \qquad r \text{ is a multiple of } \ell.$$
>
> `[HPS]` `[Gal12 Def 26.6.4]` — [Gal12] asks for an endomorphism $\psi$ with $e(P, \psi(P)) \neq 1$; for prime $\ell$ this is condition 2, by [[#Bases of the $\ell$-torsion]].

> [!definition] Parameters
> - $\phi$: an $\ell$-distortion map for $P$.
> - $Q, Q' \in E[\ell]$: points.

> [!definition] Modified Weil Pairing
> Let $E$ be an elliptic curve, let $P \in E[\ell]$, and let $\phi$ be an $\ell$-distortion map for $P$. The modified Weil pairing $\hat e_\ell$ on $E[\ell]$ (relative to $\phi$) is defined $$\hat e_\ell(Q, Q') = e_{\ell}(Q, \phi(Q')).$$
>
> `[HPS]`

## Property

### Field of definition of the $\ell$-torsion

> [!proposition] Field of definition of $E[\ell]$ — the smallest $k$ with $E[\ell] \subseteq E(\mathbb F_{p^k})$ is $1$, $\ell$, or the embedding degree
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $\ell \neq p$ be a prime. Assume that $E(\mathbb F_p)$ contains a point of order $\ell$. Then the embedding degree of $E$ with respect to $\ell$ in the sense of [HPS] (the smallest $k$ with $E(\mathbb F_{p^k})[\ell] \cong \mathbb Z/\ell\mathbb Z \times \mathbb Z/\ell\mathbb Z$) is given by one of the following cases:
> 1. The embedding degree of $E$ is $1$. (This cannot happen if $\ell > \sqrt{p} + 1$)
> 2. $p \equiv 1 \pmod \ell$ and the embedding degree is $\ell$.
> 3. $p \not\equiv 1 \pmod \ell$ and the embedding degree is the smallest value of $k \geq 2$ such that $$p^k \equiv 1 \pmod \ell,$$ which is the embedding degree of the definition above.
>
> `[HPS]` `[Gal12 Thm 26.4.1]` (case 3)

### Bases of the $\ell$-torsion

> [!proposition] Bases of $E[\ell]$ — $P, Q$ form a basis iff $e_\ell(P, Q) \neq 1$
> Let $E$ be an elliptic curve, let $\ell \geq 3$ be a prime, and view $E[\ell] = \mathbb Z / \ell \mathbb Z \times \mathbb Z / \ell \mathbb Z$ as a 2-dimensional vector space over the field $\mathbb Z / \ell \mathbb Z$. Let $P, Q \in E[\ell]$. Then the following are equivalent:
> 1. $P$ and $Q$ form a basis for the vector space $E[\ell]$.
> 2. $P \neq \mathcal O$ and $Q$ is not a multiple of $P$.
> 3. $e_{\ell}(P, Q)$ is a primitive $l^{\text{th}}$ root of unity.
> 4. $e_{\ell}(P, Q) \neq 1$.
>
> `[HPS]`

> [!proposition] Non-degeneracy of $\hat e_\ell$ — on multiples of $P$, $\hat e_\ell(Q, Q') = 1$ iff $Q$ or $Q'$ is $\mathcal O$
> Let $E$ be an elliptic curve, let $P \in E[\ell]$, let $\phi$ be an $\ell$-distortion map for $P$, and let $\hat e_l$ be the modified Weil pairing relative to $\phi$. Let $Q$ and $Q'$ be multiples of $P$. Then $$\hat e_\ell(Q, Q') = 1 \quad \text{if and only if} \quad Q = \mathcal O \text{ or } Q' = \mathcal O.$$
>
> `[HPS]`

## Example

### A distortion map on $y^2 = x^3 + x$

> [!proposition] An automorphism of $y^2 = x^3 + x$ — $\phi(x, y) = (-x, \alpha y)$ with $\alpha^2 = -1$ respects the group law
> Let $E$ be the elliptic curve $$E: y^2 = x^3 + x$$ over a field $K$ and suppose that $K$ has an element $\alpha \in K$ satisfying $\alpha^2 = -1$. Define a map $\phi$ by
> $$\phi(x, y) = (-x, \alpha y)$$
> $$\phi(\mathcal O) = \mathcal O.$$
> 1. Let $P \in E(K)$. Then $\phi(P) \in E(K)$, so $\phi$ is a map from $E(K)$ to itself.
> 2. The map $\phi$ respects the addition law on $E$, $$\phi(P_1 + P_2) = \phi(P_1) + \phi(P_2) \quad \forall P_1, P_2 \in E(K).$$
>
> In particular, $\phi(nP) = n\phi(P)$ for all $P \in E(K)$ and all $n \geq 1$.
>
> `[HPS]`

> [!proposition] A distortion map for $y^2 = x^3 + x$ over $\mathbb F_p$, $p \equiv 3 \pmod 4$ — $\hat e_\ell(P, P)$ is a primitive $\ell$-th root of unity
> Fix the following quantities
> - A prime $p$ satisfying $p \equiv 3 \pmod 4$.
> - The elliptic curve $E: y^2 = x^3 + x$.
> - An element $\alpha \in \mathbb F_{p^2}$ satisfying $\alpha^2 = -1$.
> - The map $\phi(x, y) = (-x, \alpha y)$.
> - A prime $\ell \geq 3$ such that there exists a nonzero point $P \in E(\mathbb F_p)[\ell]$.
>
> Then $\phi$ is an $l$-distortion map for $P$, i.e., the quantity $$\hat e_{\ell}(P, P) = e_{\ell}(P, \phi (P))$$ is a primitive $\ell^{\text{th}}$ root of unity.
>
> `[HPS]`

## Related

### Prerequisites
- [[Bilinear Pairings]] — the Weil pairing $e_\ell$ and its properties
- [[Elliptic Curves over Finite Fields]] — $E(\mathbb F_p)$ and Hasse's bound, used in case 1

### Constructions
- [[Bilinear Group]] — the modified Weil pairing on $\langle P \rangle$ is a symmetric pairing, $\mathbb G_1 = \mathbb G_2$ (Type 1); Type 1 pairings use supersingular curves `[GPS06 §2]`
