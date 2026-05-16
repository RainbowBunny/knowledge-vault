## Other Summaries

### Median

> [!definition] Median
> The **median** of a random variable $X$ is defined as any number $m$ that satisfies both of the following conditions: $$P(X \geq m) \geq \frac{1}{2} \quad \text{and} \quad P(X \leq m) \geq \frac{1}{2}$$ Note that the median of $X$ is not necessarily unique.

### Memoryless

> [!proposition] Memoryless
> If $X$ is exponential with parameter $\lambda > 0$, then $X$ is a **memoryless** random variable that is $$P(X > x + a | X > a) = P(X > x), \quad \text{for } a, x \geq 0.$$

### Mixed Random Variables

> [!proposition] Mixed Random Variables
> The CDF of a mixed random variable $Y$ can be written as the sum of a continuous function and a staircase function: $$F_Y(y) = C(y) + D(y).$$
> Expected value of $Y$: $$EY = \int_{-\infty}^{\infty} y c(y) dy + \sum_{y_k} y_k P(Y = y_k).$$

### Generalized PDF

> [!definition] Generalized PDF for Discrete Random Variable
> For a discrete random variable $X$ with range $R_X = \{x_1, x_2, x_3, \dots\}$ and PMF $P_X(x_k)$, we define the (generalized) probability density function (PDF) as $$f_X(x) = \sum_{x_k \in R_X} P_X(x_k) \delta(x - x_k).$$

> [!definition] Generalized PDF for Mixed Random Variable
> The (generalized) PDF of a mixed random variable can be written in the form $$f_X(x) = \sum_k a_k \delta(x - x_k) + g(x),$$ where $a_k = P(X = x_k)$, and $g(x) \geq 0$ does not contain any delta functions.
> Furthermore, we have $$\int_{-\infty}^\infty f_X(x) dx = \sum_k a_k \int_{-\infty}^\infty g(x) dx = 1.$$

### Method of Transformations

> [!theorem]
> Let $X$ and $Y$ be two jointly continuous random variables. Let $(Z, W) = g(X, Y) = (g_1(X, Y), g_2(X, Y))$, where $g: \mathbb R^2 \mapsto \mathbb R^2$ is a continuous one-to-one (invertible) function with continuous partial derivatives. Let $h = g^{-1}$, i.e., $(X, Y) = h(Z, W) = (h_1(Z, W), h_2(Z, W))$. Then $Z$ and $W$ are jointly continuous and their joint PDF, $f_{ZW}(z, w)$, for $(z, w) \in R_{ZW}$ is given by $$f_{ZW}(z, w) = f_{XY}(h_1(x, y), h_2(z, w)) |J|,$$ where $J$ is the Jacobian of $h$ defined by $$J = \det \begin{bmatrix} \frac{\partial h_1}{\partial z} & \frac{\partial h_1}{\partial w} \\ \frac{\partial h_2}{\partial z} & \frac{\partial h_2}{\partial w} \end{bmatrix} = \frac{\partial h_1}{\partial z} \frac{\partial h_2}{\partial w} - \frac{\partial h_1}{\partial w} \frac{\partial h_2}{\partial z}$$ 

> [!corollary]
> If $X$ and $Y$ are two jointly continuous random variables and $Z = X + Y$, then $$f_Z(z) = \int_{-\infty}^{\infty} f_{XY}(w, z - w) dw = \int_{\infty}^{\infty} f_{XY} (z - w, w) dw.$$
> If $X$ and $Y$ are also independent, then $$f_Z(z) = f_X(z) * f_Y(z) = \int_{-\infty}^{\infty} f_X(w) f_Y(z - w) dw = \int_{-\infty}^{\infty} f_X(z - w) f_Y(w) dw.$$

### The Union Bound and Extension

> [!theorem] The Union Bound
> For any events $A_1, A_2, \dots, A_n$, we have $$P(\cup_{i = 1}^n A_i) \leq \sum_{i = 1}^n P(A_i).$$

> [!theorem] Generalization of the Union Bound: Bonferroni Inequalities
> For any events $A_1, A_2, \dots, A_n$, we have: $$\begin{align}
> P(\cup_{i = 1}^n A_i) &\leq \sum_{i = 1}^n P(A_i); \\
> P(\cup_{i = 1}^n A_i) &\geq \sum_{i = 1}^n P(A_i) - \sum_{i < j} P(A_i \cap A_j) \\
> P(\cup_{i = 1}^n A_i) &\leq \sum_{i = 1}^n P(A_i) - \sum_{i < j} P(A_i \cap A_j) + \sum_{i < j < k} P(A_i \cap A_j \cap A_k).
> \end{align}$$
 
