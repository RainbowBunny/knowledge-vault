## Vector Spaces

> [!definition] Vector Spaces
> A **vector space** is a set $V$ along with an addition on $V$ and a scalar multiplication on $V$ such that the following properties hold:
> - **Commutativity Law** for addition: $u + v = u + v \; \forall \; u, v \in V$;
> - **Associativity Law** for addition and scalar multiplication: $(u + v) + w = u + (v + w)$ and $(ab)v = a (bv)$ for all $u, v, w \in V$ and $a, b \in \mathbb F$;
> - **Identity Law** for addition and scalar multiplication: Exist $0 \in V$ such that $v + 0 = v \; \forall \; v \in V$, exist $1 \in \mathbb F: 1v = v \; \forall \; v \in V$;
> - **Inverse Law** for addition: $\forall v \in V, \exists w \in V: v + w = 0$;
> - **Distributive Law**: $a(u + v) = au + av$ and $(a + b)u = au + bu$ for all $a, b \in \mathbb F$ and all $u, v \in V$.

### Subspace

> [!definition] Subspaces
> A subset $U$ of $V$ is called a **subspace** of $V$ if $U$ is also a vector space (using the same addition and scalar multiplication as on $V$).

> [!proposition]
> If $U$ is a subset of $V$, then to check that $U$ is a subspace of $V$ we need only check that $U$ satisfies the following:
> - **Additive identity**: $0 \in U$
> - **Closed under addition**: $u, v \in U$ implies $u + v \in U$; 
> - **Closed under scalar multiplication**: $a \in F$ and $u \in U$ implies $au \in U$.

> [!proposition]
> The intersection of any collection of subspaces of $V$ is a subspace of $V$.
> The union of two subspaces of $V$ is a subspace if and only if one of the subspaces is contained in the other.

### Sum and Direct Sums

> [!definition] Sum of Subspaces
> Suppose $U_1, \dots, U_m$ are subspaces of $V$. The **sum** of $U_1, \dots, U_m$, denoted $U_1 + \cdots + U_m$, is defined to be the set of all possible sums of elements of $U_1, \dots, U_m$. More precisely, $$U_1 + \cdots + U_m = \{u_1 + \cdots + u_m : u_1 \in U_1, \dots, u_m \in U_m\}.$$

> [!definition] Direct Sum of Subspaces
> We say that $V$ is the **direct sum** of subspaces $U_1, \dots, U_m$, written $V = U_1 \oplus \cdots \oplus U_m$, if each element of $V$ can be written uniquely as a sum $u_1 + \cdots + u_m$, where each $u_j \in U_j.$

> [!proposition]
> Suppose that $U_1, \dots, U_n$ are subspaces of $V$. Then $V = U_1 \oplus \cdots \oplus U_n$ if and only if both the following conditions hold:
> 1. $V = U_1 + \cdots + U_n$;
> 2. The only way to write $0$ as a sum $u_1 + \cdots + u_n$, where each $u_j \in U_j$, is by taking all the $u_j$'s equal to $0$.

> [!proposition]
> Suppose that $U$ and $W$ are subspaces of $V$. Then $V = U \oplus W$ if and only if $V = U + W$ and $U \cap W = \{0\}$.

## Finite-Dimensional Vector Spaces

### Span and Linear Independence

> [!definition] Linear Combinations
> Let $\textbf{v}_1, \textbf{v}_2, \cdots, \textbf{v}_k \in V$. A **linear combination** of $\textbf{v}_1, \textbf{v}_2, \cdots, \textbf{v}_k \in V$ is any vector of the form $$\textbf{w} = \alpha_1 \textbf{v}_1 + \alpha_2 \textbf{v}_2 + \cdots + \alpha_k \textbf{v}_k \quad \text{with } \alpha_1, \cdots, \alpha_k \in \mathbb R.$$
> The collection of all such linear combinations, $$\{\alpha_1 \textbf{v}_1 + \cdots + \alpha_k \textbf{v}_k : \alpha_1, \dots, \alpha_k \in \mathbb R\},$$ is called the **span** of $\{\textbf{v}_1, \dots, \textbf{v}_k\}.$

> [!definition] Dimensional
> A vector space is called **finite dimensional** if some list of vectors in it spans the space.
> A vector space that is not finite dimensional is called **infinite dimensional**.

> [!definition] Independence
> A set of vectors $\textbf{v}_1, \textbf{v}_2, \cdots, \textbf{v}_k \in V$ is **(linearly) independent** if the only way to get $$\alpha_1 \textbf{v}_1 + \alpha_2 \textbf{v}_2 + \cdots + \alpha_k \textbf{v}_k = 0$$ is to have $\alpha_1 = \alpha_2 = \cdots = \alpha_k = 0$. The set is **(linearly) dependent** if there is a combination with at least one $\alpha \neq 0$.

> [!lemma] Linear Dependence Lemma
> If $(v_1, \dots, v_m)$ is linearly dependent in $V$ and $v_1 \neq 0$, then there exists $j \in \{2, \dots, m\}$ such that the following hold:
> 1. $v_j \in \text{span}(v_1, \dots, v_{j - 1});$
> 2. If the $j^{\text{th}}$ term is removed from $(v_1, \dots, v_m)$, the span of the remaining list equals $\text{span}(v_1, \dots, v_m)$.

> [!theorem]
> In a finite-dimensional vector space, the length of every linearly independent list of vectors is less than or equal to the length of every spanning list of vectors.

> [!proposition]
> Every subspace of a finite-dimensional vector space is finite dimensional.

> [!theorem]
> A set $S$ spans every vector in $L(s)$ uniquely if and only if $S$ spans the zero vector uniquely.

> [!theorem]
> Let $S = \{A_1, \dots, A_k\}$ be a linearly independent set of $k$ vectors in $V_n$, and let $L(S)$ be the linear span of $S$. Then, every set of $k + 1$ vectors in $L(S)$ is linearly dependent.

### Bases

> [!definition] Bases
> A **basis** for $V$ is a set of linearly independent vectors $\textbf{v}_1, \dots, \textbf{v}_n$ that span $V$. This is equivalent to saying that every vector $\textbf{w} \in V$ can be written in the form $$\textbf{w} = \alpha_1 \textbf{v}_1 + \alpha_2 \textbf{v}_2 + \cdots + \alpha_n \textbf{v}_n$$ for a **unique** choice of $\alpha_1, \dots, \alpha_n \in \mathbb R$.

> [!theorem]
> Every spanning list in a vector space can be reduced to a basis of the vector space.

> [!corollary]
> Every finite-dimensional vector space has a basis.

> [!theorem]
> Every linearly independent list of vectors in a finite-dimensional vector space can be extended to a basis of the vector space.

> [!proposition]
> Suppose $V$ is finite dimensional and $U$ is a subspace of $V$. Then there is a subspace $W$ of $V$ such that $V = U \oplus W$.

