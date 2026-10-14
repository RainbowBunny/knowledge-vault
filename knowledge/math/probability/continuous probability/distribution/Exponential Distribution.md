
## Definition

> [!definition] Exponential Distribution
> A continuous random variable $X$ is said to have an **exponential** distribution with parameter $\lambda > 0$, shown as $X \sim \text{Exponential}(\lambda)$, if its PDF is given by $$f_X(x) = \begin{cases} \lambda e^{-\lambda x} &x > 0 \\ 0 &\text{otherwise} \end{cases}$$
> Also, we have the CDF $$F_X(x) = (1 - e^{-\lambda x}) u(x).$$
> The parameters $\lambda$ is the **expected (average) number of events** (same as [[Discrete Probability#Poisson Distribution|Poisson]]) and $x$ is the **waiting time** until the **next event**.

## Property

> [!proposition] Properties of Exponential
> Let $X \sim \text{Exponential}(\lambda)$
> - $EX = \frac{1}{\lambda}$
> - $\text{Var}(X) = \frac{1}{\lambda^2}$
> - $E(X^n) = \frac{n}{\lambda} E(X^{n - 1})$, for $n = 1, 2, 3, \cdots$;
> - $E(X^n) = \frac{n!}{\lambda^n}$, for $n = 1, 2, 3, \cdots$;
> - Median $m = \frac{\ln 2}{\lambda}$

> [!proposition] Exponential as the limit of Geometric
> Let $Y \sim \text{Geometric}(p),$ where $p = \lambda \Delta$. Define $X = Y \Delta$, where $\lambda, \Delta > 0$, then for any $x \in (0, \infty)$, we have $$\lim_{\Delta \rightarrow 0} F_X(x) = 1 - e^{-\lambda x}.$$

> [!proposition]
> Let $X \sim \text{Exponential}(\lambda)$, and $Y = aX$, where $a$ is a positive real number. Then $$Y \sim \text{Exponential}(\frac{\lambda}{a}).$$

> [!proposition] Memoryless
> If $X$ is exponential with parameter $\lambda > 0$, then $X$ is a **memoryless** random variable, that is $$P(X > x + a | X > a) = P(X > x), \quad \text{for } a, x \geq 0.$$
