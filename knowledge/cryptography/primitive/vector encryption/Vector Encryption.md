Reference:
- `[ISW21]` — Y. Ishai, H. Su, D. J. Wu, _Shorter and Faster Post-Quantum Designated-Verifier zkSNARKs from Lattices_, ACM CCS 2021; full version ePrint 2021/977: https://eprint.iacr.org/2021/977.pdf
- `[BISW17]` — D. Boneh, Y. Ishai, A. Sahai, D. J. Wu, _Lattice-Based SNARGs and Their Application to More Efficient Obfuscation_, EUROCRYPT 2017; ePrint 2017/240: https://eprint.iacr.org/2017/240.pdf
- `[LUNA]` — R. Steinfeld, A. Sakzad, M. F. Esgin, V. Kuchta, M. Yassi, R. K. Zhao, _LUNA: Quasi-Optimally Succinct Designated-Verifier Zero-Knowledge Arguments from Lattices_, ACM CCS 2024; ePrint 2022/1690: https://eprint.iacr.org/2022/1690.pdf

## Syntax

> [!definition] Parameters
> - $\lambda$: the security parameter. $\ell$: the plaintext dimension, given in unary $1^\ell$.
> - $\mathbb F$: a finite field; plaintexts are vectors in $\mathbb F^\ell$.
> - $\mathrm{pp}$: the public parameters. $\mathrm{sk}$: the secret key.
> - $n$: the number of ciphertexts one $\mathsf{Add}$ combines; $c_1, \dots, c_n \in \mathbb F$ its scalars.
>
> `[ISW21 Def 3.3]`

> [!definition] Vector Encryption
> A **secret-key additively-homomorphic vector encryption scheme** over $\mathbb F^\ell$ is a tuple $\Pi_\mathsf{Enc} = (\mathsf{Setup}, \mathsf{Enc}, \mathsf{Dec}, \mathsf{Add})$:
> - $(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$:
> 	- **Input**: the security parameter $\lambda$ and the plaintext dimension $\ell$.
> 	- **Output**: public parameters $\mathrm{pp}$ and a secret key $\mathrm{sk}$.
> - $\mathrm{ct} \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf v)$:
> 	- **Input**: the secret key and a vector $\mathbf v \in \mathbb F^\ell$.
> 	- **Output**: a ciphertext $\mathrm{ct}$.
> - $\mathbf v / \perp \leftarrow \mathsf{Dec}(\mathrm{sk}, \mathrm{ct})$:
> 	- **Input**: the secret key and a ciphertext.
> 	- **Output**: a vector $\mathbf v \in \mathbb F^\ell$, or the symbol $\perp$.
> - $\mathrm{ct}^* \leftarrow \mathsf{Add}(\mathrm{pp}, \{\mathrm{ct}_i\}_{i \in [n]}, \{c_i\}_{i \in [n]})$:
> 	- **Input**: the public parameters, ciphertexts $\mathrm{ct}_1, \dots, \mathrm{ct}_n$ and scalars $c_1, \dots, c_n \in \mathbb F$.
> 	- **Output**: a new ciphertext $\mathrm{ct}^*$.
>
> `[ISW21 Def 3.3]`

> [!remark] Notation in the literature
> | source | algorithms | differences |
> | --- | --- | --- |
> | `[ISW21 Def 3.3]` | $(\mathsf{Setup}, \mathsf{Encrypt}, \mathsf{Decrypt}, \mathsf{Add})$ | as above, with $\mathsf{Encrypt}$, $\mathsf{Decrypt}$ for $\mathsf{Enc}$, $\mathsf{Dec}$ |
> | `[BISW17 Def 4.1]` | $(\mathsf{Setup}, \mathsf{Encrypt}, \mathsf{Decrypt})$ | over $\mathbb Z_p^\ell$; $\mathsf{Setup}$ outputs only $\mathrm{sk}$; no $\mathsf{Add}$ |
> | `[LUNA §4.1]` | $\mathsf{HGSW}.(\mathsf{Setup}, \mathsf{Encrypt}, \mathsf{Add}, \mathsf{Decrypt})$ | $\mathsf{Encrypt}(i, \mathrm{sk}, \boldsymbol\mu)$ takes a message index $i$; the output of $\mathsf{Add}$ has a different format from a fresh ciphertext — see [[Module HGSW]] |

## Property

### Additive homomorphism

