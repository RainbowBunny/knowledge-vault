Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 7: Randomized computation, Section 7.3: One-Sided and "Zero-Sided" Error: RP, coRP, ZPP.

## Definition

> [!definition] Class complement Randomized Polynomial
> Requires:: [[Class RP]]
> 
> ---
> $\mathsf{coRP} = \{\mathcal{L} \mid \overline{\mathcal{L}} \in \mathsf{RP}\}$.

> [!remark]
> This class captures one-sided error algorithms (may output 1 when $x \notin \mathcal{L}$ but will never output 0 in $x \in \mathcal{L}$).

## Property

### Relation to Other Classes

> [!proposition]
> Requires:: [[Class BPP]]
> 
> ---
> $\mathsf{coRP} \subseteq \mathsf{BPP}$.

