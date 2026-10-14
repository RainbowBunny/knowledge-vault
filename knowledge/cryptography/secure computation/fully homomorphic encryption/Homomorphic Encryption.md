
Reference:
- `[T x]` — Gentry, _A Fully Homomorphic Encryption Scheme_, PhD thesis, Stanford, 2009: https://crypto.stanford.edu/craig/craig-thesis.pdf
- `[S x]` — Gentry, _Fully Homomorphic Encryption Using Ideal Lattices_, STOC 2009: https://www.cs.cmu.edu/~odonnell/hits09/gentry-homomorphic-encryption.pdf
- `[C x]` — Gentry, _Computing Arbitrary Functions of Encrypted Data_ (CACM expository article): https://dl.acm.org/doi/pdf/10.1145/1666420.1666444
- `[DS16]` — Ducas, Stehlé, _Sanitization of FHE Ciphertexts_, EUROCRYPT 2016 (ePrint 2016/164): https://eprint.iacr.org/2016/164.pdf
- `[BV]` — Brakerski, Vaikuntanathan, FOCS 2011: https://eprint.iacr.org/2011/344.pdf

## Syntax

> [!definition] Parameters
> 
> - $\lambda$: security parameter.
> - $\mathcal{SK}, \mathcal{PK}, \mathcal{M}, \mathcal{C}$: secret key, public key, message, ciphertext spaces. In the sources $\mathrm{pk}$ determines the plaintext and ciphertext spaces `[T §2.1]`; listing them as parameters is just notation.
> - $\mathcal{C}_E$: the set of **permitted circuits**, i.e. the circuits $\mathsf{Eval}$ is required to handle correctly `[T 2.1.1]` `[S §1.1]`. 
> - $\Gamma$: a set of gates (e.g. ${\mathsf{NAND}, \mathsf{id}}$), used for bootstrapping below `[S Def 4]`.
> - $\ell$: the number of message-space elements (bits) used to write a secret key or a ciphertext as input to the decryption circuit `[S Def 4]`.

