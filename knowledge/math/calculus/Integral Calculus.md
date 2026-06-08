## Interval

> [!definition] Interval
> If $a < b$, we denoted by $[a, b]$ the set of all $x$ satisfying the inequalities $a \leq x \leq b$ and refer to this set as the **closed interval** from $a$ to $b$. 
> The corresponding **open interval**, written $(a, b)$, is the set of all $x$ satisfying $a < x < b$. The open interval $(a, b)$ is also called the **interior** of $[a, b]$.
> Half-open intervals $(a, b]$ and $[a, b)$, which include just one endpoint are defined by the inequalities $a < x \leq b$ and $a \leq x < b$, respectively.

## Partitions and Step Functions

> [!definition] Partition
> Suppose we decompose a given closed interval $[a, b]$ into $n$ subintervals by inserting $n - 1$ points of subdivision, say $x_1, x_2, \dots, x_{n - 1}$, subject to the restriction $$a < x_1 < x_2 < \cdots < x_{n - 1} < b.$$ It is convenient to denote the point $a$ itself by $x_0$ and the point $b$ by $x_n$. This is called a **partition** $P$ of $[a, b]$ and we use the symbol $$P = \{x_0, x_1, \dots, x_n\}$$ to designate this partition. The partition $P$ determines $n$ closed subintervals $$[x_0, x_1], [x_1, x_2], \dots, [x_{n - 1}, x_n].$$

> [!definition] Refinement
> A new partition $P'$ formed by adjoining more subdivision points to a given partition $P$ of $[a, b]$ is called a **refinement** of $P$ or is said to be **finer** than $P$.

## Step Function

> [!definition] Step Function
> A function $s$, whose domain is a closed interval $[a, b]$, is called a **step function** if there is a partition $P = \{x_0, x_1, \dots, x_n\}$ of $[a, b]$ such that $s$ is constant on each open subinterval of $P$. That is, for each $k = 1, 2, \dots, n$, there is a real number $s_k$ such that $$s(x) = s_k \quad \text{if} \quad x_{k - 1} < x < x_k.$$ Step functions are sometimes called **piecewise constant functions**.
> **Note:** At each of the endpoints $x_{k - 1}$ and $x_k$ the function must have some well-defined value, but this need not be the same as $s_k$.

> [!definition] Characteristic Function
> Let $S$ be a set of points on the real line. The **characteristic function** of $S$ is, by definition, the function $\chi_S(x) = 1$ for every $x$ in $S$, and $\chi_S(x) = 0$ for those $x$ not in $S$.

> [!proposition]
> Let $f$ be a step function which takes the constant value $c_k$ on the $k$-th open subinterval $I_k$ of some partition of an interval $[a, b]$. Then for $x \in I_1 \cup I_2 \dots \cup I_n$, we have $$f(x) = \sum_{k = 1}^n c_k \chi_{I_k}(x).$$

## Integral

> [!definition] Integral of Step Functions
> The integral of $s$ from $a$ to $b$, denoted by the symbol $\int_a^b s(x) dx$, is defined by the following formula: $$\int_a^b s(x) dx = \sum_{k = 1}^n s_k (x_k - x_{k - 1}).$$

