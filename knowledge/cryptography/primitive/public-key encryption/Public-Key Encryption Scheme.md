Reference:
- `[BS x]` — Boneh, Shoup, _A Graduate Course in Applied Cryptography_, Ch. 11, public-key encryption: https://toc.cryptobook.us/
- `[G x]` — Goldreich, _Foundations of Cryptography, Vol. 2: Basic Applications_, Cambridge University Press, 2004, Ch. 5 (sample chapter: https://assets.cambridge.org/97805218/30843/excerpt/9780521830843_excerpt.pdf). Read through a summarizer; check the wording against the book.
- `[HHK17]` — Hofheinz, Hövelmanns, Kiltz, _A Modular Analysis of the Fujisaki-Okamoto Transformation_, TCC 2017 (ePrint 2017/604): https://eprint.iacr.org/2017/604
- `[T x]` — Gentry, _A Fully Homomorphic Encryption Scheme_, PhD thesis, Stanford, 2009: https://crypto.stanford.edu/craig/craig-thesis.pdf
- `[carried]` — kept from the previous version of this note; its source was not re-checked in this pass.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

> [!todo] Draft of the PKE rewrite — delete this block when you are done
> - **Goldreich viewpoint (2026-10-14):** the syntax follows `[G Def 5.1.1]`: $\mathsf{Gen}(1^\lambda)$, spaces as subsets of $\{0,1\}^*$. [BS Def 11.3] (system parameters) is gone; its role is played by the optional context $\mathrm{aux}$.
> - **Not carried over:** `## Construction` and `## Case Study`; they stay in [[Public-Key Encryption Scheme (Old)]].
> - **Removed by you, to add back when needed:** Injectivity, Min-Entropy, Rigidity, Non-Malleability, One-way Encryption, the KDM pointer, Relations (SS ⟹ CPA). Their older versions are in the Old note.
> - **Links:** after the rename, links elsewhere in the vault still point to the Old note (Obsidian updated them). Re-point them when you swap in this note.

## Syntax

> [!definition] Parameters
> - $\lambda$: the security parameter, given to $\mathsf{Gen}$ in unary $1^\lambda$ `[G Def 5.1.1]`. All algorithms run in probabilistic polynomial time in $\lambda$.
> - $\mathrm{aux}$: the **context**, output by a context generator $\mathcal P(1^\lambda)$ and shared by everyone who uses the scheme (a group description, a ring dimension, …). It is part of both keys. A scheme with no shared context has $\mathrm{aux} = \perp$.
> - $\mathcal M, \mathcal C \subseteq \{0,1\}^*$: the plaintext and ciphertext sets, which may depend on $(\lambda, \mathrm{aux})$. `[G]` takes $\mathcal M = \{0,1\}^*$; the length-restricted case is $\mathcal M = \{0,1\}^{\ell(\lambda)}$.
> - $\mathcal R$: the randomness space of $\mathsf{Enc}$. $\mathcal K$: the set of key pairs $(\mathrm{pk}, \mathrm{sk})$ that $\mathsf{Gen}$ can output. Neither is named in `[G]`, where keys are bit strings of length $\mathrm{poly}(\lambda)$.

> [!definition] Public-Key Encryption Scheme `[G Def 5.1.1]`
> A **public-key encryption scheme** $\mathsf{PKE} = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ is a triple of efficient algorithms over the spaces of Parameters. The context generator $\mathcal P$ is not one of them: it runs first, and its output is an input of $\mathsf{Gen}$.
> - $(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{Gen}(1^\lambda, \mathrm{aux})$: (Randomized) Key-generation algorithm.
>     - **Input**: the security parameter $1^\lambda$ and the context $\mathrm{aux}$. Written $\mathsf{Gen}(1^\lambda)$ when $\mathrm{aux} = \perp$.
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
> I did not open Katz–Lindell or `[HHK17]` for their notation. In the vault, other notes write $\mathsf{Gen}()$ with $\lambda$ implicit ([[Key Encapsulation Mechanism]], [[Symmetric Key Encryption]]); here $\lambda$ is written out because [[Homomorphic Encryption]] imports it.

> [!remark] Context
> - `⚠️ CLAUDE – verify:` $\mathrm{aux}$ is the system parameter $\Lambda \leftarrow P(\lambda)$ of `[BS Def 11.3]`, and has the same role as the $\mathrm{aux}$ returned by the relation generator in [Alinush](https://alinush.github.io/zkps) (see [[Relation Generator]]): produced before the scheme, public. The difference is that here $\mathrm{aux}$ is an input of $\mathsf{Gen}$, while there it is adversary-side information. Treating the two as one pattern is my reading. I dropped the rest of `[BS Def 11.3]` (recognizable spaces, an effective length function), since the games only need $|m_0| = |m_1|$.
> - `⚠️ CLAUDE – verify:` for the syntax alone the context is optional: $\mathsf{Gen}$ can sample $\mathrm{aux} \leftarrow \mathcal P(1^\lambda)$ itself and keep it in the keys, which is the Goldreich form $\mathsf{Gen}(1^\lambda)$. The two differ only when many users share one $\mathrm{aux}$, or when $\mathrm{aux}$ may be chosen adversarially. This is my reasoning, not a quotation.

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
> $$\mathbb E_{(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{Gen}}\Big[\min_{m \in \mathcal M} \Pr\big[\mathsf{Dec}(\mathrm{sk}, \mathsf{Enc}(\mathrm{pk}, m)) = m\big]\Big] \geq 1 - \delta.$$

> [!remark]
> `⚠️ CLAUDE – verify:` the previous note had $\max_{m}$ in place of $\min_m$. With $\max$ the condition holds for a scheme that decrypts a single message correctly, so I changed it to $\min$. Equivalently, $\mathbb E[\delta(\mathrm{pk}, \mathrm{sk})] \le \delta$ with $\delta(\mathrm{pk}, \mathrm{sk}) = \max_m \Pr[\mathsf{Dec}(\mathrm{sk}, \mathsf{Enc}(\mathrm{pk}, m)) \ne m]$. I believe this is the formulation of `[HHK17]` but I only read its abstract; check its correctness definition before keeping this.
> Some papers state the same notion through the decryption failure rate; use the definition above when writing.
> `[G Def 5.1.1]` requires probability $1$ and comments that a negligible decryption error, or correctness for all but a negligible fraction of key pairs, is a possible relaxation. $(1-\delta)$-correctness is of the second kind, with $\delta$ concrete instead of negligible. I read this through the sample chapter only.
> Correctness of a homomorphic scheme is a different, stronger statement (all permitted circuits): [[Homomorphic Encryption#Correctness]].

## Security

### Indistinguishability

> [!definition] Parameters
> - $\mathsf{atk} \in \{\mathsf{cpa}, \mathsf{lta}, \mathsf{cca}\}$: the attack.
> - $\mathcal O_\mathsf{find}$, $\mathcal O_\mathsf{guess}$: the oracles of the two phases, fixed by $\mathsf{atk}$.
> - $t$, $\varepsilon$: the running-time bound and the advantage bound.

> [!definition] PKE Indistinguishability Advantage
> For an [[Adversary]] $\mathcal A = (\mathcal A_\mathsf{find}, \mathcal A_\mathsf{guess})$ and $\mathsf{atk} \in \{\mathsf{cpa}, \mathsf{lta}, \mathsf{cca}\}$, define the advantage
> $$\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{atk}}_{\mathsf{PKE}}(\mathcal A) = \left|\; \Pr\!\left[ b = b' \;\middle|\; \begin{array}{l} \mathrm{aux} \leftarrow \mathcal P(1^\lambda); (\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{Gen}(1^\lambda, \mathrm{aux}); \\ (m_0, m_1, s) \leftarrow \mathcal A_\mathsf{find}^{\mathcal O_\mathsf{find}}(\mathrm{pk}); \\ b \xleftarrow{\$} \{0, 1\}; \; c^* \leftarrow \mathsf{Enc}(\mathrm{pk}, m_b); \\ b' \leftarrow \mathcal A_\mathsf{guess}^{\mathcal O_\mathsf{guess}}(s, c^*) \end{array} \right] - \frac{1}{2} \right|.$$
> Where:
> 1. **Chosen plaintext attack**, $\mathsf{atk} = \mathsf{cpa}$: $\mathcal O_\mathsf{find}(\cdot) = \varepsilon$ and $\mathcal O_\mathsf{guess}(\cdot) = \varepsilon$ (no oracle; $\mathcal A$ encrypts by itself with $\mathrm{pk}$).
> 2. **Lunch-time attack**, $\mathsf{atk} = \mathsf{lta}$ (sometimes $\mathsf{cca1}$): $\mathcal O_\mathsf{find}(\cdot) = \mathsf{Dec}(\mathrm{sk}, \cdot)$ and $\mathcal O_\mathsf{guess}(\cdot) = \varepsilon$.
> 3. **Adaptive chosen ciphertext attack**, $\mathsf{atk} = \mathsf{cca}$: $\mathcal O_\mathsf{find}(\cdot) = \mathsf{Dec}(\mathrm{sk}, \cdot)$ and $\mathcal O_\mathsf{guess}(\cdot) = \mathsf{Dec}(\mathrm{sk}, \cdot)$.
>
> Also:
> 4. The output of $\mathcal A_\mathsf{find}$ satisfies $|m_0| = |m_1|$.
> 5. For $\mathsf{atk} = \mathsf{cca}$, $\mathcal A_\mathsf{guess}$ may not query $\mathcal O_\mathsf{guess}$ on $c^*$.

> [!definition] $(t, \varepsilon)$-IND-ATK Security
> $\mathsf{PKE}$ is **$(t, \varepsilon)$-IND-ATK secure** if for every adversary $\mathcal A$ with running time at most $t$,
> $$\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{atk}}_{\mathsf{PKE}}(\mathcal A) \leq \varepsilon.$$

> [!remark]
> - ATK is a placeholder for the attack. A lunch-time attack has one oracle phase, "before lunch".
> - Relation to `[BS]`: with $\mathsf{atk} = \mathsf{cpa}$ the advantage above is the bit-guessing advantage $\mathsf{SSadv}^*[\mathcal A, \mathsf{PKE}]$ of Attack Game 11.1, and $\mathsf{SSadv} = 2 \cdot \mathsf{SSadv}^*$ (their Eq. 11.1). **Semantic security** is Definition 11.2. The multi-query game, where $\mathcal A$ submits a sequence of message pairs, is Attack Game 11.2 with advantage $\mathsf{CPAadv}$; **CPA security** is Definition 11.4.
> - In the CPA game the oracle is empty because $\mathrm{pk}$ is public. Contrast [[Symmetric Key Encryption#Indistinguishability]], where CPA needs an explicit encryption oracle.


> [!remark] Asymptotic security
> `[G]` states security asymptotically: for every probabilistic polynomial-time (or polynomial-size) adversary the advantage is negligible in $\lambda$, and the adversary receives $1^\lambda$, plus the public key in the public-key setting `[G Def 5.2.1–5.2.3]`. A scheme family is IND-ATK secure in this sense when, for every polynomial $t$, every adversary of running time $t(\lambda)$ has advantage negligible in $\lambda$: the $(t, \varepsilon)$ definition above with $\varepsilon = \varepsilon(\lambda)$ negligible. `⚠️ CLAUDE – verify:` `[G]` fixes the pair $(x_n, y_n)$ and uses non-uniform circuits instead of the find–guess form above; that the two coincide for non-uniform adversaries is from memory. I read `[G]` through the sample chapter only.

## Related

- [[Public-Key Cryptography]], [[Public-Key Encryption MOC]]
- [[Symmetric Key Encryption]], [[Key Encapsulation Mechanism]], [[Fujisaki-Okamoto Transformation]]
- [[Homomorphic Encryption]] extends this note; [[KDM Security]]
- [[Security Game]], [[Indistinguishability]], [[Elementary Wrapper]], [[Adversary]]
