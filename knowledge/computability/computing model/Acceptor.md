Reference:
- Sipser, *Introduction to the Theory of Computation*, §3.1 — configuration, yields, accepts
- Hopcroft–Motwani–Ullman — instantaneous descriptions and the ⊢ notation
- Eilenberg, *Automata, Languages and Machines* vol. A — acceptor / transducer

## Definition

> [!definition] Acceptor
> Extends:: [[Abstract Reduction System]]
> An **acceptor** over $\Sigma$ is an [[Abstract Reduction System]] $(C, \vdash)$ together with
> - $\mathrm{init} : \Sigma^* \rightarrow C$, the **start configuration** on an input, and
> - $\mathrm{Acc} \subseteq C$, the **accepting configurations**.
>
> $C$ are the **configurations** and $\vdash$ the **step relation**.

### Derived

> [!definition] Run, Accepts, Language
> - A **run** of $M$ on $w$ is a maximal $\vdash$-path starting at $\mathrm{init}(w)$.
> - $M$ **accepts** $w$ iff $\mathrm{init}(w) \vdash^{*} c$ for some $c \in \mathrm{Acc}$.
> - The **language of $M$** is $\mathcal L(M) := \{w \in \Sigma^* : M \text{ accepts } w\}$.

> [!remark]
> Acceptance is **reachability**: $w \in \mathcal L(M)$ iff $\mathrm{Acc}$ is reachable from $\mathrm{init}(w)$
> in the directed graph $(C, \vdash)$. A halted configuration is exactly a
> [[Abstract Reduction System|Normal Form]] of $\vdash$.

## Property

> [!definition] Deterministic
> $M$ is **deterministic** iff $\vdash$ is a partial function — every configuration has at most one successor.

> [!definition] Loop, Halting, Decider
> - $M$ might run forever or **loop** on an input $w$.
> - $M$ **halts on** $w$ iff every run on $w$ is finite — i.e. $\vdash$ is [[Abstract Reduction System|Terminating]] on the
> configurations reachable from $\mathrm{init}(w)$. 
> - $M$ is a **decider** iff it halts on every $w$.

> [!remark] 


## Variant

| machine                                 | $C$                                 | $\mathrm{init}(w)$      | $\mathrm{Acc}$                             |
| --------------------------------------- | ----------------------------------- | ----------------------- | ------------------------------------------ |
| [[Deterministic Finite Automaton\|DFA]] | $Q \times \Sigma^*$                 | $(q_0, w)$              | $F \times \{\varepsilon\}$                 |
| NFA                                     | $Q \times \Sigma^*$                 | $(q_0, w)$              | $F \times \{\varepsilon\}$                 |
| PDA                                     | $Q \times \Sigma^* \times \Gamma^*$ | $(q_0, w, \varepsilon)$ | $F \times \{\varepsilon\} \times \Gamma^*$ |
| [[Turing Machine]]                      | $\Gamma^* Q \Gamma^*$               | $q_0 w$                 | $\Gamma^* q_\mathsf{accept} \Gamma^*$      |

> [!remark] What $\mathrm{Acc}$ is doing
> A DFA must **consume the whole input** to accept; a Turing machine need not. That difference is not
> visible in the framework — it is encoded in the shape of $\mathrm{Acc}$. The abstraction *records* the
> difference rather than explaining it.

## Related

- [[Enumerator]] — **not** an acceptor: no input, and it outputs rather than accepts