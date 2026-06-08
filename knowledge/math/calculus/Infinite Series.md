## Sequences

> [!definition] Infinite Sequence
> A function $f$ whose domain is the set of all positive integers $1, 2, 3, \dots$ is called an infinite sequence. The function value $f(n)$ is called the $n$-th term of the sequence.

> [!definition] Limit of a Sequence
> A sequence ${f(n)}$ is said to have a limit $L$ if, for every positive number $\epsilon$, there is another positive number $N$ (which may depend on $\epsilon$) such that $$|f(n) - L| < \epsilon \; \forall n \geq N.$$
> In this case, we say the sequence $\{f(n)\}$ converges to $L$ and we write $$\lim_{n \rightarrow \infty} f(n) = L, \quad \text{or} \quad f(n) \rightarrow L \quad \text{as } n \rightarrow \infty.$$ A sequence which does not converge is called divergent.

## Monotonic sequences of real numbers

> [!definition] Monotonic Sequence
> A sequence $\{f(n)\}$ is said to be **increasing** if $$f(n) \leq f(n + 1) \quad \forall n \geq 1.$$ We indicate this briefly by writing $f(n) \nearrow$. If, on the other hand, we have $$f(n) \geq f(n + 1), \quad \forall n \geq 1,$$ we call the sequence **decreasing** and write $f(n) \searrow$. A sequence is called **monotonic** if it is increasing or if it is decreasing.

> [!definition] Bounded Sequence
> A sequence $\{f(n)\}$ is called **bounded** if there exist a positive number $M$ such that $|f(n)| \leq M \; \forall n$. A sequence that is not bounded is called **unbounded**.

> [!theorem]
> A monotonic sequence converges if and only if it is bounded.

> [!proposition]
> If $\lim_{n \rightarrow \infty} a_n = A$ and $\lim_{n \rightarrow \infty} b_n = B$, then:
> 1. $\lim_{n \rightarrow \infty} (a_n + b_n) = A + B$.
> 2. $\lim_{n \rightarrow \infty} (ca_n) = c A$, where $c$ is constant.
> 3. $\lim_{n \rightarrow \infty} (a_n b_n) = AB$.

## Infinite Sequence

> [!definition] Infinite Series
> For a sequence of real or complex numbers $$a_1, a_2, \dots, a_n, \dots,$$ we can define the partial sum $s_n$ of the first $n$ terms being defined as follows: $$s_n = \sum_{k = 1}^n a_k.$$ The sequence $\{s_n\}$ of partial sum is called an **infinite series**, or simply a series and denoted by the symbols: $$\sum_{k = 1}^\infty a_k.$$

> [!definition] Convergent, Divergent
> If there is a real or complex number $S$ such that $$\lim_{n \rightarrow \infty} s_n = S,$$ we say that the series $\sum_{k = 1}^{\infty} a_k$ is **convergent** and has the sum $S$, in which case we write $$\sum_{k = 1}^{\infty} a_k = S.$$ If $\{s_n\}$ diverges, we say that the series $\sum_{k = 1}^{\infty} a_k$ **diverges** and has no sum.

> [!theorem]
> Let $\sum a_n$ and $\sum b_n$ be convergent infinite series of complex term and let $\alpha$ and $\beta$ be complex constants. Then the series $\sum (\alpha a_n + \beta b_n)$ also converges, and its sum is given by the equation $$\sum_{n = 1}^{\infty} (\alpha a_n + \beta b_n) = \alpha \sum_{n = 1}^{\infty} a_n + \beta \sum_{n = 1}^{\infty} b_n.$$

> [!theorem]
> If $\sum a_n$ converges and if $\sum b_n$ diverges, then $\sum (a_n + b_n)$ diverges.

## Test for convergence

> [!theorem]
> If the series $\sum a_n$ converges, then its $n$-th term tends to $0$; that is, $$\lim_{n \rightarrow \infty} a_n = 0.$$

### Comparison tests for series of nonnegative terms

> [!theorem]
> Assume that $a_n \geq 0$ for each $n \geq 1$. Then the series $\sum a_n$ converges if and only if the sequence of its partial sums is bounded above.

