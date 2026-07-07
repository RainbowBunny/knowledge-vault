# Interactive Proofs

Replace the deterministic verifier of NP with a probabilistic, interactive one. The verifier exchanges messages with a (possibly cheating) prover and decides at the end.

## Verifier and Prover

> [!definition] Verifier
> The **verifier** is a function $V$ that computes its next transmission to the prover from the message history sent so far. The function $V$ has three inputs:
> 1. **Input string**: the objective is to determine whether this string is a member of some language.
> 2. **Random input**: a string of random coin flips.
> 3. **Partial message history**: the function has no memory of the dialog so far, so we provide the memory externally via a string representing the exchange of messages up to the present point. We use the notation $m_1\#m_2\#\cdots\#m_i$ to represent the exchange of messages $m_1$ through $m_i$.
>
> Form $V: \Sigma^* \times \Sigma^* \times \Sigma^* \rightarrow \Sigma^* \cup \{\text{accept}, \text{reject}\}$.

> [!definition] Prover
> The **prover** is a function $P$ with two inputs:
> 1. **Input string**
> 2. **Partial message history**
>
> Form $P: \Sigma^* \times \Sigma^* \rightarrow \Sigma^*$.

> [!definition] Interaction
> For particular strings $w$ and $r$, we write $(V \leftrightarrow P)(w, r) = \text{accept}$ if a message sequence $m_1, \ldots, m_k$ exists for some $k$ whereby
> 1. for $0 \leq i < k$, where $i$ is even, $V(w, r, m_1\#\cdots\#m_i) = m_{i+1}$;
> 2. for $0 < i < k$, where $i$ is odd, $P(w, m_1\#\cdots\#m_i) = m_{i+1}$;
> 3. the final message $m_k$ in the message history is $\text{accept}$.

## Class IP

[[Book Reference#Introduction to the Theory of Computation|Introduction to the Theory of Computation]]

> [!definition] Class IP
> Language $A$ is in $\text{IP}$ if some polynomial-time computable function $V$ exists such that for some (arbitrary) function $P$ and for every (arbitrary) function $\tilde P$ and for every string $w$:
> 1. $w \in A$ implies $\Pr[V \leftrightarrow P \text{ accepts } w] \geq \frac{2}{3}$ (completeness), and
> 2. $w \notin A$ implies $\Pr[V \leftrightarrow \tilde P \text{ accepts } w] \leq \frac{1}{3}$ (soundness).

> [!theorem] Shamir's Theorem
> $$\text{IP} = \text{PSPACE}.$$

A striking equality: interaction plus randomness is *exactly* as powerful as polynomial space.

## Related Classes

- $\text{MA}$ (Merlin-Arthur) — one-round IP: prover sends one message, verifier checks probabilistically.
- $\text{AM}$ (Arthur-Merlin) — verifier sends random challenge first, prover responds.
- $\text{NIP}$ — interactive proofs with public coins.
- $\text{PCP}$ — probabilistically checkable proofs (a transformation of IP into static proofs).

## Related

- [[Oracle Machines]] — relativization
- [[Polynomial Hierarchy]] — MA, AM sit inside PH
- [[Randomized Complexity]] — IP uses randomized verification
- [[Proof System|Zero-knowledge IP]] — the cryptographic specialization (in `cryptography/zero-knowledge/`)
- [[Space Complexity]] — IP = PSPACE
