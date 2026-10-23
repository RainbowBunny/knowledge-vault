Reference:
- `[BS x]` — Boneh, Shoup, _A Graduate Course in Applied Cryptography_, Ch. 11, public-key encryption: https://toc.cryptobook.us/
- `[G x]` — Goldreich, _Foundations of Cryptography, Vol. 2: Basic Applications_, Cambridge University Press, 2004, Ch. 5 (sample chapter: https://assets.cambridge.org/97805218/30843/excerpt/9780521830843_excerpt.pdf). Read through a summarizer; check the wording against the book.
- `[BSW11 x]` — Boneh, Segev, Waters, _Targeted Malleability: Homomorphic Encryption for Restricted Computations_ (ePrint 2011/311): https://eprint.iacr.org/2011/311.pdf. Definition 2.2 read through a summarizer.
- `[BDPR98]` — M. Bellare, A. Desai, D. Pointcheval, P. Rogaway, _Relations Among Notions of Security for Public-Key Encryption Schemes_, CRYPTO 1998; full version: https://www.di.ens.fr/david.pointcheval/Documents/Papers/1998_crypto.pdf
- `[HHK17]` — Hofheinz, Hövelmanns, Kiltz, _A Modular Analysis of the Fujisaki-Okamoto Transformation_, TCC 2017 (ePrint 2017/604): https://eprint.iacr.org/2017/604
- `[T x]` — Gentry, _A Fully Homomorphic Encryption Scheme_, PhD thesis, Stanford, 2009: https://crypto.stanford.edu/craig/craig-thesis.pdf
- `[carried]` — kept from the previous version of this note; its source was not re-checked in this pass.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

> [!todo] Draft of the PKE rewrite — delete this block when you are done
> - **Goldreich viewpoint (2026-10-14):** the syntax follows `[G Def 5.1.1]`, with the house name $\mathsf{KeyGen}$ for $G$: $\mathsf{KeyGen}(1^\lambda)$, spaces as subsets of $\{0,1\}^*$. [BS Def 11.3] (system parameters) is gone; its role is played by the optional context $\mathrm{aux}$.
> - **Not carried over:** `## Construction` and `## Case Study`; they stay in [[Public-Key Encryption Scheme (Old)]].
> - **Removed by you, to add back when needed:** Injectivity, Min-Entropy, Rigidity, Non-Malleability, the KDM pointer, Relations (SS ⟹ CPA). Their older versions are in the Old note.
> - **Links:** after the rename, links elsewhere in the vault still point to the Old note (Obsidian updated them). Re-point them when you swap in this note.

## Syntax

> [!definition] Parameters
> - $\lambda$: the security parameter, given to $\mathsf{KeyGen}$ in unary $1^\lambda$ `[G Def 5.1.1]`. All algorithms run in probabilistic polynomial time in $\lambda$.
> - $\mathrm{aux}$: the **context**, output by a context generator $\mathcal P(1^\lambda)$ and shared by everyone who uses the scheme (a group description, a ring dimension, …). It is part of both keys. A scheme with no shared context has $\mathrm{aux} = \perp$.
> - $\mathcal M, \mathcal C \subseteq \{0,1\}^*$: the plaintext and ciphertext sets, which may depend on $(\lambda, \mathrm{aux})$. `[G]` takes $\mathcal M = \{0,1\}^*$; the length-restricted case is $\mathcal M = \{0,1\}^{\ell(\lambda)}$.
> - $\mathcal R$: the randomness space of $\mathsf{Enc}$. $\mathcal K$: the set of key pairs $(\mathrm{pk}, \mathrm{sk})$ that $\mathsf{KeyGen}$ can output. Neither is named in `[G]`, where keys are bit strings of length $\mathrm{poly}(\lambda)$.

> [!definition] Public-Key Encryption Scheme `[G Def 5.1.1]`
> A **public-key encryption scheme** $\mathsf{PKE} = (\mathsf{KeyGen}, \mathsf{Enc}, \mathsf{Dec})$ is a triple of efficient algorithms:
> - $(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{KeyGen}(1^\lambda)$: (Randomized) Key-generation algorithm.
>     - **Input**: the security parameter $1^\lambda$. Usually, this algorithm will also run the context generator $\mathcal{P}$ to generate auxiliary $\mathsf{aux}$.
>     - **Output**: a public key $\mathrm{pk}$ and a secret key $\mathrm{sk}$, with $(\mathrm{pk}, \mathrm{sk}) \in \mathcal K$. Both keys contain $\mathrm{aux}$, so $\mathsf{Enc}$ and $\mathsf{Dec}$ do not take it.
> - $c \leftarrow \mathsf{Enc}(\mathrm{pk}, m; r)$: (Randomized) Encryption algorithm.
>     - **Input**: a public key $\mathrm{pk}$, a message $m \in \mathcal M$ and internal randomness $r \in \mathcal R$. Written $\mathsf{Enc}(\mathrm{pk}, m)$ when $r \xleftarrow{\$} \mathcal R$ is left implicit, and $\mathsf{Enc}(\mathrm{pk}, m; r)$ when the coins are fixed, as in [[Fujisaki-Okamoto Transformation]].
>     - **Output**: a ciphertext $c \in \mathcal C$.
> - $m \leftarrow \mathsf{Dec}(\mathrm{sk}, c)$: (Deterministic) Decryption algorithm.
>     - **Input**: a secret key $\mathrm{sk}$ and a ciphertext $c \in \mathcal C$.
>     - **Output**: a message $m \in \mathcal M$, or a special symbol $\perp \notin \mathcal M$ that signals **rejection**.

> [!remark] Notation in the literature
> The form above is the most general one I found: each source below is this definition with an argument fixed or an output forgotten.
>
> | source | algorithms | differences |
> | --- | --- | --- |
> | `[G Def 5.1.1]` | $(G, E, D)$, written $E_e(\alpha)$ and $D_d(\beta)$ | $G(1^n)$ outputs a pair of bit strings $(e, d)$; plaintexts $\alpha \in \{0,1\}^*$; $E$ and $D$ are probabilistic and correctness holds with probability $1$ over both; no reject symbol; key lengths polynomially related to $n$. The same definition covers private-key schemes: the two settings differ only in the security definitions, where the adversary receives $e$ or not. |
> | `[BS Def 11.1]` | $(G, E, D)$ | $G()$ takes no argument; $D$ is deterministic and may output a reject symbol. Definition 11.3 adds $\lambda$ and a system parameter $\Lambda$, which is the context $\mathrm{aux}$ here. |
> | `[T §2.1]` | $\mathsf{KeyGen}_E(\lambda)$, $\mathsf{Encrypt}_E(\mathrm{pk}, \pi)$, $\mathsf{Decrypt}_E(\mathrm{sk}, \psi)$ | $\lambda$ is written, not $1^\lambda$; plaintext $\pi \in P$ and ciphertext $\psi \in C$; $\mathrm{pk}$ itself defines $P$ and $C$; no reject symbol and no explicit coins. |
>
> | `[BDPR98 §2]` | $(\mathcal K, \mathcal E, \mathcal D)$ | $\mathcal K$ takes the security parameter in unary and returns $(\mathrm{pk}, \mathrm{sk})$. |
>
> The vault calls key generation $\mathsf{KeyGen}$ whatever the source writes ([[Note Layouts]] § *Game form*). Other notes leave $\lambda$ implicit ([[Key Encapsulation Mechanism]], [[Symmetric Key Encryption]]); here it is written out because [[Homomorphic Encryption]] imports it.

> [!remark] Context
> - `⚠️ CLAUDE – verify:` $\mathrm{aux}$ is the system parameter $\Lambda \leftarrow P(\lambda)$ of `[BS Def 11.3]`, and has the same role as the $\mathrm{aux}$ returned by the relation generator in [Alinush](https://alinush.github.io/zkps) (see [[Relation Generator]]): produced before the scheme, public. The difference is that here $\mathrm{aux}$ is an input of $\mathsf{KeyGen}$, while there it is adversary-side information. Treating the two as one pattern is my reading. I dropped the rest of `[BS Def 11.3]` (recognizable spaces, an effective length function), since the games only need $|m_0| = |m_1|$.
> - `⚠️ CLAUDE – verify:` for the syntax alone the context is optional: $\mathsf{KeyGen}$ can sample $\mathrm{aux} \leftarrow \mathcal P(1^\lambda)$ itself and keep it in the keys, which is the Goldreich form $\mathsf{KeyGen}(1^\lambda)$. The two differ only when many users share one $\mathrm{aux}$, or when $\mathrm{aux}$ may be chosen adversarially. This is my reasoning, not a quotation.

> [!remark] Conventions
> - $\mathsf{Dec}$ is deterministic with a reject output, as in `[BS Def 11.1]`; `[G Def 5.1.1]` has a probabilistic $D$ and no reject symbol.
> - $\mathsf{Enc}$ is randomized as a deterministic $\mathsf{Enc}$ can not be IND-CPA secure.

## Property

### Correctness

> [!definition] Correctness `[BS Def 11.1]`
> $\mathsf{PKE}$ is **correct** if for every $(\mathrm{pk}, \mathrm{sk}) \in \mathcal K$ and every $m \in \mathcal M$,
> $$\Pr\big[\mathsf{Dec}(\mathrm{sk}, \mathsf{Enc}(\mathrm{pk}, m)) = m\big] = 1,$$
> over the coins of $\mathsf{Enc}$.

> [!definition] Parameters
> - $\delta \in [0, 1]$: the allowed decryption failure probability.

> [!definition] $(1-\delta)$-Correctness `[HHK17]`
> $\mathsf{PKE}$ is **$(1-\delta)$-correct** if
> $$\mathbb E_{(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{KeyGen}}\Big[\min_{m \in \mathcal M} \Pr\big[\mathsf{Dec}(\mathrm{sk}, \mathsf{Enc}(\mathrm{pk}, m)) = m\big]\Big] \geq 1 - \delta.$$

> [!remark]
> `⚠️ CLAUDE – verify:` the previous note had $\max_{m}$ in place of $\min_m$. With $\max$ the condition holds for a scheme that decrypts a single message correctly, so I changed it to $\min$. Equivalently, $\mathbb E[\delta(\mathrm{pk}, \mathrm{sk})] \le \delta$ with $\delta(\mathrm{pk}, \mathrm{sk}) = \max_m \Pr[\mathsf{Dec}(\mathrm{sk}, \mathsf{Enc}(\mathrm{pk}, m)) \ne m]$. I believe this is the formulation of `[HHK17]` but I only read its abstract; check its correctness definition before keeping this.
> Some papers state the same notion through the decryption failure rate; use the definition above when writing.
> `[G Def 5.1.1]` requires probability $1$ and comments that a negligible decryption error, or correctness for all but a negligible fraction of key pairs, is a possible relaxation. $(1-\delta)$-correctness is of the second kind, with $\delta$ concrete instead of negligible. I read this through the sample chapter only.
> Correctness of a homomorphic scheme is a different, stronger statement (all permitted circuits): [[Homomorphic Encryption#Correctness]].

## Security

### Indistinguishability

> [!definition] Parameters
> - $\mathsf{atk} \in \{\mathsf{cpa}, \mathsf{lta}, \mathsf{cca}\}$: the attack; it fixes which decryption queries are allowed.
> - $t$, $\varepsilon$: the running-time bound and the advantage bound.

> [!definition] PKE Indistinguishability Experiment
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pk}$, and decryption answers according to $\mathsf{atk}$:
>     - $\mathsf{cpa}$ (chosen-plaintext attack): no decryption query — rows 2 and 5 are skipped. It has its own note: [[Indistinguishability under Chosen-Plaintext Attack|IND-CPA]].
>     - $\mathsf{lta}$ (lunch-time attack, also CCA1): decryption queries before the challenge only — row 2.
>     - $\mathsf{cca}$ (adaptive chosen-ciphertext attack, also CCA2): decryption queries before and after the challenge — rows 2 and 5 — except on $c^*$ itself.
> - **Promise** — $|m_0| = |m_1|$.
> - **Quantifier** — $\forall \mathcal A$ of running time at most $t$.
> - **Adaptivity** — queries and the choice of $m_0, m_1$ are adaptive. One challenge.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in row 4 only, **Game 0** and **Game 1**. `[BDPR98 Def 2.1]`; `[BSW11 Def 2.2]`.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\mathrm{aux} \leftarrow \mathcal P(1^\lambda)$<br>$(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{KeyGen}(1^\lambda, \mathrm{aux})$ | $\xrightarrow{\ \mathrm{pk}\ }$ | |
> | 2 | | $\xleftarrow{\ c\ }$ | **Decryption queries** (repeated, adaptive; $\mathsf{lta}$ and $\mathsf{cca}$ only): sends $c \in \mathcal C$ |
> | | $m \leftarrow \mathsf{Dec}(\mathrm{sk}, c)$ | $\xrightarrow{\ m\ }$ | |
> | 3 | | $\xleftarrow{\ m_0,\, m_1\ }$ | chooses $m_0, m_1 \in \mathcal M$ with $\lvert m_0 \rvert = \lvert m_1 \rvert$ |
> | 4 | **Game 0**: $c^* \leftarrow \mathsf{Enc}(\mathrm{pk}, m_0)$<br>**Game 1**: $c^* \leftarrow \mathsf{Enc}(\mathrm{pk}, m_1)$ | $\xrightarrow{\ c^*\ }$ | |
> | 5 | | $\xleftarrow{\ c\ }$ | **Decryption queries** (repeated, adaptive; $\mathsf{cca}$ only): sends $c \neq c^*$ |
> | | $m \leftarrow \mathsf{Dec}(\mathrm{sk}, c)$ | $\xrightarrow{\ m\ }$ | |
> | 6 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}^{\mathsf{ind}\text{-}\mathsf{atk}}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart its probabilities of being $1$ in the two games are:
>   $$\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{atk}}_{\mathsf{PKE}}(\mathcal A) = \Big|\Pr\big[\mathsf{Expt}_0^{\mathsf{ind}\text{-}\mathsf{atk}}(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1^{\mathsf{ind}\text{-}\mathsf{atk}}(\mathcal A) = 1\big]\Big|.$$

> [!definition] $(t, \varepsilon)$-IND-ATK Security
> $\mathsf{PKE}$ is **$(t, \varepsilon)$-IND-ATK secure** if for every adversary $\mathcal A$ with running time at most $t$,
> $$\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{atk}}_{\mathsf{PKE}}(\mathcal A) \leq \varepsilon.$$

> [!remark] The source's form
> - `[BDPR98 Def 2.1]` writes the attacks as $\mathsf{cpa}$, $\mathsf{cca1}$, $\mathsf{cca2}$ and gives the two stages of the adversary oracles $\mathcal O_1, \mathcal O_2$: $\mathcal O_1 = \mathcal O_2 = \varepsilon$ for $\mathsf{cpa}$; $\mathcal O_1 = \mathcal D_{\mathrm{sk}}$, $\mathcal O_2 = \varepsilon$ for $\mathsf{cca1}$; $\mathcal O_1 = \mathcal O_2 = \mathcal D_{\mathrm{sk}}$ for $\mathsf{cca2}$, where $A_2$ may not ask for $y = c^*$. Its adversary $A = (A_1, A_2)$ passes a state $s$, and its advantage is $2\Pr[b' = b] - 1$. Here the adversary is one stateful machine and the stages are rows 2 and 5, see [[Security Game]].
> - In the CPA game there is no oracle because $\mathrm{pk}$ is public. Contrast [[Symmetric Key Encryption#Indistinguishability]], where CPA needs an explicit encryption oracle.
> - A lunch-time attack has its decryption access "before lunch", i.e. before the challenge.

> [!remark] Asymptotic security
> `[G]` states security asymptotically: for every probabilistic polynomial-time (or polynomial-size) adversary the advantage is negligible in $\lambda$, and the adversary receives $1^\lambda$, plus the public key in the public-key setting `[G Def 5.2.1–5.2.3]`. A scheme family is IND-ATK secure in this sense when, for every polynomial $t$, every adversary of running time $t(\lambda)$ has advantage negligible in $\lambda$: the $(t, \varepsilon)$ definition above with $\varepsilon = \varepsilon(\lambda)$ negligible. `⚠️ CLAUDE – verify:` `[G]` fixes the pair $(x_n, y_n)$ and uses non-uniform circuits instead of the interactive game above; that the two coincide for non-uniform adversaries is from memory. I read `[G]` through the sample chapter only.

### One-wayness

> [!definition] Parameters
> - $\mathsf{ATK} \in \{\mathsf{CPA}, \mathsf{PCA}, \mathsf{VA}, \mathsf{PCVA}\}$: the attack; it fixes the oracles $\mathcal O_\mathsf{ATK}$.
> - $\mathsf{Pco}(m, c)$: the plaintext-checking oracle, which returns $1$ iff $\mathsf{Dec}(\mathrm{sk}, c) = m$; defined for $m \in \mathcal M$ only.
> - $\mathsf{Cvo}(c)$: the ciphertext-validity oracle, which returns $1$ iff $\mathsf{Dec}(\mathrm{sk}, c) \in \mathcal M$; defined for $c \neq c^*$ only.
>
> `[HHK17 Def 2.1, Fig. 3]`

> [!definition] One-Wayness (OW-ATK)
> ### Scope
> A public-key encryption scheme $\mathsf{PKE}$ with message space $\mathcal M$ and an efficient adversary $\mathcal A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pk}$ and the challenge $c^*$, and the oracles of $\mathsf{ATK}$:
>     - $\mathsf{CPA}$: none;
>     - $\mathsf{PCA}$: $\mathsf{Pco}$;
>     - $\mathsf{VA}$: $\mathsf{Cvo}$;
>     - $\mathsf{PCVA}$: $\mathsf{Pco}$ and $\mathsf{Cvo}$.
> - **Promise** — the challenge message is uniform in $\mathcal M$.
> - **Quantifier** — $\forall$ efficient $\mathcal A$.
> - **Adaptivity** — oracle queries are adaptive, all after $c^*$ is known.
>
> ---
> ### Experiment
> A search game with one branch. `[HHK17 Def 2.1, Fig. 3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{KeyGen}(1^\lambda)$<br>$m^* \xleftarrow{\$} \mathcal M$<br>$c^* \leftarrow \mathsf{Enc}(\mathrm{pk}, m^*)$ | $\xrightarrow{\ \mathrm{pk},\, c^*\ }$ | |
> | 2 | | $\xleftarrow{\ m,\, c\ }$ | **Plaintext-checking queries** ($\mathsf{PCA}$, $\mathsf{PCVA}$; repeated, adaptive): sends $m \in \mathcal M$ and $c$ |
> | | $\beta \leftarrow [\mathsf{Dec}(\mathrm{sk}, c) = m]$ | $\xrightarrow{\ \beta\ }$ | |
> | 3 | | $\xleftarrow{\ c\ }$ | **Validity queries** ($\mathsf{VA}$, $\mathsf{PCVA}$; repeated, adaptive): sends $c \neq c^*$ |
> | | $\beta \leftarrow [\mathsf{Dec}(\mathrm{sk}, c) \in \mathcal M]$ | $\xrightarrow{\ \beta\ }$ | |
> | 4 | | $\xleftarrow{\ m'\ }$ | outputs a message $m'$ |
>
> **Goal** — $\mathcal A$ wins iff:
> - $\mathsf{Dec}(\mathrm{sk}, c^*) = m'$, i.e. $\mathsf{Pco}(m', c^*) = 1$.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{OW}\text{-}\mathsf{ATK}}_{\mathsf{PKE}}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
> - $\mathsf{PKE}$ is **OW-ATK secure** if this is negligible for every efficient $\mathcal A$. `[HHK17 Def 2.1]`
>
> It is a *search* game, see [[Security Game]].

> [!remark] Two details of the source
> - The usual one-wayness game is won iff $m' = m^*$. `[HHK17]` instead checks $m'$ with $\mathsf{Pco}$, i.e. against $\mathsf{Dec}(\mathrm{sk}, c^*)$; for a $\delta$-correct scheme the two games differ statistically by $\delta$. `[HHK17 §2.1]`
> - $\mathsf{Pco}$ refuses messages outside $\mathcal M$ (by convention it returns $\perp$ on them); otherwise $\mathsf{Cvo}$ could be simulated by plaintext-checking queries on $\perp$. `[HHK17 §2.1]`
> - `[HHK17 Fig. 3]` writes key generation as $\mathsf{Gen}$ without input and runs the adversary as $m' \leftarrow \mathcal A^{\mathcal O_\mathsf{ATK}}(\mathrm{pk}, c^*)$; here it is one interactive machine that receives row 1.

## Related

### Descendants
- [[Homomorphic Encryption]] — adds $\mathsf{Eval}$ and the permitted circuits $\mathcal C_E$; its own descendants are the table there

### Instantiations
`⚠️ CLAUDE – verify:` the hardness column is from memory, not from the scheme notes; check it before keeping.

| | hardness it rests on |
| --- | --- |
| [[RSA Public Key Cryptosystem]] | RSA / factoring |
| [[Goldwasser–Micali Cryptosystem]] | quadratic residuosity |
| [[ElGamal Public Key Cryptosystem]] | discrete logarithm / DDH |
| [[GGH Public Key Cryptosystem]] | lattice problems (CVP) |
| [[NTRU Public Key Cryptosystem]] | NTRU assumption |
| [[Lindner-Peikert Public Key Encryption]] | LWE |
| [[Lyubashevsky-Peikert-Regev Public Key Encryption]] | Ring-LWE |
| [[Kyber PKE]] | Module-LWE |
| [[Alekhnovich Encryption Scheme]] | decoding / LPN-type problems |
| [[Merkle–Hellman Subset-Sum Cryptosystem]] | subset sum (broken) |

I did not place [[A Congruential Public Key Cryptosystem]], [[ID-based Public Key Cryptosystems]] (a different primitive: identity-based) or [[Massey-Omura Three-Pass Cryptosystem]].

### Constructions
- [[Fujisaki-Okamoto Transformation]] — builds on a PKE and a symmetric scheme
- [[Traitor Tracing Encryption Scheme]], [[Multi-Receiver Encryption Scheme]] — built from a PKE
- [[Blind Signature]] — uses a CPA-secure PKE as a building block

### Properties
- [[Indistinguishability under Chosen-Plaintext Attack|IND-CPA]] (the case atk = cpa of the game in `## Security`), [[Indistinguishability]], [[Key-Dependent Message Security|KDM Security]]
- [[Security Game]], [[Elementary Wrapper]], [[Adversary]] — the tools the games use

### Siblings
- [[Symmetric Key Encryption]] — same triple, one key; the adversary gets no public key
- [[Key Encapsulation Mechanism]] — encrypts a fresh key instead of a message
- [[Public-Key Cryptography]], [[Public-Key Encryption MOC]] — the hubs
