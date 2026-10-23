Reference:
- `[Ax2]` — S. Axler, _Linear Algebra Done Right_, 2nd ed. (1997), Chapter 10: Trace and Determinant. Not opened; the note follows its order, and the key marks results whose 4th-edition number I could not check (the 4th-edition Chapter 9 PDF could not be opened, and the Chapter 8 PDF stops before §8D Trace).
- `[LNS16]` — I. Lankham, B. Nachtergaele, A. Schilling, _Linear Algebra As an Introduction to Abstract Mathematics_ (2016), §8.2 Determinants, LibreTexts edition: https://math.libretexts.org/Bookshelves/Linear_Algebra/Book%3A_Linear_Algebra_(Schilling_Nachtergaele_and_Lankham)

## Definition

> [!definition] Parameters
> - $V$: a finite-dimensional [[Vector Spaces|vector space]] over $\mathbb F$, $n = \dim V$.
> - $T \in \mathcal L(V)$: an operator ([[Operators]]).

> [!definition] Trace of a Linear Map
> For $T \in \mathcal L(V)$, the negative of the coefficient of $z^{n - 1}$ (or $x^{n - 1}$ for real vector spaces) in the characteristic polynomial of $T$ is called the **trace** of $T$, denoted $\text{trace } T$. `[Ax2]`

> [!definition] Parameters
> - $A = (a_{i, j})$: an $n$-by-$n$ [[Matrix]] with entries in $\mathbb F$.

> [!definition] Trace of a Square Matrix
> The **trace** of a square matrix $A$, denoted $\text{trace } A$, to be the sum of the diagonal entries. `[Ax2]`

> [!definition] Determinant
> If $A$ is an $n$-by-$n$ matrix $$A = \begin{bmatrix}a_{1, 1} & \dots & a_{1, n} \\ \vdots & & \vdots \\ a_{n, 1} & \cdots & a_{n, n}\end{bmatrix},$$ then the **determinant** of $A$, denoted $\det A$, is defined by $$\det A = \sum_{(m_1, \dots, m_n) \in \text{perm } n} (\text{sign}(m_1, \dots, m_n)) a_{m_1, 1} \dots a_{m_n, n}$$
>
> `[Ax2]`; `[LNS16 Def 8.2.1]` permutes the column index instead, $\det A = \sum_{\pi \in S_n} \operatorname{sign}(\pi)\, a_{1, \pi(1)} \cdots a_{n, \pi(n)}$ — the same number, since $\det A^T = \det A$ `[LNS16 Thm 8.2.3]`.

## Property

### Change of Basis

> [!definition] Parameters
> - $(u_1, \dots, u_n)$, $(v_1, \dots, v_n)$: bases of $V$.
> - $I$: the identity operator on $V$.

> [!proposition] The change-of-basis matrix is invertible
> If $(u_1, \dots, u_n)$ and $(v_1, \dots, v_n)$ are bases of $V$, then $\mathcal M(I, (u_1, \dots, u_n), (v_1, \dots, v_n))$ is invertible and $$\mathcal M(I, (u_1, \dots, u_n), (v_1, \dots, v_n))^{-1} = \mathcal M(I, (v_1, \dots, v_n), (u_1, \dots, u_n)).$$ `[Ax2]`

> [!definition] Parameters
> - $A = \mathcal M(I, (u_1, \dots, u_n), (v_1, \dots, v_n))$.

> [!theorem] Change-of-basis formula — $\mathcal M(T, (u)) = A^{-1} \mathcal M(T, (v)) A$
> Suppose $T \in \mathcal L(V)$. Let $(u_1, \dots, u_n)$ and $(v_1, \dots, v_n)$ be bases of $V$. Let $A = \mathcal M(I, (u_1, \dots, u_n), (v_1, \dots, v_n))$. Then $$\mathcal M(T, (u_1, \dots, u_n)) = A^{-1} \mathcal M(T, (v_1, \dots, v_n)) A.$$ `[Ax2]`

### Trace

> [!definition] Parameters
> - $A, B$: square matrices of the same size.

> [!proposition] $\text{trace}(AB) = \text{trace}(BA)$
> If $A$ and $B$ are square matrices of the same size, then $$\text{trace}(AB) = \text{trace}(BA).$$ `[Ax2]`

> [!corollary] The trace of the matrix of an operator does not depend on the basis
> Suppose $T \in \mathcal L(V)$. If $(u_1, \dots, u_n)$ and $(v_1, \dots, v_n)$ are bases of $V$, then $$\text{trace } \mathcal M(T, (u_1, \dots, u_n)) = \text{trace } \mathcal M(T, (v_1, \dots, v_n)).$$ `[Ax2]`

> [!theorem] Trace of an operator equals trace of its matrix
> If $T \in \mathcal L(V)$, then $\text{trace } T = \text{trace } \mathcal M(T)$. `[Ax2]`

> [!definition] Parameters
> - $S \in \mathcal L(V)$: an operator.

> [!corollary] Trace is additive and $\text{trace}(ST) = \text{trace}(TS)$
> If $S, T \in \mathcal L(V)$, then
> - $\text{trace}(ST) = \text{trace}(TS)$
> - $\text{trace}(S + T) = \text{trace } S + \text{trace } T$
>
> `[Ax2]`

