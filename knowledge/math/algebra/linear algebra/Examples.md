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
