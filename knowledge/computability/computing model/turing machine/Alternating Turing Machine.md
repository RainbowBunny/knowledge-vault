Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 5: The polynomial hierarchy and alternations, Section 5.3: Alternating Turing Machines

## Definition

> [!definition] Alternating Turing Machine
> Generalizes:: [[Turing Machine]], [[Non-deterministic Turing Machine]]
> 
> ---
> An ATM labels each state as either $\exists$ or $\forall$, and acceptance is defined by induction on the configuration tree:
> - An $\exists$-configuration accepts iff at least one successor accepts.
> - A $\forall$-configuration accepts iff every successor accepts.
> - A halting configuration accepts iff it's in the accept state.

> [!definition] Alternating Time
> For every $T: \mathbb{N} \rightarrow \mathbb{N}$, we say that an [[Alternating Turing Machine]] runs in $T(n)$-time if for every $x \in \{0, 1\}^*$ and for every possible sequence of transition function choices, $M$ halts after at most $T(|x|)$ steps. 
