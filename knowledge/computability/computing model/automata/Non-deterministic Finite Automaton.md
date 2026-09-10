Reference:
- [[Book Reference|Introduction to the Theory of Computation]] - Chapter 1: Regular Languages, Section 1.2: Nondeterministic.

## Definition

> [!definition] Non-deterministic Finite Automaton
> A Non-deterministic Finite Automata $M$ is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$:
> 1. $Q$ is a finite set called the **states**.
> 2. $\Sigma$ is a finite set called the **alphabet**.
> 3. $\delta: Q \times \Sigma \rightarrow \mathcal{P}(Q)$ is the **transition function**.
> 4. $q_0 \in Q$ is the **start state**.
> 5. $F \subseteq Q$ is the **set of accept states**.

## Property

> [!theorem]
> Every Nondeterministic Finite Automaton has an equivalent [[Deterministic Finite Automaton]].
> 
> ---

> [!corollary]
> A language is a [[Regular Language]] if and only if some Nondeterministic Finite Automaton recognizes it.
