## Limit

> [!definition] Neighborhood of a Point
> Any open interval containing a point $p$ as its midpoint is called a neighborhood of $p$.

> [!definition] Limit of a Function
> The symbolism $$\lim_{x \rightarrow p} f(x) = A \quad [\text{or} \quad f(x) \rightarrow A \quad \text{as} \quad \text x \rightarrow p]$$ means that for every neighborhood $N_1(A)$ there is some neighborhood $N_2(p)$ such that $$f(x) \in N_1(A) \quad \text{whenever} \quad x \in N_2(p) \quad \text{and} \quad x \neq p.$$
> $\epsilon, \delta$ formulation:
> The symbol $\lim_{x \rightarrow p} f(x) = A$ means that for every $\epsilon > 0$, there is a $\delta > 0$ such that $$|f(x) - A| < \epsilon \quad \text{whenever} \quad 0 < |x - p| < \delta.$$

> [!definition]
> The symbolism $$\lim_{x \rightarrow +\infty} f(x) = A$$ means that for every number $\epsilon > 0$, there is another number $M > 0$ (which may depend on $\epsilon$) such that $$|f(x) - A| < \epsilon \quad \text{whenever} \quad x > M.$$

> [!definition] Infinite Limits
> For every positive number $M$ (no matter how large), there corresponds another positive number $\delta$ (which may depend on $M$) such that $$f(x) > M \quad \text{whenever} \quad 0 < |x - a| < \delta.$$ If $f(x) > M$ whenever $0 < x - a < \delta$, we write $$\lim_{x \rightarrow a^+} f(x) = +\infty,$$ and we say that $f(x)$ tends to plus infinity as $x$ approaches $a$ from the right. If $f(x) > M$ whenever $0 < a - x < \delta$, we write $$\lim_{x \rightarrow a^-} f(x) = +\infty$$ and we say that $f(x)$ tends to plus infinity as $x$ approaches $a$ from the left.
> The symbols $$\lim_{x \rightarrow a} = -\infty, \quad \lim_{x \rightarrow a^+} = -\infty, \quad \lim_{x \rightarrow a^-} = -\infty$$ are similarly defined, the only difference being that we replace $f(x) > M$ by $f(x) < -M$.

## L'Hopital's rule

