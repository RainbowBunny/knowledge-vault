## Learning With Error Problem

> [!definition] Learning With Error (LWE) Problem
> Let $s \in \mathbb Z_q^n$ and $e \in [-B, B]^m$ where $B \ll q / 2$. Given $A \in \mathbb Z_q^{n \times m}$ and $b = As + e \pmod q \in \mathbb Z_q^m$, find $s$.
> Denote an instance of this problem by $(A, b)$ for $\text{LWE}(m, n, q, B)$.

> [!definition] Learning With Error (LWE) Problem Distribution Version
> Let $q, n, m, \alpha$ be functions of a parameter $\lambda$. For a secret $s \in \mathbb Z_q^n$, the distribution $A_{q, n, \alpha, s}$ over $\mathbb Z_q^n \times \mathbb Z_q$ is obtained by sampling $a \leftarrow \mathbb Z_q^n$ and an $e \leftarrow \mathcal D_{\mathbb Z, \alpha q}$, and returning $(a, \langle a, s \rangle + e) \in \mathbb Z_q^{n + 1}$. The Learning With Errors problem $\text{LWE}_{q, n, m, \alpha}$ is as follows: For $s \leftarrow \mathbb Z_q^n$, the goal is to distinguish between the distributions: $$D_0(s) = U(\mathbb Z_q^{m \times (n + 1)}) \quad \text{and} \quad D_1(s) = (A_{q, n, \alpha, s})^m.$$
> We say that a $2^{o(\lambda)}$-time algorithm $\mathcal A$ solves $\text{LWE}_{q, n, m, \alpha}$ if it distinguishes $D_0(s)$ and $D_1(s)$ with $2^{-\omega(\lambda)}$ advantage (over the random coins of $\mathcal A$ and the randomness of the samples), with $2^{-\omega(\lambda)}$ probability over the randomness of $s$.

> [!remark] Choosing LWE parameter $B$
> 1. If $B = 0$, then $As = b \pmod q$ can be solved efficiently.
> 2. If $B = (q - 1)/2$, then every $s$ can be the solution. Thus, assume $B < q / 4$.
> 3. **Arora-Ge**: If $B < \mathcal O(\sqrt{n})$, then LWE can be solved in [[Complexity Theory#Sub-exponential|sub-exponential]] time for sufficiently large $m \gg n$.

> [!remark]
> For $m \gg n$, one expects there is a unique LWE solution $(s, e)$.
> Imagine we are placing balls from one space ($s$ space) into another ($e$ space).

> [!remark]
> Regeus worst case to average-case reduction (2005)
> Definition: Let $L \subseteq \mathbb R^n$ be a lattice, and let $1 \leq i \leq n$. The $i^{th}$ successive minimum of $L$ is the smallest real number $\lambda_i(L)$ such that $L$ has $i$ linearly independent vectors, each of length $\leq \lambda_i(L)$.
> Note: $\lambda_1(L) \leq \lambda_2(L) \leq \cdots \leq \lambda_n(L)$.
> If LWE can be efficiently solved on average then $\text{SIVP}_\gamma$ can be efficiently solved in the worst case with a quantum algorithm.
> Corollary: If we believe that $\text{SIVP}_\gamma$ is hard in the worst case, then we must believe that LWE is also hard in the average case.
> Problem This is a highly asymptotic statement.

## Decisional Learning With Error Problem

> [!definition] Decisional Learning With Error (DLWE) Problem
> Let $A \in \mathbb Z_q^{m \times n}, s \in \mathbb Z_q^n, e \in [-B, B]^m$ where $B \ll q/2$, and $b = As + e$. 
> Let $r \in \mathbb Z_q^m$.
> Let $c = b$ with probability $1/2$, and $c = r$ with probability $1/2$.
> Given $(A, c)$, the problem is to decide (with success probability significantly greater than $1/2$) whether $c = b$ or $c = r$.
> Denote an instance of this problem by $(A, c)$ for $\text{DLWE}(m, n, q, B)$.

> [!proposition]
> LWE and DLWE are equivalent.

## Short-Secret Learning With Error Problem

> [!definition] Short-Secret Learning With Error (ss-LWE) Problem
> Let $s \in [-B, B]^n$ and $e \in [-B, B]^m$ where $B \ll q/2$. Given $A \in \mathbb Z_q^{m \times n}$ and $b = As + e \pmod q$. Find $s$.
> Denote an instance of this problem by $(A, b)$ for $\text{ss-LWE}(m, n, q, B)$.

> [!proposition]
> ss-LWE and LWE are equivalent.
> More precisely, $\text{ss-LWE}(m, n, q, B) \leq \text{LWE}(m, n, q, B)$ and $\text{LWE}(m, n, q, B) \leq \text{ss-LWE}(m - n, n, q, B)$.

> [!remark]
> We don't need $m \gg n$ for unique solutions.

## Decisional Short-Secret Learning With Error Problem

> [!definition] Decisional Short-Secret Learning With Error (DLWE) Problem
> Let $A \in \mathbb Z_q^{m \times n}, s \in [-B, B]^n, e \in [-B, B]^m$ where $B \ll q/2$, and $b = As + e$. 
> Let $r \in \mathbb Z_q^m$.
> Let $c = b$ with probability $1/2$, and $c = r$ with probability $1/2$.
> Given $(A, c)$, the problem is to decide (with success probability significantly greater than $1/2$) whether $c = b$ or $c = r$.
> Denote an instance of this problem by $(A, c)$ for $\text{DSSLWE}(m, n, q, B)$.

## Module Learning With Error

> [!definition]
> Module LWE (MLWE) ($k, l, q, n, \eta$) so $R_q = \mathbb Z_q [x] / (x^n + 1)$
Let $A \in_R R^{k \times l}_q, S \in_R R_q^l, e \in_R S_\eta^k$ and $t = As + e \in R^k_q$. Given $(A, t)$, determine $s$.

> [!remark]
> 1. MLWE generalizes LWE (set $n = 1$, get LWE)
> 2. Also, MLWE is a special "structured" version of LWE.
> 3. No one knows any method to solve MLWE that is faster than the best algorithm known for solving LWE.

## Decision Module Learning With Error

> [!definition]
> DMLWE$(k, l, q, n, \eta)$.

## Short Secret Module Learning With Error

## LWE Lattice

$L_A: \{y \in \mathbb Z^m: L y = Az \pmod q \text{ for some } z \in \mathbb Z^n\} \subseteq \mathbb Z^m$.

> [!theorem]
> $L_A$ is a full rank integer lattice of volume $q^{m - n}$

## Bounded Distance Decoding Problem

> [!definition] Bounded Distance Decoding Problem $\text{BDD}_{\alpha}$
> Given $L = L(D) \subseteq \mathbb R^m$ and be $\mathbb R^m$ with the guarantee that is a unique $y \in L$ within distance $\alpha$ of $b$.

Assumption: $\alpha < \lambda_1(L) / \sqrt{2}$
