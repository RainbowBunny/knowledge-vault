Reference:
- `[BS]` — D. Boneh, V. Shoup, _A Graduate Course in Applied Cryptography_, v0.6, 2023: https://toc.cryptobook.us/ (Ch. 4: Attack Games 4.1 and 4.4, the prediction game and strongly secure block ciphers in §4.1, the ideal cipher model in §4.7). `⚠️ CLAUDE – verify:` WebFetch returns only the first ~17 pages of the book, so Chapter 4 could not be read: the tables redraw the wording this note already had, and the attack-game numbers are those of the index table below.
- `[KL Def 3.28]` — J. Katz, Y. Lindell, _Introduction to Modern Cryptography_, 2nd ed., CRC Press, 2014, Definition 3.28 (strong pseudorandom permutation: the distinguisher also gets the inverse). The number is the one listed in https://www.cs.purdue.edu/homes/jblocki/courses/555_Spring21/slides/Week3.pdf; the definition itself was not read.
- `⚠️ CLAUDE – verify:` — a point I could not check against the source.

| Term                           | Reference                                     |                |
| ------------------------------ | --------------------------------------------- | -------------- |
| Attack Game 4.1 (Block Cipher) | [[#Secure Block Cipher\|secure block cipher]] | $\text{BCadv}$ |
| Attack Game 4.4 (Key Recovery) | [[#Key Recovery\|key recovery]]               | $\text{KRadv}$ |

## Definition

> [!definition] Block Cipher
> A **block cipher** is a deterministic cipher $\mathcal E = (E, D)$ whose message space and ciphertext space are the same (finite) set $\mathcal X$. If the key space of $\mathcal E$ is $\mathcal K$, we say that $\mathcal E$ is a block cipher **defined over $(\mathcal K, \mathcal X)$**. We call an element $x \in \mathcal X$ a **data block**, and refer to $\mathcal X$ as the **data block space** of $\mathcal E$.

### Secure Block Cipher

> [!definition] Parameters
> - $\mathcal E = (E, D)$: a block cipher defined over $(\mathcal K, \mathcal X)$.
> - $\text{Perms}[\mathcal X]$: the set of all permutations of $\mathcal X$.
> - $Q$: the maximal number of queries.

> [!definition] Secure Block Cipher
> ### Scope
> A block cipher $\mathcal E$ and all efficient adversaries.
>
> ---
> ### Condition
> - **Access** — forward queries only: $\mathcal A$ sends data blocks and receives their images under $E(k, \cdot)$ in Game 0, under a uniform permutation $f$ in Game 1.
> - **Promise** — none.
> - **Quantifier** — $\forall$ efficient $\mathcal A$; a **$Q$-query BC adversary** issues at most $Q$ queries.
> - **Adaptivity** — each query may depend on the earlier answers.
>
> ---
> ### Experiment
> A distinguishing game: two branches, **Game 0** (the block cipher) and **Game 1** (a random permutation), that differ in rows 1 and 2. `[BS Attack Game 4.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | **Game 0**: $k \xleftarrow{\$} \mathcal K$<br>**Game 1**: $f \xleftarrow{\$} \text{Perms}[\mathcal X]$ | | |
> | 2 | | $\xleftarrow{\ x_i\ }$ | **Queries** (repeated, adaptive, at most $Q$ times): sends a data block $x_i \in \mathcal X$ |
> | | **Game 0**: $y_i \leftarrow E(k, x_i)$<br>**Game 1**: $y_i \leftarrow f(x_i)$ | $\xrightarrow{\ y_i\ }$ | |
> | 3 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\text{BCadv}[\mathcal A, \mathcal E] = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
> - A block cipher $\mathcal E$ is **secure** if $\text{BCadv}[\mathcal A, \mathcal E]$ is negligible for every efficient adversary $\mathcal A$.
>
> It is a *distinguishing* game, see [[Security Game]].

> [!remark] Notation in the literature
> `[BS]` lets the challenger select $f \in \text{Perms}[\mathcal X]$ in both experiments — $k \xleftarrow{R} \mathcal K$ and $f \leftarrow E(k, \cdot)$ in Experiment 0 — and answers every query with $f(x_i)$; rows 1 and 2 above write the two cases out. It calls the output bit $\hat b$ and lets $W_b$ be the event that $\mathcal A$ outputs $1$ in Experiment $b$, so $\text{BCadv}[\mathcal A, \mathcal E] = |P[W_0] - P[W_1]|$.

> [!remark] Bit-guessing Version
> The challenger chooses $b \in \{0, 1\}$ at random, and then runs Experiment $b$ against the adversary $\mathcal A$. In this game, we measure $\mathcal A$'s **bit-guessing advantage** $\text{BCadv}^*[\mathcal A, \mathcal E]$ as $|P[\hat{b} = b] - 1/2|$: $$\text{BCadv}[\mathcal A, \mathcal E] = 2 \cdot \text{BCadv}^*[\mathcal A, \mathcal E].$$

> [!definition] Parameters
> - $\mathcal E = (E, D)$: a block cipher defined over $(\mathcal K, \mathcal X)$.
> - $Q$: the number of queries before the prediction.

> [!definition] Prediction Game
> ### Scope
> A block cipher $\mathcal E$ and all efficient adversaries.
>
> ---
> ### Condition
> - **Access** — forward queries to $E(k, \cdot)$.
> - **Promise** — none.
> - **Quantifier** — $\forall$ efficient $\mathcal A$.
> - **Adaptivity** — the queries and the final point $x_{Q+1}$ may depend on the earlier answers.
>
> ---
> ### Experiment
> A search game: one branch. `[BS §4.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $k \xleftarrow{\$} \mathcal K$ | | |
> | 2 | | $\xleftarrow{\ x_i\ }$ | **Queries** (repeated, adaptive, $Q$ times): sends $x_i \in \mathcal X$ |
> | | $y_i \leftarrow E(k, x_i)$ | $\xrightarrow{\ y_i\ }$ | |
> | 3 | | $\xleftarrow{\ x_{Q+1},\, y\ }$ | outputs a pair $(x_{Q+1}, y) \in \mathcal X^2$ |
> | 4 | $y^* \leftarrow E(k, x_{Q+1})$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $x_{Q+1} \notin \{x_1, \dots, x_Q\}$: the point is new;
> - $y = y^*$: its image is predicted.
>
> ---
> ### Property
> $$\text{Adv}^{\text{pred}}[\mathcal A, \mathcal E] = \Pr[\mathcal A \text{ wins}].$$
> - $\mathcal E$ is **unpredictable** if $\text{Adv}^{\text{pred}}[\mathcal A, \mathcal E]$ is negligible for every efficient $\mathcal A$. The name $\text{Adv}^{\text{pred}}$ is mine; the note had none.
> - If the block cipher is secure then it is unpredictable. `⚠️ CLAUDE – verify:` this needs $|\mathcal X|$ super-poly, since even a random permutation is predicted with probability $1/(|\mathcal X| - Q)$; my addition.

> [!remark] Key Recovery Game
> The game of [[#Key Recovery]]: like the prediction game, except that the objective of the adversary is to output a candidate key $k' \in \mathcal K$, and it wins iff $k' = k$.
> 
> If the block cipher is unpredictable then it is secure against key recovery game.

> [!definition] Parameters
> - $\mathcal E = (E, D)$: a block cipher defined over $(\mathcal K, \mathcal X)$; $D(k, \cdot)$ is the inverse of $E(k, \cdot)$.
> - $\text{Perms}[\mathcal X]$: the set of all permutations of $\mathcal X$; $f^{-1}$: the inverse of $f$.

> [!definition] Strongly Secure Block Cipher
> ### Scope
> A block cipher $\mathcal E$ and all efficient adversaries.
>
> ---
> ### Condition
> - **Access** — two types of queries, in any order: **forward queries**, answered with $f(x_i)$, and **inverse queries**, answered with $f^{-1}(y_j)$; in Game 0 this is done using algorithms $E$ and $D$.
> - **Promise** — none.
> - **Quantifier** — $\forall$ efficient $\mathcal A$.
> - **Adaptivity** — each query may depend on the earlier answers.
>
> ---
> ### Experiment
> A distinguishing game: the game of [[#Secure Block Cipher]] with inverse queries added; the branches differ in rows 1, 2 and 3. `[BS §4.1]`; `[KL Def 3.28]`.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | **Game 0**: $k \xleftarrow{\$} \mathcal K$<br>**Game 1**: $f \xleftarrow{\$} \text{Perms}[\mathcal X]$ | | |
> | 2 | | $\xleftarrow{\ x_i\ }$ | **Forward queries** (repeated, adaptive): sends $x_i \in \mathcal X$ |
> | | **Game 0**: $y_i \leftarrow E(k, x_i)$<br>**Game 1**: $y_i \leftarrow f(x_i)$ | $\xrightarrow{\ y_i\ }$ | |
> | 3 | | $\xleftarrow{\ y_j\ }$ | **Inverse queries** (repeated, adaptive, interleaved with row 2): sends $y_j \in \mathcal X$ |
> | | **Game 0**: $x_j \leftarrow D(k, y_j)$<br>**Game 1**: $x_j \leftarrow f^{-1}(y_j)$ | $\xrightarrow{\ x_j\ }$ | |
> | 4 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\text{Adv}^{\text{ss}}[\mathcal A, \mathcal E] = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
> - $\mathcal E$ is **strongly secure** if $\text{Adv}^{\text{ss}}[\mathcal A, \mathcal E]$ is negligible for every efficient $\mathcal A$. The name $\text{Adv}^{\text{ss}}$ is mine; the note had none.
> - `[KL Def 3.28]` calls the same notion a *strong pseudorandom permutation*.

### Using Block Cipher Directly for Encryption

> [!remark] Electronic Code Block Mode (ECB Mode)
> The use of block cipher directly for encrypting message. Longer message will be break into smaller blocks.

> [!algorithm] $\ell$-wise ECB cipher
> More precisely, suppose $\mathcal E = (E, D)$ is a block cipher defined over $(\mathcal K, \mathcal X)$. For any poly-bounded $\ell \geq 1$, we can define a cipher $\mathcal E' = (E', D')$, defined over $(\mathcal K, \mathcal X^{\leq \ell}, \mathcal X^{\leq \leq})$, as follows.
> - For $k \in \mathcal K$ and $m \in \mathcal X^{\leq \ell}$, with $v = |m|$, we define $$E'(k, m) = (E(k, m[0]), \dots, E(k, m[v - 1])).$$
> - For $k \in \mathcal K$ and $c \in \mathcal X^{\leq \ell}$, with $v = |c|$, we define $$D'(k, m) = (D(k, m[0]), \dots, D(k, m[v - 1])).$$

> [!theorem]
> Let $\mathcal E = (E, D)$ be a block cipher. Let $\ell \geq 1$ be any poly-bounded value, and let $\mathcal E' = (E', D')$ be the $\ell$-wise ECB cipher derived from $\mathcal E$, but with the message space restricted to all sequence of at most $\ell$ distinct data blocks. If $\mathcal E$ is a secure block cipher, then $\mathcal E'$ is a semantically secure cipher.
> 
> In particular, for every [[Symmetric Key Encryption#Indistinguishability|semantic security]] adversary $\mathcal A$ with respect to $\mathcal E'$, there exists a [[#Secure Block Cipher|secure block cipher]] adversary $\mathcal B$ with respect to $\mathcal E$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{SSadv}[\mathcal A, \mathcal E'] = 2 \cdot \text{BCadv}[\mathcal B, \mathcal E].$$

### Key Recovery

> [!definition] Parameters
> - $\mathcal E = (E, D)$: a block cipher defined over $(\mathcal K, \mathcal X)$.

> [!definition] Key Recovery
> ### Scope
> A block cipher $\mathcal E$ and all efficient adversaries.
>
> ---
> ### Condition
> - **Access** — forward queries to $E(k, \cdot)$: chosen plaintexts.
> - **Promise** — none.
> - **Quantifier** — $\forall$ efficient $\mathcal A$.
> - **Adaptivity** — each query may depend on the earlier answers.
>
> ---
> ### Experiment
> A search game: one branch. `[BS Attack Game 4.4]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $k \xleftarrow{\$} \mathcal K$ | | |
> | 2 | | $\xleftarrow{\ x_i\ }$ | **Queries** (repeated, adaptive): sends $x_i \in \mathcal X$ |
> | | $y_i \leftarrow E(k, x_i)$ | $\xrightarrow{\ y_i\ }$ | |
> | 3 | | $\xleftarrow{\ k'\ }$ | outputs a candidate key $k' \in \mathcal K$ |
> | 4 | compares $k'$ with $k$ | | |
>
> **Goal** — $\mathcal A$ wins iff:
> - $k' = k$.
>
> ---
> ### Property
> $$\text{KRadv}[\mathcal A, \mathcal E] = \Pr[\mathcal A \text{ wins}].$$
> - $\mathcal E$ is secure against key recovery if $\text{KRadv}[\mathcal A, \mathcal E]$ is negligible for every efficient $\mathcal A$.
> - In the [[Ideal Cipher Model|ideal cipher model]] the same advantage is written $\text{KR}^{ic}\text{adv}$, as in the theorem below.

> [!theorem]
> Let $\mathcal E = (E, D)$ be a block cipher defined over $(\mathcal K, \mathcal X)$. Then there exists a [[#Key Recovery|key recovery]] adversary $\mathcal A_{EX}$ with respect to $\mathcal E$, modeled as an ideal cipher, making $Q$ standard queries and $Q |\mathcal K|$ ideal cipher queries, such that $$\text{KR}^{ic}\text{adv}[\mathcal A_{EX}, \mathcal E] \geq 1 - \epsilon \quad \text{where} \quad \epsilon = \frac{|\mathcal K|}{(|\mathcal X| - Q)^Q}$$

## Constructing Block Cipher

> [!algorithm] Iterated Cipher
> Virtually all block ciphers used in practice use the same basic framework called the **iterated cipher** paradigm. To construct an iterated block cipher the designer makes two choices:
> - First, he picks a simple block cipher $\hat {\mathcal E} = (\hat E, \hat D)$ that is clearly insecure on its own. We call $\hat {\mathcal E}$ the **round cipher**.
> - Second, he picks a simple (not necessarily secure) PRG $G$ that is used to expand the key $k$ into $d$ keys $k_1, \dots, k_d$ for $\hat {\mathcal E}$. We call $G$ the **key expansion function**.
> ---
> Algorithm $E(k, m)$
> 1. **Key expansion**: Use the key expansion function $G$ to stretch the key $k$ to $\mathcal E$ to $d$ keys of $\hat {\mathcal E}$: $$(k_1, \dots, k_d) \leftarrow G(k)$$
> 2. **Iteration**: For $i = 1, \dots, d$ apply $\hat {E}(k_i, \cdot)$, namely: $$y \leftarrow \hat {E}(k_d, \hat {E}(k_{d - 1}, \dots, \hat {E}(k_2, \hat {E}(k_1, x)) \dots ))$$
> ---
> Each application of $\hat {\mathcal E}$ is called a **round** and the total number of rounds is $d$. The key $k_1, \dots, k_d$ are called **round keys**. The decryption algorithm $D(k, y)$ is identical except that the round keys are applied in reverse order. $D(k, y)$ is defined as: $$x \leftarrow \hat{D}(k_1, \hat{D}(k_2, \dots, \hat{D}(k_{d - 1}, \hat{D}(k_d, y)) \dots ))$$

### Feistel Permutation

> [!algorithm] Feistel Permutation
> Let $f: \mathcal X \rightarrow \mathcal X$ be a function. We construct a permutation $\pi : \mathcal X^2 \rightarrow \mathcal X^2$: $$\pi(x, y) = (y, x \oplus f(y)).$$ And the inverse $$\pi^{-1}(u, v) = (v \oplus f(u), u).$$ The function $\pi$ is called a **Feistel permutation** and is used to build the DES round cipher. The composition of $n$ Feistel permutations is called an $n$-**round Feistel network**. Block ciphers designed as a Feistel network are called **Feistel ciphers**.

### Construction from PRF

> [!algorithm] Luby-Rackoff Construction
> Let $F$ be a PRF, defined $(\mathcal K, \mathcal X, \mathcal X)$, where $\mathcal X = \{0, 1\}^n$. We describe a block cipher $\mathcal E = (E, D)$ whose key space is $\mathcal K^3$, and whose data block space is $\mathcal X^2$.
> Given a key $(k_1, k_2, k_3) \in \mathcal K^3$ and a data block $(u, v) \in \mathcal X^2$, the encryption algorithm $E$ runs as follows:
> 1. $w \leftarrow u \oplus F(k_1, v)$
> 2. $x \leftarrow v \oplus F(k_2, w)$
> 3. $y \leftarrow w \oplus F(k_3, x)$
> 4. Output $(x, y)$.
> 
> Given a key $(k_1, k_2, k_3) \in \mathcal K^3$ and a data block $(x, y) \in \mathcal X^2$, the decryption algorithm $D$ runs as follows:
> 1. $w \leftarrow y \oplus F(k_3, x)$
> 2. $v \leftarrow x \oplus F(k_2, w)$
> 3. $u \leftarrow w \oplus F(k_1, v)$
> 4. Output $(u, v)$.

> [!theorem]
> If $F$ is a secure PRF and $N = |\mathcal X| = 2^n$ is super-poly, then the Luby-Rackoff cipher $\mathcal E = (E, D)$ constructed from $F$ is a secure block cipher.
> 
> In particular, for every [[#Secure Block Cipher|secure block cipher]] adversary $\mathcal A$ that attacks $\mathcal E$, there exists a [[Pseudorandom Function#Definition|secure PRF]] adversary $\mathcal B$ with respect to $F$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{BCadv}[\mathcal A, \mathcal E] \leq 3 \cdot \text{PRFadv}[\mathcal B, F] + \frac{Q^2}{N} + \frac{Q^2}{2N^2}.$$

## Case Study

### The DES Algorithm

> [!algorithm] DES Round Function $F(k, x)$
> The DES encryption algorithm is a 16-round Feistel network where each rounds uses a different function $f: \mathcal X \rightarrow \mathcal X$. In round number $i$ the function $f$ is defined as $$f(x) = F(k_i, x)$$ where $k_i$ is a 48-bit key for round number $i$ and $F$ is fixed function called the **DES round function**. $F$ uses several auxiliary functions $E, P$, and $S_1, \dots, S_8$ defined as follows:
> - The function $E$ expands a 32-bit input to a 48-bit output by rearranging and replicating the input bits.
> - The function $P$, called the **mixing permutation**, maps a 32-bit input to a 32-bit output by rearranging the bits of the input.
> - The function $S_1, \dots, S_8$ called **S-boxes**. Each S-box $S_i$ maps a 6-bit input to a 4-bit output by a lookup table.
> ---
> Given these function, the DES round function $F(k, x)$ works as follows:
> Input: $k \in \{0, 1\}^{48}$ and $x \in \{0, 1\}^{32}$
> Output: $y \in \{0, 1\}^{32}$
> ---
> $F(k, x)$:
> 1. $t \leftarrow E(x) \oplus k \in \{0, 1\}^{48}$
> 2. Separate $t$ into 8 groups of 6-bits each: $t = t_1 || \dots || t_8$
> 3. For $i = 1$ to $8$: $s_i \leftarrow S_i(t_i)$
> 4. $s \leftarrow s_1 || \dots || s_8 \in \{0, 1\}^{32}$
> 5. $y \leftarrow P(s) \in \{0, 1\}^{32}$
> 6. Output $y$

> [!algorithm] DES Key Expansion Function
> The DES key expansion function $G$ takes as input the 56-bit key $k$ and outputs 16 keys $k_1, \dots, k_{16}$, each 48-bits long. Each key $k_i$ consists of 48 bits chosen from the 56-bit key, with each $k_i$ using a different subset of bits from $k$.

> [!algorithm] The DES Algorithm
> The complete DES algorithm consists of 16 iteration of the DES round cipher plus initial and final permutations called IP and FP. These permutation simply rearrange the 64 incoming and outgoing bits. The permutation FP is the inverse of IP. 
> 

> [!remark]
> IP and FP have no cryptographic significant and were included for unknown reasons. Since bit permutations are slow in software, but fast in hardware, one theory is that IP and FP are intended to deliberately slow down software implementations of DES.

> [!algorithm] Triple-DES
> Let $\mathcal E = (E, D)$ be a block cipher defined over $(\mathcal K, \mathcal X)$. We define the block cipher $3\mathcal E = (E_3, D_3)$ as $$E_3((k_1, k_2, k_3), x) = E(k_3, E(k_2, E(k_1, x))).$$ The $3\mathcal E$ block cipher takes key in $\mathcal K^3$. For DES the $3 \mathcal E$ block cipher, called **Triple-DES**, uses keys whose length is $3 \times 56 = 168$ bits.

> [!theorem]
> Let $\mathcal E = (E, D)$ be an ideal block cipher defined over $(\mathcal K, \mathcal X)$, and consider an attack against the $3 \mathcal E$ construction in the ideal cipher model. If $\mathcal A$ is an adversary that makes at most $Q$ queries (including both standard and ideal cipher queries) in the ideal cipher variant of [[#Secure Block Cipher|secure block cipher]], then $$\text{BC}^{ic}\text{adv}[\mathcal A, 3 \mathcal E] \leq C_1 L \frac{Q^2}{|\mathcal K|^3} + C_2 \frac{Q^{2/3}}{|\mathcal K|^{2/3} |\mathcal X|^{1/3}} + C_3 \frac{1}{|\mathcal K|},$$ where $L = max(|\mathcal K|/|\mathcal X|, \log_2 |\mathcal X|)$, and $C_1, C_2, C_3$ are constants (that do not depend on $\mathcal A$ or $\mathcal E$).
 
> [!remark] $2 \mathcal E$ is insecure
> Double-DES is no more secure than single DES. More generally, let $\mathcal E = (E, D)$ be a block cipher with key space $\mathcal K$. We show that the $2 \mathcal E = (E_2, D_2)$ construction, defined as $$E_2((k_1, k_2), x) = E(k_2, E(k_1, x))$$ is no more secure than $\mathcal E$. The attack strategy is called **meet in the middle**.

> [!theorem]
> Let $\mathcal E = (E, D)$ be a block cipher defined over $(\mathcal K, \mathcal X)$. There is an algorithm $\mathcal A_{EX}$ that takes as input $Q$ plaintext/ciphertext pairs $(x_i, y_i) \in \mathcal X^2$ for $i = 1, \dots, Q$ and outputs a key pair $(k_1, k_2) \in \mathcal K^2$ such that $$y_i = E_2((k_1, k_2), x_i) \quad \forall i = 1, \dots, Q.$$ It running time is dominated by a total of $2Q \cdot |\mathcal K|$ evaluations of algorithms $E$ and $D$.

> [!remark] Semi-weak keys cancel
> DES has pairs of keys $(K_a, K_b)$ where $K_a \neq K_b$ but $(E_{K_a})(E_{K_b}(x)) = x$ for all $x$.
> Example of such pair:
> ```python
Ka = bytes.fromhex('01FE01FE01FE01FE')
Kb = bytes.fromhex('FE01FE01FE01FE01')
> ```

### The AES Algorithm

> [!algorithm] The AES Round Permutation
> The permutation $\pi_{AES}$ is made up of a sequence of three invertible operations on the set $\{0, 1\}^{128}$. The 128 bits are organized as a $4 \times 4$ array of cells, where each cell is made up of eight bits. The following three invertible operations are then carried out in sequence, one after the other, on this $4 \times 4$ array:
> 1. `SubBytes`: Let $S: \{0, 1\}^8 \rightarrow \{0, 1\}^8$ be a fixed permutation. This permutation is applied to each of the 16 cells, one cell at a time. The permutation $S$ is specified in the AES standard as a hard-coded table of 256 entries. It is designed to have no fixed points, namely $S(x) \neq x$ for all $x \in \{0, 1\}^8$, and no inverse fixed points, namely $S(x) \neq \overline{x}$ where $\overline{x}$ is the bit-wise complement of $x$.
> 2. `ShiftRows`: This step performs a cyclic shift on the four rows of the input $4 \times 4$ array: the first row is unchanged, the second row is cyclically shifted one byte to the left, the third row is cyclically shifted two bytes, and the fourth row is cyclically shifted three bytes: $$\begin{pmatrix}a_0 & a_1 & a_2 & a_3 \\ a_4 & a_5 & a_6 & a_7 \\ a_8 & a_9 & a_{10} & a_{11} \\ a_{12} & a_{13} & a_{14} & a_{15}\end{pmatrix} \Rightarrow \begin{pmatrix}a_0 & a_1 & a_2 & a_3 \\ a_5 & a_6 & a_7 & a_4 \\ a_{10} & a_{11} & a_8 & a_9 \\ a_{15} & a_{12} & a_{13} & a_{14}\end{pmatrix}$$
> 3. `MixColumns`: In this step the $4 \times 4$ array is treated as a matrix and this matrix is multiplied by a fixed matrix where arithmetic is interpreted in the finite field $\text{GF}(2^8)$. Elements in the field $\text{GF}(2^8)$ are represented as polynomials over $\text{GF}(2)$ of degree less than eight where multiplication is done modulo the irreducible polynomial $x^8 + x^4 + x^3 + x + 1$. Specifically, the `MixColumns` transformation does: $$\begin{pmatrix}02 & 03 & 01 & 01 \\ 01 & 02 & 03 & 01 \\ 01 & 01 & 02 & 03 \\ 03 & 01 & 01 & 02\end{pmatrix} \times \begin{pmatrix}a_0 & a_1 & a_2 & a_3 \\ a_5 & a_6 & a_7 & a_4 \\ a_{10} & a_{11} & a_8 & a_9 \\ a_{15} & a_{12} & a_{13} & a_{14}\end{pmatrix} \Rightarrow \begin{pmatrix}a_0' & a_1' & a_2' & a_3' \\ a_4' & a_5' & a_6' & a_7' \\ a_8' & a_9' & a_{10}' & a_{11}' \\ a_{12}' & a_{13}' & a_{14}' & a_{15}'\end{pmatrix}$$ Here the scalars $01, 02, 03$ are interpreted as elements of $\text{GF}(2^8)$ using their binary representation. This fixed matrix is invertible over $\text{GF}(2^8)$.

> [!algorithm] The AES-128 Key Expansion Method
> The 128-bit AES key is partitioned into four 32-bit words $w_{0, 0}, w_{0, 1}, w_{0, 2}, w_{0, 3}$ and these form the first round key $k_0$. The remaining ten round keys are generated sequentially: for $i = 1, \dots, 10$, the 128-bit round key $k_i = (w_{i, 0}, w_{i, 1}, w_{i, 2}, w_{i, 3})$ is generated from the preceding round key $k_{i - 1} = (w_{i - 1, 0}, w_{i - 1, 1}, w_{i - 1, 2}, w_{i - 1, 3})$ as follows:
> - $w_{i, 0} \leftarrow w_{i - 1, 0} \oplus g_i(w_{i - 1}, 3)$
> - $w_{i, 1} \leftarrow w_{i - 1, 1} \oplus w_{i, 0}$
> - $w_{i, 2} \leftarrow w_{i - 1, 2} \oplus w_{i, 1}$
> - $w_{i, 3} \leftarrow w_{i - 1, 3} \oplus w_{i, 2}$
> Here the function $g_i : \{0, 1\}^{32} \rightarrow \{0, 1\}^{32}$ is a fixed function specified in the AES standard. It operates on its four byte input in three steps:
> 1. Perform a one-byte left circular rotation on the 4-byte input
> 2. Apply `SubBytes` to each of the four bytes obtained
> 3. XOR the left most byte with a fixed round constant $c_i$. The round constants $c_1, \dots, c_{10}$ are specified in the AES standard: round constant number $i$ is the element $x^{i - 1}$ of the field $\text{GF}(2^8)$ treated as an 8-bit string.

### The Evan-Mansour Block Cipher and the $\mathcal E X$ construction

> [!algorithm] Evan-Mansour Block Cipher
> Let $\mathcal X = \{0, 1\}^n$. Let $\pi : \mathcal X \rightarrow \mathcal X$ be a permutation and let $\pi^{-1}$ be its inverse function. Even and Mansour defined the following simple block cipher $\mathcal E_{EM} = (E, D)$ defined over $(\mathcal X^2, \mathcal X)$: $$E((P_1, P_2), x) = \pi(x \oplus P_1) \oplus P_2 \quad \text{and} \quad D((P_1, P_2), y) = \pi^{-1}(y \oplus P_2) \oplus P_1$$
> 

> [!algorithm] $\mathcal E X$ Construction and DESX
> Apply Evan-Mansour construction to block cipher $\mathcal E = (E, D)$ defined over $(\mathcal K, \mathcal X)$, we obtain a new block cipher called $\mathcal E X = (EX, DX)$ where $$EX((k, P_1, P_2), x) = E(k, x \oplus P_1) \oplus P_2, \quad DX((k, P_1, P_2), y) = D(k, y \oplus P_2) \oplus P_1.$$ 

> [!theorem]
> Let $\mathcal E = (E, D)$ be a block cipher defined over $(\mathcal K, \mathcal X)$. Let $\mathcal E X = (EX, DX)$ be the block cipher derived from $\mathcal E$, where $P_1$ and $P_2$ are each uniformly distributed over a subset $\mathcal X'$ of $\mathcal X$. If we model $\mathcal E$ as an ideal cipher, and if $\mathcal A$ is an adversary for $\mathcal E X$ that makes at most $Q_s$ standard queries and $Q_{ic}$ ideal cipher queries, then we have $$\text{BC}^{ic}\text{adv}[\mathcal A, \mathcal E X] \leq \frac{2Q_s Q_{ic}}{|\mathcal K| |\mathcal X'|}.$$ 

## Algorithmic Attacks

### Linear Cryptanalysis

> [!algorithm] Linear Relation
> Let $(E, D)$ be a block cipher where data blocks and keys are bit strings. That is, $\mathcal M = \mathcal C = \{0, 1\}^n$ and $\mathcal K = \{0, 1\}^h$.
> For a bit string $m \in \{0, 1\}^n$ and a set of bit positions $S \subseteq \{0, \dots, n - 1\}$ we use $m[S]$ to denote the XOR of the bits in positions in $S$. That is, if $S = \{i_1, \dots, i_\ell\}$ then $m[S] = m[i_1] \oplus \dots \oplus m[i_\ell]$.
> We say that the block cipher $(E, D)$ has a **linear relation** if there exist sets of bit positions $S_0, S_1 \subseteq \{0, \dots, n - 1\}$ and $S_2 \subseteq \{0, \dots, h - 1\}$, such that for all keys $k \in \mathcal K$ and for randomly chosen $m \in \mathcal M$, we have $$P[m[S_0] \oplus E(k, m)[S_1] = k[S_2]] \geq \frac{1}{2} + \epsilon$$ for some non-negligible $\epsilon$ called the **bias**. For an "ideal" cipher the plaintext and ciphertext behave like independent strings so that the relation $m[S_0] \oplus E(k, m)[S_1] = k[S_2]$ holds with probability exactly 1/2, and the bias $\epsilon = 0$.

> [!lemma]
> Let $(E, D)$ be a block cipher with a linear relation. Let $m_1, \dots, m_t$ be messages sampled uniformly and independently from the message space $\mathcal M$ and let $c_i = E(k, m_i)$ for $i = 1, \dots t$. Then $$P[k[S_2] = \text{Majority}_{i = 1}^t (m_i[S_0] \oplus c_i [S_1])] \geq 1 - e^{-t\epsilon^2 / 2}$$

## Side-Channel Attacks



## Fault Injection Attacks


## Quantum Attacks



