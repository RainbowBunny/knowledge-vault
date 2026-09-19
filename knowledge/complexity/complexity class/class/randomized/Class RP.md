Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 7: Randomized computation, Section 7.3: One-Sided and "Zero-Sided" Error: RP, coRP, ZPP.

## Definition

> [!definition] Class Randomized Polynomial
> Requires:: [[Class RTIME]]
> 
> ---
> $\mathsf{RF} = \cup_{c > 0} \mathsf{RTIME}(n^c)$.

> [!remark]
> This class captures one-sided error algorithms (may output 0 when $x \in \mathcal{L}$ but will never output 1 in $x \notin \mathcal{L}$).

## Property

### Relation to Other Classes

> [!proposition]
> Requires:: [[Class NP]]
> 
> ---
> $\mathsf{RP} \subseteq \mathsf{NP}$ since every accepting branch is a "certificate" that the input is in the [[Language]].

> [!proposition]
> Requires:: [[Class BPP]]
> 
> ---
> $\mathsf{RP} \subseteq \mathsf{BPP}$.