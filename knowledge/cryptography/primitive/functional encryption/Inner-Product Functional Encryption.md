---
aliases: [IPFE]
---
Reference:
- `[ABPSY17]` — S. Agrawal, S. Bhattacherjee, D. H. Phan, D. Stehlé, S. Yamada, _Efficient Public Trace and Revoke from Standard Assumptions_, ACM CCS 2017, pp. 2277–2293. Numbers refer to the full version, ePrint 2017/650: https://eprint.iacr.org/2017/650.pdf
- `[ABDP15]` — M. Abdalla, F. Bourse, A. De Caro, D. Pointcheval, _Simple Functional Encryption Schemes for Inner Products_, PKC 2015: https://www.iacr.org/archive/pkc2015/90200150/90200150.pdf (also ePrint 2015/017)
- `[BSW11]` — D. Boneh, A. Sahai, B. Waters, _Functional Encryption: Definitions and Challenges_, TCC 2011: https://www.iacr.org/archive/tcc2011/65970250/65970250.pdf (also ePrint 2010/543)

## Syntax

> [!definition] Parameters
> - $\lambda$: the security parameter. $\ell$: the vector length, given in unary $1^\ell$.
> - $p$: the modulus; vectors live in $\mathbb Z_p^\ell$.
> - $\mathbf x \in \mathbb Z_p^\ell$: a key vector. $\mathbf y \in \mathbb Z_p^\ell$: a message vector.
>
> `[ABPSY17 Def 2]`

