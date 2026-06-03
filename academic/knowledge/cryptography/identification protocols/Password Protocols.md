## Password Protocols

> [!algorithm] Password Protocol (version 1)
> The prover's secret key $sk$ is a password $pw$, chosen as random from some finite password space $\mathcal P$, while the verifier's key $vk$ is $H(pw)$ for some hash function $H: \mathcal P \rightarrow y$. Formally, the **password ID protocol** $\mathcal I_{\text{pwd}} = (G, P, V)$ is defined as follows:
> - $G:$ set $pw \xleftarrow{R} \mathcal P$ and output $sk := pw$ and $vk := H(pw)$.
> - Algorithm $P$, on input $sk = pw$, and algorithm $V$, in input $vk = H(pw)$, interact as follows:
> 	1. $P$ sends $pw$ to $V$;
> 	2. $V$ outputs `accept` if the received $pw$ satisfies $H(pw) = vk$;

> [!algorithm] Secure Identification: Direct Attacks
> For a given identification protocol $\mathcal I = (G, P, V)$ and a given adversary $\mathcal A$, the attack game runs as follows:
> - **Key generation phase**: The challenger runs $(vk, sk) \xleftarrow{R} G()$, and sends $vk$ to $\mathcal A$.
> - **Impersonation attempt**: The challenger and $\mathcal A$ now interact, with the challenger following the verifier's algorithm $V$ (with input $vk$), and with $\mathcal A$ playing the role of a prover, but not necessarily following the prover's algorithm $P$ (indeed, $\mathcal A$ does not receive the secret key $sk$).
> 
> We say that the adversary wins the game if $V$ outputs `accept` at the end of the interaction. We define $\mathcal A$'s advantage with respect to $\mathcal I$, denoted $\text{ID1adv}[\mathcal A, \mathcal I]$, as the probability that $\mathcal A$ wins the game.

 > [!definition] Secure Against Direct Attacks
 > We say that an identification protocol $\mathcal I$ is **secure against direct attacks** if for all efficient adversary $\mathcal A$, the quantity $\text{ID1adv}[\mathcal A, \mathcal I]$ is negligible.

> [!theorem]
> Suppose that hash function $H: \mathcal P \rightarrow \mathcal I$ is one-way. Then the ID protocol $\mathcal I_{\text{pwd}}$ is secure against direct attacks.

### Password Cracking using a Dictionary Attack

> [!definition] Strong, Weak Password
> **Strong password** is a password chosen uniformly at random from a large password space $\mathcal P$.
> **Weak password** is one that is chosen (with some arbitrary distribution) from some small dictionary of common passwords, which we will denote by $\mathcal D$, where $\mathcal D \subseteq \mathcal P$.

> [!algorithm] Online Dictionary Attack
> Suppose an adversary suspects that a certain user's password is weak, and belongs to some small dictionary $\mathcal D$ of common passwords. Then the adversary can mount an **online dictionary attack** by simply trying to log in with all words in $\mathcal D$ one after the other, until a valid password is found. To speed things up, the attacker can sort $\mathcal D$ by popularity and try the most popular passwords first.

> [!algorithm] Offline Dictionary Attack
> Suppose an adversary manages to obtain a verification key $vk = H(pw)$ for some user. If the password $pw$ is weak, and belongs to a small dictionary $\mathcal D$ of common passwords, then the adversary can mount an **offline dictionary attack**, by performing the following computation:
> ```
> for each w in D:
>     if H(w) = vk:
>          output w and halt 
> ```
> If $pw$ belongs to $\mathcal D$, then using this procedure the adversary will obtain $pw$, or possibly some $pw'$ with $H(pw) = H(pw')$.

> [!algorithm] Offline Dictionary Attacks with Preprocessing
> We partition the dictionary attack into two phases: a **processing phase** that is carried out before any hashed passwords are known, and an **attack phase** that cracks a given hashed password $vk$. Our goal is to minimize the time needed for the attack phase to crack a specific $vk$:
> ```
> Preprocessing phase:
>     build a list L of pairs (pw, H(pw)), one pair for each pw in D
> 
> Attack phase on an input vk:
>     if there is an entry (pw, vk) in L, output pw
>     otherwise, output fail
> ```

## Defense Against Dictionary Attack

> [!remark]
> - Salt (public salt)
> - Pepper (private salt)
> - Slow hash functions
> - Slow memory-hard hash functions

> [!algorithm] Password Protocol (version 2)
> - $G$: set $pw \xleftarrow{R} \mathcal P, salt \xleftarrow{R} \mathcal S, y \leftarrow H(pw, salt)$, output $sk := pw$ and $vk := (salt, y)$.
> - Algorithm $P$, on input $sk = pw$, and algorithm $V$, on input $vk = (salt, y)$, interact as follows:
>     1. $P$ sends $pw$ to $V$;
>     2. $V$ outputs `accept` if the received $pw$ satisfies $H(pw, salt) = y$; it outputs `reject` otherwise.

