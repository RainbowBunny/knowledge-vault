Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 6: Boolean circuits, Section 6.7.1: The classes NC and AC.

## Definition

> [!definition] Class AC
> Generalizes:: [[Class NC]]
> 
> ---
> Now, the gates are allowed to have unbounded fan-in (OR and AND gates can be applied to more than two bits).

## Property

### Relation to Other Classes

> [!proposition]
> Requires:: [[Class NC]]
> 
> ---
> $\mathsf{NC}^i \subseteq \mathsf{AC}^i \subseteq \mathsf{NC}^{i + 1}$.
> 
> ---
> Unbounded but $\mathsf{poly}(n)$ fan-in can be simulated using a tree of ORs/ANDs of depth $O(\log n)$.

