---
dg-publish: true
---
Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter II: Groups, first encounter, Section 1.2: Definition; Section 1.3: Basic Properties; Section 1.4: Cancellation; Exercise 1.3; Exercise 1.4; Exercise 1.5; Section 8.2: Presentations.

## Definition

>[!definition] Group
   A **group** consists of a nonempty set $G$ and a [[Binary Operation]] $\star$ on $G$:
> - $\star$ satisfies [[Associativity]], [[Identity Element]], [[Inverse Element]].

> [!definition] Group (Alternative)
> Alternatively, a group is a [[Monoid]] with [[Inverse Element]].

## Property

### Identity

> [!proposition] Uniqueness of Identity
> If $h \in G$ is an identity of $G$, then $h = e_G$.

### Inverse

> [!proposition] Uniqueness of Inverse
> If $h_1, h_2$ are both inverses of $g$ in $G$, then $h_1 = h_2$.

> [!proposition] Inverse of Product
> $$\forall g, h \in G, \quad (gh)^{-1} = h^{-1} g^{-1}$$

### Cancellation

> [!proposition]
> Let $(G, \star)$ be a group, [[Cancellativity]] for $\star$ holds. 


## Example

> [!example]
> If $|G| = p$ with prime $p$, then $G \cong \mathbb{Z} / p \mathbb{Z}$.

> [!example]
> Each of the following is a group:
> 1. $\text{GL}_n(\mathbb R) = \{n\text{-by-}n \text{ matrices } A \text{ with real coefficients and } \det(A) \neq 0\}$ with operation $\star$ is matrix multiplication.

> [!definition] General Linear Group
> The **General Linear Group** of order $s$, denoted $\text{GL}_s(\mathbb Z_n)$, is the monoid of invertible $s \times s$ matrices containing elements from $\mathbb Z_n$ with respect to multiplication such that the determinants of the matrices and $n$ are relatively prime.

> [!theorem]
> The order of the General Linear Group $\text{GL}_2(\mathbb Z_p)$ is given by $$|\text{GL}_2(\mathbb Z_p)| = (p^2 - 1)(q^2 - 1),$$ where $p$ is a prime integer.

> [!lemma]
> Let $n = pq$ where $p$ and $q$ are distinct prime integers. If $M \in \text{GL}_2(\mathbb Z_n)$, then $M \in \text{GL}_2(\mathbb Z_p)$ and $M \in \text{GL}_2(\mathbb Z_q)$. 
 