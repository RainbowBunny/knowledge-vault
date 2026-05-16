
| Term                                          | Reference                                                        |                  |
| --------------------------------------------- | ---------------------------------------------------------------- | ---------------- |
| Attack Game 7.1 (Universal Hash Function)     | [[#Secure Universal Hash Function\|secure UHF]]                  | $\text{UHFadv}$  |
| Attack Game 7.2 (Multi-query UHF)             | [[#Multi-query Universal Hash Function\|secure multi-query UHF]] | $\text{MUHFadv}$ |
| Attack Game 7.3 (Difference Unpredictability) | [[#Difference Unpredictability\|DUF]]                            | $\text{DUFadv}$  |
| Attack Game 8.1 (Collision Resistance)        | [[#Collision Resistance\|collision finder]]                      | $\text{CRadv}$   |

## Basic Definition

> [!definition] Hash Function
> A **(keyless) hash function** takes as input an arbitrarily long document $D$ in some large set $\mathcal M$ and returns a short bit string $H$ in $\mathcal T$ called **message digests** (or just digests). The primary properties that a has function $\text{Hash}$ should possess are as follows:
> - Computation of $\text{Hash}(D)$ should be fast and easy, e.g., linear time.
> - Inversion of $\text{Hash}$ should be difficult, e.g., exponential time. More precisely, given a hash value $H$, it should be difficult to find any document $D$ such that $\text{Hash}(D) = H$.
> - For many applications it is also important that $\text{Hash}$ be **collision resistant**. This means that it should be hard to find two different documents $D_1$ and $D_2$ whose hash values $\text{Hash}(D_1)$ and $\text{Hash}(D_2)$ are the same.

> [!algorithm] Hash Function (Mathematical Detail)
> A **(keyless) hash function** is an efficient algorithm $H$, along with two families of spaces with system parameterization $P$: $$M = \{\mathcal M_{\lambda, \Lambda}\}, T = \{\mathcal T_{\lambda, \Lambda}\}_{\lambda, \Lambda},$$ such that
> 1. $M$, and $T$ are efficiently recognizable.
> 2. Algorithm $H$ is an efficient deterministic algorithm that on input $\lambda, \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda))$, and $m \in \mathcal M_{\lambda, \Lambda}$, outputs an element of $\mathcal T_{\lambda, \Lambda}$.

### Collision Resistance

> [!algorithm] Collision Resistance
> For a given hash function $H$ defined over $(\mathcal M, \mathcal T)$ and adversary $\mathcal A$, the adversary takes no input and outputs two messages $m_0$ and $m_1$ in $\mathcal M$.
> We say that $\mathcal A$ wins the game if the pair $m_0, m_1$ is a collision for $H$, namely $m_0 \neq m_1$ and $H(m_0) = H(m_1)$. We define $\mathcal A$'s advantage with respect to $H$, denoted $\text{CRadv}[\mathcal A, H]$, as the probability that $\mathcal A$ wins the game. Adversary $\mathcal A$ is called a **collision finder**.

> [!definition] Collision Resistant
> We say that a hash function $H$ over $(\mathcal M, \mathcal T)$ is **collision resistant** if for all efficient adversaries $\mathcal A$, the quantity $\text{CRadv}[\mathcal A, H]$ is negligible.

## Compression Function

### Simple Inefficient Compression Function

> [!algorithm] Inefficient Compression Function
> Let $p$ be a large prime such that $q = (p - 1) / 2$ is also prime. Let $x$ and $y$ be suitably chosen integers in the range $[1, q]$. Consider the following simple compression function that takes as input two integers in $[1, q]$ and outputs an integer in $[1, q]$: $$H(a, b) = abs(x^a y^b \mod p), \quad \text{where} \quad \text{abs}(z) = \begin{cases}z&\text{if } z \leq q, \\ p - z &\text{if }z > q.\end{cases}$$

## Universal Hash Functions (UHFs)

> [!definition] Keyed Hash Functions
> A **keyed hash function** $H$ is a deterministic algorithm that takes two inputs, a **key** $k$ and a **message** $m$; its output $t = H(k, x)$ is called a **digest**. As usual, there are associated spaces: the key space $\mathcal K$, in which $k$ lies, a message space $\mathcal M$, in which $m$ lies, and the digest space $\mathcal T$, in which $t$ lies. We say that the hash function $H$ is defined over $(\mathcal K, \mathcal M, \mathcal T)$.

> [!definition] Collision Under Key
> We say that two messages $m_0, m_1 \in \mathcal M$ forms a **collision for $H$ under key $k \in \mathcal K$ if** $$H(k, m_0) = H(k, m_1) \quad \text{and} \quad m_0 \neq m_1.$$

> [!algorithm] Keyed Hash Functions (Mathematical Details)
> A **keyed hash function** is an efficient algorithm $H$, along with three families of spaces with system parameterization $P$:
> $$K = \{\mathcal K_{\lambda, \Lambda}\}_{\lambda, \Lambda}, M = \{\mathcal M_{\lambda, \Lambda}\}_{\lambda, \Lambda}, T = \{\mathcal T_{\lambda, \Lambda}\}_{\lambda, \Lambda}$$ such that
> 1. $K, M$, and $T$ are efficiently recognizable.
> 2. $K$ and $T$ are efficiently sampleable.
> 3. Algorithm $H$ is an efficient deterministic algorithm that on input $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), k \in \mathcal K_{\lambda, \Lambda}$, and $m \in \mathcal M_{\lambda, \Lambda}$, outputs an element of $\mathcal T_{\lambda, \Lambda}$.

> [!lemma] Leftover Hash Lemma
> Let $\mathcal H = \{h: \mathcal X \rightarrow \mathcal Y\}$ be a 2-universal hash function family. Then for any random variable $X \in \mathcal X$, for $\epsilon > 0$ such that $\log |\mathcal Y| \leq H_{\infty}(X) - 2 \log (1 / \varepsilon)$, the distributions $$(h, h(X)) \quad \text{and} \quad (h, \mathcal U(\mathcal Y))$$ are within statistical distance $\varepsilon$.
> Further, the family $\{A \in \mathbb Z_q^{n \times m} : r \rightarrow Ar\}$ is 2-universal for any prime $q$.

### Secure Universal Hash Function

> [!algorithm] Universal Hash Function
> For a keyed hash function $H$ defined over $(\mathcal K, \mathcal M, \mathcal T)$, and a given adversary $\mathcal A$, the attack game runs as follows:
> - The challenger picks a random $k \xleftarrow{R} \mathcal K$ and keeps $k$ to itself.
> - $\mathcal A$ outputs two distinct messages $m_0, m_1 \in \mathcal M$.
> 
> We say that $\mathcal A$ wins the above game if $H(k, m_0) = H(k, m_1)$. We define $\mathcal A$'s advantage with respect to $H$, denoted $\text{UHFadv}[\mathcal A, H]$, as the probability that $\mathcal A$ wins the game.

> [!proposition] Secure Universal Hash Function
> Let $H$ be a keyed hash function defined over $(\mathcal K, \mathcal M, \mathcal T)$,
> - We say that $H$ is an $\epsilon$-**bounded universal hash function**, or $\epsilon$-**UHF**, if $\text{UHFadv}[\mathcal A, H] \leq \epsilon$ for all adversaries $\mathcal A$ (even inefficient ones).
> - We say that $H$ is a **statistical UHF** if it is an $\epsilon$-UHF for some negligible $\epsilon$.
> - We say that $H$ is a **computational UHF** if $\text{UHFadv}[\mathcal A, H]$ is negligible for all efficient adversaries $\mathcal A$.

### Multi-query Universal Hash Function

> [!algorithm] Multi-query UHF
> For a keyed hash function $H$ over $(\mathcal K, \mathcal M, \mathcal T)$, and a given adversary $\mathcal A$, the attack game runs as follows.
> - The challenger picks a random $k \xleftarrow{R} \mathcal K$ and keeps $k$ to itself.
> - $\mathcal A$ outputs distinct messages $m_1, \dots, m_s \in \mathcal M$.
> 
> We say that $\mathcal A$ wins the above game if there are indices $i \neq j$ such that $H(k, m_i) = H(k, m_j)$. We define $\mathcal A$'s advantage with respect to $H$, denoted $\text{MUHFadv}[\mathcal A, H]$, as the probability that $\mathcal A$ wins the game. We call $\mathcal A$ a $Q$**-query UHF adversary** if it always outputs a list of size $s \leq Q$.

> [!definition] Multi-query UHF
> We say that a hash function $H$ over $(\mathcal K, \mathcal M, \mathcal T)$ is a **multi-query UHF** if for all efficient adversaries $\mathcal A$, the quantity $\text{MUHFadv}[\mathcal A, H]$ is negligible.

> [!lemma]
> If $H$ is a computational UHF, then it is also a multi-query UHF.
> 
> In particular, for every $Q$-query UHF adversary $\mathcal A$, there exists a UHF adversary $\mathcal B$, which is an elementary wrapper around $\mathcal A$, such that $$\text{MUHFadv}[\mathcal A, H] \leq (Q^2/2) \cdot \text{UHFadv}[\mathcal B, H].$$

### Difference Unpredictability

> [!algorithm] Difference Unpredictability
> For a keyed hash function $H$ defined over $(\mathcal K, \mathcal M, \mathcal T)$, where $\mathcal T = \mathbb Z_N$, and a given adversary $\mathcal A$, the attack game runs as follows
> - The challenger picks a random $k \xleftarrow{R} \mathcal K$ and keeps $k$ to itself.
> - $\mathcal A$ outputs two distinct messages $m_0, m_1 \in \mathcal M$ and a value $\delta \in \mathcal T$.
> 
> We say that $\mathcal A$ wins the game if $H(k, m_1) - H(k, m_0) = \delta$. We define $\mathcal A$'s advantage with respect to $H$, denoted $\text{DUFadv}[\mathcal A, H]$, as the probability that $\mathcal A$ wins the game.

> [!definition] Bounded Difference Unpredictable Function
> Let $H$ be a keyed hash function defined over $(\mathcal K, \mathcal M, \mathcal T)$, 
> - We say that $H$ is an $\epsilon$**-bounded difference unpredictable function**, or $\epsilon$-**DUF**, if $\text{DUFadv}[\mathcal A, H] \leq \epsilon$ for all adversaries $\mathcal A$ (even inefficient ones).
> - We say that $H$ is a **satistical DUF** if it is an $\epsilon$-DUF for some negligible $\epsilon$.
> - We say that $H$ is a **computational DUF** if $\text{DUFadv}[\mathcal A, H]$ is negligible for all efficient adversaries $\mathcal A$.

> [!remark] An alternate characterization of $\epsilon$-DUF property
> For every pair of distinct messages $m_0, m_1 \in \mathcal M$, for every $\delta \in \mathcal T$, the following inequality holds: $P[H(k, m_1) - H(k, m_0) = \delta] \leq \epsilon$. Here, the probability is over the random choice of $k \in \mathcal K$.

## Collision Resistance Construction

### Merkle-Damgard Paradigm

> [!algorithm] Merkle-Damgard Function
> Let $h: \mathcal X \times \mathcal Y \rightarrow \mathcal X$ be a hash function. We shall assume that $\mathcal Y$ is of the form $\{0, 1\}^\ell$ for some $\ell$. The **Merkle-Damgard function derived from $h$**, denoted $H_{MD}$, is a hash function defined over $(\{0, 1\}^{\leq L}, \mathcal X)$ that works as follows:
> 
> ---
> **Input**: $M \in \{0, 1\}^{\leq L}$
> **Output**: A tag in $\mathcal X$
> 1. $\hat{M} \leftarrow M || PB$
> 2. Partition $\hat{M}$ into consecutive $\ell$-bit blocks so that $$\hat{M} = m_1 || m_2 || \dots || m_s \quad \text{where} \quad m_1, \dots, m_s \in \{0, 1\}^\ell$$
> 3. $t_0 \leftarrow IV \in \mathcal X$
> 4. For $i = 1$ to $s$ do: $t_i \leftarrow h(t_{i - 1}, m_i)$
> 5. Output $t_s$.

> [!definition] Important Term
> - The hash function $h$ is called the **compression function** of $H$.
> - The constant IV is called the **initial value** and is fixed to some pre-specified value.
> - The variables $m_1, \dots, m_s$ are called **message blocks**.
> - The variables $t_0, t_1, \dots, t_s \in \mathcal X$ are called **chaining variables**.
> - The string PB is called the **padding blocks**. It is appended to the message to ensure that the message length is a multiple of $\ell$ bits.

> [!theorem]
> Let $L$ be a poly-bounded length parameter and let $h$ be a collision resistant hash function defined over $(\mathcal X \times \mathcal Y, \mathcal X)$. Then the Merkle-Damgard hash function $H_{MD}$ derived from $h$, defined over $(\{0, 1\}^{\leq L}, \mathcal X)$, is collision resistant.
> 
> In particular, for every [[#Collision Resistance|collision finder]] $\mathcal A$ attacking $H_{MD}$, there exists a [[#Collision Resistance|collision finder]] $\mathcal B$ attacking $h$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{CRadv}[\mathcal A, H_{MD}] = \text{CRadv}[\mathcal B, h].$$

### Davies-Meyer Construction

> [!algorithm] Davies-Meyer Compression Function
> Let $\mathcal E = (E, D)$ be a block cipher over $(\mathcal K, \mathcal X)$ where $\mathcal X = \{0, 1\}^n$. The **Davies-Meyer compression function derived from $E$** maps inputs in $\mathcal X \times \mathcal K$ to outputs in $\mathcal X$. The function is defined as follows: $$h_{DM}(x, y) = E(y, x) \oplus x.$$
> In symbols, $h_{DM}$ is defined over $(\mathcal X \times \mathcal K, \mathcal X)$.

> [!remark] Davies-Meyer Variant
> Secure variants:
> - Matyas-Meyer-Oseas: $h_1(x, y) = E(x, y) \oplus y$
> - Miyaguchi-Preneel: $h_2(x, y) = E(x, y) \oplus y \oplus x$
> - Or even: $h_3(x, y) = E(x \oplus y, y) \oplus y$
> 
> Insecure variants:
> - $h_4(x, y) = E(y, x) \oplus y$
> - $h_5(x, y) = E(x, x \oplus y) \oplus x$

> [!remark]
> The $\oplus$ operation can be replaced by the $\boxplus$ operation (byte adding modulo $2^{32}$).

> [!theorem] Davies-Meyer
> Let $h_{DM}$ be the Davies-Meyer hash function derived from a block cipher $\mathcal E = (E, D)$ defined over $(\mathcal K, \mathcal X)$, where $|\mathcal X|$ is large. Then $h_{DM}$ is collision resistant in the ideal cipher model.
> 
> In particular, every [[#Collision Resistance|collision finder]] adversary $\mathcal A$ that issues at most $q$ ideal-cipher queries will satisfy $$\text{CR}^{ic}\text{adv}[\mathcal A, h_{DM}] \leq (q + 1)(q + 2)/|\mathcal X|.$$

### The Sponge Construction

> [!algorithm] Sponge Construction
> - $\pi: \{0, 1\}^n \rightarrow \{0, 1\}^n$, permutation.
> - $r$: **rate** of the sponger, larger rate values lead to faster evaluation.
> - $c$: **capacity** of the sponger, larger capacity values lead to better security bounds.
> 
> ---
> **Input**: Message $M \in \{0, 1\}^{\leq L}$ and desired output length $v > 0$
> **Output**: A tag $h \in \{0, 1\}^v$
> 1. **Absorbing Phase**: 
> 	1. Pad $M$ and break into $r$-bit blocks $m_1, \dots, m_s \in \{0, 1\}^r$
> 	2. $h \leftarrow 0^n$
> 	3. For $i \leftarrow 1$ to $s$ do
> 		- $m_i' \leftarrow m_i || 0^c \in \{0, 1\}^n$
> 		- $h \leftarrow \pi(h \oplus m_i')$
> 2. **Squeezing State**:
> 	1. $z_1 \leftarrow h[0 \dots r - 1]$
> 	2. For $i \leftarrow 2$ to $\lfloor v/r \rfloor$ do
> 		- $h \leftarrow \pi(h)$
> 		- $z_i \leftarrow h[0 \dots r - 1]$
> 3. Output $(z_1 || \dots || z_{\lfloor v/r \rfloor})[0 \dots v - 1]$.

> [!theorem]
> Let $H$ be the hash function obtained from a permutation $\pi: \{0, 1\}^n \rightarrow \{0, 1\}^n$, with capacity $c$, rate $r$ (so $n = r + c$), and output length $v \leq r$. In the ideal permutation model, where $\pi$ is modeled as a random permutation $\Pi$, the hash function $H$ is collision resistant, assuming $2^v$ and $2^c$ are super-poly.
> 
> In particular, for every [[#Collision Resistance|collision finder]] adversary $\mathcal A$, if the number of ideal-permutation queries plus the number of $r$-bit blocks in the output messages of $\mathcal A$ is bounded by $q$, then $$\text{CR}^{ic}\text{adv}[\mathcal A, H] \leq \frac{q(q - 1)}{2^v} + \frac{q(q + 1)}{2^c}$$

## UHF Construction

### Using Polynomials

> [!algorithm] Polynomial UHF
> Let $\ell$ be a (poly-bounded) length parameter and let $p$ be a prime. We define a hash function $H_{poly}$ that hashes a message $m \in \mathbb Z_p^{\leq \ell}$ to a single element $t \in \mathbb Z_p$. The key space is $\mathcal K = \mathbb Z_p$.
> Let $m$ be a message, so $m = (a_1, a_2, \dots, a_v) \in \mathbb Z_p^{\leq \ell}$ for some $0 \leq v \leq \ell$. Let $k \in \mathbb Z_p$ be a key. The hash function $H_{poly}(k, m)$ is defined as follows:
> $$H_{poly}(k, (a_1, \dots, a_v)) = k^v + a_1 k^{v - 1} + a_2 k^{v - 2} + a_{v - 1} k + a_v \in \mathbb Z_p$$

> [!lemma]
> The function $H_{poly}$ over $(\mathbb Z_p, (\mathbb Z_p)^{\leq \ell}, \mathbb Z_p)$ is an $(\ell/p)$-UHF.

> [!algorithm] Polynomial DUF
> $H_{xpoly}(k, m) = k \cdot H_{poly}(k, m)$. 

> [!lemma] 
> The function $H_{xpoly}$ over $(\mathbb Z_p, (\mathbb Z_p)^{\leq \ell}, \mathbb Z_p)$ is an $(\ell + 1)/p$-DUF.

> [!remark]
> We can modify $H_{xpoly}$ to operate on $n$-bit blocks by doing all arithmetic in the finite field $GF(2^n)$ instead of $\mathbb Z_p$.

### Using Prefix-free PRF

> [!theorem]
> Let PF be an [[Pseudorandom Functions#Extendable PRF|extendable]] and prefix-free secure PRF defined over $(\mathcal K, \mathcal X^{\leq \ell + 1}, \mathcal Y)$ where $|\mathcal Y|$ is super-poly and $|\mathcal X| > 1$. Then PF is a computational UHF defined over $(\mathcal K, \mathcal X^{\leq \ell}, \mathcal Y).$
> 
> In particular, for every [[#Secure Universal Hash Function|secure UHF]] adversary $\mathcal A$ with respect to $PF$, there exists a [[Pseudorandom Functions#Secure Prefix-free PRF|secure prefix-free PRF]] adversary $\mathcal B$, which is an elementary wrapper around $\mathcal A$, such that $$\text{UHFadv}[\mathcal A, PF] \leq \text{PRF}^{pf}\text{adv}[\mathcal B, PF] + \frac{1}{|\mathcal Y|}.$$
> Moreover, $\mathcal B$ makes only two queries to $PF$.

> [!theorem]
> Let PF be an [[Pseudorandom Functions#Extendable PRF|extendable]] and prefix-free secure PRF defined over $(\mathcal K, \mathcal X^{\leq \ell + 1}, \mathcal Y)$, where $|\mathcal X|$ and $|\mathcal Y|$ are super-poly and $\ell$ is poly-bounded. Then PF is a multi-query UHF defined over $(\mathcal K, \mathcal X^{\leq \ell}, \mathcal Y)$.
> 
> In particular, if $|\mathcal X| > \ell Q$, then for every $Q$-query [[#Multi-query Universal Hash Function|secure multi-query UHF]] adversary $\mathcal A$, there exists a $Q$-query [[#Secure Prefix-free PRF|secure prefix-free PRF]] adversary $\mathcal B$, which is an elementary wrapper around $\mathcal A$, such that $$\text{MUHFadv}[\mathcal A, PF] \leq \text{PRF}^{pf}\text{adv}[\mathcal B, PF] + \frac{Q^2}{2|\mathcal Y|}.$$

> [!corollary]
> Let $F$ be a [[Pseudorandom Functions#PRF Security|secure PRF]] defined over $(\mathcal K, \mathcal X, \mathcal Y)$. Then the [[Pseudorandom Functions#CBC Construction|CBC construction]] $F_{CBC}$ (assuming $\mathcal Y = \mathcal X$ is super-poly size) and the [[Pseudorandom Functions#Cascade Construction|cascade construction]] $F^*$ (assuming $\mathcal Y = \mathcal K$), which take inputs in $\mathcal X^{\leq \ell}$ for poly-bounded $\ell$, are computational UHFs.
> 
> In particular, for every $Q$-query [[#Multi-query Universal Hash Function|secure multi-query UHF]] adversary $\mathcal A$, there exist [[Pseudorandom Functions#Secure Prefix-free PRF|secure prefix-free PRF]] adversaries $\mathcal B_1, \mathcal B_2$, which are elementary wrappers around $\mathcal A$, such that $$\begin{align}\text{MUHFadv}[\mathcal A, F_{CBC}] &\leq \text{PRF}^{pf}\text{adv}[\mathcal B_1, F] + \frac{Q^2(\ell + 1)^2 + Q^2}{2|\mathcal Y|} \\ \text{MUHFadv}[\mathcal A, F^*] &\leq Q(\ell + 1) \cdot \text{PRF}^{pf}\text{adv}[\mathcal B_2, F] + \frac{Q^2}{2|\mathcal Y|}\end{align}$$

### Parallel UHF from a small PRF

> [!theorem]
> Let $F$ be a [[Pseudorandom Functions#PRF Security|secure PRF]] and assume $|\mathcal Y|$ is super-poly. Then $F^\oplus$ is a computational UHF.
> 
> In particular, for every [[#Secure Universal Hash Function|secure UHF]] adversary $\mathcal A$, there exists a [[Pseudorandom Functions#PRF Security|secure PRF]] adversary $\mathcal B$, which is an elementary wrapper around $\mathcal A$, such that $$\text{UHFadv}[\mathcal A, F^\oplus] \leq \text{PRFadv}[\mathcal B, F] + \frac{1}{|\mathcal Y|}.$$

## Case Study

### SHA256

> [!algorithm] SHA256
> For $x, y, z$ in $\{0, 1\}^{32}$, define:
> $$\begin{align}
> \text{SHR}^n(x) &= (x >> n) \\
> \text{ROTR}^n(x) &= (x >> n) \lor (x << 32 - n) \\
> \text{Ch}(x, y, z) &= (x \land y) \oplus (\not x \land z) \\
> \text{Maj}(x, y, z) &= (x \land y) \oplus (x \land z) \oplus (y \land z) \\
> \Sigma_0(x) &= \text{ROTR}^2(x) \oplus \text{ROTR}^{13}(x) \oplus \text{ROTR}^{22}(x) \\
> \Sigma_1(x) &= \text{ROTR}^6(x) \oplus \text{ROTR}^{11}(x) \oplus \text{ROTR}^{25}(x) \\
> \sigma_0(x) &= \text{ROTR}^7(x) \oplus \text{ROTR}^{18}(x) \oplus \text{SHR}^3(x) \\
> \sigma_1(x) &= \text{ROTR}^{17}(x) \oplus \text{ROTR}^{19}(x) \oplus \text{SHR}^{10}(x) 
> \end{align}$$
> 
> ---
> SHA256
> **Input**: plaintext $t = t_0 || \dots || t_7 \in \{0, 1\}^{256}$ and key $k = k_0 || k_1 \dots || k_{15} \in \{0, 1\}^{512}$
> **Output**: ciphertext in $\{0, 1\}^{256}$.
> 1. **Key setup**: Construct 64 round keys $W_0, \dots, W_{63} \in \{0, 1\}^{32}$; $$\begin{cases}\text{for } i = 0, 1, \dots, 15 &\text{set } W_i \leftarrow k_i, \\ \text{for } i = 16, 17, \dots, 63 &\text{set } W_i \leftarrow \sigma_1(W_{i - 2}) + W_{i - 7} + \sigma_0(W_{i - 15}) + W_{i - 16}\end{cases}$$
> 2. **64 Rounds**:
> $(a_0, b_0, c_0, d_0, e_0, f_0, g_0, h_0) \leftarrow (t_0, t_1, t_2, t_3, t_4, t_5, t_6, t_7)$
> For $i = 0$ to $63$ do:
> 	- $T_1 \leftarrow h_i + \Sigma_1(e_i) + \text{Ch}(e_i, f_i, g_i) + K_i + W_i$
> 	- $T_2 \leftarrow \Sigma_0(a_i) + \text{Maj}(a_i, b_i, c_i)$
> 	- $(a_{i + 1}, b_{i + 1}, c_{i + 1}, d_{i + 1}, e_{i + 1}, f_{i + 1}, g_{i + 1}, h_{i + 1}) \leftarrow (T_1 + T_2, a_i, b_i, c_i, d_i, e_i, f_i, g_i)$
> 3. **Output**: $a_{64} || b_{64} || c_{64} || d_{64} || e_{64} || f_{64} || g_{64} || h_{64} \in \{0, 1\}^{256}$.   

### SHA3

### MD5

> [!remark]
> MD5 suffers from a **Chosen Prefix Collision**: 
> $$\text{MD5}(A) = \text{MD5}(B) \rightarrow \text{MD5}(A + S) = \text{MD5}(S)$$
> Example of one collisions:
> ```python
> block1 = bytes.fromhex("d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70")
block2 = bytes.fromhex("d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70")
> ```
> Todo: [https://github.com/corkami/collisions](https://github.com/corkami/collisions)

