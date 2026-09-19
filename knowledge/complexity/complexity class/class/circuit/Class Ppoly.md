Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 6: Boolean circuits, SSection 6.3: Turing Machine that Take Advice.

## Definition

> [!definition] Class P/poly
> Requires:: [[Class SIZE]]
> 
> ---
> $\mathsf{P_{/\mathsf{poly}}} = \cup_c \mathsf{SIZE}(n^c)$

## Property

### Relation to Other Classes

> [!theorem]
> Requires:: [[Class P]]
> 
> ---
> $\mathsf{P} \subseteq \mathsf{P_{/\mathsf{poly}}}$

> [!theorem]
> Requires:: [[Class DTIME with Advice]]
> 
> ---
> $\mathsf{P_{/\mathsf{poly}}} = \cup_{c, d} \mathsf{DTIME}(n^c) / n^d$

### Language in Class

> [!theorem]
> Let $L \subseteq \{0, 1\}^*$ be a unary [[Language]] (i.e., $\mathcal{L} \subseteq \{1^n: n \in \mathbb{N}\}$). Then $\mathcal{L} \in \mathsf{P_{/\mathsf{poly}}}$.