> [!algorithm] Salt One-way Functions with Preprocessing Attack
> Let $H$ be a hash function defined over $(\mathcal D \times \mathcal S, \mathcal Y)$. We define the advantage $\text{OWsp}^\text{ro}\text{adv}[\mathcal A, H]$ of an adversary $\mathcal A = (\mathcal A_0, \mathcal A_1)$ in defeating the one-wayness of $H$ in the preprocessing model as the probability of winning the following game:
> - $\mathcal A_0$ issues queries to $H$ and outputs an advice string $L$;
> - the challenger chooses $(pw, s) \xleftarrow{R} \mathcal D \times \mathcal S$, sets $y := H(pw, s)$, and sends $(L, y, s)$ to $\mathcal A_1$;
> - $\mathcal A_1$ issues queries to $H$ and outputs $pw' \in \mathcal D$; it wins the game if $H(pw', s) = y$.
> 
> Note that the adversary $\mathcal A_1$ is given both $L$ and the salt $s$. It needs to find a pre-image of $y$ with salt $s$. The following theorem gives a bound on the time to invert a salted function $H$ in the processing model, when $H$ is modeled as a random oracle.

> [!theorem] 
> Let $H$ be a hash function defined over $(\mathcal D \times \mathcal S, \mathcal Y)$ where $H$ is modeled as random oracle and where $|\mathcal D| \leq |\mathcal Y|$. Let $\mathcal A = (\mathcal A_0, \mathcal A_1)$ be an adversary, where $\mathcal A_0$ outputs an $\ell$-bit advice string $L$, and $\mathcal A_1$ makes at most $Q_{\text{ro}}$ queries to $H$. Then $$\text{OWsp}^\text{ro}\text{adv}[\mathcal A, H] \leq O(\frac{\ell \cdot Q_{\text{ro}}}{|\mathcal S| \cdot |\mathcal D|} + \frac{Q_{\text{ro}}}{|\mathcal D|}).$$

> [!algorithm] Password Protocol (Version 3)
> - $G$: set $pw \xrightarrow{R} \mathcal P, salt \xrightarrow{R} \mathcal S, pepper \xrightarrow{R} \mathcal S_p, y \rightarrow H(pw, salt, pepper),$ 
> $\text{ output } sk := pw \text{ and } vk := (salt, y)$.
> - Algorithm $P$, on input $sk = pw$, and algorithm $V$, on input $vk = (salt, y)$, interact as follows:
> 	1. $P$ sends $pw$ to $V$;
> 	2. $V$ outputs `accept` if the received $pw$ satisfies $H(pw, salt, p)$ for some $p \in \mathcal S_p$; it outputs `reject` otherwise.

### Password-based Key Derivation Function

> [!definition] Password-based Key Derivation Function
> A **password-based key derivation function** (or **PBKDF**), is a function $H$ that takes as input a password $pw \in \mathcal P$, a salt in $S$, and a difficulty $d \in \mathbb Z^{> 0}$. It outputs a value $y \in \mathcal Y$. We require that $H$ is computable by an algorithm that runs in time proportional to $d$. As usual, we say that the PBKDF is defined over $(\mathcal P, \mathcal S, \mathcal Y)$.

> [!algorithm] PBKDF1
> For a hash function $H$ defined over $(\mathcal X, \mathcal X)$.
> $\text{PBKDF1}_H(pw, salt, d) := H^{(d)}(pw, salt).$

> [!algorithm] PBKDF2
> Let $F$ be a PRF defined over $(\mathcal P, \mathcal X, \mathcal X)$ where $\mathcal X := \{0, 1\}^n$. The derived PBKDF, denoted $\text{PBKDF2}_F$, is defined over $(\mathcal P, \mathcal X, \mathcal X)$ and works as follows:
> $$\text{PBKDF2}_F(pw, salt, d) := \left\{  
\begin{aligned}  
&x_0 \leftarrow F(pw, \text{salt}) \\  
&\text{for } i = 1, \ldots, d-1:\quad x_i \leftarrow F(pw, x_{i-1}) \\  
&\text{output } y \leftarrow x_0 \oplus x_1 \oplus \cdots \oplus x_{d-1} \in \mathcal{X}  
\end{aligned}  
\right\}$$
> An extension for output in $\mathcal X^b$ with $1 < b < 2^32$: 
>  $$\text{PBKDF2}^{(b)}_F(pw, salt, d) := (\text{PBKDF2}_F(pw, salt_1, d), \dots, \text{PBKDF2}_F(pw, salt_b, d)) \in \mathcal X^b$$ where all $b$ salts are derived from the provided salt by setting $salt_i \leftarrow salt || \text{bin}(i)$. Here, $\text{bin}(i)$ is the binary representation of $i \in \{1, \dots, b\}$ as a 32-bit string.

### Scrypt

