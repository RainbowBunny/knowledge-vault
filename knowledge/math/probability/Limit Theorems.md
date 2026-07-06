## Sample Mean

> [!definition] Sample Mean
> For i.i.d. random variables $X_1, X_2, \dots, X_n$, the **sample mean**, denoted by $\overline{X}$, is defined as $$\overline{X} = \frac{X_1 + X_2 + \dots + X_n}{n}.$$
> Another common notation for the sample mean is $M_n$. If the $X_i$'s have CDF $F_X(x)$, we might show the sample mean by $M_n(X)$ to indicate the distribution of the $X_i$'s.

> [!remark]
> - $E[\overline{X}] = E[X]$.
> - $\text{Var}(\overline{X}) = \frac{\text{Var}(X)}{n}$.

## Laws of Large Numbers

> [!theorem] Weak Law of Large Numbers (WLLN)
> Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with a finite expected value $E[X_i] = \mu < \infty$. Then, for any $\epsilon > 0$, $$\lim_{n \rightarrow \infty} P(|\overline{X} - \mu| \geq \epsilon) = 0.$$

> [!theorem] The Strong Law of Large Numbers (SLLN)
> Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with a finite expected value $E[X_i] = \mu < \infty$. Let also $$M_n = \frac{X_1 + X_2 + \dots + X_n}{n}.$$
> Then $M_n \xrightarrow{a.s.} \mu$ (see [[Convergence]] for the modes of convergence).

## Central Limit Theorem

> [!theorem] Central Limit Theorem
> Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with expected value $E[X_i] = \mu < \infty$ and variance $0 < \text{Var}(X_i) = \sigma^2 < \infty$. Then, the random variable $$Z_n = \frac{\overline{X} - \mu}{\sigma / \sqrt{n}} = \frac{X_1 + X_2 + \dots + X_n - n \mu}{\sqrt{n} \sigma}$$ converges in distribution to the standard normal random variable as $n$ goes to infinity, that is $$\lim_{n \rightarrow \infty} P(Z_n \leq x) = \Phi(x), \forall x \in \mathbb R,$$ where $\Phi(x)$ is the standard normal CDF.

> [!principle] How to Apply The Central Limit Theorem (CLT)
> Here are the steps that we need in order to apply the CLT:
> 1. Write the random variable of interest, $Y$, as the sum of $n$ i.i.d. random variable $X_i$'s: $$Y = X_1 + \dots + X_n.$$
> 2. Find $E[Y]$ and $\text{Var}(Y)$ by noting that $$E[Y] = n \mu, \text{Var}(Y) = n \sigma^2,$$ where $\mu = E[X_i]$ and $\sigma^2 = \text{Var}(X_i)$.
> 3. According to the CLT, conclude that $\frac{Y - E[Y]}{\sqrt{\text{Var}(Y)}} = \frac{Y - n\mu}{\sqrt{n} \sigma}$ is approximately standard normal; thus, to find $P(y_1 \leq Y \leq y_2)$, we can write $$\begin{align}P(y_1 \leq Y \leq y_2) &= P(\frac{y_1 - n \mu}{\sqrt{n} \sigma} \leq \frac{Y - n \mu}{\sqrt{n} \sigma} \leq \frac{y_2 - n \mu}{\sqrt{n} \sigma}) \\ &\approx \Phi(\frac{y_2 - n \mu}{\sqrt{n} \sigma}) - \Phi(\frac{y_1 - n \mu}{\sqrt{n} \sigma})\end{align}$$

> [!theorem] Continuity Correction for Discrete Random Variables
> Let $X_1, X_2, \dots, X_n$ be independent discrete random variables and let $$Y = X_1 + X_2 + \dots + X_n.$$
> Suppose that we are interested in finding $P(A) = P(l \leq Y \leq u)$ using the CLT, where $l$ and $u$ are integers. Since $Y$ is an integer-valued random variable, we can write $$P(A) = P(l - \frac{1}{2} \leq Y \leq u + \frac{1}{2}).$$
> It turns out that the above expression sometimes provides a better approximation for $P(A)$ when applying the CLT. This is called the continuity correction and it is particularly useful when $X_i$'s are Bernoulli (i.e., $Y$ is binomial).
