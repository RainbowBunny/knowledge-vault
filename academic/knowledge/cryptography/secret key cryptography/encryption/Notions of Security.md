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

