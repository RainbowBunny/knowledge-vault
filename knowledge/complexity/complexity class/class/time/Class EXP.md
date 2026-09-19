Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.1.1: Relation between NP and P.
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 6: Boolean circuits, Section 6.4: P/poly and NP.

## Definition

> [!definition] Class EXPonential
> Requires:: [[Class DTIME]]
> 
> ---
> $\mathsf{EXP} = \cup_{c \geq 1} \mathsf{DTIME}(2^{n^c})$.

## Property

### Relation to Other Classes

> [!theorem] Meyer's Theorem
> Requires:: [[Class Ppoly]], [[Level Polynomial Hierarchy]]
> 
> ---
> If $\mathsf{EXP} \subseteq \mathsf{P_{/\mathsf{poly}}}$, then $\mathsf{EXP} = \Sigma_2^p$.