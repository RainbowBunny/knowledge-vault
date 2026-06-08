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

