Reference:
- [[Book Reference|Introduction to the Theory of Computation]] - Chapter 1: Regular Languages, Section 1.3: Regular Expressions.

## Definition

> [!definition] Generalized Nondeterministic Finite Automaton
> Extends:: [[Non-deterministic Finite Automaton]]
> 
> ---
> A Generalized Nondeterministic Finite Automaton $M$ is a [[Non-deterministic Finite Automaton]] $(Q, \Sigma, \delta, q_{start}, q_{accept})$, with:
> - $\delta: (Q - \{q_{accept}\}) \times (Q - \{q_{start}\}) \rightarrow \mathcal{R}(\Sigma)$: The transition function is now defined between two states and $\mathcal{R}(\Sigma)$ is the set of [[Regular Expression]].
> - $q_\mathsf{start}$ ($q_0$ renamed).
> - $q_\mathsf{accept}$: The set of accept states is now only one state.
