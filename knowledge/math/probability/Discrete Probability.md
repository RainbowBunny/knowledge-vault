
## Discrete Random Variables

> [!definition] Discrete Probability Models
> Consider a sample space $S$. If $S$ is a **countable set**, this refers to a **discrete** probability model. In this case, since $S$ is countable, we can list all the elements in $S$:
> $$S = \{s_1, s_2, s_3, \cdots\}.$$
> 
> If $A \subset S$ is an event, then $A$ is also countable, and by the third axiom of probability we can write $$P(A) = P(\bigcup_{s_j \in A} \{s_j\}) = \sum_{s_j \in A} P(s_j)$$

> [!definition] Finite Sample Spaces with Equally Likely Outcomes
> An important special case of discrete probability models is when we have a finite sample space $S$, where each outcome is equally likely, i.e., $$S = \{s_1, s_2, \cdots, s_N\}, \text{where } P(s_i) = P(s_j) \; \forall \; i, j \in \{1, 2, \cdots, N\}$$
> Since all outcomes are equally likely, we must have $$P(s_i) = \frac{1}{N}, \forall i \in \{1, 2, \cdots, N\}.$$
> In such a model, if $A$ is any event with cardinality $|A| = M$, we can write $$P(A) = \sum_{s_j \in A} P(s_j) = \sum_{s_j \in A} \frac{1}{N} = \frac{M}{N} = \frac{|A|}{|S|}$$ 
> Thus, finding probability of $A$ reduces to a **counting** problem in which we need to count how many elements are in $A$ and $S$.

> [!definition] Discrete Random Variables
> $X$ is a discrete random variables, if its range is countable.

### Probability Mass Function

> [!definition] Probability Mass Function
> Let $X$ be a discrete random variable with range $R_X = \{x_1, x_2, x_3, \dots\}$ (finite or countably infinite). The function $$P_X(x_k) = P(X = x_k), \text{for } k = 1, 2, 3, \dots,$$ is called the **probability mass function (PMF)** of $X$.

> [!remark]
>- It is sometimes convenient to extend the PMF of $X$ to all real numbers. If $x \notin R_X$, we can simply write $P_X(x) = P(X = 0) = 0$. Thus, in general we can write $$P_X(x) = \begin{cases}P(X = x) &\text{if } x \in R_x \\ 0 &\text{otherwise} \end{cases}$$
>- The PMF is also called **probability distribution**.

> [!proposition] Properties of PMF:
> - $0 \leq P_X(x) \leq 1$ for all $x$;
> - $\sigma_{x \in R_X} P_X(x) = 1$;
> - for any set $A \subset R_X, P(X \in A) = \sum_{x \in A} P_X(x)$.

### Joint Probability Mass Function (PMF)

> [!definition] Joint Probability Mass Function
> The **joint probability mass function** of two discrete random variables $X$ and $Y$ is defined as $$P_{XY}(x, y) = P(X = x, Y = y).$$

> [!definition] Marginal Probability Mass Function
> For the joint probability of two random variables $X$ and $Y$, we can obtain PMF of one variable from its joint PMF with the other:
> - $P_X(x) = \sum_{y_j \in R_Y} P_{XY}(x, y_j), \quad \forall x \in R_x$
> - $P_Y(y) = \sum_{x_i \in R_X} P_{XY}(x_i, y), \quad \forall y \in R_y$

### Conditional PMF

> [!definition] Conditional PMF
> For a discrete random variable $X$ and event $A$, the **conditional PMF** of $X$ given $A$ is defined as 
> $$\begin{align}P_{X | A}(x_i) &= P(X = x_i | A) \\ &= \frac{P(X = x_i \cap A)}{P(A)}, \quad \forall x_i \in R_X.\end{align}$$

> [!definition] Conditional PMF of two Variables
> For discrete random variables $X$ and $Y$, the **conditional PMFs** of $X$ given $Y$ and vice versa are defined as $$\begin{align}P_{X | Y}(x_i | y_j) = \frac{P_{XY}(x_i, y_j)}{P_Y(y_j)}\\ P_{Y | X}(y_j | x_i) = \frac{P_{XY}(x_i, y_j)}{P_X(x_i)}\end{align}$$

