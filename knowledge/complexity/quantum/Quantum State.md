Reference:
- https://abgrilo.github.io/viasm/introduction.pdf

## Basic Definition

> [!definition] Quantum State
> A quantum state is represented by a unit vector in a [[Complex Hilbert Space]].

### Qubit

> [!definition] Qubit
> Quantum state with two levels.
> - Hilbert space: $\mathbb{C}^2$.
> - Notation: $|\psi \rangle = \alpha |0 \rangle + \beta |1 \rangle, \alpha, \beta \in \mathbb{C}, |\alpha|^2 + |\beta|^2 = 1$.

### Basis

> [!definition] Computational Basis
> $\{|0 \rangle = \begin{pmatrix}1 \\ 0\end{pmatrix}, |1 \rangle = \begin{pmatrix}0 \\ 1\end{pmatrix}\}$

> [!definition] Hadamard Basis
> $\{|+ \rangle = \begin{pmatrix}\frac{1}{\sqrt{2}}\\ \frac{1}{\sqrt{2}}\end{pmatrix}, |- \rangle = \begin{pmatrix}\frac{1}{\sqrt{2}}\\ -\frac{1}{\sqrt{2}}\end{pmatrix}\}$

> [!definition] Clockwise Basis
> $\{\}$

### Dirac Notation

> [!definition] Ket
> Ket is the column vector:
> $$|\psi \rangle = \begin{pmatrix}a_1 \\ a_2 \\ \vdots \\ a_m\end{pmatrix}, |\varphi \rangle = \begin{pmatrix}b_1 \\ b_2 \\ \vdots \\ b_m\end{pmatrix}$$

> [!definition] Bra
> Bra is the row vector of complex conjugate:
> $$|\psi \rangle = \begin{pmatrix}b_1^* & b_2^* & \cdots & a_m^*\end{pmatrix}, |\varphi \rangle = \begin{pmatrix}b_1^* & b_2^* & \cdots & b_m^*\end{pmatrix}$$

> [!definition] Bra-Ket
> Bar-Ket is the inner product:
> $$\begin{align}
> \langle \phi | \psi \rangle &= \begin{pmatrix}b_1^* & b_2^* \cdots & b_m^*\end{pmatrix} \begin{pmatrix}a_1 \\ a_2 \\ \vdots \\ a_m\end{pmatrix} \\
> &= \sum_{i \in [m]}b_i^* a_i \in \mathbb{C}\end{align}$$

> [!definition] Ket-Bar
> Ket-Bar is the outer product:
> $$\begin{align}
> | \varphi \rangle \langle \psi | &=  \begin{pmatrix}b_1 \\ b_2 \\ \vdots \\ b_m\end{pmatrix} \begin{pmatrix}a_1^* & a_2^* & \cdots & a_m^*\end{pmatrix} \\
> &= \begin{pmatrix}b_1 a_1^* & b_2 a_2^* & \cdots & b_1 a_m^*\\ b_2 a_1^* & b_2 a_2^* & \cdots &b_2 a_m^* \\ \vdots & \vdots & \ddots & \vdots \\ b_m a_1^* & b_m a_2^* & \dots & b_m a_m^*\end{pmatrix} \in \mathbb{C}^{m \times m}\end{align}$$

> [!remark]
> - $X = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}$ is NOT in computational basis.
> - $Z = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}$ is NOT in Hadamard basis.
> - $H = \frac{1}{\sqrt{2}}\begin{pmatrix}1 & 1 \\ 1 & -1\end{pmatrix}$ moves from computational basis to Hadamard basis.

## Product State

> [!definition] Product State
> A bipartite state $|\psi \rangle_{AB}$ is said to be a product state if there exists $|\psi_1 \rangle_A$ and $|\psi_2 \rangle_{B}$ such that $|\psi_1 \rangle_A \otimes |\psi_2 \rangle_B$.

## Entangled State

> [!theorem]
> Not all states are product.

> [!definition] Entangled State
> If a quantum state is not a product state, it is **entangled**.

## Mixed State

> [!definition] Mixed States
> Probabilistic distribution over pure states.

> [!definition] Density Matrix of a qubit
> Density matrix of $|\psi \rangle$ is $| \psi \rangle \langle \psi |$.

> [!definition] Mathematical Representation of Mixed State
> Suppose we have a mixed state $((p_1, |\psi_1 \rangle), (p_2, |\psi_2 \rangle), \cdots, (p_k, \psi_{k}))$:
> $$\rho = \sum_{i = 1}^k p_i | \psi_i \rangle \langle \psi_i |$$