> [!proposition] 
> Let $V \subset \mathbb R^m$ be a vector space.
> 1. There exists a basis for $V$.
> 2. Any two bases for $V$ have the same number of elements. The number of elements in a basis for $V$ is called the dimension of $V$.
> 3. Let $\textbf{v}_1, \dots, \textbf{v}_n$ be a basis for $V$ and let $\textbf{w}_1, \dots, \textbf{w}_n$ be another set of $n$ vectors in $V$. Write each $\textbf{w}_j$ as a linear combination of the $\textbf{v}_i$, $$
\begin{aligned}
\mathbf{w}_1 &= \alpha_{11} \textbf{v}_1 + \alpha_{12} \textbf{v}_2 + \cdots + \alpha_{1n} \textbf{v}_n, \\
\mathbf{w}_2 &= \alpha_{21} \textbf{v}_1 + \alpha_{22} \textbf{v}_2 + \cdots + \alpha_{2n} \textbf{v}_n, \\
&\ \vdots \\
\mathbf{w}_n &= \alpha_{n1} \textbf{v}_1 + \alpha_{n2} \textbf{v}_2 + \cdots + \alpha_{nn} \textbf{v}_n. \\
\end{aligned}
$$ Then $\textbf{w}_1, \dots, \textbf{w}_n$ is also a basis for $V$ if and only if the determinant of the matrix $$\begin{pmatrix}
> \alpha_{11} & \alpha_{12} & \cdots & \alpha_{1n} \\
> \alpha_{21} & \alpha_{22} & \cdots & \alpha_{2n} \\
> \vdots & \vdots & \ddots & \vdots \\
> \alpha_{n1} & \alpha_{n2} & \cdots & \alpha_{nn}
> \end{pmatrix}$$ is not equal to $0$.

> [!theorem]
> In a given vector space $V_n$, bases have the following properties:
> 1. Every basis contains exactly $n$ vectors.
> 2. Any set of linearly independent vectors is a subset of some basis.
> 3. Any set of $n$ linearly independent vectors is a basis.

### Dimension

> [!theorem]
> Any two bases of a finite-dimensional vector space have the same length.

> [!definition] Dimension
> The **dimension** of a finite-dimensional vector space is defined to be the length of any basis of the vector space.

> [!proposition]
> If $V$ is finite dimensional and $U$ is a subspace of $V$, then $\dim U \leq \dim V$.
> If $V$ is finite dimensional, then every spanning list of vectors in $V$ with length $\dim V$ is a basis of $V$.
> If $V$ is finite dimensional, then every linearly independent list of vectors in $V$ with length $\dim V$ is a basis of $V$.

> [!theorem]
> If $U_1$ and $U_2$ are subspaces of a finite-dimensional vector space, then $$\dim(U_1 + U_2) = \dim U_1 + \dim U_2 - \dim(U_1 \cap U_2)$$

> [!proposition]
> Suppose $V$ is finite dimensional and $U_1, \dots, U_m$ are subspaces of $V$ such that $$V = U_1 + \cdots + U_m$$ and $$\dim V = \dim U_1 + \cdots + \dim U_m.$$ Then $V = U_1 \oplus \cdots \oplus U_m$.

> [!proposition]
> If $V$ is finite dimensional and $U_1, \dots, U_m$ are subspaces of $V$, then $$\dim(U_1 + \cdots + U_m) \leq \dim U_1 + \cdots + \dim U_m.$$

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


## Eigenvalues and Eigenvectors

> [!proposition]
> Suppose $T \in \mathcal L(V)$. Let $\lambda_1, \dots, \lambda_m$ denote the distinct eigenvalues of $T$. Then the following are equivalent:
> 1. $T$ has a diagonal matrix with respect to some basis of $V$;
> 2. $V$ has a basis consisting of eigenvectors of $T$;
> 3. There exist one-dimensional subspaces $U_1, \dots, U_n$ of $V$, each invariant under $T$, such that $$V = U_1 \oplus \cdots \oplus U_n;$$
> 4. $V = \text{null}(T - \lambda_1 I) \oplus \cdots \oplus \text{null}(T - \lambda_m I);$
> 5. $\dim V = \dim \text{null}(T - \lambda_1 I) + \cdots + \dim \text{null} (T - \lambda_m I).$
> 6. Every generalized eigenvector of $T$ is an eigenvector of $T$.
> 7. The minimal polynomial of $T$ has no repeated roots.

### Invariant Subspaces

> [!definition] Invariant Subspaces
> For $T \in \mathcal L(V)$ and $U$ is a subspace of $V$, we say that $U$ is **invariant** under $T$ if $u \in U$ implies $T(u) \in U$ and denote this operator by $T|_U$.

> [!definition] Eigenvalue
> A scalar $\lambda \in \mathbb F$ is called an **eigenvalue** of $T \in \mathcal L(V)$ if there exists a nonzero vector $u \in V$ such that $T(u) = \lambda u$.

> [!definition] Eigenvector
> Suppose $T \in \mathcal L(V)$ and $\lambda \in \mathbb F$ is an eigenvalue of $T$. A vector $u \in V$ is called an **eigenvector** of $T$ (corresponding to $\lambda$) if $T(u) = \lambda u$.

> [!remark]
> The set of eigenvector of $T \in \mathcal L(V)$ corresponding to $\lambda$ equals $\text{null } (T - \lambda I)$. 

> [!theorem]
> Let $T \in \mathcal L(V)$. Suppose $\lambda_1, \dots, \lambda_m$ are distinct eigenvalues of $T$ and $v_1, \dots, v_m$ are corresponding nonzero eigenvectors. Then $(v_1, \dots, v_m)$ is linearly independent.

> [!corollary]
> Each operator on $V$ has at most $\dim V$ distinct eigenvalues.

> [!proposition]
> Suppose $\mathbb F = \mathbb C, T \in \mathcal L(V), p \in \mathcal P(\mathbb C),$ and $a \in \mathcal C$. Then, $a$ is an eigenvalue of $\mathcal p(T)$ if and only if $a = \mathcal p(\lambda)$ for some eigenvalue $\lambda$ of $T$.
> The result does not hold if $\mathbb F = \mathbb R$.

### Polynomials Applied to Operators




### Invariant Subspaces on Real Vector Space

> [!theorem]
> Every operator on a finite-dimensional, nonzero, real vector space has an invariant subspace of dimension $1$ or $2$.

> [!remark]
> There exist real numbers $a_0, \dots, a_n$, not all $0$, such that $$0 = a_0 v + a_1 T(v) + \cdots + a_n T^n(v).$$ Thus we have $$0 = c(T - \lambda_1 I) \dots (T - \lambda_m I) (T^2 + \alpha_1 T + \beta_1 I) \dots (T^2 + \alpha_m T + \beta_m I) (v).$$

> [!theorem]
> Every operator on an odd-dimensional real vector space has an eigenvalue.

> [!proposition]
> Suppose $S, T \in \mathcal L(V)$. Then, $ST$ and $TS$ have the same eigenvalues.

## Inner-Product Spaces

### Inner Product

