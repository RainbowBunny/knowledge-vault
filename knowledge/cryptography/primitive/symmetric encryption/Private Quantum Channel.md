---
aliases: [PQC]
---
Reference:
- `[MTW00]` — M. Mosca, A. Tapp, R. de Wolf, _Private Quantum Channels and the Cost of Randomizing Quantum Information_, arXiv:quant-ph/0003101 (2000): https://arxiv.org/abs/quant-ph/0003101. Conference version: A. Ambainis, M. Mosca, A. Tapp, R. de Wolf, _Private quantum channels_, FOCS 2000, pp. 547–553.

## Definition

> [!definition] Parameters
> - $n$: the number of qubits of a message; $\mathcal H_{2^n}$: the space of $n$-qubit states. $m \geq n$: the number of qubits once an ancilla is attached.
> - $S \subseteq \mathcal H_{2^n}$: a set of pure $n$-qubit states, the messages.
> - $\mathcal E = \{\sqrt{p_i}\, U_i \mid 1 \leq i \leq N\}$: the superoperator that applies the unitary $U_i$ on $\mathcal H_{2^m}$ with probability $p_i$, where $\sum_i p_i = 1$; so $\mathcal E(\rho) = \sum_i p_i U_i \rho U_i^\dagger$. The index $i$ is the key.
> - $\rho_a$: an $(m - n)$-qubit density matrix, the ancilla. $\rho_0$: an $m$-qubit density matrix.
> - $\tilde I_M = \frac1M I_M$: the totally mixed state of dimension $M$.
>
> `[MTW00 §2.1, Def 3.1]`

> [!definition] Private Quantum Channel
> $[S, \mathcal E, \rho_a, \rho_0]$ is a **private quantum channel** if for every $|\varphi\rangle \in S$
> $$\mathcal E\big(|\varphi\rangle\langle\varphi| \otimes \rho_a\big) = \sum_{i=1}^N p_i\, U_i \big(|\varphi\rangle\langle\varphi| \otimes \rho_a\big) U_i^\dagger = \rho_0.$$
> If $n = m$ (no ancilla), $\rho_a$ is omitted. `[MTW00 Def 3.1]`

> [!remark] Reading it as encryption
> Alice and Bob share the key $i$, drawn with probability $p_i$. Alice attaches $\rho_a$ to $|\varphi\rangle$ and applies $U_i$; Bob, who knows $i$, applies $U_i^\dagger$ and removes the ancilla. Eve does not know $i$, so what she holds is the average $\mathcal E(\cdot)$, and that is the same $\rho_0$ for every message in $S$. The key is classical, and its cost is measured by the entropy $H(p_1, \dots, p_N)$ `[MTW00 §5]`.

## Property

### Key length

> [!theorem] Pauli encryption — $2n$ key bits suffice for $n$ qubits
> If $\mathcal E = \{\frac{1}{\sqrt{2^{2n}}}\, \bar\sigma_x \mid x \in \{0, 1, 2, 3\}^n\}$, with $\bar\sigma_x$ the $n$-qubit [[Pauli Matrices|Pauli operator]], then $[\mathcal H_{2^n}, \mathcal E, \tilde I_{2^n}]$ is a private quantum channel. `[MTW00 Thm 4.1]`
>
> ---
> Applying each $\sigma_i$ with probability $1/4$ to a qubit puts that qubit in the totally mixed state $\tilde I_2$, even if it is entangled with other qubits. Doing so to each of the $n$ qubits takes $2n$ random bits. `[MTW00 proof of Thm 4.1]`

> [!theorem] Lower bound — $2n$ key bits are necessary, even with an ancilla
> If $[\mathcal H_{2^n}, \{\sqrt{p_i}\, U_i \mid 1 \leq i \leq N\}, \rho_a, \rho_0]$ is a private quantum channel, then $H(p_1, \dots, p_N) \geq 2n$, and in particular $N \geq 2^{2n}$. `[MTW00 Cor 5.4]`
>
> ---
> The route: a channel for all $n$-qubit states yields, with the same key, one for $2^{2n}$ classical basis states (Thm 5.2), and a channel for the classical basis states of $m$ qubits needs $H \geq m$ (Thm 5.3). The case with no ancilla and $\rho_0 = \tilde I_{2^n}$ is Thm 5.1; earlier work had the $2n$ bound only without an ancilla. `[MTW00 §1, §5]`

> [!remark] Compared with the one-time pad
> The [[One-time Pad]] hides $n$ classical bits with $n$ key bits. The two theorems above say that a qubit costs exactly two: one for $X$, one for $Z$.

## Related

### Siblings
- [[One-time Pad]] — the classical case
- [[Symmetric Key Encryption]] — the classical primitive; here the key is classical and the message quantum

### Prerequisites
- [[Quantum State#Mixed State]] — density matrices and the totally mixed state
- [[Pauli Matrices]], [[Perfect Security]]
