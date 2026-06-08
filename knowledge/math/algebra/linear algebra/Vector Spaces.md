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

