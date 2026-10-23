Reference:
- `[T x]` — Gentry, _A Fully Homomorphic Encryption Scheme_, PhD thesis, Stanford, 2009: https://crypto.stanford.edu/craig/craig-thesis.pdf
- `[S x]` — Gentry, _Fully Homomorphic Encryption Using Ideal Lattices_, STOC 2009: https://www.cs.cmu.edu/~odonnell/hits09/gentry-homomorphic-encryption.pdf
- `[C x]` — Gentry, _Computing Arbitrary Functions of Encrypted Data_ (CACM): https://dl.acm.org/doi/pdf/10.1145/1666420.1666444
- `[DS16]` — Ducas, Stehlé, _Sanitization of FHE Ciphertexts_, EUROCRYPT 2016 (ePrint 2016/164): https://eprint.iacr.org/2016/164.pdf
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - [[Homomorphic Encryption]]: Import $(\lambda, \mathrm{aux}, \mathcal M, \mathcal C, \mathcal C_E, f_\mathsf{Dec})$.
> - [[Leveled Fully Homomorphic Encryption]]: Import $(\Gamma)$, with the identity gate $\mathsf{id} \in \Gamma$ `[S Def 4]`.
> - $\ell$: the number of elements of $\mathcal M$ (bits, with $\mathcal M = \{0,1\}$ in the sources `[S §1.2]`) used to write a secret key or a ciphertext as input to $f_\mathsf{Dec}$ `[S Def 4]`.

> [!definition] Parameters
> - $g \in \Gamma$: a gate with $t$ inputs.

> [!definition] Augmented Decryption Circuit `[S Def 4]`
> For a gate $g \in \Gamma$ with $t$ inputs, the **$g$-augmented decryption circuit** is $g$ applied to $t$ copies of $f_\mathsf{Dec}$:
> $$f_{\mathsf{Dec},g}(\mathrm{sk}, c_1, \dots, c_t) = g\big(f_\mathsf{Dec}(\mathrm{sk}, c_1), \dots, f_\mathsf{Dec}(\mathrm{sk}, c_t)\big),$$
> where $\mathrm{sk}$ and each $c_j$ are written as elements of $\mathcal M^\ell$. Write $\mathcal D_E(\Gamma)$ for the set of these circuits.
> `⚠️ CLAUDE – verify:` I write one shared $\mathrm{sk}$ for all $t$ copies, as the previous Fully Homomorphic Encryption note did. `[S Def 4]` says "$g$ applied to $t$ copies of $f_\mathsf{Dec}$" and I did not re-check whether each copy has its own key input.

> [!definition] Bootstrappable `[S Def 5]`
> Let $\mathcal C_E$ be a set of circuits for which $E$ is homomorphic. $E$ is **bootstrappable with respect to $\Gamma$** if
> $$\mathcal D_E(\Gamma) \subseteq \mathcal C_E.$$
> Informally: $E$ can evaluate its own decryption circuit, and that circuit followed by one more gate. Gentry's usual choice is $\Gamma = \{\mathsf{NAND}, \mathsf{id}\}$, and any other universal gate set works `[T §1.3, fn 1]`.

> [!remark]
> The definition is only the inclusion $\mathcal D_E(\Gamma) \subseteq \mathcal C_E$. It says nothing about how keys are chained; that belongs to the construction in [[Gentry Bootstrapping Transformation]].

## Syntax

> [!definition] Parameters
> - $(\mathrm{pk}_1, \mathrm{sk}_1)$: the key pair under which the input ciphertext is encrypted; $\mathrm{sk}_1$ is written as $(\mathrm{sk}_{1,1}, \dots, \mathrm{sk}_{1,\ell}) \in \mathcal M^\ell$.
> - $\mathrm{pk}_2$: the new public key. $\mathrm{bk} = (\mathrm{bk}_1, \dots, \mathrm{bk}_\ell)$: the bootstrapping key.
> - $c = (c_1, \dots, c_\ell) \in \mathcal M^\ell$: a ciphertext under $\mathrm{pk}_1$, written in bits.

