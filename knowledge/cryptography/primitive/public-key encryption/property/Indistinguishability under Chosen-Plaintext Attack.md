---
aliases: [IND-CPA, CPA Security, CPA]
---
Reference:
- `[BS x]` — Boneh, Shoup, _A Graduate Course in Applied Cryptography_, Ch. 11: https://toc.cryptobook.us/ (Attack Games 11.1 and 11.2, Definitions 11.2 and 11.4, Eq. 11.1). Carried over from the PKE note of this vault; not re-read in this pass.
- `[BSW11 Def 2.2]` — Boneh, Segev, Waters, _Targeted Malleability: Homomorphic Encryption for Restricted Computations_ (ePrint 2011/311): https://eprint.iacr.org/2011/311.pdf. Read through a summarizer, not verbatim.
- `[G Def 5.2.1–5.2.3]` — Goldreich, _Foundations of Cryptography, Vol. 2_, Ch. 5 (sample chapter). Read through a summarizer.
- `#supplemented` marks what I added to your text; its source is on this line. Delete the tag once you have read it.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - [[Public-Key Encryption Scheme]]: Import $(\lambda, \mathrm{aux}, \mathcal M, \mathcal C, \mathcal R, \mathcal K)$.
> - $\mathbb A$: the class of efficient [[Adversary|adversaries]]. $t$: the running-time bound, $\varepsilon$: the advantage bound.
> - $\mathcal A = (\mathcal A_\mathsf{find}, \mathcal A_\mathsf{guess})$: the two phases of one adversary.
> - $q$: the number of challenges, in the multi-challenge variant only.

> [!definition] Indistinguishability under Chosen-Plaintext Attack
> ### Scope
> A [[Public-Key Encryption Scheme]] $\mathsf{PKE}$ and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pk}$ and nothing else: no oracle. It can encrypt by itself, because $\mathrm{pk}$ is public.
> - **Promise** — the two challenge messages have equal length, $|m_0| = |m_1|$.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — $\mathcal A_\mathsf{find}$ sees $\mathrm{pk}$ before it chooses $m_0, m_1$. One challenge.
>
> ---
> ### Experiment
> An interaction between a challenger $\mathcal C$ and $\mathcal A$, played in two branches that differ in step 3 only: **Game 0** and **Game 1**.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\mathrm{aux} \leftarrow \mathcal P(1^\lambda)$; $(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{Gen}(1^\lambda, \mathrm{aux})$ | $\xrightarrow{\ \mathrm{pk}\ }$ | |
> | 2 | | $\xleftarrow{\ m_0,\, m_1\ }$ | $(m_0, m_1) \leftarrow \mathcal A_\mathsf{find}(\mathrm{pk})$ |
> | 3 | **Game 0**: $c^* \leftarrow \mathsf{Enc}(\mathrm{pk}, m_0)$<br>**Game 1**: $c^* \leftarrow \mathsf{Enc}(\mathrm{pk}, m_1)$ | $\xrightarrow{\ c^*\ }$ | |
> | 4 | | $\xleftarrow{\ b'\ }$ | $b' \leftarrow \mathcal A_\mathsf{guess}(c^*)$ |
>
> **Target** — one bit: $\mathsf{Expt}_b(\mathcal A)$ is the bit $b'$ that $\mathcal A$ outputs in Game $b$. The property compares the two bits' distributions.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{cpa}}_{\mathsf{PKE}}(\mathcal A) = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
> $\mathsf{PKE}$ is **$(t, \varepsilon)$-IND-CPA secure** if $\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{cpa}}_{\mathsf{PKE}}(\mathcal A) \leq \varepsilon$ for every $\mathcal A \in \mathbb A$ with running time at most $t$, and **IND-CPA secure** if $\varepsilon$ is negligible in $\lambda$ for every polynomial $t$. It is a *distinguishing* game, see [[Security Game]].

> [!remark] The phases share memory
> $\mathcal A_\mathsf{find}$ and $\mathcal A_\mathsf{guess}$ are two moments of one adversary: everything $\mathcal A_\mathsf{find}$ computed, in particular $m_0, m_1$, is available to $\mathcal A_\mathsf{guess}$. `[BSW11 Def 2.2]` passes it explicitly as `state` from $\mathcal A_1$ to $\mathcal A_2$.

