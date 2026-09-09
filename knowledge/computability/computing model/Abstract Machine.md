Reference:
- Sipser, *Introduction to the Theory of Computation*, §3.1 — configuration, yields, accepts
- Hopcroft–Motwani–Ullman — instantaneous descriptions and the ⊢ notation
- Eilenberg, *Automata, Languages and Machines* vol. A — acceptor / transducer

> [!remark]
> This abstraction is not a textbook generalization!

## Definition

> [!definition] Abstract Machine
> Extends:: [[Abstract Reduction System]]
> An **abstract machine** over $\Sigma$ is a confluent [[Abstract Reduction System]] $(C, \vdash)$ together with
> - $\mathsf{init} : \Sigma^* \rightarrow C$: the **start configuration** on an input.
> - $\mathsf{halt} \subseteq C$: the **halting configurations**.
>
> $C$ are the **configurations** and $\vdash$ the **step relation**.

### Derived

> [!definition] Run
> A **run** of $M$ on $w$ is a maximal $\vdash$-path starting at $\mathsf{init}(w)$.

> [!definition] Yield
> For two configurations $C_1$ and $C_2$ that $C_1 \vdash C_2$, we say that $C_1$ yields $C_2$.

> [!remark]
> A halting configuration is exactly a [[Abstract Reduction System|Normal Form]] of $\vdash$.

> [!definition] Loop
> A run that revisit a configuration is called a loop.

> [!definition] Halting
> $M$ **halts on** $w$ iff every run on $w$ is finite — i.e. $\vdash$ is [[Abstract Reduction System|Terminating]] on the configurations reachable from $\mathsf{init}(w)$.

> [!definition] Decider
> $m$ is a **decider** iff it halts on every $w$.

## Property

### Deterministic

> [!definition] Deterministic
> $M$ is **deterministic** iff $\vdash$ is a [[Function|Partial Function]] — every configuration has at most one successor.

## Variant

### Acceptor

> [!definition] Acceptor
> A machine is called acceptor if there exists some $\mathsf{acc} \subseteq \mathsf{halt}$ called the acceptance configuration.

> [!definition] Accepts Input
> A Machine $M$ **accepts** input $w$ if $\mathsf{init}(w)$'s normal form is an acceptance configuration.

> [!definition] Language of Acceptor
> [[Language]] of an acceptor $M$ is defined as
> $$\mathcal{L}(M) = \{w \in \Sigma^*: M \text{ accepts } w\}.$$

| machine                                 | $C$                                 | $\mathsf{init}(w)$      | $\mathsf{acc}$                             |
| --------------------------------------- | ----------------------------------- | ----------------------- | ------------------------------------------ |
| [[Deterministic Finite Automaton\|DFA]] | $Q \times \Sigma^*$                 | $(q_0, w)$              | $F \times \{\varepsilon\}$                 |
| NFA                                     | $Q \times \Sigma^*$                 | $(q_0, w)$              | $F \times \{\varepsilon\}$                 |
| PDA                                     | $Q \times \Sigma^* \times \Gamma^*$ | $(q_0, w, \varepsilon)$ | $F \times \{\varepsilon\} \times \Gamma^*$ |
| [[Turing Machine]]                      | $\Gamma^* Q \Gamma^*$               | $q_0 w$                 | $\Gamma^* q_\mathsf{accept} \Gamma^*$      |

### Transducer

## Related

- [[Enumerator]] — **not** an acceptor: no input, and it outputs rather than accepts