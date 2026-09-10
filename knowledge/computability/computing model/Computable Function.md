- [[Book Reference|Computational Complexity: A Modern Approach]]: - Chapter 1: The computational model —and why it doesn’t matter, Section 1.3: Efficiency and Running Time.
- [[Book Reference|Introduction to the Theory of Computation]]: - Chapter 5: Reducibility, Section 5.3: Mapping Reducibility.

## Definition

> [!definition] Computable Function
> A function $f: \Sigma^* \rightarrow \Sigma^*$ is a computable function if some [[Turing Machine]] $M$, on every input $w$, halts with just $f(x)$ on its tape.

> [!definition] Computing a function and running time
> Let $f: \{0, 1\}^* \rightarrow \{0, 1\}^*$ and let $T: \mathbb{N} \rightarrow \mathbb{N}$ be some functions, and let $M$ be a [[Turing Machine]]. We say that $M$ *computes* $f$ if for every $x \in \{0, 1\}^*$, whenever $M$ is initialized to the start configuration on input $x$, then it halts with $f(x)$ written on its output tape. We say $M$ computes $f$ in $T(n)$-time if its computation on every input $x$ requires at most $T(|x|)$ steps.