> [!remark] Names and the other literature
> - `[BSW11 Def 2.2]` writes $\mathsf{Expt}^{\mathsf{CPA}}_{\Pi, \mathcal A, b}(k)$ with $\mathcal A = (\mathcal A_1, \mathcal A_2)$, takes the advantage as $|\Pr[\mathsf{Expt}_0 = 1] - \Pr[\mathsf{Expt}_1 = 1]|$, and calls the property *semantic security against chosen-plaintext attacks*.
> - `[BS]`: the advantage above is $\mathsf{SSadv}[\mathcal A, \mathsf{PKE}]$ of Attack Game 11.1, and **semantic security** is Definition 11.2. The bit-guessing form $|\Pr[b' = b] - 1/2|$ with a uniform $b$ is $\mathsf{SSadv}^*$, and $\mathsf{SSadv} = 2 \cdot \mathsf{SSadv}^*$ (their Eq. 11.1). The interaction form is used here because a reduction moves between Game 0 and Game 1 one step at a time.
> - `[BS]` reserves the name **CPA security** (Definition 11.4, advantage $\mathsf{CPAadv}$) for the multi-challenge game below. `⚠️ CLAUDE – verify:` that the two coincide up to a factor $q$ is the standard hybrid argument, which I state from memory in the variant below; I did not reread the proof in `[BS]`.
> - `[G Def 5.2.1–5.2.3]` states security asymptotically, fixes a pair $(x_n, y_n)$ and uses non-uniform circuits instead of the find–guess form. See the asymptotic remark in [[Public-Key Encryption Scheme#Indistinguishability|the PKE note]].

> [!remark] A deterministic encryption cannot be IND-CPA secure
> If $\mathsf{Enc}$ is deterministic, $\mathcal A_\mathsf{guess}$ computes $\mathsf{Enc}(\mathrm{pk}, m_1)$ itself and outputs $1$ iff it equals $c^*$: the advantage is $1$. This is why $\mathsf{Enc}$ in the base note is randomized. #supplemented

## Variant

### Multi-challenge: CPA security `[BS Def 11.4]`
The adversary asks for $q$ challenges, adaptively, under one hidden branch: step 2 and step 3 repeat for $i = 1, \dots, q$.

| | challenger $\mathcal C$ | | adversary $\mathcal A$ |
| --- | --- | --- | --- |
| 1 | $\mathrm{aux} \leftarrow \mathcal P(1^\lambda)$; $(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{Gen}(1^\lambda, \mathrm{aux})$ | $\xrightarrow{\ \mathrm{pk}\ }$ | |
| 2 | | $\xleftarrow{\ m_{i,0},\, m_{i,1}\ }$ | $\mathcal A$ chooses the $i$-th pair after seeing $\mathrm{pk}, c_1, \dots, c_{i-1}$ |
| 3 | **Game 0**: $c_i \leftarrow \mathsf{Enc}(\mathrm{pk}, m_{i,0})$<br>**Game 1**: $c_i \leftarrow \mathsf{Enc}(\mathrm{pk}, m_{i,1})$ | $\xrightarrow{\ c_i\ }$ | |
| 4 | | $\xleftarrow{\ b'\ }$ | $\mathcal A$ outputs $b'$ after the $q$-th round |

**Target** — one bit, as above, over $q$ challenges. The same branch is used in all rounds; that is what makes the games differ by a hybrid argument, not by $q$ independent experiments.

`⚠️ CLAUDE – verify:` $\mathsf{Adv}_q \leq q \cdot \mathsf{Adv}_1$, by hybrids that switch the challenges from $m_{i,0}$ to $m_{i,1}$ one at a time, and the converse is trivial ($q = 1$). Stated from memory.

### Bit-guessing form
$\mathsf{Adv}^* = |\Pr[b' = b] - 1/2|$ with $b \xleftarrow{\$} \{0, 1\}$ chosen by the challenger; $\mathsf{Adv} = 2 \cdot \mathsf{Adv}^*$ `[BS Eq. 11.1]`. Not used in this vault, see [[Note Layouts]].

### Stronger attacks
Give $\mathcal A$ a decryption oracle before the challenge (lunch-time attack, $\mathsf{atk} = \mathsf{lta}$) or also after it (adaptive chosen ciphertext, $\mathsf{atk} = \mathsf{cca}$): the family game in [[Public-Key Encryption Scheme#Indistinguishability|the PKE note]], of which this note is the case $\mathsf{atk} = \mathsf{cpa}$.

### Secret-key setting
There is no public key, so $\mathcal A$ cannot encrypt by itself and gets an encryption oracle: [[Symmetric Key Encryption#Indistinguishability]] with $\mathsf{atk} = \mathsf{cpa}$.

## Related

### Properties
- Stronger: lta and cca in [[Public-Key Encryption Scheme#Indistinguishability|the PKE family game]]
- Different in kind: [[Key-Dependent Message Security]] (the message may depend on $\mathrm{sk}$; implies IND-CPA, not conversely)
- Needed beside it: [[Circuit Privacy]] and [[Linear-Only Security]] for [[Vector Encryption]] — they speak about $\mathsf{Add}$, which IND-CPA does not mention

### Used by
- [[Gentry Bootstrapping Transformation]] — its theorem is a reduction between two IND-CPA games
- [[Homomorphic Encryption (draft)]] — takes IND-CPA of $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ as the security notion
- [[Blind Signature]] — assumes a CPA-secure PKE (that note still links to the old PKE note)

### Prerequisites
- [[Public-Key Encryption Scheme]], [[Security Game]], [[Adversary]], [[Indistinguishability]]
