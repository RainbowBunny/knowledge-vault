## Carmichael Numbers

> [!definition] Carmichael Numer
> An integer $n > 1$ is called a **Carmichael number** if $n$ is composite and $(a, n) = 1 \Rightarrow a^{n - 1} \equiv 1 \mod n$ for all $a \in \mathbb Z$.

> [!theorem] Korselt's Criterion
> A composite integer $n > 1$ is a Carmichael number if and only if 
> 1. $n$ is square-free
> 2. For every prime $p$ dividing $n$, also $(p - 1) \mid (n - 1)$.

> [!corollary]
> A composite integer $n$ is a Carmichael number if and only if $a^n \equiv a \mod n$ for all $a \in \mathbb Z$.

> [!theorem]
> If $n$ is a Carmichael number then
> 1. $n$ is odd,
> 2. $n$ has at least three different prime factors,
> 3. every prime factor of $n$ is less than $\sqrt{n}$.
> 4. $(n, \phi(n)) = 1$.

> [!remark]
> The condition $(n, \phi(n)) = 1$ implies $n$ is square-free, since if $p^2 \mid n$ for some prime $p$ then $p \mid \phi(n)$, so $(n, \phi(n)) > 1$.

> [!theorem] Larsen
> If $m > 2$, then there are infinitely many Carmichael numbers divisible by $m$ if and only if $(m, \phi(m)) = 1$.

> [!example]
> If $k$ is a positive integer such that $6k + 1$, $12k + 1$, and $18k + 1$ are all prime then the product $n = (6k + 1)(12k + 1)(18k + 1)$ is a Carmichael number.

## Smooth Numbers

> [!definition] $B$-smooth Number
> An integer $n$ is called $B$-smooth if all of its prime factors are less than or equal to $B$.
> 

> [!definition] B-smooth counting function
> The function $\psi(X, B)$ counts $B$-smooth numbers, $$\psi(X, B) = \text{Number of } B\text{-smooth integers } n \text{ such that } 1 < n \leq X.$$ 

> [!theorem] Canfield, Erdos, Pomerance
> Fix a number $0 < \epsilon < 1$, and let $X$ and $B$ increase together while satisfying $$(\ln X)^\epsilon < \ln B < (\ln X)^{1 - \epsilon}$$
> For notational convenience, we let $$u = \frac{\ln X}{\ln B}.$$
> Then the number of $B$-smooth numbers less than $X$ satisfies $$\psi(X, B) = X \cdot u^{-u(1 + o(1))}.$$

> [!definition] B-power-smooth
> An integer $M$ is called $B$-power-smooth if every prime power $p^e$ dividing $M$ satisfies $p^e \leq B$.

> [!proposition]
> Properties of $B$-power-smooth
> 1. Suppose that $M$ is $B$-power-smooth, $M$ is also $B$-smooth.
> 2. $M$ is $B$-power-smooth if and only if $M$ divides the least common multiple of $[1, 2, \dots, B]$.

> [!remark]
> $$B\text{-power-}\text{smooth} \subsetneq B\text{-smooth}$$

> [!corollary]
> Let $L(x) = e^{\sqrt{(\ln X) (\ln \ln X)}}$ . For any fixed value of $c$ with $0 < c < 1$, $$\psi(X, L(x)^c) = X \cdot L(x)^{-(1/2c)(1 + o(1))} \text{ as } X \rightarrow \infty.$$

> [!proposition]
> Let $L(x) = e^{\sqrt{(\ln X) (\ln \ln X)}}$, $N$ be a large integer, and $B = L(N)^{\frac{1}{\sqrt 2}}.$
> 1. We expect to check approximately $L(N)^{\sqrt 2}$ random numbers modulo $N$ in order to find $\pi(B)$ numbers that are $B$-smooth.
> 2. We expect to check approximately $L(N)^{\sqrt 2}$ random numbers of the form $a^2 \pmod N$ in order to find enough $B$-smooth numbers to factor $N$.

> [!example]
> The function $L(X) = e^{\sqrt{(\ln X) (\ln \ln X)}}$ is subexponential.

> [!example]
> For any fixed positive constants $a$ and $b$, define the function $$F_{a, b}(X) = e^{(\ln X)^{1/a} (\ln \ln X)^{1 / b}}.$$
> 1. If $a > 1$, $F_{a, b}(X)$ is subexponential.
> 2. If $a = 1$, $F_{a, b}(X)$ is exponential.
> 3. If $a < 1$, $F_{a, b}(X)$ is superexponential.

