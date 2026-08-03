## Definition

> [!definition] Function
> A function $f$ is a set of ordered pairs $(x, y)$ no two of which have the same first member.

> [!definition] Domain
> For a function $f$, the set of all elements $x$ that occur as the first members of pairs $(x, y)$ in $f$ is called the **domain** of $f$.

> [!definition] Co-domain
> For a function $f$, the set of all possible elements $y$ is called the **co-domain** of $f$.

> [!definition] Range
> The **range** of a function is the set containing all the possible values of $f(x)$.

> [!theorem]
> Two function $f$ and $g$ are equal if and only if
> 1. $f$ and $g$ have the same domain, and
> 2. $f(x) = g(x)$ for every $x$ in the domain of $f$.

> [!definition] Odd, Even Function
> Let $f$ be a function whose domain contains $-x$ whenever it contains $x$. We say that $f$ is an **even** function if $f(-x) = f(x)$ and an **odd** function if $f(-x) = -f(x)$ for all $x$ in the domain of $f$.


## Basic Function

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

### Logarithmic Integral 

> [!definition] Logarithmic Integral Function
> $$\text{Li}(X) = \int_2^X \frac{dt}{\ln t}$$

> [!proposition] Properties of Logarithmic Integral Function
> 1. $\text{Li}(X) = \frac{X}{\ln X} + \int_2^X \frac{dt}{(\ln t)^2} + O(1)$
> 2. $\lim_{X \rightarrow \infty} \frac{\text{Li}(X)}{X / \ln X} = 1$

## Special Type

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

### Convex/Concave Function

> [!definition] Convex Function
> A function $g$ is said to be **convex** on an interval $[a, b]$ if, for all $x$ and $y$ in $[a, b]$ and for every $\alpha$ satisfying $0 < \alpha < 1$, we have $$g(z) \leq \alpha g(y) + (1 - \alpha) g(x), \quad \text{where} \quad z = \alpha y + (1 - \alpha) x.$$ We say $g$ is **concave** on $[a, b]$ if the reverse inequality holds, $$g(z) \geq \alpha g(y) + (1 - \alpha) g(x), \quad \text{where} \quad z = \alpha y + (1 - \alpha) x.$$

> [!theorem]
> Let $A(x) = \int_a^x f(t) dt$. Then $A$ is convex on every interval where $f$ is increasing, and concave on every interval where $f$ is decreasing.

> [!theorem] Derivative test for Convexity
> Assume $f$ is continuous on $[a, b]$ and has a derivative in the open interval $(a, b)$. If $f'$ is increasing on $(a, b)$, then $f$ is convex on $[a, b]$. In particular, $f$ is convex if $f''$ exists and is nonnegative in $(a, b)$.
> 

> [!theorem] Jensen's Inequality
> If $f$ is a convex function and $X$ is a random variable, $$E[f(X)] \geq f(E[X]).$$
> Moreover, if $f$ is strictly convex, the equality implies that $X = E[X]$ with probability $1$ ($X$ is a constant).

> [!theorem] Jensen's Inequality
> Suppose that $F$ is concave on an interval $I$, and let $\alpha_1, \alpha_2, \dots, \alpha_n$ be nonnegative numbers satisfying $$\alpha_1 + \alpha_2 + \cdots + \alpha_n = 1.$$ Then $$\sum_{i = 1}^n \alpha_i F(t_i) \leq F(\sum_{i = 1}^n \alpha_i t_i) \qquad \forall t_1, t_2, \dots, t_n \in I.$$ Further, equality holds if and only if $t_1 = t_2 = \cdots = t_n.$

### Composition Function

> [!definition] Composition
> $f(x)$ is obtained by combining two other functions $u$ and $v$ by the formula $$f(x) = u[v(x)].$$ We say that $f$ is the **composition** of $u$ and $v$ (in that order). We denote the composition by $f = u \circ v$.

### Inversion Function

> [!definition] Inverse
> For a function $f$ with domain $A$ and range $B$. For each $x$ in $A$, there is exactly one $y$ in $B$ such that $y = f(x)$. For each $y$ in $B$, there is at least one $x$ in $A$ such that $f(x) = y$. Suppose that there is **exactly one** such $x$. Then we can define a new function $g$ on $B$ as follows: $$g(y) = x \quad \text{means} \quad y = f(x).$$ This new function $g$ is called the **inverse** of $f$. The process by which $g$ is obtained from $f$ is called **inversion**.

## Root

> [!definition] Root
> A real number $x_1$ such that $f(x_1) = 0$, is said to be a real root of the equation $f(x) = 0.$ We say that a real root of an equation has been **isolated** if we exhibit an interval $[a, b]$ containing this root and no others.

## Special Function

### Lipschitz-1 Function

> [!example]
> Let $f$ be a function that $|f(u) - f(v)| \leq |u - v|$ for all $u$ and $v$ in an interval $[a, b]$.
> 1. $f$ is continuous at each point of $[a, b]$.
> 2. Assume that $f$ is integrable on $[a, b]$, then for any $c$ in $[a, b]$, $$|\int_a^b f(x) dx - (b - a) f(c)| \leq \frac{(b - a)^2}{2}$$

### Lambda Function

