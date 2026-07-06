## Convergence

### Convergence in Distribution

> [!definition] Convergence in Distribution
> A sequence of random variables $X_1, X_2, X_3, \dots$ converges **in distribution** to a random variable $X$, shown by $X_n \xrightarrow{d} X$, if $$\lim_{n \rightarrow \infty} F_{X_n}(x) = F(x),$$ for all $x$ at which $F_X(x)$ is continuous.

### Convergence in Probability

> [!definition] Convergence in Probability
> A sequence of random variables $X_1, X_2, X_3, \dots$ converges **in probability** to a random variable $X$, shown by $X_n \xrightarrow{p} X$, if $$\lim_{n \rightarrow \infty} P(|X_n - X| \geq \epsilon) = 0, \forall \epsilon > 0.$$

> [!theorem]
> If $X_n \xrightarrow{d} c$, where $c$ is a constant, then $X_n \xrightarrow{p} c$.

### Convergence in Mean

> [!definition] Convergence in Mean
> Let $r \geq 1$ be a fixed number. A sequence of random variables $X_1, X_2, X_3, \dots$ converges **in the $r$-th mean** or **in the $L^r$ norm** to a random variable $X$, shown by $X_n \xrightarrow{L^r} X$, if $$\lim_{n \rightarrow \infty} E(|X_n - X|^r) = 0.$$
> If $r = 2$, it is called the **mean-square convergence**, and it is shown by $X_n \rightarrow{m.s.} X$.

> [!theorem]
> Let $1 \leq r \leq s$. If $X_n \xrightarrow{L^s} X$, then $X_n \xrightarrow{L^r} X$.

> [!theorem]
> If $X_n \xrightarrow{L^r} X$ for some $r \geq 1$, then $X_n \xrightarrow{p} X$.

### Almost Sure Convergence

> [!definition] Almost Sure Convergence
> A sequence of random variables $X_1, X_2, X_3, \dots$ converges **almost surely** to a random variable $X$, shown by $X_n \xrightarrow{a.s.} X$ if $$P(\{s \in S: \lim_{n \rightarrow \infty} X_n(s) = X(s)\}) = 1$$

> [!theorem]
> Consider the sequence $X_1, X_2, X_3, \dots$. If for all $\epsilon > 0$, we have $$\sum_{i = 1}^\infty P(|X_n - X| > \epsilon) < \infty,$$ then $X_n \xrightarrow{a.s.} X$.

> [!theorem]
> Consider the sequence $X_1, X_2, X_3, \dots$. For any $\epsilon > 0$, define the set of events $$A_m = \{|X_n - X| < \epsilon, \forall n \geq m\}.$$
> Then $X_n \xrightarrow{a.s.} X$ if and only if for any $\epsilon > 0$, we have $$\lim_{m \rightarrow \infty} P(A_m) = 1.$$

> [!remark]
> The Strong Law of Large Numbers ($M_n \xrightarrow{a.s.} \mu$) and the other limit theorems (WLLN, CLT) live in [[Limit Theorems]].

> [!theorem]
> Let $X_1, X_2, X_3, \dots$ be a sequence of random variables. Let also $h: \mathbb R \mapsto \mathbb R$ be a continuous function. Then, the following statements are true:
> 1. If $X_n \xrightarrow{d} X$, then $h(X_n) \xrightarrow{d} h(X)$.
> 2. If $X_n \xrightarrow{p} X$, then $h(X_n) \xrightarrow{p} h(X)$.
> 3. If $X_n \xrightarrow{a.s.} X$, then $h(X_n) \xrightarrow{a.s.} h(X)$.