### Indicator Random variables

> [!definition] Indicator Random Variables
> Suppose we are given a sample space $S$ and an event $A$. Then the **indicator random variable** $I\{A\}$ associated with event $A$ is defined as $$I\{A\} = \begin{cases}1 &\text{if } A \text{occurs}, \\ 0 &\text{if } A \text{ does not occur}.\end{cases}$$

> [!lemma]
> Given a sample space $S$ and an event $A$ in the sample space $S$, let $X_A = I\{A\}$. Then $E[X_A] = P\{A\}$

### Continuity Correction for Discrete Random Variables

> [!theorem] Continuity Correction for Discrete Random Variables
> Let $X_1, X_2, \dots, X_n$ be independent discrete random variables and let $$Y = X_1 + X_2 + \dots + X_n.$$
> Suppose that we are interested in finding $P(A) = P(l \leq Y \leq u)$ using the CLT, where $l$ and $u$ are integers. Since $Y$ is an integer-valued random variables, we can write $$P(A) = P(l - \frac{1}{2} \leq Y \leq u + \frac{1}{2}).$$
> It turns out that the above expression sometimes provides a better approximation for $P(A)$ when applying the CLT. This is called the continuity correction and it is particular useful when $X_i$'s are Bernoulli (i.e., $Y$ is binomial).

## Independence

> [!definition] Independent Random Variables (Discrete, Two Variables)
> Consider two discrete random variables $X$ and $Y$. We say that $X$ and $Y$ are independent if $$P(X = x, Y = y) = P(X = x) P(Y = y), \forall x, y.$$
> In general, if two random variables are independent, then we have $$P(X \in A, Y \in B) = P(X \in A) P(Y \in B), \forall \text{ sets } A, B.$$

> [!definition] Independent Random Variables (Discrete, $n$ Variables)
> Consider $n$ discrete random variables $X_1, X_2, X_3, \dots, X_n$. We say that $X_1, X_2, X_3, \dots X_n$ are independent if $$P(X_1 = x_1, X_2 = x_2, \dots, X_n = x_n) = P(X_1 = x_1) P(X_2 = x_2) \dots P(X_n = x_n), \forall x_1, x_2, \dots, x_n$$

> [!proposition]
> Two discrete random variables $X$ and $Y$ are independent if $$P_{XY}(x, y) = P_X(x) P_Y(y), \quad \forall x, y.$$
> Equivalent, $X$ and $Y$ are independent if $$F_{XY}(x, y) = F_X(x) F_Y(y), \quad \forall x, y.$$

## Some useful bounds

> [!theorem] Markov's inequality
> Let $X \in \mathbb{R}^+$ be a random variable. Then for every $\alpha > 0$, we have:
> $$\Pr[X \ge \alpha] \leq \dfrac{E[X]}{\alpha}$$


> [!theorem] Chebyshev's inequality
> Let $X \in \mathbb{R}$ be a random variable with $\mu := E[X]$ and $\nu := Var[X]$. Then for every $\alpha > 0$, we have:
> $$\Pr[|X - \mu| \ge \alpha] \le \dfrac{\nu}{\alpha^2}$$

> [!theorem] Chernoff bound
> Let $\{X_i\}_{i \in I}$ be a finite, non-empty, and mutually independent family of random variables, such that each $X_i$ is $1$ with probability $p$ and $0$ with probability $q := 1 - p$. Assume that $0 < p < 1$. Also, let $n := |I|$ and $\overline{X}$ be the sample mean of $\{X_i\}_{i \in I}$. Then for every $\varepsilon > 0$, we have:
> - $\Pr[\overline{X} - p \ge \epsilon] \le \exp(-n\epsilon^2/2q)$
> - $\Pr[\overline{X} - p \le -\epsilon] \le \exp(-n\epsilon^2/2p)$
> - $\Pr[|\overline{X} - p \ge \epsilon|] \le 2\exp(-n\epsilon^2/2)$





## Discrete Special Distribution

### Bernoulli Distribution

