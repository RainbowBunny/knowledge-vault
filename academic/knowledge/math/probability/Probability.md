## Probability Foundations

### Random experiments & events

> [!definition] Random Experiments
> **Trial**: When we repeat a random experiment several times, we call each one of them a **trial**.

> [!definition] Sample Space
> A **sample space (or set of outcomes)** is a finite set $\Omega$. Each outcome $\omega \in \Omega$ is assigned a probability $P(\omega)$, where we require that the probability function $$P: \omega \rightarrow \mathbb R$$ satisfy the following two properties: 
> 1. $0 \leq P(w) \leq 1 \quad \forall \omega \in \Omega$
> 2. $\sum_{\omega \in \Omega} P(\omega) = 1.$

> [!definition] Event
> An **event** is any subset of $\Omega$. We assign a probability to an event $E \subset \Omega$ by setting $$P(E) = \sum_{\omega \in E} P(\omega)$$
> In particular, $P(\emptyset) = 0$ by convention, and $P(\Omega) = 1$

> [!definition] Disjoint
> We say that two events $E$ and $F$ are **disjoint** if $E \cap F = \emptyset$.

### Axiomatic Probability

> [!axiom] Axioms of Probability
> - Axiom 1: For any event $A$, $P(A) \geq 0$.
> - Axiom 2: Probability of the sample space $S$ is $P(S) = 1.$
> - Axiom 3: If $A_1, A_2, A_3, \cdots$ are disjoint events, then $P(A_1 \cup A_2 \cup A_3 \cdots) = P(A_1) + P(A_2) + P(A_3) + \cdots$

> [!example]
> Using the axioms of probability:
> 1. For any event $A$, $P(A^c) = 1 - P(A)$.
> 2. The probability of the empty set is zero, i.e., $P(\emptyset) = 0$.
> 3. For any event $A$, $P(A) \leq 1$.
> 4. $P(A - B) = P(A) - P(A \cap B)$.
> 5. $P(A \cup B) = P(A) + P(B) - P(A \cap B)$,
> 6. If $A \subset B$ then $P(A) \leq P(B)$.

> [!proposition] Continuity of probability
> 1. Let $A_1, A_2, A_3, \cdots$ be a sequence of increasing events, that is $$A_1 \subset A_2 \subset A_3 \subset \cdots$$ then $$P(\bigcup_{i = 1}^{\infty} A_i) = \lim_{n \rightarrow \infty} P(A_n).$$
> 2. Let $A_1, A_2, A_3, \cdots$ be a sequence of decreasing events, that is $$A_1 \supset A_2 \supset A_3 \supset \cdots$$ then $$P(\bigcap_{i = 1}^{\infty}) = \lim_{n \rightarrow \infty} P(A_n).$$
> 3. For any sequence of events $A_1, A_2, A_3, \cdots$ prove 
> $$P(\bigcup_{i = 1}^{\infty} A_i) = \lim_{n \rightarrow \infty} P(\bigcup_{i = 1}^n A_i),$$ 
> $$P(\bigcap_{i = 1}^{\infty} A_i) = \lim_{n \rightarrow \infty} P(\bigcap_{i = 1}^n A_i).$$ 

> [!remark]
> Idea: Let $B_1 = A_1, B_{i + 1} = A_{i + 1} - A_i$

> [!theorem] Difference Lemma
> Let $Z, W_0, W_1$ be events defined over some probability space. Suppose that $W_0 \land \overline{Z}$. Suppose that $W_0 \land \overline{Z}$ occurs if and only if $W_1 \land \overline{Z}$ occurs. Then we have $$|P[W_0] - P[W_1]| \leq P[Z].$$

### Conditional Probability

> [!definition] Conditional Probability
> If $A$ and $B$ are two events in a sample space $S$, then the **conditional probability of** $A$ **given** $B$ is defined as $$P(A | B) = \frac{P(A \cap B)}{P(B)}, \text{when } P(B) > 0.$$

> [!definition] Axiom of Probability for Conditional Probability
> - Axiom 1: For any event $A$, $P(A | B) \geq 0$.
> - Axiom 2: Conditional probability of $B$ given $B$ is $1$, i.e., $P(B | B) = 1$.
> - Axiom 3: If $A_1, A_2, A_3, \cdots$ are disjoint events, then $$P(A_1 \cup A_2 \cup A_3 \cdots | B) = P(A_1 | B) + P(A_2 | B) + P(A_3 | B) + \cdots$$