| Property                                                | Description                                                                                                                                                               |
| ------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Additive Property                                       | $\int_a^b [f(x) + g(x)] dx = \int_a^b f(x) dx + \int_a^b g(x) dx$                                                                                                         |
| Homogeneous                                             | $\int_a^b c \cdot f(x) dx = c \int_a^b f(x) dx \quad \forall c \in \mathbb R$                                                                                             |
| Linearity Property                                      | $\int_a^b [c_1 f(x) + c_2 g(x)] dx = c_1 \int_a^b f(x) dx + c_2 \int_a^b g(x) dx \quad \forall c_1, c_2 \in \mathbb R$                                                    |
| Comparison Theorem                                      | If $g(x) \leq f(x)$ for every $x \in [a, b]$, then $\int_a^b g(x) dx \leq \int_a^b f(x) dx$                                                                               |
| Additivity with Respect to the Interval of Integration  | $\int_a^c f(x) dx + \int_c^b f(x) dx = \int_a^b f(x) dx \quad \text{if} \quad a < c < b$<br>Or sometimes:<br>$\int_a^c f(x) dx + \int_c^b f(x) dx + \int_b^a f(x) dx = 0$ |
| Invariance Under Translation                            | $\int_a^b f(x) dx = \int_{a + c}^{b + c} f(x - c) dx \quad \forall c \in \mathbb R$<br>Or sometimes:<br>$\int_{a+c}^{b+c} f(x) dx = \int_a^b f(x + c) dx$                 |
| Expansion or Contraction of the Interval of Integration | $\int_{ka}^{kb} f(\frac{x}{k}) dx = k \int_{a}^b f(x) dx \quad \forall k \neq 0$.<br>Or sometimes:<br>$\int_{ka}^{kb} f(x) dx = k \int_a^b f(kx) dx$                      |
|                                                         | $\int_b^a s(x) dx = -\int_a^b s(x) dx \quad \text{if} \quad a < b$                                                                                                        |
|                                                         | $\int_a^a s(x) dx = 0$                                                                                                                                                    |
| Reflection Property                                     | $\int_a^b s(x) dx = \int_{-b}^{-a} s(-x) dx$                                                                                                                              |
|                                                         | For even $f$, $\int_{-b}^b f(x) dx = 2 \int_0^b f(x) dx$<br>For odd $f$, $\int_{-b}^b f(x)dx = 0$                                                                         |
|                                                         | $\int_a^b f(x) dx = (b - a) \int_0^1 f[a + (b - a)x] dx$                                                                                                                  |
|                                                         | $\int_a^b f(Ax + B) dx = \frac{1}{A} \int_{Aa + B}^{Ab + B} f(u) du$                                                                                                      |
|                                                         | $\int_a^b f(c - x) dx = \int_{c - b}^{c - a} f(x) dx$                                                                                                                     |
|                                                         |                                                                                                                                                                           |


> [!definition] Integral of a Bounded Function
> Let $f$ be a function defined and bounded on $[a, b]$. Let $s$ and $t$ denote arbitrary step function defined on $[a, b]$ such that $$s(x) \leq f(x) \leq t(x)$$ for every $x$ in $[a, b]$. If there is one and only one number $I$ such that $$\int_a^b s(x) dx \leq I \leq \int_a^b t(x) dx$$ for every pair of steps functions $s$ and $t$, then this number $I$ is called the integral of $f$ from $a$ to $b$, and denoted by the symbol $\int_a^b f(x) dx$. When such an $I$ exists, the function $f$ is said to be **integrable** on $[a, b]$.
> The function $f$ is called the **integrand**, the numbers $a$ and $b$ are called the **limits of integration**, and the interval $[a, b]$ the **interval of integration**.

> [!theorem] 
> Every function $f$ which is bounded on $[a, b]$ has a **lower** integral $\underline{I}(f)$ and an **upper** integral $\overline{I}(f)$ satisfying the inequalities $$\int_a^b s(x) dx \leq \overline{I}(f) \leq \underline{I}(f) \leq \int_a^b t(x) dx$$ for all step function $s$ and $t$ with $s \leq f \leq t$. The function $f$ is integrable on $[a, b]$ if and only if its upper and lower integrals are equal, in which case we have $$\int_a^b f(x) dx = \underline{I}(f) = \overline{I}(f).$$

> [!theorem]
> Let $f$ be a nonnegative function, integrable on an interval $[a, b]$. Then the graph of $f$: $$\{(x, y) \mid a \leq x \leq b, y = f(x)\},$$ is measurable and has area equal to $0$.

> [!question]
> 1. Which bounded function are integrable?
> 2. Given that a function $f$ is integrable, how do we compute the integral of $f$?

> [!theorem]
> If $f$ is monotonic on a closed interval $[a, b]$, then $f$ is integrable on $[a, b]$.

> [!theorem]
> Assume $f$ is increasing on a closed interval $[a, b]$. Let $x_k = a + k(b - a)/n$ for $k = 0, 1, \dots, n$. If $I$ is any number which satisfies the inequalities $$\frac{b - a}{n} \sum_{k = 0}^{n - 1} f(x_k) \leq I \leq \frac{b - a}{n} \sum_{k = 1}^n f(x_k)$$ for every integer $n \geq 1$, then $I = \int_a^b f(x) dx$.

