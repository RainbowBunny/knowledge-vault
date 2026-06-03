## Linear Code

> [!definition] Linear Code
> A **linear code** $C$ of length $n$ over $\mathbb F_q$ is a subspace of $\mathbb F_q^n$.

> [!definition] Dual Code, Dimension
> Let $C$ be a linear code over $\mathbb F_q$.
> 1. The **dual code** of $C$ is $C^{\perp}$, the orthogonal complement of the subspace $C$ of $\mathbb F_q^n$.
> 2. The **dimension** of the linear code $C$ is the dimension of $C$ as a vector space over $\mathbb F_q$, i.e., $\dim(C)$.

> [!theorem]
> Let $C$ be a linear code of length $n$ over $\mathbb F_q$. Then,
> 1. $|C| = q^{\dim(C)}$, i.e., $\dim(C) = \log_q |C|$;
> 2. $C^{\perp}$ is a linear code and $\dim(C) + \dim(C)^{\perp} = n$;
> 3. $(C^\perp)^\perp = C$.

> [!remark]
> A linear code $C$ of length $n$ and dimension $k$ over $\mathbb F_q$ is often called a $q$-ary $[n, k]$-code or, if $q$ is clear from the context, an $[n, k]$-code. It is also an $(n, q^k)$-linear code. If the distance $d$ of $C$ is known, it is also sometimes referred to as an $[n, k, d]$-linear code.

> [!definition] Self-orthogonal, Self-dual
> Let $C$ be a linear code.
> 1. $C$ is **self-orthogonal** if $C \subseteq C^{\perp}$.
> 2. $C$ is **self-dual** if $C = C^{\perp}$.

> [!proposition]
> The dimension of a self-orthogonal code of length $n$ must be $\leq n/2$, and the dimension of a self-dual code of length $n$ is $n/2$.

### Hamming Weight

> [!definition] Hamming weight
> Let $x$ be a word in $\mathbb F_q^n$. The **(Hamming) weight** of $x$, denoted by $\text{wt}(x)$, is defined to be the number of nonzero coordinates in $x$; i.e., $$\text{wt}(x) = d(x, 0),$$ where $0$ is the zero word.

> [!proposition]
> 1. If $x, y \in \mathbb F_q^n$, then $d(x, y) = \text{wt}(x - y)$.
> 2. If $q$ is even, then we also have $d(x, y) = \text{wt}(x + y)$.
> 3. If $x, y \in \mathbb F_2^n$, then $\text{wt}(x + y) = \text{wt}(x) + \text{wt}(y) - 2 \text{wt}(x \star y)$
> 4. For any prime power $q$ and $x, y \in \mathbb F_q^n$, we have $$\text{wt}(x) + \text{wt}(y) \geq \text{wt}(x + y) \geq \text{wt}(x) - \text{wt}(y).$$

> [!definition] Minimum (Hamming) weight
> Let $C$ be a code (not necessarily linear). The **minimum (Hamming) weight** of $C$, denoted $\text{wt}(C)$, is the smallest of the weights of the nonzero codewords of $C$.

> [!theorem]
> Let $C$ be a linear code over $\mathbb F_q$. Then $d(C) = \text{wt}(C)$.

> [!remark] Advantages of Linear Codes
> 1. As a linear code is a vector space, it can be described completely by using a basis
> 2. The distance of a linear code is equal to the smallest weight of its nonzero codewords.
> 3. The encoding and decoding procedures for a linear code are faster and simpler than those for arbitrary nonlinear codes.

> [!definition] Minimum Distance
> Let $C$ be an $[n, k]$ linear code over $\mathcal R$ and let $\omega$ be a norm on $\mathcal R$. The minimum distance of $C$ is: $$d = \min_{u, v \in C, u \neq v} \omega(u - v).$$
> 
> A code of length $n$ and dimension $k$ with minimum distance $d$ is capable of decoding arbitrary patterns of up to $\Delta = \lfloor \frac{d - 1}{2} \rfloor$ errors and is denoted as an $[n, k, d]$ code.

