
> [!question]
> Suppose Alice and Bob share a secret key $k$. Alice wants to transmit a message $m$ to Bob over a network while maintaining the secrecy of $m$ in the presence of an eavesdropping adversary.

| Term                                                      | Reference                                                                   |                    |
| --------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------ |
| Attack Game 2.1 (Semantic Security)                       | [[#Semantic Security\|semantic security]]                                   | $\text{SSadv}$     |
| Attack Game 2.2 (Message Recovery)                        | [[#Message Recovery\|message recovery]]                                     | $\text{MRadv}$     |
| Attack Game 2.3 (Parity Prediction)                       | [[#Parity Prediction\|parity prediction]]                                   | $\text{Parityadv}$ |
| Attack Game 2.4 (Semantic Security: Bit-guessing Version) | [[#Semantic Security Bit-guessing Version\|bit guessing semantic security]] | $\text{SSadv}^*$   |
| Attack Game 3.3 (Distinguishing $P_0$ from $P_1$)         | [[#Indistinguishability]]                                                   | $\text{Distadv}$   |
| Attack Game 5.1 (Multi-key Semantic Security)             | [[#Multi-key Semantic Security\|multi-key semantic security]]               | $\text{MSSadv}$    |
| Attack Game 5.2 (CPA Security)                            | [[#Chosen Plaintext Attack Security\|CPA security]]                         | $\text{CPAadv}$    |
| Attack Game 5.3 (Nonce-based CPA Security)                | [[#Nonce-based CPA Security\|nonce-based CPA security]]                     | $\text{nCPAadv}$   |
| Attack Game 8.3 (Guessing Advantage)                      | [[#Key Derivation Problem\|guessing advantage]]                             | $\text{Guessadv}$  |
| Attack Game 9.1 (Ciphertext Integrity)                    | [[#Ciphertext Integrity\|ciphertext integrity]]                             | $\text{CIadv}$     |
| Attack Game 9.2 (Chosen Ciphertext Attack)                | [[#Chosen Ciphertext Attack Security\|CCA security]]                        | $\text{CCAadv}$    |
| One-time secure against chosen ciphertext attack          |                                                                             | $1CCAadv$          |

## Shannon Cipher and Perfect Security

> [!algorithm] Shannon Cipher
> A **Shannon cipher** is a pair $\mathcal E = (E, D)$ of functions.
> - The function $E$ (the **encryption function**) takes as input a **key** $k$ and a **message** $m$ (also called a **plaintext**), and produces as output a **ciphertext** $c$. That is, $$c = E(k, m),$$ and we say that $c$ is the **encryption of $m$ under $k$**.
> - The function $D$ (the **decryption function**) takes as input a key $m$ and a ciphertext $c$, and produces a message $m$. That is, $$m = D(k, c),$$ and we say that $m$ is the **decryption of $c$ under $k$**.
> - We require that decryption "undoes" encryption: that is, the cipher must satisfy the following **correctness property**: for all keys $k$ and all messages $m$, we have $$D(k, E(k, m)) = m.$$
> 
> To be slightly more formal, let assume $\mathcal K$ is the set of all keys (the **key space**), $\mathcal M$ is the set of all messages (the **message space**), and that $\mathcal C$ is the set of all ciphertexts (the **ciphertext space**). With this notation, we can write $$\begin{align}E: \mathcal K \times \mathcal M \rightarrow \mathcal C, \\ D: \mathcal K \times \mathcal C \rightarrow \mathcal M.\end{align}$$
> 
> Also, we shall say that $\mathcal E$ is **defined over** $(\mathcal K, \mathcal M, \mathcal C)$.

> [!algorithm] One-time Pad
> A **one-time pad** is a Shannon cipher $\mathcal E = (E, D)$, where the keys, messages, and ciphertexts are bit strings of the same length; that is, $\mathcal E$ is defined over $(\mathcal K, \mathcal M, \mathcal C)$, where $$\mathcal K = \mathcal M = \mathcal C = \{0, 1\}^L,$$ for some fixed parameter $L$. For a key $k \in \{0, 1\}^L$ and a message $m \in \{0, 1\}^L$ the encryption function is defined as follows: $$E(k, m) = k \oplus m$$ and for a key $k \in \{0, 1\}^L$ and a ciphertext $c \in \{0, 1\}^L$, the decryption function is defined as follows: $$D(k, c) = k \oplus c.$$

> [!algorithm] Variable Length One-time Pad
> A **variable length one-time pad** is a Shannon cipher $\mathcal E = (E, D)$, where the keys are bit strings of some fixed length $L$, while messages and ciphertexts are variable length bit strings, of length at most $L$. Thus, $\mathcal E$ is defined over $(\mathcal K, \mathcal M, \mathcal C)$, where $$\mathcal K = \{0, 1\}^L \quad \text{and} \quad \mathcal M = \mathcal C = \{0, 1\}^{\leq L}.$$ for some parameter $L$. For a key $k \in \mathcal K$ and a message $m \in \mathcal M$ of length $\ell$, the encryption function is defined as follows: $$E(k, m) = k[0 \dots \ell - 1] \oplus m,$$ and for a key $k \in \mathcal K$ and a ciphertext $c \in \mathcal C$ of length $\ell$, the decryption function is defined as follows: $$D(k, c) = k[0 \dots \ell - 1] \oplus c.$$

> [!algorithm] Substitution Cipher
> A **substitution cipher** is a Shannon cipher $\mathcal E = (E, D)$. Let $\Sigma$ be a finite alphabet of symbols. The message space $\mathcal M$ and the ciphertext space $\mathcal C$ are both sequences of symbols from $\Sigma$ of some fixed length $L$: $$\mathcal M = \mathcal C = \Sigma^L.$$ The key space $\mathcal K$ consists of all permutations on $\Sigma$; that is, each $k \mathcal K$ is a one-to-one function from $\Sigma$ onto itself.
> 
> Encryption of a message $m \in \Sigma^L$ under a key $k \in \mathcal K$ is defined as: $$E(k, m) = (k(m[0]), \dots, k(m[L - 1])).$$ Decryption of a ciphertext $c \in \Sigma^L$ under a key $k \in \mathcal K$ is defined as: $$D(k, c) = (k^{-1}(c[0]), \dots, k(c[L - 1])).$$

> [!algorithm] Additive One-time Pad
> Replace the encryption and decryption of one-time pad by $E(k, m) = m + k \mod n$ and $D(k, c) = c - k \mod n$.

> [!definition] Perfect Security
> Let $\mathcal E = (E, D)$ be a Shannon cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. Consider a probabilistic experiment in which the random variable $K$ is uniformly distributed over $\mathcal K$. If for all $m_0, m_1 \in \mathcal K$. If for all $m_0, m_1 \in \mathcal M$, and all $c \in \mathcal C$, we have $$P[E(K, m_0) = c] = P[E(K, m_1) = c],$$ then we say that $\mathcal E$ is a **perfect secure** Shannon cipher.

> [!theorem]
> Let $\mathcal E = (E, D)$ be a Shannon cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. The following are equivalent:
> 1. $\mathcal E$ is perfectly secure.
> 2. For every $c \in \mathcal C$, there exists an integer $N_c$ (possibly depending on $c$) such that for all $m \in \mathcal M$, we have $$|\{k \in \mathcal K : E(k, m) = c\}| = N_c.$$
> 3. If the random variable $K$ is uniformly distributed over $\mathcal K$, then each of the random variables $E(K, m)$, for $m \in \mathcal M$, has the same distribution.

> [!theorem]
> The one-time pad is a perfect secure Shannon cipher.

> [!theorem]
> Let $\mathcal E = (E, D)$ be a Shannon cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. Consider a probabilistic experiment in which $K$ is a random variable uniformly distributed over $\mathcal K$. Then $\mathcal E$ is perfectly secure if and only if for every predicate $\phi$ on $\mathcal C$, for all $m_0, m_1 \in \mathcal M$, we have $$P[\phi(E(k, m_0))] = P[\phi(E(k, m_1))].$$

> [!theorem]
> Let $\mathcal E = (E, D)$ be a Shannon cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. Consider a random experiment in which $K$ and $M$ are random variables, such that 
> - $K$ is uniformly distributed over $\mathcal K$,
> - $M$ is distributed over $\mathcal M$, and
> - $K$ and $M$ are independent.
> Define the random variable $c = E(K, M)$. Then we have:
> - If $\mathcal E$ is perfectly secure, then $C$ and $M$ are independent;
> - Conversely, if $C$ and $M$ are independent, and each message in $\mathcal M$ occurs with nonzero probability, then $\mathcal E$ is perfectly secure.

> [!theorem] Shannon's theorem
> Let $\mathcal E = (E, D)$ be a Shannon cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. If $\mathcal E$ is perfect secure, then $|\mathcal K| \geq |\mathcal M|$.

## Computational Cipher

> [!algorithm] Computational Cipher
> Let $\mathcal E = (E, D)$ be a computational cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$, where $\mathcal K$ is the key space, $\mathcal M$ is the message space, and $\mathcal C$ is the ciphertext space. We associate with $\mathcal E$ families of key, message, and ciphertext spaces, indexed by
> - A **security parameter**, which is a positive integer, and is denoted by $\lambda$, and
> - A **system parameter**, which is a bit string, and is denoted by $\Lambda$.
> 
> Thus, instead of just finite sets $\mathcal K, \mathcal M$ and $\mathcal C$, we have families of finite sets c which we view as sets of bit strings.

> [!definition] Support
> $\text{Supp}(P(\lambda))$ refer to the **support** of the distribution $P(\lambda)$, which is the set of all possible outputs of algorithm $P$ on input $\lambda$.

> [!definition] System Parameterization
> A **system parameterization** is an efficient probabilistic algorithm $P$ that given a security parameter $\lambda \in \mathbb Z_{\geq 1}$ as input, outputs a bit string $\Lambda$, called a **system parameter**, whose length is always bounded by a polynomial in $\lambda$.

> [!remark]
> A collection $S = \{\mathcal S_{\lambda, \Lambda}\}_{\lambda, \Lambda}$ of finite sets of bits strings, where $\lambda$ runs over $\mathbb Z_{\geq 1}$ and $\Lambda$ runs over $\text{Supp}(P(\lambda))$.

> [!definition] Family of Spaces with System Parameterization
> $S$ is called a **family of spaces with system parameterization** $P$, provided the lengths of all the strings in each of the sets $\mathcal S_{\lambda, \Lambda}$ are bounded by some polynomial $p$ in $\lambda$.

> [!definition] Efficiently Recognizable
> We say that $S$ is **efficiently recognizable** if there is an efficient deterministic algorithm that on input $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda))$, and $s \in \{0, 1\}^{\leq p(\lambda)}$, determines if $s \in \mathcal S_{\lambda, \Lambda}$.

> [!definition] Efficiently Sampleable
> We say that $S$ is **efficiently sampleable** if there is an efficient probabilistic algorithm that on input $\lambda \in \mathbb Z_{\geq 1}$ and $\Lambda \in \text{Supp}(P(\lambda))$, outputs an element uniform distributed over $\mathcal S_{\lambda, \Lambda}$.

> [!definition] Effective Length Function
> We say that $S$ **has an effective length function** if there is an efficient deterministic algorithm that on input $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda))$, and $s \in \mathcal S_{\lambda, \Lambda}$, outputs a non-negative integer, called the **length** of $s$.

> [!algorithm] Computational Cipher (Mathematical Detail)
> Let $\mathcal E = (E, D)$ be a computational cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$, where $\mathcal K$ is the key space, $\mathcal M$ is the message space, and $\mathcal C$ is the ciphertext space. We associate with $\mathcal E$ families of key, message, and ciphertext spaces, indexed by
> - A **security parameter**, which is a positive integer, and is denoted by $\lambda$, and
> - A **system parameter**, which is a bit string, and is denoted by $\Lambda$.
> 
> Thus, instead of just finite sets $\mathcal K, \mathcal M$ and $\mathcal C$, we have families of finite sets $$\{K = \mathcal K_{\lambda, \Lambda}\}_{\lambda, \Lambda}, \quad M = \{\mathcal M_{\lambda, \Lambda}\}_{\lambda, \Lambda}, \quad \text{and} \quad C = \{\mathcal C_{\lambda, \Lambda}\}_{\lambda, \Lambda},$$ such that 
> 1. $K, M$, and $C$ are efficiently recognizable.
> 2. $K$ is efficiently sampleable.
> 3. $M$ has an effective length function.
> 4. Algorithm $E$ is an efficient probabilistic algorithm that on input $\lambda, \Lambda, k, m$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), k \in \mathcal K_{\lambda, \Lambda}$, and $m \in \mathcal M_{\lambda, \Lambda}$, always outputs an element of $\mathcal C_{\lambda, \Lambda}$.
> 5. Algorithm $D$ is an efficient deterministic algorithm that on input $\lambda, \Lambda, k, c$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), k \in \mathcal K_{\lambda, \Lambda}$, and $c \in \mathcal C_{\lambda, \Lambda}$, outputs either an element of $\mathcal M_{\lambda, \Lambda}$, or a special symbol $\text{reject} \notin \mathcal M_{\lambda, \Lambda}$.
> 6. For all $\lambda, \Lambda, k, m, c$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), k \in \mathcal K_{\lambda, \Lambda}, m \in \mathcal M_{\lambda, \Lambda}$, and $c \in \text{Supp}(E(\lambda, \Lambda; k, m))$, we have $D(\lambda, \Lambda; k, c) = m$.

### Elementary Wrapper

> [!definition] Efficient Interactive Machine
> We say that $M$ is an **efficient interactive machine** if there exist a poly-bounded function $t$ and a negligible function $\epsilon$, such that for all environments (not even computationally unbounded ones), the probability that the total running time of $M$ exceeds $t(\lambda)$ is at most $\epsilon(\lambda)$.

> [!definition] Elementary Wrapper
> An interactive machine $M'$ is called an **efficient interface** if there exists a poly-bounded function $t$ and a negligible function $\epsilon$, such that for all $M$ (not necessarily computationally bounded), when we execute the composed machine $\langle M', M \rangle$ in an arbitrary environment (not necessarily computationally bounded), the following property holds:
> - At every point in the execution of $\langle M', M \rangle$, if $I$ is the number of interactions between $M'$ and $M$ up to at that point, and $T$ is the total running time of $M'$ up to that point, then the probability that $T > t(\lambda + I)$ is at most $\epsilon(\lambda)$.
> 
> If $M'$ is an efficient interface, and $M$ is any machine, then we say $\langle M, M' \rangle$ is an **elementary wrapper around** $M$.

## Notions of Security

### Semantic Security

> [!algorithm] Semantic Security
> For a given cipher $\mathcal E = (E, D)$, defined over $(\mathcal K, \mathcal M, \mathcal C)$, and for a given adversary $\mathcal A$, we define two experiments, Experiment 0 and Experiment 1. For $b = 0, 1,$ we define
> **Experiment $b$:**
> - The adversary computes $m_0, m_1 \in \mathcal M$, of the same length, and sends them to the challenger.
> - The challenger computes $k \xleftarrow{R} \mathcal K, c \xleftarrow{R} E(k, m_b)$, and sends $c$ to the adversary.
> - The adversary outputs a bit $\hat{b} \in \{0, 1\}$.
> 
> For $b = 0, 1,$ let $W_b$ be the event that $\mathcal A$ outputs 1 in Experiment $b$. We define $\mathcal A$'s **semantic security advantage** with respect to $\mathcal E$ as $$\text{SSadv}[\mathcal A, \mathcal E] = |P[W_0] - P[W_1]|.$$

> [!definition] Semantic Security
> A cipher $\mathcal E$ is **semantically secure** if for all efficient adversaries $\mathcal A$, the value $\text{SSadv}[\mathcal A, \mathcal E]$ is negligible.

### Message Recovery

> [!algorithm] Message Recovery
> For a given cipher $\epsilon = (E, D)$, defined over $(\mathcal K, \mathcal M, \mathcal C)$, and for a given adversary $\mathcal A$, the attack game proceeds as follows:
> - The challenger computes $m \xleftarrow{R} \mathcal M, k \xleftarrow{R} \mathcal K, c \xleftarrow{R} E(k, m)$, and sends $c$ to the adversary.
> - The adversary outputs a message $\hat{m} \in \mathcal M$.
> 
> Let $W$ be the event that $\hat{m} = m$. We say that $\mathcal A$ wins the game in this case, and we define $\mathcal A$'s **message recovery advantage** with respect to $\mathcal E$ as $$\text{MRadv}[\mathcal A, \mathcal E] = Pr[W] - 1 / |\mathcal M|.$$

> [!definition] Security Against Message Recovery
> A cipher $\mathcal E$ is **secure against message recovery** if for all efficient adversaries $\mathcal A$, the value $\text{MRadv}[\mathcal A, \mathcal E]$ is negligible.

> [!theorem]
> Let $\mathcal E = (E, D)$ be a cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. If $\mathcal E$ is semantically secure then $\mathcal E$ is secure against message recovery.

### Parity Prediction

> [!algorithm] Parity Prediction
> For a given cipher $\mathcal E = (E, D)$, defined over $(\mathcal K, \mathcal M, \mathcal C)$, and for a given adversary $\mathcal A$, the attack game proceeds as follows:
> - The challenger computes $m \xleftarrow{R} \mathcal M, k \xleftarrow{R} \mathcal K, c \xleftarrow E(k, m),$ and sends $c$ to the adversary.
> - The adversary outputs $\hat{b} \in \{0, 1\}$.
> 
> Let $W$ be the event that $\hat{b} = \text{parity}(m)$. We define $\mathcal A$'s **parity prediction advantage** with respect to $\mathcal E$ as $$\text{Parityadv}[\mathcal A, \mathcal E] = |P[W] - 1/2|.$$

> [!definition] Parity Prediction
> A cipher $\mathcal E$ is **secure against parity prediction** if for all efficient adversaries $\mathcal A$, the value $\text{Parityadv}[\mathcal A, \mathcal E]$ is negligible.

> [!theorem]
> Let $\mathcal E = (E, D)$ be a cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$, and $\mathcal M = \{0, 1\}^L$. If $\mathcal E$ is semantically secure, then $\mathcal E$ is secure against parity prediction.

### Semantic Security: Bit-guessing Version

> [!algorithm] Semantic Security: Bit-guessing Version
> For a given cipher $\mathcal E = (E, D)$, defined over $(\mathcal K, \mathcal M, \mathcal C)$, and for a given adversary $\mathcal A$, the attack game runs as follows:
> - The adversary computes $m_0, m_1 \in \mathcal M$, of the same length, and sends them to the challenger.
> - The challenger computes $b \xleftarrow{R} \{0, 1\}, k \xleftarrow{R} \mathcal K, c \xleftarrow{R} E(k, m_b)$, and sends $c$ to the adversary.
> - The adversary output a bit $\hat{b} \in \{0, 1\}$.
> 
> We say that $\mathcal A$ **wins** the game if $\hat{b} = b$.

> [!definition] Bit-guessing Semantic Security
> As any adversary can win the game with probability 1/2, we want to know how much better than random guessing an adversary can do. If $W$ denotes the event that adversary wins the game, we are interested in $\text{SSadv}^*[\mathcal A, \mathcal E] = |P[W] - 1/2|$.

> [!theorem]
> For every cipher $\mathcal E$ and every adversary $\mathcal A$, we have $$\text{SSadv}[\mathcal A, \mathcal E] = 2 \cdot \text{SSadv}^*[\mathcal A, \mathcal E]$$

### Indistinguishability

> [!algorithm] Distinguishing $P_0$ from $P_1$
> For given probability distributions $P_0$ and $P_1$ on a finite set $\mathcal R$, and for a given adversary $\mathcal A$, we define two experiments, Experiment 0 and Experiment 1. For $b = 0, 1$, we define:
> **Experiment $b$**:
> - The challenger computes $x$ as follows:
> $$x \xleftarrow{R} P_b$$
> and sends $x$ to the adversary.
> - Given $x$, the adversary computes and outputs a bit $\hat{b} \in \{0, 1\}$.
> 
> For $b = 0, 1$, let $W_b$ be the event that $\mathcal A$ outputs 1 in Experiment $b$. We define $\mathcal A$'s **advantage** with respect to $P_0$ and $P_1$ as $$\text{Distadv}[\mathcal A, P_0, P_1] = |P[W_0] - P[W_1]|.$$

> [!definition] Computational Indistinguishability
> Distribution $P_0$ and $P_1$ are called **computational indistinguishable** if the value $\text{Distadv}[\mathcal A, P_0, P_1]$ is negligible for all efficient adversaries $\mathcal A$.

> [!definition] Statistical Distance
> Suppose $P_0$ and $P_1$ are probability distributions on a finite set $\mathcal R$. Then their **statistical distance** is defined as $$\Delta[P_0, P_1] = \frac{1}{2} \sum_{r \in \mathcal R} |P_0(r) - P_1(r)|.$$

> [!theorem]
> Let $P_0$ and $P_1$ be probability distributions on a finite set $\mathcal R$. Then we have $$\max_{\mathcal R' \subseteq \mathcal R}|P_0[\mathcal R'] - P_1[\mathcal R']| = \Delta[P_0, P_1],$$
> where the maximum is taken over all subsets $\mathcal R'$ of $\mathcal R$.

> [!theorem]
> Let $P_0$ and $P_1$ be probability distributions on a finite set $\mathcal R$. Then for every adversary $\mathcal A$, we have $$\text{Distadv}[\mathcal A, P_0, P_1] \leq \Delta[P_0, P_1].$$

> [!definition] Statistical Indistinguishability
> Let $P_0$ and $P_1$ be probability distributions on a finite set $\mathcal R$. We say that $P_0$ and $P_1$ are **statistical indistinguishability** if the statistical distance $\Delta[P_0, P_1]$ is negligible.

> [!corollary]
> Let $P_0$ and $P_1$ be probability distributions on a finite set $\mathcal R$. If $P_0$ and $P_1$ are statistically indistinguishable, then they are also computationally indistinguishable.

> [!theorem]
> If $\mathcal S$ and $\mathcal T$ are finite sets, $X$ and $Y$ are random variables taking values in $\mathcal S$, and $f: \mathcal S \rightarrow \mathcal T$ is a function, then $\Delta[f(X), f(Y)] \leq \Delta [X, Y]$.
 
### Multi-key Semantic Security

> [!algorithm] Multi-key Semantic Security
> For a given cipher $\mathcal E = (E, D)$, defined over $(\mathcal K, \mathcal M, \mathcal C)$, and for a given adversary $\mathcal A$, we define two experiments, Experiment 0 and Experiment 1. For $b = 0, 1$, we define
> **Experiment $b$:**
> - The adversary submits a sequence of queries to the challenger.
> 	For $i = 1, 2, \dots$, the $i$-th query is a pair of messages, $m_{i0}, m_{i1} \in \mathcal M$, of the same length.
> 	 The challenger computes $k_i \xleftarrow{R} \mathcal K, c_i \xleftarrow{R} E(k_i, m_{ib})$, and sends $c_i$ to the adversary.
> - The adversary outputs a bit $\hat{b} \in \{0, 1\}$.
> For $b = 0, 1$, let $W_b$ be the event that $\mathcal A$ outputs 1 in Experiment $b$. We define $\mathcal A$'s **advantage** with respect to $\mathcal E$ as $$\text{MSSadv}[\mathcal A, \mathcal E] = |P[W_0] - P[W_1]|.$$

> [!definition] Multi-key Semantic Security
> A cipher $\mathcal E$ is called **multi-key semantically secure** if for all efficient adversaries $\mathcal A$, the value $\text{MSSadv}[\mathcal A, \mathcal E]$ is negligible.

> [!theorem]
> If a cipher $\mathcal E$ is semantically secure, it is also multi-key semantically secure.
> 
> In particular, for every [[#Multi-key Semantic Security|multi-key semantic security]] adversary $\mathcal A$ that attacks $\mathcal E$, and which makes at most $Q$ queries to its challenger, there exists an [[#Semantic Security|semantic security]] adversary $\mathcal B$ that attacks $\mathcal E$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{MSSadv}[\mathcal A, \mathcal E] = Q \cdot \text{SSadv}[\mathcal B, \mathcal E].$$

### Chosen Plaintext Attack Security

> [!algorithm] CPA Security
> For a given cipher $\mathcal E = (E, D)$, defined over $(\mathcal K, \mathcal M, \mathcal C)$, and for a given adversaries $\mathcal A$, we define two experiments, Experiment 0 and Experiment 1. For $b = 0, 1$, we define
> **Experiment $b$:**
> - The challenger selects $k \xleftarrow{R} \mathcal K$.
> - The adversary submits a sequence of queries to the challenger.
> 	For $i = 1, 2, \dots$, the $i$-th query is a pair of messages, $m_{i0}, m_{i1} \in \mathcal M$, of the same length.
> 	The challenger computes $c_i \xleftarrow{R} E(k, m_{ib})$, and sends $c_i$ to the adversary.
> - The adversary outputs a bit $\hat{b} \in \{0, 1\}$.
> For $b = 0, 1$, let $W_b$ be the event that $\mathcal A$ outputs 1 in Experiment $b$. We define $\mathcal A$'s **advantage** with respect to $\mathcal E$ as $$\text{CPAadv}[\mathcal A, \mathcal E] = |P[W_0] - P[W_1]|.$$

> [!definition] CPA security
> A cipher $\mathcal E$ is called **semantically secure against chosen plaintext attack**, or simply **CPA secure**, if for all efficient adversaries $\mathcal A$, the value $\text{CPAadv}[\mathcal A, \mathcal E]$ is negligible.

> [!remark] Bit-guessing Version
> Instead of having two separate experiments, the challenger chooses $b \in \{0, 1\}$ at random, and then runs Experiment $b$ against the adversary $\mathcal A$; we define $\mathcal A$'s **bit-guessing advantage** as $\text{CPAadv}^*[\mathcal A, \mathcal E] = |P[\hat{b} = b] - 1/2|$, and we have $$\text{CPAadv}[\mathcal A, \mathcal E] = 2 \cdot \text{CPAadv}^*[\mathcal A, \mathcal E].$$

### Nonce-based CPA Security

> [!algorithm] Nonce-based CPA Security
> For a given cipher $\mathcal E = (E, D)$, defined over $(\mathcal K, \mathcal M, \mathcal C, \mathcal N)$, and for a given adversary $\mathcal A$, we define two experiments, Experiment 0 and Experiment 1. For $b = 0, 1$, we define
> **Experiment $b$:**
> - The challenger selects $k \xleftarrow{R} \mathcal K$.
> - The adversary submits a sequence of queries to the challenger.
> For $i = 1, 2, \dots$, the $i$-th query is a pair of messages, $m_{i0}, m_{i1} \in \mathcal M$, of the same length, and a nonce $n_i \in \mathcal N \backslash \{n_1, \dots, n_{i - 1}\}$.
> The challenger computes $c_i \leftarrow E(k, m_{ib}, n_i)$, and sends $c_i$ to the adversary.
> - The adversary outputs a bit $\hat{b} \in \{0, 1\}$.
> 
> For $b = 0, 1$, let $W_b$ be the event that $\mathcal A$ outputs 1 in Experiment $b$. We define $\mathcal A$'s **advantage** with respect to $\mathcal E$ as $$\text{nCPAadv}[\mathcal A, \mathcal E] = |P[W_0] - P[W_1]|.$$

> [!definition] Nonce-based CPA Security
> A nonce-based cipher $\mathcal E$ is called **semantically secure against chosen plaintext attack**, or simply **CPA secure**, if for all efficient adversaries $\mathcal A$, the value $\text{nCPAadv}[\mathcal A, \mathcal E]$ is negligible.

### Key Derivation Problem

> [!algorithm] Guessing Advantage
> Let $P$ be a probability distribution defined on a finite set $\mathcal S$ and let $I$ be a function defined in $\mathcal S$. For a given adversary $\mathcal A$, the attack game runs as follows:
> - The challenger chooses $s$ at random according to $P$ and sends $I(s)$ to $\mathcal A$;
> - The adversary outputs a guess $\hat{s}$ for $s$, and wins the game if $\hat{s} = s$.
> 
> The probability that $\mathcal A$ wins this game is called its **guessing advantage**, and is denoted $\text{Guessadv}[\mathcal A, P, I]$.

### Ciphertext Integrity

> [!algorithm] Ciphertext Integrity
> For a given cipher $\mathcal E = (E, D)$ defined over $(\mathcal K, \mathcal M, \mathcal C)$, and a given adversary $\mathcal A$, the attack game runs as follows:
> - The challenger chooses a random $k \xleftarrow{R} \mathcal K$.
> - $\mathcal A$ queries the challenger several times. For $i = 1, 2, \dots$, the $i$-th query consists of a message $m_i \in \mathcal M$. The challenger computes $c_i \xleftarrow{R} E(k, m_i)$, and gives $c_i$ to $\mathcal A$.
> - Eventually $\mathcal A$ outputs a candidate ciphertext $c \in \mathcal C$ that is not among the ciphertexts it was given, i.e., $$c \notin \{c_1, c_2, \dots\}.$$
> 
> We say that $\mathcal A$ wins the game if $c$ is a valid ciphertext under $k$, that is, $D(k, c) \neq \text{reject}$. We define $\mathcal A$'s advantage with respect to $\mathcal E$, denoted $\text{CIadv}[\mathcal A, \mathcal E]$, as the probability that $\mathcal A$ wins the game. Finally, we say that $\mathcal A$ is a $Q$**-query adversary** if $\mathcal A$ issues at most $Q$ encryption queries.

 > [!definition] Ciphertext Integrity
 > We say that a $\mathcal E = (E, D)$ provides **ciphertext integrity**, or CI for short, if for every efficient adversary $\mathcal A$, the value $\text{CIadv}[\mathcal A, \mathcal E]$ is negligible.

> [!definition] One-time Ciphertext Integrity
> We say that a $\mathcal E = (E, D)$ provides **one-time ciphertext integrity** if for every efficient single-query adversary $\mathcal A$, the value $\text{CIadv}[\mathcal A, \mathcal E]$ is negligible.

### Chosen Ciphertext Attack Security

> [!algorithm] CCA Security
> For a given cipher $\mathcal E = (E, D)$ defined over $(\mathcal K, \mathcal M, \mathcal C)$, and for a given adversary $\mathcal A$, we define two experiments. For $b = 0, 1$, we define
> **Experiment** $b$:
> - The challenger selects $k \xleftarrow{R} \mathcal K$.
> - $\mathcal A$ then makes a series of queries to the challenger. Each query can be one of two types:
> 	- **Encryption query**: For $i = 1, 2, \dots$, the $i$-th encryption query consists of a pair of messages $(m_{i0}, m_{i1}) \in \mathcal M^2$. The challenger computes $c_i \xleftarrow{R} E(k, m_{ib})$ and sends $c_i$ to $\mathcal A$.
> 	- **Decryption query**: For $j = 1, 2, \dots$, the $j$-th decryption query consists of a ciphertext $\hat{c_j} \in \mathcal C$ that is not among the responses to the previous encryption queries, i.e., $\hat{c_j} \notin \{c_1, c_2, \dots\}$.
> 	The challenger computes $\hat{m_j} \leftarrow D(k, \hat{c_j})$, and sends $\hat{m_j}$ to $\mathcal A$.
> - At the end of the game, the adversary outputs a bit $\hat{b} \in \{0, 1\}$.
> 
> Let $W_b$ be the event that $\mathcal A$ outputs 1 in Experiment $b$ and define $\mathcal A$'s **advantage** with respect to $\mathcal E$ as $$\text{CCAadv}[\mathcal A, \mathcal E] = |P[W_0] - P[W_1]|.$$

> [!definition] CCA Security
> A cipher $\mathcal E$ is called **semantically secure against chosen ciphertext attack**, or simply **CCA-secure**, if for all efficient adversaries $\mathcal A$, the value $\text{CCAadv}[\mathcal A, \mathcal E]$ is negligible.

> [!definition] 1CCA Security
> If the adversary $\mathcal A$ is restricted to making a single encryption query, we denote its advantage by $\text{1CCAadv}[\mathcal A, \mathcal E]$. A ciphertext $\mathcal E$ is **one-time semantically secure against chosen ciphertext attack**, or simply, **1CCA-secure**, if for all efficient adversaries $\mathcal A$, the value $\text{1CCAadv}[\mathcal A, \mathcal E]$ is negligible.

## The Ideal Cipher Model

### Ideal Block Model

> [!algorithm] Ideal Block Model
> Suppose we have some type of cryptographic scheme $\mathcal S$ whose implementation makes use of a block cipher $\mathcal E = (E, D)$ defined over $(\mathcal K, \mathcal X)$. Moreover, suppose the scheme $\mathcal S$ evaluates $E$ at various inputs $(k, a) \in \mathcal K \times \mathcal X$, and $D$ at various inputs $(k, b) \in \mathcal K \times \mathcal X$, but does not look at the internal implementation of $\mathcal E$. In this case, we say that $\mathcal S$ **uses $\mathcal E$ as an oracle**.
> We wish to analyze the security of $\mathcal S$. Let us assume that whatever security property we are interested in property $X$ and an arbitrary adversary $\mathcal A$. This game defines an advantage $\text{Xadv}[\mathcal A, \mathcal S]$, and security with respect to property $X$ means that this advantage should be negligible for all efficient adversaries $\mathcal A$.
> To analyze $\mathcal S$ in the ideal cipher model, then the attack game defining security is modified so that $\mathcal E$ is effectively replaced by a family of random permutations $\{\Pi_{k}\}_{k \in \mathcal K}$ to which both the adversary and the challenger have oracle access. The game is modified as follows:
> - At the beginning of the game, the challenger chooses $\Pi_k \in \text{Perms}[\mathcal K]$ at random, for each $k \in \mathcal K$.
> - In addition to its standard queries, the adversary $\mathcal A$ may submit **ideal cipher queries**. There are two types of queries: $\Pi$-queries and $\Pi^{-1}$-queries.
> 	- For a $\Pi$-query, the adversary submits a pair $(k, a) \in \mathcal K \times \mathcal X$, to which the challenger responds with $\Pi_k(a)$.
> 	- For a $\Pi^{-1}$-query, the adversary submits a pair $(k, b) \in \mathcal K \times \mathcal X$, to which the challenger responds with $\Pi^{-1}_k(b)$.
> 
> The adversary may make any number of ideal cipher queries, arbitrarily interleaved with standard queries.
> - In processing standard queries, the challenger performs its computations using $\Pi_k(a)$ in place of $E(k, a)$ and $\Pi^{-1}_k(b)$ in place of $D(k, b)$.
> 
> The adversary's advantage is defined using the same rule as before, but is denoted $\text{X}^{ic}\text{adv}[\mathcal A, \mathcal S]$. Security in the ideal cipher model means that $\text{X}^{ic}\text{adv}[\mathcal A, \mathcal S]$ should be negligible for all efficient adversaries $\mathcal A$.

### Ideal Permutation Model

> [!algorithm] Ideal Permutation Model
> Some constructions, make use of a permutation $\pi: \mathcal X \rightarrow \mathcal X$, rather than a block cipher.

## Random Oracles

> [!algorithm] Security in the Random Oracle Model
> Suppose we have some type of cryptographic scheme $\mathcal S$ whose implementation makes use of a subroutine for computing a hash function $H$ defined over $(\mathcal M, \mathcal T)$. The scheme $\mathcal S$ evaluates $H$ at arbitrary points of its choice, but does not look at the internal implementation of $H$. We say that $\mathcal S$ **uses $H$ as an oracle**. 
> We wish to analyze the security of $\mathcal S$. Let us assume that whatever security property we are interested in property $X$ and an arbitrary adversary $\mathcal A$. This game defines an advantage $\text{Xadv}[\mathcal A, \mathcal S]$, and security with respect to property $X$ means that this advantage should be negligible for all efficient adversaries $\mathcal A$.
> If we wish to analyze $\mathcal S$ in the random oracle model, then the attack game defining security is modified so that $H$ is effectively replaced by a **random function** $\mathcal O \in \text{Funs}[\mathcal M, \mathcal T]$, to which both the adversary and the challenger have oracle access. More precisely, the game is modified as follows.
> - At the beginning of the game, the challenger chooses $\mathcal O \in \text{Funs}[\mathcal M, \mathcal T]$ at random.
> - In addition to its standard queries, the adversary $\mathcal A$ may submit **random oracle queries**: it gives $m \in \mathcal M$ to the challenger, who responds with $t = \mathcal O(m)$. The adversary may make any number of random oracle queries, arbitrarily interleaved with standard queries.
> - In processing standard queries, the challenger performs its computations using $\mathcal O$ in place of $H$.
> 
> The adversary's advantage is defined using the same rule as before, but is denoted $\text{X}^{ro}\text{adv}[\mathcal A, \mathcal S]$ to emphasize that this is an advantage **in the random oracle model**. Security **in the random oracle model** means that $\text{X}^{ro}\text{adv}[\mathcal A, \mathcal S]$ should be negligible for all efficient adversaries $\mathcal A$.

### List Guessing Advantage

> [!algorithm] List Guessing Advantage
> Generalize of [[#Key Derivation Problem|guessing advantage]] problem by output a list of guesses $\hat{s}_1, \dots, \hat{s}_Q$, where the adversary is said to win the game if $\hat{s}_i = s$ for some $i = 1, \dots, Q$. An adversary $\mathcal A$'s probability of winning in this game is called his **list guessing advantage**, denoted $\text{ListGuessadv}[\mathcal A, P, I]$.

> [!theorem]
> If $H$ is modeled as a random oracle, then for every distinguishing adversary $\mathcal A$ that makes at most $Q_{ro}$ random oracle queries, there exists a list guessing adversary $\mathcal B$, which is an elementary wrapper around $\mathcal A$, such that $$\text{Dist}^{ro}\text{adv}[\mathcal A, P, I, H] \leq \text{ListGuessadv}[\mathcal B, P, I]$$ and $\mathcal B$ outputs a list of size at most $Q_{ro}$. In particular, there exists a guessing adversary $\mathcal B'$, which is an elementary wrapper around $\mathcal A$, such that $$\text{Dist}^{ro}\text{adv}[\mathcal A, P, I, H] \leq Q_{ro} \cdot \text{Guessadv}[\mathcal B', P, I].$$
 
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

## Nonce-based CPA Secure Cipher Construction

### Nonce-based Generic Hybrid Construction

> [!algorithm] Nonce-based Generic Hybrid Construction
> Let $\mathcal E = (E, D)$ is a cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$, and $F$ is a PRF defined over $(\mathcal K', \mathcal X, \mathcal K)$. We define the nonce-based cipher $\mathcal E'$, which is defined over $(\mathcal K', \mathcal M, \mathcal C, \mathcal X)$, as follows:
> - For $k' \in \mathcal K', m \in \mathcal M$, and $x \in \mathcal X$, we define $E'(k', m, x) = E(k, m)$, where $k = F(k', x)$;
> - For $k' \in \mathcal K', c \in \mathcal C, x \in \mathcal X$, we define $D'(k', c, x) = D(k, c)$, where $k = F(k', x)$.

> [!theorem]
> If $F$ is a secure PRF and $\mathcal E$ is a semantically secure cipher, then the cipher $\mathcal E'$ described above is a CPA secure cipher.
> 
> In particular, for every [[#Nonce-based CPA Security|nonce-based CPA security]] adversary $\mathcal A$ that attacks $\mathcal E'$ which makes at most $Q$ queries to its challenger, there exists a [[Pseudo Random Function#PRF Security|secure PRF]] adversary $\mathcal B_F$ that attacks $F$ and an [[#Semantic Security|semantic security]] adversary $\mathcal B_{\mathcal E}$ that attacks $\mathcal E$, where both $\mathcal B_F$ and $\mathcal B_{\mathcal E}$ are elementary wrappers around $\mathcal A$, such that $$\text{nCPAadv}[\mathcal A, \mathcal E'] \leq 2 \cdot \text{PRFadv}[\mathcal B_F, F] + Q \cdot \text{SSadv}[\mathcal B_{\mathcal E}, \mathcal E].$$

### Nonce-based Counter Mode

> [!algorithm] Nonce-based Counter Mode
> Let assume $\ell$ divides $N$, we modify the cipher scheme in [[#Randomized Counter Mode]] by using nonce space $\{0, \dots, N / \ell - 1\}$ and translate the nonce $n$ to the PRF input $x = n \ell$.


> [!theorem]
> If $F$ is a secure PRF, then the nonce-based cipher $\mathcal E$ above is a CPA secure cipher.
> In particular, for every [[#Nonce-based CPA Security|nonce-based CPA security]] adversary $\mathcal A$ that attacks $\mathcal E$, there exists a [[Pseudo Random Function#PRF Security|secure PRF]] adversary $\mathcal B$ that attacks $F$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{CPAadv}[\mathcal A, \mathcal E] \leq 2 \cdot \text{PRFadv}[\mathcal B, F].$$

### Nonce-based CBC Mode

> [!algorithm] Nonce-based CBC Mode
> Assume that we have a PRF $F$ defined over $(\mathcal K', \mathcal N, \mathcal X)$. Here, the key space $\mathcal K'$ and input space $\mathcal N$ of $F$ may be arbitrary sets, but the output space $\mathcal X$ of $F$ must match the block space of the underlying block cipher $\mathcal E = (E, D)$, which is defined over $(\mathcal K, \mathcal X)$. In the nonce-based CBC scheme $\mathcal E'$, the key space $\mathcal K \times \mathcal K'$, and the encryption and decryption algorithms, the IV is computed from the nonce $n$ and the key $k'$ as $c[0] = F(k', n)$.

> [!theorem]
> If $\mathcal E = (E, D)$ is a secure block cipher defined over $(\mathcal K, \mathcal X)$, and $N = |\mathcal X|$ is super-poly, and $F$ is a secure PRF defined over $(\mathcal K', \mathcal N, \mathcal X)$, then for any poly-bounded $\ell \geq 1$, the nonce-based cipher $\mathcal E'$ is a CPA secure cipher.
> 
> In particular, for every [[#Nonce-based CPA Security|nonce-based CPA security]] adversary $\mathcal A$ that attack $\mathcal E'$, and which makes at most $Q$ queries to its challenger, there exists [[Block Ciphers#Secure Block Cipher|secure block cipher]] adversary $\mathcal B$ that attacks $\mathcal E$, and a [[Pseudo Random Function#PRF Security|secure PRF]] adversary $\mathcal B_F$ that attacks $F$, where $\mathcal B$ and $\mathcal B_F$ are elementary wrappers around $\mathcal A$, such that $$\text{nCPAadv}[\mathcal A, \mathcal E'] \leq \frac{2Q^2 \ell^2}{N} + 2 \cdot \text{PRFadv}[\mathcal B_F, F] + 2 \cdot \text{BCadv}[\mathcal B, \mathcal E].$$

## Example

### Anonymous Routing

