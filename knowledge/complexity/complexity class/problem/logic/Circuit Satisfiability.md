Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 6: Boolean circuits, Section 6.1.2: Circuit satisfiability and an alternative proof of the Cook-Levin theorem.

## Definition

> [!definition] Circuit Satisfiability
> Reference Name: $\mathsf{CKT} \mbox{-} \mathsf{SAT}$
> 
> ---
> The set of (strings representing) circuits $C$ that produces a single bit of output and have a satisfying assignment.
> 
> ---
> Certificate:
> An assignment $w$ such that $C(w) = 1$.

## Property

> [!lemma]
> Requires:: [[Hardness and Completeness]]
> Hard for:: [[Class NP]] under [[Polynomial-time Karp Reducibility]]
> 
> ---
> $\mathsf{CKT} \mbox{-} \mathsf{SAT}$ is $\mathsf{NP} \mbox{-} \mathsf{hard}$.

> [!lemma]
> Requires: [[3Satisfiability]].
> 
> ---
> $\mathsf{CKT} \mbox{-} \mathsf{SAT} \leq_p \mathsf{3SAT}$.