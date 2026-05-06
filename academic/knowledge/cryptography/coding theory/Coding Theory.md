
> [!remark] Goal 
> 1. Fast encoding of messages;
> 2. Easy transmission of encoded messages;
> 3. Fast decoding of received messages;
> 4. Maximum transfer of information per unit time;
> 5. Maximal detection or correction capability

## Communication Channel

> [!definition]
> Let $A = \{a_1, a_2, \dots, a_q\}$ be a set of size $q$, which we refer to as a **code alphabet** and whose elements are called **code symbols**.
> 1. A **q-ary word** of length $n$ over $A$ is a sequence $w = w_1 w_2 \cdots w_n$ with each $w_i \in A$ for all $i$. Equivalently, $w$ may also be regarded as the vector $(w_1, w_2, \dots, w_n)$.
> 2. A **q-ary block code** of length $n$ over $A$ is a nonempty set $C$ of q-ary words having the same length $n$.
> 3. An element of $C$ is called a **codeword** in $C$.
> 4. The number of codewords in $C$, denoted by $|C|$, is called the **size** of $C$,
> 5. The **(information) rate** of a code $C$ of length $n$ is defined to be $(\log_q |C|) / n$.
> 6. A code of length $n$ and size $M$ is called an $(n, M)$-code.

> [!definition] Communication Channel
> A **communication channel** consists of a **finite channel alphabet** $A = \{a_1, \dots, a_q\}$ as well as a set of **forward channel probabilites** $\mathcal P(a_j \text{ received} | a_i \text{ sent})$, satisfying $$\sum_{j = 1}^q \mathcal P(a_j \text{ received} | a_i \text{ sent}) = 1$$ for all $i$.

> [!definition] Memoryless
> A communication channel is said to be **memoryless** if the outcome of any one transmission is independent of the outcome of the previous transmissions; i.e., if $c = c_1 c_2 \cdots c_n$ and $x = x_1 x_2 \cdots x_n$ are words of length $n$, then $$\mathcal P(x \text{ received} | c \text{ sent}) = \prod \mathcal P(x_i \text{ received} | c_i \text{ sent})$$

> [!definition] $q$-ary symmetric channel
> A **$q$-ary symmetric channel** is a memoryless channel which has a channel alphabet of size $q$ such that
> 1. Each symbol transmitted has the same probability $p (< 1/2)$ of being received in error;
> 2. If a symbol is received in error, then each of the $q - 1$ possible errors is equally likely.

> [!example] Binary symmetric channel
> The **binary symmetric channel (BSC)** is a memoryless channel which has channel alphabet $\{0, 1\}$ and channel probabilities $$\begin{align}\mathcal P(1 \text{ received} | 0 \text{ sent}) &= \mathcal P(0 \text{ received} | 1 \text{ sent}) = p \\ \mathcal P(0 \text{ received} | 0 \text{ sent}) &= P(1 \text{ received} | 1 \text{ sent}) = 1 - p\end{align}$$
> The probability of a bit error in a BSC is $p$. This is called the **crossover probability** of the BSC.

## Decoding Rule

> [!definition] Decoding Rule
> In a communication channel with coding, only codewords are transmitted. Suppose that a word $w$ is received. If $w$ is a valid codeword, we may conclude that there is no error in the transmission. Otherwise, we know that some errors have occurred. In this case, we need a rule for finding the most likely codeword sent. Such a rule is known as a **decoding rule**.

### Maximum Likelihood Decoding

