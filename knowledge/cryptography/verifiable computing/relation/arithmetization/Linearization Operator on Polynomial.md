Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.3.3: Protocol for TQBF: proof of Theorem 8.19.

## Definition

> [!definition] Parameters
> - $n$: Number of variables.
> - $\mathbb{F}$: [[Field]].

> [!definition] Scope
> A [[Multivariate Polynomial]] $p: \{0, 1\}^n \rightarrow \mathbb F$.

> [!scheme] Linearization Operator on Polynomial
> $L_{X_i}(p)(X_1, \dots, X_n) = X_i \cdot p(X_1, \dots, X_{i - 1}, 1, X_{i + 1}, \dots, X_n) + (1 - X_i) \cdot p(X_1, \dots, X_{i - 1}, 0, X_{i + 1}, \dots, X_n)$