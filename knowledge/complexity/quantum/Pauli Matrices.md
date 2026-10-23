Reference:
- `[MTW00]` — M. Mosca, A. Tapp, R. de Wolf, _Private Quantum Channels and the Cost of Randomizing Quantum Information_, arXiv:quant-ph/0003101 (2000): https://arxiv.org/abs/quant-ph/0003101. Conference version: A. Ambainis, M. Mosca, A. Tapp, R. de Wolf, _Private quantum channels_, FOCS 2000, pp. 547–553.
- `[Pre]` — J. Preskill, _Lecture Notes for Physics 219: Quantum Computation_, Chapter 2: https://preskill.caltech.edu/ph219/chap2_15.pdf
- `[dW]` — R. de Wolf, _Quantum Computing: Lecture Notes_, arXiv:1907.09415: https://arxiv.org/abs/1907.09415

## Definition

> [!definition] Pauli Matrices
> $$\sigma_0 = I = \begin{pmatrix}1 & 0 \\ 0 & 1\end{pmatrix}, \quad \sigma_1 = X = \begin{pmatrix}0 & 1 \\ 1 & 0\end{pmatrix}, \quad \sigma_2 = Y = \begin{pmatrix}0 & -i \\ i & 0\end{pmatrix}, \quad \sigma_3 = Z = \begin{pmatrix}1 & 0 \\ 0 & -1\end{pmatrix}.$$
> They are unitary `[MTW00 §2.1]`. For $x = (x_1, \dots, x_n) \in \{0, 1, 2, 3\}^n$, the $n$-qubit Pauli operator is $\bar\sigma_x = \sigma_{x_1} \otimes \cdots \otimes \sigma_{x_n}$ `[MTW00 §4]`.

## Property

> [!proposition] Anticommuting square roots of the identity
> For $k, \ell \in \{1, 2, 3\}$: $\sigma_k \sigma_\ell + \sigma_\ell \sigma_k = 2 \delta_{k\ell} I$ `[Pre eq. (2.30)]`. So each of $X, Y, Z$ squares to $I$, two different ones anticommute ($XZ = -ZX$), and each is traceless `[Pre §2.3.2]`. Multiplying out, $Y = iXZ$.

> [!remark] Bit flip and phase flip
> $X$, the *bitflip* or NOT gate, swaps $|0\rangle$ and $|1\rangle$; $Z$, the *phaseflip*, puts a $-$ in front of $|1\rangle$ `[dW §1.4]`. The Hadamard gate exchanges the two: $HXH = Z$ `[dW Ch. 1, Exercise 3]`. Hence on the Hadamard basis $Z$ acts as a bit flip: $Z|+\rangle = |-\rangle$ and $Z|-\rangle = |+\rangle$.

## Related

### Used by
- [[Private Quantum Channel]] — a uniformly random $\bar\sigma_x$ hides every $n$-qubit state `[MTW00 Thm 4.1]`

### Prerequisites
- [[Quantum State]], [[Quantum Bit]]
