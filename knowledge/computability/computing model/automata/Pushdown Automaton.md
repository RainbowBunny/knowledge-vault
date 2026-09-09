## Definition

>[!definition] Pushdown Automaton
> A **pushdown automaton** is a 6-tuple $(Q, \Sigma, \Gamma, \delta, q_0, F)$ where $Q, \Sigma, \Gamma, F$ are all finite sets, and
>1. $Q$ is the set of states,
>2. $\Sigma$ is the set of input alphabet,
>3. $\Gamma$ is the set of stack alphabet,
>4. $\delta: Q \times \Sigma_\varepsilon \times \Gamma_\varepsilon \rightarrow \mathcal P(Q \times \Gamma_\varepsilon)$ is the transition function.
>5. $q_0 \in Q$ is the start state, and
>6. $F \subseteq Q$ is the set of accept states.
