## Linear Maps

> [!definition] Linear Map
> A **linear map** from $V$ to $W$ is a function $T: V \rightarrow W$ with the following properties:
> - Additivity: $T(u + v) = T(u) + T(v)$ for all $u, v \in V$;
> - Homogeneity: $$T(av) = a T(v)$$ for all $a \in F$ and all $v \in V$.

> [!remark]
> The set of all linear maps from $V$ to $W$ is denoted $\mathcal L(V, W)$.

> [!definition] Product of Linear Maps
> For linear map $S$ and $T$ in $\mathcal L(V, W)$, then the **product** of these maps by $$(ST)(v) = S(T(v))$$

> [!proposition] Properties of Product
> - **Associativity Law**
> - **Identity Law**
> - **Distributive Law**

### Null Spaces and Ranges

> [!definition] Null Space
> For $T \in \mathcal L(V, W)$, the **null space (or kernel)** of $T$, denoted by $\text{null } T$, is the subset of $V$ consisting of those vectors that $T$ maps to $0$: $$\text{null } T = \{v \in V: T(v) = 0\}.$$ 
> We have $\text{null } T$ is a subspace of $V$.

> [!proposition]
> Let $T \in \mathcal L(V, W)$. Then $T$ is injective if and only if $\text{null } T= \{0\}$

> [!definition] Range
> For $T \in \mathcal(V, W)$, the **range** of $T$, denoted $\text{range } T$, is the subset of $W$ consisting of those vectors that are of form $T(v)$ for some $v \in V$: $$\text{range } T = \{T(v) : v \in V\}.$$ we have $\text{range } T$ is a subspace of $W$.

> [!theorem]
> If $V$ is finite dimensional and $T \in \mathcal L(V, W)$, then $\text{range } T$ is a finite-dimensional subspace of $W$ and $$\dim V = \dim \text{null } T + \dim \text{range } T.$$

> [!corollary]
> If $V$ and $W$ are finite-dimensional vector spaces such that $\dim V > \dim W$, then no linear map from $V$ to $W$ is injective.
> If $V$ and $W$ are finite-dimensional vector spaces such that $\dim V < \dim W$, then no linear map from $V$ to $W$ is surjective.

> [!definition] Operator
> A linear map from a vector space to itself is called an **operator**.

### Invertibility

> [!definition] Invertible, Inverse
> A linear map $T \in \mathcal L(V, W)$ is called **invertible** if there exists a linear map $S \in \mathcal L(W, V)$ such that $ST$ equals the identity map on $V$ and $TS$ equals the identity map on $W$. A linear map $S \in \mathcal L(W, V)$ satisfying $ST = I$ and $TS = I$ is called an **inverse** of $T$.

> [!proposition]
> A linear map is invertible if and only if it is injective and surjective.

> [!definition] Isomorphic
> Two vector spaces are called **isomorphic** if there is an invertible linear map from one vector space onto the other one.

> [!theorem]
> Two finite-dimensional vector spaces are isomorphic if and only if they have the same dimension.

> [!proposition]
> Suppose that $(v_1, \dots, v_n)$ is a basis of $V$ and $(w_1, \dots, w_m)$ is a basis of $W$. Then $\mathcal M$ is an invertible linear map between $\mathcal L(V, W)$ and $\text{Mat}(m, n, F)$.

> [!proposition]
> If $V$ and $W$ are finite dimensional, then $\mathcal L(V, W)$ is finite dimensional and $$\dim \mathcal L(V, W) = (\dim V)(\dim W)$$

> [!theorem]
> Suppose $V$ is finite dimensional. If $T \in \mathcal L(V)$, then the following are equivalent:
> 1. $T$ is invertible;
> 2. $T$ is injective;
> 3. $T$ is surjective.

> [!proposition]
> Suppose that $V$ is finite-dimensional. If $U$ is a subspace of $V$ and $S \in \mathcal L(U, W)$, then there exists $T \in \mathcal L(V, W)$ such that $T(u) = S(u)$ for all $u \in U$.

> [!proposition]
> If $S_1, \dots, S_n$ are injective linear maps such that $S_1 \dots S_n$ makes sense, 
then $S_1 \dots S_n$ is injective.

> [!proposition]
> Suppose that $V$ is finite dimensional and $S, T \in \mathcal L(v)$, then $ST = I$ if and only if $TS = I$.

> [!proposition]
> Suppose $n$ is a positive integer and $a_{i, j} \in F$ for $i, j = 1, \dots, n$. Then, the following are equivalent:
> 1. The trivial solution $x_1 = \cdots = x_n = 0$ is the only solution to the homogeneous system of equations $$\begin{align}\sum_{k = 1}^n a_{1, k}x_k = 0 \\ \vdots \\ \sum_{k = 1}^n a_{n, k} x_k = 0 \end{align}$$
> 2. For every $c_1, \dots, c_n \in F$, there exists a solution to the system of equations $$\begin{align}\sum_{k = 1}^n a_{1, k}x_k = c_1 \\ \vdots \\ \sum_{k = 1}^n a_{n, k} x_k = c_n \end{align}$$

