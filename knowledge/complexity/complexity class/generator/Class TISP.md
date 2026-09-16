Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 5: The polynomial hierarchy and alternations, Section 5.4: Time Versus Alternations: Time-Space Tradeoffs for SAT

## Definition

> [!definition] Class TISP
> For every two functions $S, T: \mathbb{N} \rightarrow \mathbb{N}$, define $\mathsf{TISP}(T(n), S(n))$ to be the set of languages decided by a [[Offline Turing Machine|Turing Machine]] $M$ that on every input $x$ takes at most $O(T(|x|))$ steps and uses at most $O(S(|x|))$ cells of its read-write tapes.

## Property

> [!theorem] Time/Space Tradeoff for SAT
> Requires:: [[Satisfiability]]
> 
> ---
> $\mathsf{SAT} \notin \mathsf{TISP}(n^{1.1}, n^{0.1})$