> [!definition] Maximum Likelihood Decoding
> Suppose that codewords from a code $C$ are being sent over a communication channel. If a word $x$ is received, we can compute the forward channel probabilities $$\mathcal P(x \text{ received} | c \text{ sent})$$ for all codewords $c \in C$. The **maximum likelihood decoding (MLD) rule** will conclude that $c_x$ is the most likely codeword transmitted if $c_x$ maximize the forward channel probabilities: $$\mathcal P(x \text{ received} | c_x \text{ sent}) = \max_{c \in C} \mathcal P(x \text{ received} | c \text{ sent}).$$ 
> The problem is there might be more than one $c_x$, we have two strategies:
> 1. **Complete maximum likelihood decoding (CMLD)**: Select one of them arbitrarily.
> 2. **Incomplete maximum likelihood decoding (IMLD)**: Request a retransmission.

### Nearest Neighbour/Minimum Distance Decoding

> [!definition] Nearest Neighbour/Minimum Distance Decoding
> Suppose that codewords from a code $C$ are being sent over a communication channel, if a word $x$ is received, the **nearest neighbour decoding rule** (or **minimum distance decoding rule**) will decode $x$ to $c_x$ if $d(x, c_x)$ is minimal among all the codewords in $C$, i.e, $$d(x, c_x) = \min_{c \in C} d(x, c)$$
> We can also define the complete and incomplete strategy just like the [[#Maximum Likelihood Decoding]] case as there might be more than one $x_c$.

> [!theorem]
> For a BSC with crossover probability $p < 1/2$, the maximum likelihood decoding rule is the same as the nearest neighbour decoding rule.

## Distance of a code

> [!definition] Minimum Distance
> For a code $C$ containing at least two words, the **(minimum) distance** of $C$, denoted by $d(C)$, is $$d(C) = \min\{d(x, y) : x, y \in C, x \neq y\}.$$

> [!definition] Parameters of the Code 
> A code of length $n$, size $M$ and distance $d$ referred to as an $(n, M, d)$-code. The numbers $n, M$ and $d$ are called the **parameters** of the code.

> [!definition] $u$-error-detecting
> Let $u$ be a positive integer. A code $C$ is **$u$-error-detecting** if, whenever a codeword incurs at least one but at most $u$ errors, the resulting word is not a code word. A code $C$ is **exactly $u$-error-detecting** if it is $u$-error detecting but not $(u + 1)$-error-detecting.

> [!theorem]
> A code $C$ is $u$-error-detecting if and only if $d(C) \geq u + 1$; i.e., a code with distance $d$ is an exactly $(d - 1)$-error-detecting.

> [!definition] $v$-error-correcting
> Let $v$ be a positive integer. A code $C$ is **$v$-error-correcting** if minimum distance decoding is able to correct $v$ or fewer errors, assuming that the incomplete decoding rule is used. A code $C$ is **exactly $v$-error-correcting** if it is $v$-error correcting but not $(v + 1)$-error correcting.

> [!theorem]
> A code $C$ is $v$-error-correcting if and only if $d(C) \geq 2v + 1$; i.e., a code with distance $d$ is an exactly $\lfloor (d - 1) / 2 \rfloor$-error-correcting code.

### Hamming Distance

> [!definition] Hamming Distance
> Let $x$ and $y$ be words of length $n$ over the alphabet $A$. The **(Hamming) distance** from $x$ to $y$, denoted by $d(x, y)$, is defined to be the number of places at which $x$ and $y$ differ. If $x = x_1 \cdots x_n$ and $y = y_1 \cdots y_n$, then $$d(x, y) = d(x_1, y_1) + \cdots + d(x_n, y_n),$$ where $x_i$ and $y_i$ are regarded as words of length $1$, and $$d(x_i, y_i) = \begin{cases}1 &\text{ if } x_i \neq y_i \\ 0 &\text{ if } x_i = y_i\end{cases}$$

> [!proposition]
> Let $x, y, z$ be words of length $n$ over $A$. Then we have
> 1. $0 \leq d(x, y) \leq n$,
> 2. $d(x, y) = 0$ if and only if $x = y$,
> 3. $d(x, y) = d(y, x)$
> 4. (Triangle inequality) $d(x, z) \leq d(x, y) + d(y, z)$.

## Weight of a Code

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

## Bounds in coding theory

### The Main Coding Theory Problem

> [!definition] Relative Minimum Distance
> For a $q$-ary code $C$ with parameters $(n, M, d)$, the **relative minimum distance** of $C$ is defined to be $\delta(C) = (d - 1) / n$

> [!definition] Optimal code
> For a given code alphabet $A$ of size $q$ (with $q > 1$) and given values of $n$ and $d$, let $A_q(n, d)$ denote the largest possible size $M$ for which there exists an $(n, M, d)$-code over $A$. Thus, $$A_q(n, d) = \max \{M : \text{there exists an } (n, M, d)\text{-code over } A\}.$$ Any $(n, M, d)$-code $C$ that has the maximum size, that is, for which $M = A_q(n, d)$, is called an **optimal code**.

> [!definition] Main Coding Theory Problem
> The problem of determining the values of $A_q(n, d)$ is sometimes known as the **main coding theory problem**.

> [!definition] Linear Codes Version
> For a given prime power $q$ and given values of $n$ and $d$, let $B_q(n, d)$ denote the largest possible size $q^k$ for which there exists an $[n, k, d]$-code over $\mathbb F_q$. Thus, $$B_q(n, d) = \max\{q^k : \text{there exists an } [n, k, d]\text{-code over } \mathbb F_q\}.$$

> [!theorem]
> Let $q \geq 2$ be a prime power. Then
> 1. $B_q(n, d) \leq A_q(n, d) \leq q^n$ for all $1 \leq d \leq n$;
> 2. $B_q(n, 1) = A_q(n, 1) = q^n$;
> 3. $B_q(n, n) = A_q(n, n) = q$.

> [!definition] Extended Code
> For any code $C$ over $\mathbb F_q$, the **extended code** of $C$, denoted by $\overline{C}$, is defined to be $$\overline{C} = \{(c_1, \dots, c_n, - \sum_{i = 1}^n c_i) : (c_1, \dots, c_n) \in C\}.$$ When $q = 2$, the extra coordinate is called the **parity-check** coordinate.

> [!theorem]
> If $C$ is an $(n, M, d)$-code over $\mathbb F_q$, then $\overline{C}$ is an $(n + 1, M, d')$-code over $\mathbb F_q$, with $d \leq d' \leq d + 1$. If $C$ is linear, then so is $\overline{C}$. Moreover, when $C$ is linear, $$\begin{pmatrix}H & 0 \\ \textbf{1} & 1\end{pmatrix}$$ is a parity-check matrix of $\overline{C}$ if $H$ is a parity-check matrix of $C$.

> [!theorem]
> Suppose $d$ is odd.
> 1. Then a binary $(n, M, d)$-code exists if and only if a binary $(n + 1, M, d + 1)$-code exists. Therefore, if $d$ is odd, $A_2(n + 1, d + 1) = A_2(n, d)$.
> 2. Similarly, a binary $[n, k, d]$-linear code exists if and only if a binary $[n + 1, k, d + 1]$-linear code exists, so $B_2(n + 1, d + 1) = B_2(n, d)$.

### Lower Bounds

> [!definition] Sphere
> Let $A$ be an alphabet of size $q$, where $q > 1$. For any vector $u \in A^n$ and any integer $r \geq 0$, the **sphere** of radius $r$ and center $u$, denoted $S_A(u, r)$, is the set $\{v \in A^n : d(u, v) \leq r\}$.

> [!definition] 
> For a given integer $q > 1$, a positive integer $n$ and an integer $r \geq 0$, define $V_q^n(r)$ to be $$V_q^n(r) = \begin{cases}\binom{n}{0} + \binom{n}{1} (q - 1) + \cdots + \binom{n}{r} (q - 1)^r &\text{ if } 0 \leq r \leq n\\ q^n & \text{ if } n \leq r\end{cases}$$

> [!lemma]
> For all integers $r \geq 0$, a sphere of radius $r$ in $A^n$ contains exactly $V_q^n(r)$ vectors, where $A$ is an alphabet of size $q > 1$.

> [!theorem] Sphere-covering bound
> For an integer $q > 1$ and integers $n, d$ such that $1 \leq d \leq n$, we have $$\frac{q^n}{V_q^n(d - 1)} = \frac{q^n}{\sum_{i = 0}^{d - 1} \binom{n}{i} (q - 1)^i} \leq A_q(n, d)$$

> [!theorem] Gilbert-Varshamov Bound
> Let $n, k$ and $d$ be integers satisfying $2 \leq d \leq n$ and $1 \leq k \leq n$. If $$\sum_{i = 0}^{d - 2} \binom{n - 1}{i} (q - 1)^i < q^{n - k},$$ then there exists an $[n, k]$ linear code over $\mathbb F_q$ with minimum distance at least $d$.

> [!corollary]
> For a prime power $q > 1$ and integers $n, d$ such that $2 \leq d \leq n$, we have $$B_q(n, d) \geq q^{n - \lceil \log_q (V_q^{n - 1}(d - 2) + 1) \rceil} \geq \frac{q^{n - 1}}{V_q^{n - 1}(d - 2)}$$

### Hamming Bound and Perfect Codes



### Reed-Muller Codes

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



### Quasi-Cyclic Codes

> [!definition] Quasi-Cyclic Codes
> View a vector $c = (c_0, \dots, c_{s - 1})$ of $\mathbb F_2^{sn}$ as $s$ successive blocks ($n$-tuples). An $[sn, k, d]$ linear code $C$ is Quasi-Cyclic (QC) of index $s$ if, for any $c = (c_0, \dots, c_{s - 1}) \in C$, the vector obtained after applying a simultaneous circular shift to every block $c_0, \dots, c_{s - 1}$ is also a codeword. More formally, by considering each block $c_i$ as a polynomial in $\mathcal R = \mathbb F_2[X] / (X^n - 1)$, the code $C$ is QC of index $s$ if for any $c = (c_0, \dots, c_{s - 1}) \in C$ it holds that $(X \cdot c_0, \dots, X \cdot c_{s - 1}) \in C$.

### Systematic Quasi-Cyclic Codes

> [!definition] Systematic Quasi-Cyclic Codes
> A systematic Quasi-Cyclic $[sn, n]$ code of index $s$ (number of blocks) and rate $1/s$ is a quasi-cyclic code with an $(s - 1)n \times sn$ parity-check matrix of the form: $$H = \begin{bmatrix}
> I_n & 0   & \cdots & 0   & A_0    \\
> 0   & I_n &        &     & A_1    \\
>     &     & \ddots &     & \vdots \\
> 0   &     & \cdots & I_n & A_{s - 2} \\    
> \end{bmatrix}$$ where $A_0, \dots, A_{s - 2}$ are circulant $n \times n$ matrices.

### Concatenated Codes

> [!definition] Concatenated Codes
> A concatenated code consists of an external code $[n_e, k_e, d_e]$ over $\mathbb F_q$ and an internal code $[n_i, k_i, d_i]$ over $\mathbb F_2$, with $q = 2^{k_i}$. We use a bijection between elements of $\mathbb F_q$ and the words of the internal code to obtain a transformation: $$\mathbb F_q^{n_e} \rightarrow \mathbb F_2^N$$ where $N = n_e n_i$. The external code is thus transformed into a binary code of parameters $[N = n_e n_i, K = k_e k_i, D \geq d_e d_i]$.

## Error Correcting Code


> [!definition] Levenshtein Distance

> [!definition] Ulam Distance

> [!definition] Cayley Distance

> [!definition] Kendall tau Distance

> [!definition] Generalized Kendall tau Distance
> 

> [!definition] Generalized Cayley Distance

> [!example] Permutation Code
> 