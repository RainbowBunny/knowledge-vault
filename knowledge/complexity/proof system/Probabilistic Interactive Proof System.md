Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.1.2: The Class IP: Probabilistic verifier.

## Definition

> [!definition] $k$-round Probabilistic Interactive Proof System
> Generalizes:: [[Deterministic Interactive Proof System]]
> 
> ---
> - Now, the verifier $\mathcal{V}$ is a [[Probabilistic Turing Machine]].
> - (Completeness): Condition $\mathsf{out}_\mathcal{V} \langle \mathcal{V}, \mathcal{P} \rangle (x) = 1$ is replaced by $\Pr[\mathsf{out}_\mathcal{V} \langle \mathcal{V}, \mathcal{P} \rangle (x) = 1] \geq \frac{2}{3}.$
> - (Soundness): Condition $\mathsf{out}_\mathcal{V} \langle \mathcal{V}, \mathcal{P} \rangle (x) = 0$ is replaced by$\Pr[\mathsf{out}_\mathcal{V} \langle \mathcal{V}, \mathcal{P} \rangle (x) = 1] \leq \frac{1}{3}.$