> [!example]
> For three events, $A$, $B$ and $C$, with $P(C) > 0$, we have
> - $P(A^c | C) = 1 - P(A | C)$;
> - $P(\emptyset | C) = 0$;
> - $P(A | C) \leq 1$;
> - $P(A - B | C) = P(A - C) - P(A \cap B | C)$;
> - $P(A \cup B | C) = P(A | C) + P(B | C) - P(A \cap B | C)$;
> - if $A \subset B$ then $P(A | C) \leq P(B | C)$.

> [!proposition] Chain Rule for Conditional Probability
> Let $A_1, A_2, \ldots, A_n$ be events with
> $$P(A_1 \cap A_2 \cap \cdots \cap A_n) > 0.$$
> Then
> $$P(A_1 \cap A_2 \cap \cdots \cap A_n)
> = P(A_1)
>   P(A_2 \mid A_1)
>   P(A_3 \mid A_1 \cap A_2)
>   \cdots
>   P(A_n \mid A_1 \cap \cdots \cap A_{n-1}).$$

> [!theorem] Law of Total Probability
> 1. If $B_1, B_2, B_3, \cdots$ is a partition of the sample space $S$, then for any event $A$, we have: $$P(A) = \sum_{i} P(A \cap B_i) = \sum_{i} P(A | B_i) P(B_i)$$
> 2. Continuous version: $$P(A) = \int_{-\infty}^\infty P(A | X = x) f_X(x) dx$$

> [!theorem] Bayes's Rule
> - For any two events $A$ and $B$, where $P(A) \neq 0$, we have $$P(B | A) = \frac{P(A | B) P(B)}{P(A)}.$$
> - If $B_1, B_2, B_3, \cdots$ form a partition of the sample space $S$, and $A$ is any event with $P(A) \neq 0$, we have $$P(B_j | A) = \frac{P(A | B_j) P(B_j)}{\sum_i P(A | B_i) P(B_i)}$$

### Independence

