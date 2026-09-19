Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.1.2: Some space complexity classes; Section 4.3: NL Completeness.

## Definition

> [!definition] Class deterministic Logarithm space
> Requires:: [[Class SPACE]]
> 
> ---
> $\mathsf{L} = \mathsf{SPACE}(\log{n})$

## Property

### Language in Class

> [!lemma]
> Requires:: [[Log-space Reducibility]]
> 
> ---
> $\mathcal{B} \leq_l \mathcal{C} \land \mathcal{C} \in \mathsf{L} \implies \mathcal{B} \in \mathsf{L}$.