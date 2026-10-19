Reference:
- `[T x]` — Gentry, _A Fully Homomorphic Encryption Scheme_, PhD thesis, Stanford, 2009: https://crypto.stanford.edu/craig/craig-thesis.pdf
- `[S x]` — Gentry, _Fully Homomorphic Encryption Using Ideal Lattices_, STOC 2009: https://www.cs.cmu.edu/~odonnell/hits09/gentry-homomorphic-encryption.pdf
- `[C x]` — Gentry, _Computing Arbitrary Functions of Encrypted Data_ (CACM expository article): https://dl.acm.org/doi/pdf/10.1145/1666420.1666444
- `[BV]` — Brakerski, Vaikuntanathan, _Efficient Fully Homomorphic Encryption from (Standard) LWE_, FOCS 2011 (ePrint 2011/344): https://eprint.iacr.org/2011/344.pdf
- `[BGV]` — Brakerski, Gentry, Vaikuntanathan, _Fully Homomorphic Encryption without Bootstrapping_ (ePrint 2011/277): https://eprint.iacr.org/2011/277
- `[DS16]` — Ducas, Stehlé, _Sanitization of FHE Ciphertexts_, EUROCRYPT 2016 (ePrint 2016/164): https://eprint.iacr.org/2016/164.pdf
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

> [!todo] Draft of the Homomorphic Encryption note after the split — delete this block when you swap it in
> - **What moved out:** Bootstrapping, `Refresh`, the augmented decryption circuit, "bootstrappable" → [[Bootstrappable Encryption]]; the theorem and the construction $E^{(d)}$ → [[Gentry Bootstrapping Transformation]]; circular security → [[Key-Dependent Message Security|KDM Security]]; FHE and leveled FHE → [[Fully Homomorphic Encryption]], [[Leveled Fully Homomorphic Encryption]].
> - **Parameters:** $\lambda, \mathrm{aux}, \mathcal M, \mathcal C, \mathcal R, \mathcal K$ are imported from [[Public-Key Encryption Scheme]]. $\mathcal{SK}, \mathcal{PK}$ are dropped: nothing in the note used them. $\Gamma, \ell$ moved to where they are first used.
> - **Reference list:** the `[BV]` entry now points to ePrint 2011/344 (Brakerski–Vaikuntanathan, FOCS 2011), as in your current note; the draft adds the title and a separate `[BGV]` entry for ePrint 2011/277. The two statements credited to `[BV]` were checked against the 2011/344 text: see [[Leveled Fully Homomorphic Encryption]] and [[Fully Homomorphic Encryption]].

## Syntax

> [!definition] Parameters
> - [[Public-Key Encryption Scheme]]: Import $(\lambda, \mathrm{aux}, \mathcal M, \mathcal C, \mathcal R, \mathcal K)$.
> - $\mathcal C_E$: the set of **permitted circuits**, the circuits $\mathsf{Eval}$ is required to handle correctly `[T 2.1.1]` `[S §1.1]`.

> [!definition] Homomorphic Encryption Scheme
> Extends:: [[Public-Key Encryption Scheme]]
>
> ---
> A **homomorphic encryption scheme** $E = (\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec}, \mathsf{Eval})$ is a [[Public-Key Encryption Scheme]] $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ together with one more algorithm and the parameter $\mathcal C_E$. The first three algorithms are those of the base note. All algorithms run in time $\mathrm{poly}(\lambda)$, and $\mathsf{Eval}$ in time $\mathrm{poly}(\lambda, |C|)$ `[S §1.1]`.
> - $c \leftarrow \mathsf{Eval}(\mathrm{pk}, C, (c_1, \dots, c_t))$: (Possibly randomized) Evaluation algorithm `[T §2.1]`.
>     - **Input**: a public key $\mathrm{pk}$; a circuit $C \in \mathcal C_E$ with $t$ inputs over $\mathcal M$; ciphertexts $c_1, \dots, c_t \in \mathcal C$ of its input wires.
>     - **Output**: a ciphertext $c \in \mathcal C$ meant to encrypt $C(m_1, \dots, m_t)$ (see Correctness).

