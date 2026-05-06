
## Basic Definition

> [!definition] Entropy
> The **entropy** $H(X)$ of a discrete random variable $X$ is defined by $$H(X) = -\sum_{x \in \mathcal X} p(x) \log p(x).$$

> [!remark]
> - If the base of the logarithm is $b$, we denote the entropy as $H_b(X)$.
> - If the base of the logarithm is $e$, the entropy is measured in *nats*.
> - If the base of the logarithm is $2$, the entropy is measured in bits.

> [!remark]
> - $H(x) = E_p[\log \frac{1}{p(X)}]$.

> [!lemma]
> 1. $H(x) \geq 0$.
> 2. $H_b(x) = (\log_b a) H_a(X)$.

> [!theorem] Chain Rule for Entropy
> Let $X_1, X_2, \dots, X_n$ be drawn according to $p(x_1, x_2, \dots, x_n)$. Then $$H(X_1, X_2, \dots X_n) = \sum_{i = 1}^n H(X_i | X_{i - 1}, \dots, X_1).$$

### Joint Entropy

> [!definition] Joint Entropy
> The **joint entropy** $H(X, Y)$ of a pair of discrete random variables $(X, Y)$ with a joint distribution $p(x, y)$ is defined as $$H(x, y) = -\sum_{x \in \mathcal X} \sum_{y \in \mathcal Y} p(x, y) \log p(x, y),$$ which can also be expressed as $$H(x, y) = -E_p [\log p(X, Y)].$$

### Conditional Entropy

> [!definition] Conditional Entropy
> If $(X, Y) \sim p(x, y)$, the **conditional entropy** $H(Y | X)$ is defined as $$\begin{align}H(Y | X) &= \sum_{x \in \mathcal X} p(x) H(Y | X = x)\\&= -\sum_{x \in \mathcal X} p(x) \sum_{y \in \mathcal Y} p(y | x) \log p(y | x)\\&= -\sum_{x \in \mathcal X} \sum_{y \in \mathcal Y} p(x, y) \log p(y | x)\\ &= -E_p[\log p(Y | X)]\end{align}$$

> [!theorem] Chain Rule
> $$H(X, Y) = H(X) + H(Y | X)$$

> [!corollary]
> $$H(X, Y | Z) = H(X | Z) + H(Y | X, Z)$$

### Relative Entropy

> [!definition] Relative Entropy
> The **relative entropy** or **Kullback-Leibler distance** between two probability mass function $p(x)$ and $q(x)$ is defined as $$\begin{align}D(p || q) &= \sum_{x \in \mathcal X} p(x) \log \frac{p(x)}{q(x)}\\ &= E_p[\log \frac{p(X)}{q(X)}]\end{align}.$$

> [!theorem] Chain Rule for Relative Entropy
> $$D(p(x, y) || q(x, y)) = D(p(x) || q(x)) + D(p(y | x) || q(y | x)).$$

### Mutual Information

> [!definition] Mutual Information
> Consider two random variables $X$ and $Y$ with a joint probability mass function $p(x, y)$ and marginal probability mass functions $p(x)$ and $p(y)$. The **mutual information** $I(X; Y)$ is the relative entropy between the joint distribution and the product distribution $p(x) p(y)$: $$\begin{align}I(X; Y) &= \sum_{x \in \mathcal X} \sum_{y \in \mathcal Y} p(x, y) \log \frac{p(x, y)}{p(x) p(y)} \\ &= D(p(x, y) || p(x) p(y)) \\ &= E_{p(x, y)} \log \frac{p(X, Y)}{p(X) p(Y)}.\end{align}$$

> [!theorem] Mutual Information and Entropy
> $$\begin{align}
> I(X; Y) &= H(X) - H(X | Y) \\
> I(X; Y) &= H(Y) - H(Y | X) \\
> I(X; Y) &= H(X) + H(Y) - H(X, Y) \\
> I(X; Y) &= I(Y; X) \\
> I(X; X) &= H(X)
> \end{align}$$

> [!theorem] Chain Rule for Information
> $$I(X_1, X_2, \dots, X_n; Y) = \sum_{i = 1}^n I(X_i; Y | X_{i - 1}, X_{i - 2}, \dots, X_1).$$

### Conditional Mutual Information

> [!definition] Conditional Mutual Information
> The **conditional mutual information** of random variables $X$ and $Y$ given $Z$ is defined by $$\begin{align}I(X; Y | Z) &= H(X | Z) - H(X | Y, Z) \\ &= E_{p(x, y, z)} \log \frac{p(X, Y | Z)}{p(X | Z) p(Y | Z)}.\end{align}$$ 

### Conditional Relative Entropy

> [!definition] Conditional Relative Entropy
> For joint probability mass functions $p(x, y)$ and $q(x, y)$, the **conditional relative entropy** $D(p(y | x) || q(y | x))$ is the average of the relative entropies between the conditional probability mass functions $p(y | x)$ and $q(y | x)$ averaged over the probability mass function $p(x)$. More precisely, $$\begin{align}D(p(y | x) || q(y | x)) &= \sum_{x} p(x) \sum_{y} p(y | x) \log \frac{p(y | x)}{q(y | x)} \\ &= E_{p(x, y)} \log \frac{p(Y | X)}{q(Y | X)}.\end{align}$$

## Special Property

### Consequence of Jensen Inequality

> [!theorem] Information Inequality
> Let $p(x), q(x), x \in \mathcal X$, be two probability mass function. Then $$D(p || q) \geq 0$$ with equality if and only if $p(x) = q(x)$ for all $x$.

> [!corollary] Nonnegativity of Mutual Information
> For any two random variables, $X$, $Y$, $$I(X; Y) \geq 0,$$ with equality if and only if $X$ and $Y$ are indepedent.

