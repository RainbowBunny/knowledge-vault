Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.2: Reducibility and NP-completeness.

## Definition

> [!definition] Turing Machine Satisfiability
> Reference name: $\mathsf{TMSAT}$
> 
> ---
> Input:
> - $\alpha$: Encoding of a Turing machine.
> - $x$: Input string of the machine.
> - $1^n$: Witness length (See [[Computable Function]]).
> - $1^t$: The number of running step.
> 
> ---
> Output: Decide whether there exist a witness $w \in \{0, 1\}^n$ such that $M_\alpha$ outputs $1$ on input $\langle x, u \rangle$ within $t$ steps.
> 
> ---
> Certificate: The witness $w$.

## Property

> [!theorem]
> $$\mathsf{TMSAT} \in \mathsf{NP}\mbox{-}\mathsf{complete}$$
> 
> ---
> To be completed.

