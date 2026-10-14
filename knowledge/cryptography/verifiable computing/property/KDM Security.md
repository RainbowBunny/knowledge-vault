Reference:
- `[BRS x]` — Black, Rogaway, Shrimpton, _Encryption-Scheme Security in the Presence of Key-Dependent Messages_, SAC 2002: https://home.cs.colorado.edu/~jrblack/papers/kdm.pdf
- `[BV x]` — Brakerski, Vaikuntanathan, _Efficient Fully Homomorphic Encryption from (Standard) LWE_, FOCS 2011 (ePrint 2011/344): https://eprint.iacr.org/2011/344.pdf
- `[HK07]` — Halevi, Krawczyk, _Security under Key-Dependent Inputs_, CCS 2007 (ePrint 2007/315): https://eprint.iacr.org/2007/315 (abstract only)
- `[S x]` — Gentry, _Fully Homomorphic Encryption Using Ideal Lattices_, STOC 2009: https://www.cs.cmu.edu/~odonnell/hits09/gentry-homomorphic-encryption.pdf
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - [[Public-Key Encryption Scheme]]: Import $(\lambda, \mathrm{aux}, \mathcal M, \mathcal C, \mathcal R, \mathcal K)$.
> - $\mathcal F$: a class of efficiently computable functions $f$ from secret keys to $\mathcal M$.
> - $\mathbb A$: the class of PPT adversaries.

> [!definition] Key-Dependent Message (KDM) Security
> ### Scope
> A [[Public-Key Encryption Scheme]] $\mathsf{PKE}$, the function class $\mathcal F$ and the [[Adversary]] class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pk}$ and one oracle $\mathcal O$, queried adaptively on functions $f \in \mathcal F$:
>     - Real: $\mathcal O_\mathsf{real}(f) = \mathsf{Enc}(\mathrm{pk}, f(\mathrm{sk}))$.
>     - Fake: $\mathcal O_\mathsf{fake}(f) = \mathsf{Enc}(\mathrm{pk}, 0^{|f(\mathrm{sk})|})$.
> - **Promise** — every $f \in \mathcal F$ has fixed output length: $|f(\mathrm{sk})|$ does not depend on $\mathrm{sk}$ `[BRS Def 4.1]`.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — queries are adaptive; $\mathcal A$ sees $\mathrm{pk}$ before it queries.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{kdm}}_{\mathsf{PKE}, \mathcal F}(\mathcal A) = \left| \Pr\!\left[ b' = 1 \;\middle|\; \begin{array}{l} (\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{Gen}(1^\lambda); \\ b' \leftarrow \mathcal A^{\mathcal O_\mathsf{real}}(\mathrm{pk}) \end{array} \right] - \Pr\!\left[ b' = 1 \;\middle|\; \begin{array}{l} (\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{Gen}(1^\lambda); \\ b' \leftarrow \mathcal A^{\mathcal O_\mathsf{fake}}(\mathrm{pk}) \end{array} \right] \right|.$$
> $\mathsf{PKE}$ is **KDM$[\mathcal F]$-secure** if this advantage is negligible in $\lambda$ for every $\mathcal A \in \mathbb A$. It is a *distinguishing* game, see [[Security Game]].

> [!remark] Provenance of this definition
> `[BRS Def 4.1]` defines KDM security for **symmetric** encryption: the oracle takes a key index $j$ and a deterministic program $g$ that may depend on a whole vector of independently generated keys $K = (K_1, K_2, \dots)$; the Real experiment returns an encryption of $g(K)$ under $K_j$, the Fake experiment an encryption of $|g(K)|$ zero bits. Definition 4.2 is the random-oracle version.
> `⚠️ CLAUDE – verify:` the public-key, single-key version above is my adaptation of that definition (one key pair, functions of $\mathrm{sk}$ only). I did not open a source that states KDM security for public-key encryption (Boneh–Halevi–Hamburg–Ostrovsky, CRYPTO 2008, is where I would look; I have not read it). Check that the paper's function class and fixed-length condition match.

## Variant

### Circular security

> [!definition] Parameters
> - $\mathrm{sk}_j$: the $j$-th bit of $\mathrm{sk}$, for $j \in [1, \ell]$, where $\ell$ is the bit-length of $\mathrm{sk}$.

