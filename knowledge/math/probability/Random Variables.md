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

### Function of Random Variables

> [!definition] Function of Random Variables
> If $X$ is a random variable and $Y = g(X)$, then $Y$ itself is a random variable.  $Y$ is the function of random variable with range $$R_Y = \{g(x) | x \in R_X\}.$$ If we already know the PMF of $X$, to find the PMF of $Y = g(X)$, we can write $$P_Y(y) = \sum_{x : g(x) = y} P_X(x)$$

### Conditioning on an Event

> [!definition] Conditional PDF of random variable
> If $X$ is a continuous random variables, and $A$ is the event that $a < X < b$ (where possibly $b = \infty$ or $a = -\infty$), then 
> $$F_{X | A}(x) = \begin{cases}1 &x > b \\ \frac{F_X(x) - F_X(a)}{F_X(b) - F_X(a)} &a \leq x < b \\ 0& x < a\end{cases}$$
> $$f_{X | A}(x) = \begin{cases} \frac{f_X(x)}{P(A)} &a \leq x < b \\ 0 &\text{otherwise} \end{cases}$$

> [!remark] Conditional Expectation and Variance
> $$\begin{align}&E[X | A] = \int_{-\infty}^\infty x f_{X | A}(x) dx, \\ &E[g(X) | A] = \int_{-\infty}^\infty g(x) f_{X | A}(x) dx \\ &\text{Var}(X | A) = E[X^2 | A] - (E[X | A])^2\end{align}$$

### Median

> [!definition] Median
> The **median** of a random variable $X$ is defined as any number $m$ that satisfies both of the following conditions: $$P(X \geq m) \geq \frac{1}{2} \quad \text{and} \quad P(X \leq m) \geq \frac{1}{2}$$ Note that the median of $X$ is not necessarily unique.

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

## Related

- Joint CDFs, conditioning on another random variable, covariance and correlation: [[Multiple Random Variables]]
- Expectation, variance, MGF: [[Expectation]]
- Distribution catalogs: [[Discrete Probability]], [[Continuous Probability]]
