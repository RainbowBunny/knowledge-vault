Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 1: The computational model —and why it doesn’t matter, Section 1.5: Uncomputability: An introduction.

## Definition

## Property

> [!theorem]
> There exists a function $\mathsf{UC}: \{0, 1\}^* \rightarrow \{0, 1\}$ that is not computable by any [[Turing Machine]].
> 
> ---
> For every $\alpha \in \{0, 1\}^*$, if $M_\alpha(\alpha) = 1$ ([[Machine Encoding]]), then $\mathsf{UC}(\alpha) = 0$; otherwise $\mathsf{UC}(\alpha) = 1$.
> This function is uncomputable as:
> $$\mathsf{UC}(\langle M \rangle) = M(\langle M \rangle)$$

