Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.6.2: EXP and NEXP

## Definition

> [!definition] Class NEXP
> Requires:: [[Class NTIME]]
> 
> ---
> $\mathsf{EXP} = \cup_{c \geq 1} \mathsf{NTIME}(2^{n^c})$.

## Property

> [!theorem]
> Requires:: [[Class P]], [[Class NP]], [[Class EXP]].
> 
> ---
> If $\mathsf{EXP} \neq \mathsf{NEXP}$, then $\mathsf{P} \neq \mathsf{NP}$.