> [!definition] Independence
> Two events $A$ and $B$ are independent if $P(A \cap B) = P(A) P(B)$.
> If $P(B) \neq 0$, then $P(A | B) = P(A)$.
> For $n$ events $A_1, A_2, \cdots, A_n$ to be independent, we must have
> $$P(A_i \cap A_j) = P(A_i) P(A_j), \forall i, j \in \{1, 2, \cdots, n\};$$
> $$P(A_i \cap A_j \cap A_k) = P(A_i) P(A_j) P(A_k), \forall i, j, k \in \{1, 2, \cdots, n\};$$
> $$\vdots$$
> $$P(A_1 \cap A_2 \cap A_3 \cdots \cap A_n = P(A_1) P(A_2) P(A_3) \cdots P(A_n).$$

> [!lemma]
> If $A$ and $B$ are independent then
> - $A$ and $B^c$ are independent,
> - $A^c$ and $B$ are independent,
> - $A^c$ and $B^c$ are independent.

> [!proposition]
> If $A_1, A_2, \cdots, A_n$ are independent then
> $$P(A_1 \cup A_2 \cup \cdots \cup A_n) = 1 - (1 - P(A_1))(1 - P(A_2)) \cdots (1 - P(A_n))$$

> [!lemma]
> Consider two events $A$ and $B$, with $P(A) \neq 0$ and $P(B) \neq 0$. If $A$ and $B$ are disjoint, then they are **not** independent.

> [!definition] Conditional Independent
> Two events $A$ and $B$ are **conditional independent** given an event $C$ with $P(C) > 0$ if $$P(A \cap B | C) = P(A | C) P(B | C)$$
> If $A$ and $B$ are conditionally independent given $C$, then $$P(A | B,C) = P(A | C)$$

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

## Expectation & moments

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

## Convergence

### Convergence in Distribution

> [!definition] Convergence in Distribution
> A sequence of random variables $X_1, X_2, X_3, \dots$ converges **in distribution** to a random variable $X$, shown by $X_n \xrightarrow{d} X$, if $$\lim_{n \rightarrow \infty} F_{X_n}(x) = F(x),$$ for all $x$ at which $F_X(x)$ is continuous.

### Convergence in Probability

> [!definition] Convergence in Probability
> A sequence of random variables $X_1, X_2, X_3, \dots$ converges **in probability** to a random variable $X$, shown by $X_n \xrightarrow{p} X$, if $$\lim_{n \rightarrow \infty} P(|X_n - X| \geq \epsilon) = 0, \forall \epsilon > 0.$$

> [!theorem]
> If $X_n \xrightarrow{d} c$, where $c$ is a constant, then $X_n \xrightarrow{p} c$.

### Convergence in Mean

> [!definition] Convergence in Mean
> Let $r \geq 1$ be a fixed number. A sequence of random variables $X_1, X_2, X_3, \dots$ converges **in the $r$-th mean** or **in the $L^r$ norm** to a random variable $X$, shown by $X_n \xrightarrow{L^r} X$, if $$\lim_{n \rightarrow \infty} E(|X_n - X|^r) = 0.$$
> If $r = 2$, it is called the **mean-square convergence**, and it is shown by $X_n \rightarrow{m.s.} X$.

> [!theorem]
> Let $1 \leq r \leq s$. If $X_n \xrightarrow{L^s} X$, then $X_n \xrightarrow{L^r} X$.

> [!theorem]
> If $X_n \xrightarrow{L^r} X$ for some $r \geq 1$, then $X_n \xrightarrow{p} X$.

### Almost Sure Convergence

> [!definition] Almost Sure Convergence
> A sequence of random variables $X_1, X_2, X_3, \dots$ converges **almost surely** to a random variable $X$, shown by $X_n \xrightarrow{a.s.} X$ if $$P(\{s \in S: \lim_{n \rightarrow \infty} X_n(s) = X(s)\}) = 1$$

> [!theorem]
> Consider the sequence $X_1, X_2, X_3, \dots$. If for all $\epsilon > 0$, we have $$\sum_{i = 1}^\infty P(|X_n - X| > \epsilon) < \infty,$$ then $X_n \xrightarrow{a.s.} X$.

> [!theorem]
> Consider the sequence $X_1, X_2, X_3, \dots$. For any $\epsilon > 0$, define the set of events $$A_m = \{|X_n - X| < \epsilon, \forall n \geq m\}.$$
> Then $X_n \xrightarrow{a.s.} X$ if and only if for any $\epsilon > 0$, we have $$\lim_{m \rightarrow \infty} P(A_m) = 1.$$

> [!theorem] The Strong Law of Large Number
> Let $X_1, X_2, \dots, X_n$ be i.i.d. random variables with a finite expected value $E[X_i] = \mu < \infty$. Let also $$M_n = \frac{X_1 + X_2 + \dots + X_n}{n}.$$
> Then $M_n \xrightarrow{a.s.} \mu$.

> [!theorem]
> Let $X_1, X_2, X_3, \dots$ be a sequence of random variables. Let also $h: \mathbb R \mapsto \mathbb R$ be a continuous function. Then, the following statements are true:
> 1. If $X_n \xrightarrow{d} X$, then $h(X_n) \xrightarrow{d} h(X)$.
> 2. If $X_n \xrightarrow{p} X$, then $h(X_n) \xrightarrow{p} h(X)$.
> 3. If $X_n \xrightarrow{a.s.} X$, then $h(X_n) \xrightarrow{a.s.} h(X)$.
 
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


## Example

### The Birthday Paradox

> [!question]
> In a random group of 40 people, consider the following two questions
> 1. What is the probability that someone has the same birthday as you?
> 2. What is the probability that at least two people share the same birthday?

> [!remark] Answer
> 1. Answer: $1 - (\frac{364}{365})^{40} \approx 10.4\%$
> 2. Answer: $1 - \frac{365}{365} \cdot \frac{364}{365} \cdot \frac{363}{365} \cdots \frac{326}{365} \approx 89.1\%$

### Coupon Collector's Problem

> [!example] Coupon Collector's problem
> Suppose that there are $N$ different types of coupons. Each time you get a coupon, it is equally likely to be any of the $N$ possible types. Let $X$ be the number of coupons you will need to get before having observed each coupon at least once.
> 1. $X = X_0 + X_1 + \cdots + X_{N - 1}$, where $X_i \sim \text{Geometric}(\frac{N - i}{N})$ ($X_i$ is the number of coupon to get $i$ to $i + 1$ types).
> 2. $E[X] = N \sum_{k = 1}^N \frac{1}{k}$

### Streaks

> [!example] Streaks
> Suppose you flip a fair coin $n$ times. The longest streak of consecutive heads that you expect to see $\Theta(\lg n)$.

### Variance of Geometric Distribution
 
> [!example] Variance of Geometric Distribution
> Let $X \sim \text{Geometric}(p)$. We have $X = 1 + (1 - p) X'$ where $X' \sim \text{Geometrix}$, thus:
> $$E[X^2] = 1 + 2 (1 - p) E[X] + (1 - p)^2 E[x]^2 \rightarrow E[X^2] = \frac{2 - p}{p^2}$$

