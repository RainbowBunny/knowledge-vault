## Multiple Random Variables

### Joint Cumulative Distribution Function

> [!definition] Joint Cumulative Distribution Function
> The **joint cumulative distribution function** of two random variables $X$ and $Y$ is defined as $$F_{XY}(x, y) = P(X \leq x, Y \leq y).$$ 

> [!definition] Marginal Cumulative Distribution Function
> - $F_X(x) = F_{XY}(x, \infty) = \lim_{y \rightarrow \infty} F_{XY}(x, y) \quad \forall x$
> - $F_Y(y) = F_{XY}(\infty, y) = \lim_{x \rightarrow \infty} F_{XY}(x, y) \quad \forall y$

> [!remark]
> - $F_{XY}(\infty, \infty) = 1$
> - $F_{XY}(-\infty, y) = 0, \quad \forall y$
> - $F_{XY}(x, -\infty) = 0, \quad \forall x$

> [!lemma]
> For two random variables $X$ and $Y$, and real numbers $x_1 \leq x_2, y_1 \leq y_2$, we have $$P(x_1 < X \leq x_2, y_1 < Y \leq y_2) = F_{XY}(x_2, y_2) - F_{XY}(x_1, y_2) - F_{XY}(x_2, y_1) + F_{XY}(x_1, y_1).$$

> [!remark]
> If $X$ and $Y$ are independent, then $F_{XY}(x, y) = F_X(x) F_Y(y)$.

> [!proposition]
> - $F_{XY}(x, y) = \int_{-\infty}^y \int_{-\infty}^x f_{XY}(u, v) du dv$
> - $f_{XY}(x, y) = \frac{\partial^2}{\partial x \partial y} F_{XY}(x, y)$

### Conditioning by Another Random Variable

> [!definition] Conditioning by Another Random Variable
> For two jointly continuous random variables $X$ and $Y$, we can define the following conditional concepts:
> 1. The conditional PDF of $X$ given $Y = y$: $$f_{X | Y}(x | y) = \frac{f_{XY}(x, y)}{f_Y(y)}$$
> 2. The conditional probability that $X \in A$ given $Y = y$: $$P(X \in A | Y = y) = \int_A f_{X | Y}(x | y) dx$$
> 3. The conditional CDF of $X$ given $Y = y$: $$F_{X | Y}(x | y) = P(X \leq x | Y = y) = \int_{-\infty}^x f_{X | Y}(x | y) dx$$

> [!proposition]
> For two jointly continuous random variables $X$ and $Y$, we have:
> 1. Expected value of $X$ given $Y = y$: $$E[X | Y = y] = \int_{-\infty}^\infty x f_{X | Y}(x | y) dx$$
> 2. Conditional LOTUS: $$E[g(x) | Y = y] = \int_{-\infty}^\infty g(x) f_{X | Y}(x | y) dx$$
> 3. Conditional variance of $X$ given $Y = y$: $$\text{Var}(X | Y = y) = E[X^2 | Y = y] - (E[X | Y = y])^2$$

### Independence

> [!proposition]
> Two continuous random variables $X$ and $Y$ are independent if $$f_{XY}(x, y) = f_X(x) f_Y(y), \quad \forall x, y.$$ Equivalently, $X$ and $Y$ are independent if $$F_{XY}(x, y) = F_X(x) F_Y(y), \quad \forall x, y.$$ If $X$ and $Y$ are independent, we have $$\begin{align}&E[XY] = E[X] E[Y],\\ &E[g(X)h(y)] = E[g(X)] E[h(y)]\end{align}$$

> [!definition] Independent and Identically Distributed
> Random variables $X_1, X_2, \dots, X_n$ are said to be **independent and identically distributed (i.i.d.)** if they are **independent**, and they have the same **marginal distributions**: $$F_{X_1}(x) = F_{X_2}(x) = \dots = F_{X_n}(x), \forall x \in \mathbb R.$$

### Covariance and Correlation

> [!definition] Covariance
> Consider two random variables $X$ and $Y$. The **covariance** between $X$ and $Y$ is defined as $$\text{Cov}(X, Y) = E[(X - EX)(Y - EY)] = E[XY] - (EX)(EY).$$

> [!lemma] Properties of Covariance
> 1. $\text{Cov}(X, X) = \text{Var}(X)$;
> 2. If $X$ and $Y$ are independent then $\text{Cov}(X, Y) = 0$.
> 3. $\text{Cov}(X, Y) = \text{Cov}(Y, X)$;
> 4. $\text{Cov}(aX, Y) = a \text{Cov}(X, Y)$;
> 5. $\text{Cov}(X + c, Y) = \text{Cov}(X, Y)$;
> 6. $\text{Cov}(X + Y, Z) = \text{Cov}(X, Z) + \text{Cov}(Y, Z)$;
> 7. More generally, $$\text{Cov}(\sum_{i = 1}^m a_i X_i, \sum_{j = 1}^n b_j Y_j) = \sum_{i = 1}^m \sum_{j = 1}^n a_i b_j \text{Cov}(X_i, Y_j).$$