> [!algorithm] Scrypt
> Function $Scypt_h(x_0, d)$
> 
> **Input**: $x_0 \in \mathcal X$, difficulty $d \in \mathbb Z^{> 0}$
> 
> ---
> 1. Calculate $x_i = h^{(i)}(x_0)$ for $i \in 1,\cdots, d$
> 2. $y_0 \leftarrow x_d$
> 3. For $i = 1, \cdots, d$:
> 	1. $j \leftarrow \text{int}(y_{i - 1}) \mod (d + 1)$
> 	2. $y_i \rightarrow h(y_{i - 1} \oplus x_j)$
> 4. Returns $y_d \in \mathcal X$.

> [!algorithm] Scrypt PBKDF
> The Scrypt PBKDF, defined over $(\mathcal P, \mathcal X, \mathcal X)$, is built from the Scrypt hash and works as follows:
> $$\text{ScryptPBKDF}_h(pw, salt, d) := \left\{ 
> \begin{align}&x_0 \leftarrow \text{PBKDF2}_F(pw, salt, 1) \\ &y \leftarrow \text{Scrypt}_h(x_0, d) \\ &\text{output } \text{PBKDF2}_F(pw, y, 1)\end{align}
> \right \}$$

> [!algorithm] Parallel Random Oracle Algorithm
> A **parallel random oracle algorithm** $\mathcal A$ takes as input an $x \in \mathcal X$ and runs through a sequence states. At each state the algorithm issues a set of queries to the random oracle $h$. The algorithm is given the responses to all its queries and it then moves to the next state. This process is repeated until the algorithm terminates, at which point the final state contains the output. We record all the intermediate states to keep track of their size.
> Formally, the algorithm $\mathcal A$ implements a deterministic mapping:
> $$\mathcal A : \mathcal X \times \mathcal S \times \mathcal Z^{\leq p} \rightarrow \mathcal S \times \mathcal Y^{\leq p}$$ for some positive integer $p$, and operates as follows:
> - $\mathcal A$ is first invoked as $\mathcal A(x, \varepsilon, \varepsilon)$ and outputs a pair $(s_1, \overline{y}_1)$ in $\mathcal S \times \mathcal Y^{\leq p}$. Here, $s_1$ is $\mathcal A$'s current state and $\overline{y} = (y_1, \dots, y_r)$ is its first set of parallel queries to the random oracle $h: \mathcal Y \rightarrow \mathcal Z$.
> - For $i = 1, \dots, t$, when $\mathcal A$ outputs $(s_i, \overline{y}_i)$ with $\overline{y}_i = (y_1, \dots, y_r) \in \mathcal Y^{\leq p}$, we do the following:
> 	- Evaluate the oracle $h$ in parallel by setting $\overline{z}_i \leftarrow (h(y_1), \dots, h(y_r))$, and
> 	- Re-invoke $\mathcal A$ as $(s_{i + 1}, \overline{y}_{i + 1}) \leftarrow \mathcal A(x, s_i, \overline{z}_i)$.
> - Eventually $\mathcal A$ outputs $(s, \varepsilon)$ indicating that it is done and that the output is $s$.
> The running time of $\mathcal A$ on input $x \in \mathcal X$ is the number of times that $\mathcal A$ is invoked until it terminates. Measuring running time this way captures the fact a hardware implementation can evaluate the hash function $h$ at many points in parallel.
> 
> We record the data given to $\mathcal A$ in step $i$ as $st_i := (s_i, \overline{z}_i)$. We call $st_i$ the input state at time $i$. For $s \in \mathcal S$ we let $|s|$ denote the length of $s$ in bits, and similarly we let $|z|$ denote the length of $z \in \mathcal Z$. For $\overline{z} = (z_1, \dots, z_r) \in \mathcal Z^{\leq p}$, we let $|\overline{z}| := \sum_{j = 1}^r |z_i|$. When $\mathcal Z = \{0, 1\}^n$ we have $|\overline{z}| = rn$. Finally, the bit length of an input state $st = (s, \overline{z})$ is defined as $|st| := |s| + |t|$.

> [!definition] Cumulative Memory Complexity
> Let $\mathcal A$ be a parallel random oracle algorithm taking inputs in $\mathcal X$. The cumulative memory complexity of $\mathcal A$ with respect to $h: \mathcal Y \rightarrow \mathcal Z$ and $x \in \mathcal X$, denoted $\text{mem}[\mathcal A, h, x]$, is defined as $$\text{mem}[\mathcal A, h, x] := \sum_{i = 1}^t |st_i|$$

> [!theorem]
> Let $\mathcal X := \{0, 1\}^n$ be such that $|\mathcal X|$ is super-poly and let $d$ be chosen so that $2^{-d}$ is negligible. Then for all parallel random oracle algorithms $\mathcal A$ and all $x \in \mathcal X$, $$P[\mathcal A(x, d) = \text{Scrypt}_h(x, d)] \leq P[\text{mem}[\mathcal A, h, (x, d)] \geq \ohm(d^2 n)] + \delta$$

