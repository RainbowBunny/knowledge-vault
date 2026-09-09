Reference:
- [[Book Reference|Introduction to the Theory of Computation]]: - Chapter 3: The Church-Turing Thesis, Exercise 3.4.

## Definition

> [!definition] Enumerator
> An Enumerator is a 6-tuple $(Q, \Sigma, \Gamma, \delta, q_0, q_\mathsf{print})$ where $Q, \Sigma, \Gamma$ are all finite sets:
>1. $Q$ is the set of states,
>2. $\Sigma$ is the output tape alphabet not containing the **blank symbol** $\textvisiblespace$.
>3. $\Gamma$ is the working tape alphabet, where $\textvisiblespace \in \Gamma$ and $\Sigma \subseteq \Gamma$,
>4. $\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R, S\}$ is the transition function, the head is on the working tape.
>5. $q_0 \in Q$ is the start state.
>6. $q_\mathsf{print} \in Q$ is the print state, if the print state is reached, then the string is put on output tape.

> [!remark]
> Different from [[Turing Machine#Decider|Decider Turing Machine]], we usually work with never halt enumerator because the language is usually infinite.

## Property

> [!theorem]
> A [[Language]] is [[Language#Recognizable|Turing-Recognizable]] if and only if some enumerator enumerates it. 