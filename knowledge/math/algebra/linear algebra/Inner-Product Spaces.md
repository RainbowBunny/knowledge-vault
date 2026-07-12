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

## Example

### Hermitian Inner Product

