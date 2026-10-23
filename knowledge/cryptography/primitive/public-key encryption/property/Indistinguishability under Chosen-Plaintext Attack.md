---
aliases: [IND-CPA, CPA Security, CPA]
---
Reference:
- `[BDPR98]` — M. Bellare, A. Desai, D. Pointcheval, P. Rogaway, _Relations Among Notions of Security for Public-Key Encryption Schemes_, CRYPTO 1998; full version: https://www.di.ens.fr/david.pointcheval/Documents/Papers/1998_crypto.pdf
- `[BS x]` — Boneh, Shoup, _A Graduate Course in Applied Cryptography_, Ch. 11: https://toc.cryptobook.us/ (Attack Games 11.1 and 11.2, Definitions 11.2 and 11.4, Eq. 11.1).
- `[BSW11 Def 2.2]` — Boneh, Segev, Waters, _Targeted Malleability: Homomorphic Encryption for Restricted Computations_ (ePrint 2011/311): https://eprint.iacr.org/2011/311.pdf
- `[G Def 5.2.1–5.2.3]` — Goldreich, _Foundations of Cryptography, Vol. 2_, Ch. 5 (sample chapter).
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - [[Public-Key Encryption Scheme]]: Import $(\lambda, \mathrm{aux}, \mathcal M, \mathcal C, \mathcal R, \mathcal K)$.
> - $\mathbb A$: the class of efficient [[Adversary|adversaries]]. $t$: the running-time bound. $\varepsilon$: the advantage bound.
> - $q$: the number of challenges, in the multi-challenge variant only.

> [!definition] Indistinguishability under Chosen-Plaintext Attack
> ### Scope
> A [[Public-Key Encryption Scheme]] $\mathsf{PKE} = (\mathsf{KeyGen}, \mathsf{Enc}, \mathsf{Dec})$ and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pk}$ and nothing else: no oracle. It can encrypt by itself, because $\mathrm{pk}$ is public.
> - **Promise** — the two challenge messages have equal length, $|m_0| = |m_1|$.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — $\mathcal A$ chooses $m_0, m_1$ after seeing $\mathrm{pk}$. One challenge.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in row 3 only, **Game 0** and **Game 1**. `[BDPR98 Def 2.1]` with $\mathsf{atk} = \mathsf{cpa}$; `[BS Attack Game 11.1]`.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\mathrm{aux} \leftarrow \mathcal P(1^\lambda)$<br>$(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{KeyGen}(1^\lambda, \mathrm{aux})$ | $\xrightarrow{\ \mathrm{pk}\ }$ | |
> | 2 | | $\xleftarrow{\ m_0,\, m_1\ }$ | chooses $m_0, m_1 \in \mathcal M$ with $\lvert m_0 \rvert = \lvert m_1 \rvert$ |
> | 3 | **Game 0**: $c^* \leftarrow \mathsf{Enc}(\mathrm{pk}, m_0)$<br>**Game 1**: $c^* \leftarrow \mathsf{Enc}(\mathrm{pk}, m_1)$ | $\xrightarrow{\ c^*\ }$ | |
> | 4 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{cpa}}_{\mathsf{PKE}}(\mathcal A) = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
> - $\mathsf{PKE}$ is **$(t, \varepsilon)$-IND-CPA secure** if $\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{cpa}}_{\mathsf{PKE}}(\mathcal A) \leq \varepsilon$ for every $\mathcal A \in \mathbb A$ with running time at most $t$.
> - $\mathsf{PKE}$ is **IND-CPA secure** if the advantage is negligible in $\lambda$ for every polynomial-time $\mathcal A$ `[BDPR98 Def 2.1]`.
>
> It is a *distinguishing* game, see [[Security Game]].

