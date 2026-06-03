## CPA Secure Cipher Construction

### A Generic Hybrid Construction

> [!algorithm] Generic Hybrid Construction
> Let $\mathcal E = (E, D)$ be a cipher, defined over $(\mathcal K, \mathcal M, \mathcal C)$. Let $F$ be a PRF defined over $(\mathcal K', \mathcal X, \mathcal K)$; that is, the output space of $F$ should be equal to the key space of $\mathcal E$. We define a new cipher $\mathcal E' = (E', D')$, defined over $(\mathcal K', \mathcal M, \mathcal X \times \mathcal C)$, as follows:
> - For $k' \in \mathcal K'$ and $m \in \mathcal M$, we define:
> $$E'(k', m) = x \xleftarrow{R} \mathcal X, k \leftarrow F(k', x), c \xleftarrow{R} E(k, m), \text{output } (x, c);$$
> - For $k' \in \mathcal K'$ and $c' = (x, c) \in \mathcal X \times \mathcal C$, we define
> $$D'(k', c') = k \leftarrow F(k', x), m \leftarrow D(k, c), \text{output } m.$$

> [!theorem]
> If $F$ is a secure PRF, $\mathcal E$ is a semantically secure cipher, and $N = |\mathcal X|$ is super-poly, then the cipher $\mathcal E'$ is CPA secure.
> 
> In particular, for every [[#Chosen Plaintext Attack Security|CPA security]] adversary $\mathcal A$ that attacks $\mathcal E'$ which makes at most $Q$ queries to its challenger, there exists a [[Pseudo Random Function#PRF Security|secure PRF]] adversary $\mathcal B_F$ that attacks $F$ and an [[#Semantic Security|semantic security]] adversary $\mathcal B_{\mathcal E}$ that attacks $\mathcal E$, where both $\mathcal B_F$ and $\mathcal B_{\mathcal E}$ are elementary wrappers around $\mathcal A$, such that $$\text{CPAadv}[\mathcal A, \mathcal E'] \leq \frac{Q^2}{N} + 2 \cdot \text{PRFadv}[\mathcal B_F, F] + Q \cdot \text{SSadv}[\mathcal B_{\mathcal E}, \mathcal E].$$

### Randomized Counter Mode

> [!algorithm] Randomized Counter Mode
> Suppose $F$ is a PRF defined over $(\mathcal K, \mathcal X, \mathcal Y)$. We shall assume that $\mathcal X = \{0, \dots, N - 1\}$, and that $\mathcal Y = \{0, 1\}^n$.
> For any poly-bounded $\ell \geq 1$, we define a cipher $\mathcal E = (E, D)$, with key space $\mathcal K$, message space $\mathcal Y^{\leq \ell}$, and ciphertext space $\mathcal X \times \mathcal Y^{\leq \ell}$, as follows:
> - For $k \in \mathcal K$ and $m \in \mathcal Y^{\leq \ell}$, with $v = |m|$, we define
> $E(k, m)$:
> 1. $x \xleftarrow{R} \mathcal X$
> 2. Compute $c \in \mathcal Y^v$ as follows:
> 	for $j \leftarrow 0$ to $v - 1$ do $c[j] \leftarrow F(k, x + j \mod N) \oplus m[j]$
> 3. Output $(x, c)$;
> - For $k \in \mathcal K$ and $c' = (x, c) \in \mathcal X \times \mathcal Y^{\leq \ell}$, with $v = |c|$, we define
> $D(k, c')$
> 1. Compute $m \in \mathcal Y^v$ as follows:
> 	for $j \leftarrow 0$ to $v - 1$ do $m[j] \leftarrow F(k, x + j \mod N) \oplus c[j]$
> 2. Output $m$.

> [!remark]
> The $x$ component of the ciphertext is typically called an **initial value**, or **IV** for short.

> [!theorem]
> If $F$ is a secure PRF and $N$ is super-poly, then for any poly-bounded $\ell \geq 1$, the cipher $\mathcal E$ above is a CPA secure cipher.
> In particular, for every [[#Chosen Plaintext Attack Security|CPA security]] adversary $\mathcal A$ that attacks $\mathcal E$, and which makes at most $Q$ queries to its challenger, there exists a [[Pseudo Random Function#PRF Security|secure PRF]] adversary $\mathcal B$ that attacks $F$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{CPAadv}[\mathcal A, \mathcal E] \leq \frac{2Q^2 \ell}{N} + 2 \cdot \text{PRFadv}[\mathcal B, F].$$

### Cipher Block Chaining Mode

> [!algorithm] CBC Mode
> Suppose $\mathcal E = (E, D)$ is a block cipher defined over $(\mathcal K, \mathcal X)$, where $\mathcal X = \{0, 1\}^n$. Let $N = |\mathcal X| = 2^n$. For any poly-bounded $\ell \geq 1$, we define a cipher $\mathcal E' = (E', D')$, with key space $\mathcal K$, message space $\mathcal X^{\leq \ell}$, and ciphertext space $\mathcal X^{\ell + 1} \backslash \mathcal X^0$; that is, the ciphertext space consists of all nonempty sequences of at most $\ell + 1$ data blocks. Encryption and decryption are defined as follows:
> - For $k \in \mathcal K$ and $m \in \mathcal X^{\leq \ell}$, with $v = |m|$, we define 
> $E'(k, m)$
> 1. Compute $c \in \mathcal X^{v + 1}$ as follows:
> 	1. $c[0] \xleftarrow{R} \mathcal X$
> 	2. for $j \leftarrow 0$ to $v - 1$ do $c[j + 1] \leftarrow E(k, c[j] \oplus m[j])$
> 2. Output $c$.
> - For $k \in \mathcal K$ and $c \in \mathcal X^{\ell + 1} \backslash \mathcal X^0$, with $v = |c| - 1$, we define
> $D'(k, c)$
> 1. Compute $m \in \mathcal X^v$ as follows:
> 	1. for $j \leftarrow 0$ to $v - 1$ do $m[j] \leftarrow D(k, c[j + 1]) \oplus c[j]$
> 2. Output $m$.

> [!theorem]
> If $\mathcal E = (E, D)$ is a secure block cipher defined over $(\mathcal K, \mathcal X)$, and $N = |\mathcal X|$ is super-poly, then for any poly-bounded $\ell \geq 1$, the cipher $\mathcal E'$ is a CPA secure cipher.
> 
> In particular, for every [[#Chosen Plaintext Attack Security|CPA security]] adversary $\mathcal A$ that attack $\mathcal E'$, and which makes at most $Q$ queries to its challenger, there exists [[Block Ciphers#Secure Block Cipher|secure block cipher]] adversary $\mathcal B$ that attacks $\mathcal E$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{CPAadv}[\mathcal A, \mathcal E'] \leq \frac{2Q^2 \ell^2}{N} + 2 \cdot \text{BCadv}[\mathcal B, \mathcal E].$$