> [!algorithm] Find Basis of Dual Code
> **Input**: A nonempty subset $S$ of $\mathbb F_q^n$.
> **Output**: A basis for the dual code $C^\perp$, where $C = <S>$.
> **Description**: Form the matrix $A$ whose rows are the words in $S$. Use elementary row operations to place $A$ in reduced row echelon form (RREF). Let $G$ be the $k \times n$ matrix consisting of all the nonzero rows of the RREF: $$A \rightarrow \begin{pmatrix}G \\ O\end{pmatrix}.$$ (Here, $O$ denotes the zero matrix.)
> The matrix $G$ contains $k$ leading columns. Permute the columns of $G$ to form $$G' = \begin{pmatrix}I_k | X\end{pmatrix}.$$ Form a matrix $H'$ as follows: $$H' = \begin{pmatrix}-X^T | I_{n - k}\end{pmatrix},$$ where $X^T$ denotes the transpose of $X$.
> Apply the inverse of permutation applied to the columns of $G$ to the columns of $H'$ to form $H$. Then the rows of $H$ form a basis for $C^\perp$.

### Generator Matrix and Parity-Check Matrix

> [!definition] Generator Matrix
> A **generator matrix** for a linear code $C$ is a matrix $G$ whose rows form a basis for $C$.

> [!definition] Parity-Check Matrix
> A **parity-check matrix** $H$ for a linear code $C$ is a generator matrix for the dual code $C^{\perp}$.

> [!definition] Standard Form
> 1. A generator matrix of the form $(I_k, X)$ is said to be in **standard form**.
> 2. A parity-check matrix in the form $(Y, I_{n - k})$ is said to be in **standard form**.

> [!lemma]
> Let $C$ be an $[n, k]$-linear code over $\mathbb F_q$, with generator matrix $G$. Then, $v \in \mathbb F_q^n$ belongs to $C^{\perp}$ if and only if $v$ is orthogonal to every row of $G$; i.e., $v \in C^\perp \Leftrightarrow vG^T = 0$. In particular, given an $(n - k) \times n$ matrix $H$, then $H$ is a parity check matrix for $C$ if and only if the rows of $H$ are linearly independent and $HG^T = O$.

> [!theorem]
> Let $C$ be a linear code and let $H$ (size $(n - k) \times n$) be a parity-check matrix for $C$. Then
> 1. $C$ has distance $\geq d$ if and only if any $d - 1$ **columns** of $H$ are linearly independence; and
> 2. $C$ has distance $\leq d$ if and only if $H$ has $d$ **columns** that are linearly dependent.

### Equivalence of linear codes

> [!definition] Equivalent
> Two $(n, M)$-codes over $\mathbb F_q$ are **equivalent** if one can be obtained from the other by a combination of operations of the following types:
> 1. Permutation of the $n$ digits of the codewords;
> 2. Multiplication of the symbols appearing in a fixed position by a nonzero scalar.

> [!theorem]
> Any linear code $C$ is equivalent to a linear code $C'$ with a generator matrix in standard from.

### Encoding with a Linear Code

> [!definition] Encoding
> Let $C$ be an $[n, k, d]$-linear code over the finite field $\mathbb F_q$. Each codeword of $C$ can represent one piece of information, so $C$ can represent $q^k$ distinct pieces of information. If we fix a basis $\{r_1, \dots, r_k\}$ then each information piece $v$ can be represent: $$v = \sum_{i = 1}^k u_i r_i$$ where $u_i \in \mathbb F_q$ and if we choose generator matrix $G$ whose $i$-th row is $r_i$ then we have $$v = uG.$$ This process is called **encoding**.

> [!remark] Advantages of $G$ in the standard form
> 1. If a linear code $C$ has generator matrix $G = (I | X)$, then we can easily calculate the parity-check matrix for $C$: $$H = (-X^T | I).$$ 
> 2. If an $[n, k, d]$-linear code $C$ has a generator matrix $G$ in standard form, $G = (I | X)$, then it is trivial to recover the message $u$ from the codeword $v = uG$ since $$v = uG = u(I | X) = (u, uX);$$ i.e., the first $k$ digits in the codeword $v = uG$ give the message $u$ (**message digits**), the remaining $n - k$ digits are called **check digits** (**redundancy** added to protection against noise).

### Decoding with a Linear Code

> [!definition] Coset
> Let $C$ be a linear code of length $n$ over $\mathbb F_q$, and let $u \in \mathbb F_q^n$ be any vector of length $n$; we define the **coset** of $C$ determined by $u$ to be the set $$C + u = \{v + u : v \in C\} (= u + C)$$

