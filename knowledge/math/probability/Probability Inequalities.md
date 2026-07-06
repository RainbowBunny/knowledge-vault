## Event Inequalities

> [!theorem] The Union Bound
> For any events $A_1, A_2, \dots, A_n$, we have $$P(\cup_{i = 1}^n A_i) \leq \sum_{i = 1}^n P(A_i).$$

> [!theorem] Generalization of the Union Bound: Bonferroni Inequalities
> For any events $A_1, A_2, \dots, A_n$, we have: $$\begin{align}
> P(\cup_{i = 1}^n A_i) &\leq \sum_{i = 1}^n P(A_i); \\
> P(\cup_{i = 1}^n A_i) &\geq \sum_{i = 1}^n P(A_i) - \sum_{i < j} P(A_i \cap A_j) \\
> P(\cup_{i = 1}^n A_i) &\leq \sum_{i = 1}^n P(A_i) - \sum_{i < j} P(A_i \cap A_j) + \sum_{i < j < k} P(A_i \cap A_j \cap A_k).
> \end{align}$$

## Tail Inequalities

> [!theorem] Markov's Inequality
> If $X$ is any nonnegative random variable, then for every $a > 0$: $$P(X \geq a) \leq \frac{E[X]}{a}.$$
> Equivalently, $\Pr[X \geq r \cdot E(X)] \leq \frac{1}{r}$.

> [!remark]
> Markov tell us how to bound extreme value knowing the average.

> [!theorem] Chebyshev's Inequality
> If $X$ is any random variable, then for any $b > 0$ we have $$P(|X - E[X]| \geq b) \leq \frac{\text{Var}(X)}{b^2}.$$

> [!theorem] Chernoff Bounds (MGF Form)
> For any random variable $X$ with MGF $M_X(s)$:
> $$\begin{align}
> P(X \geq a) &\leq e^{-sa} M_X(s), \forall s > 0, \\
> P(X \leq a) &\leq e^{-sa} M_X(s), \forall s < 0
> \end{align}$$

> [!theorem] Chernoff Bound (Bernoulli Sample Mean)
> Let $\{X_i\}_{i \in I}$ be a finite, non-empty, and mutually independent family of random variables, such that each $X_i$ is $1$ with probability $p$ and $0$ with probability $q := 1 - p$. Assume that $0 < p < 1$. Also, let $n := |I|$ and $\overline{X}$ be the sample mean of $\{X_i\}_{i \in I}$. Then for every $\varepsilon > 0$, we have:
> - $\Pr[\overline{X} - p \ge \epsilon] \le \exp(-n\epsilon^2/2q)$
> - $\Pr[\overline{X} - p \le -\epsilon] \le \exp(-n\epsilon^2/2p)$
> - $\Pr[|\overline{X} - p \ge \epsilon|] \le 2\exp(-n\epsilon^2/2)$

> [!theorem] Hoefding Inequality
> Let $X_1, X_2, \dots, X_n$ be $n$ independent random variables with the same probability distribution, each ranging over the (real) interval $[a, b]$, and let $\mu$ denote the expected value of each of these variables. Then, for every $\epsilon > 0$, 
> $$\Pr[|\frac{\sum_{i = 1}^n X_i}{n} - \mu| > \epsilon] < 2 \cdot e^{-\frac{2 \epsilon^2}{(b - a^2)} n}$$

## Expectation Inequalities

> [!theorem] Cauchy-Schwarz Inequality
> For any two random variables $X$ and $Y$, we have $$E[XY] \leq \sqrt{E[X^2] E[Y^2]},$$ where equality holds if and only if $X = \alpha Y$, for some constant $\alpha \in \mathbb R$.

## Application

- [[Limit Theorems]] — Chebyshev proves the WLLN.
- [[Statistical Distance]] — union bound and tail bounds drive hybrid and failure-probability arguments in cryptography.
