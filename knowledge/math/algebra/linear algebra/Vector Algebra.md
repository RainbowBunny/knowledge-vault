Reference:
- `[SH16]` — G. Strang, E. Herman et al., _Calculus Volume 3_ (OpenStax, 2016), §2.4 The Cross Product, §2.5 Equations of Lines and Planes in Space; LibreTexts edition: https://math.libretexts.org/Bookshelves/Calculus/Calculus_(OpenStax)/12%3A_Vectors_in_Space/12.04%3A_The_Cross_Product and https://math.libretexts.org/Bookshelves/Calculus/Calculus_(OpenStax)/12:_Vectors_in_Space/12.05:_Equations_of_Lines_and_Planes_in_Space — works in $\mathbb R^3$; `[cf. SH16 …]` marks an $n$-space statement whose three-dimensional case is treated there.
- `[LNS16]` — I. Lankham, B. Nachtergaele, A. Schilling, _Linear Algebra As an Introduction to Abstract Mathematics_ (2016), §9.6 Orthogonal projections, LibreTexts edition: https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_(Schilling_Nachtergaele_and_Lankham)

## Definition

> [!definition] Parameters
> - $V_n$: the real [[Vector Spaces|vector space]] $\mathbb R^n$ with the dot product ([[Inner-Product Spaces]]).
> - $A, B \in V_n$: vectors.
> - $c \in \mathbb R$: a scalar.

> [!definition] Direction of Vector
> Two vectors $A$ and $B$ in $V_n$ are said to have the same direction if $B = cA$ for some positive scalar $c$, and the opposite direction if $B = cA$ for some negative $c$. They are called parallel if $B = cA$ for some nonzero $c$. `[SH16 §2.5]`

> [!definition] Projection of two Vectors
> Let $A$ and $B$ be two vectors, the projection of $A$ along $B$ is $$\text{proj}_B A = \frac{\langle A, B \rangle}{\langle B, B \rangle} B.$$ `[LNS16 Def 9.6.5]` (the orthogonal projection of $A$ onto $\operatorname{span}(B)$)

### Lines in $n$-space

> [!definition] Parameters
> - $P, Q$: points of $V_n$.
> - $A, B$: nonzero vectors of $V_n$.
> - $t \in \mathbb R$.

> [!definition] Lines
> Let $P$ be a given point and $A$ a given nonzero vector. The set of all points of the form $P + tA$, where $t$ runs through all real numbers, is called a line through $P$ parallel to $A$. We denote this line by $L(P; A)$ and write $$L(P; A) = \{P + tA | t \in \mathbb R\}.$$ A point $Q$ is said to be on the line $L(P; A)$ if $Q \in L(P; A)$. `[SH16 §2.5]` (vector equation $r = r_0 + tv$)

> [!theorem] Lines through the same point are equal iff their directions are parallel
> Two lines $L(P; A)$ and $L(P; B)$ through the same point $P$ are equal if and only if the direction vectors $A$ and $B$ are parallel. `[cf. SH16 §2.5]`

> [!theorem] Lines with the same direction are equal iff one point lies on both
> Two lines $L(P; A)$ and $L(Q; A)$ with the same direction vector $A$ are equal if and only if $Q$ is on $L(P; A)$. `[cf. SH16 §2.5]`

> [!definition] Parallel Line
> Two lines $L(P; A)$ and $L(Q; B)$ are called parallel if their direction vectors $A$ and $B$ are parallel. `[SH16 §2.5]`

> [!theorem] Parallel through a point — exactly one line through $Q$ parallel to $L$
> Given a line $L$ and a point $Q$ not on $L$, then there is one and only one line $L'$ containing $Q$ and parallel to $L$. `[cf. SH16 §2.5]`

> [!theorem] Two distinct points determine a line
> Two distinct points determine a line. That is, if $P \neq Q$, there is one and only one line containing both $P$ and $Q$. It can be described as the set $\{P + t(Q - P)\}$. `[cf. SH16 §2.5]`

> [!theorem] Two vectors are dependent iff they lie on one line through the origin
> Two vectors $A$ and $B$ in $V_n$ are linearly dependent if and only if they lie on the same line through the origin. `[cf. SH16 §2.5]`

> [!definition] Parameters
> - $L$: a line in $V_2$.
> - $P$: a point on $L$.
> - $N$: a nonzero vector normal to $L$.

> [!theorem] Distance from the origin to a line — $d = |P \cdot N| / ||N||$, attained at the projection of $P$ along $N$
> Let $L$ be the line in $V_2$ consisting of all points $X$ satisfying $$X \cdot N = P \cdot N,$$ where $P$ is on the line and $N$ is a nonzero vector normal to the line. Let $$d = \frac{|P \cdot N|}{||N||}.$$ Then every $X$ on $L$ has length $||X|| \geq d$. Moreover, $||X|| = d$ if and only if $X$ is the projection of $P$ along $N$:
> - $X = tN$
> - $t = \dfrac{P \cdot N}{N \cdot N}$
>
> `[cf. SH16 §2.5]` (distance from a point to a plane)

### Planes in Euclidean $n$-space

> [!definition] Parameters
> - $P, Q, R$: points of $V_n$.
> - $A, B, C, D$: vectors of $V_n$.
> - $s, t \in \mathbb R$.

