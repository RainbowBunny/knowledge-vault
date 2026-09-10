Reference:
- [[Book Reference|Introduction to the Theory of Computation]] - Chapter 1: Regular Languages, Section 1.2: Nondeterministic.

## Definition

> [!definition] Nondeterministic Finite Automaton
> Generalizes:: [[Deterministic Finite Automaton]].
> 
> ---
> A Nondeterministic Finite Automaton is a [[Deterministic Finite Automaton]] $M = (Q, \Sigma, \delta, q_0, F)$ with:
> - $\delta: Q \times \Sigma_\varepsilon \rightarrow \mathcal P(Q)$: The transition function is now a power set on $Q$ instead of a deterministic state.

## Property

> [!theorem]
> Every Nondeterministic Finite Automaton has an equivalent [[Deterministic Finite Automaton]].
> 
> ---

> [!corollary]
> A language is a [[Regular Language]] if and only if some Nondeterministic Finite Automaton recognizes it.