> [!definition] Refresh Specification `[S §1.2]` `[T §1.3]` `[C §4.3]`
> - $\mathrm{bk} \leftarrow \mathsf{BKGen}(\mathrm{pk}_2, \mathrm{sk}_1)$: (Randomized) Bootstrapping-key generation, run once by the owner of $\mathrm{sk}_1$.
>     - **Input**: a public key $\mathrm{pk}_2$ and a secret key $\mathrm{sk}_1 \in \mathcal M^\ell$.
>     - **Output**: $\mathrm{bk} = (\mathrm{bk}_1, \dots, \mathrm{bk}_\ell)$, where $\mathrm{bk}_j$ is an encryption of $\mathrm{sk}_{1,j}$ under $\mathrm{pk}_2$.
> - $c' \leftarrow \mathsf{Refresh}(\mathrm{pk}_2, \mathrm{bk}, c)$: (Randomized) Bootstrapping algorithm.
>     - **Input**: a public key $\mathrm{pk}_2$; a bootstrapping key $\mathrm{bk}$ produced by $\mathsf{BKGen}(\mathrm{pk}_2, \mathrm{sk}_1)$; a ciphertext $c$ under $\mathrm{pk}_1$, the public key of $\mathrm{sk}_1$.
>     - **Output**: a ciphertext $c'$ under $\mathrm{pk}_2$ with $\mathsf{Dec}(\mathrm{sk}_2, c') = \mathsf{Dec}(\mathrm{sk}_1, c)$, except with negligible probability.

> [!remark] Provenance of the names
> `⚠️ CLAUDE – verify:` the sources speak of "the encrypted bits of the secret key" and "the bootstrapping key" but, as far as I read, name no algorithm that produces them. $\mathsf{BKGen}$ is mine; it exists so that the promise on $\mathrm{bk}$ in the Input of $\mathsf{Refresh}$ has something to refer to. In your previous note this was the "Setup" step.

> [!remark] Notation in the literature
> This note calls the operation $\mathsf{Refresh}$ and keeps $\mathrm{bk}$ as an argument. Key generation is $\mathsf{KeyGen}$, as $\mathsf{KeyGen}_E$ in `[T §2.1]`.
>
> | source | algorithms | differences |
> | --- | --- | --- |
> | `[T §1.3]` | $\mathsf{Recrypt}_E(\mathrm{pk}_2, D_E, \langle\langle \mathrm{sk}_{1j} \rangle\rangle, \psi_1)$, output $\psi_2$ | the decryption circuit $D_E$ is an explicit argument; the encrypted key bits are the third argument. |
> | `[S §1.2]` | $\mathsf{Recrypt}_E$, same shape | the paper also calls it bootstrapping; fn. 2 notes it gives one-way proxy re-encryption. |
> | `[DS16]` | $\mathsf{Refresh}(\mathrm{pk}, c)$ | single-key case $\mathrm{pk}_2 = \mathrm{pk}_1$, $\mathrm{bk}$ left implicit; `⚠️ verify:` taken from your previous note, the PDF was not opened. See the remark under Property. |

## Construction

> [!definition] Building Blocks
> - $E = (\mathsf{KeyGen}, \mathsf{Enc}, \mathsf{Dec}, \mathsf{Eval})$: a [[Homomorphic Encryption]] scheme with $f_\mathsf{Dec} \in \mathcal C_E$ (a bootstrappable scheme). $\mathsf{Enc}$ and $\mathsf{Eval}$ are called below.

> [!definition] Refresh from Eval `[S §1.2]` `[T §1.3]` `[C §4.3]`
> - $\mathrm{bk} \leftarrow \mathsf{BKGen}(\mathrm{pk}_2, \mathrm{sk}_1)$: (Randomized) Bootstrapping-key generation.
>     - **Input**: $\mathrm{pk}_2$ and $\mathrm{sk}_1 \in \mathcal M^\ell$.
>     - **Output**: $\mathrm{bk} \in \mathcal C^\ell$.
>     - **Steps**:
>         1. $\mathrm{bk}_j \leftarrow \mathsf{Enc}(\mathrm{pk}_2, \mathrm{sk}_{1,j})$ for $j \in [1, \ell]$.
>         2. Return $\mathrm{bk} = (\mathrm{bk}_1, \dots, \mathrm{bk}_\ell)$.
> - $c' \leftarrow \mathsf{Refresh}(\mathrm{pk}_2, \mathrm{bk}, c)$: (Randomized) Bootstrapping algorithm.
>     - **Input**: $\mathrm{pk}_2$; $\mathrm{bk} \in \mathcal C^\ell$; the bits $c_1, \dots, c_\ell \in \mathcal M$ of a ciphertext $c$ under $\mathrm{pk}_1$.
>     - **Output**: $c' \in \mathcal C$, a ciphertext under $\mathrm{pk}_2$.
>     - **Steps**:
>         1. $c_j' \leftarrow \mathsf{Enc}(\mathrm{pk}_2, c_j)$ for $j \in [1, \ell]$. **(randomized)** `[S §1.2]` marks this step as sampling fresh coins.
>         2. Return $\mathsf{Eval}(\mathrm{pk}_2, f_\mathsf{Dec}, (\mathrm{bk}_1, \dots, \mathrm{bk}_\ell, c_1', \dots, c_\ell'))$.

