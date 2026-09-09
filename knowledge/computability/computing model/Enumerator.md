## Definition

> [!definition] Enumerator
> An Enumerator is a 5-tuple $(Q, \Sigma, \Gamma, \delta, q_0)$ where $Q, \Sigma, \Gamma$ are all finite sets:
>1. $Q$ is the set of states,
>2. $\Sigma$ is the input alphabet not containing the **blank symbol** $\textvisiblespace$.
>3. $\Gamma$ is the tape alphabet, where $\textvisiblespace \in \Gamma$ and $\Sigma \subseteq \Gamma$,
>4. $\delta: Q \times \Gamma^2 \rightarrow Q \times \Gamma^2 \times \{L, R, S\} ^2$ is the transition function.
>5. $q_0 \in Q$ is the start state.

## Property

> [!theorem]
> A [[Language]] is [[Language#Recognizable|Turing-Recognizable]] if and only if some enumerator enumerates it. 