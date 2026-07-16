## Syntax



## Representation



### Matrix Form

> [!definition] Matrix Representation of Rank Metric Codes
> Uses the space $\{\mathbb F_q^{m \times n}\}$ of rectangular $m \times n$ matrices over the base field $\mathbb F_q$.
> 
> 

> [!definition] Matrix Code
> The matrix code $\mathcal M$ is a subset of the space $\{\mathbb F_q^{m \times n}\}$ of matrices.

> [!definition] Matrix Norm
> The **norm** $\mathcal N(M)$ of a matrix $M \in \mathbb F_q^{m \times n}$ is its algebraic rank over the field $\mathbb F_q, \mathcal N(M) = \text{Rank}_{\mathbb F_q}(M)$.

> [!definition] Matrix Distance
> The **rank distance** between two matrices $M_1, M_2 \in \mathbb F_q^{m \times n}$ is defined as
> $$\mathcal d_r(M_1, M_2) = \text{Rank}_{\mathbb F_q}(M_1 - M_2)$$

> [!definition] Rank Code Distance
> The **rank code distance** $d_r$ is the minimum rank distance between two different code matrices:
> $$d_r = \min\{\text{Rank}_{\mathbb F_q}(M_i - M_j): M_i, M_j \in \mathcal M, i \neq j\}.$$

### Vector Form

> [!definition] Vector Representation of Rank Metric Codes
> Uses the space $\mathbb F_{q^m}^n$ of vectors of length $n$ over the extension field $\mathbb F_{q^m}$. 

> [!definition] Vector Code
> The vector code $\mathcal V$ is any subset of the vector space $\{\mathbb F_{q^m}^n\}$

> [!definition] Vector Norm
> Norm of a vector $v \in \mathbb F_{q^m}^n$ is the **column rank** of the vector
> $$N(v) = \text{Rank}_{\mathbb F_q}(v)$$

> [!definition] Vector Distance
> The **rank distance** between two vectors $v_1, v_2$ is defined as
> $$d_r(v_1, v_2) = \text{Rank}_{\mathbb F_q}(v_1 - v_2)$$