> [!corollary]
> $$D(p(y | x) || q(y | x)) \geq 0,$$ with equality if and only if $p(y | x) = q(y | x)$ for all $y$ and $x$ such that $p(x) > 0$.

> [!corollary]
> $$I(X; Y | Z) \geq 0,$$ with equality if and only if $X$ and $Y$ are conditionally independent given $Z$.

> [!theorem]
> $H(X) \leq \log |\mathcal X|$, where $|\mathcal X|$ denotes the number of elements in the range of $X$, with equality if and only if $X$ has a uniform distribution over $\mathcal X$.

> [!theorem] Conditioning Reduces Entropy
> $$H(X | Y) \leq H(X)$$ with equality if and only if $X$ and $Y$ are independent.

> [!theorem] Independence Bound on Entropy
> Let $X_1, X_2, \dots, X_n$ be drawn according to $p(x_1, x_2, \dots, x_n)$. Then $$H(X_1, X_2, \dots, X_n) \leq \sum_{i = 1}^n H(X_i)$$ with equality if and only if the $X_i$ are independent.

### Log Sum Inequality

> [!theorem] Log Sum Inequality
> For nonnegative numbers, $a_1, a_2, \dots, a_n$ and $b_1, b_2, \dots, b_n$, $$\sum_{i = 1}^n a_i \log \frac{a_i}{b_i} \geq (\sum_{i = 1}^n a_i) \log \frac{\sum_{i = 1}^n a_i}{\sum_{i = 1}^n b_i}$$ with equality if and only if $\frac{a_i}{b_i} = \text{const}$.

> [!theorem] Convexity of Relative Entropy
> $D(p || q)$ is convex in the pair $(p, q)$; that is, if $(p_1, q_1)$ and $(p_2, q_2)$ are two pairs of probability mass functions, then $$D(\lambda p_1 + (1 - \lambda) p_2 || \lambda q_1 + (1 - \lambda) q_2) \leq \lambda D(p_1 || q_1) + (1 - \lambda) D(p_2 || q_2)$$ for all $0 \leq \lambda \leq 1$.

> [!theorem] Concavity of Entropy
> $H(p)$ is a concave function of $p$.

> [!theorem]
> Let $(X, Y) \sim p(x, y) = p(x) p(y | x)$. The mutual information $I(X; Y)$ is a concave function of $p(x)$ for fixed $p(y | x)$ and a convex function of $p(y | x)$ for fixed $p(x)$.

### Data-Processing Inequality

> [!definition] Form Markov Chain
> Random variables $X, Y, Z$ are said to **form a Markov chain in that order** (denoted by $X \rightarrow Y \rightarrow Z$) if the conditional distribution of $Z$ depends only on $Y$ and is conditionally independent of $X$. Specifically, $X, Y$, and $Z$ form a Markov chain $X \rightarrow Y \rightarrow Z$ if the joint probability mass function can be written as $$p(x, y, z) = p(x) p(y | x) p(z | y).$$

> [!theorem] Data-processing Inequality
> If $X \rightarrow Y \rightarrow Z$, then $I(X; Y) \geq I(X; Z)$.

> [!corollary]
> In particular, if $Z = g(Y)$, we have $I(X; Y) \geq I(X; g(Y))$.

> [!corollary]
> If $X \rightarrow Y \rightarrow Z$, then $I(X; Y | Z) \leq I(X; Y)$.

### Sufficient Statistics

> [!definition] Sufficient Statistics
> A function $T(X)$ is said to be a **sufficient statistic** relative to the family $\{f_{\theta}(x)\}$ if $X$ is independent of $\theta$ given $T(X)$ for any distribution on $\theta$ (i.e., $\theta \rightarrow T(X) \rightarrow X$ forms a Markov chain).

> [!definition] Minimal Sufficient Statistics
> A statistic $T(X)$ is a **minimal sufficient statistics** relative to $\{f_{\theta}(x)\}$ if it is a function of every other sufficient statistic $U$. Interpreting this in terms of the data-processing inequality, this implies that $$\theta \rightarrow T(X) \rightarrow U(X) \rightarrow X.$$

### Fano's Inequality

> [!theorem] Fano's Inequality
> For any estimator $\hat{X}$ such that $X \rightarrow Y \rightarrow \hat{X}$, with $P_e = P(X \neq \hat{X})$, we have $$H(P_e) + P_e \log |\mathcal X| \geq H(X | \hat{X}) \geq H(X | Y).$$
> This inequality can be weakened to $$1 + P_e \log |\mathcal X| \geq H(X | Y)$$ or $$P_e \geq \frac{H(X | Y) - 1}{\log |\mathcal X|}.$$

> [!corollary]
> For any two random variables $X$ and $Y$, let $p = P(X \neq Y)$. $$H(p) + p \log |\mathcal X| \geq H(X | Y).$$

> [!corollary]
> Let $P_e = P(X \neq \hat{X})$, and let $\hat{X} : \mathcal Y \rightarrow \mathcal X$; then $$H(P_e) + P_e \log (|\mathcal X| - 1) \geq H(X | Y).$$

> [!lemma]
> If $X$ and $X'$ are i.i.d. with entropy $H(X)$, $$P(X = X') \geq 2^{-H(X)},$$ with equality if and only if $X$ has a uniform distribution.

> [!corollary]
> Let $X, X'$ be independent with $X \sim p(x), X' \sim r(x), x, x' \in \mathcal X$. Then $$\begin{align}P(X = X') &\geq 2^{-H(p) - D(p || r)} \\ P(X = X') &\geq 2^{-H(r) - D(r || p)}\end{align}$$ 