> [!theorem]
> Assume $f$ is decreasing on $[a, b]$. Let $x_k = a + k(b - a)/n$ for $k = 0, 1, \dots, n$. If $I$ is any number which satisfies the inequalities $$\frac{b - a}{n} \sum_{k = 1}^n f(x_k) \leq I \leq \frac{b - a}{n} \sum_{k = 0}^{n - 1} f(x_k)$$ for every integer $n \leq 1$, then $I = \int_a^b f(x) dx$.

> [!theorem]
> If $p$ is a positive integer and $b > 0$, we have $$\int_0^b x^p dx = \frac{b^{p + 1}}{p + 1}$$

> [!theorem]
> For $a > 0$, $b > 0$ and $n$ a positive integer, we have $\int_a^b x^{1/n} dx = \frac{b^{1 + 1/n} - a^{1 + 1/n}}{1 + 1/n}$

## Application

### The area of a region between two graphs expressed as an integral

> [!theorem] 
> Assume $f$ and $g$ are integrable and satisfy $f \leq g$ on $[a, b]$. Then the region $S$ between their graphs is measurable and its area $a(S)$ is given by the integral $$a(s) = \int_a^b [g(x) - f(x)] dx$$

> [!proposition]
> $$\pi = 2\int_{-1}^1 \sqrt{1 - x^2} dx$$

### The integral for area in polar coordinates

> [!proposition]
> If a function $f$ is periodic with period $p > 0$ and integrable on $[0, p]$, then for all $a$: $$\int_0^p f(x) dx = \int_a^{a + p} f(x) dx.$$

> [!definition] Radial Set
> Let $f$ be a nonnegative function defined on an interval $[a, b]$, where $0 \leq b - a \leq 2 \pi$. The set of all points with polar coordinates $(r, \theta)$ satisfying the inequalities $$0 \leq r \leq f(\theta), \quad a \leq \theta \leq b,$$ is called the **radial set** of $f$ over $[a, b]$.

> [!theorem]
> Let $R$ denote the radial set of a nonnegative function $f$ over an interval $[a, b]$, where $0 \leq b - a \leq 2\pi$, and assume that $R$ is measurable. If $f^2$ is integrable on $[a, b]$ the area of $R$ is given by the integral $$a(R) = \frac{1}{2} \int_a^b f^2(\theta) d\theta$$

> [!remark]
> The area is calculated by $\sum \frac{1}{2} (\theta_k - \theta_{k - 1}) s_k^2$