> [!definition] Dot Product
> Let $\textbf{v}, \textbf{w} \in V \subset \mathbb R^{m}$ and write $\textbf{v}$ and $\text{w}$ using coordinates as $$\textbf{v} = (x_1, x_2, \dots, x_m) \quad \text{and} \quad w = (y_1, y_2, \dots, y_m).$$
> The **dot product** of $\textbf{v}$ and $\textbf{w}$ is the quantity $$\textbf{v} \cdot \textbf{w} = x_1 y_1 + x_2 y_2 + \dots + x_m y_m.$$

> [!definition] Inner Product
> An **inner product** on $V$ is a function that takes each ordered pair $(u, v)$ of elements of $V$ to a number $\langle u, v \rangle \in \mathbb F$ and has the following properties:
> - **Positivity**: $\langle v, v \rangle \geq 0 \; \forall \; v \in V;$
> - **Definiteness**: $\langle v, v \rangle = 0 \Leftrightarrow v = 0;$
> - **Additivity in first slot**: $\langle u + v, w \rangle = \langle u, w \rangle + \langle v, w \rangle \; \forall \; u, v, w \in V;$
> - **Homogeneity in first slot**: $\langle av, w \rangle = a \langle v, w \rangle \; \forall \; a \in \mathbb F \; \forall \; v, w \in V;$
> - **Conjugate symmetry**: $\langle v, w \rangle = \overline {\langle w, v \rangle} \; \forall \; v, w \in V$.

> [!definition] Inner Product Space
> An **inner product space** is a vector space $V$ along with an inner product on $V$.

> [!example] Euclidean Inner Product
> The **Euclidean inner product** on $\mathbb F^n$ is defined by $$\langle (w_1, \dots, w_n), (z_1, \dots, z_n) \rangle = w_1 \overline{z_1} + \cdots + w_n \overline{z_n}.$$

### Norms

> [!definition] Norm
> For $v \in V$, we define the **norm** of $v$, denoted by $||v||$, by $$||v|| = \sqrt{\langle v, v \rangle}.$$

> [!proposition]
> A norm on a vector space $U$ is a function $||\;||: U \rightarrow [0, \infty)$  such that:
> 1. $||u|| = 0$ if and only if $u = 0$
> 2. $||\alpha u|| = |\alpha| \; ||u||$ for all $\alpha \in \mathbb F$ and all $u \in U$
> 3. $||u + v|| \leq ||u|| + ||v||$ for all $u, v \in U$.
> 
> Then, a norm satisfying the parallelogram equality comes from an inner product (there is an inner product $\langle , \rangle$ on $U$ such that $||u|| = \langle u, u \rangle^{1/2}$ for all $u \in U$).

> [!example] Euclidean Norm
>  The **length**, or **Euclidean norm**, of $\textbf{v}$ is the quantity $$||(x_1, \dots, x_n)|| = \sqrt{x_1^2 + x_2^2 + \cdots + x_m^2}.$$

> [!definition] Orthogonal
> Two vectors $u, v \in V$ are said to be **orthogonal** if $\langle u, v \rangle = 0$.

> [!theorem] Pythagorean Theorem
> If $u, v$ are orthogonal vectors in $V$, then $$||u + v||^2 = ||u||^2 + ||v||^2.$$

> [!proposition]
> Let $v, w \in V \subset \mathbb R^m.$
> 1. Let $\theta$ be the angle between the vectors $v$ and $w$, where we place the starting points of $v$ and $w$ at the origin $0$. Then $$v \cdot w = ||v|| \; ||w|| \cos(\theta),$$
> 2. (**Cauchy-Schwars Inequality**) $$|v \cdot w| \leq ||v|| \; ||w||.$$
> 3. (**Triangle Inequality**) $$||u + v|| \leq ||u|| + ||v||.$$
> 4. (**Parallelogram Equality**) $$||u + v||^2 + ||u - v||^2 = 2(||u||^2 + ||v||^2).$$

### Orthogonal Bases

> [!definition] Orthonormal
> A list of vectors is called **orthonormal** if the vectors in it are pairwise orthogonal and each vector has norm 1.

> [!proposition]
> If $(e_1, \dots, e_m)$ is an orthonormal list of vectors in $V$, then $$||a_1 e_1 + \cdots + a_m e_m||^2 = |a_1|^2 + \cdots + |a_m|^2$$ for all $a_1, \dots, a_m \in \mathbb F$.

> [!corollary]
> Every orthogonal list of vectors is linearly independent.

> [!definition] Orthogonal Basis
> An **orthogonal basis** for a vector space $V$ is a basis $v_1, \dots, v_n$ with the property that $$v_i \cdot v_j = 0 \quad \forall i \neq j.$$ The basis is **orthonormal** if in addition, $||v_i|| = 1 \; \forall i$.

> [!theorem]
> Suppose $(e_1, \dots, e_n)$ is an orthonormal basis of $V$. Then $$v = \langle v, e_1 \rangle e_1 + \cdots + \langle v, e_n \rangle e_n$$ and $$||v||^2 = |\langle v, e_1 \rangle|^2 + \cdots + |\langle v, e_n \rangle|^2$$ for every $v \in V$.

> [!theorem]
> Suppose $(f_1, \dots, f_m)$ is an orthogonal basis of $V$. Then $$v = \sum_{i = 1}^m \frac{\langle v, f_i \rangle}{\langle f_i, f_i \rangle} f_i$$ and $$||v||^2 = \sum_{i = 1}^m \frac{\langle v, f_i \rangle}{\langle f_i, f_i \rangle}$$ for every $v \in V$.

> [!proposition]
> Suppose $n$ is a positive integer then $$(\frac{1}{\sqrt{2\pi}}, \frac{\sin x}{\sqrt{\pi}}, \frac{\sin 2x}{\sqrt{\pi}}, \dots, \frac{\sin nx}{\sqrt{\pi}}, \frac{\cos x}{\sqrt{\pi}}, \frac{\cos 2x}{\sqrt{\pi}}, \dots, \frac{\cos nx}{\sqrt{\pi}})$$ is an orthonormal list of vectors in $C[-\pi, \pi]$, the vector space of continuous real-valued functions on $[-\pi, \pi]$ with inner product $$\langle f, g \rangle = \int_{-\pi}^{\pi} f(x) g(x) dx.$$

> [!proposition]
> Suppose $(e_1, \dots, e_m)$ is an orthonormal list of vectors in $V$. Let $v \in V$, then $$||v||^2 = \sum_{i = 1}^m |\langle v, e_i \rangle|^2$$ if and only if $v \in \text{span}(e_1, \dots, e_m)$.

### Gram-Schmidt Algorithm

> [!algorithm] Gram–Schmidt Orthogonalization Algorithm
> **Input:**  
> A basis $(v_1, v_2, \ldots, v_n)$ of a vector space $V \subset \mathbb{R}^m$
>
> **Output:**  
> An orthogonal basis $(v_1^{*}, v_2^{*}, \ldots, v_n^{*})$ of $V$
>
> ---
>
> 1. Set:
>    $$v_1^{*} \gets v_1.$$
>
> 2. For $i = 2, 3, \ldots, n$, do:
>
>    2.1. For each $j = 1, 2, \ldots, i-1$, compute:
>    $$\mu_{ij} \gets \frac{\langle v_i, v_j^{*} \rangle}{\langle v_j^{*}, v_j^{*} \rangle}.$$
>
>    2.2. Set:
>    $$v_i^{*} \gets v_i - \sum_{j=1}^{i-1} \mu_{ij} v_j^{*}.$$
>
> 3. Return the orthogonal basis $(v_1^{*}, v_2^{*}, \ldots, v_n^{*})$.

