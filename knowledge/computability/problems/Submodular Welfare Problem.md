
> [!definition] Submodular
> A function $f: 2^X \rightarrow \mathbb R$ is monotone if $f(S) \leq f(T)$ whenever $S \subseteq T$. We say that $f$ is *submodular*, if $$f(S \cup T) + f(S \cap T) \leq f(S) + f(T)$$ for any $S, T$.

> [!definition] Submodular Welfare Problem
> Given $m$ items and $n$ players with monotone submodular utility function $w_i: 2^{[m]} \rightarrow \mathbb R_{+}$, we seek a partition of the items into disjoint sets $S_1, \dots, S_n$ in order to maximize $\sum_{i = 1}^n w_i(S_i)$.

> [!definition] Online Submodular Welfare Problem
> The items arrive one by one in a random order.