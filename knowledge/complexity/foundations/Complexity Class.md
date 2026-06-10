## Efficient Algorithm

> [!definition] Efficient Algorithm
> Let $A$ be an algorithm (possibly probabilistic) that takes as input a security parameter $\lambda \in \mathbb Z_{\geq 1}$, as well as other parameters encoded as a bit string $x \in \{0, 1\}^{p(\lambda)}$ for some fixed polynomial $p$. We call $A$ an **efficient algorithm** if there exist a poly-bounded function $t$ and a negligible function $\epsilon$ such that for all $\lambda \in \mathbb Z_{\geq 1}$, and all $x \in \{0, 1\}^{\leq p(\lambda)}$, the probability that the running time of $A$ on input $(\lambda, x)$ exceeds $t(\lambda)$ is at most $\epsilon(\lambda)$.

> [!definition] Polynomial-time Computable Function
> A function $f: \Sigma^{*} \rightarrow \Sigma^{*}$ is a **polynomial-time computable function** if some polynomial-time Turing machine $M$ exists that halts with just $f(w)$ on its tape, when started on any input $w$.

## Complexity Relationships Among Models

> [!theorem]
> Let $t(n)$ be a function, where $t(n) \geq n$. Then every $t(n)$-time multitape Turing machine has an equivalent $O(t^2(n))$-time single-tape Turing machine.

## Class Inclusions

The standard inclusion lattice among the major classes:

$$\text{P} \subseteq \text{NP} \subseteq \text{PSPACE} = \text{NPSPACE} = \text{IP} \subseteq \text{EXPTIME}$$
$$\text{NL} \subset \text{PSPACE} \subset \text{EXPSPACE}$$
$$\text{P} \subset \text{EXPTIME}$$

Strict inclusions follow from the [[Hierarchy Theorems|time and space hierarchy theorems]]; equalities like $\text{PSPACE} = \text{NPSPACE}$ follow from [[Space Complexity#Savitch's Theorem|Savitch's theorem]] and $\text{IP} = \text{PSPACE}$ from Shamir's theorem (see [[Interactive Proofs]]).

## Related

- [[Reductions]] — poly-time and log-space mapping reductions, the structural relations among classes
- [[Hierarchy Theorems]] — proofs that more resources yield strictly more computational power
- [[Time Complexity]] / [[Space Complexity]] — the canonical resource bounds
- [[Randomized Complexity]] — what changes when the machine has access to random coins
