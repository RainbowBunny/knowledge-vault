---
aliases: [KDM Security]
---
Reference:
- `[BHHO08]` — D. Boneh, S. Halevi, M. Hamburg, R. Ostrovsky, _Circular-Secure Encryption from Decision Diffie-Hellman_, CRYPTO 2008: https://www.iacr.org/archive/crypto2008/51570109/51570109.pdf
- `[BRS x]` — Black, Rogaway, Shrimpton, _Encryption-Scheme Security in the Presence of Key-Dependent Messages_, SAC 2002: https://home.cs.colorado.edu/~jrblack/papers/kdm.pdf
- `[BV x]` — Brakerski, Vaikuntanathan, _Efficient Fully Homomorphic Encryption from (Standard) LWE_, FOCS 2011 (ePrint 2011/344): https://eprint.iacr.org/2011/344.pdf
- `[HK07]` — Halevi, Krawczyk, _Security under Key-Dependent Inputs_, CCS 2007 (ePrint 2007/315): https://eprint.iacr.org/2007/315 (abstract only)
- `[S x]` — Gentry, _Fully Homomorphic Encryption Using Ideal Lattices_, STOC 2009: https://www.cs.cmu.edu/~odonnell/hits09/gentry-homomorphic-encryption.pdf

## Definition

> [!definition] Parameters
> - [[Public-Key Encryption Scheme]]: Import $(\lambda, \mathrm{aux}, \mathcal M, \mathcal C, \mathcal R, \mathcal K)$.
> - $n$: the number of key pairs. $\mathcal F$: a set of functions $f$ from $n$-tuples of secret keys to $\mathcal M$ whose output length $|f(z)|$ is the same for all inputs $z$.
> - $\mathbb A$: the class of adversaries running in expected polynomial time.
>
> `[BHHO08 §2.1]`

