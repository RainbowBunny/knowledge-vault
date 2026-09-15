Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 2: NP and NP completeness, Section 2.3.2: The Cook-Levin Theorem.

## Definition

> [!definition] Boolean Formula
> A boolean formula over the variable $u_1, \dots, u_n$ consists of the variables and the logical operators $\land, \lor, \lnot$.

> [!definition] SAT
> $\mathsf{SAT} = \{\varphi | \varphi \; \text{is in CNF form} \land \exists w: \varphi(w) = 1\}$

## Property

> [!theorem] Cook-Levin Theorem
> Requires:: [[Class NP-complete]]
> 
> ---
> $\mathsf{SAT} \in \mathsf{NP}\mbox{-}\mathsf{complete}$