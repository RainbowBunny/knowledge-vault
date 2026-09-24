## Subfield Codes

### Concatenated Codes

> [!theorem] Concatenated Codes
> Let $A$ be an $[N, K, D]$-linear code over $\mathbb F_{q^m}$. Then there exists an $[nN, mK, d']$-linear code $C$ over $\mathbb F_q$ with $d' = d(C) \geq dD$, provided that there exists an $[n, m, d]$-linear code $B$ over $\mathbb F_q$. Moreover, an $[nN, mK, dD]$-linear code over $\mathbb F_q$ can be obtained.

> [!corollary]
> We have an $[mN, mK, D]$-linear code over $\mathbb F_q$ whenever there is an $[N, K, D]$-linear code over $\mathbb F_{q^m}$.

### Subfield Codes

> [!theorem] Subfield Codes
> Let $C$ be an $[N, K, D]$-linear code over $\mathbb F_q^m$. Then the subfield subcode $C|_{\mathbb F_q} = C \cap \mathbb F_q^N$ is an $[n, k, d]$-linear code over $\mathbb F_q$ with $n = N, k \geq mK - (m - 1)N$ and $d \geq D$. Moreover, an $[N, mK - (m - 1)N, D]$-linear code over $\mathbb F_q$ can be obtained provided that $mK > (m - 1)N$.

### Trace Codes

> [!theorem] Trace Codes
> Let $C$ be an $[N, K, D]$-linear code over $\mathbb F_q^m$. Then the trace code of $C$ defined by $$\text{Tr}_{F_{q^m} / \mathbb F_q} = \{(\text{Tr}_{F_{q^m} / \mathbb F_q}(c_1), \dots, \text{Tr}_{F_{q^m} / \mathbb F_q}(c_n) : (c_1, \dots, c_n) \in C\}$$ is an $[n, k]$-linear code over $\mathbb F_q$ with $n = N$ and $k \leq mK$.

