Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.2: Public Coins and AM.

## Definition

> [!definition] Class Arthur-Merlin
> Subset of:: [[Class IP]]
> 
> ---
> For every $k$ the complexity class $\mathsf{AM}[k]$ is defined as the subset of $\mathsf{IP}[k]$ obtained when we restrict the verifier's messages to be random bits, and not allowing it to use any other random bits that are not contained in these messages.
> 
> We denote by $\mathsf{AM}$ the class $\mathsf{AM}[2]$. That is, $\mathsf{AM}$ is the class of [[Language]] with an [[Probabilistic Interactive Proof System]] that consist of the verifier sending a random string, and the prover responding with a message, where the verifier's decision is obtained by applying a deterministic polynomial-time function to the transcript.

## Property

> [!theorem]
> For every $k: \mathbb{N} \rightarrow \mathbb{N}$ with $k(n)$ computable in $\mathsf{poly}(n)$:
> $$\mathsf{AM}[k] \subseteq \mathsf{IP}[k] \subseteq \mathsf{AM}[k + 2]$$