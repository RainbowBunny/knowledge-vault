---
dg-publish: false
---
Reference:
- `[BDPR98]` — M. Bellare, A. Desai, D. Pointcheval, P. Rogaway, _Relations Among Notions of Security for Public-Key Encryption Schemes_, CRYPTO 1998; full version: https://www.di.ens.fr/david.pointcheval/Documents/Papers/1998_crypto.pdf
- `[HHK17]` — D. Hofheinz, K. Hövelmanns, E. Kiltz, _A Modular Analysis of the Fujisaki-Okamoto Transformation_, TCC 2017 (ePrint 2017/604): https://eprint.iacr.org/2017/604
- `[BS]` — Boneh, Shoup, _A Graduate Course in Applied Cryptography_, Ch. 11: https://toc.cryptobook.us/

## Syntax

> [!definition] Public-Key Encryption Scheme
> A **public-key encryption scheme** $\text{PKE} = (\mathsf{KeyGen}, \text{Enc}, \text{Dec})$ is a triple of efficient algorithms with a message space $\mathcal M$, ciphertext space $\mathcal C$, randomness space $\mathcal R$ and key space $\mathcal K$.
> - $(pk, sk) \leftarrow \mathsf{KeyGen}()$: The key-generation algorithm $\mathsf{KeyGen}$ returns a pair $(pk, sk)$ consisting of a public key $pk$ and a secret key $sk$. 
> - $c \leftarrow \text{Enc}(pk, m)$ (Deterministic) or $c \leftarrow \text{Enc}(pk, m; r)$ (Probabilistic): The encryption algorithm takes a public key $pk$, a message $m \in \mathcal M$ and possibly an internal random $r \leftarrow \mathcal R$ to produce a ciphertext $c \in \mathcal C$.
> - $m \leftarrow \text{Dec}(sk, c)$: The deterministic decryption algorithm takes a secret key $sk$ and a ciphertext $c$, and outputs either a message $m \in \mathcal M$ or a special symbol $\perp$ to indicate **rejection**. 

> [!algorithm] Public-key Encryption Scheme (Mathematical Detail)
> A **public-key encryption scheme** consists of three algorithms, $\mathsf{KeyGen}$, $E$, and $D$, along with two families of spaces with system parameterization $P$: 
> $$M = \{\mathcal M_{\lambda, \Lambda}\}_{\lambda, \Lambda} \quad \text{and} \quad C = \{\mathcal C_{\lambda, \Lambda}\}_{\lambda, \Lambda},$$
> such that
> 1. $M$ and $C$ are efficiently recognizable.
> 2. $M$ has an effective length function.
> 3. Algorithm $\mathsf{KeyGen}$ is an efficiently probabilistic algorithm that on input $\lambda, \Lambda$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda))$, outputs a pair $(pk, sk)$, where $pk$ and $sk$ are bit strings whose lengths are always bounded by a polynomial in $\lambda$.
> 4. Algorithm $E$ is an efficiently probabilistic algorithm that on input $\lambda, \Lambda, pk, m$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(\mathsf{KeyGen}(\lambda, \Lambda))$ for some $sk$, and $m \in \mathcal M_{\lambda, \Lambda}$, always outputs an element of $\mathcal C_{\lambda, \Lambda}$.
> 5. Algorithm $D$ is an efficiently deterministic algorithm that on input $\lambda, \Lambda, sk, c$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(\mathsf{KeyGen}(\lambda, \Lambda))$ for some $pk$, and $c \in \mathcal C_{\lambda, \Lambda}$, outputs either an element of $\mathcal M_{\lambda, \Lambda}$, or a special symbol $\text{reject} \notin \mathcal M_{\lambda, \Lambda}$.
> 6. For all $\lambda, \Lambda, pk, sk, m, c$, where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(\mathsf{KeyGen}(\lambda, \Lambda)), k \in \mathcal K_{\lambda, \Lambda}, m \in \mathcal M_{\lambda, \Lambda}$ and $c \in \text{Supp}(E(\lambda, \Lambda; pk, m))$, we have $D(\lambda, \Lambda; sk, c) = m$.

