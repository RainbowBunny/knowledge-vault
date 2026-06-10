# Reductions

Reductions are the workhorse of complexity theory: a way to transfer hardness from one problem to another. "$A$ reduces to $B$" means $B$ is at least as hard as $A$.

## Generic Notion

> [!definition] Reduce
> Problem $A$ **reduces** to Problem $B$, written $A \leq B$, if one can efficiently solve $A$ (with non-negligible probability), given an algorithm that efficiently solves $B$ (with non-negligible probability).

## Polynomial-Time Mapping Reductions

> [!definition] Polynomial-Time Reduction
> Language $A$ is **polynomial-time mapping reducible**, or simply **polynomial-time reducible**, to language $B$, written $A \leq_\text{P} B$, if a polynomial-time computable function $f: \Sigma^* \rightarrow \Sigma^*$ exists, where for every $w$, $$w \in A \Longleftrightarrow f(w) \in B.$$
> The function $f$ is called the **polynomial-time reduction** of $A$ to $B$.

> [!theorem] Closure of P under Reduction
> If $A \leq_\text{P} B$ and $B \in \text{P}$, then $A \in \text{P}$.

The same closure property holds for NP, PSPACE, etc. — this is what makes poly-time reductions useful for proving membership in a class via reduction to a known member.

## Log-Space Reductions

For sub-polynomial classes (L, NL), log-space reductions are needed instead of poly-time reductions.

> [!definition] Log-Space Reduction
> Language $A$ is **log-space reducible** to language $B$, written $A \leq_\text{L} B$, if there is a log-space computable function $f: \Sigma^* \to \Sigma^*$ such that for every $w$, $w \in A \Longleftrightarrow f(w) \in B$.

Used to define [[Space Complexity#Class NL-completeness|NL-completeness]].

## Why the Reduction Type Must Match

A reduction is only useful if the reduction itself is *easier* than the target class. Using poly-time reductions to define NL-completeness would be circular (every NL problem trivially reduces to itself in poly time). Log-space reductions resolve this: they're strictly weaker than NL, so a log-space reduction to an NL-complete problem genuinely captures NL hardness.

## Related

- [[Complexity Class]] — the abstract notion that reductions structure
- [[Time Complexity#Class NP-Complete|NP-completeness]] — defined via poly-time reductions
- [[Space Complexity#Class NL-completeness|NL-completeness]] — defined via log-space reductions
- [[Cook-Levin Theorem]] — the founding NP-completeness reduction
