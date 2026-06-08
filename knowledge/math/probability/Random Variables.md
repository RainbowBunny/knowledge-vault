## Random Variables

### Definition of random variables

> [!definition] Random Variables
> A random variable $X$ is a function from the sample space to the real numbers. $$X : S \rightarrow \mathbb R$$

> [!definition] Range
> The range of a random variable $X$, shown by $\text{Range}(X)$ or $R_X$, is the set of possible values of $X$. If $X$ is a continuous random variable, we can define the range of $X$ as the set of real number $x$ for which the PDF is larger than zero, i.e, $$R_X = \{x | f_X(x) > 0\}.$$
> The set $R_X$ defined here might not exactly show all possible values of $X$, but the difference is practically unimportant

### Cumulative Distribution Function

> [!definition] Discrete Cumulative Distribution Function
> The cumulative distribution function (CDF) of random variable $X$ is defined as $$F_X(x) = P(X \leq x), \forall x \in \mathbb R$$

> [!corollary]
> For $a \leq b$, we have $$P(a < X \leq B) = F_X(b) - F_X(a)$$

> [!definition] Continuous Cumulative Distribution Function
> A random variable $X$ with CDF $F_X(x)$ is said to be continuous if $F_X(x)$ is a continuous function for all $x \in \mathbb R$.
> We will also assume that the CDF of a continuous random variable is differentiable almost everywhere in $\mathbb R$.

> [!definition] Conditional CDF
> The **conditional CDF** of $X$ given $A$ is defined as $$F_{X | A}(x) = P(X \leq x | A).$$

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


### Function of Random Variables

> [!definition] Function of Random Variables
> If $X$ is a random variable and $Y = g(X)$, then $Y$ itself is a random variable.  $Y$ is the function of random variable with range $$R_Y = \{g(x) | x \in R_X\}.$$ If we already know the PMF of $X$, to find the PMF of $Y = g(X)$, we can write $$P_Y(y) = \sum_{x : g(x) = y} P_X(x)$$

### Conditioning and Independence

> [!definition] Conditional PDF of random variable
> If $X$ is a continuous random variables, and $A$ is the event that $a < X < b$ (where possibly $b = \infty$ or $a = -\infty$), then 
> $$F_{X | A}(x) = \begin{cases}1 &x > b \\ \frac{F_X(x) - F_X(a)}{F_X(b) - F_X(a)} &a \leq x < b \\ 0& x < a\end{cases}$$
> $$f_{X | A}(x) = \begin{cases} \frac{f_X(x)}{P(A)} &a \leq x < b \\ 0 &\text{otherwise} \end{cases}$$

> [!remark] Conditional Expectation and Variance
> $$\begin{align}&E[X | A] = \int_{-\infty}^\infty x f_{X | A}(x) dx, \\ &E[g(X) | A] = \int_{-\infty}^\infty g(x) f_{X | A}(x) dx \\ &\text{Var}(X | A) = E[X^2 | A] - (E[X | A])^2\end{align}$$

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

> [!proposition]
> Two continuous random variables $X$ and $Y$ are independent if $$f_{XY}(x, y) = f_X(x) f_Y(y), \quad \forall x, y.$$ Equivalently, $X$ and $Y$ are independent if $$F_{XY}(x, y) = F_X(x) F_Y(y), \quad \forall x, y.$$ If $X$ and $Y$ are independent, we have $$\begin{align}&E[XY] = E[X] E[Y],\\ &E[g(X)h(y)] = E[g(X)] E[h(y)]\end{align}$$

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
