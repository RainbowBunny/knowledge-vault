
| Term                                 | Reference                                           |                 |
| ------------------------------------ | --------------------------------------------------- | --------------- |
| Attack Game 11.1 (Semantic Security) | [[#Semantic Security\|semantic security]]           | $\text{SSadv}$  |
| Attack Game 11.2 (CPA Security)      | [[#Chosen Plaintext Attack Security\|CPA security]] | $\text{CPAadv}$ |
## Basic Definition

> [!definition] Public-key Encryption Scheme
> A **public-key encryption scheme** $\mathcal E = (G, E, D)$ is a triple of efficient algorithms: a **key generation algorithm** $G$, an **encryption algorithm** $E$, a **decryption algorithm** $D$.
> - $G$ is a probabilistic algorithm that is invoked as $(pk, sk) \xleftarrow{R} G()$, where $pk$ is called a **public key** and $sk$ is called a **secret key**.
> - $E$ is a probabilistic algorithm that is invoked as $c \xleftarrow{R} E(pk, m)$, where $pk$ is a public key (as output by $G$), $m$ is a message, and $c$ is a ciphertext.
> - $D$ is a deterministic algorithm that is invoked as $m \leftarrow D(sk, c)$, where $sk$ is a secret key (as output by $G$), $c$ is a ciphertext, and $m$ is either a message, or a special `reject` value (distinct from all messages).
> - As usual, we require that decryption undoes encryption; specifically, for all possible outputs $(pk, sk)$ of $G$, and all messages $m$, we have $$P[D(sk, E(pk, m)) = m] = 1$$
> - Messages are assumed to lie in some finite **message space** $\mathcal M$, and ciphertexts in some finite **ciphertext space** $\mathcal C$. We say that $\mathcal E = (G, E, D)$ is defined over $(\mathcal M, \mathcal C)$.

> [!algorithm] Public-key Encryption Scheme (Mathematical Detail)
> A **public-key encryption scheme** consists of three algorithms, $G$, $E$, and $D$, along with two families of spaces with system parameterization $P$: $$M = \{\mathcal M_{\lambda, \Lambda}\}_{\lambda, \Lambda} \quad \text{and} \quad C = \{\mathcal C_{\lambda, \Lambda}\}_{\lambda, \Lambda},$$
> such that
> 1. $M$ and $C$ are efficiently recognizable.
> 2. $M$ has an effective length function.
> 3. Algorithm $G$ is an efficiently probabilistic algorithm that on input $\lambda, \Lambda$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda))$, outputs a pair $(pk, sk)$, where $pk$ and $sk$ are bit strings whose lengths are always bounded by a polynomial in $\lambda$.
> 4. Algorithm $E$ is an efficiently probabilistic algorithm that on input $\lambda, \Lambda, pk, m$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(G(\lambda, \Lambda))$ for some $sk$, and $m \in \mathcal M_{\lambda, \Lambda}$, always outputs an element of $\mathcal C_{\lambda, \Lambda}$.
> 5. Algorithm $D$ is an efficiently deterministic algorithm that on input $\lambda, \Lambda, sk, c$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(G(\lambda, \Lambda))$ for some $pk$, and $c \in \mathcal C_{\lambda, \Lambda}$, outputs either an element of $\mathcal M_{\lambda, \Lambda}$, or a special symbol $\text{reject} \notin \mathcal M_{\lambda, \Lambda}$.
> 6. For all $\lambda, \Lambda, pk, sk, m, c$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(G(\lambda, \Lambda)), k \in \mathcal K_{\lambda, \Lambda}, m \in \mathcal M_{\lambda, \Lambda}$ and $c \in \text{Supp}(E(\lambda, \Lambda; pk, m))$, we have $D(\lambda, \Lambda; sk, c) = m$.

### Semantic Security

> [!algorithm] Semantic Security
> For a given public-key encryption scheme $\mathcal E = (G, E, D)$, defined over $(\mathcal M, \mathcal C)$, for a given adversary $\mathcal A$, we define two experiments.
> **Experiment $b (b = 0, 1)$**:
> - The challenger computes $(pk, sk) \xleftarrow{R} G()$, and sends $pk$ to the adversary.
> - The adversary computes $m_0, m_1 \in \mathcal M$, of the same length, and sends them to the challenger.
> - The challenger computes $c \xleftarrow{R} E(pk, m_b)$, and sends $c$ to the adversary.
> - The adversary outputs a bit $\hat{b} \in \{0, 1\}$.
> 
> If $W_b$ is the event that $\mathcal A$ outputs 1 in Experiment $b$, we define $\mathcal A$'s **advantage** with respect to $\mathcal E$ as $$\text{SSadv}[\mathcal A, \mathcal E] = |P[W_0] - P[W_1]|.$$

> [!definition] Semantic Security
> A public-key encryption scheme $\mathcal E$ is **semantically secure** if for all efficient adversaries $\mathcal A$, the value $\text{SSadv}[\mathcal A, \mathcal E]$ is negligible.

### Chosen Plaintext Attack Security

> [!algorithm] CPA Security
> For a given public-key encryption scheme $\mathcal E = (G, E, D)$, defined over $(\mathcal M, \mathcal C)$, and for a given adversary $\mathcal A$, we define two experiments.
> **Experiment $b (b = 0, 1)$**:
> - The challenger computes $(pk, sk) \xleftarrow{R} G()$, and sends $pk$ to the adversary.
> - The adversary submits a sequence of queries to the challenger.
> For $i = 1, 2, \dots$, the $i$-th query is a pair of messages, $m_{i0}, m_{i1} \in \mathcal M$, of the same length.
> The challenger computes $c_i \xleftarrow{R} E(pk, m_{ib})$, and sends $c_i$ to the adversary.
> - The adversary outputs a bit $\hat{b} \in \{0, 1\}$.
> 
> If $W_b$ is the event that $\mathcal A$ outputs 1 in Experiment $b$, then we define $\mathcal A$'s **advantage** with respect to $\mathcal E$ as $$\text{CPAadv}[\mathcal A, \mathcal E] = |P[W_0] - P[W_1]|.$$

> [!definition] CPA Security
> A public-key encryption scheme $\mathcal E$ is called **semantically secure against chosen plaintext attack**, or simply **CPA secure**, if for all efficient adversaries $\mathcal A$, the value $\text{CPAadv}[\mathcal A, \mathcal E]$ is negligible.

 > [!theorem]
 > If a public-key encryption scheme $\mathcal E$ is semantically secure, then it is also CPA secure.
 > 
 > In particular, for every [[#Chosen Plaintext Attack Security|CPA security]] adversary $\mathcal A$ with respect to $\mathcal E$, and which makes at most $Q$ queries to its challenger, there exists an [[#Semantic Security|semantic security]] adversary $\mathcal B$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{CPAadv}[\mathcal A, \mathcal E] = Q \cdot \text{SSadv}[\mathcal B, \mathcal E].$$

## Construction

### Based on a Trapdoor Function Scheme

> [!algorithm] PKE by Trapdoor Function Scheme
> Component of $\mathcal E_{TDF}$:
> - A trapdoor function scheme $\mathcal T = (G, F, I)$, defined over $(\mathcal X, \mathcal Y)$,
> - A symmetric cipher $\mathcal E_s = (E_s, D_s)$, defined over $(\mathcal K, \mathcal M, \mathcal C)$,
> - A hash function $H: \mathcal X \rightarrow \mathcal K$.
> 
> Message space for $\mathcal E_{TDF}$ is $\mathcal M$, ciphertext space is $\mathcal Y \times \mathcal C$.
> - The key generation algorithm for $\mathcal E_{TDF}$ is the key generation algorithm for $\mathcal T$.
> - For a given public key $pk$, and a given message $m \in \mathcal M$, the encryption algorithm runs as follows: $$E(pk, m) = x \xleftarrow{R} \mathcal X, y \leftarrow F(pk, x), k \leftarrow H(x), c \xleftarrow{R} E_s(k, m), \text{output } (y, c)$$
> - For a given secret key $sk$, and a given ciphertext $(y, c) \in \mathcal Y \times \mathcal C$, the decryption algorithm runs as follows: $$D(sk, (y, c)) = x \leftarrow I(sk, y), k \leftarrow H(x), m \leftarrow D_s(k, c), \text{output } m.$$
> 
> Thus $\mathcal E_{TDF} = (G, E, D)$, and is defined over $(\mathcal M, \mathcal Y \times \mathcal C)$.

> [!theorem] 
> Assume $H: \mathcal X \rightarrow \mathcal K$ is modeled as a random oracle. If $\mathcal T$ is one-way and $\mathcal E_s$ is semantically secure, then $\mathcal E_{TDF}$ is semantically secure.
> 
> In particular, for every [[#Semantic Security|semantic security]] adversary $\mathcal A$ that attacks $\mathcal E_{TDF}$, there exists an [[#One-way Security|inverting]] adversary $\mathcal B_{ow}$ that attacks $\mathcal T$, and an [[#Semantic Security|semantic security]] adversary $\mathcal B_s$ that attacks $\mathcal E_s$, where $\mathcal B_{ow}$ and $\mathcal B_s$ are elementary wrappers around $\mathcal A$, such that $$\text{SS}^{ro}\text{adv}[\mathcal A, \mathcal E_{TDF}] \leq 2 \cdot \text{OWadv}[\mathcal B_{ow}, \mathcal T] + \text{SSadv}[\mathcal B_s, \mathcal E_s]$$

## Case Study

### RSA Trapdoor Function Scheme

> [!algorithm] RSA Trapdoor Function Scheme
> The basic RSA encryption scheme is $\mathcal E_{RSA} = (G, E, D)$, with message space $\mathcal M$ and ciphertext space $\mathcal X \times \mathcal C$, where
> - The key generation algorithm runs as follows: $$G() = (n, d) \xleftarrow{R} \text{RSAGen}(\ell, e), pk \leftarrow (n, e), sk \leftarrow (n, d), \text{output } (pk, sk);$$
> - For a given public key $pk = (n, e)$, and message $m \in \mathcal M$, the encryption algorithm runs as follows: $$E(pk, m) = x \xleftarrow{R} \mathbb Z_n, y \leftarrow x^e, k \leftarrow H(x), c \xleftarrow{R} E_s(k, m), \text{output } (y, c) \in \mathcal X \times \mathcal C'$$
> - For a given secret key $sk = (n, d)$, and a given ciphertext $(y, c) \in \mathcal X \times \mathcal C$, where $y$ represents an element of $\mathbb Z_n$, the decryption algorithm runs as follows: $$D(sk, (y, c)) = x \leftarrow y^d, k \leftarrow H(x), m \leftarrow D_s(k, c), \text{output } m.$$

> [!theorem]
> Assume $H : \mathcal X \rightarrow \mathcal K$ is modeled as a random oracle. If the RSA assumption holds for parameters $(\ell, e)$, and $\mathcal E_s$ is semantically secure, then $\mathcal E_{RSA}$ is semantically secure.
> 
> In particular, for any [[#Semantic Security|semantic security]] $\mathcal A$ that attacks $\mathcal E_{RSA}$, there exist an RSA adversary $\mathcal B_{rsa}$ that breaks the [[Trapdoor Functions#A Trapdoor Permutation Scheme Based on RSA|RSA assumption]] for $(\ell, e)$, and an [[#Semantic Security|semantic security]] adversary $\mathcal B_s$ that attacks $\mathcal E_s$, where $\mathcal B_{rsa}$ and $\mathcal B_s$ are elementary wrappers around $\mathcal A$, such that $$\text{SS}^{ro}\text{adv}^*[\mathcal A, \mathcal E_{RSA}] \leq \text{RSAadv}[\mathcal B_{RSA}, \ell, e] + \text{SSadv}^*[\mathcal B_s, \mathcal E_s].$$

### ElGamal Encryption

> [!algorithm] ElGamal Encryption
> Components of ElGamal encryption:
> - A cyclic group $\mathbb G$ of prime order $q$ with generator $g \in \mathbb G$,
> - A symmetric cipher $\mathcal E_s = (E_s, D_s)$, defined over $(\mathcal K, \mathcal M, \mathcal C)$,
> - A hash function $H: \mathbb G^2 \rightarrow \mathcal K$.
> The key generation, encryption, and decryption algorithms for $\mathcal E_{EG}$.
> - The key generation algorithm runs as follows: $$\begin{align} G() = \quad &\alpha \xleftarrow{R} \mathbb Z_q, u \leftarrow g^\alpha, \\ &pk \leftarrow u, sk \leftarrow \alpha \\ &\text{output }(pk, sk); \end{align}$$
> - For a given public key $pk = u \in \mathbb G$ and message $m \in \mathcal M$, the encryption algorithm runs as follows:
> $$E(pk, m) = \beta \xleftarrow{R} \mathbb Z_q, v \leftarrow g^\beta, w \leftarrow u^\beta, k \leftarrow H(v, w), c \leftarrow E_s(k, m), \text{output } (v, c);$$
> - For a given secret key $sk = \alpha \in \mathbb Z_q$ and a ciphertext $(v, c) \in \mathbb G \times \mathcal C$, the decryption algorithm runs as follows: $$D(sk, (v, c)) = w \leftarrow v^\alpha, k \leftarrow H(v, w), m \leftarrow D_s(k, c), \text{output } m.$$
> 
> Thus, $\mathcal E_{EG} = (G, E, D)$, and is defined over $(\mathcal M, \mathbb G \times \mathcal C)$.

> [!theorem]
> Assume $H: \mathbb G^2 \rightarrow \mathcal K$ is modeled as a random oracle. If the CDH assumption holds for $\mathbb G$, and $\mathcal E_s$ is semantically secure, then $\mathcal E_{EG}$ is semantically secure.
> 
> In particular, for every [[#Semantic Security|semantic security]] adversary $\mathcal A$ with respect to $\mathcal E_{EG}$, and makes at most $Q$ queries to the random oracle, there exist a [[Key Exchange#Computational Diffie-Hellman|computational Diffie-Hellman]] adversary $\mathcal B_{cdh}$ with respect to $\mathbb G$, and an [[#Semantic Security|semantic security]] adversary $\mathcal B_s$ with respect to $\mathcal E_s$, where $\mathcal B_{cdh}$ and $\mathcal B_s$ are elementary wrappers around $\mathcal A$, such that $$\text{SS}^{ro}\text{adv}[\mathcal A, \mathcal E_{EG}] \leq 2Q \cdot \text{CDHadv}[\mathcal B_{cdh}, \mathbb G] + \text{SSadv}[\mathcal B_s, \mathcal E_s].$$

### Lattice-Based Instantiation

> [!algorithm] Lattice-Based Instatiation
> - $\text{Setup}$
> 	- $\tau$: $\ell_{\infty}$-norm bound on all short elements in the scheme.
> 	- $q_{PKE}$: a modulus
> 	- $p < q_{PKE}$: a positive integer
> - $\text{KeyGen}()$:
> 	- Sample $A_1 \in \mathcal R_{128}^{8 \times 8}$ uniform modulo $q_{PKE}$.
> 	- Sample $S_1, S_2 \leftarrow U(\mathcal S_r^{12 \times 8})$.
> 	- Compute $A_2 = S_1 \cdot A_1 + S_2$
> 	- Set $pk = (A_1, A_2)$ and $sk = S_1$
> - $\text{Enc}(pk = (A_1, A_2), m \in \mathcal R_{128}^{12})$
> 	- Sample $s, e_1 \leftarrow U(\mathcal S_\tau^8)$, and $e_2 \leftarrow U(\mathcal S_{\tau}^{12})$
> 	- Compute $c_1 = A_1 \cdot s + e_1$
> 	- Compute $c_2 = A_2 \cdot s + e_2 + p \cdot m$
> 	- Return $ct = (c_1, c_2)$.
> - $\text{Dec}(sk = S_1, ct = (c_1, c_2))$
> 	- Compute $t = c_2 - S_1 \cdot c_1$
> 	- Return $(t - t \mod p) / p$.