> [!proposition]
> Let $\mathcal B = \{v_1, v_2, \dots, v_n\}$ be a basis for a lattice $L$ and $\mathcal B = \{v_1^*, v_2^*, \dots, v_n^*\}$ be the associated Gram-Schmidt orthogonal basis. Then $$\det(L) = \prod_{i = 1}^n ||v_i^*||$$

> [!corollary]
> Every finite-dimensional inner-product space has an orthonormal basis.

> [!corollary]
> Every orthonormal list of vectors in $V$ can be extended to an orthonormal basis of $V$.

> [!corollary]
> Suppose $T \in \mathcal L(V)$. If $T$ has an upper-triangular matrix with respect to some basis of $V$, then $T$ has an upper-triangular matrix with respect to some orthonormal basis of $V$.

> [!theorem] Schur's Theorem
> Suppose $V$ is a complex vector space and $T \in \mathcal L(V)$. Then $T$ has an upper-triangular matrix with respect to some orthonormal basis of $V$.

### Orthogonal Projections and Minimization Problems

> [!definition] Orthogonal Complement
> Let $V$ be a vector space and let $W \subset V$ be a vector subspace of $V$. The **orthogonal complement** of $W$ (in $V$) is $$W^{\perp} = \{v \in V: \langle v, w \rangle = 0 \; \forall \; w \in W\}.$$

> [!theorem]
> If $U$ is a subspace of $V$, then $$V = U \oplus U^{\perp}.$$

> [!corollary]
> If $U$ is subspace of $V$, then $$U = (U^{\perp})^{\perp}$$

> [!definition] Orthogonal Projection
> Suppose $U$ is a subspace of $V$, because of the decomposition $V = U \oplus U^{\perp}$ so each vector $v \in V$ can be written uniquely in the form $$v = u + w,$$ where $u \in U$ and $w \in U^{\perp}$. Then, we can define operator $P_U$ on $V$, called the **orthogonal projection** of $V$ onto $U$ by: $P_U(v) = u$.

> [!proposition] Properties of Projection
> 1. $\text{range } P_U = U$;
> 2. $\text{null } P_U = U^{\perp}$;
> 3. $v - P_U v \in U^{\perp} \; \forall \; v \in V$;
> 4. $P_u^2 = P_u$;
> 5. $||P_U(v)|| \leq ||v|| \; \forall \; v \in V$.

> [!proposition]
> Suppose $U$ is a subspace of $V$ and $v \in V$. Then $$||v - P_U(v)|| \leq ||v - u||$$ for every $u \in U$. Furthermore, if $u \in U$ and the inequality above is an equality, then $u = P_U(v)$.

### Linear Functionals and Adjoints

> [!definition] Linear Functional
> A **linear functional** on $V$ is a linear map from $V$ to the scalars $\mathbb F$.

> [!theorem]
> Suppose $\varphi$ is a linear function on $V$. Then there is a unique vector $v \in V$ such that $$\varphi(u) = \langle u, v \rangle$$ for every $u \in V$.

> [!remark]
> Let $(e_1, \dots, e_n)$ be an orthonormal basis of $V$. Then, $$\varphi(u) = \langle u, \sum_{i = 1}^n \overline{\varphi(e_i)} e_i \rangle$$

> [!definition] Adjoint
> Let $T \in \mathcal L(V, W)$. The **adjoint** of $T$, denoted $T^* \in \mathcal L(W, V)$ such that $$\langle T(v), w \rangle = \langle v, T^*(w) \rangle$$ for all $v \in V$ and $w \in W$.

> [!definition] Adjoint Riesz representation
> Let $T \in \mathcal L(V, W)$. The **adjoint** of $T$, denoted $T^*$, is the function from $W$ to $V$ defined as follow. Fix $w \in W$. Consider the linear functional on $V$ that maps $v \in V$ to $\langle T(v), w \rangle$. Let $T^*(w)$ be the unique vector in $V$ such that this linear functional is given by taking inner products with $T^*(w)$. In other words, $T^*(w)$ is the unique vector in $V$ such that $$\langle T(v), w \rangle = \langle v, T^*(w) \rangle$$ for all $v \in V$.

> [!proposition]
> The function $T \rightarrow T^*$ has the following properties:
> - **Additivity**: $(S + T)^* = S^* + T^*$ for all $S, T \in \mathcal L(V, W);$
> - **Conjugate Homogeneity**: $(aT)^* = \overline{a} T^*$ for all $a \in \mathbb F$ and $T \in \mathcal L(V, W)$;
> - **Adjoint of adjoint**: $(T^*)^* = T$ for all $T \in \mathcal L(V, W)$;
> - **Identity**: $I^* = I$, where $I$ is the identity operator in $V$;
> - **Products**: $(ST)^* = T^* S^*$ for all $T \in \mathcal L(V, W)$ and $S \in \mathcal L(W, u)$.

> [!proposition]
> Suppose $T \in \mathcal L(V, W)$. Then
> 1. $\text{null } T^* = (\text{range } T)^\perp$;
> 2. $\text{range } T^* = (\text{null } T)^\perp$;
> 3. $\text{null } T = (\text{range } T^*)^\perp$;
> 4. $\text{range } T = (\text{null } T^*)^\perp$.

> [!definition] Conjugate Transpose
> The **conjugate transpose** of an $m$-by-$n$ matrix is the $n$-by-$m$ matrix obtained by interchanging the rows and columns and then taking the complex conjugate of each entry.

> [!proposition]
> Suppose $T \in \mathcal L(V, W)$. If $(e_1, \dots, e_n)$ is an orthonormal basis of $V$ and $(f_1, \dots, f_m)$ is an orthonormal basis of $W$, then $$\mathcal M(T^*, (f_1, \dots, f_m), (e_1, \dots, e_n))$$ is the conjugate transpose of $$\mathcal M(T, (e_1, \dots, e_n), (f_1, \dots, f_m)).$$

> [!remark]
> Let $\lambda$ is an eigenvalue of $T$ then $\overline{\lambda}$ is an eigenvalue of $T^*$.

## Operators on Inner-Product Space

### Self-Adjoint and Normal Operators

> [!definition] Self-Adjoint
> An operator $T \in \mathcal L(V)$ is called **self-adjoint** if $T = T^*$. 

> [!proposition]
> Every eigenvalue of a self-adjoint operator is real.

> [!proposition]
> If $V$ is a complex inner-product space and $T$ is an operator on $V$ such that $$\langle T(v), v \rangle = 0$$ for all $v \in V$, then $T = 0$.

