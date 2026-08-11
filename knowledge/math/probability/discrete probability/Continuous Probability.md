
## Continuous Random Variables

> [!definition] Probability Density Function (PDF)
> Consider a continuous random variable $X$ with an absolutely continuous CDF $F_X(x)$. The function $f_X(x)$ defined by $$f_X(x) = \frac{d F_X(x)}{d x} = F'_X(x), \qquad \text{if } F_X(x) \text{ is differentiable at } x$$ is called the probability density function (PDF) of $X$.

> [!proposition] Properties of Probability Density Function
> Consider a continuous random variable $X$ with PDF $f_X(x)$. We have
> 1. $f_X(x) \geq 0$ for all $x \in \mathbb R$
> 2. $\int_{-\infty}^{\infty} f_X(u) du = 1$.
> 3. $P(a < X \leq b) = F_X(b) - F_X(a) = \int_{a}^{b} f_X(u) du$.
> 4. More generally, for a set $A$, $P(X \in A) = \int_A f_X(u) du$.

## Joint continuous Distributions

### Joint Probability Density Function

> [!definition] Joint Probability Density Function
> Two variables $X$ and $Y$ are **jointly continuous** if there exists a nonnegative function $f_{XY}: \mathbb R^2 \rightarrow \mathbb R$, such that, for any set $A \in \mathbb R^2$, we have $$P((X, Y) \in A) = \iint_A f_{XY}(x, y) dx dy$$ The function $f_{XY}(x, y)$ is called the **joint probability density function (PDF)** of $X$ and $Y$.

> [!remark]
> $$\int_{-\infty}^\infty \int_{-\infty}^\infty f_{XY}(x, y) dx dy = 1$$

### Joint Marginal Probability Density Function

> [!definition] Joint Marginal Probability Density Function
> - $f_X(x) = \int_{-\infty}^\infty f_{XY}(x, y) dy, \quad \forall x$.
> - $f_Y(y) = \int_{-\infty}^\infty f_{XY}(x, y) dx, \quad \forall y$.

## Transformations of Random Variables

