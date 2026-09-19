Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.3.2: The Cook-Levin Theorem.

## Definition

> [!definition] 3SAT
> $\mathsf{3SAT} = \{\varphi \; | \; \varphi \; \text{is in 3CNF form} \land \exists w: \varphi(w) = 1\}$

## Property

> [!theorem] Cook-Levin Theorem
> Complete for:: [[Class NP]] under [[Polynomial-time Karp Reducibility]]
> 
> ---
> $\mathsf{3SAT} \in \mathsf{NP}\mbox{-}\mathsf{complete}$