> [!remark] Names and the other literature
> - `[BDPR98 Def 2.1]` writes the scheme as $\Pi = (\mathcal K, \mathcal E, \mathcal D)$ and the adversary as $A = (A_1, A_2)$: $A_1$ receives $\mathrm{pk}$ and outputs $(x_0, x_1, s)$ with a state $s$, a random bit $b$ is chosen, and $A_2$ receives $(x_0, x_1, s, y)$ for $y \leftarrow \mathcal E_{\mathrm{pk}}(x_b)$. Its advantage $2 \Pr[b' = b] - 1$ equals $\Pr[\mathsf{Expt}_1 = 1] - \Pr[\mathsf{Expt}_0 = 1]$, since $2\Pr[b' = b] - 1 = \Pr[b' = 1 \mid b = 1] - \Pr[b' = 1 \mid b = 0]$. Here the adversary is one stateful machine, so no $s$ is passed — see [[Security Game]].
> - `[BSW11 Def 2.2]` writes $\mathsf{Expt}^{\mathsf{CPA}}_{\Pi, \mathcal A, b}(k)$ with $\mathcal A = (\mathcal A_1, \mathcal A_2)$ passing a `state`, takes the advantage $|\Pr[\mathsf{Expt}_0 = 1] - \Pr[\mathsf{Expt}_1 = 1]|$, and calls the property *semantic security against chosen-plaintext attacks*.
> - `[BS]`: the advantage above is $\mathsf{SSadv}[\mathcal A, \mathsf{PKE}]$ of Attack Game 11.1, and **semantic security** is Definition 11.2. The bit-guessing form $|\Pr[b' = b] - 1/2|$ with a uniform $b$ is $\mathsf{SSadv}^*$, and $\mathsf{SSadv} = 2 \cdot \mathsf{SSadv}^*$ (their Eq. 11.1). `[BS]` reserves the name **CPA security** (Definition 11.4) for the multi-challenge game below.
> - `[G Def 5.2.1–5.2.3]` states security asymptotically with non-uniform adversaries and a fixed pair $(x_n, y_n)$. See the asymptotic remark in [[Public-Key Encryption Scheme#Indistinguishability|the PKE note]].

> [!remark] A deterministic encryption cannot be IND-CPA secure
> If $\mathsf{Enc}$ is deterministic, $\mathcal A$ computes $\mathsf{Enc}(\mathrm{pk}, m_1)$ itself after row 3 and outputs $1$ iff it equals $c^*$: the advantage is $1$. This is why $\mathsf{Enc}$ in the base note is randomized.

## Variant

### Multi-challenge: CPA security `[BS Def 11.4]`

The adversary asks for $q$ challenges, adaptively, under one hidden branch: rows 2 and 3 repeat for $i = 1, \dots, q$. `[BS Attack Game 11.2]`

| | challenger $\mathcal C$ | | adversary $\mathcal A$ |
| --- | --- | --- | --- |
| 1 | $\mathrm{aux} \leftarrow \mathcal P(1^\lambda)$<br>$(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{KeyGen}(1^\lambda, \mathrm{aux})$ | $\xrightarrow{\ \mathrm{pk}\ }$ | |
| 2 | | $\xleftarrow{\ m_{i,0},\, m_{i,1}\ }$ | **Challenge queries** (repeated, adaptive, $q$ times): chooses $m_{i,0}, m_{i,1} \in \mathcal M$ of equal length |
| 3 | **Game 0**: $c_i \leftarrow \mathsf{Enc}(\mathrm{pk}, m_{i,0})$<br>**Game 1**: $c_i \leftarrow \mathsf{Enc}(\mathrm{pk}, m_{i,1})$ | $\xrightarrow{\ c_i\ }$ | |
| 4 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |

**Goal**
- **Output** — the bit $b'$ after the $q$-th challenge; the same branch is used in every round.
- **Measure** — how far apart its distributions in Game 0 and Game 1 are.

`⚠️ CLAUDE – verify:` $\mathsf{Adv}_q \leq q \cdot \mathsf{Adv}_1$, by hybrids that switch the challenges from $m_{i,0}$ to $m_{i,1}$ one at a time; the converse is the case $q = 1$. Stated from memory; `[BS]` proves the relation in Chapter 11.

### Bit-guessing form
$\mathsf{Adv}^* = |\Pr[b' = b] - 1/2|$ with $b \xleftarrow{\$} \{0, 1\}$ chosen by the challenger; $\mathsf{Adv} = 2 \cdot \mathsf{Adv}^*$ `[BS Eq. 11.1]`. Not used in this vault, see [[Note Layouts]].

### Stronger attacks
Decryption queries before the challenge (lunch-time attack, $\mathsf{atk} = \mathsf{lta}$, also CCA1) or before and after it (adaptive chosen-ciphertext attack, $\mathsf{atk} = \mathsf{cca}$, also CCA2): the family game in [[Public-Key Encryption Scheme#Indistinguishability|the PKE note]], of which this note is the case $\mathsf{atk} = \mathsf{cpa}$ `[BDPR98 Def 2.1]`.

### Secret-key setting
There is no public key, so $\mathcal A$ cannot encrypt by itself and gets an encryption oracle: [[Symmetric Key Encryption#Indistinguishability]] with $\mathsf{atk} = \mathsf{cpa}$.

## Related

### Properties
- Stronger: lta and cca in [[Public-Key Encryption Scheme#Indistinguishability|the PKE family game]]
- Different in kind: [[Key-Dependent Message Security]] — the message may depend on $\mathrm{sk}$; with the constant functions in its class it implies IND-CPA
- Needed beside it: [[Circuit Privacy]] and [[Linear-Only Security]] for [[Vector Encryption]] — they speak about $\mathsf{Add}$, which IND-CPA does not mention

### Used by
- [[Gentry Bootstrapping Transformation]] — its theorem is a reduction between two IND-CPA games
- [[Homomorphic Encryption (draft)]] — takes IND-CPA of $(\mathsf{KeyGen}, \mathsf{Enc}, \mathsf{Dec})$ as the security notion
- [[Blind Signature]] — assumes a CPA-secure PKE

### Prerequisites
- [[Public-Key Encryption Scheme]], [[Security Game]], [[Adversary]], [[Indistinguishability]]
