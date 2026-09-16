Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.1.2: Some space complexity classes; Section 4.3.2: NL = coNL.

## Definition

> [!definition] Class NPSPACE
> Requires:: [[Class NSPACE]]
> 
> ---
> $\mathsf{NPSPACE} = \cup_{c > 0} \mathsf{NSPACE}(n^c)$

## Property

> [!corollary]
> Requires:: [[Complement Class]], [[Class NL]]
> 
> --- 
> For every [[Computable Function|Space Constructible]] $S(n) > \log n$:
> $$\mathsf{NSPACE}(S(n)) = \mathsf{coNSPACE}(S(n))$$
> 
> ---
> Corollary of $\mathsf{NL} = \mathsf{coNL}$.
