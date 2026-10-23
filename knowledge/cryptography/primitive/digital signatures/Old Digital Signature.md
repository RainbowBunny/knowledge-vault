Reference:
- `[BS]` — D. Boneh, V. Shoup, _A Graduate Course in Applied Cryptography_, v0.6, 2023, Ch. 13: https://toc.cryptobook.us/ (Attack Games 13.1 and 13.2, and the random-oracle version of 13.1). `⚠️ CLAUDE – verify:` WebFetch reaches only the front of the book, so Ch. 13 could not be read; the games redraw the wording this note already had, checked against `[GMR88]`, `[ADR02]` and `[AABN02]`.
- `[GMR88]` — S. Goldwasser, S. Micali, R. L. Rivest, _A Digital Signature Scheme Secure Against Adaptive Chosen-Message Attacks_, SIAM J. Comput. 17(2), 1988, pp. 281–308: https://people.csail.mit.edu/rivest/pubs/GMR88.pdf (§2.1 syntax, §2.2 attacks, §2.3 forgeries, §9 security).
- `[ADR02]` — J. H. An, Y. Dodis, T. Rabin, _On the Security of Joint Signature and Encryption_, EUROCRYPT 2002: https://cims.nyu.edu/~dodis/ps/signcrypt.pdf (§2.2, strong unforgeability).
- `[AABN02]` — M. Abdalla, J. H. An, M. Bellare, C. Namprempre, _From Identification to Signatures via the Fiat–Shamir Transform_, EUROCRYPT 2002; full version ePrint 2002/022: https://eprint.iacr.org/2002/022 (Def 2.2, unforgeability in the random-oracle model).
- `⚠️ CLAUDE – verify:` — a point I could not check against the source.

## Overview

> [!definition] Abstract Description of the Digital Signature Scheme
> - $K^{\text{Pri}}$: A private signing key.
> - $K^{\text{Pub}}$: A public verification key.
> - $\text{Sign}$: A **signing algorithm** that takes as input a digital document $D$ and a private key $K^{\text{Pri}}$ and returns a signature $D^{\text{Sig}}$ for $D$.
> - $\text{Verify}$: A **verification algorithm** that takes as input a digital document $D$, a signature $D^{\text{sig}}$, and a public key $K^{\text{Pub}}$. The algorithm returns `True` is $D^{\text{sig}}$ is a signature for $D$ associated to the private key $K^{\text{Pri}}$, and otherwise it returns `False`.

> [!remark] 
> Necessary general conditions for a secure digital signature scheme include the following:
> - Given $K^{\text{Pub}}$, an attacker cannot feasibly determine $K^{\text{Pri}}$, nor can she determine any other private key that produces the same signatures as $K^{\text{Pri}}$.
> - Given $K^{\text{Pub}}$, and a list of signed documents $D_1, \dots, D_n$ with their signatures $D_1^{\text{sig}}, \dots, D_n^{\text{sig}}$, an attacker cannot feasibly determine a valid signature on any document $D$ that is not in the list $D_1, \dots, D_n$.