> [!definition] Weak Circular Security `[BV Def 3.8]`
> $\mathsf{PKE}$ has **weak circular security** if it remains IND-CPA secure when the adversary, in addition to $\mathrm{pk}$, receives encryptions $\mathsf{Enc}(\mathrm{pk}, \mathrm{sk}_j)$ of every bit $\mathrm{sk}_j$ of the secret key, under its own public key.
> This is exactly the bootstrapping key of [[Bootstrappable Encryption]] with $\mathrm{pk}_2 = \mathrm{pk}_1$, which is why it is the assumption of the self-loop in [[Gentry Bootstrapping Transformation]] `[BV Thm 3.2]` `[S §2]`.

> [!remark] Relation to KDM$[\mathcal F]$
> `⚠️ CLAUDE – verify:` let $\mathcal F_\mathsf{proj} = \{\mathrm{sk} \mapsto \mathrm{sk}_j\}_j$ be the bit projections. KDM$[\mathcal F_\mathsf{proj}]$ security implies weak circular security: replace the encrypted key bits by encryptions of zeros (this costs one KDM advantage, by a hybrid), then use plain IND-CPA. I did not check the converse, and I did not find this implication stated in the sources. It is my argument.

### Other axes

- **Number of keys.** `[BRS]` lets the oracle name a key index $j$ in a vector of keys, so a function may depend on all keys (key cycles and cliques). The single-key definition above is the case of one key.
- **Random oracle model.** `[BRS Def 4.2]`: both $g$ and the adversary may query the random oracle $H$.
- **Function class $\mathcal F$.** The strength of the notion depends on $\mathcal F$. Other classes (for example affine functions of the key) are studied in later work that I did not read.

## Property

> [!remark] Relations
> - KDM security implies IND-CPA, but not conversely `[BRS §4]`.
> - `⚠️ CLAUDE – verify:` for the first half, take $\mathcal F$ to contain the constant functions: then $\mathcal O_\mathsf{real}(f_m) = \mathsf{Enc}(\mathrm{pk}, m)$ against $\mathcal O_\mathsf{fake}(f_m) = \mathsf{Enc}(\mathrm{pk}, 0^{|m|})$, which is IND-CPA against the all-zero message. That is my argument for the public-key case; `[BRS §4]` states it for symmetric encryption.

## Example

### IND-CPA does not imply KDM security `[BRS §2]`

> [!example] A separation
> Given an IND-CPA secure symmetric scheme $\mathsf{E}$, define $\mathsf{E}'_K(M) = 0 \,\|\, \mathsf{E}_K(M)$ if $M \ne K$, and $1 \,\|\, K$ if $M = K$. $\mathsf{E}'$ is still IND-CPA secure (an adversary that does not know $K$ will not submit $M = K$), but an encryption of its own key is the key itself `[BRS §2]`.
> `⚠️ CLAUDE – verify:` the public-key analogue, $\mathsf{Enc}'(\mathrm{pk}, m) = 0 \,\|\, \mathsf{Enc}(\mathrm{pk}, m)$ if $m \ne \mathrm{sk}$ and $1 \,\|\, \mathrm{sk}$ if $m = \mathrm{sk}$, is my adaptation and is only meant as an illustration; it needs $\mathrm{sk} \in \mathcal M$.

### Positive results

- `[BRS Thm 5.1]`: in the random oracle model, the symmetric scheme $\mathsf{E}_K(M, R) = R \,\|\, (H(K \| R) \oplus M)$ is KDM secure; the advantage is bounded by $q^2/2^{k-2}$, $q$ counting all encryption and random-oracle queries. `[BRS §1]` leaves a standard-model KDM-secure scheme as an open problem (as of 2002).
- `[HK07]` (abstract only): extends the study to deterministic symmetric primitives and the standard model, and shows that many natural constructions fail, including some proven secure in the random oracle model.
- For lattice schemes, the working assumption in `[BV]` is exactly weak circular security (above); no proof from LWE alone is claimed there.

## Related

- [[Public-Key Encryption Scheme]] — the base primitive and its CPA/CCA games
- [[Bootstrappable Encryption]], [[Gentry Bootstrapping Transformation]], [[Fully Homomorphic Encryption]]
- [[Security Game]], [[Adversary]]