> [!corollary]
> Let $V$ be a complex inner-product space and let $T \in \mathcal L(V)$. Then $T$ is self-adjoint if and only if $$\langle T(v), v \rangle \in \mathbb R$$ for every $v \in V$.

> [!proposition]
> If $T$ is a self-adjoint operator on $V$ such that $$\langle T(v), v \rangle = 0$$ for all $v \in V$, then $T = 0$.

> [!remark]
> Let $S, T$ be self-adjoint, then:
> - $(S + T)^* = S^* + T^* = S + T$
> - $(aT)^* = \overline{a}T^* = \overline{a}T$
> 
> The set of self-adjoint operators on a real inner-product space $V$ is a subspace of $\mathcal L(V)$.
> 
> The set of self-adjoint operators on a complex inner-product space $V$ is a subspace of $\mathcal L(V)$.

> [!definition] Normal Operator
> An operator $T \in \mathcal L(V)$ is called **normal** if it commutes with its adjoint: $$TT^* = T^* T.$$

> [!proposition]
> An operator $T \in \mathcal L(V)$ is normal if and only if $$||T(v)|| = ||T^*(v)||$$ for all $v \in V$.

> [!corollary]
> Suppose $T \in \mathcal L(V)$ is normal. If $v \in V$ is an eigenvector of $T$ with eigenvalue $\lambda \in \mathbb F$, then $v$ is also an eigenvector of $T^*$ with eigenvalue $\overline{\lambda}$.

> [!corollary]
> If $T \in \mathcal L(V)$ is normal, then eigenvectors of $T$ corresponding to distinct eigenvalues are orthogonal.

> [!example]
> If $T \in \mathcal L(v)$ is normal, then:
> 1. $\text{range } T = \text{range } T^*.$
> 2. $\text{null } T^k = \text{null } T$ and $\text{range } T^k = \text{range } T$ for every positive integer $k$.

> [!proposition]
> A normal operator on a complex inner-product space is self-adjoint if and only if all its eigenvalues are real.


### The Spectral Theorem

> [!theorem] Complex Spectral Theorem
> Suppose that $V$ is a complex inner-product space and $T \in \mathcal L(V)$. Then $V$ has an **orthonormal basis** consisting of eigenvectors of $T$ if and only if $T$ is normal.

> [!lemma]
> Suppose $T \in \mathcal L(V)$ is self-adjoint. If $\alpha, \beta \in \mathbb R$ are such that $\alpha^2 < 4\beta$, then $$T^2 + \alpha T + \beta I$$ is invertible.

> [!lemma]
> Suppose $T \in \mathcal L(V)$ is self-adjoint. Then $T$ has an eigenvalue.

>[!theorem] Real Spectral Theorem
>Suppose that $V$ is a real inner-product space and $T \in \mathcal L(V)$. Then $V$ has an **orthonormal basis** consisting of eigenvectors of $T$ if and only if $T$ is self-adjoint.

> [!proposition] Approximate Eigenvalue by nearby Eigenvalue
> Suppose $T \in \mathcal L(V)$ is self-adjoint, $\lambda \in \mathbb F$, and $\epsilon > 0$. Then, if there exists $v \in V$ such that $||v|| = 1$ and $$||T(v) - \lambda v|| < \epsilon$$ then $T$ has an eigenvalue $\lambda'$ such that $|\lambda - \lambda'| < \epsilon$.

> [!corollary]
> Suppose that $T \in \mathcal L(V)$ is self-adjoint (or that $\mathbb F = \mathbb C$ and that $T \in \mathcal L(V)$ is normal). Let $\lambda_1, \dots, \lambda_m$ denote the distinct eigenvalues of $T$. Then $$V = \text{null }(T - \lambda_1 I) \oplus \cdots \oplus \text{null } (T - \lambda_m I).$$ Furthermore, each vector in each $\text{null } (T - \lambda_j I)$ is orthogonal to all vectors in the other subspaces of this decomposition.

> [!proposition]
> Suppose $U$ is a finite-dimensional real vector space and $T \in \mathcal L(U)$. Then, $U$ has a basis consisting of eigenvectors of $T$ if and only if there is an inner product on $U$ that makes $T$ into a self-adjoint operator.

> [!remark]
> We can define an inner product by choosing a basis and declare it orthonormal.

### Normal Operators on Real Inner-Product Spaces

> [!lemma]
> Suppose $V$ is a two-dimensional real inner-product space and $T \in \mathcal L(V)$. Then the following are equivalent:
> 1. $T$ is normal but not self-adjoint;
> 2. The matrix of $T$ with respect to every orthonormal basis of $V$ has the form $$\begin{bmatrix}a & -b \\ b & a\end{bmatrix},$$ with $b \neq 0$;
> 3. The matrix of $T$ with respect to some orthonormal basis of $V$ has the form $$\begin{bmatrix}a & -b \\ b & a\end{bmatrix},$$ with $b > 0$.

> [!proposition]
> Suppose $T \in \mathcal L(V)$ is normal and $U$ is a subspace of $V$ that is invariant under $T$. Then
> 1. $U^{\perp}$ is invariant under $T$;
> 2. $U$ is invariant under $T^*$;
> 3. $(T|_U)^* = (T^*)|_U$;
> 4. $T_U$ is a normal operator on $U$;
> 5. $T_{U^\perp}$ is a normal operator on $U^\perp$.

> [!definition] Block Diagonal Matrix
> A **block diagonal matrix** is a square matrix of the form $$\begin{bmatrix}A_1 & & 0 \\ & \ddots & \\ 0 & & A_m \end{bmatrix},$$ where $A_1, \dots, A_m$ are square matrices lying along the diagonal and all the other entries of the matrix equal $0$.

> [!theorem]
> Suppose that $V$ is a real inner-product space and $T \in \mathcal L(V)$. Then $T$ is normal if and only if there is an orthonormal basis of $V$ with respect to which $T$ has a block diagonal matrix where each block is a $1$-by-$1$ matrix or a $2$-by-$2$ matrix of the form $$\begin{bmatrix}a & -b \\ b & a\end{bmatrix},$$ with $b > 0$.

### Positive Operators

> [!definition] Positive Operator
> An operator $T \in \mathcal L(V)$ is called **positive** if $T$ is self-adjoint and $$\langle T(v), v \rangle \geq 0$$ for all $v \in V$.

> [!definition] Square Root
> An operator $S$ is called a **square root** of an operator $T$ if $S^2 = T$.

> [!theorem]
> Let $T \in \mathcal L(V)$. Then the following are equivalent:
> 1. $T$ is positive;
> 2. $T$ is self-adjoint and all the eigenvalues of $T$ are nonnegative;
> 3. $T$ has a positive square root;
> 4. $T$ has a self-adjoint square root;
> 5. There exists an operator $S \in \mathcal L(V)$ such that $T = S^* S$.

> [!proposition]
> Every positive operator on $V$ has a unique positive square root.

> [!remark]
> 1. Sum of any two positive operators on $V$ is positive.
> 2. If $T \in \mathcal L(V)$ is positive, then so is $T^k$ for every positive integer $k$.