> [!theorem] Comparison Test
> Assume $a_n \geq 0$ and $b_n \geq 0$ for all $n \geq 1$. If there exists a positive constant $c$ such that $$a_n \leq c b_n$$ for all $n$, then convergence of $\sum b_n$ implies convergence of $\sum a_n$. Also, the divergence of $\sum a_n$ implies divergence of $\sum b_n$ and thus we say the $\sum b_n$ dominates the series $\sum a_n$.

> [!theorem] Limit Comparison Test
> Assume that $a_n > 0$ and $b_n > 0$ for all $n \geq 1$, and suppose that $$\lim_{n \rightarrow \infty} \frac{a_n}{b_n} = 1.$$ Then $\sum a_n$ converges if and only if $\sum b_n$ converges.

> [!theorem]
> Two series $\sum a_n$ and $\sum b_n$ with terms that are positive and asymptotically equal converge together or they diverge together.

### The integral test

> [!theorem] Integral Test
> Let $f$ be a positive decreasing function, defined for all real $x \geq 1$. For each $n \geq 1$, let $$s_n = \sum_{k = 1}^n f(k) \quad \text{and} \quad t_n = \int_1^n f(x) dx.$$ Then both sequences $\{s_n\}$ and $\{t_n\}$ converges or both diverge.

> [!proposition]
> Assume $f$ is a nonnegative increasing function defined for all $x \geq 1$. Then, $$\sum_{k = 1}^{n - 1} f(k) \leq \int_1^n f(x) dx \leq \sum_{k = 2}^n f(k).$$

### The root test and the ratio test for series of nonnegative terms

> [!theorem] Root Test
> Let $\sum a_n$ be a series of nonnegative terms such that $$\lim_{n \rightarrow \infty} a_n^{1/n} = R.$$
> 1. If $R < 1$, the series converges.
> 2. If $R > 1$, the series diverges.
> 3. If $R = 1$, the test is inconclusive.

> [!theorem] Ratio Test
> Let $\sum a_n$ be a series of positive terms such that $$\lim_{n \rightarrow \infty} \frac{a_{n + 1}}{a_n} = L.$$
> 1. If $L < 1$, the series converges.
> 2. If $L > 1$, the series diverges.
> 3. If $L = 1$, the test is inconclusive.

> [!proposition]
> Let $\{a_n\}$ and $\{b_n\}$ be two sequences with $a_n > 0$ and $b_n > 0$ for all $n \geq N$, and let $c_n = b_n - b_{n + 1} a_{n + 1} / a_n$.
> 1. If there is a positive constant $r$ such that $c_n \geq r > 0$ for all $n \geq N$, then $\sum a_n$ converges.
> 2. If $c_n \leq 0$ for $n \geq N$ and if $\sum 1/b_n$ diverges, then $\sum a_n$ diverges.

> [!theorem] Raabe's Test
> Let $\sum a_n$ be a series of positive terms. If there is an $r > 0$ and an $N \geq 1$ such that $$\frac{a_{n + 1}}{a_n} \leq 1 - \frac{1}{n} - \frac{r}{n} \quad \forall n \geq N,$$ then $\sum a_n$ converges. The series $\sum a_n$ diverges if $$\frac{a_{n + 1}}{a_n} \geq 1 - \frac{1}{n} \quad \forall n \geq N.$$ ($b_{n + 1} = n$)

