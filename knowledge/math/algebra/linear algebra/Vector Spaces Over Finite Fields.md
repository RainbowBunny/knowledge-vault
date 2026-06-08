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

