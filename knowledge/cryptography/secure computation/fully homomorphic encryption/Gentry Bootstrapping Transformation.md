Reference:
- `[S x]` — Gentry, _Fully Homomorphic Encryption Using Ideal Lattices_, STOC 2009: https://www.cs.cmu.edu/~odonnell/hits09/gentry-homomorphic-encryption.pdf
- `[T x]` — Gentry, _A Fully Homomorphic Encryption Scheme_, PhD thesis, Stanford, 2009: https://crypto.stanford.edu/craig/craig-thesis.pdf
- `[C x]` — Gentry, _Computing Arbitrary Functions of Encrypted Data_ (CACM): https://dl.acm.org/doi/pdf/10.1145/1666420.1666444
- `[BV x]` — Brakerski, Vaikuntanathan, _Efficient Fully Homomorphic Encryption from (Standard) LWE_, FOCS 2011 (ePrint 2011/344): https://eprint.iacr.org/2011/344.pdf
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Syntax

> [!definition] Parameters
> - [[Homomorphic Encryption]]: Import $(\lambda)$.
> - [[Leveled Fully Homomorphic Encryption]]: Import $(\Gamma, d)$.
> - [[Bootstrappable Encryption]]: Import $(\ell, f_\mathsf{Dec})$.

> [!definition] Building Blocks
> - $E = (\mathsf{KeyGen}, \mathsf{Enc}, \mathsf{Dec}, \mathsf{Eval})$: any [[Bootstrappable Encryption|bootstrappable]] [[Homomorphic Encryption]] with respect to $\Gamma$ (universally quantified).