> [!theorem] Gauss' Test
> Let $\sum a_n$ be a series of positive terms. If there is an $N \geq 1$, an $s > 1$, and an $M > 0$ such that $$\frac{a_{n + 1}}{a_n} = 1 - \frac{A}{n} + \frac{f(n)}{n^s} \quad \forall n \geq N,$$ where $|f(n)| \leq M$ for all $n$, then $\sum a_n$ converges if $A > 1$ and diverges if $A \leq 1$.
> ($A = 1 \rightarrow b_{n + 1} = n \log n$, $A \neq 1 \rightarrow$ Raabe's Test).

### Alternating Series

> [!definition] Alternating Series
> Series are called **alternating series** if they have the form $$\sum_{n = 1}^{\infty} (-1)^{n - 1} a_n$$ where each $a_n > 0$.

> [!theorem] Leibniz's Rule
> If $\{a_n\}$ is a monotonic decreasing sequence with limit $0$, then the alternating series $\sum_{n = 1}^{\infty} (-1)^{n - 1} a_n$ converges. If $S$ denotes its sum and $s_n$ its $n$-th partial sum, we also have the inequalities $$0 < (-1)^n (S - s_n) < a_{n + 1} \quad \forall n \geq 1.$$

### Conditional and absolute convergence

> [!theorem]
> Assume $\sum |a_n|$ converges. Then $\sum a_n$ also converges, and we have $$|\sum_{n = 1}^{\infty} a_n| \leq \sum_{n = 1}^{\infty} |a_n|.$$

> [!definition] Absolute Convergent, Conditional Convergent
> A series $\sum a_n$ is called absolutely convergent if $\sum |a_n|$ converges. It is called conditionally convergent if $\sum a_n$ converges but $\sum |a_n|$ diverges.

### The convergence tests of Dirichlet and Abel

> [!theorem] Abel's Partial Summation Formula
> Let $\{a_n\}$ and $\{b_n\}$ be two sequences of complex numbers, and let $$A_n = \sum_{k = 1}^n a_k.$$ Then we have the identity $$\sum_{k = 1}^n a_k b_k = A_n b_{n + 1} + \sum_{k = 1}^n A_k (b_k - b_{k + 1}).$$

> [!theorem] Dirichlet's Test
> Let $\sum a_n$ be a series of complex terms whose partial sums form a bounded sequence. Let $\{b_n\}$ be a decreasing sequence which converges to $0$. Then the series $\sum a_n b_n$ converges.

> [!theorem] Abel's Test
> Let $\sum a_n$ be a convergent series of complex terms and let $\{b_n\}$ be a monotonic convergent sequence of real terms. Then the series $\sum a_n b_n$ converges.

> [!theorem]
> For every real $\theta$ not an integer multiple of $\pi$, we have the identity $$\sum_{k = 1}^n e^{2ik\theta} = \frac{\sin n \theta}{\sin \theta} e^{i(n + 1) \theta},$$ from which we obtain the estimate $$|\sum_{k = 1}^n e^{2ik\theta}| \leq \frac{1}{|\sin \theta|}.$$

> [!proposition]
> If $\sum |a_n|$ converges, then $\sum a_n^2$ converges.

> [!theorem] Tail Comparison
> 1. If $\sum a_n$ converges absolutely, then so does $\sum a_n^2 / (1 + a_n^2)$.
> 2. If $\sum a_n$ converges absolutely, and if no $a_n = -1$, then $\sum a_n/(1 + a_n)$ converges absolutely.

### Rearrangements of series

> [!definition] Rearrangement of Series
> If $\sum a_n$ and $\sum b_n$ are two series such that for every $n \geq 1$ we have $$b_n = a_{f(n)}$$ for some permutation $f$, then the series $\sum b_n$ is said to be a rearrangement of $\sum a_n$.

> [!theorem]
> Let $\sum a_n$ be an absolutely convergent series having sum $S$. Then every rearrangement of $\sum a_n$ also converges absolutely and has sum $S$.

> [!theorem]
> Given a series $\sum a_n$ of real terms, define $$a_n^+ = \frac{a_n + |a_n|}{2}, \quad a_n^- = \frac{a_n - |a_n|}{2}.$$
> 1. If $\sum a_n$ is conditionally convergent, both $\sum a_n^+$ and $\sum a_n^-$ diverge.
> 2. If $\sum a_n$ is absolutely convergent, both $\sum a_n^+$ and $\sum a_n^-$ converge, and we have $$\sum_{n = 1}^{\infty} a_n = \sum_{n = 1}^{\infty} a_n^+ + \sum_{n = 1}^{\infty} a_n^-.$$

> [!theorem]
> Let $\sum a_n$ be a conditionally convergent series of real terms, and let $S$ be a given real number. Then there is a rearrangement $\sum b_n$ of $\sum a_n$ which converges to the sum $S$.

## Convergence of Functions

### Pointwise Convergence of sequences of functions

> [!definition] Limit Function, Converges Pointwise
> Consider sequences of function $\{f_n\}$ whose terms are real- or complex-valued functions having a common domain. For each $x$ in the domain, we can form another number sequence $\{f_n(x)\}$. Let $S$ denote the set of points $x$ for which this sequence converges. The function $f$ defined on $S$ by the equation $$f(x) = \lim_{n \rightarrow \infty} f_n(x) \quad \text{if} \quad x \in S,$$ is called the **limit function** of the sequence $\{f_n\}$, and we say that the sequence $\{f_n\}$ **converges pointwise** to $f$ on the set $S$.

### Uniform convergence of sequences of functions

> [!definition] Converge Uniformly
> A sequence of functions $\{f_n\}$ is said to **converge uniformly** to $f$ on a set $S$ if for every $\epsilon > 0$ there is an $N$ (depending only on $\epsilon$) such that $n \geq N$ implies $$|f_n(x) - f(x)| < \epsilon \quad \forall x \in S.$$ We denote this symbolically by writing $$f_n \rightarrow f \quad \text{uniformly on } S.$$

### Uniform convergence and continuity

> [!theorem]
> Assume $f_n \rightarrow f$ uniformly on an interval $S$. If each function $f_n$ is continuous at a point $p$ in $S$, then the limit function $f$ is also continuous at $p$. 

> [!theorem]
> If a series of functions $\sum u_k$ converges uniformly to a sum function $f$ on a set $S$, and if each term $u_k$ is continuous at a point $p$ in $S$, then the sum $f$ is also continuous at $p$.
> Note: $$\lim_{x \rightarrow p} \sum_{k = 1}^\infty u_k(x) = \sum_{k = 1}^\infty \lim_{x \rightarrow p} u_k(x).$$

### Uniform convergence and integration

> [!theorem]
> Assume $f_n \rightarrow f$ uniformly on an interval $[a, b]$, and assume that each function $f_n$ is continuous on $[a, b]$. Define a new sequence $\{g_n\}$ by the equation $$g_n(x) = \int_a^x f_n(t) dt \quad \text{if} \quad x \in [a, b],$$ and let $$g(x) = \int_a^x f(t) dt.$$ Then $g_n \rightarrow g$ uniformly on $[a, b]$. In symbols, we have $$\lim_{n \rightarrow \infty} \int_a^x f_n(t) dt = \int_a^x \lim_{n \rightarrow \infty} f_n(t) dt.$$

> [!theorem]
> Assume that a series of functions $\sum u_k$ converges uniformly to a sum function $f$ on an interval $[a, b]$, where each $u_k$ is continuous on $[a, b]$. If $x \in [a, b]$, define $$g_n(x) = \sum_{k = 1}^n \int_a^x u_k(t) dt \quad \text{and} \quad g(x) = \int_a^x f(t) dt.$$ Then $g_n \rightarrow g$ uniformly on $[a, b]$. In other words, we have $$\lim_{n \rightarrow \infty} \sum_{k = 1}^n \int_a^x u_k(t) dt = \int_a^x \lim_{n \rightarrow \infty} \sum_{k = 1}^n u_k(t) dt$$ or $$\sum_{k = 1}^\infty \int_a^x u_k(t) dt = \int_a^x \sum_{k = 1}^\infty u_k(t) dt.$$

### A sufficient condition for uniform convergence

> [!theorem] The Weierstrass M-test
> Given a series of functions $\sum u_n$ which converges pointwise to a function $f$ on a set $S$. If there is a convergent series of a positive constants $\sum M_n$ such that $$0 \leq |u_n(x)| \leq M_n \quad \forall n \geq 1, x \in S.$$ then the series $\sum u_n$ converges uniformly on $S$.

## Power series

### Power series, Circle of convergence

> [!theorem]
> Assume the power series $\sum a_n z^n$ converges for a particular $z \neq 0$, say for $z = z_1$. Then we have:
> 1. The series converges absolutely for every $z$ with $|z| < |z_1|$.
> 2. The series converges uniformly on every circular disk with center at $0$ and radius $R < |z_1|$.

> [!theorem] Existence of a Circle of Convergence
> Assume that the power series $\sum a_n z^n$ converges for at least one $z \neq 0$, say for $z = z_1$, and that it diverges for at least one $z$, say for $z = z_2$. Then there exists a positive real number $r$ such that the series converges absolutely if $|z| < r$ and diverges if $|z| > r$.

### Properties of functions represented by real power series

> [!theorem]
> Assume a function $f$ is represented by the power series $$f(x) = \sum_{n = 0}^\infty a_n (x - a)^n$$ in an open interval $(a - r, a + r)$. Then $f$ is continuous on this interval, and its integral over any closed subinterval may be computed by integrating the series term by term. In particular, for every $x$ in $(a - r, a + r)$, we have $$\int_a^x f(t) dt = \sum_{n = 0}^\infty a_n \int_a^x (t - a)^n dt = \sum_{n = 0}^\infty \frac{a_n}{n + 1} (x - a)^{n + 1}$$

> [!theorem]
> Let $f$ be represented by the power series $f(x) = \sum_{n = 0}^\infty a_n(x - a)^n$ in the interval of convergence $(a - r, a + r)$. Then we have:
> 1. The differentiated series $\sum_{n = 1}^\infty na_n(x - a)^{n - 1}$ also has radius of convergence $r$.
> 2. The derivative $f'(x)$ exists for each $x$ in the interval of convergence and is given by $$f'(x) = \sum_{n = 1}^\infty n a_n (x - a)^{n - 1}.$$

> [!theorem]
> If two power series $\sum a_n (x - a)^n$ and $\sum b_n (x - a)^n$ have the same sum function $f$ in some neighborhood of the point $a$, then the two series are equal term by term; in fact, we have $a_n = b_n = f^{(n)}(a) / n!$ for each $n \geq 0$.

### The Taylor's series generated by a function

> [!definition] Taylor's series generated by $f$ at $a$
> $$f(x) = \sum_{k = 0}^n \frac{f^{(k)}(a)}{k!} (x - a)^k + E_n(x)$$

> [!theorem] 
> Assume $f$ is infinitely differentiable in open interval $I = (a - r, a + r)$, and assume that there is a positive constant $A$ such that $$|f^{(n)}(x)| \leq A^n \quad \text{for} \quad n = 1, 2, 3, \dots,$$ and every $x$ in $I$. Then the Taylor's series generated by $f$ at a converges to $f(x)$ for each $x$ in $I$.

> [!theorem] Bernstein's Theorem
> Assume $f$ and all its derivatives are nonnegative on a closed interval $[0, r]$. That is, assume that $$f(x) \geq 0 \quad \text{and} \quad f^{(n)}(x) \geq 0$$ for each $x$ in $[0, r]$ and each $n = 1, 2, 3, \dots.$ Then, if $0 \leq x < r$, the Taylor's series $$\sum_{k = 0}^{\infty} \frac{f^{(k)(0)}}{k!} x^k$$ converges to $f(x)$.

## Special Series

### Telescoping Series

> [!theorem]
> Let $\{a_n\}$ and $\{b_n\}$ be two sequences of complex numbers such that $$a_n = b_n - b_{n + 1} \quad \text{for} \quad n = 1, 2, 3, \dots.$$ Then the series $\sum a_n$ converges if and only if the sequence $\{b_n\}$ converges, in which case we have $$\sum_{n = 1}^{\infty} a_n = b_1 - L, \quad \text{where} \quad L = \lim_{n \rightarrow \infty} b_n.$$

### The geometric series

> [!theorem]
> If $x$ is complex, with $|x| < 1$, the geometric series $\sum_{n = 0}^{\infty} x^n$ converges and has sum $1/(1 - x)$.

### Other Series

| Series                                     | Formula                          |
| ------------------------------------------ | -------------------------------- |
| $\sum_{n = 1}^\infty n^k x^n$              | $\frac{P_k(x)}{(1 - x)^{k + 1}}$ |
| $\sum_{n = 0}^\infty \binom{n + k}{k} x^n$ | $\frac{1}{(1 - x)^{k + 1}}$      |
|                                            |                                  |
