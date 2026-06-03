## Divisibility and Greatest Common Divisors

> [!definition] Divides and Divisible: 
> Let $a$ and $b$ be integers with $b \neq 0$. We say that $b$ **divides** $a$, or that $a$ is **divisible** by $b$, if there is an integer $c$ such that $$a = bc.$$We write $b \mid a$ to indicate that $b$ divides $a$. If $b$ does not divide $a$, then we write $b \nmid a.$

> [!proposition] 
> Let $a, b, c \in \mathbb Z$ be integers.
>- If $a \mid b$ and $b \mid c$, then $a \mid c.$
>- If $a \mid b$ and $b \mid a$, then $a = \pm b.$
>- If $a \mid b$ and $a \mid c$, then $a \mid (b + c)$ and $a \mid (b - c).$

> [!definition] Common Divisor and Greatest Common Divisor
>  A **common divisor** of two integers $a$ and $b$ is a positive integer $d$ that divides both of them. The **greatest common divisor** of $a$ and $b$ is the largest positive integer $d$ such that $d \mid a$ and $d \mid b$. The greatest common divisor of $a$ and $b$ is denoted $\gcd(a, b)$. If there is no possibility of confusion, it is also sometimes denoted by $(a, b)$. (If $a$ and $b$ are both $0$, then $\gcd(a, b)$ is not defined.)

> [!definition] Division Algorithm
>  Let $a$ and $b$ be positive integers. Then $a$ divided by $b$ has quotient $q$ and remainder $r$ means that $$a = b \cdot q + r \qquad \text{with } 0 \leq r < b.$$

> [!theorem] The Euclidean Algorithm
>  Let $a$ and $b$ be positive integers with $a \geq b$. The following algorithm computes $\gcd(a, b)$ in a finite number of steps.
>1. Let $r_0 = a$ and $r_1 = b$.
>2. Set $i = 1$.
>3. Divide $r_{i - 1}$ by $r_i$ to get a quotient $q_i$ and remainder $r_{i + 1}$: $$r_{i - 1} = r_i q_i + r{i + 1} \qquad \text{with } 0 \leq r_{i + 1} < r_i.$$
>4. If the remainder $r_{i + 1} = 0$, then $r_i = \gcd(a, b)$ and the algorithm terminates.
>5. Otherwise, $r_{i + 1} > 0$, so set $i = i + 1$ and go to Step 3.
>
The division step (Step 3) is executed at most $2 \log_2{b} + 1$ times.

> [!algorithm] Storage-Efficient Extended Euclidean Algorithm
> **Input:**  
> Positive integers $a$ and $b$
>
> **Output:**  
> - $g = \gcd(a,b)$  
> - Integers $(u,v)$ satisfying
> $$a u + b v = g$$
>
> ---
>
> 1. Initialize:
>    $$u \gets 1,\quad g \gets a,\quad x \gets 0,\quad y \gets b.$$
>
> 2. If $y = 0$, set
>    $$v \gets \frac{g - a u}{b}$$
>    and return $(g,u,v)$.
>
> 3. Divide $g$ by $y$ with remainder:
>    $$g = qy + t,\quad 0 \le t < y.$$
>
> 4. Set:
>    $$s \gets u - qx.$$
>
> 5. Update:
>    $$u \gets x,\quad g \gets y.$$
>
> 6. Update:
>    $$x \gets s,\quad y \gets t.$$
>
> 7. Go to Step 2.

> [!theorem] The Extended Euclidean Algorithm
>  Let $a$ and $b$ be positive integers. Then the equation $$au + bv = \gcd(a, b)$$always has a solution in integers $u$ and $v$.
If $(u_0, v_0)$ is any one solution, then every solution has the form
$$u = u_0 + \frac{b \cdot k}{\gcd(a, b)} \text{ and } v = v_0 - \frac{a \cdot k}{\gcd(a, b)} \text{ for some } k \in \mathbb Z$$

> [!example]
> Let $a_1, a_2, \dots, a_k$ be integers with $\gcd(a_1, a_2, \dots, a_k) = 1$, i.e., the largest positive integer dividing all of $a_1, \dots, a_k$ is $1$. The equation $$a_1 u_1 + a_2 u_2 + \cdots + a_k u_k = 1$$ has a solution in integers $u_1, u_2, \dots, u_k$.

> [!definition] Relatively Prime
>  Let $a$ and $b$ be integers. We say that $a$ and $b$ are **relatively prime** if $\gcd(a, b) = 1$.

