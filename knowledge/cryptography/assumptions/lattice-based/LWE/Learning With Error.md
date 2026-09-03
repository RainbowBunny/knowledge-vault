## Parameters

> [!definition] Parameters
> - $n$: Number of variables.
> - $m$: Number of equations.
> - $q$: Modulus.
> - $\chi$: Error distribution, usually interval $[-B, \dots, B]$.

## Distribution

> [!definition] Learning With Error Distribution
> ### Distribution
> Sampling Experiment: $\text{LWE}(n, m, q, \chi)$
> 1. $A \xleftarrow{\$} \mathbb Z_q^{m \times n}$
> 2. $s \leftarrow \mathbb Z_q^n$
> 3. $e \leftarrow \chi^m$
> 4. Output $(A, b = As + e)$

> [!remark] Choosing LWE parameter $B$
> 1. If $B = 0$, then $As = b \pmod q$ can be solved efficiently.
> 2. If $B = (q - 1)/2$, then every $s$ can be the solution. Thus, assume $B < q / 4$.
> 3. **Arora-Ge**: If $B < \mathcal O(\sqrt{n})$, then LWE can be solved in [[Complexity Theory#Sub-exponential|sub-exponential]] time for sufficiently large $m \gg n$.

> [!remark]
> For $m \gg n$, one expects there is a unique LWE solution $(s, e)$.
> Imagine we are placing balls from one space ($s$ space) into another ($e$ space).

> [!definition] Learning With Error (LWE) Problem Distribution Version
> Let $q, n, m, \alpha$ be functions of a parameter $\lambda$. For a secret $s \in \mathbb Z_q^n$, the distribution $A_{q, n, \alpha, s}$ over $\mathbb Z_q^n \times \mathbb Z_q$ is obtained by sampling $a \leftarrow \mathbb Z_q^n$ and an $e \leftarrow \mathcal D_{\mathbb Z, \alpha q}$, and returning $(a, \langle a, s \rangle + e) \in \mathbb Z_q^{n + 1}$. The Learning With Errors problem $\text{LWE}_{q, n, m, \alpha}$ is as follows: For $s \leftarrow \mathbb Z_q^n$, the goal is to distinguish between the distributions: $$D_0(s) = U(\mathbb Z_q^{m \times (n + 1)}) \quad \text{and} \quad D_1(s) = (A_{q, n, \alpha, s})^m.$$
> We say that a $2^{o(\lambda)}$-time algorithm $\mathcal A$ solves $\text{LWE}_{q, n, m, \alpha}$ if it distinguishes $D_0(s)$ and $D_1(s)$ with $2^{-\omega(\lambda)}$ advantage (over the random coins of $\mathcal A$ and the randomness of the samples), with $2^{-\omega(\lambda)}$ probability over the randomness of $s$.

## Problem

### Search Variant

> [!definition] Search Learning With Error Problem Advantage
> Reference Name: $\text{SLWE}(n, m, q, \chi)$
> 
> ---
> For any adversary $\mathcal A_\text{search}$, we define the following advantage:
> $$\text{Adv}_\text{LWE}^\text{search}(\mathcal A_\text{search}) = 
> \Pr\!\left[ 
> \begin{array}{l}
> (b - As \bmod q) \in \chi^m
> \end{array} 
> \;\middle |\; 
> \begin{array}{l}
> (A, b) \leftarrow \text{LWE}(n, m, q, \chi) \\
> s \leftarrow \mathcal A_\text{search}(A, b)
> \end{array} \right] 
> $$

### Decision Variant

> [!definition] Decision Learning With Error Problem Advantage
> Reference Name: $\text{DLWE}(n, m, q, \chi)$
> 
> ---
> For any adversary $\mathcal A_\text{decide}$, we define the following advantage:
> $$\text{Adv}^\text{decide}_\text{LWE}(\mathcal A_\text{decide}) = 
> \left|\; \Pr\!\left[
> \begin{array}{l}
> b' = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (A, b) \leftarrow \text{LWE}(n, m, q, \chi) \\
> b' \leftarrow \mathcal A_\text{decide}(A, b)
> \end{array} \right] 
> \;- 
> \Pr\!\left[
> \begin{array}{l}
> b' = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (A, b) \xleftarrow{\$} \mathbb Z_q^{n \times m} \times \mathbb Z_q^n \\
> b' \leftarrow \mathcal A_\text{decide}(A, b)
> \end{array} \right] 
> \right|.
> $$

> [!proposition]
> SLWE and DLWE are equivalent.

## Definition

> [!remark]
> Regeus worst case to average-case reduction (2005)
> Definition: Let $L \subseteq \mathbb R^n$ be a lattice, and let $1 \leq i \leq n$. The $i^{th}$ successive minimum of $L$ is the smallest real number $\lambda_i(L)$ such that $L$ has $i$ linearly independent vectors, each of length $\leq \lambda_i(L)$.
> Note: $\lambda_1(L) \leq \lambda_2(L) \leq \cdots \leq \lambda_n(L)$.
> If LWE can be efficiently solved on average then $\text{SIVP}_\gamma$ can be efficiently solved in the worst case with a quantum algorithm.
> Corollary: If we believe that $\text{SIVP}_\gamma$ is hard in the worst case, then we must believe that LWE is also hard in the average case.
> Problem This is a highly asymptotic statement.

## LWE Lattice

> [!theorem]
> $L_A: \{y \in \mathbb Z^m: L y = Az \pmod q \text{ for some } z \in \mathbb Z^n\} \subseteq \mathbb Z^m$ is a full rank integer lattice of volume $q^{m - n}$.

## Bounded Distance Decoding Problem

> [!definition] Bounded Distance Decoding Problem $\text{BDD}_{\alpha}$
> Given $L = L(D) \subseteq \mathbb R^m$ and be $\mathbb R^m$ with the guarantee that is a unique $y \in L$ within distance $\alpha$ of $b$.

Assumption: $\alpha < \lambda_1(L) / \sqrt{2}$