> [!remark] Notation in the literature
> The base algorithms are as in [[Public-Key Encryption Scheme#Syntax|PKE]]. For $\mathsf{Eval}$ and the key material the sources differ as follows.
>
> | source | algorithms | differences |
> | --- | --- | --- |
> | `[T §2.1]` | $\mathsf{Evaluate}_E(\mathrm{pk}, C, \Psi)$ with $\Psi = \langle \psi_1, \dots, \psi_t \rangle$ | possibly randomized; $C$ ranges over the permitted set $\mathcal C_E$; the decryption circuit is $D_E$ (here $f_\mathsf{Dec}$). |
> | `[S §1.1, §2]` | $\mathsf{Evaluate}_E(\mathrm{pk}, C, \Psi)$; leveled: $\mathsf{KeyGen}_E(\lambda, d)$ and $\mathsf{Evaluate}_E^{(\delta)}$ | the depth $d$ is an input of key generation; $\delta$ indexes the level of a circuit and of the key it is evaluated under. |
> | `[BV §3.1]` | $\mathsf{HE.Keygen}(1^\kappa) \to (\mathrm{pk}, \mathrm{evk}, \mathrm{sk})$ and $\mathsf{HE.Eval}_\mathrm{evk}(f, c_1, \dots, c_\ell)$ | a separate **evaluation key** $\mathrm{evk}$; $f$ is a function on bits, represented as a GF(2) arithmetic circuit; messages are bits. Leveled: $\mathsf{Keygen}(1^\kappa, 1^L)$ `[BV Def 3.6]`. |
>
> The generic form above folds $\mathrm{evk}$ into $\mathrm{pk}$; with the `[BV]` split, $\mathsf{Eval}$ takes $\mathrm{evk}$ instead of $\mathrm{pk}$.

> [!remark] Deterministic or randomized $\mathsf{Eval}$
> The thesis allows $\mathsf{Eval}$ to be randomized `[T §2.1]`. Restricting to schemes whose $\mathsf{Eval}$ uses no coins is a legitimate convention, but it is a choice, not what the source requires.

## Property

### Correctness

> [!definition] Parameters
> - $C \in \mathcal C_E$: a permitted circuit with $t$ inputs over $\mathcal M$.

> [!definition] Correctness for $\mathcal C_E$ `[T 2.1.1]` `[S §1.1]`
> $E$ is **correct for $\mathcal C_E$** if for **every** key pair $(\mathrm{pk}, \mathrm{sk})$ output by $\mathsf{Gen}(1^\lambda)$, **every** circuit $C \in \mathcal C_E$ with $t$ inputs, **every** $(m_1, \dots, m_t) \in \mathcal M^t$ and every $c_i \leftarrow \mathsf{Enc}(\mathrm{pk}, m_i)$:
> $$\mathsf{Dec}(\mathrm{sk}, \mathsf{Eval}(\mathrm{pk}, C, (c_1, \dots, c_t))) = C(m_1, \dots, m_t)$$
> except with negligible probability over the coins of $\mathsf{Eval}$ `[T 2.1.1]`.

> [!remark]
> This is stronger than $(1-\delta)$-correctness of the base note in one respect: it quantifies over all messages and all circuits of $\mathcal C_E$, not an average. `⚠️ CLAUDE – verify:` this matters for bootstrapping, where the inputs of $f_\mathsf{Dec}$ are the specific bits of $\mathrm{sk}$ and $c$, not uniformly random messages, so an average-case statement would not justify $\mathsf{Refresh}$ (my reasoning, not a quotation).

### Compactness

> [!definition] Parameters
> - $p$: a polynomial.
> - $f_\mathsf{Dec}$: the decryption algorithm written as a circuit (called $D_E$ in the sources `[T §1.2]`); it takes the bits of $\mathrm{sk}$ and of a ciphertext $c$ and outputs $\mathsf{Dec}(\mathrm{sk}, c)$.

> [!definition] Compactness `[T 2.1.2]` `[S Def 1]`
> $E$ is **compact** if there is a polynomial $p$ such that for every $\lambda$ the decryption algorithm can be written as the circuit $f_\mathsf{Dec}$ of size at most $p(\lambda)$.
> - Consequence: the ciphertext size is bounded by a function of $\lambda$ alone, independent of the circuit $C$ that was evaluated `[T §1.2]`.
> - $E$ **compactly evaluates** $\mathcal C_E$ if it is compact and correct for $\mathcal C_E$ `[T 2.1.3]`. `[S]` calls this "homomorphic for $\mathcal C_E$" `[S Def 1]`.
> - Why it is required: without it, $\mathsf{Eval}$ could output $(C, c_1, \dots, c_t)$ unprocessed and $\mathsf{Dec}$ could do all the work `[T 2.1.1]` `[S fn 1]` `[C §2.2]`.
> - A relaxation, **quasi-compact**, lets the size depend on the depth of $C$ but not on its size `[T §2.1]` `[S §1.1]`.

## Variant

| variant | $\mathcal C_E$ | note |
| --- | --- | --- |
| somewhat homomorphic | a restricted class, typically bounded depth | remark below |
| leveled | depth at most $d$ over a gate set $\Gamma$, a family indexed by $d$ | [[Leveled Fully Homomorphic Encryption]] |
| fully homomorphic | all circuits | [[Fully Homomorphic Encryption]] |

> [!remark] Somewhat homomorphic
> A scheme that is correct only for a restricted $\mathcal C_E$ (typically bounded depth, because ciphertext noise grows with each operation and decryption fails once it is too large) is called **somewhat homomorphic** `[T §1.1, §1.3]` `[C §3]`. [[Bootstrappable Encryption|Bootstrapping]] turns such a scheme into a leveled or fully homomorphic one.

## Security

> [!remark] What "secure" means for a homomorphic scheme
> `⚠️ CLAUDE – verify:` I take the notion to be that of the base note, [[Indistinguishability under Chosen-Plaintext Attack|IND-CPA]] of $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$, with no separate game for $\mathsf{Eval}$: $\mathsf{Eval}$ takes only public inputs ($\mathrm{pk}$, $C$, ciphertexts), so an adversary can run it itself. This is my reasoning; I did not locate the sentence in `[T §2.1]` or `[S §1.1]` in this pass.
> By the same token IND-CCA2 is out of reach for a scheme whose $\mathsf{Eval}$ turns a challenge ciphertext into a different valid ciphertext of a related plaintext: the adversary submits that ciphertext to the decryption oracle. This is folklore, not taken from the sources above; confirm it before relying on it.
> Security that depends on how keys are used inside bootstrapping is separate: see [[Key-Dependent Message Security|KDM Security]].

## Related

### Descendants
| | permitted circuits $\mathcal C_E$ | adds |
| --- | --- | --- |
| [[Fully Homomorphic Encryption]] | all circuits | the cost bound: evaluation cost polynomial in $\lambda$ and the circuit size |
| [[Leveled Fully Homomorphic Encryption]] | all circuits of depth at most $d$, one scheme $E^{(d)}$ per $d$ | the depth parameter $d$; a family of schemes, so it points back with a `Requires` field, not `Extends` |
| [[Bootstrappable Encryption]] | $\mathcal C_E$ contains the augmented decryption circuit | $\mathsf{Refresh}$ |

### Instantiations
- [[Additively-Homomorphic Encryption]] — $\mathcal C_E$ restricted to additions

### Constructions
- [[Gentry Bootstrapping Transformation]] — a bootstrappable scheme in, a leveled scheme out

### Properties
- [[Key-Dependent Message Security|KDM Security]] — what publishing an encrypted secret key costs; the self-loop of the transformation needs it
- [[Indistinguishability]] — the security notion, from [[Public-Key Encryption Scheme]]

### Siblings
- [[Secure Multi-party Computation]] — computing on private inputs without a single key holder