### One-sided Inverse

> [!definition] Left Inverse, Right Inverse
> Suppose $V$ and $W$ are vector spaces over a field $\mathbb F$, and $T \in \mathcal L(V, W)$. A **left inverse** for $T$ is a linear map $S \in \mathcal L(W, V)$ with the property that $ST = I_V$ (the identity map on $V$). That is, we have $$ST(v) = v \quad \forall v \in V.$$
> A **right inverse** for $T$ is a linear map $S' \in \mathcal L(W, V)$ with the property that $TS' = I_W$ (the identity map on $W$). That is, we require $$TS'(w) = w \quad \forall w \in W.$$

> [!proposition]
> Suppose $S$ is a left inverse of $T$. Then the only possible solution of $T(x) = c$ is $x = S(c)$.

> [!proposition]
> Suppose $S'$ is a right inverse of $T$. Then $x = S'(c)$ is a solution of $T(x) = c$.

> [!theorem]
> Suppose $V$ and $W$ are finite-dimensional, and that $T \in \mathcal L(V, W)$.
> 1. The operator $T$ has a left inverse if and only if $\text{Null}(T) = 0$.
> 2. If $S$ is a left inverse of $T$, then $\text{Null}(S)$ is a complement to $\text{Range}(T)$: $$W = \text{Range}(T) \oplus \text{Null}(S).$$
> 3. Assuming that $\text{Null}(T) = 0$, there is a one-to-correspondence between left inverses of $T$ and subspaces of $W$ complementary to $\text{Range}(T)$.
> 4. The operator $T$ has a right inverse if and only if $\text{Range}(T) = W$.
> 5. If $S'$ is a right inverse of $T$, then $\text{Range}(S')$ is a complement to $\text{Null}(T)$: $$V = \text{Null}(T) \oplus \text{Range}(S').$$
> 6. Assuming that $\text{Range}(T) = W$, there is a one-to-correspondence between right inverses of $T$ and subspaces of $V$ complementary to $\text{Null}(T)$.
> 7. If $T$ has both a left and a right inverse, then the left and right inverses are unique and equal to each other. That, is there is a unique linear map $S \in \mathcal L(W, V)$ characterized by either of the two properties $ST = I_V$ or $TS = I_V$. If it has one of these properties, then it automatically has the other.

### Projection

> [!definition] Projection between Subspaces
> Suppose $U$ and $W$ are subspaces of $V$ with $$V = U \oplus W.$$ Each vector $v \in V$ can be written uniquely in the form $$v = u + w,$$ where $u \in U$ and $w \in W$. With this representation, define $P_{U, W} \in \mathcal L(V)$ by $$P_{U, W}(v) = u.$$ And $P_{U, W}$ is often called the **projection** onto $U$ with null space $W$.

> [!definition] Projection of Operator
> Suppose $V$ is a vector space. A **projection** on $V$ is a linear map $P \in \mathcal L(V)$ with the property $P^2 = P$.

> [!proposition]
> Suppose $V$ is a vector space. The following things are in one-to-one correspondence:
> 1. Projections $P \in \mathcal L(V)$;
> 2. Pairs of linear transformations $P$ and $Q$ in $\mathcal L(V)$ such that $$P + Q = I, \quad PQ = 0;$$
> 3. Direct sum decompositions $V = U \oplus W$.

> [!example]
> Suppose $P \in \mathcal L(V)$ and $P^2 = P$. Then, $V = \text{null } P \oplus \text{range } P$.
> ($v = (v - P(v)) + P(v)$; $P(v - P(v)) = 0$)

> [!example]
> If $P \in \mathcal L(V)$ is such that $P^2 = P$ and every vector in $\text{null } P$ is orthogonal to every vector in $\text{range } P$, then $P$ is an orthogonal projection.
> $(V = \text{null } P \oplus \text{range } P)$

> [!example]
> If $P \in \mathcal L(V)$ is such that $P^2 = P$ and $$||P(v)|| \leq ||v||$$ for every $v \in V$, then $P$ is an orthogonal projection.
> (Let $u \in \text{range } P$ and $w \in \text{null } P$, we have $P(u + tw) = u$, thus $||u|| \leq ||u + tw|| \; \forall \; t \in \mathbb R$)

> [!example]
> Suppose $P \in \mathcal L(V)$ is such that $P^2 = P$. $P$ is an orthogonal projection if and only if $P$ is self-adjoint.


