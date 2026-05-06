## Short Integer Solutions Problem

> [!definition] Shortest Integer Solutions (SIS) problem
> Given $A \in \mathbb Z_q^{n \times m}$, find $z \in \mathbb Z^m$ such that $Az = 0 \pmod q$, where $z \neq 0$ and $z \in [-B, B]^m$ (and $B \ll q/2$).
> Denote an instance of this problem by $A$ for $\text{SIS}(n, m, q, B)$.

> [!proposition] Existence of an SIS solution
> For an instance $\text{SIS}(n, m, q, B, A)$:
> 1. Consider $n \geq m$, then $Az = 0$ has at most one unique solution thus only consider $n < m$.
> 2. If $(B + 1)^m > q^n$ then by pigeonhole principle there must exist $z_1, z_2 \in [-B/2, B/2]^m$ such that $z_1 \neq z_2$ and $Az_1 \equiv Az_2 \pmod q$, thus $z = z_1 - z_2$ is a solution to the problem. Thus, we assume $m > (n \log q) / \log(B + 1)$
> 3. The SIS solution is not unique.

## Inhomogeneous Short Integer Solutions Problem

> [!definition] Inhomogeneous Short Integer Solutions (ISIS) Problem
> Given $A \in \mathbb Z_q^{n \times m}$ and $b \in \mathbb Z_q^m$, find $z \in \mathbb Z^m$ such that $Az \equiv b \pmod q$ and $z \in [-B, B]^m$.
> Denote an instance of this problem by $(A, b)$ for $\text{ISIS}(n, m, q, B)$.

> [!remark]
> For an instance $\text{ISIS}(n, m, q, B, A, b)$:
> 1. Also consider $n < m$.
> 2. If $(2B + 1)^m \gg q^n$, then an ISIS solution is likely to exist (prove?).

> [!proposition]
> $\text{ISIS}$ and $\text{SIS}$ are equivalent.

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
