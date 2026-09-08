Reference:
- [[Book Reference|Introduction to the Theory of Computation]]: - Chapter 3: The Church-Turing Thesis, Section 3.1: Turing Machines.

## Definition

> [!definition] Turing Machine
>  A Turing Machine is a 7-tuple, $(Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject})$, where $Q, \Sigma, \Gamma$ are all finite sets and
> 1. $Q$ is the set of states,
>2. $\Sigma$ is the input alphabet not containing the **blank symbol** $\textvisiblespace$.
>3. $\Gamma$ is the tape alphabet, where $\textvisiblespace \in \Gamma$ and $\Sigma \subseteq \Gamma$,
>4. $\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R\}$ is the transition function,
>5. $q_0 \in Q$ is the start state,
>6. $q_{accept} \in Q$ is the accept state, and
>7. $q_{reject} \in Q$ is the reject state, where $q_{reject} \neq q_{accept}$.

> [!definition] Turing-recognizable
> A language is called **Turing-recognizable** if some Turing machine recognizes it.

> [!definition] Turing-decidable
> A language is called **Turing-decidable** or simply **decidable** if some Turing machine decides it. (Halts on all input)

## Variant


| Variant                                                 | Tapes      | Moves         | Determinism | Simulation Cost |
| ------------------------------------------------------- | ---------- | ------------- | ----------- | --------------- |
| Basic                                                   | 1          | $\{L, R\}$    | det         | -               |
| [[Turing Machine with Stay Option\|Stay Option]]        | 1          | $\{L, R, S\}$ | det         | $\times 2$      |
| [[Multitape Turing Machine\|Multitape]]                 | $k$        | $\{L, R, S\}$ | det         | quadratic       |
| [[Non-Deterministic Turing Machine\|Non-Deterministic]] | 1          | $\{L, R\}$    | nondet      | exponential     |
|                                                         | 1, bounded | $\{L, R\}$    | det         | -               |
