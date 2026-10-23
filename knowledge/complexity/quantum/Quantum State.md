Reference:
- https://abgrilo.github.io/viasm/introduction.pdf
- `[dW]` — R. de Wolf, _Quantum Computing: Lecture Notes_, arXiv:1907.09415: https://arxiv.org/abs/1907.09415
- `[Wat]` — J. Watrous, CPSC 519 lecture notes, Lectures 14 and 15: https://cs.uwaterloo.ca/~watrous/QC-notes/QC-notes.14.pdf, https://cs.uwaterloo.ca/~watrous/QC-notes/QC-notes.15.pdf
- `[Pre]` — J. Preskill, _Lecture Notes for Physics 219: Quantum Computation_, Chapter 2: https://preskill.caltech.edu/ph219/chap2_15.pdf

## Definition

> [!definition] Quantum State
> A quantum state is represented by a unit vector in a [[Complex Hilbert Space]].

### Qubit


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

> [!example] Density matrices of the basis states
> $|0\rangle = (1, 0)^T$ and $|1\rangle = (0, 1)^T$ `[dW §1.3]`; $|\pm\rangle = \frac{1}{\sqrt 2}(|0\rangle \pm |1\rangle)$, which are $H|0\rangle$ and $H|1\rangle$ `[dW §1.2.2, §1.4]`. Their density matrices $|\psi\rangle\langle\psi|$:
>
> | state | vector | density matrix |
> | --- | --- | --- |
> | $\vert 0 \rangle$ | $\begin{pmatrix}1 \\ 0\end{pmatrix}$ | $\begin{pmatrix}1 & 0 \\ 0 & 0\end{pmatrix}$ |
> | $\vert 1 \rangle$ | $\begin{pmatrix}0 \\ 1\end{pmatrix}$ | $\begin{pmatrix}0 & 0 \\ 0 & 1\end{pmatrix}$ |
> | $\vert + \rangle$ | $\frac{1}{\sqrt 2}\begin{pmatrix}1 \\ 1\end{pmatrix}$ | $\frac12\begin{pmatrix}1 & 1 \\ 1 & 1\end{pmatrix}$ |
> | $\vert - \rangle$ | $\frac{1}{\sqrt 2}\begin{pmatrix}1 \\ -1\end{pmatrix}$ | $\frac12\begin{pmatrix}1 & -1 \\ -1 & 1\end{pmatrix}$ |
>
> The equal mixtures of $|0\rangle, |1\rangle$ and of $|+\rangle, |-\rangle$ give the same matrix, $\frac12 I$: the *totally mixed state*, which represents complete ignorance about the qubit `[Wat L15]` and can be prepared as an ensemble of pure states in infinitely many ways `[Pre eq. (2.101)]`.

> [!definition] Mathematical Representation of Mixed State
> Suppose we have a mixed state $((p_1, |\psi_1 \rangle), (p_2, |\psi_2 \rangle), \cdots, (p_k, \psi_{k}))$:
> $$\rho = \sum_{i = 1}^k p_i | \psi_i \rangle \langle \psi_i |$$

> [!proposition] Density matrices are the positive semidefinite matrices of trace 1
> Every density matrix has trace $1$ and is positive semidefinite; conversely, any matrix with these two properties is the density matrix of some mixture `[Wat L14]`.

> [!proposition] Measuring a mixed state
> Measuring $\rho$ with operators $\{M_a\}_a$, $\sum_a M_a^\dagger M_a = I$, gives outcome $a$ with probability $\mathrm{Tr}(M_a \rho M_a^\dagger)$ `[Wat L15]`. For the measurement in an orthonormal basis $\{|m\rangle\}$, $M_m = |m\rangle\langle m|$, so for $\rho = \sum_i p_i |\psi_i\rangle\langle\psi_i|$
> $$P(m) = \langle m | \rho | m \rangle = \sum_i p_i\, |\langle m | \psi_i \rangle|^2:$$
> the average, over the mixture, of the pure-state probabilities $|\langle m|\psi_i\rangle|^2$ `[dW §1.2.2]`.
