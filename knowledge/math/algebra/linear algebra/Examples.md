Reference:
- `[Ax]` — S. Axler, _Linear Algebra Done Right_, 4th ed. (2024, open access): https://linear.axler.net/ — §8A. Numbers checked in the chapter PDF at https://link.springer.com/book/10.1007/978-3-031-41026-0.
- `[Ax2]` — S. Axler, _Linear Algebra Done Right_, 2nd ed. (1997). Not opened; the key marks results whose 4th-edition number I could not check.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Example

### Polynomial

> [!definition] Parameters
> - $n$: a positive integer.
> - $a_0, \dots, a_{n - 1} \in \mathbb C$.
> - $p(z) = z^n + a_{n - 1} z^{n - 1} + \cdots + a_1 z + a_0$: a monic [[Polynomial]].

> [!proposition] Companion matrix — $p$ is both its minimal and its characteristic polynomial
> Suppose $a_0, \dots, a_{n - 1} \in \mathbb C$. Then the matrix $$A = \begin{bmatrix} 0 & 0 & \cdots & 0 & -a_0\\ 1 & 0 & \cdots & 0 & -a_1\\ 0 & 1 & \ddots & \vdots & -a_2\\ \vdots & & \ddots & 0 & \vdots\\ 0 & 0 & \cdots & 1 & -a_{n-1} \end{bmatrix}$$ is called the **companion matrix** of the monic polynomial $$p(z) = z^n + a_{n - 1} z^{n - 1} + \cdots + a_1 z + a_0$$ and thus has $p(z)$ is both the minimal and characteristic polynomials. `[Ax2]`

### Hilbert-Schmidt Inner Product

> [!definition] Parameters
> - $V$: a finite-dimensional [[Inner-Product Spaces|inner-product space]].
> - $S, T \in \mathcal L(V)$: operators ([[Operators]]).

> [!definition] Hilbert–Schmidt Inner Product
> Suppose $V$ is an inner-product space. Then $$\langle S, T \rangle = \operatorname{trace}(ST^*)$$ defines an inner product on $\mathcal L(V)$. `[Ax2]`
> ⚠️ CLAUDE – verify: the formula $\operatorname{trace}(ST^*)$ is supplied by me (the standard Hilbert–Schmidt / Frobenius inner product; in an orthonormal basis it is $\sum_{i,j} a_{ij}\overline{b_{ij}}$); check it against the source exercise.

### Hmm?

> [!example]
> Suppose $T \in \mathcal L(V)$, $m$ is a positive integer, and $v \in V$ is such that $T^{m - 1}(v) \neq 0$ but $T^m(v) = 0$. Then, $$(v, T(v), T^2(v), \dots, T^{m - 1}(v))$$ is linearly independent.

> [!example]
> If $T \in \mathcal L(V)$, then $$V = \text{null } T^n \oplus \text{range } T^n,$$ where $n = \dim V$. `[Ax 8.4]`

> [!remark]
> When we have a formula about $T$ and want to find a formula about $T^*$, we use:
> $$\langle T(v), w \rangle = \langle v, T^* (w) \rangle$$

## Related

### Prerequisites
- [[Operators]] — nilpotent operators, adjoints
- [[Trace, Determinant, and Volume]] — the trace in the Hilbert–Schmidt inner product
- [[Eigenvalues and Eigenvectors]] — minimal polynomial