> [!definition] Key-Dependent Message (KDM) Security
> ### Scope
> A [[Public-Key Encryption Scheme]] $\mathsf{PKE}$, the number of keys $n$, the function set $\mathcal F$ and the [[Adversary]] class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pk}_1, \dots, \mathrm{pk}_n$ and asks queries $(i, f)$ with $1 \leq i \leq n$ and $f \in \mathcal F$.
> - **Promise** — every $f \in \mathcal F$ has a fixed output length, so $0^{|y|}$ in Game 1 does not depend on the keys.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — queries are adaptive; $\mathcal A$ sees all public keys first.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in the answer to each query, **Game 0** (real) and **Game 1** (zeros). `[BHHO08 §2.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\mathrm{aux} \leftarrow \mathcal P(1^\lambda)$<br>$(\mathrm{pk}_j, \mathrm{sk}_j) \leftarrow \mathsf{KeyGen}(1^\lambda, \mathrm{aux})$ for $j = 1, \dots, n$ | $\xrightarrow{\ \mathrm{pk}_1, \dots, \mathrm{pk}_n\ }$ | |
> | 2 | | $\xleftarrow{\ i,\, f\ }$ | **KDM queries** (repeated, adaptive): sends $i \in [n]$ and $f \in \mathcal F$ |
> | | $y \leftarrow f(\mathrm{sk}_1, \dots, \mathrm{sk}_n)$<br>**Game 0**: $c \leftarrow \mathsf{Enc}(\mathrm{pk}_i, y)$<br>**Game 1**: $c \leftarrow \mathsf{Enc}(\mathrm{pk}_i, 0^{\lvert y \rvert})$ | $\xrightarrow{\ c\ }$ | |
> | 3 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{kdm}(n)}_{\mathsf{PKE}, \mathcal F}(\mathcal A) = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
> $\mathsf{PKE}$ is **$n$-way KDM-secure with respect to $\mathcal F$** if this advantage is negligible in $\lambda$ for every $\mathcal A \in \mathbb A$ `[BHHO08 Def 1]`. It is a *distinguishing* game, see [[Security Game]].

> [!remark] Notation in the literature
> - `[BHHO08]` writes the key generator $G(\lambda)$, picks a random bit $b$ at the start and measures $\mathsf{KDM}^{(n)}\mathsf{Adv}[\mathcal A, \mathcal E](\lambda) = |\Pr[W] - 1/2|$ with $W$ the event $b' = b$: half the advantage above, see [[Indistinguishability under Chosen-Plaintext Attack#Bit-guessing form]].
> - `[BRS Def 4.1]` introduced the notion for **symmetric** encryption: the oracle takes a key index $j$ and a deterministic program $g$ of the whole key vector $K = (K_1, K_2, \dots)$, and returns an encryption of $g(K)$ under $K_j$ (Real) or of $|g(K)|$ zero bits (Fake); Definition 4.2 is the random-oracle version.

## Variant

### Circular security

> [!definition] Parameters
> - $\mathrm{sk}_j$: the $j$-th bit of $\mathrm{sk}$, for $j \in [1, \ell]$, where $\ell$ is the bit-length of $\mathrm{sk}$.

> [!definition] Weak Circular Security `[BV Def 3.8]`
> $\mathsf{PKE}$ has **weak circular security** if it remains IND-CPA secure when the adversary, in addition to $\mathrm{pk}$, receives encryptions $\mathsf{Enc}(\mathrm{pk}, \mathrm{sk}_j)$ of every bit $\mathrm{sk}_j$ of the secret key, under its own public key.
> This is exactly the bootstrapping key of [[Bootstrappable Encryption]] with $\mathrm{pk}_2 = \mathrm{pk}_1$, which is why it is the assumption of the self-loop in [[Gentry Bootstrapping Transformation]] `[BV Thm 3.2]` `[S §2]`.

> [!remark] Circular security from KDM
> A set $\mathcal F$ is *non-trivial* if it contains all constant functions and the $n$ selector functions $f_i(x_1, \dots, x_n) = x_i$. The selector functions give the adversary $\mathsf{Enc}(\mathrm{pk}_i, \mathrm{sk}_j)$ for all $i, j$, which is circular security; `[BHHO08]` treats circular security this way rather than as a separate definition. `[BHHO08 Thm 1]` builds a scheme from DDH that is $n$-way KDM-secure for the affine functions, a non-trivial set.

### Other axes

- **Number of keys.** The definition above has $n$ key pairs and functions of all secret keys, which covers key cycles; $n = 1$ is the single-key case.
- **Random oracle model.** `[BRS Def 4.2]`: both $g$ and the adversary may query the random oracle $H$.
- **Function class $\mathcal F$.** The strength of the notion depends on $\mathcal F$: `[BHHO08]` achieves the affine functions.

## Property

> [!proposition] KDM security with constants implies IND-CPA, not conversely
> If $\mathcal F$ contains the constant functions, a query $(i, f_m)$ with $f_m \equiv m$ is answered by $\mathsf{Enc}(\mathrm{pk}_i, m)$ in Game 0 and $\mathsf{Enc}(\mathrm{pk}_i, 0^{|m|})$ in Game 1, so KDM security gives semantic security `[BHHO08 §2.1]`. The converse fails `[BRS §2]`, by the example below.

## Example

### IND-CPA does not imply KDM security `[BRS §2]`

> [!example] A separation
> Given an IND-CPA secure symmetric scheme $\mathsf{E}$, define $\mathsf{E}'_K(M) = 0 \,\|\, \mathsf{E}_K(M)$ if $M \ne K$, and $1 \,\|\, K$ if $M = K$. $\mathsf{E}'$ is still IND-CPA secure (an adversary that does not know $K$ will not submit $M = K$), but an encryption of its own key is the key itself `[BRS §2]`.

### Positive results

- `[BRS Thm 5.1]`: in the random oracle model, the symmetric scheme $\mathsf{E}_K(M, R) = R \,\|\, (H(K \| R) \oplus M)$ is KDM secure; the advantage is bounded by $q^2/2^{k-2}$, $q$ counting all encryption and random-oracle queries. `[BRS §1]` leaves a standard-model KDM-secure scheme as an open problem (as of 2002).
- `[HK07]` (abstract only): extends the study to deterministic symmetric primitives and the standard model, and shows that many natural constructions fail, including some proven secure in the random oracle model.
- For lattice schemes, the working assumption in `[BV]` is exactly weak circular security (above); no proof from LWE alone is claimed there.

## Related

### Descendants
- Weak circular security — a variant in `## Variant` above, the notion `[BV Def 3.8]` uses

### Constructions
- [[Gentry Bootstrapping Transformation]] — the self-loop needs circular security
- [[Bootstrappable Encryption]] — publishing $\mathrm{bk}$

### Siblings
- [[Indistinguishability]] — the base game this one extends with key-dependent messages

### Prerequisites
- [[Public-Key Encryption Scheme]], [[Security Game]], [[Adversary]]
