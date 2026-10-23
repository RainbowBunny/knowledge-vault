Reference:
- `[BS]` — D. Boneh, V. Shoup, _A Graduate Course in Applied Cryptography_, v0.6, 2023, Ch. 18: https://toc.cryptobook.us/ (Attack Game 18.1; password protocols; the salted one-wayness game with preprocessing). `⚠️ CLAUDE – verify:` WebFetch reaches only the front of the book, so Ch. 18 could not be read; the games redraw the wording this note already had, checked against `[AABN02]` and `[CDGS18]`.
- `[AABN02]` — M. Abdalla, J. H. An, M. Bellare, C. Namprempre, _From Identification to Signatures via the Fiat–Shamir Transform_, EUROCRYPT 2002; full version ePrint 2002/022: https://eprint.iacr.org/2002/022 (Def 2.1, impersonation under passive attack).
- `[CDGS18]` — S. Coretti, Y. Dodis, S. Guo, J. Steinberger, _Random Oracles and Non-Uniformity_, EUROCRYPT 2018; full version ePrint 2017/937: https://cims.nyu.edu/~dodis/ps/presampling.pdf (Def 2, the $(S, T)$-attacker; §3.1, one-wayness; §6.1, salting).
- `⚠️ CLAUDE – verify:` — a point I could not check against the source.

## Password Protocols

> [!algorithm] Password Protocol (version 1)
> The prover's secret key $sk$ is a password $pw$, chosen as random from some finite password space $\mathcal P$, while the verifier's key $vk$ is $H(pw)$ for some hash function $H: \mathcal P \rightarrow \mathcal Y$. Formally, the **password ID protocol** $\mathcal I_{\text{pwd}} = (\mathsf{KeyGen}, P, V)$ is defined as follows:
> - $\mathsf{KeyGen}$: set $pw \xleftarrow{R} \mathcal P$ and output $sk := pw$ and $vk := H(pw)$.
> - Algorithm $P$, on input $sk = pw$, and algorithm $V$, in input $vk = H(pw)$, interact as follows:
> 	1. $P$ sends $pw$ to $V$;
> 	2. $V$ outputs `accept` if the received $pw$ satisfies $H(pw) = vk$;

### Security Against Direct Attacks

