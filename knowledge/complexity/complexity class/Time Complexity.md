# Time Complexity

The canonical resource bound: how many steps does a Turing machine take?

## Time Complexity

> [!definition] Nondeterministic Time Complexity
> Let $N$ be a nondeterministic Turing machine that is a decider. The **running time** of $N$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the maximum number of steps that $N$ uses on any branch of its computation on any input of length $n$.


## Class Non-Uniform Polynomial

Reference: [[Book Reference#Foundation of Cryptography Volume I Basic Tools|Foundation of Cryptography Volume I Basic Tools]]

> [!theorem]
> $\text{BPP} \subseteq \text{P/poly}$


## Sub-Exponential

> [!definition] Sub-Exponential
> A function $f(x)$ is **sub-exponential** if:
> 1. $f(x) = \Omega((\ln x)^\alpha)$ for some $\alpha > 0$.
> 2. $f(x) = \mathcal O(x^\beta)$ for every $\beta > 0$.

Sub-exponential functions sit strictly between polynomial and exponential. Used in cryptography (e.g., $L_n[1/3, c]$ notation for the [[Index Calculus|index-calculus]] running time).

## Related

- [[Space Complexity]] — the other canonical resource bound
- [[Reductions]] — how NP-completeness is defined
- [[Hierarchy Theorems]] — why P $\subset$ EXPTIME
- [[Randomized Complexity]] — what changes with random coins
- [[P vs NP]] — the famous open problem
