Reference:
- [[Book Reference|Introduction to the Theory of Computation]]: - Chapter 3: The Church-Turing Thesis, Section 3.1: Turing Machines.

## Definition

> [!definition] Turing Machine
>  A **Turing Machine** is a 7-tuple, $M = (Q, \Sigma, \Gamma, \delta, q_0, q_\mathsf{accept}, q_\mathsf{reject})$, where $Q, \Sigma, \Gamma$ are all finite sets and
> 1. $Q$ is the set of states,
>2. $\Sigma$ is the input alphabet not containing the **blank symbol** $\textvisiblespace$.
>3. $\Gamma$ is the tape alphabet, where $\textvisiblespace \in \Gamma$ and $\Sigma \subseteq \Gamma$,
>4. $\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R\}$ is the transition function,
>5. $q_0 \in Q$ is the start state,
>6. $q_\mathsf{accept} \in Q$ is the accept state, and
>7. $q_\mathsf{reject} \in Q$ is the reject state, where $q_\mathsf{reject} \neq q_\mathsf{accept}$.

> [!definition] Turing Machine (Abstract Machine Formulation)
> Instantiates:: [[Abstract Machine|Acceptor]]
> 
> ---
> - Configuration $C$: $\Sigma^* Q \Sigma^*$.
> - $\mathsf{init}(w)$: $q_0 w$.
> - $\mathsf{acc}$: $\Gamma^* q_\mathsf{accept} \Gamma^*$.
> 
> ---
> The reduction rule $\vdash$:
> 
> Suppose $a, b, c \in \Gamma$ and $u, v \in \Gamma^*$, states $q_i$ and $q_j$ are states. Then,
> - $u a \; q_i \; b v$ yields $u \; q_j \; a c v$ if $\delta(q_i, b) = (q_j, c, L)$.
> - $u a \; q_i \; b v$ yields $u a c \; q_j \; v$ if $\delta(q_i, b) = (q_j, c, R)$.
> 
> Also, there is an edge case on the left-hand end:
> - $q_i \; b v$ yields $q_j \; c v$ if $\delta(q_i, b) = (q_j, c, L)$.
> - $q_i \; b v$ yields $c \; q_j \; v$ if $\delta(q_i, b) = (q_j, c, R)$.

> [!remark] About Tape
> The Turing machine model use an infinite readable and writable tape as its unlimited memory. The Turing machine uses a head that can move left and right, and the machine can read and write input of the head.

## Variant

| Variant                                                 | Tapes      | Moves         | Determinism | Simulation Cost |
| ------------------------------------------------------- | ---------- | ------------- | ----------- | --------------- |
| Basic                                                   | 1          | $\{L, R\}$    | det         | -               |
| [[Turing Machine with Stay Option\|Stay Option]]        | 1          | $\{L, R, S\}$ | det         | $\times 2$      |
| [[Multitape Turing Machine\|Multitape]]                 | $k$        | $\{L, R, S\}$ | det         | quadratic       |
| [[Non-deterministic Turing Machine\|Non-Deterministic]] | 1          | $\{L, R\}$    | nondet      | exponential     |
|                                                         | 1, bounded | $\{L, R\}$    | det         | -               |
