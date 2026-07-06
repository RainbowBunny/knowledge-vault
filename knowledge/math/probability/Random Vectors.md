## Random Vectors

### Multivariate Normal Distribution

> [!theorem]
> $\mathbf{X} \sim \mathcal{N}_k(\boldsymbol{\mu}, \boldsymbol{\Sigma}) \iff \exists \boldsymbol{\mu} \in \mathbb{R}^k, \boldsymbol{A} \in \mathbb{R}^{k \times \ell} \text{ s.t } \mathbf{X} = \boldsymbol{A}\mathbf{Z} + \boldsymbol{\mu} \text{ and } \forall n = 1, \dots, \ell: Z_n \sim \mathcal{N}(0,1), \text{i.i.d.}$
> Here the covariance matrix is $\boldsymbol{\Sigma} = \boldsymbol{A}\boldsymbol{A}^\top$

> [!proposition]
> $\mathcal{N}_k(\boldsymbol{\mu_1}, \boldsymbol{\Sigma_1}) + \mathcal{N}_k(\boldsymbol{\mu_2}, \boldsymbol{\Sigma_2}) = \mathcal{N}_k(\boldsymbol{\mu_1}+\boldsymbol{\mu_2}, \boldsymbol{\Sigma_1} + \boldsymbol{\Sigma_2})$ (immediate from theorem)

> [!definition] Density function (Non-degenerate case)
> When the covariance matrix $\mathbf{\Sigma}$ is positive definite, we have:
> $$f_{\mathbf{X}}(x_1, \dots, x_k) = \frac{\exp\left( -\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^\text{T} \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) \right)}{\sqrt{(2\pi)^k |\boldsymbol{\Sigma}|}}$$

### Bivariate Normal Distribution

> [!definition] Bivariate Normal
> Two random variables $X$ and $Y$ are said to be **bivariate normal**, or **jointly normal**, if $aX + bY$ has a normal distribution for all $a, b \in \mathbb R$.

> [!remark]
> - If $X$ and $Y$ are bivariate normal, then letting $a = 1, b = 0$, we conclude that $X$ must be normal. Similarly, we have $Y$ must be normal.
> - If $X \sim N(\mu_X, \sigma_X^2)$ and $Y \sim N(\mu_Y, \sigma_Y^2)$ are independent, then they are jointly normal.
> - If $X \sim N(\mu_X, \sigma_X^2)$ and $Y \sim N(\mu_Y, \sigma_Y^2)$ are jointly normal, then $X + Y \sim N(\mu_X + \mu_Y, \sigma_X^2 + \sigma_Y^2 + 2\rho(X, Y) \sigma_X \sigma_Y)$.

> [!definition] Standard Bivariate Normal Distribution 
> Two random variables $X$ and $Y$ are said to have the **standard bivariate normal distribution with correlation coefficient** $\rho$ if their joint PDF is given by $$f_{XY}(x, y) = \frac{1}{2\pi \sqrt{1 - p^2}} \exp\{-\frac{1}{2(1 - \rho^2)} [x^2 - 2\rho xy + y^2]\},$$ where $\rho \in (-1, 1)$. If $\rho = 0$, then we just say $X$ and $Y$ have the standard bivariate normal distribution. 

> [!definition] Bivariate Normal Distribution
> Two random variables $X$ and $Y$ are said to have a **bivariate normal distribution** with parameters $\mu_X, \sigma_X^2, \mu_Y, \sigma_Y^2,$ and $\rho$, if their joint PDF is given by $$f_{XY} = \frac{1}{2 \pi \sigma_X \sigma_Y \sqrt{1 - \rho^2}} \exp\{-\frac{1}{2(1 - \rho^2)} [(\frac{x - \mu_X}{\sigma_X})^2 + (\frac{y - \mu_Y}{\sigma_Y})^2 - 2\rho \frac{(x - \mu_X)(y - \mu_Y)}{\sigma_X \sigma_Y}]\}$$ where $\mu_X, \mu_Y \in \mathbb R, \sigma_X, \sigma_Y > 0$ and $\rho \in (-1, 1)$ are all constants.

> [!theorem]
> Let $X$ and $Y$ be two bivariate normal random variables. Then there exist independent standard normal random variables $Z_1$ and $Z_2$ such that $$\begin{cases} X &= \sigma_X Z_1 + \mu_X \\ Y &= \sigma_Y(\rho Z_1 + \sqrt{1 - \rho^2} Z_2) + \mu_Y\end{cases}$$

> [!theorem]
> Suppose $X$ and $Y$ are jointly normal random variables with parameters $\mu_X, \sigma_X^2, \mu_Y, \sigma_Y^2$, and $\rho$. Then, given $X = x$, $Y$ is normally distributed with $$\begin{align}&E[Y | X = x] = \mu_Y + \rho \sigma_Y \frac{x - \mu_X}{\sigma_X}, \\ &\text{Var}(Y | X = x) = (1 - \rho^2) \sigma_Y^2\end{align}$$

> [!theorem]
> If $X$ and $Y$ are bivariate normal and uncorrelated, then they are independent.

> [!example]
> Let $X$ and $Y$ be jointly (bivariate) normal, with $\text{Var}(X) = \text{Var}(Y)$. Then $X + Y$ and $X - Y$ are independent.

## Related

- Lattice-oriented Gaussians over $\mathbb Z^m$ (discrete Gaussian, tail bounds, rejection sampling): [[Lattice Helper]]