> [!definition] Lambda Function
> **Lambda Function** define by a modification of Euler's $\phi$-function:
> 1. $\lambda(p^a) = \phi(p^a)$ when $p$ is an odd prime;
> 2. $\lambda(2^a) = \phi(2^a)$ if $a = 0, 1,$ or $2$;
> 3. $\lambda(2^a) = \frac{1}{2} \phi(2^a)$ if $a > 2$;
> 4. $\lambda(2^a p_1^{a_1} \cdots p_i^{a_i}) = \text{the lowest common multiple of } \lambda(2^a), \lambda(p_1^{a_1}), \cdots, \lambda(p_i)^{a_i}$ with $p_1, \cdots, p_i$ being different odd primes.

### Gamma

> [!definition] Gamma Function
> The **gamma function** $\Gamma(\alpha)$ is defined for $\alpha > 0$ by the integral $$\Gamma(\alpha) = \int_{0}^{\infty} x^{\alpha - 1} e^{-x} dx$$

> [!proposition] Properties of the Gamma Function 
> For any positive real number $\alpha$:
> 1. $\int_0^{\infty} x^{\alpha - 1} e^{-\lambda x} dx = \frac{\Gamma(\alpha)}{\lambda^{\alpha}},$ for $\lambda > 0$;
> 2. $\Gamma(1) = 1$ and $\Gamma(\alpha + 1) = \alpha \Gamma(\alpha)$;
> 3. $\Gamma(n) = (n - 1)!$, for $n = 1, 2, 3, \cdots;$
> 4. $\Gamma(\frac{1}{2}) = \sqrt{\pi}$
> 5. **Stirling's formula**: For large values of $s$ we have $$\Gamma(1 + s)^{1/s} \approx \frac{s}{e}$$ (More precisely, $\ln \Gamma(1 + s) = \ln(s/e)^s + \frac{1}{2} \ln (2 \pi s) + O(1)$ as $s \rightarrow \infty$.)

### Bessel Function

> [!definition] Bessel Function of the first kind
> The function $J_0$ and $J_1$ defined by the series $$J_0(x) = \sum_{n = 0}^\infty (-1)^n \frac{x^{2n}}{(n!)^2 2^{2n}}, \quad J_1(x) = \sum_{n = 0}^\infty (-1)^n \frac{x^{2n + 1}}{n!(n + 1)! 2^{2n + 1}}$$ are called **Bessel functions of the first kind** of orders zero and one, respectively.

> [!proposition] Properties of the Bessel Function
> 1. $J_0$ and $J_1$ converge for all real $x$;
> 2. $J'_0(x) = -J_1(x)$
> 3. $j_0(x) = j'_1(x)$, where $j_0(x) = xJ_0(x)$ and $j_1(x) = x J_1(x)$.

> [!definition] Bessel's Equation
> The differential equation $$x^2 y'' + xy' + (x^2 - n^2)y = 0$$ is called **Bessel's equation**. Then, $J_0$ and $J_1$ are solutions when $n = 0$ and $1$, respectively.

### Dirac Delta Function

> [!definition] Unit Step Function
> The unit step function $u(x)$ defined by $$u(x) = \begin{cases}1 \quad &x \geq 0 \\ 0 & \text{otherwise}\end{cases}.$$ 
> 

> [!proposition] 
> To remove the jump, define for any $\alpha > 0$ the function $u_\alpha$ as $$u_\alpha (x) = \begin{cases}1 & x > \frac{\alpha}{2} \\ \frac{1}{\alpha} (x + \frac{\alpha}{2}) & -\frac{\alpha}{2} \leq x \leq \frac{\alpha}{2} \\ 0 & x < -\frac{\alpha}{2}\end{cases}$$
> Because $u_\alpha(x)$ is a continuous function, we can define the derivative of $u_\alpha(x)$ whenever it exists: $$\delta_\alpha(x) = \frac{du_\alpha(x)}{dx} = \begin{cases}\frac{1}{\alpha} &|x| < \frac{\alpha}{2} \\ 0 &|x| > \frac{\alpha}{2} \end{cases}$$

> [!definition] Dirac Delta Function
> We notice that $$u(x) = \lim_{\alpha \rightarrow 0} u_\alpha(x),$$ Then we can define $$\delta(x) = \lim_{\alpha \rightarrow 0} \delta_\alpha(x)$$

> [!lemma]
> Let $g: \mathbb R \rightarrow \mathbb R$ be a continuous function. We have $$\int_{-\infty}^\infty g(x) \delta(x - x_0) dx = g(x_0).$$

> [!definition] Properties of the delta function
> We define the delta function $\delta(x)$ as an object with the following properties:
> 1. $\delta(x) = \begin{cases}\infty &x = 0 \\ 0 &\text{otherwise}\end{cases}$
> 2. $\delta(x) = \frac{d}{dx} u(x)$, where $u(x)$ is the unit step function;
> 3. $\int_{-\epsilon}^\epsilon \delta(x) dx = 1$, for any $\epsilon > 0$;
> 4. For any $\epsilon > 0$ and any function $g(x)$ that is continuous over $(x_0 - \epsilon, x_0 + \epsilon)$, we have $$\int_{-\infty}^\infty g(x) \delta(x - x_0) dx = \int_{x_0 - \epsilon}^{x_0 + \epsilon} g(x) \delta(x - x_0) dx = g(x_0).$$

### Von Mangoldt Function

> [!definition] Von Mangoldt Function
> $$\Lambda := \begin{cases}\log p &\text{if } n = p^m \text{ , where } p \text{ is prime} \\ 0 &\text{otherwise}\end{cases}$$
