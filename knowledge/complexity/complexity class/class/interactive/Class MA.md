Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.2: Public Coins and AM.

## Definition

> [!definition] Class Merlin-Arthur
> The class $\mathsf{MA}$ denotes the class of [[Language]] with a two-round public-coin [[Deterministic Interactive Proof System]] with the prover sending the first message. That is, $\mathcal{L} \in \mathsf{MA}$ if there's a proof system for $\mathcal{L}$ that consists of the prover first sending a message, and then the verifier tossing coins and computing its decision by doing a deterministic polynomial-time computation involving the input, the prover's message and the coins.