> [!definition] Inner-Product Functional Encryption
> Extends:: [[Functional Encryption]].
>
> ---
> A **functional encryption scheme for the inner-product functionality over $\mathbb Z_p$** is a tuple $\mathcal{FE} = (\mathsf{Setup}, \mathsf{KeyGen}, \mathsf{Enc}, \mathsf{Dec})$ of four PPT algorithms:
> - $(\mathrm{pk}, \mathrm{msk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$:
> 	- **Input**: the security parameter and the vector length.
> 	- **Output**: a public key $\mathrm{pk}$ and a master secret key $\mathrm{msk}$.
> - $\mathrm{sk}_\mathbf x \leftarrow \mathsf{KeyGen}(\mathrm{msk}, \mathbf x)$:
> 	- **Input**: $\mathrm{msk}$ and a vector $\mathbf x \in \mathbb Z_p^\ell$.
> 	- **Output**: the secret key $\mathrm{sk}_\mathbf x$.
> - $\mathrm{ct}_\mathbf y \leftarrow \mathsf{Enc}(\mathrm{pk}, \mathbf y)$:
> 	- **Input**: $\mathrm{pk}$ and a message $\mathbf y \in \mathbb Z_p^\ell$.
> 	- **Output**: the ciphertext $\mathrm{ct}_\mathbf y$.
> - $v \leftarrow \mathsf{Dec}(\mathrm{sk}_\mathbf x, \mathrm{ct}_\mathbf y)$:
> 	- **Input**: a secret key $\mathrm{sk}_\mathbf x$ and a ciphertext $\mathrm{ct}_\mathbf y$.
> 	- **Output**: an element of $\mathbb Z_p \cup \{\perp\}$.
>
> `[ABPSY17 Def 2]`

> [!remark] As a functionality
> In the terms of [[Functional Encryption]]: key space and message space $\mathbb Z_p^\ell$, and $F(\mathbf x, \mathbf y) = \langle \mathbf x, \mathbf y \rangle \bmod p$ `[ABDP15]`. `[ABDP15]` mentions no empty key; the length $\ell$ is public anyway.

> [!remark] Notation in the literature
> | source | algorithms | differences |
> | --- | --- | --- |
> | `[ABPSY17 Def 2]` | $(\mathsf{FE.Setup}, \mathsf{FE.KeyGen}, \mathsf{FE.Enc}, \mathsf{FE.Dec})$ | as above; its security game calls the public key $\mathrm{mpk}$ |
> | `[ABDP15]` | $(\mathsf{Setup}, \mathsf{KeyDer}, \mathsf{Encrypt}, \mathsf{Decrypt})$ | $\mathsf{Setup}(1^\lambda) \to (\mathrm{mpk}, \mathrm{msk})$; $\mathsf{Decrypt}(\mathrm{mpk}, \mathrm{Ct}, \mathrm{sk}_k)$ also takes the public key |
>
> In this vault $\mathbb Z_p$ means the integers modulo $p$, not the [[p-adic Number|$p$-adic integers]].

## Property

### Correctness

> [!definition] Correctness
> With overwhelming probability over the randomness of the algorithms: for $(\mathrm{pk}, \mathrm{msk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$ and all $\mathbf x, \mathbf y \in \mathbb Z_p^\ell$,
> $$\mathsf{Dec}\big(\mathsf{KeyGen}(\mathrm{msk}, \mathbf x), \mathsf{Enc}(\mathrm{pk}, \mathbf y)\big) = \langle \mathbf x, \mathbf y \rangle \bmod p.$$
> `[ABPSY17 Def 2]`

> [!remark] Small inner products in the DDH scheme
> In the DDH-based scheme of `[ABDP15]`, decryption ends with a discrete logarithm in base $g$, so the inner product must have small magnitude and the scheme suits small message spaces only. `[ABPSY17 §5.1]` restricts the exponents in the same way.

## Security

### IND-CPA

Specializes [[Indistinguishability under Chosen-Plaintext Attack]].

> [!definition] IND-CPA for Inner-Product Functional Encryption
> ### Scope
> An IPFE scheme $\mathcal{FE}$ and a PPT adversary $\mathcal A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ gets $\mathrm{pk}$ and secret keys for vectors of its choice, before and after the challenge.
> - **Promise** — admissibility: every queried $\mathbf x$, before or after the challenge, satisfies
>   $$\langle \mathbf x, \mathbf y_0 \rangle = \langle \mathbf x, \mathbf y_1 \rangle \bmod p.$$
>   Otherwise decrypting $\mathrm{ct}^*$ with $\mathrm{sk}_\mathbf x$ would tell the branch.
> - **Quantifier** — $\forall$ PPT admissible $\mathcal A$.
> - **Adaptivity** — key queries are adaptive; $\mathbf y_0, \mathbf y_1$ are chosen after the first round of keys. One challenge.
>
> ---
> ### Experiment
> Two branches that differ in row 4 only: **Game 0** and **Game 1**. `[ABPSY17 Def 3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{pk}, \mathrm{msk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$ | $\xrightarrow{\ \mathrm{pk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x\ }$ | **Key queries** (repeated, adaptive): sends $\mathbf x \in \mathbb Z_p^\ell$ |
> | | $\mathrm{sk}_\mathbf x \leftarrow \mathsf{KeyGen}(\mathrm{msk}, \mathbf x)$ | $\xrightarrow{\ \mathrm{sk}_\mathbf x\ }$ | |
> | 3 | | $\xleftarrow{\ \mathbf y_0,\, \mathbf y_1\ }$ | chooses distinct $\mathbf y_0, \mathbf y_1 \in \mathbb Z_p^\ell$, admissible for every $\mathbf x$ of row 2 |
> | 4 | **Game 0**: $\mathrm{ct}^* \leftarrow \mathsf{Enc}(\mathrm{pk}, \mathbf y_0)$<br>**Game 1**: $\mathrm{ct}^* \leftarrow \mathsf{Enc}(\mathrm{pk}, \mathbf y_1)$ | $\xrightarrow{\ \mathrm{ct}^*\ }$ | |
> | 5 | | $\xleftarrow{\ \mathbf x\ }$ | **Key queries** (repeated, adaptive): sends an admissible $\mathbf x$ |
> | | $\mathrm{sk}_\mathbf x \leftarrow \mathsf{KeyGen}(\mathrm{msk}, \mathbf x)$ | $\xrightarrow{\ \mathrm{sk}_\mathbf x\ }$ | |
> | 6 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{cpa}}_{\mathcal{FE}}(\mathcal A) = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
> $\mathcal{FE}$ is **IND-CPA secure** if this is negligible for every PPT admissible $\mathcal A$.

> [!remark] The source's form
> `[ABPSY17 Def 3]` samples $b$, encrypts $\mathbf y_b$, and defines the advantage as $|\Pr[b' = b] - 1/2|$: half the difference above, see [[Indistinguishability under Chosen-Plaintext Attack#Bit-guessing form]]. `[ABDP15]` splits its adversary into procedures with oracle access; here it is one stateful machine, see [[Security Game]].

## Variant

### Selective security
The challenge vectors are fixed before the public key is seen: $\mathcal A$ sends $\mathbf y_0, \mathbf y_1$ as its first message, then the game runs as above (**s-IND-CPA**). `[ABDP15]` prove their DDH scheme s-IND-CPA secure (Thm 1) and claim only selective security.

### Random-key bounded collusion
**$Q$-IND-CPA** `[ABPSY17 §2.2]`: the challenger samples random vectors $\mathbf x \leftarrow \mathbb Z_p^\ell$ and shows them to $\mathcal A$, which asks for keys of an adaptively chosen subset of at most $Q$ of them, and makes no key query after the challenge. Admissibility is the same.

| | challenger $\mathcal C$ | | adversary $\mathcal A$ |
| --- | --- | --- | --- |
| 1 | $(\mathrm{pk}, \mathrm{msk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$<br>$\mathbf x_1, \mathbf x_2, \ldots \leftarrow \mathbb Z_p^\ell$ | $\xrightarrow{\ \mathrm{pk},\, \mathbf x_1, \mathbf x_2, \ldots\ }$ | |
| 2 | | $\xleftarrow{\ j\ }$ | **Key queries** (repeated, adaptive, at most $Q$ times): sends an index $j$ |
| | $\mathrm{sk}_{\mathbf x_j} \leftarrow \mathsf{KeyGen}(\mathrm{msk}, \mathbf x_j)$ | $\xrightarrow{\ \mathrm{sk}_{\mathbf x_j}\ }$ | |
| 3 | | $\xleftarrow{\ \mathbf y_0,\, \mathbf y_1\ }$ | chooses $\mathbf y_0, \mathbf y_1$, admissible for every queried $\mathbf x_j$ |
| 4 | **Game 0**: $\mathrm{ct}^* \leftarrow \mathsf{Enc}(\mathrm{pk}, \mathbf y_0)$<br>**Game 1**: $\mathrm{ct}^* \leftarrow \mathsf{Enc}(\mathrm{pk}, \mathbf y_1)$ | $\xrightarrow{\ \mathrm{ct}^*\ }$ | |
| 5 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |

**Goal** — as above: the output bit $b'$, and how far apart its distributions in the two games are.

The letters change inside `[ABPSY17]`: in §4.2, $Q$ is the number of random vectors and the number of key queries is bounded by $L$ (Thm 18 says "$L$-IND-CPA").

## Related

### Used by
- [[Trace-and-Revoke Scheme]] — built from any IPFE scheme with $\ell = t + r + 1$; random-key bounded-collusion security suffices `[ABPSY17 Thm 15, 16]`

### Prerequisites
- [[Functional Encryption]], [[Security Game]], [[Indistinguishability under Chosen-Plaintext Attack]]
