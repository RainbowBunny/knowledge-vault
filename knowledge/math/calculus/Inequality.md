
## Real Number

> [!theorem] Cauchy-Schwarz Inequality
> If $a_1, \dots, a_n$ and $b_1, \dots, b_n$ are arbitrary real numbers, we have $$(\sum_{k = 1}^n a_k b_k)^2 \leq (\sum_{k = 1}^n a_k^2) (\sum_{k = 1}^n b_k^2).$$ The equality sign holds if and only if there is a real number $x$ such that $a_k x + b_k = 0$ for each $k = 1, 2, \dots, n$.

> [!theorem] Bernoulli's inequality
> Let $a_1, \dots, a_n$ be $n$ real numbers, all having the same sign and all greater than $-1$, $$(1 + a_1)(1 + a_2) \cdots (1 + a_n) \leq 1 + a_1 + a_2 + \cdots + a_n.$$
> When $a_1 = a_2 = \cdots = a_n = x$, where $x > -1$, we have the Bernoulli's inequality:
> $$(1 + x)^n \geq 1 + nx$$
> When $n > 1$, the inequality holds only for $x = 0$.


## Different Types of Averages

> [!definition] $p$th Power Mean
> Let $x_1, x_2, \dots, x_n$ be $n$ positive real numbers. If $p$ is a nonzero integer, the $p$th-power mean $M_p$ of the $n$ numbers is defined as follow: $$M_p = (\frac{x_1^p + \cdots + x_n^p}{n})^{1/p}.$$ The number $M_1$ is also called the **arithmetic mean**, $M_2$ the **root mean square**, and $M_{-1}$ the **harmonic mean**.

> [!proposition]
> If $p > 0$ and $x_1, x_2, \dots, x_n$ are not all equal, $$M_p < M_{2p}.$$

> [!definition] Geometric Mean
> The **geometric mean** $G$ of $n$ positive real numbers $x_1, \dots, x_n$ is defined by the formula $G = (x_1 x_2 \cdots x_n)^{1/n}$.
> 1. Let $M_p$ be the $p$th power mean, then $G \leq M_1$ and $G = M_1$ only when $x_1 = x_2 = \cdots = x_n$.
> 2. Let $p$ and $q$ be integers, $q < 0 < p$. $$M_q < G < M_p$$ when $x_1, x_2, \dots, x_n$ are not all equal.



## Factorial

> [!proposition]
> If $n \geq 2$, let $k = \lfloor n/2 \rfloor$: $$n!/n^n \leq (\frac{1}{2})^k$$

## Mean-Value Theorem

> [!example]
> 1. $|\sin x - \sin y| \leq |x - y|$.
> 2. $ny^{n - 1} (x - y) \leq x^n - y^n \leq nx^{n - 1} (x - y) \quad \text{if} 0 < y \leq x, \quad n = 1, 2, 3, \dots.$


## Hmm

> [!example]
> Given $n$ real numbers $a_1, \cdots, a_n$. Prove that the sum $\sum_{k = 1}^n (x - a_k)^2$ is smallest when $x$ is the arithmetic mean of $a_1, \dots, a_n$.


## Function Analysis

### Convex/Concave Function

> [!definition] Convex Function
> A function $g$ is said to be **convex** on an interval $[a, b]$ if, for all $x$ and $y$ in $[a, b]$ and for every $\alpha$ satisfying $0 < \alpha < 1$, we have $$g(z) \leq \alpha g(y) + (1 - \alpha) g(x), \quad \text{where} \quad z = \alpha y + (1 - \alpha) x.$$ We say $g$ is **concave** on $[a, b]$ if the reverse inequality holds, $$g(z) \geq \alpha g(y) + (1 - \alpha) g(x), \quad \text{where} \quad z = \alpha y + (1 - \alpha) x.$$

> [!theorem]
> Let $A(x) = \int_a^x f(t) dt$. Then $A$ is convex on every interval where $f$ is increasing, and concave on every interval where $f$ is decreasing.

> [!theorem] Derivative test for Convexity
> Assume $f$ is continuous on $[a, b]$ and has a derivative in the open interval $(a, b)$. If $f'$ is increasing on $(a, b)$, then $f$ is convex on $[a, b]$. In particular, $f$ is convex if $f''$ exists and is nonnegative in $(a, b)$.
> 

## Jensen's Inequality

> [!theorem] Jensen's Inequality
> Suppose that $F$ is concave on an interval $I$, and let $\alpha_1, \alpha_2, \dots, \alpha_n$ be nonnegative numbers satisfying $$\alpha_1 + \alpha_2 + \cdots + \alpha_n = 1.$$ Then $$\sum_{i = 1}^n \alpha_i F(t_i) \leq F(\sum_{i = 1}^n \alpha_i t_i) \qquad \forall t_1, t_2, \dots, t_n \in I.$$ Further, equality holds if and only if $t_1 = t_2 = \cdots = t_n.$