> [!definition] Parameters
> - [[Identification Protocol#ID Protocol|ID protocol]] $\mathcal I = (\mathsf{KeyGen}, P, V)$.
> - $\mathcal A$: an efficient [[Adversary|adversary]], playing a cheating prover.
> - $a_j$: the $j$-th message $\mathcal A$ sends as the prover; $b_j$: the verifier's reply.
> - $\mathrm{out} \in \{\text{accept}, \text{reject}\}$: the verifier's output.

> [!definition] Secure Identification: Direct Attacks
> ### Scope
> An identification protocol $\mathcal I = (\mathsf{KeyGen}, P, V)$ and an efficient adversary $\mathcal A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ gets $vk$ and nothing else: no transcript, no interaction with the prover, never $sk$.
> - **Promise** — none.
> - **Quantifier** — $\forall$ efficient $\mathcal A$.
> - **Adaptivity** — one impersonation attempt, after $vk$ is sent; each message of $\mathcal A$ may depend on everything it has seen.
>
> ---
> ### Experiment
> A search game with one branch: the challenger plays the honest verifier $V(vk)$, and its last row computes the verifier's output. `[BS Attack Game 18.1]`
>
> | | challenger $\mathcal C$ (honest verifier $V(vk)$) | | adversary $\mathcal A$ (cheating prover) |
> | --- | --- | --- | --- |
> | 1 | $(vk, sk) \xleftarrow{R} \mathsf{KeyGen}()$ | $\xrightarrow{\ vk\ }$ | |
> | 2 | | $\xleftarrow{\ a_j\ }$ | **Impersonation attempt** (repeated, one row pair per round of the protocol): sends the prover's next message $a_j$, not necessarily computed by $P$ |
> | | runs $V(vk)$ on $a_j$<br>$b_j \leftarrow$ the verifier's next message | $\xrightarrow{\ b_j\ }$ | |
> | 3 | $\mathrm{out} \leftarrow$ the output of $V(vk)$ | | |
>
> In a protocol where the verifier speaks first, such as a challenge–response protocol, each row pair of row 2 starts with $b_j$.
>
> **Goal** — $\mathcal A$ wins iff:
> - $\mathrm{out} = \text{accept}$.
>
> ---
> ### Property
> $$\text{ID1adv}[\mathcal A, \mathcal I] = \Pr[\mathcal A \text{ wins}].$$
> - $\mathcal I$ is **secure against direct attacks** if $\text{ID1adv}[\mathcal A, \mathcal I]$ is negligible for every efficient $\mathcal A$.
>
> A *search* game, see [[Security Game]].

> [!remark] Notation in the literature
> - `[BS]` writes the protocol as $(G, P, V)$, with $G$ taking no input, and splits the game into a *key generation phase* and an *impersonation attempt*. Here the adversary is one stateful machine and the phases are rows, see [[Security Game]].
> - For a three-move protocol, a direct attack is the passive attack of `[AABN02 Def 2.1]` with no transcript queries: the impersonator outputs a commitment and a state, receives a random challenge, and answers from that state.

> [!theorem]
> Suppose that hash function $H: \mathcal P \rightarrow \mathcal Y$ is one-way. Then the ID protocol $\mathcal I_{\text{pwd}}$ is secure against direct attacks.

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
> - $\mathsf{KeyGen}$: set $pw \xleftarrow{R} \mathcal P$, $salt \xleftarrow{R} \mathcal S$ and $y \leftarrow H(pw, salt)$; output $sk := pw$ and $vk := (salt, y)$.
> - Algorithm $P$, on input $sk = pw$, and algorithm $V$, on input $vk = (salt, y)$, interact as follows:
>     1. $P$ sends $pw$ to $V$;
>     2. $V$ outputs `accept` if the received $pw$ satisfies $H(pw, salt) = y$; it outputs `reject` otherwise.

> [!definition] Parameters
> - $H$: a hash function defined over $(\mathcal D \times \mathcal S, \mathcal Y)$, modeled as a [[Random Oracle Model|random oracle]]: $\mathcal D$ is the dictionary, $\mathcal S$ the salt space.
> - $\mathcal A$: an adversary. $\ell$: the length in bits of its advice string $L$. $Q_{\text{ro}}$: the bound on its queries to $H$ after the challenge.
> - $x_j$: a query to $H$; $h_j$: its answer. $(pw, s)$: the challenge password and salt; $y$: their hash. $pw' \in \mathcal D$: the adversary's answer.

> [!definition] Salted One-Wayness with Preprocessing
> ### Scope
> A hash function $H$ over $(\mathcal D \times \mathcal S, \mathcal Y)$, modeled as a random oracle, and an adversary $\mathcal A$ with an $\ell$-bit advice string.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ queries $H$ before and after the challenge. Before it, $\mathcal A$ sees no challenge; between the two, it keeps only the $\ell$-bit advice string $L$, which the challenger hands back with the challenge. The salt $s$ is public.
> - **Promise** — none; $pw$ and $s$ are uniform.
> - **Quantifier** — $\forall \mathcal A$ with $\ell$-bit advice and at most $Q_{\text{ro}}$ queries after the challenge. `⚠️ CLAUDE – verify:` the preprocessing queries of row 1 are not counted; in `[CDGS18 Def 2]` the first stage is computationally unbounded — check `[BS]`.
> - **Adaptivity** — $L$ is fixed before $(pw, s)$ is chosen; the later queries may depend on $(L, y, s)$.
>
> ---
> ### Experiment
> A search game with one branch; row 6 computes the winning condition. `[BS Ch. 18]`; `[CDGS18 Def 2, §3.1, §6.1]`.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | | $\xleftarrow{\ x_j\ }$ | **Preprocessing hash queries** (repeated, adaptive): sends a point $x_j \in \mathcal D \times \mathcal S$ |
> | | $h_j \leftarrow H(x_j)$ | $\xrightarrow{\ h_j\ }$ | |
> | 2 | | $\xleftarrow{\ L\ }$ | sends an advice string $L \in \{0, 1\}^\ell$, and forgets everything else |
> | 3 | $(pw, s) \xleftarrow{R} \mathcal D \times \mathcal S$<br>$y \leftarrow H(pw, s)$ | $\xrightarrow{\ L,\, y,\, s\ }$ | |
> | 4 | | $\xleftarrow{\ x_j\ }$ | **Hash queries** (repeated, adaptive, at most $Q_{\text{ro}}$ times): sends a point $x_j \in \mathcal D \times \mathcal S$ |
> | | $h_j \leftarrow H(x_j)$ | $\xrightarrow{\ h_j\ }$ | |
> | 5 | | $\xleftarrow{\ pw'\ }$ | outputs a password $pw' \in \mathcal D$ |
> | 6 | checks whether $H(pw', s) = y$ | | |
>
> **Goal** — $\mathcal A$ wins iff:
> - $H(pw', s) = y$: $pw'$ is a pre-image of $y$ under the salt $s$, not necessarily $pw$.
>
> ---
> ### Property
> $$\text{OWsp}^{\text{ro}}\text{adv}[\mathcal A, H] = \Pr[\mathcal A \text{ wins}].$$
> - The theorem below bounds it when $H$ is a random oracle: the advice helps only through the term $\ell \cdot Q_{\text{ro}} / (|\mathcal S| \cdot |\mathcal D|)$, which a large salt space makes small.

> [!remark] Notation in the literature — and why row 2 forgets
> `[BS]` writes the adversary as a pair $\mathcal A = (\mathcal A_0, \mathcal A_1)$: $\mathcal A_0$ issues queries to $H$ and outputs $L$, and the challenger sends $(L, y, s)$ to $\mathcal A_1$. `[CDGS18 Def 2]` has the same split, an $(S, T)$-attacker $(\mathcal A_1, \mathcal A_2)$ whose unbounded first stage outputs $S$ bits of advice and whose second stage makes $T$ queries. Here the split is not cosmetic: the bound counts the $\ell$ bits that cross from preprocessing to the attack. So the table keeps one adversary column, but row 2 erases everything except $L$ and row 3 hands $L$ back — the one exception to the rule that $\mathcal A$ remembers every earlier row ([[Security Game]]).

> [!theorem] 
> Let $H$ be a hash function defined over $(\mathcal D \times \mathcal S, \mathcal Y)$ where $H$ is modeled as random oracle and where $|\mathcal D| \leq |\mathcal Y|$. Let $\mathcal A$ be an adversary whose advice string $L$ has $\ell$ bits and which makes at most $Q_{\text{ro}}$ queries to $H$ after receiving the challenge (in `[BS]`: $\mathcal A_0$ outputs $L$ and $\mathcal A_1$ makes the queries). Then $$\text{OWsp}^\text{ro}\text{adv}[\mathcal A, H] \leq O(\frac{\ell \cdot Q_{\text{ro}}}{|\mathcal S| \cdot |\mathcal D|} + \frac{Q_{\text{ro}}}{|\mathcal D|}).$$

> [!algorithm] Password Protocol (Version 3)
> - $\mathsf{KeyGen}$: set $pw \xleftarrow{R} \mathcal P$, $salt \xleftarrow{R} \mathcal S$, $pepper \xleftarrow{R} \mathcal S_p$ and $y \leftarrow H(pw, salt, pepper)$; output $sk := pw$ and $vk := (salt, y)$.
> - Algorithm $P$, on input $sk = pw$, and algorithm $V$, on input $vk = (salt, y)$, interact as follows:
> 	1. $P$ sends $pw$ to $V$;
> 	2. $V$ outputs `accept` if the received $pw$ satisfies $H(pw, salt, p) = y$ for some $p \in \mathcal S_p$; it outputs `reject` otherwise.

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