> [!proposition]
> Suppose that $T$ is a positive operator on $V$. Then, $T$ is invertible if and only if $$\langle Tv, v \rangle > 0$$ for every $v \in V \backslash \{0\}$.

> [!proposition] Uniqueness of the Positive Factor
> For $T \in \mathcal L(V)$, $S \in \mathcal L(V)$ is an isometry, and $R \in \mathcal L(V)$ is a positive operator such that $T = SR$, then $$R = \sqrt{T^* T}$$

> [!proposition] Polar Decomposition with Uniqueness
> $T \in \mathcal L(V)$ is invertible if and only if there exists a **unique isometry** $S$ such that $$T = S \sqrt{T^* T}.$$ 

### Isometries

> [!definition] Isometry
> An operator $S \in \mathcal L(V)$ is called an **isometry** if $$||S(v)|| = ||v||$$ for all $v \in V$. In other words, an operator is an isometry if it preserves norms.

> [!theorem]
> Suppose $S \in \mathcal L(V)$. Then the following are equivalent:
> 1. $S$ is an isometry;
> 2. $\langle S(u), S(v) \rangle = \langle u, v \rangle$ for all $u, v \in V$;
> 3. $S^* S = I$;
> 4. $(S(e_1), \dots, S(e_n))$ is orthonormal whenever $(e_1, \dots, e_n)$ is an orthonormal list of vectors in $V$;
> 5. There exists an orthonormal basis $(e_1, \dots, e_n)$ of $V$ such that $(S(e_1), \dots, S(e_n))$ is orthonormal;
> 6. $S^*$ is an isometry;
> 7. $\langle S^*(u), S^*(v) \rangle = \langle u, v \rangle$ for all $u, v \in V$;
> 8. $S S^* = I$;
> 9. $(S^*(e_1), \dots, S^*(e_n))$ is orthonormal whenever $(e_1, \dots, e_n)$ is an orthonormal list of vectors in $V$;
> 10. There exists an orthonormal basis $(e_1, \dots, e_n)$ of $V$ such that $(S^*(e_1), \dots, S^*(e_n))$ is orthonormal.

> [!remark]
> Every isometry is normal.

> [!theorem]
> Suppose $V$ is a complex inner-product space and $S \in \mathcal L(V)$. Then $S$ is an isometry if and only if there is an orthonormal basis of $V$ consisting of eigenvectors of $S$ all of whose corresponding eigenvalues have absolute value $1$. 

> [!theorem]
> Suppose that $V$ is a real inner-product space and $S \in \mathcal L(V)$. Then $S$ is an isometry if and only if there is an orthonormal basis of $V$ with respect to which $S$ has a block diagonal matrix where each block on the diagonal is a $1$-by-$1$ matrix containing $1$ or $-1$ or a $2$-by-$2$ matrix of the form $$\begin{bmatrix}\cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{bmatrix},$$ with $\theta \in (0, \pi)$.

> [!remark]
> The product of two isometries is an isometry.

### Polar and Singular-Value Decompositions

> [!remark]
> Analogy between $\mathcal C$ and $\mathcal L(V)$: If $T$ corresponds to $z$ then $T^*$ corresponds to $\overline{z}$. 

> [!definition] Polar Decomposition
> If $T \in \mathcal L(V)$, then there exists an isometry $S \in \mathcal L(V)$ such that $$T = S\sqrt{T^* T}.$$

> [!definition] Singular Values
> Suppose $T \in \mathcal L(V)$. The **singular values** of $T$ are the eigenvalues of $\sqrt{T^* T}$, with each eigenvalue $\lambda$ repeated $\dim \text{null }(\sqrt{T^* T} - \lambda I)$ times.

> [!definition] Singular-Value Decomposition
> Suppose $T \in \mathcal L(V)$ has singular values $s_1, \dots, s_n$. Then there exist orthonormal bases $(e_1, \dots, e_n)$ and $(f_1, \dots, f_n)$ of $V$ such that $$T(v) = \sum_{i = 1}^n s_i \langle v, e_i \rangle f_i$$ for every $v \in V$.

> [!corollary]
> Suppose $T \in \mathcal L(V)$ has singular-value decomposition given by $$T(v) = \sum_{i = 1}^n s_i \langle v, e_i \rangle f_i$$ for every $v \in V$, where $s_1, \dots, s_n$ are the singular values of $T$ and $(e_1, \dots, e_n)$ and $(f_1, \dots, f_n)$ are orthonormal bases of $V$.
> 1. $T^*(v) = \sum_{i = 1}^n s_i \langle v, f_i \rangle e_i$ for every $v \in V$.
> 2. If $T$ is invertible, then $$T^{-1}(v) = \sum_{i = 1}^n \frac{\langle v, f_i \rangle e_i}{s_i}$$

> [!proposition]
> Suppose $T \in \mathcal L(V)$. Then,
> 1. $T$ is invertible if and only if $0$ is not a singular value of $T$.
> 2. $\dim \text{range } T$ equals the number of nonzero singular values of $T$.
> 3. $T$ is isometry if and only if all the singular values of $S$ equal $1$.

> [!proposition]
> Suppose $T_1, T_2 \in \mathcal L(V)$. Then, $T_1$ and $T_2$ have the same singular values if and only if there exist isometries $S_1, S_2 \in \mathcal L(V)$ such that $T_1 = S_1 T_2 S_2$.

> [!proposition]
> Suppose $T \in \mathcal L(V)$. Let $\hat{s}$ denote the smallest singular value of $T$, and let $s$ denote the largest singular value of $T$. Then, $$\hat{s} ||v|| \leq ||T(v)|| \leq s ||v||$$ for every $v \in V$.

> [!proposition]
> Suppose $T', T'' \in \mathcal L(V)$. Let $s'$ denote the largest singular value of $T'$, let $s''$ denote the largest singular value of $T''$, and let $s$ denote the largest singular value of $T' + T''$. Then, $s \leq s' + s''$.

## Operators on Complex Vector Space

### Generalized Eigenvectors

> [!definition] Generalized Eigenvector
> Suppose $T \in \mathcal L(V)$ and $\lambda$ is an eigenvalue of $T$. A vector $v \in V$ is called a **generalized eigenvector** of $T$ corresponding to $\lambda$ if $$(T - \lambda I)^j v = 0$$ for some positive integer $j$.

> [!proposition]
> If $T \in \mathcal L(V)$ and $m$ is a nonnegative integer such that $\text{null } T^m = \text{null } T^{m + 1}$, then $$\text{null } T^0 \subset \text{null } T^1 \subset \cdots \subset \text{null } T^m = \text{null } T^{m + 1} = \text{null } T^{m + 2} = \cdots .$$

> [!proposition]
> If $T \in \mathcal L(V)$, then $$\text{null } T^{\dim V} = \text{null } T^{\dim V + 1} = \text{null } T^{\dim + 2} = \cdots.$$