> [!remark]
> $\mathsf{Refresh}$ is randomized because of step 1 (and because $\mathsf{Eval}$ may be). If $\mathsf{Eval}$ is restricted to be deterministic, all the randomness is in step 1.

## Property

### Correctness

> [!property] Refresh from Eval is correct `[S §1.2]` `[C §4.3]`
> If $f_\mathsf{Dec} \in \mathcal C_E$, then $\mathsf{Refresh}$ from $\mathsf{Eval}$ meets the Refresh Specification: its output is a ciphertext under $\mathrm{pk}_2$ of $\mathsf{Dec}(\mathrm{sk}_1, c)$.

### Remarks

> [!remark] Why it works `[T §1.3]` `[S §1.2]` `[C §4.3]`
> At one point the message is doubly encrypted (under $\mathrm{pk}_1$ inside $\mathrm{pk}_2$), and $\mathsf{Eval}$ strips the inner layer. Evaluating the decryption circuit removes the noise of $c$, but $\mathsf{Eval}$ adds fresh noise under $\mathrm{pk}_2$. Progress is made when the new noise is smaller than the removed noise.

> [!remark] Is it safe to publish $\mathrm{bk}$? `[T §1.3]` `[C §4.3]`
> If $\mathrm{pk}_1 \ne \mathrm{pk}_2$, the encrypted key bits are indistinguishable from encryptions of $0$ whenever $E$ is semantically secure (hybrid argument). The hybrid argument breaks if $\mathrm{pk}_1 = \mathrm{pk}_2$; then one needs key-dependent-message security, here circular security: see [[Key-Dependent Message Security|KDM Security]].

> [!remark] A deterministic variant `[S §6]`
> `[S §6]` lists as an optimization that the homomorphic decryption circuit can take the bits of $c$ directly as inputs instead of encryptions of them (credited there to a personal communication of Canetti).
> `⚠️ CLAUDE – verify:` if so, one can hardwire $c$ into the circuit, i.e. $\mathsf{Eval}(\mathrm{pk}_2, f_\mathsf{Dec}(\cdot, c), \mathrm{bk})$, and $\mathsf{Refresh}$ has no coins of its own. "Hardwiring $c$" is my formalization, not the source's wording. Check `[S §6]` before using it.

> [!remark] Relation to the formula in `[DS16]`
> `[DS16]` writes $\mathsf{Refresh}(\mathrm{pk}, c) = \mathsf{Eval}(\mathrm{pk}, \mathsf{CDec}, (\mathrm{bk}_1, \dots, \mathrm{bk}_k, c_1', \dots, c_\ell'))$ with $\mathrm{bk}_i = \mathsf{Enc}(\mathrm{pk}, \mathrm{sk}_i)$. This is the special case $\mathrm{pk}_2 = \mathrm{pk}_1$ of the algorithm above, with $\mathrm{bk}$ left implicit. The PDF of `[DS16]` was not opened (access blocked), so their surrounding text is unchecked. The ePrint page carries a 2025 revision note saying that the paper's *sanitization* definition is incorrect (pointing to ePrint 2025/275); from the page, that concerns sanitization, not the FHE syntax or $\mathsf{Refresh}$.

> [!remark] Re-keying
> With $\mathrm{pk}_2 \ne \mathrm{pk}_1$, $\mathsf{Refresh}$ refreshes the noise and switches keys at once. Gentry observes that this yields a one-way, multi-use proxy re-encryption scheme `[S fn 2]` `[T §1.8]`.

## Related

### Constructions
- [[Gentry Bootstrapping Transformation]] — what a bootstrappable scheme buys

### Properties
- [[Key-Dependent Message Security|KDM Security]] — what publishing $\mathrm{bk}$ under its own key costs

### Siblings
- [[Leveled Fully Homomorphic Encryption]], [[Fully Homomorphic Encryption]] — what the transformation outputs

### Prerequisites
- [[Homomorphic Encryption]]
