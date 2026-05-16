## Cyclic Codes

### Basic Definition

> [!definition] Cyclic Set
> A subset $S$ of $\mathbb F_q^n$ is cyclic if $(a_{n - 1}, a_0, a_1, \dots, a_{n - 2}) \in S$ whenever $(a_0, a_1, \dots, a_{n - 1}) \in S$.

> [!definition] Cyclic Code
> A linear code $C$ is called a **cyclic code** if $C$ is a cyclic set.

> [!proposition]
> Dual code of a cyclic code is also a cyclic code.

### Construction

> [!theorem]
> Let $\pi$ be the linear map defined by $$\pi: \mathbb F_q^n \rightarrow \mathbb F_q[x] / (x^n - 1), (a_0, a_1, \dots, a_{n - 1}) \mapsto a_0 + a_1 x + \dots + a_{n - 1}x^{n - 1}.$$
> Then a nonempty subset $C$ of $\mathbb F_q^n$ is a cyclic code if and only if $\pi(C)$ is an [[Ring#Ideal|ideal]] of $\mathbb F_q[x] / (x^n - 1)$.

> [!remark]
> As $\pi(C)$ is an ideal, there exist a generator polynomial.

> [!theorem]
> Each monic divisor of $x^n - 1$ is the generator polynomial of some cyclic code in $\mathbb F_q^n$.

> [!corollary]
> There is one-to-one correspondence between the cyclic codes in $\mathbb F_q^n$ and the monic divisors of $x^n - 1 \in \mathbb F_q[x]$.

> [!theorem]
> Let $x^n - 1 \in \mathbb F_q[x]$ have the factorization $$x^n - 1 = \prod_{i = 1}^r p_i^{e_i}(x),$$ where $p_1(x), p_2(x), \dots, p_r(x)$ are distinct monic irreducible polynomials and $e_i \geq 1$ for all $i = 1, 2, \dots, r$. Then there are $\prod_{i = 1}^r (e_i + 1)$ cyclic codes of length $n$ over $\mathbb F_q$.

> [!theorem]
> Let $g(x)$ be the generator polynomial of an ideal of $\mathbb F_q[x] / (x^n - 1)$. Then the corresponding cyclic code has dimension $k$ if the degree of $g(x)$ is $n - k$.

### Generator Matrix

> [!theorem] Generator Matrix of Cyclic Code
> Let $g(x) = g_0 + g_1 x + \dots + g_{n - k} x^{n - k}$ be the generator polynomial of a cyclic code $C$ in $\mathbb F_q^n$ with $\deg(g(x)) = n - k$. Then the matrix $$G = \begin{pmatrix}g(x) \\ x g(x) \\ \dots \\ x^{k - 1} g(x)\end{pmatrix}$$ is a generator matrix of $C$ (note that we identify a vector with polynomial).

### Parity Check Matrix

> [!theorem]
> Let $g(x)$ be the generator polynomial of a $q$-ary $[n, k]$ cyclic code $C$. Put $h(x) = (x^n - 1) / g(x)$. Then $h_0^{-1} h_R(x)$ is the generator polynomial of $C^{\perp}$, where $h_0$ is the constant term of $h(x)$.

> [!definition] Parity-check Polynomial
> Let $C$ be a $q$-ary cyclic code of length $n$. Put $h(x) = (x^n - 1) / g(x)$. Then, $h_0^{-1} h_R(x)$ is called the **parity-check polynomial** of $C$, where $h_0$ is the constant term of $h(x)$.

> [!corollary] Parity-Check Matrix of Cyclic Code
> Let $C$ be a $q$-ary $[n, k]$-cyclic code with generator polynomial $g(x)$. Put $h(x) = (x^n - 1) / g(x)$. Let $h(x) = h_0 + h_1 x + \dots + h_k x^k$. Then the matrix $$H = \begin{pmatrix}h_R(x) \\ x h_R(x) \\ \dots \\ x^{n - k - 1} h_R(x)\end{pmatrix}$$

### Decoding of Cyclic Codes

> [!theorem]
> Let $H = (I_{n - k} | A)$ be a parity-check matrix of a $q$-ary cyclic code $C$. Let $g(x)$ be the generator polynomial of $C$. Then the syndrome of a vector $w \in \mathbb F_q^n$ is equal to $(w(x) \pmod {g(x)})$; i.e., the principle remainder of $w(x)$ divided by $g(x)$.

> [!corollary]
