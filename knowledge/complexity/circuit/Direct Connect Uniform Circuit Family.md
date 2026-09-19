Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 6: Boolean circuits, Section 6.1: Boolean Circuits and P/poly; Section 6.8: Circuits of Exponential Size.

## Basic Definition

> [!definition] Direct Connect Uniform Family
> Generalizes:: [[Circuit Family]]
> 
> ---
> Let $\{\mathcal{C}_n\}_{n \geq 1}$ be a [[Circuit Family]]. We say that it is a **Direct Connect uniform (DC uniform)** family if there is a polynomial-time algorithm that, given $\langle n, i \rangle$, can compute in polynomial time the $i$-th bit of (the adjacency matrix representation of the circuit $C_n$).
> 
> 

> [!definition] Direct Connect Uniform Family (Alternative)
> Alternatively, a family $\{C_n\}_{n \in \mathbb{N}}$ is DC uniform iff the functions $\mathsf{SIZE}$, $\mathsf{TYPE}$, and $\mathsf{EDGE}$ are computable in polynomial time.
> 
> Note that the circuit might be exponential size, its only requirement is a succinct representation.


   