> [!corollary]
> Suppose $T \in \mathcal L(V)$ and $\lambda$ is an eigenvalue of $T$. Then the set of generalized eigenvectors of $T$ corresponding to $\lambda$ equals $\text{null }(T - \lambda I)^{\dim V}$.

> [!definition] Nilpotent
> An operator is called **nilpotent** if some power of it equals $0$.

> [!corollary]
> Suppose $N \in \mathcal L(V)$ is nilpotent. Then $N^{\dim V} = 0$.

> [!proposition]
> If $ST$ is nilpotent, then $TS$ is nilpotent.

> [!proposition]
> If $T \in \mathcal L(V)$, then $$\text{range } T^{\dim V} = \text{range } T^{\dim V + 1} = \text{range } T^{\dim V + 2} = \cdots.$$

### Decomposition of an Operator

> [!proposition]
> If $T \in \mathcal L(V)$ and $p \in \mathcal P(\mathbb F)$, then $\text{null } p(T)$ is invariant under $T$.

> [!theorem]
> Suppose $V$ is a complex vector space and $T \in \mathcal L(V)$. Let $\lambda_1, \dots, \lambda_m$ be the distinct eigenvalues of $T$, and let $U_1, \dots, U_m$ be the corresponding subspaces of generalized eigenvectors. Then
> 1. $V = U_1 \oplus \cdots \oplus U_m$;
> 2. Each $U_j$ is invariant under $T$;
> 3. Each $(T - \lambda_j I) | U_j$ is nilpotent.

> [!corollary]
> Suppose $V$ is a complex vector space and $T \in \mathcal L(V)$. Then there is a basis of $V$ consisting of generalized eigenvectors of $T$.

> [!lemma]
> Suppose $N$ is nilpotent operator on $V$. Then there is a basis of $V$ with respect to which the matrix of $N$ has the form $$\begin{bmatrix}0 & & * \\ & \ddots & \\ 0 & & 0 \end{bmatrix}$$ here all entries on and below the diagonal are $0$'s.

> [!theorem]
> Suppose $V$ is a complex vector space and $T \in \mathcal L(V)$. Let $\lambda_1, \dots, \lambda_m$ be distinct eigenvalues of $T$. Then there is a basis of $V$ with respect to which $T$ has a block diagonal matrix of the form $$\begin{bmatrix} A_1 & & 0 \\ & \ddots & \\ 0 & & A_m\end{bmatrix},$$ where each $A_j$ is an upper-triangular matrix of the form $$\begin{bmatrix}\lambda_j & & * \\ & \ddots & \\ 0 & & \lambda_j \end{bmatrix}.$$

### Square Roots

> [!lemma]
> Suppose $N \in \mathcal L(V)$ is nilpotent. Then $1 + N$ has a square root.

> [!theorem]
> Suppose $V$ is a complex vector space. If $T \in \mathcal L(V)$ is invertible, then $T$ has a square root.

### The Minimal Polynomial

> [!theorem]
> Let $T \in \mathcal L(V)$. Then the roots of the minimal polynomial of $T$ are precisely the eigenvalues of $T$.

> [!proposition]
> Suppose $V$ is an inner-product space. If $T \in \mathcal L(V)$ is normal, then the minimal polynomial of $T$ has no repeated root.

### Jordan Form

> [!definition] Function $m(v)$
> Suppose $N \in \mathcal L(V)$ is nilpotent. For each nonzero vector $v \in V$, let $m(v)$ denote the largest nonnegative integer such that $N^{m(v)}(v) \neq 0$.
 
> [!lemma]
> If $N \in \mathcal L(V)$ is nilpotent, then there exist vectors $v_1, \dots, v_k \in V$ such that
> 1. $(v_1, N(v_1), \dots, N^{m(v_1)}(v_1), \dots, v_k, N(v_k), \dots, N^{m(v_k)}(v_k))$ is a basis of $V$;
> 2. $(N^{m(v_1)}(v_1), \dots, N^{m(v_k)}v_k)$ is a basis of $\text{null } N$.

> [!definition] Jordan Basis
> Suppose $T \in \mathcal L(V)$. A basis of $V$ is called a **Jordan basis** for $T$ if with respect to this basis $T$ has a block diagonal matrix $$\begin{bmatrix}A_1 & & 0 \\  & \ddots & \\ 0 & & A_m\end{bmatrix},$$ where each $A_j$ is an upper-triangular matrix of the form $$A_j = \begin{bmatrix}\lambda_j & 1 & & 0 \\ & \ddots & \ddots & \\ & & \ddots & 1 \\ 0 & & & \lambda_j\end{bmatrix}$$

> [!theorem]
> Suppose $V$ is a complex vector space. If $T \in \mathcal L(V)$, then there is a basis of $V$ that is a Jordan basis for $T$.

## Trace and Determinant

### Change of Basis

> [!proposition]
> If $(u_1, \dots, u_n)$ and $(v_1, \dots, v_n)$ are bases of $V$, then $\mathcal M(I, (u_1, \dots, u_n), (v_1, \dots, v_n))$ is invertible and $$\mathcal M(I, (u_1, \dots, u_n), (v_1, \dots, v_n))^{-1} = \mathcal M(I, (v_1, \dots, v_n), (u_1, \dots, u_n)).$$

> [!theorem]
> Suppose $T \in \mathcal L(V)$. Let $(u_1, \dots, u_n)$ and $(v_1, \dots, v_n)$ be bases of $V$. Let $A = \mathcal M(I, (u_1, \dots, u_n), (v_1, \dots, V_n))$. Then $$\mathcal M(T, (u_1, \dots, u_n)) = A^{-1} \mathcal M(T, (v_1, \dots, v_n)) A.$$

### Trace

> [!definition] Trace of a Linear Map
> For $T \in \mathcal L(V)$, the negative of the coefficient of $z^{n - 1}$ (or $x^{n - 1}$ for real vector spaces) in the characteristic polynomial of $T$ is called the **trace** of $T$, denoted $\text{trace } T$.

> [!definition] Trace of a Square Matrix
> The **trace** of a square matrix $A$, denoted $\text{trace } A$, to be the sum of the diagonal entries.

> [!proposition]
> If $A$ and $B$ are square matrices of the same size, then $$\text{trace}(AB) = \text{trace}(BA).$$

> [!corollary]
> Suppose $T \in \mathcal L(V)$. If $(u_1, \dots, u_n)$ and $(v_1, \dots, v_n)$ are bases of $V$, then $$\text{trace } \mathcal M(T, (u_1, \dots, u_n)) = \text{trace } \mathcal M(T, (v_1, \dots, v_n)).$$

> [!theorem]
> If $T \in \mathcal L(V)$, then $\text{trace } T = \text{trace } \mathcal M(T)$.

> [!corollary]
> If $S, T \in \mathcal L(V)$, then $$\text{trace}(ST) = \text{trace}(TS) \quad \text{and} \quad \text{trace}(S + T) = \text{trace } S + \text{trace } T.$$

> [!corollary]
> There do not exist operators $S, T \in \mathcal L(V)$ such that $ST - TS = I$.

