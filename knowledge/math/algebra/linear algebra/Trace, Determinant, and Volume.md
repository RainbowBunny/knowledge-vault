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

