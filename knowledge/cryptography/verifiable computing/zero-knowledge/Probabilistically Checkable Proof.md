## Definition

> [!definition] Restricted PCP Verifier
> For function $r, q: \mathbb Z^+ \rightarrow \mathbb Z^+$ an $(r, q, a)$-restricted PCP verifier is a probabilistic oracle algorithm $V$ that on input $x \in \{0, 1\}^n$, expects a random string $R \in \{0, 1\}^{r(n)}$ and queries an oracle $\Pi: \mathbb Z^+ \rightarrow \{0, 1\}^{a(n)}$ at most $q(n)$ times and computes a "Boolean verdict" $V^\Pi(x; R) \in \{0, 1\}$.