> [!theorem] L'Hopital Rule for 0/0
> Assume $f$ and $g$ have derivatives $f'(x)$ and $g'(x)$ at each point $x$ of an open interval $(a, b)$, and suppose that $$\lim_{x \rightarrow a^+} f(x) = 0 \quad \text{and} \quad \lim_{x \rightarrow a^+} g(x) = 0.$$ Assume also that $g'(x) \neq 0$ for each $x$ in $(a, b)$. If the limit $$\lim_{x \rightarrow a^+} \frac{f'(x)}{g'(x)}$$ exists and has the value $L$, say, then the limit $$\lim_{x \rightarrow a^+} \frac{f(x)}{g(x)}$$ also exists and has the value $L$.

> [!theorem]
> Assume that $f$ and $g$ have derivatives $f'(x)$ and $g'(x)$ for all $x$ greater than a certain fixed $M > 0$. Suppose that $$\lim_{x \rightarrow +\infty} f(x) = 0 \quad \text{and} \quad \lim_{x \rightarrow +\infty} g(x) = 0$$ and that $g'(x) \neq 0$ for $x > M$. If $f'(x) / g'(x)$ tends to a limit as $x \rightarrow +\infty$, then $f(x) / g(x)$ also tends to a limit and the two limits are equal. In other words, $$\lim_{x \rightarrow +\infty} \frac{f'(x)}{g'(x)} = L \quad \text{implies} \quad \lim_{x \rightarrow +\infty} \frac{f(x)}{g(x)} = L.$$

## Continuous Function

> [!definition] Continuity of a Function at a point
> A function $f$ is said to be continuous at a point $p$ if 
> 1. $f$ is defined at $p$, and
> 2. $\lim_{x \rightarrow p} f(x) = f(p)$.
> 
> This definition can also be formulated in terms of neighborhoods. A function $f$ is continuous at $p$ if for every neighborhood $N_1[f(p)]$ there is a neighborhood $N_2(p)$ such that $$f(x) \in N_1[f(p)] \quad \text{whenever} \quad x \in N_2(p).$$
> $\epsilon, \delta$ formulation:
> A function $f$ is continuous at $p$ if for every $\epsilon > 0$ there is a $\delta > 0$ such that $$|f(x) - f(p)| < \epsilon \quad \text{whenever} \quad |x - p| < \delta.$$

> [!theorem] Basic Limit Theorems
> Let $f$ and $g$ be functions such that $$\lim_{x \rightarrow p} f(x) = A, \quad \lim_{x \rightarrow p} g(x) = B.$$
> Then we have
> 1. $\lim_{x \rightarrow p} [f(x) + g(x)] = A + B$,
> 2. $\lim_{x \rightarrow p} [f(x) - g(x)] = A - B$,
> 3. $\lim_{x \rightarrow p} f(x) \cdot g(x) = A \cdot B$,
> 4. $\lim_{x \rightarrow p} f(x) / g(x) = A / B \quad \text{if} \quad B \neq 0$.

> [!theorem]
> Let $f$ and $g$ be continuous at a point $p$. Then the sum $f + g$, the difference $f - g$, and the product $f \cdot g$ are also continuous at $p$. The same is true of the quotient $f/g$ if $g(p) \neq 0$.

> [!principle] Squeezing Principle
> Suppose that $f(x) \leq g(x) \leq h(x)$ for all $x \neq p$ in some neighborhood $N(p)$. Suppose also that $$\lim_{x \rightarrow p} f(x) = \lim_{x \rightarrow p} h(x) = a.$$ Then we also have $\lim_{x \rightarrow p} g(x) = a$.

> [!theorem] Continuity of Indefinite Integrals
> Assume $f$ is integrable on $[a, x]$ for every $x$ in $[a, b]$, and let $$A(x) = \int_a^x f(t) dt.$$ Then the indefinite integral $A$ is continuous at each point of $[a, b]$. (At each endpoint we have one-sided continuity.)

> [!theorem]
> Assume $v$ is continuous at $p$ and that $u$ is continuous at $q$, where $q = v(p)$. Then the composite function $f = u \circ v$ is continuous at $p$.

### Intermediate-Value

> [!theorem] Bolzano's Theorem
> Let $f$ be continuous at each point of a closed interval $[a, b]$ and assume that $f(a)$ and $f(b)$ have opposite signs. Then there is at least one $c$ in the open interval $(a, b)$ such that $f(c) = 0$.

> [!theorem] Sign-Preserving Property of Continuous Functions
> Let $f$ be continuous at $c$ and suppose that $f(c) \neq 0$. Then there is an interval $(c - \delta, c + \delta)$ about $c$ in which $f$ has the same sign as $f(c)$.

> [!theorem] Intermediate-Value Theorem
> Let $f$ be continuous at each point of a closed interval $[a, b]$. Choose two arbitrary points $x_1 < x_2$ in $[a, b]$ such that $f(x_1) \neq f(x_2)$. Then $f$ takes on every value between $f(x_1)$ and $f(x_2)$ somewhere in the interval $(x_1, x_2)$.

> [!theorem]
> If $n$ is a positive integer and if $a > 0$, then there is exactly one positive $b$ such that $b^n = a$.
> If $n$ is an odd integer and $a < 0$, then there is exactly one negative $b$ such that $b^n = a$.

> [!theorem] Brouwer's Fixed-Point Theorem
> Given a real-valued function $f$ which is continuous on the closed interval $[a, b]$. Assume that $f(a) \leq a$ and that $f(b) \geq b$ then $f$ has a fixed point in $[a, b]$.

### Extreme-Value

> [!definition] Absolute Maximum/Minumum
> Let $f$ be a real-valued function defined on a set $S$ of real numbers. The function $f$ is said to have an **absolute maximum** on the set $S$ if there is at least one point $c$ in $S$ such that $$f(x) \leq f(c) \; \forall x \in S.$$
> The number $f(c)$ is called the absolute maximum value of $f$ on $S$. We say that $f$ has an **absolute minimum** on $S$ if there is a point $d$ in $S$ such that $$f(x) \geq f(d) \; \forall x \in S.$$

> [!theorem] Boundness Theorem for Continuous Functions
> Let $f$ be continuous on a closed interval $[a, b]$. Then $f$ is bounded on $[a, b]$. That is, there is a number $C \geq 0$ such that $|f(x)| \leq C$ for all $x$ in $[a, b]$.

> [!theorem] Extreme-Value Theorem for Continuous Functions
> Assume $f$ is continuous on a closed interval $[a, b]$. Then there exist points $c$ and $d$ in $[a, b]$ such that $$f(c) = \sup f \quad \text{and} \quad f(d) = \inf f.$$

### Small-span theorem

> [!definition] Span
> Let $f$ be real-valued and continuous on a closed interval $[a, b]$ and let $M(f)$ and $m(f)$ denote, respectively, the maximum and minimum values of $f$ on $[a, b]$. We shall call the difference $$M(f) - m(f)$$ the **span** of $f$ in the interval $[a, b]$.

> [!theorem]
> Let $f$ be continuous on a closed interval $[a, b]$. Then, for every $\epsilon > 0$ there is a partition of $[a, b]$ into a finite number of subintervals such that the span of $f$ in every subinterval is less than $\epsilon$.

## Inverse Function

> [!theorem]
> Assume $f$ is strictly increasing and continuous on an interval $[a, b]$. Let $c = f(a)$ and $d = f(b)$ and let $g$ be the inverse of $f$. That is, for each $y$ in $[c, d]$, let $g(y)$ be that $x$ in $[a, b]$ such that $y = f(x)$. Then
> 1. $g$ is strictly increasing on $[c, d]$;
> 2. $g$ is continuous on $[c, d]$.

