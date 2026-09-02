## Basic Definition

> [!definition] Odd, Even Function
> Let $f$ be a function whose domain contains $-x$ whenever it contains $x$. We say that $f$ is an **even** function if $f(-x) = f(x)$ and an **odd** function if $f(-x) = -f(x)$ for all $x$ in the domain of $f$.

### Logarithm

> [!definition] Natural Logarithm
> If $x$ is a positive real number, we define the natural logarithm of $x$, denoted temporarily by $L(x)$, to be the integral $$L(x) = \int_1^x \frac{1}{t}dt.$$

> [!proposition] Properties of Logarithm Function
> The logarithm function has the following properties:
> 1. $L(1) = 0$.
> 2. $L'(x) = \frac{1}{x} \quad \forall x > 0$.
> 3. $L(ab) = L(a) + L(b) \quad \forall a > 0, b > 0$.

> [!theorem]
> For every real number $b$ there is exactly one positive real number $a$ whose logarithm, $L(a)$, is equal to $b$.

> [!definition] Natural Logarithms
> We denote by $e$ that number for which $$L(e) = 1.$$

> [!definition] Logarithm Base $b$
> If $b > 0, b \neq 1$, and if $x > 0$, the **logarithm** of $x$ to the positive base $b \neq 1$ is the number $$\log_b x = \frac{\log x}{\log b}$$ where the logarithms on the right are natural logarithms.

> [!remark]
> $\log b = -\log (1/b)$

> [!theorem]
> Let $P_n$ denote the polynomial of degree $n$ given by $$P_n(x) = \sum_{k = 1}^n \frac{x^k}{k}.$$ Then, for every $x < 1$ and every $n \geq 1$, we have $$-\log(1 - x) = P_n(x) + \int_0^x \frac{u^n}{1 - u} du.$$

> [!theorem]
> Let $E_n(x) = \int_0^x \frac{u^n}{1 - u} du$ is the error made when we approximate $-\log (1 - x)$.
> If $0 < x < 1$, we have the inequalities $$\frac{x^{n + 1}}{n + 1} \leq E_n(x) \leq \frac{1}{1 - x} \frac{x^{n + 1}}{n + 1}.$$ If $x < 0$, the error $E_n(x)$ has the same sign as $(-1)^{n + 1}$, and we have $$0 < (-1)^{n + 1} E_n(x) \leq \frac{|x|^{n + 1}}{n + 1}.$$

> [!theorem]
> If $0 < x < 1$ and if $m \geq 1$, we have $$\log \frac{1 + x}{1 - x} = 2 (x + \frac{x^3}{3} + \cdots + \frac{x^{2m - 1}}{2m - 1}) + R_m(x),$$ where the error term $R_m(x)$, satisfies the inequalities $$\frac{x^{2m + 1}}{2m + 1} < R_m(x) \leq \frac{2 - x}{1 - x} \frac{x^{2m + 1}}{2m + 1}$$

> [!definition] Complex Logarithm
> If $z$ is a nonzero complex number, we define $\text{Log } z$, the complex logarithm of $z$, by the equation $$\text{Log } z = \log |z| + i \arg(z).$$

> [!proposition]
> 4. $\text{Log}(-1) = \pi i, \quad \text{Log}(i) = \pi i / 2$.
> 5. $\text{Log}(z_1 z_2) = \text{Log}(z_1) + \text{Log}(z_2) + 2n \pi i$, where $n$ is an integer.
> 6. $\text{Log}(z_1 / z_2) = \text{Log}(z_1) - \text{Log}(z_2) + 2n \pi i$, where $n$ is an integer.
> 7. $e^{\text{Log } z} = z$.

### Exponential Function

> [!definition] Exponential Function
> For any real $x$, we define $E(x)$ to be that number $y$ whose logarithm is $x$. That is, $y = E(x)$ means that $L(y) = x$.

> [!proposition] Properties of Exponential Function
> The exponential function has the following properties:
> 1. $E(0) = 1, \quad E(1) = e$.
> 2. $E'(x) = E(x) \quad \forall x$.
> 3. $E(a + b) = E(a)E(b) \quad \forall a, b$.

### Monotonic Function

> [!definition] Increasing, Decreasing
> A function $f$ is said to be **increasing** on a set $S$ if $f(x) \leq f(y)$ for every pair of points $x$ and $y$ in $S$ with $x < y$. If the strict inequality $f(x) < f(y)$ holds for all $x < y$ in $S$, the function is said to be **strictly increasing** on $S$. Similarly, $f$ is called **decreasing** on $S$ if $f(x) \geq f(y)$ for all $x < y$ in $S$. If $f(x) > f(y)$ for all $x < y$ in $S$, then $f$ is called **strictly decreasing** on $S$.

> [!definition] Monotonic, Strictly Monotonic, Piecewise Monotonic
> A function is called **monotonic** on $S$ if it is increasing on $S$ or if it is decreasing on $S$. The term **strictly monotonic** means that $f$ is strictly increasing on $S$ or strictly decreasing on $S$.
> A function $f$ is said to be **piecewise monotonic** on an interval if its graph consists of a finite number of monotonic pieces.

> [!proposition]
> Let $f$ be real-valued function that is monotonic increasing and bounded on the interval $[a, b]$. Define two sequences $\{s_n\}$ and $\{t_n\}$ as follow: $$s_n = \frac{b - a}{n} \sum_{k = 0}^{n - 1} f(a + \frac{k(b - a)}{n}), \quad t_n = \frac{b - a}{n} \sum_{k = 1}^n f(a + \frac{k(b - a)}{n}).$$
> 1. $s_n \leq \int_a^b f(x) dx \leq t_n$ and $0 \leq \int_a^b f(x) dx - s_n \leq \frac{f(b) - f(a)}{n}$.
> 2. $\lim_{n \rightarrow +\infty} s_n = \lim_{n \rightarrow +\infty} t_n = \int_a^b f(x) dx$.


### Lipschitz-1 Function

> [!example]
> Let $f$ be a function that $|f(u) - f(v)| \leq |u - v|$ for all $u$ and $v$ in an interval $[a, b]$.
> 1. $f$ is continuous at each point of $[a, b]$.
> 2. Assume that $f$ is integrable on $[a, b]$, then for any $c$ in $[a, b]$, $$|\int_a^b f(x) dx - (b - a) f(c)| \leq \frac{(b - a)^2}{2}$$



## Root

> [!definition] Root
> A real number $x_1$ such that $f(x_1) = 0$, is said to be a real root of the equation $f(x) = 0.$ We say that a real root of an equation has been **isolated** if we exhibit an interval $[a, b]$ containing this root and no others.