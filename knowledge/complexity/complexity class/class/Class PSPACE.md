Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.1.2: Some space complexity classes; Section 4.2.1: Savitch's Theorem.

## Definition

> [!definition] Class PSPACE
> Requires:: [[Class SPACE]]
> 
> ---
> $\mathsf{PSPACE} = \cup_{c > 0} \mathsf{SPACE}(n^c)$

## Property

> [!theorem] Savitch's Theorem
> Requires:: [[Class SPACE]]
> 
> ---
> For any [[Computable Function|Space-Constructible]] $S: \mathbb{N} \rightarrow \mathbb{N}$ with $S(n) \geq \log n$, 
> $$\mathsf{NSPACE}(S(n)) \subseteq \mathsf{SPACE}(S(n)^2).$$