> [!corollary] The identity is not a commutator — no $S, T$ with $ST - TS = I$
> There do not exist operators $S, T \in \mathcal L(V)$ such that $ST - TS = I$. `[Ax2]`

> [!definition] Parameters
> - $V$: a finite-dimensional inner-product space ([[Inner-Product Spaces]]).
> - $(u_1, \dots, u_n)$, $(e_1, \dots, e_n)$: orthonormal bases of $V$.

> [!proposition] Trace in an orthonormal basis — $\text{trace } T = \sum_k \langle T(u_k), u_k \rangle$
> If $T \in \mathcal L(V)$, and $(u_1, \dots, u_n)$ is an orthonormal basis then $$\text{trace } T = \sum_{k = 1}^n \langle T(u_k), u_k \rangle$$ `[Ax2]`

> [!example]
> Suppose $V$ is an inner-product space and $T \in \mathcal L(V)$, and $(e_1, \dots, e_n)$ is an orthonormal basis of $V$, then $$\text{trace}(T^* T) = \sum_{k = 1}^n \langle T^* T(e_k), e_k \rangle = \sum_{k = 1}^n \langle T(e_k), T(e_k) \rangle = \sum_{k = 1}^n ||T(e_k)||^2$$
> (the previous proposition applied to $T^* T$)

> [!remark]
> Suppose $V$ is an inner-product space and $T \in \mathcal L(V)$ and $$\begin{bmatrix}a_{1, 1} & \cdots & a_{1, n} \\ \vdots & & \vdots \\ a_{n, 1} & \cdots & a_{n, n}\end{bmatrix}$$ is the matrix of $T$ with respect to some orthonormal basis, then $$\text{trace } (T^* T) = \sum_{i, j} |a_{i, j}|^2$$

### Determinant of an Operator

> [!definition] Parameters
> - $A$, $B$: square matrices of the same size.
> - $a_1, \dots, a_n$: the columns of $A$.
> - $(m_1, \dots, m_n)$: a permutation of $(1, \dots, n)$.

> [!lemma] Interchanging two columns changes the sign of the determinant
> Suppose $A$ is a square matrix. If $B$ is the matrix obtained from $A$ by interchanging two columns, then $$\det A = -\det B.$$ `[LNS16 Thm 8.2.3]`

> [!lemma] Two equal columns give determinant $0$
> If $A$ is a square matrix that has two equal columns, then $\det A = 0$. `[LNS16 Thm 8.2.3]`

> [!lemma] Permuting the columns multiplies the determinant by the sign
> Suppose $A = \begin{bmatrix}a_1 & \dots & a_n\end{bmatrix}$ is an $n$-by-$n$ matrix. If $(m_1, \dots, m_n)$ is a permutation, then $$\det \begin{bmatrix}a_{m_1} & \dots & a_{m_n}\end{bmatrix} = (\text{sign}(m_1, \dots, m_n)) \det A.$$ `[Ax2]`

> [!theorem] Determinant is multiplicative — $\det(AB) = (\det A)(\det B)$
> If $A$ and $B$ are square matrices of the same size, then $$\det(AB) = \det(BA) = (\det A)(\det B).$$ `[LNS16 Thm 8.2.3]`

> [!corollary] The determinant of the matrix of an operator does not depend on the basis
> Suppose $T \in \mathcal L(V)$. If $(u_1, \dots, u_n)$ and $(v_1, \dots, v_n)$ are bases of $V$, then $$\det \mathcal M(T, (u_1, \dots, u_n)) = \det \mathcal M(T, (v_1, \dots, v_n)).$$ `[Ax2]`

> [!theorem] Determinant of an operator equals determinant of its matrix
> If $T \in \mathcal L(V)$, then $\det T = \det \mathcal M(T)$. `[Ax2]`

> [!corollary] Determinant of operators is multiplicative — $\det(ST) = (\det S)(\det T)$
> If $S, T \in \mathcal L(V)$, then $$\det(ST) = \det(TS) = (\det S)(\det T).$$ `[Ax2]`

### Volume

> [!definition] Parameters
> - $V$: a finite-dimensional inner-product space.
> - $S \in \mathcal L(V)$: an isometry ([[Operators#Isometries|Isometries]]).

> [!proposition] Isometries have $|\det S| = 1$
> Suppose that $V$ is an inner-product space. If $S \in \mathcal L(V)$ is an isometry, then $|\det S| = 1$. `[Ax2]`

> [!corollary] $|\det T| = \det \sqrt{T^* T}$
> Suppose $V$ is an inner-product space. If $T \in \mathcal L(V)$, then $$|\det T| = \det \sqrt{T^* T}.$$ `[Ax2]`

## Related

### Prerequisites
- [[Matrix]] — square matrices, the matrix $\mathcal M(T)$ of an operator
- [[Operators]] — polar decomposition (for $|\det T|$), isometries
- [[Symmetric Group]] — the permutations and their sign in the determinant formula
- [[Polynomial]] — the characteristic polynomial defining $\text{trace } T$
