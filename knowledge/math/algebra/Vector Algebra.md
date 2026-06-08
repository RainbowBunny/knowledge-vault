
> [!definition] Direction of Vector
> Two vectors $A$ and $B$ in $V_n$ are said to have the same direction if $B = cA$ for some positive scalar $c$, and the opposite direction if $B = cA$ for some negative $c$. They are called parallel if $B = cA$ for some nonzero $c$.

> [!definition] Projection of two Vectors
> Let $A$ and $B$ be two vectors, the projection of $A$ along $B$ is $$\text{proj}_B A = \frac{\langle A, B \rangle}{\langle B, B \rangle} B.$$ 

## Lines in $n$-space

> [!definition] Lines
> Let $P$ be a given point and $A$ a given nonzero vector. The set of all points of the form $P + tA$, where $t$ runs through all real numbers, is called a line through $P$ parallel to $A$. We denote this line by $L(P; A)$ and write $$L(P; A) = \{P + tA | t \in \mathbb R\}.$$ A point $Q$ is said to be on the line $L(P; A)$ if $Q \in L(P; A)$.

> [!theorem]
> Two lines $L(P; A)$ and $L(P; B)$ through the same point $P$ are equal if and only if the direction vectors $A$ and $B$ are parallel.

> [!theorem]
> Two lines $L(P; A)$ and $L(Q; A)$ with the same direction vector $A$ are equal if and only if $Q$ is on $L(P; A)$.

> [!definition] Parallel Line
> Two lines $L(P; A)$ and $L(Q; B)$ are called parallel if their direction vectors $A$ and $B$ are parallel.

> [!theorem]
> Given a line $L$ and a point $Q$ not on $L$, then there is one and only one line $L'$ containing $Q$ and parallel to $L$.

> [!theorem]
> Two distinct points determine a line. That is, if $P \neq Q$, there is one and only one line containing both $P$ and $Q$. It can be described as the set $\{P + t(Q - P)\}$.

> [!theorem]
> Two vectors $A$ and $B$ in $V_n$ are linearly dependent if and only if they lie on the same line through the origin.

> [!theorem]
> Let $L$ be the line in $V_2$ consisting of all points $X$ satisfying $$X \cdot N = P \cdot N,$$ where $P$ is on the line and $N$ is a nonzero vector normal to the line. Let $$d = \frac{|P \cdot N|}{||N||}.$$ Then every $X$ on $L$ has length $||X|| \geq d$. Moreover, $||X|| = d$ if and only if $X$ is the projection of $P$ along $N$: $$X = tN, \quad \text{where } t = \frac{P \cdot N}{N \cdot N}.$$

## Planes in Euclidean $n$-space

> [!definition] Plane
> A set $M$ of points in $V_n$ is called a plane if there is a point $P$ and two linearly independent vectors $A$ and $B$ such that $$M = \{P + sA + tB | s, t \in \mathbb R\}.$$

> [!theorem]
> Two planes $M = \{P + sA + tB\}$ and $M' = \{P + sC + tD\}$ through the same point $P$ are equal if and only if the linear span of $A$ and $B$ is equal to the linear span of $C$ and $D$.

> [!theorem]
> Two planes $M = \{P + sA + tB\}$ and $M' = \{Q + sA + tB\}$ spanned by the same vectors $A$ and $B$ are equal if and only if $Q$ is on $M$.

> [!definition] Parallel
> Two planes $M = \{P + sA + tB\}$ and $M' = \{Q + sA + tB\}$ are said to be parallel if the linear span of $A$ and $B$ is equal to the linear span of $C$ and $D$. We also say that a vector $X$ is parallel to the plane $M$ if $X$ is in the linear span of $A$ and $B$.

> [!theorem]
> Given a plane $M$ and a point $Q$ not on $M$, there is one and only one plane $M'$ which contains $Q$ and is parallel to $M$.

> [!theorem]
> If $P, Q$ and $R$ are three points not on the same line, then there is one and only one plane $M$ containing these three points. It can be described as the set $$M = \{P + s(Q - P) + t(R - P)\}.$$

> [!theorem]
> Three vectors $A, B, C$ in $V_n$ are linearly dependent if and only if they lie on the same plane through the origin.

> [!proposition]
> Two distinct points $P$ and $Q$ lie on a plane $M$. Then every point on the line through $P$ and $Q$ also lines on $M$.

> [!proposition]
> Given a line $L$ and a point $P$ not on $L$. Then, there is one and only one plane through $P$ which contains every point on $L$.

## Cross Product

> [!definition] Cross Product 3D
> Let $A = (a_1, a_2, a_3)$ and $B = (b_1, b_2, b_3)$ be two vectors in $V_3$. Their cross product $A \times B$ (in that order) is defined to be the vector $$A \times B = (a_2 b_3 - a_3 b_2, a_3 b_1 - a_1 b_3, a_1 b_2 - a_2 b_1).$$

> [!theorem]
> For all vectors $A, B, C$ in $V_3$ and for all real $c$ we have:
> 1. **Skew symmetry**: $A \times B = -(B \times A)$
> 2. **Distributive law**: $A \times (B + C) = (A \times B) + (A \times C)$
> 3. $c(A \times B) = (cA) \times B$
> 4. Orthogonality to $A$: $A \cdot (A \times B) = 0$
> 5. Orthogonality to $B$: $B \cdot (A \times B) = 0$
> 6. Lagrange's identity: $||A \times B||^2 = ||A||^2 ||B||^2 - (A \cdot B)^2$
> 7. $A \times B = O$ if and only if $A$ and $B$ are linearly dependent.

> [!theorem]
> Let $A$ and $B$ be linearly independent vectors in $V_3$. Then:
> 1. The vectors $A, B, A \times B$ are linearly independent.
> 2. Every vector $N$ in $V_3$ orthogonal to both $A$ and $B$ is a scalar multiple of $A \times B$.

> [!remark]
> $||A \times B|| = ||A|| \; ||B|| \sin \theta$

> [!remark]
> $$A \times B = \begin{vmatrix}i & j & k \\ a_1 & a_2 & a_3 \\ b_1 & b_2 & b_3\end{vmatrix}.$$
