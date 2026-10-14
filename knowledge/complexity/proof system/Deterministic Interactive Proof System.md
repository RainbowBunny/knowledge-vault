Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.1.1: Warmup: Interactive proofs with deterministic verifier and prover.

## Definition

> [!definition] $k$-round Deterministic Interactive Proof System
> We say that a [[Language]] $\mathcal{L}$ has a $k$**-round deterministic interactive proof system** if there's a [[Offline Turing Machine|Turing Machine]] $\mathcal{V}$ that on input $x, a_1, \dots, a_i$ runs in time polynomial in $|x|$, and can have a $k$-round interaction with any function $\mathcal{P}$ such that:
> - (Completeness): $x \in \mathcal{L} \implies \exists \mathcal{P}: \{0, 1\}^* \rightarrow \{0, 1\}^* \; \mathsf{out}_\mathcal{V} \langle \mathcal{V}, \mathcal{P} \rangle (x) = 1.$
> - (Soundness): $x \notin \mathcal{L} \implies \forall \mathcal{P}: \{0, 1\}^* \rightarrow \{0, 1\}^* \; \mathsf{out}_\mathcal{V} \langle \mathcal{V}, \mathcal{P} \rangle (x) = 0.$

### Private Coins

> [!definition] Private Coins Verifier
> The prover functions do not depend upon the verifier's random strings, only on the messages/questions the verifier sends. In other words, the verifier's random string is **private**.