| Shape                           | Function                                                             | Area                                                                                      |
| ------------------------------- | -------------------------------------------------------------------- | ----------------------------------------------------------------------------------------- |
| Spiral of Archimedes            | $f(\theta) = \theta, \quad 0 \leq \theta \leq 2\pi$                  | $\frac{1}{2} \int_0^{2\pi} \int_0^{2\pi} \theta^2 d\theta = \frac{4\pi^3}{3}$             |
| Circle tangent to $y$-axis      | $f(\theta) = 2 \cos \theta, \quad -\pi/2 \leq \theta \leq \pi / 2$   | $\frac{1}{2} \int_{-\pi / 2}^{\pi / 2} 4 \cos^2 \theta d\theta = \pi$                     |
| Two circles tangent to $y$-axis | $f(\theta) = 2 \|\cos \theta\|, \quad 0 \leq \theta \leq 2 \pi$      | $\frac{1}{2} \int_0^{2\pi} 4\cos^2 \theta d\theta = 2\pi$                                 |
| Circle tangent to $x$-axis      | $f(\theta) = 4 \sin \theta, \quad 0 \leq \theta \leq \pi$            | $\frac{1}{2} \int_0^{\pi} 16 \sin^2 \theta d\theta = 4\pi$                                |
| Two circles tangent to $x$-axis | $f(\theta) = 4 \|\sin \theta\|, \quad 0 \leq \theta \leq 2\pi$       | $\frac{1}{2} \int_0^{2\pi} 16 \sin^2 \theta d\theta = 8\pi$                               |
| Rose petal                      | $f(\theta) = \sin 2\theta, \quad 0 \leq \theta \leq \pi/2$           | $\frac{1}{2} \int_0^{\pi/2} \sin^2 2\theta d\theta = \pi / 8$                             |
| Four-leaved rose                | $f(\theta) = \|\sin 2\theta\|, \quad 0 \leq \theta \leq 2\pi$        | $\frac{1}{2} \int_0^{2\pi} \sin^2 2\theta d\theta = \pi / 2$                              |
| Lazy eight                      | $f(\theta) = \sqrt{\|\cos \theta\|}, \quad 0 \leq \theta \leq 2\pi$  | $\frac{1}{2} \int_0^{2\pi} \|\cos \theta\| d\theta = 2$                                   |
| Four-leaf clover                | $f(\theta) = \sqrt{\|\cos 2\theta\|}, \quad 0 \leq \theta \leq 2\pi$ | $\frac{1}{2} \int_0^{2\pi} \|\cos 2\theta\| d\theta = 2$                                  |
| Cardioid                        | $f(\theta) = 1 + \cos \theta, \quad 0 \leq \theta \leq 2\pi$         | $\frac{1}{2} \int_0^{2\pi} (1 + 2 \cos \theta + \cos^2 \theta) d\theta = \frac{3 \pi}{2}$ |
| Limacon                         | $f(\theta) = 2 + \cos \theta, \quad 0 \leq \theta \leq 2\pi$         | $\frac{1}{2} \int_0^{2\pi} (4 + 4 \cos \theta + \cos^2 \theta) d\theta = \frac{9 \pi}{2}$ |

### Integration to the calculation of volume

> [!theorem]
> Let $R$ be a Cavalieri solid in $\mathcal A$ with a cross-sectional area function $a_R$ which is integrable on an interval $[a, b]$ and zero outside $[a, b]$. Then the volume of $R$ is equal to the integral of the cross-sectional area: $$v(R) = \int_a^b a_R(u) du.$$

> [!example] Volume of a solid of revolution
> Let $f$ be a function which is nonnegative and integrable on an interval $[a, b]$. If the ordinate set of this function is revolved about the $x$-axis, it sweeps out a solid of revolution. Each cross section cut by a plane perpendicular to the $x$-axis is a circular disk. The area of the circular disk cut at the point $x$ is $\pi f^2(x)$, where $f^2(x)$ means the square of $f(x)$. Thus, we can calculate the volume of the solid by $$\int_a^b \pi f^2(x) dx.$$

## Average Value

> [!definition] Average Value of a Function on an Interval
> If $f$ is integrable on an interval $[a, b]$, we define $A(f)$, the **average value** of $f$ on $[a, b]$, by the formula $$A(f) = \frac{1}{b - a} \int_a^b f(x) dx.$$

> [!proposition] Weighted Arithmetic Mean
> For $w$ is a nonnegative weight function with $\int_a^b w(x) dx \neq 0$, the weighted arithmetic mean of the function $f$ is defined by $$A(f) = \frac{\int_a^b w(x) f(x) dx}{\int_a^b w(x) dx}$$

> [!proposition]
> The average value $f$ has additive property, homogenous property, monotone property.

## Integral as a Function of the Upper Limit. Indefinite Integrals

> [!definition] Indefinite Integral
> For $f$ is a function such that the integral $f_a^x f(t) dt$ exists for each $x$ in an interval $[a, b]$. The function $A$ denotes by the formula $$A(x) = \int_a^x f(t) dt \quad \text{if} \quad a \leq x \leq b$$ referred to as an **indefinite integral** of $f$ and it is said to be obtained from $f$ by integration.

## Integrability Theorem for Continuous Functions

> [!definition] Integrability of Continuous Functions
> If a function $f$ is continuous at each point of a closed interval $[a, b]$, then $f$ is integrable on $[a, b]$.

> [!definition] Mean-Value Theorem for Integrals
> If $f$ is continuous on $[a, b]$, then for some $c$ in $[a, b]$ we have $$\int_a^b f(x) dx = f(c) (b - a).$$