> [!theorem]
> Let $C$ be an $[n, k, d]$-linear code over the finite field $\mathbb F_q$. Then, 
> 1. Every vector of $\mathbb F_q^n$ is contained in some cosets of $C$;
> 2. For all $u \in \mathbb F_q^n$, $|C + u| = |C| = q^k$;
> 3. For all $u, v \in \mathbb F_q^n, u \in C + v$ implies that $C + u = C + v$;
> 4. Two cosets are either identical or they have empty intersection;
> 5. There are $q^{n - k}$ different cosets of $C$;
> 6. For all $u, v \in \mathbb F_q^n, u - v \in C$ if and only if $u$ and $v$ are in the same coset.

> [!definition] Coset Leader
> A word of the least (Hamming weight) in a coset is called a **coset leader**.

> [!proposition] Nearest Neighbour Decoding for Linear Code
> Let $C$ be a linear code. Assume the codeword $v$ is transmitted and the word $w$ is received, resulting in the **error pattern** (or **error string**) $$e = w - v \in w + C.$$ The nearest neighbour decoding rule is thus upon receiving $w$, we choose a word $e$ of least weight in the coset $w + C$ and conclude that $v = w - e$ was the codeword transmitted.

> [!definition] Syndrome
> Let $C$ be an $[n, k, d]$-linear code over $\mathbb F_q$ and let $H$ be a parity-check matrix for $C$. For any $w \in \mathbb F_q^n$, the **syndrome** of $w$ is the word $S(w) = wH^T \in \mathbb F_q^{n - k}$.

> [!theorem]
> Let $C$ be an $[n, k, d]$-linear code and let $H$ be a parity-check matrix for $C$. For $u, v \in \mathbb F_q^n$, we have
> 1. $S(u + v) = S(u) + S(v)$;
> 2. $S(u) = 0$ if and only if $u$ is a codeword in $C$;
> 3. $S(u) = S(v)$ if and only if $u$ and $v$ are in the same coset of $C$.

> [!definition] Syndrome Look-up Table
> A table which matches each coset leader with its syndrome is called a **syndrome look-up table** (**standard decoding array**).

## Reed-Muller Codes

> [!definition] First Order Reed-Muller codes
> The **(first order) Reed-Muller codes** $\mathcal R(1, m)$ are binary codes defined, for all integers $m \geq 1$, recursively as follows:
> 1. $\mathcal R(1, 1) = \mathbb F_2^2 = \{00, 01, 10, 11\}$;
> 2. For $m \geq 1$, $$\mathcal R(1, m + 1) = \{(u, u): u \in \mathcal R(1, m)\} \cup \{(u, u + 1): u \in \mathcal R(1, m)\}.$$

> [!proposition]
> For $m \geq 1$, the Reed-Muller code $\mathcal R(1, m)$ is a binary $[2^m, m + 1, 2^{m - 1}]$-linear code, in which every codeword except $0$ and $1$ has weight $2^{m - 1}$.

> [!proposition]
> 1. A generator matrix of $\mathcal R(1, 1)$ is $$\begin{pmatrix}1 & 1 \\ 0 & 1\end{pmatrix}$$
> 2. If $G_m$ is a generator matrix for $\mathcal R(1, m)$, then a generator matrix for $\mathcal R(1, m + 1)$ is $$G_{m + 1} = \begin{pmatrix}G_m & G_m \\ 0\cdots 0 & 1\cdots 1\end{pmatrix}$$

> [!proposition]
> The dual code $\mathcal R(1, m)^{\perp}$ is (equivalent to) the extended binary Hamming code $\overline{\text{Ham}(m, 2)}$.

> [!definition] $r$-th order Reed-Muller codes
> 1. The zeroth order Reed-Muller codes $\mathcal R(0, m)$, for $m \geq 0$, are defined to be the repetitions codes $\{0, 1\}$ of length $2^m$.
> 2. For any $r \geq 2$, the $r$th order Reed-Muller codes $\mathcal R(r, m)$ are defined, for $m \geq r - 1$, recursively by $$\mathcal R(r, m + 1) = \begin{cases}\mathbb F_2^{2^r} &\text{ if } m = r - 1 \\ \{(u, u + v) : u \in \mathcal R(r, m), v \in \mathcal R(r - 1, m)\} &\text{ if } m > r - 1\end{cases}$$

> [!proposition]
> $\mathcal R(r, m)$ is a linear code with parameter $[2^m, \sum_{i = 0}^r \binom{m}{i}, 2^{m - r}]$

### First-order Reed-Muller codes