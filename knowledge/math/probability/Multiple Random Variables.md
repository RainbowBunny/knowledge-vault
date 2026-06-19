## Multiple Random Variables

> [!definition] Independent and Identically Distributed
> Random variables $X_1, X_2, \dots, X_n$ are said to be **independent and identically distributed (i.i.d.)** if they are **independent**, and they have the same **marginal distributions**: $$F_{X_1}(x) = F_{X_2}(x) = \dots = F_{X_n}(x), \forall x \in \mathbb R.$$

> [!proposition] Variance of Sum
> 1. $$\text{Var}(\sum_{i = 1}^n X_i) = \sum_{i = 1}^n \text{Var}(X_i) + 2 \sum_{i < j} \text{Cov}(X_i, X_j)$$
> 2. If $X_1, X_2, \dots, X_n$ are independent, $\text{Var}(\sum_{i = 1}^n X_i) = \sum_{i = 1}^n \text{Var}(X_i)$.

### Moment Generating Function

> [!definition] Moment
> The **$n$-moment** of a random variable $X$ is defined to be $E[X^n]$. The **$n$-th central moment** of $X$ is defined to be $E[(X - EX)^n]$.

> [!definition] Moment Generating Function
> The moment generating function (MGF) of a random variable $X$ is a function $M_X(s)$ defined as $$M_X(s) = E[e^{sX}].$$
> We say that MGF of $X$ exists, if there exists a positive constant $a$ such that $M_X(s)$ is finite for all $s \in [-a, a]$. 
> 

> [!remark]
> We can obtain all moments of $X^k$ from its MGF:
> $$\begin{align}&M_X(s) = \sum_{k = 0}^\infty E[X^k] \frac{s^k}{k!} \\ &E[X^k] = \frac{d^k}{ds^k} M_X(s) |_{s = 0} \end{align}$$

> [!theorem]
> Consider two random variables $X$ and $Y$. Suppose that there exists a positive constant $c$ such that MGFs of $X$ and $Y$ are finite and identical for all values of $s$ in $[-c, c]$. Then, $$F_X(t) = F_Y(t), \forall t \in \mathbb R.$$

> [!proposition]
> If $X_1, X_2, \dots, X_n$ are $n$ independent random variable, then $$M_{X_1 + X_2 + \cdots + X_n}(s) = M_{X_1}(s) M_{X_2}(s) \cdots M_{X_n}(s).$$

### Characteristic Functions

> [!definition] Characteristic Function
> For a random variable $X$, the characteristic function is defined as $$\phi_X(\omega) = E[e^{j \omega X}]$$ 

> [!proposition]
> If $X_1, X_2, \dots, X_n$ are $n$ independent random variable, then $$\phi_{X_1 + X_2 + \cdots + X_n}(s) = \phi_{X_1}(s) \phi_{X_2}(s) \cdots \phi_{X_n}(s).$$

## Multivariate normal distribution

> [!theorem]
> $\mathbf{X} \sim \mathcal{N}_k(\boldsymbol{\mu}, \boldsymbol{\Sigma}) \iff \exists \boldsymbol{\mu} \in \mathbb{R}^k, \boldsymbol{A} \in \mathbb{R}^{k \times \ell} \text{ s.t } \mathbf{X} = \boldsymbol{A}\mathbf{Z} + \boldsymbol{\mu} \text{ and } \forall n = 1, \dots, \ell: Z_n \sim \mathcal{N}(0,1), \text{i.i.d.}$
> Here the covariance matrix is $\boldsymbol{\Sigma} = \boldsymbol{A}\boldsymbol{A}^\top$

> [!proposition]
> $\mathcal{N}_k(\boldsymbol{\mu_1}, \boldsymbol{\Sigma_1}) + \mathcal{N}_k(\boldsymbol{\mu_2}, \boldsymbol{\Sigma_2}) = \mathcal{N}_k(\boldsymbol{\mu_1}+\boldsymbol{\mu_2}, \boldsymbol{\Sigma_1} + \boldsymbol{\Sigma_2})$ (immediate from theorem)

> [!definition] Density function (Non-degenerate case)
> When the covariance matrix $\mathbf{\Sigma}$ is positive definite, we have:
> $$f_{\mathbf{X}}(x_1, \dots, x_k) = \frac{\exp\left( -\frac{1}{2}(\mathbf{x} - \boldsymbol{\mu})^\text{T} \boldsymbol{\Sigma}^{-1} (\mathbf{x} - \boldsymbol{\mu}) \right)}{\sqrt{(2\pi)^k |\boldsymbol{\Sigma}|}}$$




