> [!theorem] Weighted Mean-Value Theorem for Integrals
> Assume $f$ and $g$ are continuous on $[a, b]$. If $g$ never changes sign in $[a, b]$ then, for some $c$ in $[a, b]$, we have $$\int_a^b f(x) g(x) dx = f(c) \int_a^b g(x) dx.$$

> [!example]
> Assume $f$ is continuous on $[a, b]$. If $\int_a^b f(x) dx = 0$ then $f(c) = 0$ for at least one $c$ in $[a, b]$.

> [!example]
> Assume that $f$ is integrable and nonnegative on $[a, b]$. If $\int_a^b f(x) dx = 0$, then $f(x) = 0$ at each point of continuity of $f$.

> [!example]
> Assume $f$ is continuous on $[a, b]$, also $\int_a^b f(x) g(x) dx = 0$ for every function $g$ that is continuous on $[a, b]$. Then $f(x) = 0$ for all $x$ in $[a, b]$.

## Method of Integration
### First Fundamental Theorem of Calculus

> [!theorem] First Fundamental Theorem of Calculus
> Let $f$ be a function that is integrable on $[a, x]$ for each $x$ in $[a, b]$. Let $c$ be such that $a \leq c \leq b$ and define a new function $A$ as follows: $$A(x) = \int_c^x f(t) dt \quad \text{if} \quad a \leq x \leq b.$$ Then the derivative $A'(x)$ exists at each point $x$ in the open interval $(a, b)$ where $f$ is continuous, and for such $x$ we have $$A'(x) = f(x).$$

### Second Fundamental Theorem of Calculus

> [!definition] Primitive Function
> A function $P$ is called a **primitive** (or an **antiderivative**) of a function $f$ on an open interval $I$ if the derivative of $P$ is $f$, that is, if $P'(x) = f(x)$ for all $x$ in $I$.

> [!theorem] Second Fundamental Theorem of Calculus
> Assume $f$ is continuous on an open interval $I$, and let $P$ be any primitive of $f$ on $I$. Then, for each $c$ and each $x$ in $I$, we have $$P(x) = P(c) + \int_c^x f(t) dt.$$ 

### Leibniz Notation for Primitives

> [!theorem]
> $\int f(x) dx = P(x) + C$

### Integration by substitution

> [!theorem]
> $\int f[g(x)] g'(x) dx = P[g(x)] + C$

> [!theorem] Substitution Theorem for Integrals
> Assume $g$ has a continuous derivative $g'$ on an open interval $I$. Let $J$ be the set of values taken by $g$ on $I$ and assume that $f$ is continuous on $J$. Then for each $x$ and $c$ in $I$, we have $$\int_c^x f[g(t)] g'(t) dt = \int_{g(c)}^{g(x)} f(u) du.$$

### Integration by parts

> [!theorem] Integration by Parts
> For definite integrals $$\int_a^b f(x) g'(x) dx = f(b) g(b) - f(a) g(a) - \int_a^b f'(x) g(x) dx$$
> Abbreviated $$\int u dv = uv - \int v du + C.$$
 
> [!theorem] Second Mean-Value Theorem for Integrals
> Assume $g$ is continuous on $[a, b]$, and assume $f$ has a derivative which is continuous and never changes sign in $[a, b]$. Then, for some $c$ in $[a, b]$, we have $$\int_a^b f(x) g(x) dx = f(a) \int_a^c g(x) dx + f(b) \int_c^b g(x) dx.$$
> 

### Integration by partial functions

> [!example]
> $\int R(\sin x, \cos x) dx \rightarrow u = \tan \frac{1}{2}x$
> - $x = 2 \arctan u$
> - $dx = \frac{2}{1 + u^2} du$
> - $\sin x = \frac{2u}{1 + u^2}$
> - $\cos x = \frac{1 - u^2}{1 + u^2}$

> [!example]
> $x = a \sin t, dx = a \cos t dt$
> $\rightarrow \int R(x, \sqrt{a^2 - x^2}) dx = \int R(a \sin t, a \cos t) a \cos t dt$

## Improper Integral

> [!definition] Improper Integral
> We want to extend the notation $\int_a^b f(x) dx$.
> 1. **Improper integral of the first kind**: Extend a bound to infinity $$\int_a^\infty f(x) dx.$$
> 2. **Improper integral of the second kind**: Keep the finite range $[a, b]$, and allow $f$ to become unbounded at one or more points.

