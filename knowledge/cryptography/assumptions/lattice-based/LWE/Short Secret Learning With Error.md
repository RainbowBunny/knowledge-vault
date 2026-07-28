## Parameters

## Basic Definition

> [!definition] Short-Secret Learning With Error (ss-LWE) Problem
> Let $s \in [-B, B]^n$ and $e \in [-B, B]^m$ where $B \ll q/2$. Given $A \in \mathbb Z_q^{m \times n}$ and $b = As + e \pmod q$. Find $s$.
> Denote an instance of this problem by $(A, b)$ for $\text{ss-LWE}(m, n, q, B)$.

> [!proposition]
> ss-LWE and LWE are equivalent.
> More precisely, $\text{ss-LWE}(m, n, q, B) \leq \text{LWE}(m, n, q, B)$ and $\text{LWE}(m, n, q, B) \leq \text{ss-LWE}(m - n, n, q, B)$.

> [!remark]
> We don't need $m \gg n$ for unique solutions.

### Decisional Version

> [!definition] Decisional Short-Secret Learning With Error (DLWE) Problem
> Let $A \in \mathbb Z_q^{m \times n}, s \in [-B, B]^n, e \in [-B, B]^m$ where $B \ll q/2$, and $b = As + e$. 
> Let $r \in \mathbb Z_q^m$.
> Let $c = b$ with probability $1/2$, and $c = r$ with probability $1/2$.
> Given $(A, c)$, the problem is to decide (with success probability significantly greater than $1/2$) whether $c = b$ or $c = r$.
> Denote an instance of this problem by $(A, c)$ for $\text{DSSLWE}(m, n, q, B)$.
