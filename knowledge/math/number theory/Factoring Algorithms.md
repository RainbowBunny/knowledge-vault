## Pollard's $p - 1$ factorization algorithm

> [!algorithm] Pollard’s \(p - 1\) Factorization Algorithm
> **Input:** An integer $N$ to be factored (targeting number that has a $B$-smooth factor)  
> **Output:** A nontrivial factor of $N$, or failure
> 
> ---
>
> 1. Set:
>    $$a \gets 2$$
>    (or some other convenient initial value).
>
> 2. For $j = 2, 3, 4, \ldots$ up to a specified bound, do:
>
>    2.1. Set:
>    $$a \gets a^j \pmod N.$$
>
>    2.2. Compute:
>    $$d \gets \gcd(a - 1, N).$$
>
>    2.3. If
>    $$1 < d < N,$$
>    then return $d$ (success).
>
> 3. If no such $d$ is found, return failure.
>
> ---
>
> **Efficiency Note:**  
> For improved efficiency, choose an integer $k$ and compute the greatest
> common divisor in Step 2.2 only every $k$th iteration.

## Factoring via difference of squares

> [!algorithm] Three-Step Factorization Procedure
> **Input:** An integer $N$ to be factored  
> **Output:** A nontrivial factor of $N$, with high probability
>
>---
>
> 1. **Relation Building:**  
>    Find many integers $a_1, a_2, \ldots, a_r$ such that each quantity
>    $$c_i \equiv a_i^2 \pmod N$$
>    factors completely over a set of small primes.
>
> 2. **Elimination:**  
>    Choose a subset $\{c_{i_1}, c_{i_2}, \ldots, c_{i_s}\}$ such that every prime appearing in the product occurs to an even power. Then
>    $$c_{i_1} c_{i_2} \cdots c_{i_s} = b^2$$
>    is a perfect square.
>
> 3. **GCD Computation:**  
>    Let
>    $$a \gets a_{i_1} a_{i_2} \cdots a_{i_s},$$
>    and compute
>    $$d \gets \gcd(N, a - b).$$
>
>    Since
>    $$\begin{aligned}
>    a^2
>      &= (a_{i_1} a_{i_2} \cdots a_{i_s})^2 \\
>      &\equiv a_{i_1}^2 a_{i_2}^2 \cdots a_{i_s}^2
>       \equiv c_{i_1} c_{i_2} \cdots c_{i_s}
>       \equiv b^2 \pmod N,
>    \end{aligned}$$
>    there is a reasonable chance that $d$ is a nontrivial factor of $N$.

> [!definition] Factor Base
> The set of primes less than $B$ (or sometimes the set of prime powers less than $B$) is called the **factor base**.

## Lenstra’s Elliptic Curve Factorization Algorithm

> [!algorithm] Lenstra’s Elliptic Curve Factorization Algorithm (ECM)
> **Input:** An integer $N$ to be factored  
> **Output:** A nontrivial factor of $N$, or failure
>
> ---
>
> 1. Choose random values $A, a, b \in \mathbb{Z}/N\mathbb{Z}$.
>
> 2. Set:
>    $$P \gets (a, b)$$
>    and compute:
>    $$B \equiv b^2 - a^3 - A a \pmod N.$$
>
>    Let $E$ be the elliptic curve:
>    $$E : y^2 = x^3 + A x + B \pmod N.$$
>
> 3. For $j = 2, 3, 4, \ldots$ up to a specified bound, do:
>
>    3.1. Attempt to compute:
>    $$Q \gets jP \pmod N$$
>    using elliptic curve point addition.
>
>    3.2. Set:
>    $$P \gets Q.$$
>
>    3.3. If the computation in Step 3.1 fails, then a nontrivial
>    divisor $d > 1$ of $N$ has been found.
>
>    3.4. If $d < N$, return $d$ (success).
>
>    3.5. If $d = N$, return to Step 1 and choose a new curve and point.
>
> 4. If no factor is found within the bound, return failure.
> ---
> If $p$ is the smallest factor of $N$, then the elliptic curve factorization algorithm has an average running time approximately $$O(e^{\sqrt{2 (\log p) (\log \log p)}}) \text{ steps}.$$

## Factorize with Sum and Product

Suppose that we have $p + q$ and $p q$, we can solve the quadratic formula $$X^2 - (p + q)X + pq,$$since this polynomial factors as $(X - p)(X - q),$ so its roots are $p$ and $q$.

## Factorize with Encryption and Decryption Exponent

> [!algorithm] Factoring RSA Modulus from $(N,e,d)$
> **Input:**  
> - RSA modulus $N = pq$  
> - Public exponent $e$  
> - Private exponent $d$
>
> **Output:**  
> The prime factors $p$ and $q$ of $N$
>
> ---
>
> 1. Compute
>    $$k \gets ed - 1.$$
>
> 2. Write
>    $$k = 2^t \cdot r,$$
>    where $r$ is odd.
>
> 3. Repeat:
>
>    3.1. Choose a random integer
>    $$a \in \{2,3,\dots,N-2\}.$$
>
>    3.2. Compute
>    $$x \gets a^r \bmod N.$$
>
>    3.3. If $x = 1$ or $x = -1 \pmod N$, go back to Step 3.1.
>
>    3.4. For $i = 1$ to $t-1$, do:
>    - Compute
>      $$y \gets x^2 \bmod N.$$
>    - If $y = 1$, output
>      $$p \gets \gcd(x-1, N), \qquad q \gets \frac{N}{p}$$
>      and halt.
>    - Set $x \gets y$.
>
> 4. Repeat Step 3 until factors are found.