> [!theorem]
> Suppose that $X$ is a continuous random variable and $g: \mathbb R \rightarrow \mathbb R$ is a strictly monotonic differentiable function. Let $Y = g(X)$. Then the PDF of $Y$ is given by $$f_Y(g) = \begin{cases} \frac{f_X(x_1)}{|g'(x_1)|} = f_X(x_1) \cdot |\frac{dx_1}{dy}| & \text{where } g(x_1) = y \\ 0 &\text{if } g(x) = y \text{ does not have a solution} \end{cases}$$

> [!theorem]
> Consider a continuous random variable $X$ with domain $R_X$, and let $Y = g(X)$. Suppose that we can partition $R_X$ into a finite number of intervals such that $g(x)$ is strictly monotone and differentiable on each partition. Then the PDF of $Y$ is given by $$f_Y(y) = \sum_{i = 1}^n \frac{f_X(x_i)}{|g'(x_i)|} = \sum_{i = 1}^n f_X(x_i) \cdot |\frac{dx_i}{dy}|$$ where $x_1, x_2, \cdots, x_n$ are real solutions to $g(x) = y$.
 
## Continuous Special Distribution

### Uniform Distribution

> [!definition] Uniform Distribution
> A continuous random variable $X$ is said to have **uniform** distribution over the interval $[a, b]$, shown as $X \sim \text{Uniform}(a, b)$, if its PDF is given by $$f_X(x) = \begin{cases} \frac{1}{b - a} & a < x < b \\ 0 & x < a \text{ or } x > b \end{cases}$$

> [!proposition] Properties of Uniform
> Let $X \sim \text{Uniform}(a, b)$
> - $EX = \frac{a + b}{2}.$
> - $\text{Var}(X) = \frac{(b - a)^2}{12}.$
> - Median $m = \frac{a + b}{2}$

> [!proposition]
> Let $U \sim \text{Uniform}(0, 1)$ and $X = -\ln(1 - U)$. Then $X \sim \text{Exponential}(1)$.

### Exponential Distribution

> [!definition] Exponential Distribution
> A continuous random variable $X$ is said to have an **exponential** distribution with parameter $\lambda > 0$, shown as $X \sim \text{Exponential}(\lambda)$, if its PDF is given by $$f_X(x) = \begin{cases} \lambda e^{-\lambda x} &x > 0 \\ 0 &\text{otherwise} \end{cases}$$
> Also, we have the CDF $$F_X(x) = (1 - e^{-\lambda x}) u(x).$$
> The parameters $\lambda$ is the **expected (average) number of events** (same as [[Discrete Probability#Poisson Distribution|Poisson]]) and $x$ is the **waiting time** until the **next event**.

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

### Normal (Gaussian) Distribution

> [!definition] Standard Normal Distribution
> A continuous random variable $Z$ is said to be a **standard normal (standard Gaussian)** random variable, shown as $Z \sim N(0, 1)$, if its PDF is given by $$f_Z(z) = \frac{1}{\sqrt{2 \pi}} e^{-\frac{z^2}{2}}, \qquad \text{for all } z \in \mathbb R.$$
> Also, we have the CDF $$F_Z(z) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^z e^{-\frac{u^2}{2}} du.$$

> [!proposition] Properties of Standard Normal
> If $Z \sim N(0, 1)$
> - $EZ = 0$
> - $\text{Var}(Z) = 1$
> - $E|Z| = \sqrt{\frac{2}{\pi}}$
> - For all $x \geq 0$, $$\frac{1}{\sqrt{2\pi}} \frac{x}{x^2 + 1} e^{-\frac{x^2}{2}} \leq P(Z \geq x) \leq \frac{1}{\sqrt{2\pi}} \frac{1}{x}e^{-\frac{x^2}{2}}$$
> - Median $m = \mu$

> [!definition] The $\Phi$ Function
> The CDF of the standard normal distribution is denoted by the $\Phi$ function: $$\Phi(x) = P(Z \leq x) = \frac{1}{\sqrt{2\pi}} \int_{-\infty}^x e^{-\frac{u^2}{2}} du.$$

> [!proposition] Properties of the $\Phi$ function
> 1. $\lim_{x \rightarrow \infty} \Phi(x) = 1, \lim_{x \rightarrow -\infty} = 0;$
> 2. $\Phi(0) = \frac{1}{2};$
> 3. $\Phi(-x) = 1 - \Phi(x), \forall x \in \mathbb R$.

> [!definition] Normal Distribution
> If $Z$ is a standard normal random variable and $X = \sigma Z + \mu$, then $X$ is a normal random variable with mean $\mu$ and variance $\sigma^2$, i.e, $$X \sim N(\mu, \sigma^2).$$

> [!proposition] Properties of Normal
> If $Z \sim N(\mu, \sigma^2)$
> - $EX = \sigma EZ + \mu = \mu$,
> - $\text{Var}(X) = \sigma^2 \text{Var}(Z) = \sigma^2$.

> [!proposition] 
> If $X$ is a normal random variable with mean $\mu$ and variance $\sigma^2$, i.e, $X \sim N(\mu, \sigma^2)$, then 
> $$f_X(x) = \frac{1}{\sigma \sqrt{2 \pi}} e^{-\frac{(x - \mu)^2}{2 \sigma^2}}$$
> $$F_X(x) = P(X \leq x) = \Phi(\frac{x - \mu}{\sigma})$$ 
> $$P(a < X \leq b) = \Phi(\frac{b - \mu}{\sigma}) - \Phi(\frac{a - \mu}{\sigma})$$

> [!theorem] Relationship Between Two Normal Variables
> If $X \sim N(\mu_X, \sigma_X^2)$, and $Y = aX + b$, where $a, b \in \mathbb R$, then $Y \sim N(\mu_y, \sigma_Y^2)$ where $$\mu_Y = a \mu_X + b, \quad \sigma_y^2 = \sigma^2 \sigma_X^2$$

> [!theorem]
> If $X \sim N(\mu_X, \sigma_X^2)$ and $Y \sim N(\mu_Y, \sigma_Y^2)$ are independent, then $$X + Y \sim N(\mu_X + \mu_Y, \sigma_X^2 + \sigma_Y^2).$$

> [!remark]
> Bivariate and multivariate normal distributions live in [[Random Vectors]]. High-dimensional Gaussians over $\mathbb Z^m$ (discrete Gaussian, tail bounds, rejection sampling) live in [[Lattice Helper]].

### Log-normal Distribution

> [!definition] Log-normal Distribution
> Let $Z \sim N(0, 1)$. If we define $X = e^{\sigma Z + \mu}$, then we say $X$ has a $\text{LogNormal}(\mu, \sigma)$ distribution with parameters $\mu$ is the **location on the log scale** and $\sigma$ is the **multiplicative spread / volatility**.

> [!proposition] Log-normal Distribution
> If $X \sim \text{LogNormal}(\mu, \sigma)$
> - $EX = e^{\mu + \frac{\sigma^2}{2}}$
> - $\text{Var}(X) = e^{2\mu + \sigma^2} (e^{\sigma^2} - 1)$

### Gamma Distribution

> [!definition] Gamma Distribution
> A continuous random variable $X$ is said to have a **gamma** distribution with parameters $\alpha > 0$ and $\lambda > 0$, shown as $X \sim \text{Gamma}(\alpha, \lambda)$, if its PDF is given by $$f_X(x) = \begin{cases}\frac{\lambda^\alpha x^{\alpha - 1} e^{-\lambda x}}{\Gamma(\alpha)} &x > 0 \\ 0 &\text{otherwise}  \end{cases}$$
> Where $\alpha$ is the **number of events** to wait for, $\lambda$ is the **expected number of events**, and $X$ is the total **waiting time**.

> [!proposition] Properties of Gamma
> If $X \sim \text{Gamma}(\alpha, \lambda)$
> - $EX = \frac{\alpha}{\lambda}$
> - $\text{Var}(X) = \frac{\alpha}{\lambda^2}$

> [!proposition] Exponential to Gamma 
> We have $\text{Gamma}(1, \lambda) = \text{Exponential}(\lambda)$, thus if $X_1, X_2, \dots, X_n$ be independent random variables with $X_i \sim \text{Exponential}(\lambda)$, then random variable $Y$ such that: $$Y = X_1 + X_2 + \cdots + X_n.$$ Then $Y \sim \text{Gamma}(n, \lambda)$.

### Laplace Distribution

> [!definition] Laplace Distribution
> A continuous random variable is said to have a $\text{Laplace}(\mu, b)$ distribution if its PDF is given by $$f_X(x) = \frac{1}{2b} \exp(-\frac{|x - \mu|}{b})$$ where $\mu \in \mathbb R$ is the **location (center)** and $b > 0$ is the **scale (spread / decay rate)**.

> [!proposition] Properties of Laplace
> If $X \sim \text{Laplace}(\mu, b)$
> - $EX = \mu$
> - $\text{Var}(X) = 2b^2$
> - $X \sim bY + \mu$ with $Y = \text{Laplace}(0, 1)$
> - $|X| \sim \text{Exponential}(\frac{1}{b})$

### Cauchy Distribution

> [!definition] Cauchy Distribution
> A continuous random variable is said to have a $\text{Cauchy}(x_0, \gamma)$ distribution if its PDF is given by $$f_X(x) = \frac{1}{\pi \gamma} \frac{1}{1 + (\frac{x - x_0}{\gamma})^2}$$ where $x_0$ is the typical ratio, and $\gamma$ measures how wildly ratios can blow up. 

### Rayleigh Distribution

> [!definition] Rayleigh Distribution
> A continuous random variable is said to have a $\text{Rayleigh}(\sigma)$ distribution if its PDF is given by $$f_X(x) = \frac{x}{\sigma^2} e^{-\frac{x^2}{2 \sigma^2}} u(x)$$ where $\sigma > 0$ is the **scale (energy / power)**.

> [!proposition] Properties of Rayleigh
> If $X \sim \text{Rayleigh}(\sigma)$
> - $EX = \sigma \sqrt{\frac{\pi}{2}}$
> - $\text{Var}(X) = \frac{4 - \pi}{2} \sigma^2$
> - $X = \sqrt{2 \sigma^2 Y}$ and $Y \sim \text{Exponential}(1)$

### Pareto Distribution

> [!definition] Pareto Distribution
> A continuous random variable is said to have a $\text{Pareto}(x_m, \alpha)$ distribution if its PDF is given by $$f_X(x) = \begin{cases}\alpha \frac{x_m^\alpha}{x^{\alpha + 1}} &\text{for } x \geq x_m \\ 0 &\text{for } x < x_m\end{cases}$$ where $x_m, \alpha > 0$.

> [!proposition] Properties of Pareto
> If $X \sim \text{Pareto}(x_m, \alpha)$
> - $EX = \begin{cases}\frac{\alpha x_m}{\alpha - 1}, &\alpha > 1 \\ \text{does not exist}, &\alpha \leq 1\end{cases}$
> - $\text{Var}(X) = \begin{cases}\frac{x_m \sqrt{\alpha}}{(\alpha - 1) \sqrt{\alpha - 2}}, &\alpha > 2 \\ \text{does not exist}, &\alpha \leq 2\end{cases}$