> [!definition] Plane
> A set $M$ of points in $V_n$ is called a plane if there is a point $P$ and two linearly independent vectors $A$ and $B$ such that $$M = \{P + sA + tB | s, t \in \mathbb R\}.$$ `[cf. SH16 §2.5]`

> [!theorem] Planes through the same point are equal iff their spans agree
> Two planes $M = \{P + sA + tB\}$ and $M' = \{P + sC + tD\}$ through the same point $P$ are equal if and only if the linear span of $A$ and $B$ is equal to the linear span of $C$ and $D$. `[cf. SH16 §2.5]`

> [!theorem] Planes spanned by the same vectors are equal iff one point lies on both
> Two planes $M = \{P + sA + tB\}$ and $M' = \{Q + sA + tB\}$ spanned by the same vectors $A$ and $B$ are equal if and only if $Q$ is on $M$. `[cf. SH16 §2.5]`

> [!definition] Parallel
> Two planes $M = \{P + sA + tB\}$ and $M' = \{Q + sC + tD\}$ are said to be parallel if the linear span of $A$ and $B$ is equal to the linear span of $C$ and $D$. We also say that a vector $X$ is parallel to the plane $M$ if $X$ is in the linear span of $A$ and $B$. `[cf. SH16 §2.5]`

> [!theorem] Parallel plane through a point — exactly one plane through $Q$ parallel to $M$
> Given a plane $M$ and a point $Q$ not on $M$, there is one and only one plane $M'$ which contains $Q$ and is parallel to $M$. `[cf. SH16 §2.5]`

> [!theorem] Three non-collinear points determine a plane
> If $P, Q$ and $R$ are three points not on the same line, then there is one and only one plane $M$ containing these three points. It can be described as the set $$M = \{P + s(Q - P) + t(R - P)\}.$$ `[SH16 §2.5]`

> [!theorem] Three vectors are dependent iff they lie on one plane through the origin
> Three vectors $A, B, C$ in $V_n$ are linearly dependent if and only if they lie on the same plane through the origin. `[cf. SH16 §2.5]`

> [!proposition] A plane through two points contains the line through them
> Two distinct points $P$ and $Q$ lie on a plane $M$. Then every point on the line through $P$ and $Q$ also lies on $M$. `[cf. SH16 §2.5]`

> [!definition] Parameters
> - $L$: a line.
> - $P$: a point not on $L$.

> [!proposition] A line and a point off it determine a plane
> Given a line $L$ and a point $P$ not on $L$. Then, there is one and only one plane through $P$ which contains every point on $L$. `[cf. SH16 §2.5]`

### Cross Product

> [!definition] Parameters
> - $A = (a_1, a_2, a_3)$: a vector in $V_3$.
> - $B = (b_1, b_2, b_3)$: a vector in $V_3$.
> - $C$: a vector in $V_3$.
> - $c \in \mathbb R$.

> [!definition] Cross Product 3D
> Let $A = (a_1, a_2, a_3)$ and $B = (b_1, b_2, b_3)$ be two vectors in $V_3$. Their cross product $A \times B$ (in that order) is defined to be the vector $$A \times B = (a_2 b_3 - a_3 b_2, a_3 b_1 - a_1 b_3, a_1 b_2 - a_2 b_1).$$ `[SH16 §2.4]`

> [!theorem] Properties of the cross product
> For all vectors $A, B, C$ in $V_3$ and for all real $c$ we have:
> 1. **Skew symmetry**: $A \times B = -(B \times A)$
> 2. **Distributive law**: $A \times (B + C) = (A \times B) + (A \times C)$
> 3. $c(A \times B) = (cA) \times B$
> 4. Orthogonality to $A$: $A \cdot (A \times B) = 0$
> 5. Orthogonality to $B$: $B \cdot (A \times B) = 0$
> 6. Lagrange's identity: $||A \times B||^2 = ||A||^2 ||B||^2 - (A \cdot B)^2$
> 7. $A \times B = O$ if and only if $A$ and $B$ are linearly dependent.
>
> `[SH16 §2.4]` (items 1–5; item 6 appears in the proof of the magnitude formula)

> [!theorem] $A$, $B$, $A \times B$ form a basis, and $A \times B$ spans the common normals
> Let $A$ and $B$ be linearly independent vectors in $V_3$. Then:
> 1. The vectors $A, B, A \times B$ are linearly independent.
> 2. Every vector $N$ in $V_3$ orthogonal to both $A$ and $B$ is a scalar multiple of $A \times B$.
>
> `[cf. SH16 §2.4]`

> [!remark]
> $||A \times B|| = ||A|| \; ||B|| \sin \theta$ `[SH16 §2.4]`

> [!remark]
> $$A \times B = \begin{vmatrix}i & j & k \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3\end{vmatrix}.$$ `[SH16 §2.4]`

## Related

### Siblings
- [[Inner-Product Spaces]] — the dot product, norms and orthogonal projections in general
- [[Trace, Determinant, and Volume]] — the $3 \times 3$ determinant behind the cross-product formula

### Prerequisites
- [[Vector Spaces]] — span and linear independence
- [[Real Number]] — the scalars of $V_n$
