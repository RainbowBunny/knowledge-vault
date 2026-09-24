Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.1.2: Some space complexity classes; Section 4.2.1: Savitch's Theorem.

## Definition

> [!definition] Class Polynomial SPACE
> Requires:: [[Class SPACE]]
> 
> ---
> $\mathsf{PSPACE} = \cup_{c > 0} \mathsf{SPACE}(n^c)$

## Property

### Relation to Other Classes

> [!theorem]
> Requires:: [[Class Ppoly]], [[Class MA]].
> 
> ---
> $\mathsf{PSPACE} \subseteq \mathsf{P_{/\mathsf{poly}}} \implies \mathsf{PSPACE} = \mathsf{MA}$.
> 
> ---
> The prover can just give the polynomial circuit size to the verifier.