> [!definition] Homomorphic encryption scheme $E$ (HE)
> Extends:: [[Public-Key Encryption Scheme (Old)]]
> 
> ---
> $E$ consists of four algorithms. All run in time $\mathrm{poly}(\lambda)$, and $\mathsf{Eval}$ in time $\mathrm{poly}(\lambda, |C|)$ `[S §1.1]`.
> 
> - $(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{KeyGen}(1^\lambda)$: **(Randomized)** `[T §2.1]`.
> - $c \leftarrow \mathsf{Enc}(\mathrm{pk}, m)$: **(Randomized)** `[T §2.1]`. It must be randomized for semantic security `[C §2.3]`.
> - $m \leftarrow \mathsf{Dec}(\mathrm{sk}, c)$: **(Deterministic)**.
> - $c \leftarrow \mathsf{Eval}(\mathrm{pk}, C, (c_1, \dots, c_t))$ with $C \in \mathcal{C}_E$: (**Possibly randomized**) `[T §2.1]`. 

## Properties

### Correctness

> [!definition] Correctness for $\mathcal{C}_E$ `[T 2.1.1]` `[S §1.1]` 
> $E$ is **correct for $\mathcal{C}_E$** if for **every** key pair $(\mathrm{pk}, \mathrm{sk})$ output by $\mathsf{KeyGen}(1^\lambda)$, **every** circuit $C \in \mathcal{C}_E$ with $t$ inputs, **every** $(m_1, \dots, m_t) \in \mathcal{M}^t$ and every $c_i \leftarrow \mathsf{Enc}(\mathrm{pk}, m_i)$: $$\mathsf{Dec}(\mathrm{sk}, \mathsf{Eval}(\mathrm{pk}, C, (c_1, \dots, c_t))) = C(m_1, \dots, m_t)$$ except with negligible probability over the coins of $\mathsf{Eval}$ `[T 2.1.1]`.

### Compactness

> [!definition] Compactness `[T 2.1.2]` `[S Def 1]` 
> $E$ is **compact** if there is a polynomial $p$ such that for every $\lambda$ the algorithm $\mathsf{Dec}$ can be written as a circuit $f_\mathsf{Dec}$ (called $D_E$ in the sources) of size at most $p(\lambda)$.
> 
> - Consequence: the ciphertext size is bounded by a function of $\lambda$ alone, independent of the circuit $C$ that was evaluated `[T §1.2]`.
> - $E$ **compactly evaluates** $\mathcal{C}_E$ if it is compact and correct for $\mathcal{C}_E$ `[T 2.1.3]`. $S$ calls this "homomorphic for $\mathcal{C}_E$" `[S Def 1]`.
> - Why it is required: without it, $\mathsf{Eval}$ could output $(C, c_1, \dots, c_t)$ unprocessed and $\mathsf{Dec}$ could do all the work `[T 2.1.1]` `[S fn 1]` `[C §2.2]`.
> - A relaxation, "quasi-compact", lets size depend on the depth of $C$ but not on its size `[T §2.1]` `[S §1.1]`.

### Fully homomorphic and leveled

> [!definition] FHE `[T 2.1.4]` `[S Def 2]` 
> $E$ is **fully homomorphic** if it compactly evaluates _all_ circuits. In addition, $\mathsf{Eval}$ should cost at most $|C| \cdot \mathrm{poly}(\lambda)$ `[C §2.2]`.

> [!definition] Leveled FHE `[T 2.1.5]` `[S Def 3]` 
> A family ${E^{(d)} : d \in \mathbb{Z}^+}$ is **leveled fully homomorphic** if all members share the same decryption circuit, $E^{(d)}$ compactly evaluates all circuits of depth at most $d$ over a fixed gate set $\Gamma$, and the cost of its algorithms is polynomial in $\lambda$, $d$ and (for $\mathsf{Eval}$) $|C|$. The public key of $E^{(d)}$ grows linearly in $d$ `[T Thm 1.3.1 informal]` `[BV]`.

> [!remark] Somewhat homomorphic 
> A scheme correct only for a restricted $\mathcal{C}_E$ (typically bounded depth, because ciphertext noise grows with each operation and decryption fails once it is too large) is called _somewhat homomorphic_ `[T §1.1, §1.3]` `[C §3]`. Bootstrapping turns such a scheme into a leveled or fully homomorphic one.

## Bootstrapping

### The Refresh (Recrypt) algorithm

> [!definition] Bootstrapping key and Refresh `[S §1.2]` `[T §1.3]` `[C §4.3]` 
> Let $\mathrm{sk}_1$ be written as elements $\mathrm{sk}_{1,1}, \dots, \mathrm{sk}_{1,\ell}$ of $\mathcal{M}$ (bits, with $\mathcal{M} = {0,1}$ in the sources `[S §1.2]`).
> 
> **Setup** (once, by the owner of $\mathrm{sk}_1$): $\mathrm{bk}_j \leftarrow \mathsf{Enc}(\mathrm{pk}_2, \mathrm{sk}_{1,j})$ for $j \in [1, \ell]$.
> 
> $c' \leftarrow \mathsf{Refresh}(\mathrm{pk}_2, \mathrm{bk}, c)$: **(Randomized)**
> 
> - **Input**: new public key $\mathrm{pk}_2$, bootstrapping key $\mathrm{bk} = (\mathrm{bk}_1, \dots, \mathrm{bk}_\ell)$, ciphertext $c$ under $\mathrm{pk}_1$, with bits $c_1, \dots, c_\ell$.
> - **Steps**:
>     1. $c_j' \leftarrow \mathsf{Enc}(\mathrm{pk}_2, c_j)$ for $j \in [1, \ell]$. **(randomized)** `[S §1.2]` marks this step as sampling fresh coins.
>     2. Output $\mathsf{Eval}(\mathrm{pk}_2, f_\mathsf{Dec}, (\mathrm{bk}_1, \dots, \mathrm{bk}_\ell, c_1', \dots, c_\ell'))$.
> - **Output**: a ciphertext under $\mathrm{pk}_2$ of $\mathsf{Dec}(\mathrm{sk}_1, c)$ `[S §1.2]`, provided $f_\mathsf{Dec} \in \mathcal{C}_E$ `[S §1.2]` `[C §4.3]`.
> 
> So Refresh is randomized because of step 1 (and because $\mathsf{Eval}$ may be). If you restrict to deterministic $\mathsf{Eval}$ as in your convention, all the randomness is in step 1.

> [!note] Relation to the formula in [DS16] 
> `[DS16]` (as quoted in your message) writes $\mathsf{Refresh}(\mathrm{pk}, c) = \mathsf{Eval}(\mathrm{pk}, \mathsf{CDec}, (\mathrm{bk}_1, \dots, \mathrm{bk}_k, c_1', \dots, c_\ell'))$ with $\mathrm{bk}_i = \mathsf{Enc}(\mathrm{pk}, \mathrm{sk}_i)$. This is the special case $\mathrm{pk}_2 = \mathrm{pk}_1$ of the algorithm above, with $\mathrm{bk}$ left implicit. I could not open the PDF of `[DS16]` (the site blocks automated access), so I did not check their surrounding text. The ePrint page carries a 2025 revision note saying that the paper's _sanitization_ definition is incorrect (pointing to ePrint 2025/275); from the page, that concerns sanitization, not the FHE syntax or $\mathsf{Refresh}$.

> [!note] Why it works `[T §1.3]` `[S §1.2]` `[C §4.3]` 
> At one point the message is doubly encrypted (under $\mathrm{pk}_1$ inside $\mathrm{pk}_2$). $\mathsf{Eval}$ strips the inner layer. Evaluating the decryption circuit removes the noise of $c$, but $\mathsf{Eval}$ adds fresh noise under $\mathrm{pk}_2$. Progress is made when the new noise is smaller than the removed noise.

> [!note] Is it safe to publish $\mathrm{bk}$? `[T §1.3]` `[C §4.3]` 
> If $\mathrm{pk}_1 \ne \mathrm{pk}_2$, the encrypted key bits are indistinguishable from encryptions of $0$ whenever $E$ is semantically secure (hybrid argument). The hybrid argument breaks if $\mathrm{pk}_1 = \mathrm{pk}_2$; then one needs key-dependent-message (KDM) security, here called circular security, see below.

> [!note] A deterministic variant `[S §6]` 
> `[S §6]` lists as an optimization that the homomorphic decryption circuit can take the bits of $c$ directly as inputs instead of encryptions of them (credited there to a personal communication of Canetti). `⚠️ CLAUDE – verify:` if so, one can hardwire $c$ into the circuit, i.e. $\mathsf{Eval}(\mathrm{pk}_2, f_\mathsf{Dec}(\cdot, c), \mathrm{bk})$, and Refresh has no coins of its own. Writing it as "hardwiring $c$" is my formalization, not the source's wording. Check `[S §6]` before using it.

### Augmented decryption circuit and bootstrappable

> [!definition] Augmented decryption circuit `[S Def 4]` 
> Let $\Gamma$ be a set of gates with inputs and outputs in $\mathcal{M}$, **including the identity gate**. For $g \in \Gamma$ with $t$ inputs, the **$g$-augmented decryption circuit** is $g$ applied to $t$ copies of $f_\mathsf{Dec}$, where $f_\mathsf{Dec}$ takes the secret key and a ciphertext, both written as elements of $\mathcal{M}^{\ell}$. Write $\mathcal{D}_E(\Gamma)$ for the set of these circuits.

> [!definition] Bootstrappable `[S Def 5]` 
> Let $\mathcal{C}_E$ be a set of circuits for which $E$ is homomorphic. $E$ is **bootstrappable with respect to $\Gamma$** if $\mathcal{D}_E(\Gamma) \subseteq \mathcal{C}_E$. Informal version: $E$ can evaluate its own decryption circuit and that circuit plus one more gate. Gentry's usual choice is $\Gamma = {\mathsf{NAND}, \mathsf{id}}$, and any other universal gate set works `[T §1.3, fn 1]`.

> [!warning] Correction to my previous message 
> My earlier "bootstrappable" definition tied $\mathrm{bk}$ and $c'$ to the same $\mathrm{pk}$ (circular form) and omitted the identity gate. Per `[S Def 5]` the definition is only the inclusion $\mathcal{D}_E(\Gamma) \subseteq \mathcal{C}_E$; it says nothing about how keys are chained. Key chaining belongs to the construction below.

## Theorem: bootstrappable ⟹ leveled FHE

> [!theorem] Gentry `[S Thm 3, 4, 5]` `[T Thm 1.3.1 (informal), Ch. 4]` 
> Let $E$ be bootstrappable with respect to $\Gamma$. Then there is a family ${E^{(d)}}$, built from $E$, that is leveled fully homomorphic for circuits with gates in $\Gamma$ `[S Thm 3]`.
> 
> - With $\Gamma$ universal (e.g. NAND), this handles any circuit of depth $d$ `[T Thm 1.3.1]`. $\Gamma$ itself may be arbitrary, e.g. gates that are depth-$m$ circuits, giving depth $d \cdot m$ `[S §2]`.
> - Public key of $E^{(d)}$: $O(d)$ times that of $E$. Decryption circuit and encryption cost are unchanged. Evaluation is polynomial in $\lambda$ and linear in $|C|$ `[T Thm 1.3.1]`.
> - Security `[S Thm 4]`: an adversary against $E^{(d)}$ with advantage $\varepsilon$ yields one against $E$ with advantage at least $\varepsilon / (\ell (d+1))$, with time $\mathrm{poly}(\ell, d)$ times that of the original adversary. Semantic security of $E$ is enough; no extra assumption.
> - Cost `[S Thm 5]`: for a circuit with $s$ wires and depth $d$, $\mathsf{Eval}^{(d)}$ makes at most $s \ell d$ calls to $\mathsf{Enc}$ and at most $s d$ calls to $\mathsf{Eval}$ on circuits in $\mathcal{D}_E(\Gamma)$.

> [!definition] The construction $E^{(d)}$ `[S §2]` `[C §4.3]`
> 
> - **Keys**: $d+1$ independent key pairs $(\mathrm{pk}_i, \mathrm{sk}_i)$, and, for every $i$ except the last, the bits of $\mathrm{sk}_i$ encrypted under the _next_ public key. The public key of $E^{(d)}$ is the list of $\mathrm{pk}_i$ together with this chain of encrypted secret keys `[C §4.3]`.
> - **Evaluation**: go through the circuit level by level. At each level, take ciphertexts under $\mathrm{pk}_i$, re-encrypt their bits under $\mathrm{pk}_{i+1}$, and evaluate the gate together with $f_\mathsf{Dec}$ using the encrypted $\mathrm{sk}_i$. That is one $\mathsf{Refresh}$ plus one gate per level, in a single $\mathsf{Eval}$ call.
> - **Index convention**: `[C §4.3]` chains keys upward ($\mathrm{sk}_i$ under $\mathrm{pk}_{i+1}$). `[S §2]` indexes the other way (ciphertexts under $\mathrm{pk}_d$ at the input level, decryption with $\mathrm{sk}_0$, and $\mathrm{sk}_i$ under $\mathrm{pk}_{i-1}$). Same construction, different labels.

> [!note] Why leveled and not fully homomorphic `[T §1.3]` `[C §4.4]` 
> $E^{(d)}$ needs $d+1$ public keys, so key generation and the public key grow with $d$; strictly it is only _leveled_. The depth must be fixed in advance.

## Circular security: from leveled to unbounded FHE

> [!definition] Circular / KDM security `[C §4.4]` `[T §1.3]` `[S §1.2]` 
> $E$ is **circular secure** if it is safe to publish an encryption of $\mathrm{sk}$ under its own $\mathrm{pk}$ (more generally KDM-secure: encryptions of functions of the secret key do not hurt security).

> [!theorem] Unbounded FHE under KDM security `[S §2]` `[T §1.3]` 
> If $E$ is bootstrappable and KDM-secure, the key chain can be replaced by a single $\mathrm{pk}$ and an encryption of $\mathrm{sk}$ under it (a "self-loop"). The resulting scheme is fully homomorphic, its public key does not depend on the circuit depth, and its security follows from the KDM security of $E$ `[S §2]`.
> 
> - In this case $\mathsf{Refresh}$ is run with $\mathrm{pk}_2 = \mathrm{pk}_1$. That is the "typical" $\mathsf{Refresh}$ of `[DS16]`.
> - Historically Gentry first used the self-loop and tried to prove KDM security; Canetti suggested the acyclic leveled chain to avoid needing it `[S fn 3]`.
> - In the random oracle model, bootstrappable encryption is shown to imply a scheme that is both bootstrappable and KDM-secure `[T §1.3]`; thesis Chapter 4 has a section on it (I only saw the table of contents).
> - Later works still obtain depth-independent FHE only by adding a circular security assumption `[BV]`.

> [!note] Re-keying 
> With $\mathrm{pk}_2 \ne \mathrm{pk}_1$, $\mathsf{Refresh}$ refreshes noise and switches keys at once. Gentry observes that this yields a one-way, multi-use proxy re-encryption scheme `[S fn 2]` `[T §1.8]`.

