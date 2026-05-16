## Short Integer Solutions Problem

> [!definition] Shortest Integer Solutions (SIS) problem
> Given $A \in \mathbb Z_q^{n \times m}$, find $z \in \mathbb Z^m$ such that $Az = 0 \pmod q$, where $z \neq 0$ and $z \in [-B, B]^m$ (and $B \ll q/2$).
> Denote an instance of this problem by $A$ for $\text{SIS}(n, m, q, B)$.

> [!definition] Short Integer Solution (SIS)
> Let $q, n, m, \beta$ be functions of a parameter $\lambda$. An instance of the $\text{SIS}_{q, n, m, \beta}$ problem is a matrix $A \leftarrow \mathbb Z_q^{n \times m}$. A solution to the problem is a nonzero vector $v \in \mathbb Z^m$ such that $||v|| \leq \beta$ and $A \cdot v = 0 \mod q$.

> [!proposition] Existence of an SIS solution
> For an instance $\text{SIS}(n, m, q, B, A)$:
> 1. Consider $n \geq m$, then $Az = 0$ has at most one unique solution thus only consider $n < m$.
> 2. If $(B + 1)^m > q^n$ then by pigeonhole principle there must exist $z_1, z_2 \in [-B/2, B/2]^m$ such that $z_1 \neq z_2$ and $Az_1 \equiv Az_2 \pmod q$, thus $z = z_1 - z_2$ is a solution to the problem. Thus, we assume $m > (n \log q) / \log(B + 1)$
> 3. The SIS solution is not unique.

## Inhomogeneous Short Integer Solutions Problem

> [!definition] Inhomogeneous Short Integer Solutions (ISIS) Problem
> Given $A \in \mathbb Z_q^{n \times m}$ and $b \in \mathbb Z_q^m$, find $z \in \mathbb Z^m$ such that $Az \equiv b \pmod q$ and $z \in [-B, B]^m$.
> Denote an instance of this problem by $(A, b)$ for $\text{ISIS}(n, m, q, B)$.

> [!definition] Inhomogeneous Short Integer Solution (ISIS) Problem
> Let $q, n, m, \beta$ be functions of a parameter $\lambda$. An instance of the $\text{ISIS}_{q, n, m, \beta}$ problem is a matrix $A \leftarrow \mathbb Z_q^{n \times m}$ and a vector $t \leftarrow \mathbb Z_q^n$. A solution to the problem is a vector $v \in \mathbb Z^m$ such that $||v|| \leq \beta$ and $A \cdot v = t \mod q$.

> [!remark]
> For an instance $\text{ISIS}(n, m, q, B, A, b)$:
> 1. Also consider $n < m$.
> 2. If $(2B + 1)^m \gg q^n$, then an ISIS solution is likely to exist (prove?).

> [!proposition]
> $\text{ISIS}$ and $\text{SIS}$ are equivalent.

### One-More-ISIS Assumption

> [!algorithm] One-More-ISIS Assumption 
> Let $q, n, m, \sigma, \beta$ be functions of security parameter $\lambda$. The $\text{one-more-ISIS}_{q, n, m, \sigma, \beta}$ assumption is defined using the following experiment.
> 1. The challenger $\mathcal C$ uniformly samples a matrix $C \in \mathbb Z_q^{n \times m}$ and sends $C$ to adversary $\mathcal A$.
> 2. The adversary adaptively makes queries of the following types to the challenger, in any order.
> 	- **Syndrome queries**: The adversary $\mathcal A$ requests $\mathcal C$ for a challenge vector, to which $\mathcal C$ replies with a uniformly sampled vector $t \leftarrow \mathbb Z_q^n$. We denote the set of received vectors by $S$.
> 	- **Preimage queries**: The adversary $\mathcal A$ queries a vector $t' \in \mathbb Z_q^n$, to which $\mathcal C$ replies with a short vector $y' \leftarrow D_{\mathbb Z^m, \sigma}$ such that $Cy' = t'$. We denote by $\ell$ the total number of preimage queries.
> 3. In the end, the adversary $\mathcal A$ outputs $\ell + 1$ pairs of the form $\{(y_j, t_j)\}_{j \in [\ell + 1]}$.
> 4. The adversary wins if $Cy_j = t_j, ||y_j|| \leq \beta$ and $t_j \in S$ for all $j \in [\ell + 1]$.
> 
> The $\text{one-more-ISIS}_{q, n, m, \sigma, \beta}$ assumption states that for every adversary $\mathcal A$ running in time $2^{o(\lambda)}$ making at most $\lambda^{O(1)}$ preimage queries and $2^{o(\lambda)}$ syndrome queries, the probability (over the randomness of $\mathcal A$ and $\mathcal C$) that $\mathcal A$ wins is $2^{-\ohm(\lambda)}$.
 
## Normal Form Inhomogeneous Short Integer Solutions Problem

> [!definition] Normal Form Inhomogeneous Short Integer Solutions (nf-ISIS) Problem 
> Given $A \in \mathbb Z_q^{n \times m}$ and $b \in \mathbb Z_q^n$, find $z \in \mathbb Z^{m + n}$ such that $[A | I_n] z = b \pmod q$ and $z \in [-B, B]^{m + n}$.
> Denote an instance of this problem by $(A, b)$ for $\text{nf-ISIS}(n, m, q, B)$.

> [!proposition]
> $\text{nf-ISIS}(n, m, q, B)$ and $\text{ISIS}(n, m + n, q, B)$ are equivalent.

## Application

> [!example] Collision-resistant Hash Function
> Let $A \in \mathbb Z_q^{n \times m}$, where $m > n \log q$. Define hash function $H_A : \{0, 1\}^m \rightarrow \mathbb Z^n_q$ by $H_A(z) \equiv Az \pmod q$. We have the following properties:
> 1. **Compression**: Since $m > n \log q$, we have $2^m > q^n$.
> 2. **Collision resistance**: Assume that there exist an algorithm can effectively find a $z_1, z_2 \in \{0, 1\}^m$ with $z_1 \neq z_2$ and $H_A(z_1) = H_A(z_2)$. Then, we can verify that $A(z_1 - z_2) \equiv 0 \pmod q$ so we find a solution to $\text{SIS}(n, m, q, 1, A)$.
