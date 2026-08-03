## Overview

> [!proposition] Cryptographically Secure
> In order to be useful for cryptography, a PRNG should have the following two properties:
> 1. If Eve knows the first $k$ bits of Alice's random bit string, she should have no better than a $50\%$ chance of predicting whenever the next bit will be a $0$ or a $1$. More precisely, there should not be a fast (e.g., polynomial time) algorithm that can predict the next bit with better than $50\%$ chance of success.
> 2. Suppose that Eve somehow learns part of Alice's random bit string, for example, suppose that she finds out the values of $R_t, R_{t + 1}, R_{t + 2}, \dots$. This should not help Eve to determine the earlier part $R_0, R_1, \dots, R_{t - 1}$ of Alice's string.
> A PRNG with these properties is said to be **cryptographically secure**.

| Term                                | Reference                             |                  |
| ----------------------------------- | ------------------------------------- | ---------------- |
| Attack Game 3.1 (PRG)               | [[#Secure PRG\|secure PRG]]           | $\text{PRGadv}$  |
| Attack Game 3.2 (Unpredictable PRG) | [[#Next Bit Test\|unpredictable PRG]] | $\text{Predadv}$ |

> [!definition] Pseudo-Random Generator
> A **pseudo-random generator**, or **PRG** for short, is an efficient, deterministic algorithm $G$ that, given as input a **seed** $s$, computes an output $r$. The seed $s$ comes from a finite **seed space** $\mathcal S$ and the output $r$ belongs to a finite space **output space** $\mathcal R$. We say that $G$ is a PRG defined over $(\mathcal S, \mathcal R)$.

> [!algorithm] Pseudo-Random Generator (Mathematical Detail)
> A **pseudo-random generator** consists of an algorithm $G$, along with two families of spaces with system parameterization $P$: $$S = \{\mathcal S_{\lambda, \Lambda}\}_{\lambda, \Lambda}, R = \{\mathcal R_{\lambda, \Lambda}\}_{\lambda, \Lambda},$$ such that
> 1. $S$ and $R$ are efficiently recognizable and sampleable.
> 2. Algorithm $G$ is an efficient deterministic algorithm that on input $\lambda, \Lambda, s$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda))$, and $s \in \mathcal S_{\lambda, \Lambda}$, outputs an element of $\mathcal R_{\lambda, \Lambda}$.

## Secure PRG

> [!algorithm] PRG
> For a given PRG $G$, defined over $(\mathcal S, \mathcal R)$, and for a given adversary $\mathcal A$, we define two experiments, Experiment 0 and Experiment 1. For $b = 0, 1$, we define:
> **Experiment $b$**: 
> - The challenger computes $r \in \mathcal R$ as follows:
> 	- If $b = 0: s \xleftarrow{R} \mathcal S, r \leftarrow G(s)$;
> 	- If $b = 1: r \xleftarrow R$.
> 	and sends $r$ to the adversary.
> - Given $r$, the adversary computes and outputs a bit $\hat{b} \in \{0, 1\}$.
> For $b = 0, 1$, let $W_b$ be the event that $\mathcal A$ outputs 1 in Experiment $b$. We define $\mathcal A$'s **advantage** with respect to $G$ as $$\text{PRGadv}[\mathcal A, G] = |P[W_0] - P[W_1]|.$$

> [!definition] Secure PRG
> A PRG $G$ is **secure** if the value $\text{PRGadv}[\mathcal A, G]$ is negligible for all efficient adversary $\mathcal A$.

### Next Bit Test

> [!algorithm] Unpredictable PRG
> For a given PRG $G$, defined over $(\mathcal S, \{0, 1\}^L)$, and a given adversary $\mathcal A$, the attack game proceeds as follows:
> - The adversary sends an index $i$, with $0 \leq i \leq L - 1$, to the challenger.
> - The challenger computes $$s \xleftarrow{R} \mathcal S, r \leftarrow G(s)$$ and sends $r[0 \dots i - 1]$ to the adversary.
> - The adversary outputs $g \in \{0, 1\}$.
> 
> We say that $\mathcal A$ **wins** if $r[i] = g$, and we define $\mathcal A$'s **advantage** $\text{Predadv}[\mathcal A, G]$ to be $|P[\mathcal A \text{ wins}] - 1/2|$.

> [!definition] Unpredictable PRG
> A PRG $G$ is **unpredictable** if the value $\text{Predadv}[\mathcal A, G]$ is negligible for all efficient adversaries $\mathcal A$.

> [!theorem]
> Let $G$ be a PRG, defined over $(\mathcal S, \{0, 1\}^L)$. If $G$ is secure, then $G$ is unpredictable.
> 
> In particular, for every [[#Next Bit Test|unpredictable PRG]] adversaries $\mathcal A$ of $G$, there exists an [[#Secure PRG|secure PRG]] adversary $\mathcal B$ breaking the security of $G$, where $\mathcal B$ is an elementary wrapper $\mathcal A$, such that $$\text{Predadv}[\mathcal A, G] = \text{PRGadv}[\mathcal A, G].$$

> [!lemma] Distinguisher/Predictor Lemma
> Let $X$ be a random variable taking values in some set $S$, and let $B$ and $R$ be a 0/1-valued random variables, where $R$ is uniformly distributed over $\{0, 1\}$ and is independent of $(X, B)$. Let $d : S \times \{0, 1\} \rightarrow \{0, 1\}$ be an arbitrary function, and let $$\epsilon = P[d(X, B) = 1] - P[d(X, R) = 1].$$ Define the random variable $B'$ as follows: $$B' = \begin{cases}R &\text{if } d(X, R) = 1 \\ \overline{R} &\text{otherwise}\end{cases}$$

> [!theorem]
> Let $G$ be a PRG, defined over $(\mathcal S, \{0, 1\}^L)$. If $G$ is unpredictable, then $G$ is secure.
> 
> In particular, for every [[#Secure PRG|secure PRG]] adversary $\mathcal A$ breaking the security of $G$, there exists an [[#Next Bit Test|unpredictable PRG]] adversary $\mathcal B$ breaking $G$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{PRGadv}[\mathcal A, G] = L \cdot \text{Predadv}[\mathcal B, G].$$

## Construction
### Parallel Construction

> [!algorithm] $n$-wise parallel composition
> Let $G$ be a PRG defined over $(\mathcal S, \mathcal R)$. We construct a new PRG $G'$ that applies $G$ to $n$ seeds, and concatenates the outputs. Thus, $G'$ is defined over $(\mathcal S^n, \mathcal R^n)$, and for $s_1, \dots, s_n \in \mathcal S$, $$G'(s_1, \dots, s_n) = (G(s_1, \dots, G(s_n))).$$ We call $G'$ the $n$-**wise parallel composition of** $G$. The value $n$ is called a **repetition parameter**, and we require that it is a poly-bounded value.

> [!theorem]
> If $G$ is a secure PRG, then the $n$-wise composition $G'$ of $G$ is also a secure PRG.
> 
> In particular, for every [[#Pseudo-Random Generators|secure PRG]] adversary $\mathcal A$ that attacks $G'$, there exists a [[#Pseudo-Random Generators|secure PRG]] adversary $\mathcal B$ that attacks $G$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{PRGadv}[\mathcal A, G'] = n \cdot \text{PRGadv}[\mathcal B, G].$$

### Sequential Construction

> [!algorithm] $n$-wise sequential composition
> Let $G$ be a PRG defined over $(\mathcal S, \mathcal R \times \mathcal S)$, for some finite sets $\mathcal S$ and $\mathcal R$. For every poly-bounded value $n \geq 1$, we can construct a new PRG $G'$, defined over $(\mathcal S, \mathcal R^n \times \mathcal S)$. For $s \in \mathcal S$, we let:
> $G'(s)$:
> 1. $s_0 \leftarrow s$
> 2. for $i \leftarrow 1$ to $n$ do
> 	1. $(r_i, s_i) \leftarrow G(s_{i - 1})$
> 3. output $(r_1, \dots, r_n, s_n)$.
> 
> We call $G'$ the $n$-**wise sequential composition of** $G$.

> [!theorem]
> If $G$ is a secure PRG, then the $n$-wise sequential composition $G'$ of $G$ is also a secure PRG.
> 
> In particular, for every [[#Pseudo-Random Generators|secure PRG]] adversary $\mathcal A$ with respect to $G'$, there exists a [[#Pseudo-Random Generators|secure PRG]] adversary $\mathcal B$ with respect to $G$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{PRGadv}[\mathcal A, G'] = n \cdot \text{PRGadv}[\mathcal B, G]$$

### Construction from PRFs

> [!algorithm] PRG from PRF
> Let $F$ be a PRF defined over $(\mathcal K, \mathcal X, \mathcal Y)$, let $\ell \geq 1$ be a poly-bounded value, and let $x_1, \dots, x_\ell$ be any fixed, distinct elements of $\mathcal X$ (this require $|\mathcal X| \geq \ell$). We define a PRG $G$ with seed space $\mathcal K$ and output space $\mathcal Y^\ell$, as follows: for $k \in \mathcal K$, $$G(k) = (F(k, x_1), \dots, F(k, x_\ell)).$$

> [!theorem]
> If $F$ is a secure PRF, then the PRG $G$ described above is a secure PRG.
> 
> In particular, for every [[#Secure PRG|secure PRG]] adversary $\mathcal A$ with respect to $G$, there is a [[Pseudorandom Functionsss#PRF Security|secure PRF]] adversary $\mathcal B$ with respect to $F$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{PRGadv}[\mathcal A, G] = \text{PRFadv}[\mathcal B, F].$$

## Case Study

### Salsa and ChaCha PRGs

> [!algorithm] High Level of Salsa and ChaCha PRGs
> Components:
> - A padding function denoted $\text{pad}(s, j, 0)$ that combines a 256-bit seed $s$ with a 64-bit counter $j$ to form a 512-bit block. The third input, a 64-bit nonce, is always set to 0 for now.
> - A fixed public permutation $\pi: \{0, 1\}^{512} \rightarrow \{0, 1\}^{512}$.
> These components are used to output $L < 2^{64}$ pseudorandom blocks, each 512 bits long by the algorithm:
> ---
> Input: seed $s \in \{0, 1\}^{256}$
> 1. for $j \leftarrow 0$ to $L - 1$
> 	1. $h_j \leftarrow \text{pad}(s, j, 0) \in \{0, 1\}^{512}$
> 	2. $r_j \leftarrow \pi(h_j) \oplus h_j$
> 2. output $(r_0, \dots, r_{L - 1})$.

### Linear Congruential Generator


### Subset Sum Generator


### DVD Encryption System


### Dual Elliptic Curve Deterministic Random Bit Generator (DUAL_EC_DRBG)

> [!algorithm] DUAL_EC_DRBG
> **Parameters**
> - Elliptic curve $E$ over $\mathbb F_q$
> - Public points $P, Q \in E(\mathbb F_q)$
> - Truncation parameter $t$
> 
> **State**
> - Internal scalar $s_i \in \mathbb Z_n$
> 
> **Input**
> - Current state $s_i$
> 
> **Output**
> - Pseudorandom output block $r_i$
> - Updated state $s_{i + 1}$
> ---
> Algorithm
> 1. Compute next state point $$S = s_i \cdot P$$
> 2. Update internal state $$s_{i + 1} = x(S)$$
> 3. Compute output point $$R = s_{i + 1} \cdot Q$$
> 4. Extract output bits $$r_i = \text{truncate}_t(x(R))$$
> 5. Return $(r_i, s_{})$

> [!remark] Attack With Backdoor
> The idea of this attack is assume that we can find $Q = d \cdot P$, then if at some point, we can find a specific $x(s_{i + 1} \cdot Q)$, we can recover the next state $s_{i + 1} \cdot P$ and thus continue simulating the PRNG.
> Now, the security of this algorithm is the $\text{truncate}_t$ part, if we can fill the remaining bytes of $r_i$ to get $x(R)$, then we can recover PRNG.




