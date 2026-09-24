Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 10: Quantum computation, Section 10.2: Quantum Superposition and Qubits; Section 10.2.1: EPR Paradox.

## Definition

> [!definition] Parity Game
> - The experimenter chooses two random bits $x, y \in_R \{0, 1\}$.
> - He presents $x$ to Alice and $y$ to Bob.
> - Alice and Bob respond with bits $a, b$, respectively.
> - Alice and Bob win if and only if $a \oplus b = x \land y$.

## Property

> [!theorem]
> No strategy used by Alice and Bob can cause them to win with probability more than $\frac{3}{4}$.

> [!theorem]
> There is a quantum strategy for Alice and Bob to win with probability at least $\cos^2(\frac{\pi}{8})$.
> 
> ---
> - Before the game begins, Alice and Bob prepare a two-qubit system in the [[EPR State]] $|00 \rangle + |11 \rangle$.
> - Alice takes the first qubit, and Bob takes the second qubit that have not been **measured**.
> - Alice receives bit $x$, if $x = 1$, then she applies a rotation by $\frac{\pi}{8}$.
> - Bob receives bit $y$, if $y = 1$, then he applies a rotation by $-\frac{\pi}{8}$.
> - Alice and Bob measure their respective qubits as their response $a$ and $b$.

