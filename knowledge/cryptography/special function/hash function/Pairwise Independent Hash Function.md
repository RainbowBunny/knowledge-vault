Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.2.2: Set lower bound protocol.

## Definition

> [!definition] Pairwise Independent Hash Function
> Let $\mathcal{H}_{n, k}$ be a collection of function from $\{0, 1\}^n$ to $\{0, 1\}^k$. We say that $\mathcal{H}_{n, k}$ is pairwise independent if:
> $$\forall x, x' \in \{0, 1\}^n \text{ with } x \neq x'; \forall y, y' \in \{0, 1\}^k: \Pr_{h \in_R \mathcal{H}_{n, k}}[h(x) = y \land h(x') = y'] = 2^{-2k}.$$

## Property

> [!theorem] Efficient Pairwise Independent Hash Function
> For every $n$, define the collection $\mathcal{H}_{n, n}$ to be $\{h_{a, b}\}_{a, b \in \mathrm{GF}(2^n)}$ where for every $a, b \in \mathrm{GF}(2^n)$, the function $h_{a, b}: \mathrm{GF}(2^n) \rightarrow \mathrm{GF}(2^n)$ maps $x$ to $ax + b$. Then, $\mathcal{H}_{n, n}$ is a collection of pairwise independent hash functions.