> [!theorem]
> Assume that the proper integral $\int_a^b f(x) dx$ exists for each $b \geq a$ and suppose that $f(x) \geq 0$ for all $x \geq a$. Then $\int_a^{\infty} f(x)$ converges if and only if there is a constant $M > 0$ such that $$\int_a^b f(x) dx \leq M \quad \forall b \geq a.$$

> [!theorem]
> Assume the proper integral $\int_a^b f(x) dx$ exists for each $b \geq a$ and suppose that $0 \leq f(x) \leq g(x)$ for all $x \geq a$, where $\int_a^{\infty} g(x) dx$ converges. Then $\int_a^{\infty} f(x) dx$ also converges and $$\int_a^{\infty} f(x) dx \leq \int_a^{\infty} g(x) dx.$$
> The integral $\int_a^{\infty} g(x) dx$ is said to dominate the integral $\int_a^{\infty} f(x) dx$.

> [!theorem] Limit Comparison Test
> Assume both proper integrals $\int_a^b f(x) dx$ and $\int_a^b g(x) dx$ exist for each $b \geq a$, where $f(x) \geq 0$ and $g(x) > 0$ for all $x \geq a$. If $$\lim_{x \rightarrow +\infty} \frac{f(x)}{g(x)} = c, \quad \text{where } c \neq 0,$$ then both integrals $\int_a^\infty f(x) dx$ and $\int_a^\infty g(x) dx$ converge or both diverge.
> If $c = 0$ then convergence of $\int_a^\infty g(x) dx$ implies convergence of $\int_a^\infty f(x) dx$. 

## Common Integration

| Condition  | Integration                      | Result                                                                 |
| ---------- | -------------------------------- | ---------------------------------------------------------------------- |
| $x > 0$    | $\int \frac{1}{x} dx$            | $\ln \|x\| + C$                                                        |
| $f(x) > 0$ | $\int \frac{f'(x)}{f(x)} dx$     | $\ln \|f(x)\| + C$                                                     |
|            | $\int \tan x dx$                 | $-\ln \|\cos x\| + C$                                                  |
|            | $\int \ln x dx$                  | $x \ln x - x + C$                                                      |
|            | $\int \sin (\ln x) dx$           | $\frac{1}{2} x \sin (\ln x) - \frac{1}{2} x \cos (\ln x) + C$          |
|            | $\int \cos(\ln x)dx$             | $\frac{1}{2} x \sin (\ln x) + \frac{1}{2} x \cos (\ln x) + C$          |
|            | $\int e^x \sin x dx$             | $\frac{e^x}{2} (\sin x - \cos x) + C$                                  |
|            | $\int e^x \cos x dx$             | $\frac{e^x}{2} (\cos x + \sin x) + C$                                  |
|            | $\int \frac{dx}{1 + e^x}$        | $x - \ln(1 + e^x) + C$                                                 |
|            | $\int \frac{dx}{\sqrt{1 - x^2}}$ | $\arcsin x dx$                                                         |
|            | $\int \arcsin x dx$              | $x \arcsin x + \sqrt{1 - x^2} + C$                                     |
|            | $\int \arccos x dx$              | $x \arccos x - \sqrt{1 - x^2} + C$                                     |
|            | $\int \arctan x dx$              | $x \arctan x - \frac{1}{2} \ln(1 + x^2) + C$                           |
|            | $\int \text{arccot } x dx$       | $x \text{ arccot } x + \frac{1}{2} \ln (1 + x^2) + C$                  |
|            | $\int \text{arcsec } x dx$       | $x \text{ arcsec } x - \frac{x}{\|x\|} \ln \|x + \sqrt{x^2 - 1}\| + C$ |
|            | $\int \text{arccsc } x dx$       | $x \text{ arcsec } x + \frac{x}{\|x\|} \ln \|x + \sqrt{x^2 - 1}\| + C$ |
|            | $\int \frac{1}{1 + x^2} dx$      | $\arctan x + C$                                                        |
|            |                                  |                                                                        |
|            |                                  |                                                                        |
|            |                                  |                                                                        |