### Markov's Inequality

> [!theorem] Markov's Inequality
> If $X$ is any nonnegative random variables, then $$P(X \geq a) \leq \frac{E[X]}{a}.$$

### Chebyshev's Inequality

> [!theorem] Chebyshev's Inequality
> If $X$ is any random variable, then for any $b > 0$ we have $$P(|X - E[X]| \geq b) \leq \frac{\text{Var}(X)}{b^2}.$$

### Chernoff Bounds

> [!theorem] Chernoff Bounds
> $$\begin{align}
> P(X \geq a) &\leq e^{-sa} M_X(s), \forall s > 0, \\
> P(X \leq a) &\leq e^{-sa} M_X(s), \forall s < 0
> \end{align}$$

### Cauchy-Schwarz Inequality

> [!theorem] Cauchy-Schwarz Inequality
> For any two random variables $X$ and $Y$, we have $$E[XY] \leq \sqrt{E[X^2] E[Y^2]},$$ where equality holds if and only if $X = \alpha Y$, for some constant $\alpha \in \mathbb R$.

### Law of Large Numbers

> [!definition] Sample Mean
> For i.i.d. random variables $X_1, X_2, \dots, X_n$, the **sample mean**, denoted by $\overline{X}$, is defined as $$\overline{X} = \frac{X_1 + X_2 + \dots + X_n}{n}.$$
> Another common notation for the sample mean is $M_n$. If the $X_i$'s have CDF $F_X(x)$, we might show the sample mean by $M_n(X)$ to indicate the distribution of the $X_i$'s.

> [!remark]
> - $E[\overline{X}] = E[X]$.
> - $\text{Var}(\overline{X}) = \frac{\text{Var}(X)}{n}$.

> [!theorem] Weak Law of Large Numbers (WLLN)
> Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with a finite expected value $E[X_i] = \mu < \infty$. Then, for any $\epsilon > 0$, $$\lim_{n \rightarrow \infty} P(|\overline{X} - \mu| \geq \epsilon) = 0.$$

### Central Limit Theorem

> [!theorem] Central Limit Theorem
> Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with expected value $E[X_i] = \mu < \infty$ and variance $0 < \text{Var}(X_i) = \sigma^2 < \infty$. Then, the random variable $$Z_n = \frac{\overline{X} - \mu}{\sigma / \sqrt{n}} = \frac{X_1 + X_2 + \dots + X_n - n \mu}{\sqrt{n} \sigma}$$ converges in distribution to the standard normal random variable as $n$ goes to infinity, that is $$\lim_{n \rightarrow \infty} P(Z_n \leq x) = \Phi(x), \forall x \in \mathbb R,$$ where $\Phi(x)$ is the standard normal CDF.

> [!principle] How to Apply The Central Limit Theorem (CLT)
> Here are the steps that we need in order to apply the CLT:
> 1. Write the random variable of interest, $Y$, as the sum of $n$ i.i.d. random variable $X_i$'s: $$Y = X_1 + \dots + X_n.$$
> 2. Find $E[Y]$ and $\text{Var}(Y)$ by noting that $$E[Y] = n \mu, \text{Var}(Y) = n \sigma^2,$$ where $\mu E[X_i]$ and $\sigma^2 = \text{Var}(X_i)$.
> 3. According to the CLT, conclude that $\frac{Y - E[Y]}{\sqrt{\text{Var}(Y)}} = \frac{Y - n\mu}{\sqrt{n} \sigma}$ is approximately standard normal; thus, to find $P(y_1 \leq Y \leq y_2)$, we can write $$\begin{align}P(y_1 \leq Y \leq y_2) &= P(\frac{y_1 - n \mu}{\sqrt{n} \sigma} \leq \frac{Y - n \mu}{\sqrt{n} \sigma} \leq \frac{y_2 - n \mu}{\sqrt{n} \sigma}) \\ &\approx \Phi(\frac{y_2 - n \mu}{\sqrt{n} \sigma}) - \Phi(\frac{y_1 - n \mu}{\sqrt{n} \sigma})\end{align}$$