> [!definition] Bernoulli Distribution
> A random variable $X$ is said to be a **Bernoulli** random variables with **parameter** $p$, shown as $X \sim \text{Bernoulli}(p)$, if its PMF is given by $$P_X(x) = \begin{cases}p &\text{for } x = 1 \\ 1 - p &\text{for } x = 0 \\ 0 &\text{otherwise}\end{cases}$$ where $0 < p < 1$.

> [!proposition] Properties of Bernoulli
>  Let $X \sim \text{Bernoulli}(p)$.
>  - $EX = p$.
>  - $\text{Var}(X) = p(1 - p)$.

### Geometric Distribution

> [!definition] Geometric Distribution
> A random variable $X$ is said to be a **geometric** random variable with **parameter** $p$, shown as $X \sim \text{Geometric}(p)$, if its PMF is given by $$P_X(k) = \begin{cases} p(1 - p)^{k - 1} &\text{for } k = 1, 2, 3, \dots  \\ 0 &\text{otherwise} \end{cases}$$ where $0 < p < 1$ and $k$ is the **number of trials**.
> Sometimes, some books define geometric random variables by the total number of failures before the first success: $$P_X(x) = \begin{cases}p(1 - p)^k &\text{for } k = 0, 1, 2, 3, \dots \\ 0 &\text{otherwise}\end{cases}$$

> [!proposition] Properties of Geometric
> Let $X \sim \text{Geometric}(p)$
> - $EX = \frac{1}{p}$.
> - $\text{Var}(X) = \frac{1 - p}{p^2}$

### Binomial Distribution

> [!definition] Binomial Distribution
> A random variable $X$ is said to be a **binomial** random variable with parameters $n$ and $p$, shown as $X \sim \text{Binomial}(n, p)$, if its PMF is given by $$P_X(k) = \begin{cases} \binom{n}{k} p^k (1 - p)^{n - k} &\text{for } k = 0, 1, 2, \dots, n \\ 0 &\text{otherwise} \end{cases}$$ where $0 < p < 1$ is the success rate, $n$ is the number of trials and $k$ is the number of success.

> [!lemma] Binomial random variable as a sum of Bernoulli random variables
> If $X_1, X_2, \dots, X_n$ are independent $\text{Bernoulli}(p)$ random variables, then the random variable $X$ defined by $X = X_1 + X_2 + \dots + X_n$ has a $\text{Binomial}(n, p)$ distribution.
 
> [!example]
> Let $X \sim \text{Binomial}(n, p)$ and $Y \sim \text{Binomial}(m, p)$ be two independent random variables. Then, random variable $Z = X + Y \sim \text{Binomial}(n + m, p)$

> [!proposition] Properties of Binomial
> Let $X \sim \text{Binomial}(n, p)$
> - $EX = np$.
> - $\text{Var}(X) = np(1 - p)$.

### Pascal Distribution

> [!definition] Negative Binomial (Pascal) Distribution
> A random variable $X$ is said to be a **Pascal** random variable with parameters $m$ and $p$, shown as $X \sim \text{Pascal}(m, p)$, if its PMF is given by $$P_X(k) = \begin{cases} \binom{k - 1}{m - 1} p^m (1 - p)^{k - m} &\text{for } k = m, m + 1, m + 2, m + 3, \dots \\ 0 &\text{otherwise} \end{cases}$$ where $m$ is the number of **successes**, $p$ is the success rate and $k$ is the number of **failures**.

> [!example]
> $\text{Pascal}(1, p) = \text{Geometric}(p)$

> [!example] 
> Let $X \sim \text{Pascal}(m, p)$ and $Y \sim \text{Pascal}(l, p)$ be two independent random variables. Then, random variable $Z = X + Y \sim \text{Pascal}(m + l, p)$ 

> [!proposition] Properties of Pascal
> Let $X \sim Pascal(m, p)$
> - $EX = \frac{m}{p}$
> - $\text{Var}(X) = \frac{m(1 - p)}{p^2}$

### Hypergeometric Distribution