> [!proposition]
> If $T \in \mathcal L(V)$, and $(u_1, \dots, u_n)$ is an orthonormal basis then $$\text{trace } T = \sum_{k = 1}^n \langle T(u_k), u_k \rangle$$

> [!example]
> Suppose $V$ is an inner-product space and $T \in \mathcal L(V)$, and $(e_1, \dots, e_n)$ is an orthonormal basis of $V$, then $$\text{trace } T = \sum_{k = 1}^n \langle T^* T(e_k), e_k \rangle = \langle T(e_k), T(e_k) \rangle = \sum_{k = 1}^n ||T(e_k)||^2$$

> [!remark]
> Suppose $V$ is an inner-product space and $T \in \mathcal L(V)$ and $$\begin{bmatrix}a_{1, 1} & \cdots & a_{1, n} \\ \vdots & & \vdots \\ a_{n, 1} & \cdots & a_{n, n}\end{bmatrix}$$ is the matrix of $T$ with respect to some orthonormal basis, then $$\text{trace } (T^* T) = \sum_{i, j} |a_{i, j}|^2$$

### Determinant of an Operator

> [!definition] Determinant
> If $A$ is an $n$-by-$n$ matrix $$A = \begin{bmatrix}a_{1, 1} & \dots & a_{1, n} \\ \vdots & & \vdots \\ a_{n, 1} & \cdots & a_{n, n}\end{bmatrix},$$ then the **determinant** of $A$, denoted $\det A$, is defined by $$\det A = \sum_{(m_1, \dots, m_n) \in \text{perm } n} (\text{sign}(m_1, \dots, m_n)) a_{m_1, 1} \dots a_{m_n, n}$$

> [!lemma]
> Suppose $A$ is a square matrix. If $B$ is the matrix obtained from $A$ by interchanging two columns, then $$\det A = -\det B.$$

> [!lemma]
> If $A$ is a square matrix that has two equal columns, then $\det A = 0$.

> [!lemma]
> Suppose $A = \begin{bmatrix}a_1 & \dots & a_n\end{bmatrix}$ is an $n$-by-$n$ matrix. If $(m_1, \dots, m_n)$ is a permutation, then $$\det \begin{bmatrix}a_{m_1} & \dots & a_{m_n}\end{bmatrix} = (\text{sign}(m_1, \dots, m_n)) \det A.$$

> [!theorem]
> If $A$ and $B$ are square matrices of the same size, then $$\det(AB) = \det(BA) = (\det A)(\det B).$$

> [!corollary]
> Suppose $T \in \mathcal L(V)$. If $(u_1, \dots, u_n)$ and $(v_1, \dots, v_n)$ are bases of $V$, then $$\det \mathcal M(T, (u_1, \dots, u_n)) = \det \mathcal M(T, (v_1, \dots, v_n)).$$

> [!theorem]
> If $T \in \mathcal L(V)$, then $\det T = \det \mathcal M(T)$.

> [!corollary]
> If $S, T \in \mathcal L(V)$, then $$\det(ST) = \det(TS) = (\det S)(\det T).$$

## Volume

> [!proposition]
> Suppose that $V$ is an inner-product space. If $S \in \mathcal L(V)$ is an isometry, then $|\det S| = 1$.

> [!corollary]
> Suppose $V$ is an inner-product space. If $T \in \mathcal L(V)$, then $$|\det T| = \det \sqrt{T^* T}.$$

## Vector Space Over $\mathbb F_q$

> [!theorem]
> Let $V$ be a vector space over $\mathbb F_q$. If $\dim(V) = k$, then
> 1. $V$ has $q^k$ elements;
> 2. $V$ has $\frac{1}{k!} \prod_{i = 0}^{k = 1} (q^k - q^i)$ different bases.

> [!definition] Inner Product on $\mathbb F_q^n$
> An inner product on $\mathbb F_q^n$ is a pairing $\langle, \rangle : \mathbb F_q^n \times \mathbb F_q^n \rightarrow \mathbb F_q$ satisfying the following conditions: for all $u, v, w \in \mathbb F_q^n$
> 2. $\langle u + v, w \rangle = \langle u, w \rangle + \langle v, w \rangle$;
> 3. $\langle u, v + w \rangle = \langle u, v \rangle + \langle u, w \rangle$;
> 4. $\langle u, v \rangle = 0$ for all $u \in \mathbb F_q^n$ if and only if $v = 0$;
> 5. $\langle u, v \rangle = 0$ for all $v \in \mathbb F_q^n$ if and only if $u = 0$;

> [!definition] Scalar Product and Orthogonal
> Let $v = (v_1, \dots, v_n), w = (w_1, \dots, w_n) \in \mathbb F_q^n$/
> 1. The **scalar product** of $v$ and $w$ is defined as $$v \dot w = \sum_{i = 1}^n v_i w_i \in \mathbb F_q$$ is an inner product.
> 2. Two vectors $v$ and $w$ are said to be **orthogonal** if $v \cdot w = 0$.
> 3. Let $S$ be a nonempty subset of $\mathbb F_q^n$. The **orthogonal complement** $S^{\perp}$ of $S$ is defined to be $$S^\perp = \{v \in \mathbb F_q^n : v \cdot s = 0 \; \forall s \in S\}.$$ If $S = \emptyset$, then we define $S^{\perp} = \mathbb F_q^n$.

> [!theorem]
> Let $S$ be a subset of $\mathbb F_q^n$, then we have $$\dim(<S>) + \dim(S^{\perp}) = n.$$

## Example


### Polynomial

> [!proposition]
> Suppose $a_0, \dots, a_{n - 1} \in \mathbb C$. Then the matrix $$A = \begin{bmatrix} 0 & 0 & \cdots & 0 & -a_0\\ 1 & 0 & \cdots & 0 & -a_1\\ 0 & 1 & \ddots & \vdots & -a_2\\ \vdots & & \ddots & 0 & \vdots\\ 0 & 0 & \cdots & 1 & -a_{n-1} \end{bmatrix}$$ is called the **companion matrix** of the monic polynomial $$p(z) = z^n + a_{n - 1} z^{n - 1} + \cdots + a_1 z + a_0$$ and thus has $p(z)$ is both the minimal and characteristic polynomials.

### Hilbert-Schmidt Inner Product

> [!definition] Hilber-Schmidt Inner Prodcut
> Suppose $V$ is an inner-product space. Then $$\langle S, T \rangle$$ defines an inner product on $\mathcal L(V)$.


### Hmm?

> [!example]
> Suppose $T \in \mathcal L(V)$, $m$ is a positive integer, and $v \in V$ is such that $T^{m - 1}(v) \neq 0$ but $T^m(v)$. Then, $$(v, T(v), T^2(v), \dots, T^{m - 1}(v))$$ is linearly independent.

> [!example]
> If $T \in \mathcal L(V)$, then $$V = \text{null } T^n \oplus \text{range } T^n,$$ where $n = \dim V$.

> [!remark]
> When we have a formula about $T$ and want to find a formula about $T*$, we use:
> $$\langle T(v), w \rangle = \langle v, T^* (w) \rangle$$
