## Reed-Muller Codes

> [!definition] First Order Reed-Muller codes
> The **(first order) Reed-Muller codes** $\mathcal R(1, m)$ are binary codes defined, for all integers $m \geq 1$, recursively as follows:
> 1. $\mathcal R(1, 1) = \mathbb F_2^2 = \{00, 01, 10, 11\}$;
> 2. For $m \geq 1$, $$\mathcal R(1, m + 1) = \{(u, u): u \in \mathcal R(1, m)\} \cup \{(u, u + 1): u \in \mathcal R(1, m)\}.$$

> [!proposition]
> For $m \geq 1$, the Reed-Muller code $\mathcal R(1, m)$ is a binary $[2^m, m + 1, 2^{m - 1}]$-linear code, in which every codeword except $0$ and $1$ has weight $2^{m - 1}$.

> [!proposition]
> 1. A generator matrix of $\mathcal R(1, 1)$ is $$\begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}$$
> 2. If $G_m$ is a generator matrix for $\mathcal R(1, m)$, then a generator matrix for $\mathcal R(1, m + 1)$ is $$G_{m + 1} = \begin{pmatrix}G_m & G_m \\ 0\cdots 0 & 1\cdots 1\end{pmatrix}$$

> [!proposition]
> The dual code $\mathcal R(1, m)^{\perp}$ is (equivalent to) the extended binary Hamming code $\overline{\text{Ham}(m, 2)}$.

## Higher Order

> [!definition] $r$-th order Reed-Muller codes
> 1. The zeroth order Reed-Muller codes $\mathcal R(0, m)$, for $m \geq 0$, are defined to be the repetitions codes $\{0, 1\}$ of length $2^m$.
> 2. For any $r \geq 2$, the $r$th order Reed-Muller codes $\mathcal R(r, m)$ are defined, for $m \geq r - 1$, recursively by $$\mathcal R(r, m + 1) = \begin{cases}\mathbb F_2^{2^r} &\text{ if } m = r - 1 \\ \{(u, u + v) : u \in \mathcal R(r, m), v \in \mathcal R(r - 1, m)\} &\text{ if } m > r - 1\end{cases}$$

> [!proposition]
> $\mathcal R(r, m)$ is a linear code with parameter $[2^m, \sum_{i = 0}^r \binom{m}{i}, 2^{m - r}]$

## Related

- [[Linear Code]] — the underlying theory
- [[Hamming Quasi-Cyclic]] — HQC's public code is built from concatenated Reed-Muller and Reed-Solomon codes
