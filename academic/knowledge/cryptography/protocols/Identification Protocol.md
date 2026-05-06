
| Term                                                           | Reference                                                                       |                  |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------- | ---------------- |
| Attack Game 18.1 (Secure identification: direct attacks)       | [[#Password Protocols\|direct attack]]                                          | $\text{ID1adv}$  |
| Attack Game 18.2 (Secure identification: eavesdropping attack) | [[#Security Against Eavesdropping\|eavesdropping attack]]                       | $\text{ID2adv}$  |
| Attack Game 18.3 (Secure identification: active attacks)       | [[#Security Against Active Attacks\|active attacks]]                            | $\text{ID3adv}$  |
| Attack Game 19.1 ($r$-impersonating eavesdropping attack)      | [[#Repeated Impersonating Attacks\|r-impersonation eavesdropping attack]]       | $\text{rID2adv}$ |
| Attack Game 19.2 (One-way key generation)                      | [[#Identification and Signatures from Sigma Protocols\|one-way key generation]] | $\text{OWadv}$   |
|                                                                |                                                                                 |                  |

> [!definition] Identification Problem
> Party $A$ wished to identify itself to party $B$ to gain access to resources available at $B$.

## Interactive Protocol

> [!definition] Interactive Protocol
> - A protocol may be run many times. Each such protocol run is called a **protocol instance**.
> - When a party executes a protocol instance, it starts by supplying **input value**, which defines the **initial configuration** of the protocol instance for that party.
> - The interaction can be modelled by an **interactive protocol algorithm**, which is an efficient probabilistic algorithm $I$ that takes as input a pair $(config_{\text{old}}, data_{\text{in}})$, where $config_{\text{old}}$ is an encoding of the current configuration and $data_{\text{in}}$ is an encoding of the incoming message; and outputs a pair $(config_{\text{new}}, data_{\text{out}})$ where $(config_{\text{new}})$ is an encoding of the new configuration, and $data_{\text{out}}$ encodes an outgoing message. 
> - The party iterates this as many times required by the protocol, until some **terminal configuration** is reached. This terminal configuration may specify an **output value**, which maybe used by the party, presumably in some higher-level protocol.

## ID Protocol

> [!definition] Identification (ID) Protocols
> The identification problem involves two parties, a **prover** and a **verifier**. The prover has a **secret key** $sk$ that it uses to convince the verifier of its identity. The verifier has a corresponding **verification key** $vk$ that it uses to confirm the prover's claim.

> [!definition] ID Protocol
> An **identification protocol** is a triple $\mathcal I = (G, P, V)$.
> - $G$ is a probabilistic, **key generation** algorithm, that takes no input, and output $(vk, sk)$, where $vk$ is called the **verification key** and $sk$ is called the **secret key**.
> - $P$ is an interactive protocol algorithm called the **prover**, which takes as input a secret key $sk$, as output by $G$.
> - $V$ is an interactive protocol algorithm called the **verifier**, which takes as input a verification key $vk$, as output by $G$, and which outputs `accept` or `reject`.
> 
> We require that when $P(sk)$ and $V(vk)$ interact with one another, $V(vk)$ always outputs `accept`. That is, for all possible outputs $(vk, sk)$ of $G$, if $P$ is initialized with $sk$, and $V$ is initialized with $vk$, then with probability $1$, at the end of the interaction between $P$ and $V$, $V$ outputs `accept`.

> [!definition] Attack models for ID Protocol
> - **Direct Attacks**: The adversity cannot eavesdrop on conversations. Then using no information other than what is publicly available, the adversary must somehow impersonate the prover to the verifier. A simple password protocol is sufficient to defend against such direct attacks.
> - **Eavesdropping Attacks**: The adversary can eavesdrop on the channel and obtain the transcript of several interactions between the prover and the verifier. In this case, the simple password protocol is insecure. However, a slightly more sophisticated protocol based on one-time passwords is secure.
> - **Active Attacks**: The adversary uses the interaction to try and learn something that will let it later impersonate the prover to the verifier. Identification protocols secure against such active attacks require interaction between the prover and verifier. They use a technique called challenge-response.
> - **Concurrent vs Sequential Attacks**: Note that in the active probing phase of the attack game, we allow the adversary to interact concurrently with many instances of the prover. One could consider a weaker attack model in which these interactions must be run sequentially. However, all of the protocols we consider achieve security in this stronger, concurrent attack model.

> [!proposition] Type of ID Protocol
> - **Secret vs Public Verification Keys**: In some ID protocols the verifier must keep its verification key $vk$ secret, while in the other protocols $vk$ can be public. Clearly protocols where $vk$ can be public are preferable since no damage is caused if the verifier is compromised.
> - **Stateless vs Stateful Protocol**: Ideally, $vk$ and $sk$ should not change after they are chosen at setup time. In some protocols, however, $vk$ and $sk$ are updated every time the protocol executes: the prover updates $sk$ and the verifier updates $vk$. Protocols where $vk$ and $sk$ are fixed forever are called **stateless**. Protocols where $vk$ and $sk$ are updated are called **stateful**. Some stateful protocols provide higher levels of security at lower cost than their stateless counterparts. However, stateful protocols can be harder to use because the prover and verifier must remain properly synchronized.
> - **One-sided vs mutual identification**: **One-sided identification** problem is Bob wishes to verify Alice's identity. **Mutual identification** is Bob also identifies itself to Alice.

> [!remark] Security and Limitation of Identification Protocols
> - Identification protocols are designed to prevent an adversary from impersonating Alice without Alice's assistance. When defining the security of the protocols, we may allow the adversary to eavesdrop and possibly interact with Alice; however, when it comes time to impersonate Alice, the adversary must do so without communicating with Alice.
> - ID protocols can be vulnerable to a man in the middle (MiTM) attack.

> [!proposition] Keeping $vk$ secret
> If $vk$ is kept secret, then we must now allow the adversary to interact with the verifier, since such interactions could potentially leak information about $vk$. Therefore, in the active probing phase, we allow the adversary to interact concurrently with multiple instances of both the prover and the verifier. When interacting with an instance of the verifier, the adversary learns if the verifier outputs `accept` or `reject`. In addition, during the impersonation attempt, we let the adversary interact concurrently with several verifiers, and the adversary wins the game if at least one of these verifiers accepts.

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

## Security Against Eavesdropping

> [!algorithm] Secure Identification: Eavesdropping Attacks
> For a given identification protocol $\mathcal I = (G, P, V)$ and a given adversary $\mathcal A$, the attack game runs as follow:
> - **Key generation phase**: The challenger runs $(vk, sk) \xleftarrow{R} G()$, and sends $vk$ to $\mathcal A$.
> - **Eavesdropping phase**: The adversary requests some number, say $Q$, of transcripts of conversations between $P$ and $V$. The challenger complies by running the interaction between $P$ and $V$ a total of $Q$ times, each time with $P$ initialized with input $sk$ and $V$ initialized with $vk$. The challenger sends these transcripts $T_1, \dots, T_Q$ to the adversary.
> - **Impersonate attempt**: The challenger and $\mathcal A$ interact, with the challenger following the verifier's algorithm $V$ (with input $vk$), and with $\mathcal A$ playing the role of a prover, but not necessarily following the prover's algorithm $P$.
> 
> We say that the adversary wins the game if $V$ outputs `accept` at the end of the interaction. We define $\mathcal A$'s advantage with respect to $\mathcal I$, denoted $\text{ID2adv}[\mathcal A, \mathcal I]$, as the probability that $\mathcal A$ wins the game.

> [!definition] Secure Against Eavesdropping Attacks
> We say that an identification protocol $\mathcal I$ is **secure against eavesdropping attacks** if for all efficient adversaries $\mathcal A$, the quantity $\text{ID2adv}[\mathcal A, \mathcal I]$ is negligible.

> [!proposition] 
>  We let $\text{wIDadv}[\mathcal A, \mathcal I]$ denote the adversary's advantage in winning when keeping $vk$ secret in this eavesdropping attack. ID protocols secure in these settings are said to be **weakly secure**.

> [!definition] Weakly Secure Against Eavesdropping Attacks
> Let $\text{wIDadv}[\mathcal A, \mathcal I]$ denote the adversary's advantage in winning the weaker version of Eavesdropping Attacks. We say that an identification protocol $\mathcal I$ is **weakly secure against eavesdropping attacks** if for all efficient adversaries $\mathcal A$, the quantity $\text{wID2adv}[\mathcal A, \mathcal I]$ is negligible.

### Hash-based One-Time Password

> [!algorithm] Hash-based One-Time Password
> Let $F$ be a PRF defined over $(\mathcal K, \mathbb Z_N, \mathcal Y)$ for some large integer $N$, say $N = 2^{128}$. This $F$ is used to update the password after every successful invocation. The HOTP protocol HOTP $= (G, P, V)$ works as follows:
> - $G$: choose a random $k \xleftarrow{R} \mathcal K$ and output $sk := (k, 0)$ and $vk := (k, 0)$.
> - Algorithm $P$ given $sk$, and algorithm $V$ given $vk$, interact as follows:
> 	1. $P(sk = (k, i))$: send $r := F(k, i)$ to $V$ and set $sk \leftarrow (k, i + 1)$,
> 	2. $V(vk = (k, i))$: if the received $r$ from $P$ satisfies $r = F(k, i)$ output `accept` and set $vk \leftarrow (k, i + 1)$. Otherwise, output `reject`.
> 
> Here both $vk$ and $sk$ must be kept secret, and therefore HOTP is only **weakly** secure against eavesdropping. Note that the integer $N$ is chosen to be so large that, in practice, the counter $i$ will never wrap around. Implementations of HOTP typically use HMAC-SHA256 as the underlying PRF, where the output is truncated to the desired size, typically six decimal digits.

> [!theorem]
> Let $F$ be a PRF defined over $(\mathcal K, \mathbb Z_N, \mathcal Y)$, where $N$ and $|\mathcal Y|$ are both super-poly. Then the ID protocol HOTP is weakly secure against eavesdropping.

> [!remark] Problem of HOTP
> 1. Counter is required because there is no implicit counter for synchronize between client and server.
> 2. The one-time password of HOTP is only updated when the user initiates the protocol so impersonate is easy.

### Time-based One-Time Password

> [!algorithm] Time-based One-Time Password
> **Time-based one-time passwords**, or **TOTP** is when the counter $i$ is incremented by one every 30 seconds, whether the user authenticates or not. 

### S/Key Protocol

> [!algorithm] The S/key Protocol
> The protocol $\text{SKey}_n = (G, P, V)$, designed for $n$ invocations, works as follows:
> - $G$: choose a random $k \xleftarrow{R} \mathcal X$. Output $sk := (k, n)$ and $vk := H^{(n + 1)}(k)$,
> - Algorithm $P$ given $sk$, and algorithm $V$ given $vk$, interact as follows:
> 	1. $P(sk = (k, i))$: send $t := H^{(i)}(k)$ to $V$ and set $sk \leftarrow (k, i - 1)$,
> 	2. $V(vk)$: if the received $t$ from $P$ satisfies $vk = H(t)$ output `accept` and set $vk \leftarrow t$. Otherwise, output `reject`. 

> [!remark]
> S/key protocol remains secure even if $vk$ is made public. Hence, S/key is fully secure against eavesdropping, while HOTP is only weakly secure.

> [!theorem]
> Let $H: \mathcal X \rightarrow \mathcal X$ be a one-way function on $n$ iterates. Then the ID protocol $SKey_n$ is secure against eavesdropping.

> [!remark]
> Algorithm $G$ could choose a public salt at setup time and prepend this salt to the input on every application of $H$. Moreover, to avoid the attack of **14.18** it is recommended to use a different hash function at every step in the chain.

> [!remark] The trouble with S/Key
> In every authentication attempt, the prover $P$ must send to $V$ an element $t \in \mathcal X$. For $H$ to be one-way, the set $\mathcal X$ must be large and therefore $t$ can not be a 6-digit number as in the TOTP system. In practice, $t$ needs to be at least 128 bits to ensure that $H$ is one-way. This makes it inconvenient to use S/key as a one-time password scheme where the user needs to type in a password. Encoding a 128-bit $t$ as printable characters requires at least 22 characters.

## Security Against Active Attacks

> [!algorithm] Secure Identification: Active Attacks
> For a given identification protocol $\mathcal I = (G, P, V)$ and given adversary $\mathcal A$, the attack game, runs as follows:
> - **Key generation phase**: The challenger runs $(vk, sk) \xleftarrow{R} G()$, and sends $vk$ to $\mathcal A$.
> - **Active probing phase**: The adversary requests to interact with the prover. The challenger complies by interacting with the adversary in an ID protocol with the challenger playing the role of the prover by running algorithm $P$ initialized with $sk$. The adversary plays the role of verifier, but not necessarily following the verifier's algorithm $V$. The adversary may interact concurrently with many instances of the prover - these interactions may be arbitrarily interleaved with one another.
> - **Impersonation attempt**: The challenger and $\mathcal A$ interact, with the challenger following the verifier's algorithm $V$ (with input $vk$), and with $\mathcal A$ playing the role of a prover, but not necessarily following the prover's algorithm $P$.
> 
> We say that the adversary wins the game if the verification protocol $V$ outputs `accept` at the end of the interactions. We define $\mathcal A$'s advantage with respect to $\mathcal I$, denoted $\text{ID3Adv}[\mathcal A, \mathcal I]$, as the probability that $\mathcal A$ wins the game.

> [!definition] Secure Against Active Attacks
> We say that an identification protocol $\mathcal I$ is secure against active attacks if for all efficient adversaries $\mathcal A$, the quantity $\text{ID3adv}[\mathcal A, \mathcal I]$ is negilgile.

> [!definition] Weakly Secure Against Active Attack
> Let $\text{wID3adv}[\mathcal A, \mathcal I]$ denote the adversary's advantage in winning the weaker version of Active Attacks. We say an identification protocol $\mathcal I$ is **weakly secure against active attacks** if for all efficient adversaries $\mathcal A$, the quantity $\text{wID3adv}[\mathcal A, \mathcal I]$ is negligible.

### Challenge Response Protocols

> [!algorithm] MAC Challenge-Response Protocol
> Let $\mathcal I = (S_{\text{mac}}, V_{\text{mac}})$ be a MAC defined over $(\mathcal K, \mathcal M, \mathcal T)$. The challenge-response protocol $\text{ChalResp}_{mac} = (G, P, V)$, works as follows:
> - $G$: choose a random $k \xleftarrow{R} \mathcal K$, and output $sk := k$ and $vk := k$.
> - Algorithm $P$ with input $sk = k$, algorithm $V$ with input $vk = k$, interact as follows:
> 	1. $V$ chooses a random $c \xleftarrow{R} \mathcal M$, and sends $c$ to $P$;
> 	2. $P$ computes $t \xleftarrow{R} S_{\text{mac}}(k, c)$, and sends $t$ to $V$;
> 	3. $V$ outputs $V_{\text{mac}}(k, c, t)$.
> The random $c$ is called the **challenge** while $t$ is called the **response**. Clearly $vk$ must be kept secret for the protocol to be secure.

> [!theorem]
> Suppose $\mathcal I$ is a secure MAC system, and that the size of the message space, $|\mathcal M|$, is super-poly. Then ID protocol $\text{ChalResp}_{mac}$ is weakly secure against active attacks.

> [!algorithm] Signature Challenge-Response Protocol
> Replace the MAC with a signature scheme $(G, S_{sig}, V_{sig})$ defined over $(\mathcal M, \mathcal T)$. The main change is that prover responds to the challenge using algorithm $S_{sig}$ and the secret signing key. The verifier checks the response using algorithm $V_{sig}$ and the public verification key. We refer to the resulting protocol as $\text{ChalResp}_{sig}$.

> [!theorem]
> Assume $\mathcal S$ is a secure signature scheme, and that the size of the message space, $|\mathcal M|$, is super-poly. Then $\text{ChalResp}_{sig}$ is secure against active attacks.

## Schnorr's Identification Protocol

> [!algorithm] Schnorr's Identification Protocol
> Let $\mathcal C$ be a subset of $\mathbb Z_q$. Then Schnorr's identification protocol is $\mathcal I_{sch} = (G, P, V)$, where:
> - The key generation algorithm $G$ runs as follows: $$\alpha \xleftarrow{R} \mathbb Z_q, u \leftarrow g^{\alpha}.$$ The verification key is $vk := u$, and the secret key is $sk := \alpha$.
> - The protocol between $P$ and $V$ runs as follows, where the prover $P$ is initialized with $sk = \alpha$, and the verifier $V$ is initialized with $vk = u$:
> 	1. $P$ computes $\alpha_t \xleftarrow{R} \mathbb Z_q, u_t \leftarrow g^{\alpha_t}$, and sends $u_t$ to $V$;
> 	2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends $c$ to $P$;
> 	3. $P$ computes $\alpha_z \leftarrow \alpha_t + \alpha c \in \mathbb Z_q$, and sends $\alpha_z$ to $V$;
> 	4. $V$ checks if $g^{\alpha_z} = u_t \cdot u^c$; if so $V$ outputs `accept`; otherwise, $V$ outputs `reject`.

> [!definition]
> An interaction between $P(\alpha)$ and $V(u)$ generates a **conversation** $(u_t, c, \alpha_z) \in \mathbb G \times \mathcal C \times \mathbb Z_q$. We call such a conversation an **accepting conversation for** $u$ if $V$'s check passes, i.e., if $g^{\alpha_z} = u_t \cdot u^c$. The set $\mathcal C$ is called the **challenge space**.

> [!theorem]
> Under the DL assumption for $\mathbb G$, and assuming $N := |\mathcal C|$ is super-poly, Schnorr's identification protocol is secure against direct attacks.
> 
> In particular, suppose $\mathcal A$ is an efficient impersonation adversary attacking $\mathcal I_{sch}$ via a direct attack with advantage $\epsilon := \text{ID1adv}[\mathcal A, \mathcal I_{sch}]$. Then there exists an efficient DL adversary $\mathcal B$ (whose running time is about twice that of $\mathcal A$), with advantage $\epsilon' := \text{DLadv}[\mathcal B, \mathbb G]$, such that $$\epsilon' \geq \epsilon^2 - \epsilon / N,$$ which implies $$\epsilon \leq \frac{1}{N} + \sqrt{\epsilon'}.$$

> [!lemma] Rewinding Lemma
> Let $S$ and $T$ be finite, non-empty sets, and let $f : S \times T \rightarrow \{0, 1\}$ be a function. Let $X$, $Y$ and $Y'$ be mutually independent random variables, where $X$ takes values in the set $S$, and $Y$ and $Y'$ are each uniformly distributed over $T$. Let $\epsilon := P[f(X, Y) = 1]$ and $N := |T|$. Then $$P[f(X, Y) = 1 \land f(X, Y') = 1 \land Y \neq Y'] \geq \epsilon^2 - \epsilon / N.$$

### Security Against Eavesdropping

> [!definition] Honest Verifier Zero Knowledge
> Let $\mathcal I = (G, P, V)$ be an identification protocol. We say that $\mathcal I$ is **honest verifier zero knowledge**, or **HVZK** for short, if there exists an efficient probabilistic algorithm $\text{Sim}$ (called a **simulator**) such that for all possible outputs $(vk, sk)$ of $G$, the output distribution of $\text{Sim}$ on input $vk$ is identical to the distribution of a transcript of a conversation between $P$ (on input $sk$) and $V$ (on input $vk$).

> [!theorem]
> If an identification protocol $\mathcal I$ is secure against direct attacks, and is HVZK, then it is secure against eavesdropping attacks.
> 
> In particular, if $\mathcal I$ is HVZK with simulator Sim, then for every impersonation adversary $\mathcal A$ that attacks $\mathcal I$ via an [[#Security Against Eavesdropping|eavesdropping attack]], obtaining up to $Q$ transcripts, there is an adversary $\mathcal B$ that attacks $\mathcal I$ via a [[#Password Protocols|direct attack]], where $\mathcal B$ is an elementary wrapper around $\mathcal A$ (and where $\mathcal B$ runs Sim at most $Q$ times), such that $$\text{ID2adv}[\mathcal A, \mathcal I] = \text{ID1adv}[\mathcal B, \mathcal I].$$

> [!theorem]
> Schnorr's identification protocol is HVZK.

> [!theorem]
> If Schnorr's identification protocol is secure against direct attacks, then it is also secure against eavesdropping attacks.
> 
> In particular, for every impersonation adversary $\mathcal A$ that attacks $\mathcal I_{sch}$ via an [[#Security Against Eavesdropping|eavesdropping attack]], there is an adversary $\mathcal B$ that attacks $\mathcal I_{sch}$ via a [[#Password Protocols|direct attack]], where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{ID2adv}[\mathcal A, \mathcal I_{sch}] = \text{ID1adv}[\mathcal B, \mathcal I_{sch}].$$

> [!remark]
> We still don't know if Schnorr's identification protocol is secure against [[#Security Against Active Attacks|active attacks]]: there are no known effective, active attacks, but there is also no proof that rules out such an attack under the DL assumption.

## From Identification Protocols to Signatures

> [!algorithm] Schnorr Signature Scheme
> The Schnorr signature scheme is $\mathcal S_{sch} = (G, S, V)$, where:
> - The key generation algorithm $G$ runs as follows: $$\alpha \xleftarrow{R} \mathbb Z_q, u \leftarrow g^{\alpha}.$$
> The public key is $pk := u$, and the secret key is $sk := \alpha$.
> - To sign a message $m \in \mathcal M$ using a secret key $sk = \alpha$, the signing algorithm runs as follows: $$\begin{gather}S(sk, m) := \alpha_t \xleftarrow{R} \mathbb Z_q, u_t \leftarrow u^{\alpha_t}, c \leftarrow H(m, u_t), \alpha_z \leftarrow \alpha_t + \alpha c \\ \text{output } \sigma := (u_t, \alpha_z)\end{gather}$$
> - To verify a signature $\sigma = (u_t, \alpha_z)$ on a message $m \in \mathcal M$, using the public key $pk = u$, the signature verification algorithm $V$ computes $c \leftarrow H(m, u_t)$, and outputs `accept` if $g^{\alpha_z} = u_t \cdot u^c$, and outputs `reject`, otherwise.

### Repeated Impersonating Attacks

> [!algorithm] $r$-Impersonating Eavesdropping Attacks
> For a given identification protocol $\mathcal I = (G, P, V)$, positive integer $r$, and adversary $\mathcal A$, the attack runs as follows. The key generation and eavesdropping phase is exactly the same as in [[#Security Against Eavesdropping|eavesdropping attack]].
> The only difference is that in the impersonation phase, the adversary $\mathcal A$ is allowed to interact **concurrently** with up to $r$ verifiers. The challenger plays the role of these verifiers, all of which use the same verification key as generated during the key generation phase. The adversary wins the game if it makes any of these verifiers output `accept`.
> We define $\mathcal A$'s advantage with respect to $\mathcal I$ and $r$, denoted $\text{rID2adv}[\mathcal A, \mathcal I, r]$, as the probability that $\mathcal A$ wins the game.

> [!lemma]
> Let $\mathcal I$ be an identification protocol. For every $r$-impersonation eavesdropping adversary $\mathcal A$, there exists a standard eavesdropping adversary $\mathcal B$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{rID2adv}[\mathcal A, \mathcal I, r] \leq r \cdot \text{ID2adv}[\mathcal B, \mathcal I].$$

### Security Analysis of Schnorr Signatures

> [!theorem] 
> If $H$ is modeled as a random oracle and Schnorr's identification scheme is secure against eavesdropping attacks, then Schnorr's signature scheme is also secure.
> 
> In particular, let $\mathcal A$ be an adversary attacking $\mathcal S_{sch}$ as in the random oracle version Attack Game 13.1. Moreover, assume that $\mathcal A$ issues at most $Q_s$ signing queries and $Q_{ro}$ random oracle queries. Then there exists a $(Q_{ro} + 1)$-impersonating adversary $\mathcal B$ that attacks $\mathcal I_{sch}$ via an [[#Repeated Impersonating Attacks|r-impersonation eavesdropping attack]], where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{SIG}^{\text{ro}}\text{adv}[\mathcal A, \mathcal S_{sch}] \leq Q_s (Q_s + Q_{ro} + 1) / q + \text{rID2adv}[\mathcal B, \mathcal I_{sch}, Q_{ro} + 1].$$

> [!lemma]
> Consider Schnorr's identification protocol $\mathcal I_{sch}$, defined with respect to a group $\mathbb G$ of prime order $q$ generated by $g \in \mathbb G$, and with a challenge space $\mathcal C$ of size $N$. For every efficient $r$-impersonation eavesdropping adversary $\mathcal A$ attacking $\mathcal I_{sch}$, with advantage $\epsilon := \text{rID2adv}[\mathcal A, \mathcal I, r]$, there exists an efficient DL adversary $\mathcal B$ (whose running time is about twice that of $\mathcal A$), with advantage $\epsilon' := \text{DLadv}[\mathcal B, \mathbb G]$, such that $$\epsilon' \geq \epsilon^2 / r - \epsilon / N,$$ which implies $$\epsilon \leq \frac{r}{N} + \sqrt{r \epsilon'}.$$

## Sigma Protocols

> [!definition] Effective Relation
> An **effective relation** is a binary relation $\mathcal R \subset \mathcal X \times \mathcal Y$, where $\mathcal X, \mathcal Y$ and $\mathcal R$ are efficiently recognizable finite sets. Elements of $\mathcal Y$ are called **statements**. If $(x, y) \in \mathcal R$, then $x$ is called a **witness for** $y$.

> [!algorithm] Sigma Protocol
> Let $\mathcal R \subseteq \mathcal X \times \mathcal Y$ be an effective relation. A **Sigma protocol** for $\mathcal R$ is a pair $(P, V)$.
> - $P$ is an interactive protocol algorithm called the **prover**, which takes as input a witness-statement pair $(x, y) \in \mathcal R$.
> - $V$ is an interactive protocol algorithm called the **verifier**, which takes as input a statement $y \in \mathcal Y$, and which outputs `accept` or `reject`.
> - $P$ and $V$ are structured so that an interaction between them always works as follows:
> 	- To start the protocol, $P$ computes a message $t$, called the **commitment**, and sends $t$ to $V$;
> 	- Upon receiving $P$'s commitment $t$, $V$ chooses a **challenge** $c$ at random from a finite **challenge space** $\mathcal C$, and sends $c$ to $P$;
> 	- Upon receiving $V$'s challenge $c$, $P$ computes a **response** $z$, and sends $z$ to $V$;
> 	- Upon receiving $P$'s response $z$, $V$ outputs either `accept` or `reject`, which must be computed strictly as a function of the statement $y$ and the **conversation** $(t, c, z)$. In particular, $V$ does not make any random choices other than the selection of the challenge - all other computations are completely deterministic.
> 
> We require that for all $(x, y) \in \mathcal R$, when $P(x, y)$ and $V(y)$ interact with each other, $V(y)$ always outputs `accept`.

> [!definition] Accepting Conversation
> We require that the verifier computes its output as a function of the statement $y$ and its conversation $(t, c, z)$ with the prover. If the output is `accept` we call the conversation $(t, c, z)$ an **accepting conversation for** $y$.

> [!example] Schnorr's Sigma Protocol
> It should be clear that for Schnorr's identification protocol $(G, P, V)$, the pair $(P, V)$ is an example of a Sigma protocol for the relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$, where $$\mathcal X = \mathbb Z_q, \mathcal Y, \mathbb G, \text{and } \mathcal R = \{(\alpha, u) \in \mathbb Z_q \times \mathbb G: g^{\alpha} = u\}.$$ The challenge space $\mathcal C$ is a subset of $\mathbb Z_q$. We call $(P, V)$ **Schnorr's Sigma protocol**.

### Special Soundness

> [!definition] Special Soundness
> Let $(P, V)$ be a Sigma protocol for $\mathcal R \subseteq \mathcal X \times \mathcal Y$. We say that $(P, V)$ provides **special soundness** if there is an efficient deterministic algorithm $\text{Ext}$, called a **witness extractor**, with the following property: whenever $\text{Ext}$ is given as input a statement $y \in \mathcal Y$, and two accepting conversations $(t, c, z)$ and $(t, c', z')$, with $c \neq c'$, algorithm $\text{Ext}$ always outputs $x \in \mathcal X$ such that $(x, y) \in \mathcal R$ (i.e., $x$ is a witness for $y$).

### Special Honest Verifier Zero Knowledge

> [!definition] Special HVZK
> Let $(P, V)$ be a Sigma protocol for $\mathcal R \subseteq \mathcal X \times \mathcal Y$ with challenge space $\mathcal C$. We say that $(P, V)$ is **special honest verifier zero knowledge**, or **special HVZK**, if there exists an efficient probabilistic algorithm $\text{Sim}$ (called a **simulation**) that takes as input $(y, c) \in \mathcal Y \times \mathcal C$, and satisfies the following properties:
> 1. For all inputs $(y, c) \in \mathcal Y \times \mathcal C$, algorithm $\text{Sim}$ always outputs a pair $(t, z)$ such that $(t, c, z)$ is an accepting conversation for $y$;
> 2. For all $(x, y) \mathcal R$, if we compute $$c \xleftarrow{R} \mathcal C, (t, z) \xleftarrow{R} \text{Sim}(y, c),$$ then $(t, c, z)$ has the same distribution as that of a transcript of a conversation between $P(x, y)$ and $V(y)$.

### Okamoto's Protocol for Representations

> [!algorithm] Okamoto's Protocol
> - Relation: $\mathcal R = \{( (\alpha, \beta), u) \in \mathbb Z_q^2 \times \mathbb G : g^{\alpha} h^{\beta} = u\}.$
> - Challenge space $\mathcal C$: Subset of $\mathbb Z_q$.
> - The protocol $(P, V)$ runs as follows, where the prover $P$ is initialized with $((\alpha, \beta), u) \in \mathbb R$ and the verifier $V$ is initialized with $g \in \mathbb G$:
> 1. $P$ computes $$\alpha_t \xleftarrow{R} \mathbb Z_q, \beta_t \xleftarrow{R} \mathbb Z_q, u \leftarrow g^{\alpha_t} h^{\beta_t},$$ and sends the commitment $u_t$ to $V$;
> 2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends the challenge $c$ to $P$;
> 3. $P$ computes $$\alpha_z \leftarrow \alpha_t + \alpha c, \beta_z \leftarrow \beta_t + \beta c \in \mathbb Z_q,$$ and sends the response $(\alpha_z, \beta_z)$ to $V$;
> 4. $V$ checks if $g^{\alpha_z} h^{\beta_z} = u_t \cdot u^c$; if so $V$ outputs `accept`; otherwise, $V$ outputs `reject`.

> [!theorem]
> Okamoto's protocol is a Sigma protocol for the relation $\mathcal R$. Moreover, it provides special soundness and is special HVZK.

### The Chaum-Pedersen Protocol for DH-Triples

> [!algorithm] Chaum-Pedersen Protocol for DH-Triples
> - Relation: $\mathcal R = \{(\beta, (u, v, w)) \in \mathbb Z_q \times \mathbb G^3 : v = g^{\beta} \text{ and } w = u^\beta\}.$
> - Challenge space $\mathcal C$: Subset of $\mathbb Z_q$.
> - The protocol $(P, V)$ runs as follows, where the prover $P$ is initialized with $(\beta, (u, v, w)) \in \mathbb R$ and the verifier $V$ is initialized with $g, u \in \mathbb G$.
> 1. $P$ computes $$\beta_t \xleftarrow{R} \mathbb Z_q, v_t \leftarrow g^{\beta_t}, w_t \leftarrow u^{\beta_t}$$ and sends the commitment $v_t, w_t$ to $V$;
> 2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends the challenge $c$ to $P$;
> 3. $P$ computes $$\beta_z \leftarrow \beta_t + \beta c$$ and sends the response $\beta_z$ to $V$;
> 4. $V$ checks if $g^{\beta_z} = v_t \cdot v^c$ and $u^{\beta_z} = w_t \cdot w^c$.

> [!theorem]
> The Chaum-Pedersen protocol is a Sigma protocol for the relation $\mathcal R$. Moreover, it provides special soundness and is special HVZK.

### A Sigma Protocol for Arbitrary Linear Relations

> [!definition] Arbitrary Linear Relations
> Let $\mathbb G$ be a cyclic group of prime order $q$ generated by $g \mathbb G$. We shall consider boolean formulas $\phi$ of the following type: $$\phi(x_1, \dots, x_n) = \{\prod_{j = 1}^n g_{1j}^{x_j} = u_1 \land \cdots \land \prod_{j = 1}^n g_{mj}^{x_j} = u_m\}.$$

> [!algorithm] Generic Linear Protocol
> - Relation: $\mathcal R = \{((\alpha_1, \dots, \alpha_n), \phi) \in \mathbb Z_q^n \times \mathcal F: \phi(\alpha_1, \dots, \alpha_n) = true\}$.
> - Challenge space $\mathcal C$: Subset of $\mathbb Z_q$.
> - The protocol $(P, V)$ runs as follows, where the prover $P$ is initialized with $((\alpha_1, \dots, \alpha_n), \phi)$ and the verifier $V$ is initialized with $g$.
> 1. $P$ computes $\alpha_{t j} \xleftarrow{R} \mathbb Z_q (j = 1, \dots, n)$, $u_{ti} \leftarrow \prod_{j = 1}^n g_{i j}^{\alpha_{i j}} (i = 1, \dots, m)$ and sends the commitment $u_{t1}, \dots, u_{tm} \in \mathbb G$ to $V$;
> 2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends the challenge $c$ to $P$;
> 3. $P$ computes $$\alpha_{z j} \leftarrow \alpha_{t j} + \alpha_{j} c \quad (j = 1, \dots, n)$$ and sends the response $\alpha_{z 1}, \dots, \alpha_{z n} \in \mathbb Z_q$ to $V$.
> 4. $V$ checks if $\prod_{j = 1}^n g_{i j}^{\alpha_{z j}} = u_{i j} \cdot u_i^c \quad (i = 1, \dots, m)$.

> [!remark]
> - Schnorr's protocol is a special case with $\phi_1(x) := \{u = g^x\}$.
> - Okamoto's protocol is a special case with $\phi_2(x, y) := \{u = g^x h^y\}$.
> - The Chaum-Pederson protocol is a special case with $\phi_3(x) := \{v = g^x \land w = u^x\}$.

> [!theorem]
> The generic linear protocol is a Sigma protocol for the relation $\mathcal R$. Moreover, it provides special soundness and is special HVZK.

### A Sigma Protocol for the Pre-Image of a Homomorphism

> [!algorithm] Pre-Image of a Homomorphism Sigma Protocol
> - Relation: $\mathcal R = \{ (\alpha, (u, \psi)) \in \mathbb H_1 \times (\mathbb H_2 \times \mathcal F) : \psi(\alpha) = u\}$ where $\mathbb H_1$ and $\mathbb H_2$ be two finite abelian groups of known order and let $\psi: \mathbb H_1 \rightarrow \mathbb H_2$ be a group homomorphism.
> - The challenge space $\mathcal C$ is $\{0, 1, \dots, N - 1\} \subseteq \mathbb Z$ for some integer $N$.
> - The protocol $(P, V)$ runs as follows, where the prover $P$ is initialized with $(\alpha, (u, \psi))$ and the verifier $V$ is initialized with $g$.
> 1. $P$ computes $\alpha_t \xleftarrow{R} \mathbb H_1, u_1 \leftarrow \psi(\alpha_t)$ and sends the commitment $u_t \in \mathbb H_2$ to $V$.
> 2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends the challenge $c$ to $P$;
> 3. $P$ computes $\alpha_z \leftarrow \alpha_t + \alpha \cdot c \in \mathbb H_1$ and sends the response $\alpha_z \in \mathbb H_1$ to $V$.
> 4. $V$ checks if $\psi(\alpha_z) = u_t \cdot u^c$.

> [!theorem]
> The homomorphism protocol above is a Sigma protocol for the relation $\mathcal R$. Moreover, it is special HVZK, and provides special soundness whenever the smallest prime factor of $|\mathbb H_1| \times |\mathbb H_2|$ is at least $|\mathcal C|$.

### A Sigma Protocol for RSA

> [!algorithm] Guillou-Quisquater (GQ) Protocol
> - Relation: $\mathcal R = \{(x, y) \in \mathbb Z_n^* \times \mathbb Z_n^* : x^e = y\}$.
> - The challenge space $\mathcal C$ is $\{0, \dots, e - 1\}$.
> - The protocols $(P, V)$ runs as follows, where prover $P$ is initialized with $(x, y)$ and the verifier $V$ is initialized with $e$.
> 1. $P$ computes $x_t \xleftarrow{R} \mathbb Z_n^*, y_t \leftarrow x_t^e$ and sends the commitment $y_t$ to $V$.
> 2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends the challenge $c$ to $P$.
> 3. $P$ computes $x_z \leftarrow x_t \cdot x^c$, and sends the response $x_z$ to $V$.
> 4. $V$ checks if $x_z^e = y_t \cdot y^c$.

> [!theorem]
> The GQ protocol is a Sigma protocol for the relation $\mathcal R$. Moreover, it provides special soundness and is special HVZK.

## Identification and Signatures from Sigma Protocols

> [!definition] Key Generation Algorithm
> Suppose we have a Sigma protocol $(P, V)$ for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$. In addition to $P$ and $V$, we need a **key generation algorithm for** $\mathcal R$. This is a probabilistic algorithm $G$ that generates a public-key/secret-key pair $(pk, sk)$, where $pk = y$ and $sk = (x, y)$ for some $(x, y) \in \mathcal R$.

> [!algorithm] One-way Key generation
> Let $G$ be a key generation algorithm for $\mathcal R \subseteq \mathcal X \times \mathcal Y$. For a given adversary $\mathcal A$, the attack game runs as follows:
> - The challenger runs $(pk, sk) \xleftarrow{R} G()$, and sends $pk = y$ to $\mathcal A$;
> - $\mathcal A$ output $\hat{x} \in \mathcal X$.
> 
> We say that the adversary wins the game if $(\hat{x}, y) \in \mathcal R$. We define $\mathcal A$'s advantage with respect to $G$, denoted $\text{OWadv}[\mathcal A, G]$, the quantity $\text{OWadv}[\mathcal A, G]$ is negligible.

> [!definition] One Way Key Generation
> We say that a key generation algorithm $G$ is **one way** if for all efficient adversaries $\mathcal A$, the quantity $\text{OWadv}[\mathcal A, G]$ is negligible.

> [!theorem]
> Let $(P, V)$ be a Sigma protocol for an effective relation $\mathcal R$ with a large challenge space. Let $G$ be a key generation algorithm for $\mathcal R$. If $(P, V)$ provides special soundness and $G$ is one-way, then the identification scheme $\mathcal I = (G, P, V)$ is secure against direct attacks.
> 
> In particular, suppose $\mathcal A$ is an efficient impersonating adversary attacking $\mathcal I$ via a [[#Password Protocols|direct attack]], with advantage $\epsilon = \text{ID1adv}[\mathcal A, \mathcal I]$. Then there exists an efficient adversary $\mathcal B$ attacking $G$ as in [[#Identification and Signatures from Sigma Protocols|one-way key generation]], with advantage $\epsilon' = \text{OWadv}[\mathcal B, G]$, such that $$\epsilon' \geq \epsilon^2 - \epsilon / N,$$ where $N$ is the size of the challenge space, which implies $$\epsilon \leq \frac{1}{N} + \sqrt{e'}.$$

> [!theorem]
> Let $(P, V)$ be a Sigma protocol for an effective relation $\mathcal R$. Let $G$ be a key generation algorithm for $\mathcal R$. If the identification protocol $\mathcal I = (G, P, V)$ is secure against direct attacks, and $(P, V)$ is special HVZK, then $\mathcal I$ is also secure against eavesdropping attacks.
> 
> In particular, for every impersonating adversary $\mathcal A$ that attacks $\mathcal I$ via an [[#Security Against Eavesdropping|eavesdropping attack]], there is an adversary $\mathcal B$ that attacks $\mathcal I$ via a [[#Password Protocols|direct attack]], where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{ID2adv}[\mathcal A, \mathcal I] = \text{ID1adv}[\mathcal B, \mathcal I].$$

### The Fiat-Shamir Heuristic for Signatures

> [!algorithm] Fiat-Shamir Signature Scheme
> Building Block:
> - A Sigma protocol $(P, V)$ for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$; we assume that conversations are of the form $(t, c, z)$, where $t \in \mathcal T, c \in \mathcal C$, and $z \in \mathcal Z$;
> - A key generation algorithm $G$ for $\mathcal R$;
> - A hash function $H: \mathcal M \times \mathcal T \rightarrow \mathcal C$, which will be modeled as a random oracle; the set $\mathcal M$ will be the message space of the signature scheme.
> 
> The **Fiat-Shamir signature scheme** derived from $G$ and $(P, V)$ works as follows:
> - The key generation algorithm is $G$, so a public key is of the form $pk = y$, where $y \in \mathcal Y$, and a secret key is of the form $sk = (x, y) \in \mathcal R$.
> - To sign a message $m \in \mathcal M$ using the secret key $sk = (x, y)$, the signing algorithm runs as follows:
> 	- It starts the prover $P(x, y)$, obtaining a commitment $t \in \mathcal T$;
> 	- It computes a challenge $c \leftarrow H(m, t)$;
> 	- Finally, it feeds $c$ to the prover, obtaining a response $z$, and outputs the signature $\sigma = (t, z) \in \mathcal T \times \mathcal Z$.
> - To verify a signature $\sigma = (t, z) \in \mathcal T \times \mathcal Z$ on a message $m \in \mathcal M$ using a public key $pk = y$, the verification algorithm computes $c \leftarrow H(m, t)$, and checks that $(t, c, z)$ is an accepting conversation for $y$.

> [!definition] Unpredictable Commitments
> Let $(P, V)$ be a Sigma protocol for $\mathcal R \subseteq \mathcal X \times \mathcal Y$, and suppose that all conversations $(t, c, z)$ lie in $\mathcal T \times \mathcal C \times \mathcal Z$. We say that $(P, V)$ has **$\delta$-unpredictable commitments** if for every $(x, y) \in \mathcal R$ and $\hat{t} \in \mathcal T$, with probability at most $\delta$, an interaction between $P(x, y)$ and $V(y)$ produces a conversation $(t, c, z)$ with $t = \hat{t}$. We say that $(P, V)$ has **unpredictable commitments** if it is has $\delta$-unpredictable commitments for negligible $\delta$.

> [!theorem]
> If $H$ is modeled as a random oracle, the identification scheme $\mathcal I = (G, P, V)$ is secure against eavesdropping attacks, and $(P, V)$ has unpredictable commitments, then the Fiat Shamir signature scheme $\mathcal S$ derived from $G$ and $(P, V)$ is secure.
> 
> In particular, let $\mathcal A$ be an adversary attacking $\mathcal S$ as in the 
