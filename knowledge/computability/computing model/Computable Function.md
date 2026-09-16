- [[Book Reference|Computational Complexity: A Modern Approach]]: - Chapter 1: The computational model —and why it doesn’t matter, Section 1.3: Efficiency and Running Time.
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 4: Space complexity, Section 4.1: Definition of Space-bounded Computation; Section 4.3: NL Completeness.
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 5: The polynomial hierarchy and alternations, Section 5.3: Alternating Turing Machines.
- [[Book Reference|Introduction to the Theory of Computation]]: - Chapter 5: Reducibility, Section 5.3: Mapping Reducibility.

## Definition

> [!definition] Computable Function
> A function $f: \Sigma^* \rightarrow \Sigma^*$ is a computable function if some [[Turing Machine]] $M$, on every input $w$, halts with just $f(x)$ on its tape.

### Running Time

> [!definition] Computing a Function and Running Time
> Let $f: \{0, 1\}^* \rightarrow \{0, 1\}^*$ and let $T: \mathbb{N} \rightarrow \mathbb{N}$ be some functions, and let $M$ be a [[Turing Machine]]. We say that $M$ *computes* $f$ if for every $x \in \{0, 1\}^*$, whenever $M$ is initialized to the start configuration on input $x$, then it halts with $f(x)$ written on its output tape. We say $M$ computes $f$ in $T(n)$-time if its computation on every input $x$ requires at most $T(|x|)$ steps.

> [!remark]
> Often in complexity theory, we include the string $1^k$ in the input to allow a polynomial TM to run in time polynomial in $k$.

### Time-constructible Function

> [!definition] Time-constructible Function
> A function $T: \mathbb{N} \rightarrow \mathbb{N}$ is **time-constructible** if $T(n) \geq n$ and there is a [[Turing Machine]] $M$ that computes the function $x \mapsto \langle T(|x|) \rangle$ in time $T(n)$.

### Space-constructible Function

> [!definition] Space-constructible Function
> A function $S: \mathbb{N} \rightarrow \mathbb{N}$ is **space-constructible** if a [[Turing Machine]] $M$ computes $S(|x|)$ in $O(S(|x|))$ space given $x$ as input.

### Log-space Computable Function

> [!definition] Log-space Computable Function
> Requires:: [[Class L]]
> 
> ---
> A function $f: \{0, 1\}^* \rightarrow \{0, 1\}^*$ is **implicitly log-space computable**, if 
> - $f$ is [[Polynomial]] bounded (i.e., there's some $c$ such that $|f(x)| \leq |x|^c \; \forall \; x \in \{0, 1\}^*$).
> - $\mathcal{L}_f = \{\langle x, i \rangle \mid f(x)_i = 1\} \in \mathsf{L}$.
> - $\mathcal{L}_f' = \{\langle x, i \rangle \mid i \leq |f(x)|\} \in \mathsf{L}$.