> [!remark] Notation in the literature
> Key generation is $\mathsf{KeyGen}$ in this vault ([[Note Layouts]] § *Game form*); the current syntax, with the full table, is [[Public-Key Encryption Scheme#Syntax]].
>
> | source | key generation | differences |
> | --- | --- | --- |
> | `[BS Def 11.1, 11.3]` | $G()$; $G(\lambda, \Lambda)$ | the form of the "Mathematical Detail" callout above, with system parameter $\Lambda$; row taken from the table in [[Public-Key Encryption Scheme]] |
> | `[BDPR98 §2]` | $\mathcal K(1^k)$ | the scheme is $(\mathcal K, \mathcal E, \mathcal D)$ |
> | `[HHK17 §2.1]` | $\mathsf{Gen}$ | the scheme is $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ with a finite message space $\mathcal M$ |

## Property

### Injectivity

> [!definition] PKE Injectivity
> A public-key encryption scheme $\text{PKE}$ is *injective* if for all key pairs $(pk, sk) \leftarrow \mathsf{KeyGen}()$, it holds that $\text{Enc}(pk, m; r) = \text{Enc}(pk, m'; r') \Rightarrow (m, r) = (m', r')$ for all $m, m' \in \mathcal M$ and $r, r' \in \mathcal R$.

### Correctness

> [!definition] PKE $(1-\delta)$-Correctness
> A public-key encryption scheme $\text{PKE}$ is $(1-\delta)$-correct if 
> $$E[\max_{m \in \mathcal M} \Pr[\text{Dec}(sk, \text{Enc}(pk, m)) = m]] \geq 1 - \delta$$

> [!remark]
> For some literature, this definition comes from the decryption failure rate and thus we have the following correctness definition. So in writing please use the above definition instead.

### Min-Entropy

> [!definition] Min-Entropy
> Given $(pk, sk) \in \mathcal K, m \in \mathcal M$, we define the **min-entropy** of $\text{Enc}(pk, m)$ by 
> $$\gamma(pk, m) = -\log \max_{c \in \mathcal C} \Pr[c = \text{Enc}(pk, m; r) \; | \; r \in \mathcal R].$$
> We say that a $\text{PKE}$ is $\gamma$**-spread** if: 
> $$\forall (pk, sk) \in \mathcal K, m \in \mathcal M, c \in \mathcal C: \gamma(pk, m) \geq \gamma$$

> [!corollary]
> For every ciphertext $c \in \mathcal C$, we have 
> $$\Pr[c = \text{Enc}(pk, m; r) \; | \; r \leftarrow \mathcal R] \leq 2^{-\gamma}$$

### Rigidity

> [!definition] PKE Rigidity
> We say that a $\text{PKE}$ is **rigid** if for all key pairs $(pk, sk) \leftarrow \mathsf{KeyGen}()$, and all ciphertexts $c$, it holds that either $\text{Dec}(sk, c) = \perp$ or $\text{Enc}(pk, \text{Dec}(sk, c)) = c$.

## Security

### Indistinguishability

> [!definition] PKE Indistinguishability Advantage
> A distinguishing game: two branches that differ in row 4 only, **Game 0** and **Game 1**. `[BDPR98 Def 2.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(pk, sk) \leftarrow \mathsf{KeyGen}()$ | $\xrightarrow{\ pk\ }$ | |
> | 2 | | $\xleftarrow{\ c\ }$ | **Decryption queries** (repeated, adaptive; $\text{atk} \in \{\text{lta}, \text{cca}\}$ only): sends $c$ |
> | | $m \leftarrow \text{Dec}(sk, c)$ | $\xrightarrow{\ m\ }$ | |
> | 3 | | $\xleftarrow{\ m_0,\, m_1\ }$ | chooses $m_0, m_1 \in \mathcal M$ with $\lvert m_0 \rvert = \lvert m_1 \rvert$ |
> | 4 | **Game 0**: $c^* \leftarrow \text{Enc}(pk, m_0)$<br>**Game 1**: $c^* \leftarrow \text{Enc}(pk, m_1)$ | $\xrightarrow{\ c^*\ }$ | |
> | 5 | | $\xleftarrow{\ c\ }$ | **Decryption queries** (repeated, adaptive; $\text{atk} = \text{cca}$ only): sends $c \neq c^*$ |
> | | $m \leftarrow \text{Dec}(sk, c)$ | $\xrightarrow{\ m\ }$ | |
> | 6 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are:
>   $$\text{Adv}_\text{PKE}^{\text{ind-atk}}(\mathcal A) = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
>
> Where:
> 1. Chosen Plaintext Attack: $\text{atk} = \text{cpa}$: no decryption query; rows 2 and 5 are skipped.
> 2. Lunch Time Attack: $\text{atk} = \text{lta}$ (or sometimes $\text{cca1}$): decryption queries in row 2 only.
> 3. Adaptive Chosen Ciphertext Attack: $\text{atk} = \text{cca}$: decryption queries in rows 2 and 5, never on $c^*$.

> [!remark] The source's form and the previous one
> `[BDPR98 Def 2.1]` splits the adversary into $(A_1, A_2)$, which pass a state $s$ and get oracles $\mathcal O_1, \mathcal O_2$, and measures $2 \Pr[b' = b] - 1$ for a uniform bit $b$. The previous version of this note had $\mathcal A = (\mathcal A_\text{find}, \mathcal A_\text{guess})$ and $|\Pr[b = b'] - 1/2|$, which is half the difference above. Here the adversary is one stateful machine, see [[Security Game]]. The current version of this game is [[Public-Key Encryption Scheme#Indistinguishability]].

> [!definition] $(t,\varepsilon)$-IND-ATK security of a PKE 
> A PKE scheme is **$(t, \varepsilon)$-IND-ATK secure** if for every adversary $\mathcal{A}$ that has running time bounded by $t$, we have: 
> $$\text{Adv}_{\text{PKE}}^{\text{ind-atk}}(\mathcal A) \leq \varepsilon$$

> [!remark]
> 6. ATK here is a placeholder for the attacker.
> 7. Lunch time attack means that only one phase (before lunch) for oracle.

 > [!security]
 > If a public-key encryption scheme $\mathcal E$ is semantically secure, then it is also CPA secure.
 > 
 > In particular, for every [[Public-Key Encryption Scheme (Old)#Indistinguishability|CPA security]] adversary $\mathcal A$ with respect to $\mathcal E$, and which makes at most $Q$ queries to its challenger, there exists an [[Public-Key Encryption Scheme (Old)#Indistinguishability|semantic security]] adversary $\mathcal B$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that 
 > $$\text{CPAadv}[\mathcal A, \mathcal E] = Q \cdot \text{SSadv}[\mathcal B, \mathcal E].$$

### Non-Malleability

> [!definition] PKE Non-Malleability Advantage
> Two experiments that differ in row 7 only: the relation is checked against the encrypted message in **Game 0** (real) and against an independent sample of $M$ in **Game 1** (random). `[BDPR98 Def 2.2]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(pk, sk) \leftarrow \mathsf{KeyGen}()$ | $\xrightarrow{\ pk\ }$ | |
> | 2 | | $\xleftarrow{\ c'\ }$ | **Decryption queries** (repeated, adaptive; $\text{atk} \in \{\text{lta}, \text{cca}\}$ only): sends $c'$ |
> | | $m' \leftarrow \text{Dec}(sk, c')$ | $\xrightarrow{\ m'\ }$ | |
> | 3 | | $\xleftarrow{\ M\ }$ | chooses a message distribution $M$ whose messages all have the same length |
> | 4 | $m \leftarrow M$<br>$c \leftarrow \text{Enc}(pk, m)$ | $\xrightarrow{\ c\ }$ | |
> | 5 | | $\xleftarrow{\ c'\ }$ | **Decryption queries** (repeated, adaptive; $\text{atk} = \text{cca}$ only): sends $c' \neq c$ |
> | | $m' \leftarrow \text{Dec}(sk, c')$ | $\xrightarrow{\ m'\ }$ | |
> | 6 | | $\xleftarrow{\ R,\, (c_1, \dots, c_n)\ }$ | outputs a relation $R$ and ciphertexts $c_1, \dots, c_n$ |
> | 7 | $m_i \leftarrow \text{Dec}(sk, c_i)$ for $i \in [1, n]$<br>**Game 0**: $\hat m \leftarrow m$<br>**Game 1**: $\hat m \leftarrow M$, a fresh sample independent of $m$ | | |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A) = 1$ in Game $b$ iff all hold:
>     - $c \notin (c_1, \dots, c_n)$;
>     - $\perp \notin (m_1, \dots, m_n)$;
>     - $R(\hat m, (m_1, \dots, m_n))$.
> - **Measure** — how far apart the two success probabilities are:
>   $$\text{Adv}_\text{PKE}^{\text{nm-atk}}(\mathcal A) = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
>
> Where:
> 1. Chosen Plaintext Attack: $\text{atk} = \text{cpa}$: no decryption query; rows 2 and 5 are skipped.
> 2. Lunch Time Attack: $\text{atk} = \text{lta}$: decryption queries in row 2 only.
> 3. Adaptive Chosen Ciphertext Attack: $\text{atk} = \text{cca}$: decryption queries in rows 2 and 5, never on $c$.
>
> Also:
> 1. $R$ is a predicate.

> [!remark] The source's form and the previous one
> `[BDPR98 Def 2.2]` splits the adversary into $(A_1, A_2)$ passing a state $s$, calls the two probabilities $\mathrm{Succ}^{\mathrm{nm\text{-}atk}}_{A, \Pi}$ and $\mathrm{Succ}^{\mathrm{nm\text{-}atk}}_{A, \Pi, \$}$, and asks that $M$ be samplable and $R$ computable. The previous version of this note listed the oracles of $\text{atk} = \text{cpa}$ under the label "cca" and decrypted $(y_1, \dots, y_n)$ instead of the adversary's $(c_1, \dots, c_n)$; both are corrected above.

> [!definition] $(t,\varepsilon)$-NM-ATK security of a PKE 
> A PKE scheme is **$(t, \varepsilon)$-NM-ATK secure** if for every adversary $\mathcal{A}$ that has running time bounded by $t$, we have: 
> $$\text{Adv}_{\text{PKE}}^{\text{nm-atk}}(\mathcal A) \leq \varepsilon$$

### One-way Encryption

> [!definition] PKE OWE Advantage
> A search game with one branch: `[HHK17 Def 2.1]` with $\text{ATK} = \text{CPA}$, where it is called OW-CPA.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(pk, sk) \leftarrow \mathsf{KeyGen}()$<br>$m \xleftarrow{\$} \mathcal M$<br>$c \leftarrow \text{Enc}(pk, m)$ | $\xrightarrow{\ pk,\, c\ }$ | |
> | 2 | | $\xleftarrow{\ m'\ }$ | outputs a message $m'$ |
>
> **Goal** — $\mathcal A$ wins iff:
> - $\text{Dec}(sk, c) = m'$.
>
> $$\text{Adv}_{\text{PKE}}^{\text{owe}}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$

> [!definition] $(t,\varepsilon)$-OWE security of a PKE 
> A PKE scheme is **$(t, \varepsilon)$-OWE secure** if for every adversary $\mathcal{A}$ that has running time bounded by $t$, we have: 
> $$\text{Adv}_{\text{PKE}}^{\text{owe}}(\mathcal A) \leq \varepsilon$$

### One-Wayness under Chosen Plaintext Attacks

> [!definition] PKE OWE-CPA Advantage
> For any adversary $\mathcal A$, we define the OWE-CPA advantage:
> $$\text{Adv}_\text{PKE}^{\text{owe-cpa}}$$

## Construction

### Based on a Trapdoor Function Scheme

> [!algorithm] PKE by Trapdoor Function Scheme
> Component of $\mathcal E_{TDF}$:
> - A trapdoor function scheme $\mathcal T = (\mathsf{KeyGen}, F, I)$, defined over $(\mathcal X, \mathcal Y)$,
> - A symmetric cipher $\mathcal E_s = (E_s, D_s)$, defined over $(\mathcal K, \mathcal M, \mathcal C)$,
> - A hash function $H: \mathcal X \rightarrow \mathcal K$.
> 
> Message space for $\mathcal E_{TDF}$ is $\mathcal M$, ciphertext space is $\mathcal Y \times \mathcal C$.
> - The key generation algorithm for $\mathcal E_{TDF}$ is the key generation algorithm for $\mathcal T$.
> - For a given public key $pk$, and a given message $m \in \mathcal M$, the encryption algorithm runs as follows: 
> $$E(pk, m) = x \xleftarrow{R} \mathcal X, y \leftarrow F(pk, x), k \leftarrow H(x), c \xleftarrow{R} E_s(k, m), \text{output } (y, c)$$
> - For a given secret key $sk$, and a given ciphertext $(y, c) \in \mathcal Y \times \mathcal C$, the decryption algorithm runs as follows: 
> $$D(sk, (y, c)) = x \leftarrow I(sk, y), k \leftarrow H(x), m \leftarrow D_s(k, c), \text{output } m.$$
> 
> Thus $\mathcal E_{TDF} = (\mathsf{KeyGen}, E, D)$, and is defined over $(\mathcal M, \mathcal Y \times \mathcal C)$.

> [!theorem] 
> Assume $H: \mathcal X \rightarrow \mathcal K$ is modeled as a random oracle. If $\mathcal T$ is one-way and $\mathcal E_s$ is semantically secure, then $\mathcal E_{TDF}$ is semantically secure.
> 
> In particular, for every [[Public-Key Encryption Scheme (Old)#Indistinguishability|semantic security]] adversary $\mathcal A$ that attacks $\mathcal E_{TDF}$, there exists an [[Public-Key Encryption Scheme (Old)#One-way Encryption|inverting]] adversary $\mathcal B_{ow}$ that attacks $\mathcal T$, and an [[Public-Key Encryption Scheme (Old)#Indistinguishability|semantic security]] adversary $\mathcal B_s$ that attacks $\mathcal E_s$, where $\mathcal B_{ow}$ and $\mathcal B_s$ are elementary wrappers around $\mathcal A$, such that 
> $$\text{SS}^{ro}\text{adv}[\mathcal A, \mathcal E_{TDF}] \leq 2 \cdot \text{OWadv}[\mathcal B_{ow}, \mathcal T] + \text{SSadv}[\mathcal B_s, \mathcal E_s]$$

## Case Study

### RSA Trapdoor Function Scheme

> [!algorithm] RSA Trapdoor Function Scheme
> The basic RSA encryption scheme is $\mathcal E_{RSA} = (\mathsf{KeyGen}, E, D)$, with message space $\mathcal M$ and ciphertext space $\mathcal X \times \mathcal C$, where
> - The key generation algorithm runs as follows: 
> $$\mathsf{KeyGen}() = (n, d) \xleftarrow{R} \text{RSAGen}(\ell, e), pk \leftarrow (n, e), sk \leftarrow (n, d), \text{output } (pk, sk);$$
> - For a given public key $pk = (n, e)$, and message $m \in \mathcal M$, the encryption algorithm runs as follows: 
> $$E(pk, m) = x \xleftarrow{R} \mathbb Z_n, y \leftarrow x^e, k \leftarrow H(x), c \xleftarrow{R} E_s(k, m), \text{output } (y, c) \in \mathcal X \times \mathcal C'$$
> - For a given secret key $sk = (n, d)$, and a given ciphertext $(y, c) \in \mathcal X \times \mathcal C$, where $y$ represents an element of $\mathbb Z_n$, the decryption algorithm runs as follows: 
> $$D(sk, (y, c)) = x \leftarrow y^d, k \leftarrow H(x), m \leftarrow D_s(k, c), \text{output } m.$$

> [!theorem]
> Assume $H : \mathcal X \rightarrow \mathcal K$ is modeled as a random oracle. If the RSA assumption holds for parameters $(\ell, e)$, and $\mathcal E_s$ is semantically secure, then $\mathcal E_{RSA}$ is semantically secure.
> 
> In particular, for any [[Public-Key Encryption Scheme (Old)#Indistinguishability|semantic security]] $\mathcal A$ that attacks $\mathcal E_{RSA}$, there exist an RSA adversary $\mathcal B_{rsa}$ that breaks the [[Trapdoor Functions#A Trapdoor Permutation Scheme Based on RSA|RSA assumption]] for $(\ell, e)$, and an [[Public-Key Encryption Scheme (Old)#Indistinguishability|semantic security]] adversary $\mathcal B_s$ that attacks $\mathcal E_s$, where $\mathcal B_{rsa}$ and $\mathcal B_s$ are elementary wrappers around $\mathcal A$, such that 
> $$\text{SS}^{ro}\text{adv}^*[\mathcal A, \mathcal E_{RSA}] \leq \text{RSAadv}[\mathcal B_{RSA}, \ell, e] + \text{SSadv}^*[\mathcal B_s, \mathcal E_s].$$

### ElGamal Encryption

> [!algorithm] ElGamal Encryption
> Components of ElGamal encryption:
> - A cyclic group $\mathbb G$ of prime order $q$ with generator $g \in \mathbb G$,
> - A symmetric cipher $\mathcal E_s = (E_s, D_s)$, defined over $(\mathcal K, \mathcal M, \mathcal C)$,
> - A hash function $H: \mathbb G^2 \rightarrow \mathcal K$.
> The key generation, encryption, and decryption algorithms for $\mathcal E_{EG}$.
> - The key generation algorithm runs as follows: 
> $$\begin{align} \mathsf{KeyGen}() = \quad &\alpha \xleftarrow{R} \mathbb Z_q, u \leftarrow g^\alpha, \\ &pk \leftarrow u, sk \leftarrow \alpha \\ &\text{output }(pk, sk); \end{align}$$
> - For a given public key $pk = u \in \mathbb G$ and message $m \in \mathcal M$, the encryption algorithm runs as follows:
> $$E(pk, m) = \beta \xleftarrow{R} \mathbb Z_q, v \leftarrow g^\beta, w \leftarrow u^\beta, k \leftarrow H(v, w), c \leftarrow E_s(k, m), \text{output } (v, c);$$
> - For a given secret key $sk = \alpha \in \mathbb Z_q$ and a ciphertext $(v, c) \in \mathbb G \times \mathcal C$, the decryption algorithm runs as follows: 
> $$D(sk, (v, c)) = w \leftarrow v^\alpha, k \leftarrow H(v, w), m \leftarrow D_s(k, c), \text{output } m.$$
> 
> Thus, $\mathcal E_{EG} = (\mathsf{KeyGen}, E, D)$, and is defined over $(\mathcal M, \mathbb G \times \mathcal C)$.

> [!theorem]
> Assume $H: \mathbb G^2 \rightarrow \mathcal K$ is modeled as a random oracle. If the CDH assumption holds for $\mathbb G$, and $\mathcal E_s$ is semantically secure, then $\mathcal E_{EG}$ is semantically secure.
> 
> In particular, for every [[Public-Key Encryption Scheme (Old)#Indistinguishability|semantic security]] adversary $\mathcal A$ with respect to $\mathcal E_{EG}$, and makes at most $Q$ queries to the random oracle, there exist a [[Key Exchange#Computational Diffie-Hellman|computational Diffie-Hellman]] adversary $\mathcal B_{cdh}$ with respect to $\mathbb G$, and an [[Public-Key Encryption Scheme (Old)#Indistinguishability|semantic security]] adversary $\mathcal B_s$ with respect to $\mathcal E_s$, where $\mathcal B_{cdh}$ and $\mathcal B_s$ are elementary wrappers around $\mathcal A$, such that 
> $$\text{SS}^{ro}\text{adv}[\mathcal A, \mathcal E_{EG}] \leq 2Q \cdot \text{CDHadv}[\mathcal B_{cdh}, \mathbb G] + \text{SSadv}[\mathcal B_s, \mathcal E_s].$$

### Lattice-Based Instantiation

> [!algorithm] Lattice-Based Instatiation
> - $\text{Setup}$
> 	- $\tau$: $\ell_{\infty}$-norm bound on all short elements in the scheme.
> 	- $q_{PKE}$: a modulus
> 	- $p < q_{PKE}$: a positive integer
> - $\mathsf{KeyGen}()$:
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