> [!remark]
> $\text{RELPRIME} = \{\langle x, y \rangle | x \text{ and } y \text{ are relatively prime}\}$ is in [[Complexity Theory#Class P|Class P]].

## Modular Arithmetic

> [!definition] Congruent Modulo
>  Let $m \geq 1$ be an integer. We say that the integers $a$ and $b$ are **congruent modulo** $m$ if their difference $a - b$ is divisible by $m$. We write $$a \equiv b \pmod m$$to indicate that $a$ and $b$ are congruent modulo $m$. The number $m$ is called the **modulus**.

> [!proposition] 
> Let $m \geq 1$ be an integer.
>- If $a_1 \equiv a_2 \pmod m$ and $b_1 \equiv b_2 \pmod m$, then $$a_1 \pm b_1 \equiv a_2 \pm b_2 \pmod m \quad \text{ and } \quad a_1 \cdot b_1 \equiv a_2 \cdot b_2 \pmod m.$$
>- Let $a$ be an integer. Then $$a \cdot b \equiv 1 \pmod m \quad \text{for some integer } b \text{ if and only if } \gcd(a, m) = 1.$$If such an integer $b$ exists, then we say that $b$ is the (multiplicative) inverse of a modulo $m.$

> [!definition] Ring of Integers
>  We write $$\mathbb Z / m \mathbb Z = \{0, 1, \dots, m - 1\}$$and call $\mathbb Z / m\mathbb Z$ the **ring of integers modulo** $m$. Whenever we perform an addition or multiplication in $\mathbb Z / m \mathbb Z$, we divide the result by $m$ and take the remainder in order to obtain an element in $\mathbb Z / m \mathbb Z$.

### Modular Reduction

> [!definition] Modular Reduction
> For an even (resp. odd) positive integer $\alpha$, we define $r' = r \mod^{\pm} \alpha$ to be the unique element $r'$ in the range $-\frac{\alpha}{2} < r' \leq \frac{\alpha}{2}$ (resp. $-\frac{\alpha - 1}{2} \leq r' \leq \frac{\alpha - 1}{2}$) such that $r' \equiv r \mod \alpha$. We will sometimes refer to this as a **centered** reduction modulo $q$.

### Modular Exponentiation

> [!algorithm] Fast Powering Algorithm
> **Input:** Integers $g, A, N$  
> **Output:** $g^A \bmod N$
> 
> ---
>
> 1. Compute the binary expansion of $A$:
>    $$A = A_0 + A_1 \cdot 2 + A_2 \cdot 2^2 + \cdots + A_r \cdot 2^r,$$
>    where $A_0, \ldots, A_r \in \{0,1\}$ and $A_r = 1$.
>
> 2. Compute the powers $g^{2^i} \bmod N$ for $0 \le i \le r$ by successive squaring:
>    $$\begin{aligned}
>    a_0 &\equiv g \pmod{N} \\
>    a_1 &\equiv a_0^2 \equiv g^2 \pmod{N} \\
>    a_2 &\equiv a_1^2 \equiv g^{2^2} \pmod{N} \\
>    a_3 &\equiv a_2^2 \equiv g^{2^3} \pmod{N} \\
>    &\ \vdots \\
>    a_r &\equiv a_{r-1}^2 \equiv g^{2^r} \pmod{N}.
>    \end{aligned}$$
>
> 3. Compute $g^A \bmod N$ using the binary expansion:
>    $$\begin{aligned}
>    g^A
>    &= g^{A_0 + A_1 2 + A_2 2^2 + \cdots + A_r 2^r} \\
>    &= g^{A_0} (g^2)^{A_1} (g^{2^2})^{A_2} \cdots (g^{2^r})^{A_r} \\
>    &\equiv a_0^{A_0} a_1^{A_1} a_2^{A_2} \cdots a_r^{A_r} \pmod{N}.
>    \end{aligned}$$
>---
> **Complexity of the algorithm**: $2 \log_2(A)$ multiplication modulo $N$.

> [!algorithm] Low-Storage Modular Exponentiation
> **Input:**  
> Positive integers $N$, $g$, and $A$
>
> **Output:**  
> The value
> $$g^{A} \bmod N$$
>
> ---
>
> 4. Initialize:
>    $$a \gets g,\qquad b \gets 1.$$
>
> 5. While $A > 0$, do:
>
>    2.1. If $A \equiv 1 \pmod 2$, set
>    $$b \gets b \cdot a \pmod N.$$
>
>    2.2. Set
>    $$a \gets a^2 \pmod N,$$
>    and
>    $$A \gets \left\lfloor \frac{A}{2} \right\rfloor.$$
>
> 6. Return $b$.

## Euler Totient Function

> [!definition] Euler's Phi Function
>  **Euler's Phi Function** is the function $\phi(m)$ defined by the rule $$\phi(m) = \# (\mathbb Z / m \mathbb Z)^* = \# \{0 \leq a < m : \gcd(a, m) = 1\}.$$

> [!proposition]
> $m$ is prime if and only if $\phi(m) = m - 1$.

> [!theorem] Euler's Formula
> $a^{\phi(N)} \equiv 1 \pmod N$ for all integers $a$ satisfying $\gcd(a, N) = 1$.

> [!proposition] Properties of Euler's Formula
> Let $M$ and $N$ be integers satisfying $\gcd(M, N) = 1$, $$\phi(MN) = \phi(M) \phi(N).$$
> Let $p_1, p_2, \dots, p_r$ be distinct primes that divide $N$, $$\phi(N) = N \prod_{i = 1}^r (1 - \frac{1}{p_i}).$$

> [!example]
> Let $N$, $c$ and $e$ be positive integers satisfying the condition $\gcd(N, c) = 1$ and $\gcd(e, \phi(N)) = 1$, the solution of $$x^e \equiv c \pmod N$$ is $c^{d} \pmod N$ where $d = e^{-1} \pmod {\phi(N)}$.

## The Chinese Remainder Theorem

> [!theorem] Chinese Remainder Theorem
> Let $m_1, m_2, \dots, m_k$ be a collection of pairwise relatively prime integers. This means that $$\gcd(m_i, m_j) = 1 \quad \forall i \neq j$$
> Let $a_1, a_2, \dots, a_k$ be arbitrary integers. Then the system of simultaneous congruences $$x \equiv a_1 \pmod {m_1}, \quad x \equiv a_2 \pmod {m_2}, \quad \dots, \quad x \equiv a_k \pmod {m_k}$$ has a unique solution $x = c \pmod {m_1 m_2 \cdots m_k}$.

## Euler Formula

> [!theorem] Euler's Formula for $pq$
> Let $p$ and $q$ be distinct primes and let $$g = \gcd(p - 1, q - 1).$$ Then $$a^{\frac{(p - 1)(q - 1)}{g}} \equiv 1 \pmod {pq} \; \forall a : \gcd(a, pq) = 1.$$ In particular, if $p$ and $q$ are odd primes, then $$a^{\frac{(p - 1)(q - 1)}{2}} \equiv 1 \pmod {pq} \; \forall a : \gcd(a, pq) = 1$$

> [!proposition]
> Let $p$ be a prime and let $e \geq 1$ be an integer satisfying $\gcd(e, p - 1) = 1$. Then $e$ has an inverse modulo $p - 1$, say $$de \equiv 1 \pmod {p - 1}.$$ Then the congruence $$x^e \equiv c \pmod p$$ has the unique solution $x \equiv c^d \pmod p$.

> [!proposition] 
> Let $p$ and $q$ be distinct primes and let $e \geq 1$ satisfy $$\gcd(e, (p - 1)(q - 1)) = 1.$$ Then $e$ has an inverse modulo $(p - 1)(q - 1)$, say $$de \equiv 1 \pmod {(p - 1)(q - 1)}.$$ Then the congruence $$x^e \equiv c \pmod {pq}$$ has the unique solution $x \equiv c^d \pmod {pq}$.

## Quadratic Residues and Quadratic Reciprocity

> [!proposition] Square root modulo $p = 4k + 3$
> Let $p$ be a prime satisfying $p \equiv 3 \pmod 4$. Let $a$ be an integer such that the congruence $x^2 \equiv a \pmod p$ has a solution. Then $$b \equiv a^{\frac{p + 1}{4}} \pmod p$$ is a solution; it satisfies $b^2 \equiv a \pmod p$.

> [!definition] Quadratic Residue
> Let $p$ be an odd prime number and let $a$ be a number with $p \nmid a$. We say that $a$ is a **quadratic residue modulo** $p$ if $a$ is a square modulo $p$, i.e., if there is a number $c$ so that $c^2 \equiv a \pmod p$. If $a$ is not a square modulo $p$, i.e., if there exists no such $c$, then $a$ is called a **quadratic nonresidue modulo** $p$.

> [!proposition]
> Let $p$ be an odd prime number and let $b$ be an integer with $p \nmid b$. Then,
> 1. Either $b$ has two square roots modulo $p$ or else $b$ has no square roots modulo $p$.
> 2. Let $g$ be a primitive root modulo $p$, so $b \equiv g^k \pmod p$. Then, $b$ has square root modulo $p$ if and only if $k$ is even.

> [!proposition]
> Let $p \geq 3$ be a prime and suppose that the congruence $$X^2 \equiv b \pmod p$$ has a solution.
> 1. For every exponent $e \geq 1$ the congruence $$X^2 \equiv b \pmod {p^e}$$ has a solution.
 
> [!proposition]
> Let $p$ be an odd prime number,
> 1. The product of two quadratic residues modulo $p$ is a quadratic residue modulo $p$.
> 2. The product of a quadratic residue and a quadratic nonresidue modulo $p$ is a quadratic nonresidue modulo $p$.
> 3. The product of two quadratic nonresidue modulo $p$ is a quadratic residue modulo $p$.

> [!definition] Legendre Symbol
> Let $p$ be an odd prime. The **Legendre symbol** of $a$ is the quantity $(\frac{a}{p})$ defined by the rules $$(\frac{a}{p}) = \begin{cases}
> 1 \quad &\text{if } a \text{ is a quadratic residue modulo } p,\\
> -1 \quad &\text{if } a \text{ is a quadratic nonresidue modulo } p,\\
> 0 \quad &\text{if } p \mid a
> \end{cases}$$
> Another formulation: $$(\frac{a}{p}) = a^{\frac{(p - 1)}{2}} \pmod p$$

> [!theorem] Quadratic Reciprocity
> Let $p$ and $q$ be odd primes.
> 1. $(\frac{-1}{p}) = \begin{cases}1 &\text{if } p \equiv 1 &\pmod 4 \\ -1 &\text{if } p \equiv -1 &\pmod 4 \end{cases}$ or $(\frac{-1}{p}) = (-1)^{\frac{p - 1}{2}}$
> 2. $(\frac{2}{p}) = \begin{cases}1 &\text{if } p \equiv 1 \text{ or } 7 \pmod 8 \\ -1 &\text{if } p \equiv 3 \text{ or } 5 \pmod 8\end{cases}$ or $(\frac{2}{p}) = (-1)^{\frac{p^2 - 1}{8}}$
> 3. $(\frac{p}{q}) = \begin{cases} (\frac{p}{q}) &\text{ if } p \equiv 1 \pmod 4 \text{ or } q \equiv 1 \pmod 4 \\ -(\frac{p}{q}) &\text{ if } p \equiv 3 \pmod 4 \text{ and } q \equiv 3 \pmod 4 \end{cases}$ or $(\frac{p}{q})(\frac{q}{p}) = (-1)^{\frac{p - 1}{2} \cdot \frac{q - 1}{2}}$

> [!theorem] Jacobi Symbol
> Let $a$ and $b$ be integers and let $b$ be odd and positive. Suppose that the factorization of $b$ into primes is $$b = p_1^{e_1} p_2^{e_2} p_3^{e_3} \cdots p_t^{e_t}.$$
> The **Jacobi Symbol** $(\frac{a}{b})$ is defined by the formula $$(\frac{a}{b}) = (\frac{a}{p_1})^{e_1} (\frac{a}{p_2})^{e_2} (\frac{a}{p_3})^{e_3} \cdots (\frac{a}{p_t})^{e_t}$$

> [!proposition] 
> Let $a, a_1, a_2, b, b_1, b_2$ be integers with $b, b_1, b_2$ positive and odd
> 1. $(\frac{a_1a_2}{b}) = (\frac{a_1}{b})(\frac{a_2}{b})$ and $(\frac{a}{b_1 b_2}) = (\frac{a}{b_1}) (\frac{a}{b_2})$
> 2. If $a_1 \equiv a_2 \pmod b$, then $(\frac{a_1}{b}) = (\frac{a_2}{b}).$

> [!theorem] Quadratic Reciprocity: Version II
> Let $a$ and $b$ be integers that are odd and positive
> 1. $(\frac{-1}{b}) = \begin{cases}1 &\text{if } b \equiv 1 &\pmod 4 \\ -1 &\text{if } b \equiv -1 &\pmod 4 \end{cases}$
> 2. $(\frac{2}{b}) = \begin{cases}1 &\text{if } b \equiv 1 \text{ or } 7 \pmod 8 \\ -1 &\text{if } b \equiv 3 \text{ or } 5 \pmod 8\end{cases}$
> 3. $(\frac{a}{b}) = \begin{cases} (\frac{b}{a}) &\text{ if } p \equiv 1 \pmod 4 \text{ or } q \equiv 1 \pmod 4 \\ -(\frac{b}{a}) &\text{ if } p \equiv 3 \pmod 4 \text{ and } q \equiv 3 \pmod 4 \end{cases}$

> [!example]
> For any $a \in \mathbb F_p^*$, the discrete logarithm of $a$ is a number $\log_g(a)$ satisfying $$g^{\log_g(a)} \equiv a \pmod p.$$ Then $$(\frac{a}{p}) = (-1)^{\log_g(a)} \quad \forall a \in \mathbb F_p^*.$$

## Cubic Residues

> [!definition] Cubic Residue
> Let $p \geq 5$ be a prime. We say that $a$ is a **cubic residue** modulo $p$ if $p \nmid a$ and there is an integer $c$ satisfying $a \equiv c^3 \pmod p$.

> [!proposition] 
> Properties of cubic residue:
> 1. Let $a$ and $b$ be cubic residues modulo $p$, then $ab$ is a cubic residue modulo $p$.
> 2. Let $g$ be a primitive root modulo $p$, then $a$ is a cubic residue modulo $p$ if and only if $3 \mid \log_g(a)$.