| Term                                                  | Reference                                                  |                   |
| ----------------------------------------------------- | ---------------------------------------------------------- | ----------------- |
| Attack Game 13.1 (Signature Security)                 | [[Old Digital Signature#Unforgeability\|signature security]]                 | $\text{SIGadv}$   |
| Attack Game 13.2 (Strongly Secure Signature Security) | [[Old Digital Signature#Strong Unforgeability\|strongly secure signature security]] | $\text{stSIGadv}$ |

> [!remark] Syntax in `[GMR88 §2.1]`
> The original definition lists six components. Its key generation algorithm $G$ is $\mathsf{KeyGen}$ here, and its signing algorithm is called $\sigma$.
> - A **security parameter** $k$, which is chosen by the user when he creates his public and secret keys. The parameter $k$ determines a number of quantities (length of signatures, length of signable messages, running time of the signing algorithm, overall security, etc).
> - A **message space** $\mathcal M$, which is the set of messages to which the signature algorithm may be applied. Without loss of generality, all messages are represented as binary strings, $\mathcal M \subseteq \{0, 1\}^*$. To ensure that the entire signing process is polynomial in the security parameter, the length of the messages to be signed is bounded by $k^c$, for some constant $c > 0$.
> - A **signature bound** $B$, which is an integer bounding the total number of signatures that can be produced with an instance of the signature scheme. This value is typically bounded above by a low-degree polynomial in $k$, but may be infinite.
> - A **key generation algorithm** $G$, which any user $A$ can use on input $1^k$ ($k$ in unary) to generate in polynomial time a pair $(P_A, S_A)$ of matching public and secret keys. The secret key is sometimes called the trap-door information.
> - A **signature algorithm** $\sigma$, which produces a signature $\sigma(M, S_A)$ for a message $M$ using the secret key $S_A$. Here $\sigma$ may receive other inputs as well; in the first scheme of `[GMR88]`, $\sigma$ has an additional input, the number of previously signed messages.
> - A **verification algorithm** $V$, which tests whether $S$ is a valid signature for message $M$ using the public key $P_A$: $V(S, M, P_A)$ is true if and only if it is valid.
>
> Any of these algorithms may be randomized, using an auxiliary random bit stream. $G$ must be, since part of its output is the secret key, which must be unpredictable to an adversary. The signing algorithm may be randomized — the one of `[GMR88]` is, and can produce many different signatures for the same message. The verification algorithm need not be randomized, and theirs is not.

> [!algorithm] Signature Scheme
> A **signature scheme** $\mathcal S = (\mathsf{KeyGen}, S, V)$ is triple of efficient algorithms where $\mathsf{KeyGen}$ is called a **key generation algorithm**, $S$ is called a **signing algorithm**, and $V$ is called a **verification algorithm**. Algorithm $S$ is used to generate signatures and algorithm $V$ is used to verify signatures.
> - $\mathsf{KeyGen}$ is a probabilistic algorithm that takes no input. It outputs a pair $(pk, sk)$, where $sk$ is called a secret **signing key** and $pk$ is called a public **verification key**.
> - $S$ is a probabilistic algorithm that is invoked as $\sigma \xleftarrow{R} S(sk, m)$, where $sk$ is a secret key (as output by $\mathsf{KeyGen}$) and $m$ is a message. The algorithm output a **signature** $\sigma$.
> - $V$ is a deterministic algorithm invoked as $V(pk, m, \sigma)$. It outputs either `accept` or `reject`.
> - We require that a signature generated by $S$ is always accepted by $V$. That is, for all $(pk, sk)$ output by $\mathsf{KeyGen}$ and all messages $m$, we have $$P[V(pk, m, S(sk, m)) = \text{accept}] = 1.$$
> 
> We say that messages lie in a finite **message space** $\mathcal M$, and signatures lie in some finite **signature space** $\Sigma$. We say that $\mathcal S = (\mathsf{KeyGen}, S, V)$ is defined over $(\mathcal M, \Sigma)$.
> 
> `[BS]` calls the key generation algorithm $G$; here it is $\mathsf{KeyGen}$.

> [!algorithm] Signature
> A **signature** scheme is a triple of efficient algorithms $(\mathsf{KeyGen}, S, V),$ along with two families of spaces with system parameterization $P$: $$M = \{\mathcal M_{\lambda, \Lambda}\}, \Sigma = \{\Sigma_{\lambda, \Lambda}\}_{\lambda, \Lambda},$$ As usual, $\lambda \in \mathbb Z_{\geq 1}$ is a security parameter and $\Lambda \in \text{Supp}(P(\lambda))$ is a system parameter. We require that
> 1. $M$ and $\Sigma$ are efficient recognizable.
> 2. Algorithm $\mathsf{KeyGen}$ is an efficient probabilistic algorithm that on input $\lambda, \Lambda,$ where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda))$, outputs a pair $(pk, sk),$ where $pk$ and $sk$ are bit strings whose lengths are always bounded by a polynomial in $\lambda$.
> 3. Algorithm $S$ is an efficient probabilistic algorithm that on input $\lambda, \Lambda, sk, m,$ where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(\mathsf{KeyGen}(\lambda, \Lambda))$ for some $pk,$ and $m \in \mathcal M_{\lambda, \Lambda},$ always outputs an element of $\Sigma_{\lambda, \Lambda}$.
> 4. Algorithm $V$ is an efficient deterministic algorithm that on input $\lambda, \Lambda, pk, m, \sigma,$ where $\lambda \in \mathbb Z_{\geq 1}, \Lambda \in \text{Supp}(P(\lambda)), (pk, sk) \in \text{Supp}(\mathsf{KeyGen}(\lambda, \Lambda))$ for some $sk, m \in \mathcal M_{\lambda, \Lambda},$ and $\sigma \in \Sigma_{\lambda, \Lambda},$ and outputs either `accept` or `reject`.

## Security Model

### Unforgeability

> [!definition] Parameters
> - [[#Overview|Signature scheme]] $\mathcal S = (\mathsf{KeyGen}, S, V)$ defined over $(\mathcal M, \Sigma)$.
> - $\mathcal A$: an efficient [[Adversary|adversary]]. $Q$: a bound on the number of its signing queries.
> - $m_i \in \mathcal M$: the $i$-th signing query. $\sigma_i \in \Sigma$: the signature returned for it.
> - $(m, \sigma) \in \mathcal M \times \Sigma$: the candidate forgery.

> [!definition] Signature Security
> ### Scope
> A signature scheme $\mathcal S = (\mathsf{KeyGen}, S, V)$ defined over $(\mathcal M, \Sigma)$ and an efficient adversary $\mathcal A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ gets $pk$ and a signature $\sigma_i \xleftarrow{R} S(sk, m_i)$ on each message $m_i$ it asks for; never $sk$. It is a **$Q$-query adversary** if it asks at most $Q$ times.
> - **Promise** — none.
> - **Quantifier** — $\forall$ efficient $\mathcal A$.
> - **Adaptivity** — an adaptive chosen-message attack: each $m_i$ may depend on $pk$ and on $\sigma_1, \dots, \sigma_{i-1}$. The forgery comes after the last query.
>
> ---
> ### Experiment
> A search game with one branch; row 4 computes the winning conditions. `[BS Attack Game 13.1]`; `[GMR88 §2.2–2.3]`.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(pk, sk) \xleftarrow{R} \mathsf{KeyGen}()$ | $\xrightarrow{\ pk\ }$ | |
> | 2 | | $\xleftarrow{\ m_i\ }$ | **Signing queries** (repeated, adaptive, at most $Q$ times): sends a message $m_i \in \mathcal M$ |
> | | $\sigma_i \xleftarrow{R} S(sk, m_i)$ | $\xrightarrow{\ \sigma_i\ }$ | |
> | 3 | | $\xleftarrow{\ m,\, \sigma\ }$ | outputs a candidate forgery $(m, \sigma) \in \mathcal M \times \Sigma$ |
> | 4 | runs $V(pk, m, \sigma)$<br>checks whether $m \in \{m_1, m_2, \dots\}$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $V(pk, m, \sigma) = \text{accept}$;
> - $m$ is new: $m \notin \{m_1, m_2, \dots\}$. A signature on one new message suffices — an **existential forgery**.
>
> ---
> ### Property
> $$\text{SIGadv}[\mathcal A, \mathcal S] = \Pr[\mathcal A \text{ wins}].$$
> - $\mathcal S$ is **secure**, or **existentially unforgeable under an adaptive chosen-message attack** (EUF-CMA), if $\text{SIGadv}[\mathcal A, \mathcal S]$ is negligible for every efficient $\mathcal A$.
> - $\mathcal S$ is a **secure $q$-time signature** if $\text{SIGadv}[\mathcal A, \mathcal S]$ is negligible for every efficient $\mathcal A$ that issues at most $q$ signing queries. When $q = 1$, $\mathcal S$ is a **secure one-time signature**.
>
> A *search* game, see [[Security Game]].

> [!remark] Notation in the literature
> - `[BS]` writes the scheme as $(G, S, V)$, with $G$ taking no input, and the game as a list of steps; the advantage is $\text{SIGadv}[\mathcal A, \mathcal S]$ of Attack Game 13.1.
> - `[GMR88]` has a security parameter $k$ and key generation on input $1^k$. Of its five attacks — key-only, known-message, generic chosen-message, directed chosen-message, adaptive chosen-message (§2.2) — this game grants the strongest, and of its four breaks — total break, universal, selective, existential forgery (§2.3) — it asks for the weakest. Its main theorem (§9) shows that its scheme is not even $1/Q(k)$-existentially forgeable under an adaptive chosen-message attack, for every polynomial $Q$, with the coins of key generation inside the probability space.
> - `[AABN02 Def 2.2]` writes the forger as an oracle machine $F^{S_{sk}(\cdot)}(pk)$ that outputs $(M, \sigma)$, and the experiment returns $0$ when $M$ was queried. Here $\mathcal A$ is one stateful machine and each oracle call is a pair of rows, see [[Security Game]].

> [!question] Security Against Multi-key Attacks
> In real systems there are many users, and each one of them can have a signature key pair $(pk_i, sk_i)$ for $i = 1, \dots, n$. Can a chosen message attack on $pk_1$ help the adversary forge signatures for $pk_2$?

#### Random-oracle version

When $\mathcal S$ uses a hash function $H$ modeled as a [[Random Oracle Model|random oracle]], the challenger also plays $H$: a random function $H \in \mathsf{Funs}[\mathcal X_H, \mathcal Y_H]$ from the hash's domain to its range, evaluated on demand. Hash queries and signing queries interleave as $\mathcal A$ chooses, and $S$ and $V$ call the same $H$. `[BS Attack Game 13.1, random-oracle version]`; `[AABN02 Def 2.2]`

| | challenger $\mathcal C$ | | adversary $\mathcal A$ |
| --- | --- | --- | --- |
| 1 | $H \xleftarrow{R} \mathsf{Funs}[\mathcal X_H, \mathcal Y_H]$<br>$(pk, sk) \xleftarrow{R} \mathsf{KeyGen}()$ | $\xrightarrow{\ pk\ }$ | |
| 2 | | $\xleftarrow{\ x_j\ }$ | **Hash queries** (repeated, adaptive, at most $Q_{ro}$ times): sends a point $x_j \in \mathcal X_H$ |
| | $y_j \leftarrow H(x_j)$ | $\xrightarrow{\ y_j\ }$ | |
| 3 | | $\xleftarrow{\ m_i\ }$ | **Signing queries** (repeated, adaptive, at most $Q_s$ times): sends a message $m_i \in \mathcal M$ |
| | $\sigma_i \xleftarrow{R} S^H(sk, m_i)$ | $\xrightarrow{\ \sigma_i\ }$ | |
| 4 | | $\xleftarrow{\ m,\, \sigma\ }$ | outputs a candidate forgery $(m, \sigma) \in \mathcal M \times \Sigma$ |
| 5 | runs $V^H(pk, m, \sigma)$<br>checks whether $m \in \{m_1, m_2, \dots\}$ | | |

**Goal** — $\mathcal A$ wins iff all of:
- $V^H(pk, m, \sigma) = \text{accept}$;
- $m \notin \{m_1, m_2, \dots\}$.

The advantage is $\text{SIG}^{\text{ro}}\text{adv}[\mathcal A, \mathcal S] = \Pr[\mathcal A \text{ wins}]$. The [[Schnorr Identification#Security Analysis of Schnorr Signatures|Schnorr]] and [[ID and Signatures from Sigma#The Fiat-Shamir Heuristic for Signatures|Fiat–Shamir]] signature theorems are stated for it.

### Strong Unforgeability

> [!definition] Parameters
> - As in [[#Unforgeability|signature security]]: the scheme $\mathcal S = (\mathsf{KeyGen}, S, V)$ over $(\mathcal M, \Sigma)$, the adversary $\mathcal A$, the query bound $Q$, the queries $m_i$ with their signatures $\sigma_i$, and the candidate forgery $(m, \sigma)$.

> [!definition] Strongly Secure Signature
> ### Scope
> A signature scheme $\mathcal S = (\mathsf{KeyGen}, S, V)$ defined over $(\mathcal M, \Sigma)$ and an efficient adversary $\mathcal A$.
>
> ---
> ### Condition
> - **Access** — as in [[#Unforgeability|signature security]]: $pk$ and a signature on each message it asks for; never $sk$.
> - **Promise** — none.
> - **Quantifier** — $\forall$ efficient $\mathcal A$.
> - **Adaptivity** — an adaptive chosen-message attack, as in signature security.
>
> ---
> ### Experiment
> A search game with one branch; it differs from [[#Unforgeability|signature security]] only in the freshness check of row 4. `[BS Attack Game 13.2]`; `[ADR02 §2.2]`.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(pk, sk) \xleftarrow{R} \mathsf{KeyGen}()$ | $\xrightarrow{\ pk\ }$ | |
> | 2 | | $\xleftarrow{\ m_i\ }$ | **Signing queries** (repeated, adaptive, at most $Q$ times): sends a message $m_i \in \mathcal M$ |
> | | $\sigma_i \xleftarrow{R} S(sk, m_i)$ | $\xrightarrow{\ \sigma_i\ }$ | |
> | 3 | | $\xleftarrow{\ m,\, \sigma\ }$ | outputs a candidate forgery $(m, \sigma) \in \mathcal M \times \Sigma$ |
> | 4 | runs $V(pk, m, \sigma)$<br>checks whether $(m, \sigma) \in \{(m_1, \sigma_1), (m_2, \sigma_2), \dots\}$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $V(pk, m, \sigma) = \text{accept}$;
> - $(m, \sigma)$ is new: $(m, \sigma) \notin \{(m_1, \sigma_1), (m_2, \sigma_2), \dots\}$. A new signature on a message that was already signed counts.
>
> ---
> ### Property
> $$\text{stSIGadv}[\mathcal A, \mathcal S] = \Pr[\mathcal A \text{ wins}].$$
> - $\mathcal S$ is **strongly secure** if $\text{stSIGadv}[\mathcal A, \mathcal S]$ is negligible for every efficient $\mathcal A$.
> - $\mathcal S$ is a **strongly secure $q$-time signature** if $\text{stSIGadv}[\mathcal A, \mathcal S]$ is negligible for every efficient $\mathcal A$ that issues at most $q$ signing queries. When $q = 1$, $\mathcal S$ is a **strongly secure one-time signature**.
>
> Strong security implies security: a forgery on a new message is in particular a new pair.

> [!remark] Notation in the literature
> `[ADR02 §2.2]` calls this **strong unforgeability** (sUF-CMA): the forger must be unable to produce even a different signature on an already signed message, a notion that only makes sense under a chosen-message attack. `[BS]` calls it *strongly secure* and its advantage $\text{stSIGadv}$.

## Extending The Message Space

### Collision Resistant Hashing

> [!algorithm] Extending Message Space with Collision Resistant Hashing
> Let $\mathcal S = (\mathsf{KeyGen}, S, V)$ be a signature scheme defined over $(\mathcal M, \sigma)$ and let $H : \mathcal M' \rightarrow \mathcal M$ be a hash function, where the set $\mathcal M'$ is much larger than $\mathcal M$. Define a new signature scheme $\mathcal S' = (\mathsf{KeyGen}, S', V')$ over $(\mathcal M', \Sigma)$ as $$S'(sk, m) = S(sk, H(m)) \text{ and } V'(pk, m, \sigma) = V(pk, H(m), \sigma).$$
> 

> [!remark]  
> The new scheme signs much larger messages than the original scheme. This approach is often called the **hash-and-sign paradigm**. Thus, we can just create signature scheme for a small space, like 256-bit messages.

> [!theorem]
> Suppose the signature scheme $\mathcal S$ is secure and the hash function $H$ is collision resistant. Then the derived signature scheme $\mathcal S' = (\mathsf{KeyGen}, S', V')$ is a secure signature.
> 
> In particular, suppose $\mathcal A$ is a signature adversary in [[Old Digital Signature#Unforgeability|signature security]]. Then there exist an efficient signature adversary $\mathcal B_{\mathcal S}$ and an efficient collision finder $\mathcal B_H$, which are elementary wrappers around $\mathcal A$, such that $$\text{SIGadv}[\mathcal A, \mathcal S'] \leq \text{SIGadv}[\mathcal B_{\mathcal S}, \mathcal S] + \text{CRadv}[\mathcal B_H, H]$$

### TCR Functions

> [!algorithm] Extending Message Space with TCR Functions
> Let $H$ be a TCR hash function defined over $(\mathcal K_H, \mathcal M, \mathcal T)$. Let $\mathcal S = (\mathsf{KeyGen}, S, V)$ be a signature scheme for short messages in $\mathcal K_H \times \mathcal T$. We build a new signature scheme $S' = (\mathsf{KeyGen}, S', V')$ for signing messages in $\mathcal M$ as follows:
> - $S'(sk, m) = r \xleftarrow{R} \mathcal K_H, h \leftarrow H(r, m), \sigma \leftarrow S(sk, (r, h))$ and output $(\sigma, r)$.
> - $V'(pk, m, (\sigma, r)) = h \leftarrow H(r, m)$ and output $V(pk, (r, h), \sigma)$.

> [!theorem]
> Suppose $\mathcal S = (\mathsf{KeyGen}, S, V)$ is a secure signature scheme and the hash function $H$ is TCR. Then the derived signature scheme $S' = (\mathsf{KeyGen}, S', V')$ is secure.
> 
> In particular, for every signature adversary $\mathcal A$ in [[Old Digital Signature#Unforgeability|signature security]] that issues at most $Q$ signing queries, there exist an efficient signature adversary $\mathcal B_{\mathcal S}$ and an efficient TCP adversary $\mathcal B_H,$ which are elementary wrapper around $\mathcal A$, such that $$\text{SIGadv}[\mathcal A, \mathcal S'] \leq \text{SIGadv}[\mathcal B_{\mathcal S}, \mathcal S] + Q \cdot \text{TCRadv}[\mathcal B_{H}, H].$$ 

## Signatures from Trapdoor Permutations


## Construction

### Based on SIS

[Lattice Signatures Without Trapdoors](https://eprint.iacr.org/2011/537)
> [!algorithm] SIS Signature Scheme
> ### Building Block
> - Random Oracle: $H : \{0, 1\}^* \rightarrow \{v : v \in \{-1, 0, 1\}, ||v||_1 \leq K\}$
> 
> ---
> ### Algorithms
> - $(pk = (A, AS), sk = (S)) \leftarrow \mathsf{KeyGen}()$:
> 1. Signing Key: $S \leftarrow \{-d, \dots, 0, \dots, d\}^{m \times k}$
> 2. Verification Key: $A \leftarrow \mathbb Z_q^{n \times m}, T \leftarrow AS \in \mathbb Z_q^{n \times k}$
> - $S(\mu, A, S)$:
> 1. $y \leftarrow D_\sigma^m$
> 2. $c \leftarrow H(Ay, \mu)$
> 3. $z \leftarrow Sc + y$
> 4. Output $(z, c)$ with probability $\min(\frac{D^m_\sigma(z)}{MD^m_{Sc, \sigma}(z)}, 1)$
> - $V(\mu, z, c, A, T)$
> 1. Accept iff $||z|| \leq \eta \sigma \sqrt{m}$ and $c = H(Az - Tc, \mu)$.

> [!theorem]
> If there is a polynomial-time forger, who makes at most $s$ queries to the signing oracle and $h$ queries to the random oracle $H$, who breaks the signature above with probability $\delta$, then there is a polynomial-time algorithm who can solve the $\ell_2\text{-SIS}_{q, n, m, \beta}$ problem for $\beta = (2 \eta \sigma + 2 dk) \sqrt{m} = \tilde{O}(dn)$ with probability $\approx \frac{\delta^2}{2(h + s)}$. Moreover, the signing produces a signature with probability $\approx 1/M$ and the verifying algorithm accepts a signature produced by an honest signer with probability at least $1 - 2^{-m}$.

### Basic Lamport Signatures

> [!algorithm] One-bit Lamport Signatures
> ### Building Block
> - One-way function $f$ defined over $(\mathcal X, \mathcal Y)$.
> 
> ---
> ### Algorithms
> We denote the system $\mathcal S_{1bit} = (\mathsf{KeyGen}, S, V)$
> - $(pk = (f(x_0), f(x_1)) = (y_0, y_1), sk = (x_0, x_1)) \leftarrow \mathsf{KeyGen}()$, with $x_0$ and $x_1$ are two random values.
> - $x_m \leftarrow S(sk, m \in \{0, 1\})$
> - $V(pk, m, \sigma)$: Accept if $f(\sigma) = y_m$.

> [!theorem]
> Let $f$ be a one-way function over $(\mathcal X, \mathcal Y)$. Then $\mathcal S_{1bit}$ is a secure one-time signature for message in $\{0, 1\}$.

> [!remark]
> $\text{SIGadv}[\mathcal A, \mathcal S_{1bit}] \leq 2 \cdot \text{OWadv}[\mathcal B, f]$.

> [!algorithm] Basic Lamport Signatures
> ### Building Block
> - One-way function $f$ defined over $(\mathcal X, \mathcal Y)$.
> 
> ---
> ### Algorithms
> We denote the system $\mathcal S_L = (\mathsf{KeyGen}, S, V)$
> - $(pk \in \mathcal Y^{2v}, sk \in \mathcal X^{2v}) \leftarrow \mathsf{KeyGen}()$:
> 	1. Choose $2v$ random values: $\begin{pmatrix}x_{1, 0}, & \dots, & x_{v, 0} \\ x_{1, 1}, & \dots, & x_{v, 1}\end{pmatrix} \xleftarrow{R} \mathcal X^{2v}$
> 	2. For $i = 1, \dots, v$ and $j = 0, 1$ do: $y_{i, j} \leftarrow f(x_{i, j})$
> 	3. Output: $sk = \begin{pmatrix}x_{1, 0}, & \dots, & x_{v, 0} \\ x_{1, 1}, & \dots, & x_{v, 1}\end{pmatrix} \in \mathcal X^{2v}$, and $pk = \begin{pmatrix}y_{1, 0}, & \dots, & y_{v, 0} \\ y_{1, 1}, & \dots, & y_{v, 1}\end{pmatrix} \in \mathcal Y^{2v}$
> - Algorithm $S(sk, m)$, where $m = m_1 \dots m_v \in \{0, 1\}^v$, outputs the signature: $$\sigma = (x_{1, m_1}, x_{2, m_2}, \dots, x_{v, m_v}) \in \mathcal Y^v$$
> - Algorithm $V(pk, m, \sigma)$ where $m \in \{0, 1\}^v$ and $\sigma = (\sigma_1, \dots, \sigma_v) \in \mathcal X^v$ outputs $$\begin{cases}\text{accept} &\text{if } f(\sigma_i) = y_{i, m_i} \forall i = 1, \dots, v \\ \text{reject} &\text{otherwise}\end{cases}$$

> [!algorithm] Randomized Lamport
> ### Building Block
> - $H_{etcr}$ is an enhanced TCR function defined over $(\mathcal R, \mathcal M, \{0, 1\}^v)$.
> - Basic Lamport scheme $\mathcal S_L = (\mathsf{KeyGen}, S, V)$.
> 
> ---
> ### Algorithms
> - $S'(sk, M)$: Given $m \in \mathcal M$ as input, do: $$r \xleftarrow{R} \mathcal R, m \leftarrow H_{etcr}, \sigma' \leftarrow S(sk, m), \text{output } \sigma = (r, \sigma').$$
> - $V'(pk, M, (r, \sigma'))$: Given $m \in \mathcal M$ and $(r, \sigma')$ as input, do: $$m \leftarrow H_{etcr}(r, M), \text{output } V(pk, m, \sigma')$$
 
### General Lamport Framework

> [!algorithm] General Lamport Framework
> ### Building Block
> - One-way function $f$ defined over $(\mathcal X, \mathcal Y)$.
> - [[Pseudorandom Function#Definition|Secure PRF]] $F$.
> - Function $P$
> 
> ---
> ### Algorithms
> The generalized Lamport system $\mathcal S_P = (\mathsf{KeyGen}, S, V)$ works as follows:
> - $(pk, sk) = \mathsf{KeyGen}()$:
> 	1. $k \xleftarrow{R} \mathcal K$
> 	2. For $i = 1, \dots, n: x_i \leftarrow F(k, i) \in \mathcal X; y_i \leftarrow f(x_i) \in \mathcal Y$.
> 	3. Output ($pk = (y_1, \dots, y_n)$, $sk = (k)$)
> - $\sigma \leftarrow S(sk, m)$:
> 	1. $s \leftarrow P(m) \subseteq \{1, \dots, n\}$
> 	2. Let $s = \{s_1, \dots, s_\ell\}$
> 	3. For $j = 1, \dots, \ell: \sigma_j \leftarrow F(k, s_j)$
> 	4. Output $\sigma \leftarrow (\sigma_1, \dots, \sigma_\ell)$
> - $V(pk, m, \sigma)$:
> 	1. Let $P(m) = \{s_1, \dots, s_\ell\}$
> 	2. Let $\sigma = \{\sigma_1, \dots, \sigma_u\}$
> 	3. If $\ell = u$ and $f(\sigma_i) = y_{s_i}$ for all $i = 1, \dots, \ell$ then output $\text{accept}$, else $\text{reject}$.

> [!theorem]
> Suppose $f$ is a one-way hash over $(\mathcal X, \mathcal Y)$ and $F$ is a [[Pseudorandom Function#Definition|secure PRF]] defined over $(\mathcal K, \{1, \dots, n\}, \mathcal X)$. Let $P$ be a containment free function from $\mathcal M$ to subsets of $\{1, \dots, n\}$. Then $\mathcal S_P$ is a secure one-time signature for messages in $\mathcal M$.
> In particular, suppose $\mathcal A$ is a signature adversary attacking $\mathcal S_P$ that issues at most one signature query. Then there exist an efficient adversary $\mathcal B_f$ attacking the one-wayness of $f$, and a PRF adversary $\mathcal B_F$, where $\mathcal B_f$ and $\mathcal B_F$ are elementary wrappers around $\mathcal A$, such that $$\text{SIGadv}[\mathcal A, \mathcal S_P] \leq n \cdot \text{OWadv}[\mathcal B_f, f] + \text{PRFadv}[\mathcal B_F, F]$$

### Winternitz Signatues

> [!algorithm] Winternitz Scheme
> ### Building Block
> 
> ---
> ### Algorithms
> - $(pk, sk) \leftarrow \mathsf{KeyGen}()$
> 	1. $k \xleftarrow{R} \mathcal S$
> 	2. $(x_1, \dots, x_n) \leftarrow G_{prg}(k)$
> 	3. For $i = 1, \dots, n: y_i \leftarrow f^{(d)}(x_i)$
> 	4. Output: $pk = H(y_1, \dots, y_n), sk = (k)$.
> - $\sigma \leftarrow S(sk, m)$
> 	1. $(x_1, \dots, x_n) \leftarrow G_{prg}(k)$
> 	2. $s \leftarrow P(m) \in I_d^n$
> 	3. Let $s = (s_1, \dots, s_n)$
> 	4. For $i = 1, \dots, n$: $\sigma_i \leftarrow f^{(s_i)}(x_i)$
> 	5. Output: $\sigma \leftarrow (\sigma_1, \dots, \sigma_n)$.
> - $V(pk, m, \sigma)$
> 	1. Let $P(m) = (s_1, \dots, s_n)$
> 	2. Let $\sigma = (\sigma_1, \dots, \sigma_n)$
> 	3. For $i = 1, \dots, n$: $\hat{y}_i \leftarrow f^{(d - s_i)}(\sigma_i)$
> 	4. $\hat{y} \leftarrow (\hat{y}_1, \dots, \hat{y}_n)$
> 	5. If $H(\hat{y}) = pk$ output $\text{accept}$, otherwise output $\text{reject}$.

> [!theorem]
> Let $f$ be a [[Trapdoor Functions#One-way on $d$ iterates|one-way function on d iterates]] defined over $(\mathcal X, \mathcal X)$. Let $G_{prg}$ be a [[Pseudorandom Generators#Secure PRG|secure PRG]] over $(\mathcal S, \mathcal X^n)$, let $H$ be [[Hash Function#Definition|collision resistant]] over $(\mathcal X^n, \mathcal T)$, and let $P: \mathcal M \rightarrow I_n^d$ be [[Cryptographically Special Function#Domination Free Function|dominaiton free]]. Then the Winternitz scheme $\mathcal S_{win}$ is a secure one-time signature for messages in $\mathcal M$.
> In particular, suppose $\mathcal A$ is a signature adversary attacking $\mathcal S_{win}$ that issues at most one signature query. Then there exist efficient adversaries $\mathcal B_f, \mathcal B_G, \mathcal B_H$, where all three are elementary wrappers around $\mathcal A$, such that $$\text{SIGadv}[\mathcal A, \mathcal S_{win}] \leq nd \cdot \text{iOWadv}[\mathcal B_f, f, d] + \text{PRGadv}[\mathcal B_G, G_{prg}] + \text{CRadv}[\mathcal B_H, H]$$

## Concrete Signature Schemes

- [[Digital Signature Algorithm]]
- [[GGH Public Key Cryptosystem]]
- [[ElGamal Public Key Cryptosystem]]
- [[NTRU Public Key Cryptosystem]]