> [!definition] Hypergeometric Distribution
> A random variable $X$ is said to be a **Hypergeometric** random variable with parameters $b$, $r$ and $k$, shown as $X \sim \text{Hypergeometric}(b, r, k)$, if its range is $R_X = \{\max(0, k - r), \max(0, k - r) + 1, \max(0, k - r) + 2, \dots, \min(k, b)\}$, and its PMF is given by $$P_X(x) = \begin{cases} \frac{\binom{b}{x} \binom{r}{k - x}}{\binom{b + r}{k}} &\text{for } x \in R_X  \\ 0 &\text{otherwise} \end{cases}$$ is the solution to choose $k$ marbles consist of $x$ **blue marbles** and $k - x$ **red marbles** from $b$ **blue marbles** and $r$ **red marbles**.

> [!proposition] Properties of Hypergeometric
> - $EX = \frac{kb}{b + r}$

### Poisson Distribution

> [!definition] Poisson Distribution
> A random variable $X$ is said to be a **Poisson** random variable with parameter $\lambda$, shown as $X \sim \text{Poisson}(\lambda)$, if its range is $R_X = \{0, 1, 2, 3, \dots\}$, and its PMF is given by $$P_X(k) = \begin{cases} \frac{e^{-\lambda} \lambda^k}{k!} &\text{for } k \in R_X \\ 0 &\text{otherwise} \end{cases}$$ where $\lambda$ represents the **expected (average) number of events** occurring in a **fixed interval** of time, space, area, or volume and $k$ is the **number of events observed**.

> [!theorem] Poisson as an approximation for binomial
> Let $X \sim \text{Binomial}(n, p = \frac{\lambda}{n})$, where $\lambda > 0$ is fixed. Then for any $k \in \{0, 1, 2, \dots\}$, we have $$\lim_{n \rightarrow \infty} P_X(k) = \frac{e^{-\lambda} \lambda^k}{k!}$$

> [!proposition] Properties of Poisson
> Let $X \sim \text{Poisson}(\lambda)$
> - $EX = \lambda$.
> - $\text{Var}(X) = \lambda$

> [!proposition] Poisson to Exponential
> Suppose the number of customers arriving at a store obeys a Poisson distribution with an average of $\lambda$ customers per unit time. That is, if $Y$ is the number of customers arriving in an interval of length $t$, then $Y \sim \text{Poisson}(\lambda t)$. Suppose that the store opens at time $t = 0$. Let $X$ be the arrival time of the first customer. Then $X \sim \text{Exponential}(\lambda)$.

### Discrete Gaussian 

> [!definition] Discrete Gaussian
> For a full-rank lattice $\Lambda \subset \mathbb{R}^n, s > 0$ and $\mathbf{z} \in \mathbb{R}^n$, the mass function of discrete Gaussian distribution $D_{\Lambda + \mathbf{z},s}$ is defined as:
> $$\Pr_{X \sim D_{\Lambda + \mathbf{z}, s}}[X = \mathbf{x}] = \dfrac{\rho_s(\mathbf{x})}{\rho_s(\Lambda + \mathbf{z})}$$
> where $\rho_s(\mathbf{x}) := \exp(-\pi\|\mathbf{x}/s\|^2)$ for $s> 0$

> [!theorem] Strong tail bound
> For $\mathcal{L} \subset \mathbb{R}^n$ a full-rank lattice, $r \ge 1, s > 0$ and $\mathbf{X} \sim D_{\mathcal{L}+\mathbf{t},s}$, we have
> $$ \Pr \left[ \|\mathbf{X}\| > rs\sqrt{\frac{n}{2\pi}} \right] \le \frac{\rho_s(\mathcal{L})}{\rho_s(\mathcal{L} + \mathbf{t})} r^n e^{-\frac{n}{2}(r^2 - 1)} \le \frac{\rho_s(\mathcal{L})}{\rho_s(\mathcal{L} + \mathbf{t})} e^{-\frac{n}{2}(r - 1)^2}$$

> [!remark]
> For cryptography usage, $r$ is often chosen to be $\mathcal{w}(\sqrt{\log \lambda})$, where $\lambda$ is security parameter. In such case, the theorem yields:
> $$ \Pr \left[ \|\mathbf{X}\| > s\sqrt{n} \cdot\mathcal{w}(\sqrt{\log \lambda}) \right] \le \mathsf{negl}(\lambda)$$