> [!definition] Gentry Bootstrapping Transformation `[S §2]` `[C §4.3]`
> The output is the family $\{E^{(d)}\}$. Keys are indexed as in `[S §2]`: ciphertexts enter under $\mathrm{pk}_d$ and are decrypted with $\mathrm{sk}_0$.
> - $(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{KeyGen}^{(d)}(1^\lambda)$: (Randomized) Key-generation algorithm.
>     - **Input**: the security parameter $1^\lambda$ (and the depth $d$ of Parameters).
>     - **Output**: a public key $\mathrm{pk}$, made of the $d+1$ public keys of $E$ and a chain of encrypted secret keys, and a secret key $\mathrm{sk} = \mathrm{sk}_0$.
>     - **Steps**:
>         1. $(\mathrm{pk}_i, \mathrm{sk}_i) \leftarrow E.\mathsf{KeyGen}(1^\lambda)$ for $i \in [0, d]$.
>         2. $\mathrm{bk}^{(i)} \leftarrow E.\mathsf{BKGen}(\mathrm{pk}_{i-1}, \mathrm{sk}_i)$ for $i \in [1, d]$, that is, $\mathrm{bk}^{(i)}_j = E.\mathsf{Enc}(\mathrm{pk}_{i-1}, \mathrm{sk}_{i,j})$ for $j \in [1, \ell]$.
>         3. Return $\mathrm{pk} = \big((\mathrm{pk}_i)_{i \in [0,d]}, (\mathrm{bk}^{(i)})_{i \in [1,d]}\big)$ and $\mathrm{sk} = \mathrm{sk}_0$.
> - $c \leftarrow \mathsf{Enc}^{(d)}(\mathrm{pk}, m)$: (Randomized) Encryption algorithm.
>     - **Input**: a public key $\mathrm{pk}$ and a message $m \in \mathcal M$.
>     - **Output**: a ciphertext $c$ under $\mathrm{pk}_d$.
>     - **Steps**: Return $E.\mathsf{Enc}(\mathrm{pk}_d, m)$.
> - $m \leftarrow \mathsf{Dec}^{(d)}(\mathrm{sk}, c)$: (Deterministic) Decryption algorithm.
>     - **Input**: the secret key $\mathrm{sk} = \mathrm{sk}_0$ and a ciphertext $c$ under $\mathrm{pk}_0$.
>     - **Output**: a message $m \in \mathcal M$ (or $\perp$).
>     - **Steps**: Return $E.\mathsf{Dec}(\mathrm{sk}_0, c)$.
> - $c \leftarrow \mathsf{Eval}^{(d)}(\mathrm{pk}, C, (c_1, \dots, c_t))$: (Possibly randomized) Evaluation algorithm.
>     - **Input**: a public key $\mathrm{pk}$; a circuit $C$ over $\Gamma$ of depth at most $d$; ciphertexts $c_1, \dots, c_t$ under $\mathrm{pk}_d$.
>     - **Output**: a ciphertext under $\mathrm{pk}_0$ of $C(m_1, \dots, m_t)$.
>     - **Steps**: evaluate $C$ level by level, starting from the input level $d$. For a gate $g$ at level $i \in [1, d]$ whose inputs are ciphertexts $\psi_1, \dots, \psi_a$ under $\mathrm{pk}_i$ ($a$ is the arity of $g$), with bits $\psi_{k,j}$:
>         1. $\psi_{k,j}' \leftarrow E.\mathsf{Enc}(\mathrm{pk}_{i-1}, \psi_{k,j})$.
>         2. The output of the gate is $E.\mathsf{Eval}\big(\mathrm{pk}_{i-1}, f_{\mathsf{Dec},g}, (\mathrm{bk}^{(i)}, \psi')\big)$, a ciphertext under $\mathrm{pk}_{i-1}$.
>
>         The result at level $0$ is a ciphertext under $\mathrm{pk}_0$. Each gate costs one [[Bootstrappable Encryption|Refresh]] plus the gate itself, in a single $E.\mathsf{Eval}$ call.

> [!remark] Provenance of the algorithms
> `⚠️ CLAUDE – verify:` the previous Homomorphic Encryption note described $E^{(d)}$ in prose (keys; level-by-level evaluation; the two index conventions). Writing it as four algorithms, and the formula for the gate step, is my formalization of that prose. Check it against `[S §2]` before keeping it, in particular: (a) how wires that skip a level are handled (I expect the identity gate $\mathsf{id} \in \Gamma$ is used for this, which would explain why $\mathsf{id}$ is required in $\Gamma$ `[S Def 4]`; that is my guess); (b) the index convention. `[C §4.3]` chains keys upward ($\mathrm{sk}_i$ under $\mathrm{pk}_{i+1}$), `[S §2]` the other way, as above.

> [!remark] Notation in the literature
> The output family is written with the superscript $(d)$ for the depth. Key generation is $\mathsf{KeyGen}$, as $\mathsf{KeyGen}_E$ in `[S §1.1]` and `[T §2.1]`.
>
> | source | algorithms | differences |
> | --- | --- | --- |
> | `[S §2]` | $\mathsf{KeyGen}_E(\lambda, d)$, $\mathsf{Encrypt}_E$, $\mathsf{Decrypt}_E$, $\mathsf{Evaluate}_E^{(\delta)}$ | the depth $d$ is an input of key generation; $\delta$ indexes the level. Ciphertexts enter under $\mathrm{pk}_d$ and are decrypted with $\mathrm{sk}_0$. |
> | `[C §4.3]` | same construction | keys are chained the other way: $\mathrm{sk}_i$ under $\mathrm{pk}_{i+1}$. |
> | `[BV Def 3.6]` | $\mathsf{HE.Keygen}(1^\kappa, 1^L)$ | the depth bound $L$ is a unary input; only the bit-length of the evaluation key depends on $L$. |

## Property

### Correctness

> [!theorem] Leveled homomorphism `[S Thm 3]` `[T Thm 1.3.1, informal]`
> If $E$ is bootstrappable with respect to $\Gamma$, then $\{E^{(d)}\}$ is [[Leveled Fully Homomorphic Encryption|leveled fully homomorphic]] for circuits with gates in $\Gamma$.
> - With $\Gamma$ universal (for example NAND), $E^{(d)}$ handles every circuit of depth $d$ `[T Thm 1.3.1]`. $\Gamma$ may even contain gates that are depth-$m$ circuits, giving depth $d \cdot m$ `[S §2]`.
> - The public key of $E^{(d)}$ is $O(d)$ times that of $E$. The decryption circuit and the cost of encryption are unchanged. Evaluation is polynomial in $\lambda$ and linear in $|C|$ `[T Thm 1.3.1]`.

> [!theorem] Cost `[S Thm 5]`
> For a circuit with $s$ wires and depth $d$, $\mathsf{Eval}^{(d)}$ makes at most $s \ell d$ calls to $E.\mathsf{Enc}$ and at most $s d$ calls to $E.\mathsf{Eval}$ on circuits in $\mathcal D_E(\Gamma)$.

> [!remark] Why leveled and not fully homomorphic `[T §1.3]` `[C §4.4]`
> $E^{(d)}$ needs $d+1$ key pairs, so key generation and the public key grow with $d$, and the depth must be fixed in advance.

## Security

### Indistinguishability

> [!definition] Parameters
> - $\varepsilon$: the IND-CPA advantage of the adversary $\mathcal A$ against $E^{(d)}$. $\mathcal B$: the adversary against $E$ built from $\mathcal A$.

> [!security] Security of $E^{(d)}$ `[S Thm 4]`
> For any [[Indistinguishability under Chosen-Plaintext Attack|IND-CPA]] adversary $\mathcal A$ against $E^{(d)}$ with advantage $\varepsilon$, there is an IND-CPA adversary $\mathcal B$ against $E$, running in time $\mathrm{poly}(\ell, d)$ times that of $\mathcal A$, with
> $$\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{cpa}}_{E}(\mathcal B) \geq \frac{\varepsilon}{\ell\,(d+1)}.$$
> The only hypothesis on the building block $E$ is its semantic security; no circular-security assumption is needed `[S Thm 4]`.

## Variant

### Self-loop: unbounded depth

> [!definition] Parameters
> - $(\mathrm{pk}, \mathrm{sk})$: the single key pair of the self-loop; $\mathrm{sk} = (\mathrm{sk}_1, \dots, \mathrm{sk}_\ell)$ in bits.
> - $\mathrm{bk}_j$: the bootstrapping key, an encryption of the bit $\mathrm{sk}_j$ under $\mathrm{pk}$.

> [!theorem] Unbounded FHE under KDM security `[S §2]` `[T §1.3]` `[BV Thm 3.2]`
> If $E$ is bootstrappable and [[Key-Dependent Message Security|circular secure]], replace the key chain by one key pair $(\mathrm{pk}, \mathrm{sk})$ and the bootstrapping key $\mathrm{bk}_j \leftarrow E.\mathsf{Enc}(\mathrm{pk}, \mathrm{sk}_j)$, so that $\mathsf{Refresh}$ runs with $\mathrm{pk}_2 = \mathrm{pk}_1$. The result is [[Fully Homomorphic Encryption|fully homomorphic]], its keys do not depend on the circuit depth, and its security follows from the KDM security of $E$ `[S §2]`.
> - `[BV Thm 3.2, Def 3.8]` states this with *weak circular security* (IND-CPA stays secure when the adversary also gets encryptions of every bit of the secret key).
> - I do not state a concrete advantage bound for this variant: the notes I worked from give none.

> [!remark] History `[S fn 3]`
> Gentry first used the self-loop and tried to prove KDM security; Canetti suggested the acyclic leveled chain above to avoid needing it.

> [!remark] In the random oracle model `[T §1.3]`
> Bootstrappable encryption is shown to imply a scheme that is both bootstrappable and KDM-secure; thesis Chapter 4 has a section on it (I only saw the table of contents).

## Related

### Properties
- [[Key-Dependent Message Security|KDM Security]] — needed by the self-loop variant
- [[Indistinguishability]] — the notion preserved, with loss $\varepsilon/(\ell(d+1))$

### Siblings
- [[Fujisaki-Okamoto Transformation]] — another transformation in this vault with the same layout

### Prerequisites
- [[Bootstrappable Encryption]], [[Leveled Fully Homomorphic Encryption]], [[Fully Homomorphic Encryption]], [[Public-Key Encryption Scheme]]
