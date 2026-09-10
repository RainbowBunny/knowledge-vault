Reference:
- [[Book Reference|Introduction to the Theory of Computation]] - Chapter 1: Regular Languages, Section 1.1: Finite Automata.

## Definition

> [!definition] Deterministic Finite Automaton
> Extends:: [[Non-deterministic Finite Automaton]]
> 
> ---
> A Deterministic Finite Automaton is a [[Non-deterministic Finite Automaton]] $M = (Q, \Sigma, \delta, q_0, F)$ with:
> - $\delta: Q \times \Sigma_\varepsilon \rightarrow Q$: The transition function is now a state (Adding determinism).

> [!definition] Deterministic Finite Automata
> A Deterministic Finite Automata $M$ is a 5-tuple $(Q, \Sigma, \delta, q_0, F)$:
> 1. $Q$ is a finite set called the **states**.
> 2. $\Sigma$ is a finite set called the **alphabet**.
> 3. $\delta: Q \times \Sigma \rightarrow Q$ is the **transition function**.
> 4. $q_0 \in Q$ is the **start state**.
> 5. $F \subseteq Q$ is the **set of accept states**.

> [!definition] Finite Automata (Abstract Machine Formulation)
> Instantiates:: [[Abstract Machine|Acceptor]]
> 
> ---
> - Configuration $C$: $Q \times \Sigma^*$.
> - $\mathsf{init}(w)$: $(q_0, w)$.
> - $\mathsf{acc}$: $F \times \{\varepsilon\}$.
> 
> ---
> The reduction rule $\vdash$:
> 
> Suppose $u \in \Sigma, v \in \Sigma^*$, $q_i$ and $q_j$ are states. Then,
> - $(q_i, uv)$ yields $(q_j, v)$ if $\delta(q_i, u) = q_j$.


