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

> [!remark] About Tape
> The Turing machine model use an infinite readable and writable tape as its unlimited memory. The Turing machine uses a head that can move left and right, and the machine can read and write input of the head.

### Computation by Turing Machine

> [!definition] Initial State of the Tape
> The initial state of the Tape when running Turing Machine $M$ on input $w$ by putting $w$ at the beginning of the tape and blank else where.

> [!definition] Configuration
> A configuration of the Turing Machine can be represented by format $u \; q \; v$ where $q$ is a state, $u$ is the string formed by reading from the left most cell to the cell before the head while $v$ is the string formed by reading from the head until the last non-empty symbol.
> - **Starting configuration**: $q_0 \; w$.
> - **Accepting configuration**: $u \; q_\mathsf{accept} \; v$.
> - **Rejecting configuration**: $u \; q_\mathsf{reject} \; v$.
> - **Halting configuration**: Either an **accepting configuration** or **rejecting configuration**.

> [!definition] Yield
> A configuration $C_1$ **yields** configuration $C_2$ if the Turing machine can legally go from $C_1$ to $C_2$ in a single step.
> Formally, suppose $a, b, c \in \Gamma$ and $u, v \in \Gamma^*$ and states $q_i$ and $q_j$. Then,
> - $u a \; q_i \; b v$ yields $u \; q_j \; a c v$ if $\delta(q_i, b) = (q_j, c, L)$.
> - $u a \; q_i \; b v$ yields $u a c \; q_j \; v$ if $\delta(q_i, b) = (q_j, c, R)$.
> 
> Also, there is an edge case on the left-hand end:
> - $q_i \; b v$ yields $q_j \; c v$ if $\delta(q_i, b) = (q_j, c, L)$.
> - $q_i \; b v$ yields $c \; q_j \; v$ if $\delta(q_i, b) = (q_j, c, R)$.

> [!definition] Accepts Input
> A Turing Machine $M$ **accepts** input $w$ if a sequence of configurations $C_1, C_2, \dots, C_k$ exists, where
> 1. $C_1$ is the start configuration of $M$ on input $w$,
> 2. each $C_i$ yields $C_{i + 1}$, and
> 3. $C_k$ is an accepting configuration.

> [!definition] Recognize Language
> The collection of strings that $M$ accepts is **the [[Language]] of $M$**, or **the language recognized by $M$**, denoted $\mathcal{L}(M)$

## Property

### Decider

> [!definition] Loop
> When a Turing machine is started on an input, the machine may **loop** (or never leads to a halting configuration).

> [!definition] Decider
> A **decider** is a Turing machine that halts on all input.

## Variant

| Variant                                                 | Tapes      | Moves         | Determinism | Simulation Cost |
| ------------------------------------------------------- | ---------- | ------------- | ----------- | --------------- |
| Basic                                                   | 1          | $\{L, R\}$    | det         | -               |
| [[Turing Machine with Stay Option\|Stay Option]]        | 1          | $\{L, R, S\}$ | det         | $\times 2$      |
| [[Multitape Turing Machine\|Multitape]]                 | $k$        | $\{L, R, S\}$ | det         | quadratic       |
| [[Non-Deterministic Turing Machine\|Non-Deterministic]] | 1          | $\{L, R\}$    | nondet      | exponential     |
|                                                         | 1, bounded | $\{L, R\}$    | det         | -               |
