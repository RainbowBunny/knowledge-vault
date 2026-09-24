
> [!definition] Divide-and-conquer approach
> The divide-and-conquer paradigm involves three steps at each level of the recursion:
> - **Divide** the problem into a number of subproblems that are smaller instances of the same problem.
> - **Conquer** the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the subproblems in a straightforward manner.
> - **Combine** the solutions to the subproblems into the solution for the original problem.

## The Substitution Method for Solving Recurrences

> [!definition] Substitution Method
> The **substitution method** for solving recurrences comprises two steps:
> 1. Guess the form of the solution.
> 2. Use mathematical induction to find the constants and show that the solution works.

## The Recursion-Tree Method for Solving Recurrences

> [!definition] Recursion Tree
> Hmmmm


## The Master Method for Solving Recurrences

> [!theorem] Master Theorem
> Let $a \geq 1$ and $b > 1$ be constants, let $f(n)$ be a function, and let $T(n)$ be defined on the nonnegative integers by the recurrence $$T(n) = aT(\frac{n}{b}) + f(n)$$ where we interpret $\frac{n}{b}$ to mean either $\lfloor \frac{n}{b} \rfloor$ or $\lceil \frac{n}{b} \rceil$. Then $T(n)$ has the following asymptotic bounds:
> 1. If $f(n) = O(n^{\log_b a - \epsilon})$ for some constant $\epsilon > 0$, then $T(n) = \Theta(n^{\log_b a})$.
> 2. If $f(n) = \Theta(n^{\log_b a})$, then $T(n) = \Theta(n^{\log_b a} \log n)$.
> 3. If $f(n) = \ohm(n^{\log_b a + \epsilon})$ for some constant $\epsilon > 0$, and if $af(\frac{n}{b}) \leq cf(n)$ for some constant $c < 1$ and all sufficiently large $n$, then $T(n) = \Theta(f(n))$.

### Proof of the Master theorem

> [!lemma]
> Let $a \geq 1$ and $b > 1$ be constants, and let $f(n)$ be a nonnegative function defined on exact powers of $b$. Define $T(n)$ on exact powers of $b$ by the recurrence $$T(n) = \begin{cases}\Theta(1) &\text{if } n = 1 \\ aT(\frac{n}{b}) + f(n) &\text{if } n = b^i \end{cases}$$ where $i$ is a positive integer. Then $$T(n) = \Theta(n^{\log_b a}) + \sum_{j = 0}^{\log_b n - 1} a^j f(\frac{n}{b^j}).$$

> [!lemma]
> Let $a \geq 1$ and $b > 1$ be constants, and let $f(n)$ be a nonnegative function defined on exact powers of $b$. A function $g(n)$ defined over exact powers of $b$ by $$g(n) = \sum_{j = 0}^{\log_b n - 1} a^j f(\frac{n}{b^j})$$ has the following asymptotic bounds for exact powers of $b$:
> 1. If $f(n) = O(n^{\log_b a - \epsilon})$ for some constant $\epsilon > 0$, then $g(n) = O(n^{\log_b a})$.
> 2. If $f(n) = \Theta(n^{\log_b a})$, then $g(n) = \Theta(n^{\log_b a} \log n)$.
> 3. If $af(\frac{n}{b}) \leq cf(n)$ for some constant $c < 1$ and for all sufficiently large $n$, then $g(n) = \Theta(f(n))$.

> [!lemma]
> Let $a \geq 1$ and $b > 1$ be constants, and let $f(n)$ be a nonnegative function defined on exact powers of $b$. Define $T(n)$ on exact powers of $b$ by the recurrence $$T(n) = \begin{cases}\Theta (1) &\text{if } n = 1, \\ aT(\frac{n}{b}) + f(n) &\text{if } n = b^i,\end{cases}$$ where $i$ is a positive integer. Then $T(n)$ has the following asymptotic bounds for exact powers of $b$:
> 1. If $f(n) = O(n^{\log b_a - \epsilon})$ for some constant $\epsilon > 0$, then $T(n) = \Theta (n^{\log_b a})$.
> 2. If $f(n) = \Theta(n^{\log_b a})$, then $T(n) = \Theta(n^{\log_b a} \log n)$.
> 3. If $f(n) = \ohm(n^{\log_b a + \epsilon})$ for some constant $\epsilon > 0$, and if $af(\frac{n}{b}) \leq cf(n)$ for some constant $c < 1$ and all sufficiently large $n$, then $T(n) = \Theta(f(n))$.


