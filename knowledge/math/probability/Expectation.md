## Expectation & Moments

### Expected Value

> [!definition] Expected Value
> Let $X$ be a discrete random variable with range $R_X = \{x_1, x_2, x_3, \dots\}$ (finite or countably infinite). The expected value of $X$, denoted by $EX$ is defined as $$EX = \sum_{x_k \in R_k} x_k P(X = x_k) = \sum_{x_k \in R_X} x_k P_X(x_k).$$
> For $X$ be a continuous random variable, the expected value of $X$ is $$EX = \int_{-\infty}^{\infty} x f_X(x) dx$$ 

> [!remark] 
> Different notations for expected value of $X$: $EX = E[X] = E(X) = \mu_X$

> [!theorem] Expectation is linear
> We have
> - $E[aX + b] = aEX + b, \forall a, b \in \mathbb R$
> - $E[X_1 + X_2 + \cdots X_n] = EX_1 + EX_2 + \cdots + EX_n$, for any set of random variables $X_1, X_2, \cdots, X_n$.

> [!proposition] 
> Let $X$ be a discrete random variable with $R_X \subset \{0, 1, 2, \cdots\}$, $$EX = \sum_{k = 0}^{\infty} P(X > k).$$

> [!proposition]
> Let $X$ be a **positive** continuous random variable, $$EX = \int_0^{\infty} P(X \geq x) dx$$

> [!proposition]
> Let $X$ be a random variable with mean $EX = \mu$. Define the function $f(\alpha)$ as $$f(\alpha) = E[(X - \alpha)^2].$$ Then $\alpha = \mu$ minimizes $f$.

> [!definition] Conditional Expectation
> For a random variable $X$, the conditional expectation of $X$ is defined as
> $$\begin{align}
> &E[X | A] = \sum_{x_i \in R_X} x_i P_{X | A}(x_i), \\
> &E[X | Y = y_j] = \sum_{x_i \in R_X} x_i P_{X | Y}(x_i | y_j)
> \end{align}$$

> [!theorem] Law of Total Expectation
> 1. If $B_1, B_2, B_3, \dots$ is a partition of the sample space $S$, $$EX = \sum_i E[X | B_i] P(B_i)$$
> 2. For a random variable $X$ and a discrete random variable $Y$, $$EX = \sum_{y_j \in R_Y} E[X | Y = y_j] P_Y(y_j)$$

> [!theorem] Law of the unconscious statistician (LOTUS)
> 1. For discrete random variables:
> $$E[g(x)] = \sum_{x_k \in R_X} g(x_k) P_X(x_k)$$
> 2. For continuous random variables:
> $$E[g(x)] = \int_{-\infty}^{\infty} g(x) f_X(x) dx$$
> 3. For two discrete random variables:
> $$E[g(X, Y)] = \sum_{(x_i, y_j) \in R_{XY}} g(x_i, y_j) P_{XY}(x_i, y_j)$$
> 4. For two continuous random variables:
> $$E[g(x, y)] = \int_{-\infty}^\infty \int_{-\infty}^\infty g(x, y) f_{XY}(x, y) dx dy$$

> [!theorem] Law of Iterated Expectations
> $$E[X] = E[E[X | Y]]$$

> [!lemma]
> If $X$ and $Y$ are independent random variables, then
> 5. $E[X | Y] = EX$
> 6. $E[g(X) | Y] = E[g(X)]$
> 7. $E[XY] = E[X] E[Y]$
> 8. $E[g(X)h(Y)] = E[g(X)] E[h(Y)]$

### Variance

> [!definition] Variance
> The **variance** of a random variable $X$, with mean $EX = \mu_X$,
> For discrete random variable is defined as $$\text{Var}(X) = E[(X - \mu_X)^2] = \sum_{x_k \in R_X} (x_k - \mu_X)^2 P_X(x_k).$$
> For continuous random variable is defined as $$\text{Var}(X) = E[(X - \mu_X)^2] = \int_{-oo}^{oo} (x - \mu_X)^2 f_X(x) dx$$

> [!definition] Standard Deviation
> The **standard deviation** of a random variable $X$ is defined as $$\text{SD}(X) = \sigma_X = \sqrt{\text{Var}(X)}.$$

> [!proposition] 
> Computational formula for the variance
> $$\text{Var}(X) = E[X^2] - [EX]^2$$

> [!theorem]
> For a random variable $X$ and real numbers $a$ and $b$, $$\text{Var}(aX + b) = a^2 \text{Var}(X)$$
> For standard deviation: $$\text{SD}(aX + b) = |a| \text{SD}(X)$$

> [!theorem]
> If $X_1, X_2, \cdots, X_n$ are independent random variables and $X = X_1 + X_2 + \cdots + X_n,$ then $$\text{Var}(X) = \text{Var}(X_1) + \text{Var}(X_2) + \cdots + \text{Var}(X_n)$$ 

> [!theorem] Law of Total Variance
> $$\text{Var}(X) = E[\text{Var}(X | Y)] + \text{Var}(E[X | Y])$$

> [!proposition] Variance of a sum
> $$\text{Var}(aX + bY) = a^2 \text{Var}(X) + b^2 \text{Var}(Y) + 2ab \text{Cov}(X, Y)$$

### Moment Generating Function

> [!definition] Moment
> The **$n$-moment** of a random variable $X$ is defined to be $E[X^n]$. The **$n$-th central moment** of $X$ is defined to be $E[(X - EX)^n]$.

> [!definition] Moment Generating Function
> The moment generating function (MGF) of a random variable $X$ is a function $M_X(s)$ defined as $$M_X(s) = E[e^{sX}].$$
> We say that MGF of $X$ exists, if there exists a positive constant $a$ such that $M_X(s)$ is finite for all $s \in [-a, a]$. 

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