> [!definition] Additive Homomorphism
> For all $\lambda \in \mathbb N$, vectors $\mathbf v_1, \dots, \mathbf v_k \in \mathbb F^\ell$ and scalars $y_1, \dots, y_k \in \mathbb F$, where $k = k(\lambda)$:
> $$\Pr\Big[\mathsf{Dec}(\mathrm{sk}, \mathrm{ct}^*) = \sum_{i \in [k]} y_i \mathbf v_i\Big] = 1 - \mathsf{negl}(\lambda),$$
> where
> - $(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$,
> - $\mathrm{ct}_i \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf v_i)$ for all $i \in [k]$,
> - $\mathrm{ct}^* \leftarrow \mathsf{Add}(\mathrm{pp}, \{\mathrm{ct}_i\}_{i \in [k]}, \{y_i\}_{i \in [k]})$.
>
> `[ISW21 Def 3.3, Eq. (3.1)]`

> [!remark] Relative to a set, and correctness
> - $\Pi_\mathsf{Enc}$ is additively homomorphic **with respect to a set** $S \subseteq R_p^k$ if the equation holds for all $(y_1, \dots, y_k) \in S$. Here $R_p = R / pR$ for $R = \mathbb Z[x]/(x^d + 1)$; for $d = 2$ and $p \equiv 3 \pmod 4$, $R_p \cong \mathbb F_{p^2}$. ISW21 instantiate it with $S = \{\mathbf y : \lVert \mathbf y \rVert_1 \leq B_1,\ \lVert \mathbf y \rVert_2 \leq B_2\}$. `[ISW21 Def 3.3, §1.2, §3.3, Thm 3.12]`
> - Additive homomorphism implies correctness of decryption (take $k = 1$, $y_1 = 1$). `[ISW21 Def 3.3]`

## Security

### CPA security

> [!definition] CPA Security
> ### Scope
> A vector encryption scheme $\Pi_\mathsf{Enc}$ and an efficient adversary $\mathcal A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pp}$ and an encryption oracle for pairs of vectors; in the $Q$-query version, at most $Q$ queries.
> - **Promise** — none.
> - **Quantifier** — $\forall$ efficient $\mathcal A$.
> - **Adaptivity** — queries are adaptive, all under the same hidden branch.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in the oracle's answer only, **Game 0** and **Game 1**. `[ISW21 Def 3.3, Eq. (3.2)]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$ | $\xrightarrow{\ \mathrm{pp}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf v_0,\, \mathbf v_1\ }$ | **Encryption queries** (repeated, adaptive, at most $Q$ times): sends $\mathbf v_0, \mathbf v_1 \in \mathbb F^\ell$ |
> | | **Game 0**: $\mathrm{ct} \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf v_0)$<br>**Game 1**: $\mathrm{ct} \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf v_1)$ | $\xrightarrow{\ \mathrm{ct}\ }$ | |
> | 3 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^\mathsf{cpa}_{\Pi_\mathsf{Enc}}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
> - $\Pi_\mathsf{Enc}$ is **CPA secure** if this is negligible for every efficient $\mathcal A$, and **$Q$-query CPA secure** if so for every efficient $\mathcal A$ making at most $Q$ queries. `[ISW21 Def 3.3]`
>
> It is a *distinguishing* game, see [[Security Game]].

> [!remark] The source's form
> `[ISW21 Eq. (3.2)]` samples $b \leftarrow \{0, 1\}$, gives $\mathcal A$ the oracle $\mathcal O_b(\mathrm{sk}, \cdot, \cdot)$ that answers $(\mathbf v_0, \mathbf v_1)$ with $\mathsf{Encrypt}(\mathrm{sk}, \mathbf v_b)$, and asks $\Pr[\mathcal A^{\mathcal O_b}(1^\lambda, \mathrm{pp}) = b] = \frac12 + \mathsf{negl}(\lambda)$: the bit-guessing form, half the difference above; see [[Indistinguishability under Chosen-Plaintext Attack#Bit-guessing form]]. The scheme is secret-key, so the oracle is how $\mathcal A$ gets ciphertexts at all.

## Related

### Instantiations
- [[Module HGSW]] — the scheme behind [[LUNA]]

### Constructions
- [[LUNA]] and `[ISW21]` compile a [[Linear Probabilistically Checkable Proofs|linear PCP]] through this primitive

### Properties
- [[Linear-Only Security]] — every valid ciphertext an adversary makes is a linear combination of those it was given, and an extractor finds it
- [[Strictly Linear Targeted Malleability]] — the simulation-based version
- [[Circuit Privacy]] — the output of $\mathsf{Add}$ reveals only $\sum_i y_i \mathbf v_i$

### Siblings
- [[Homomorphic Encryption]] — evaluates arbitrary circuits (public key); here only linear combinations (secret key)