> [!definition] Correlation Coefficient
> The **correlation coefficient** (for linear relationship), denoted by $\rho_{XY}$ or $\rho(X, Y)$, is obtained by normalizing the covariance: $$\rho_{XY} = \rho(X, Y) = \frac{\text{Cov}(X, Y)}{\sqrt{\text{Var}(X) \text{Var}(Y)}} = \frac{\text{Cov}(X, Y)}{\sigma_X \sigma_Y}$$

> [!lemma] Properties of the Correlation Coefficient
> 1. $-1 \leq \rho(X, Y) \leq 1$;
> 2. if $\rho(X, Y) = 1$, then $Y = aX + b$, where $a > 0$;
> 3. if $\rho(X, Y) = -1$, then $Y = aX + b$, where $a < 0$;
> 4. $\rho(aX + b, cY + d) = \rho(X, Y)$ for $a, c > 0$.

> [!definition]
> Consider two random variables $X$ and $Y$:
> - If $\rho(X, Y) = 0$, we say that $X$ and $Y$ are **uncorrelated**.
> - If $\rho(X, Y) > 0$, we say that $X$ and $Y$ are **positively correlated**.
> - If $\rho(X, Y) < 0$, we say that $X$ and $Y$ are **negatively correlated**.

> [!corollary]
> If $X$ and $Y$ are uncorrelated, then $$\text{Var}(X + Y) = \text{Var}(X) + \text{Var}(Y).$$
> More generally, if $X_1, X_2, \dots, X_n$ are pairwise uncorrelated, i.e., $\rho(X_i, X_j) = 0$ when $i \neq j$, then $$\text{Var}(X_1 + X_2 + \dots + X_n) = \text{Var}(X_1) + \text{Var}(X_2) + \dots + \text{Var}(X_n).$$

> [!proposition] Variance of Sum
> 1. $$\text{Var}(\sum_{i = 1}^n X_i) = \sum_{i = 1}^n \text{Var}(X_i) + 2 \sum_{i < j} \text{Cov}(X_i, X_j)$$
> 2. If $X_1, X_2, \dots, X_n$ are independent, $\text{Var}(\sum_{i = 1}^n X_i) = \sum_{i = 1}^n \text{Var}(X_i)$.

### Transformations of Two Random Variables

> [!theorem] Method of Transformations (Jacobian)
> Let $X$ and $Y$ be two jointly continuous random variables. Let $(Z, W) = g(X, Y) = (g_1(X, Y), g_2(X, Y))$, where $g: \mathbb R^2 \mapsto \mathbb R^2$ is a continuous one-to-one (invertible) function with continuous partial derivatives. Let $h = g^{-1}$, i.e., $(X, Y) = h(Z, W) = (h_1(Z, W), h_2(Z, W))$. Then $Z$ and $W$ are jointly continuous and their joint PDF, $f_{ZW}(z, w)$, for $(z, w) \in R_{ZW}$ is given by $$f_{ZW}(z, w) = f_{XY}(h_1(x, y), h_2(z, w)) |J|,$$ where $J$ is the Jacobian of $h$ defined by $$J = \det \begin{bmatrix} \frac{\partial h_1}{\partial z} & \frac{\partial h_1}{\partial w} \\ \frac{\partial h_2}{\partial z} & \frac{\partial h_2}{\partial w} \end{bmatrix} = \frac{\partial h_1}{\partial z} \frac{\partial h_2}{\partial w} - \frac{\partial h_1}{\partial w} \frac{\partial h_2}{\partial z}$$ 

> [!corollary] Sum of Two Random Variables (Convolution)
> If $X$ and $Y$ are two jointly continuous random variables and $Z = X + Y$, then $$f_Z(z) = \int_{-\infty}^{\infty} f_{XY}(w, z - w) dw = \int_{\infty}^{\infty} f_{XY} (z - w, w) dw.$$
> If $X$ and $Y$ are also independent, then $$f_Z(z) = f_X(z) * f_Y(z) = \int_{-\infty}^{\infty} f_X(w) f_Y(z - w) dw = \int_{-\infty}^{\infty} f_X(z - w) f_Y(w) dw.$$

## Related

- Multivariate distributions (multivariate / bivariate normal): [[Random Vectors]]
- Moment generating and characteristic functions: [[Expectation]]
- Sums of i.i.d. variables in the limit: [[Limit Theorems]]
