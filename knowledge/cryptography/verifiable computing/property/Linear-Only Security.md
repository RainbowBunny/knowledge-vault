---
aliases: [Strictly Linear-Only, Linear-Only]
---
Reference:
- `[ISW21 x]` — Ishai, Su, Wu, _Shorter and Faster Post-Quantum Designated-Verifier zkSNARKs from Lattices_, CCS 2021 (ePrint 2021/977): https://eprint.iacr.org/2021/977.pdf. Definition 3.4 and Remark 3.5 were read through a summarizer, not verbatim.
- `[LUNA]` — see [[LUNA]], ePrint 2022/1690. Its Conjecture 1 states that HGSW is "strictly linear-only". `⚠️ CLAUDE – verify:` I did not find a definition in the text I read, so I cannot say whether it uses `[ISW21 Def 3.4]` as written here.
- `#supplemented` marks what I added to your text; its source is on this line. Delete the tag once you have read it.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - [[Vector Encryption]]: Import $(\lambda, \ell, \mathbb F, \mathrm{pp}, \mathrm{sk})$.
> - $m$: the number of ciphertexts given to $\mathcal A$. $k$: the number it outputs.
> - $\mathcal M$: an efficient plaintext generator. $z$: auxiliary input.
> - $\mathcal E$: the extractor. $\boldsymbol\Pi \in \mathbb F^{k \times m}$: the matrix it outputs.

> [!definition] Linear-Only Security
> ### Scope
> A [[Vector Encryption]] $\Pi_\mathsf{Enc}$, a polynomial-size [[Adversary]] $\mathcal A$, an extractor $\mathcal E$, a plaintext generator $\mathcal M$ and auxiliary input $z$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ and $\mathcal E$ both receive $\mathrm{pp}$, the ciphertexts and $z$; neither receives $\mathrm{sk}$, and there is no oracle.
> - **Promise** — the ciphertexts are honest encryptions of the vectors $\mathcal M$ outputs.
> - **Quantifier** — $\forall \mathcal A\ \exists \mathcal E$ (both polynomial-size), and the bound holds for every efficient $\mathcal M$ and every $z$. `⚠️ CLAUDE – verify:` I read the order of the quantifiers from a summary of `[ISW21 Def 3.4]`; check whether $\mathcal E$ may depend on $\mathcal M$.
> - **Adaptivity** — none: $\mathcal A$ outputs once, after seeing the ciphertexts. #supplemented
>
> ---
> ### Experiment
> A *search* game: there is one branch, and the experiment itself outputs the bit. The challenger runs $\mathcal E$ on the view of $\mathcal A$.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$; $(\mathbf v_1, \dots, \mathbf v_m) \leftarrow \mathcal M(1^\lambda, \mathrm{pp})$; $\mathrm{ct}_i \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf v_i)$ | $\xrightarrow{\ \mathrm{pp},\, \mathrm{ct}_1, \dots, \mathrm{ct}_m\ }$ | |
> | 2 | | $\xleftarrow{\ \mathrm{ct}'_1, \dots, \mathrm{ct}'_k\ }$ | $(\mathrm{ct}'_1, \dots, \mathrm{ct}'_k) \leftarrow \mathcal A(\mathrm{pp}, \mathrm{ct}_1, \dots, \mathrm{ct}_m; z)$ |
> | 3 | $\boldsymbol\Pi \leftarrow \mathcal E(\mathrm{pp}, \mathrm{ct}_1, \dots, \mathrm{ct}_m; z)$; $\mathbf V_0 = \boldsymbol\Pi \cdot [\mathbf v_1 \mid \cdots \mid \mathbf v_m]^\top$ with rows $\mathbf v'_1, \dots, \mathbf v'_k$ | | |
> | 4 | output $1$ iff for some $i$: $\mathsf{Dec}(\mathrm{sk}, \mathrm{ct}'_i) \neq \perp$ and $\mathsf{Dec}(\mathrm{sk}, \mathrm{ct}'_i) \neq \mathbf v'_i$ | | |
>
> **Target** — several results, folded into one bit: the vector $(w_1, \dots, w_k)$ with $w_i = 1$ iff $\mathsf{Dec}(\mathrm{sk}, \mathrm{ct}'_i) \notin \{\perp, \mathbf v'_i\}$, one entry per output ciphertext. $\mathcal A$ wins if *any* output is unexplained, so $\mathsf{Expt} = \bigvee_i w_i$ `[ISW21 Def 3.4]`.
>
> ---
> ### Property
> $\mathsf{Adv}^\mathsf{lo}_{\Pi_\mathsf{Enc}}(\mathcal A, \mathcal E) = \Pr[\mathsf{Expt}(\mathcal A, \mathcal E) = 1]$, and $\Pi_\mathsf{Enc}$ is **strictly linear-only** if this is negligible in $\lambda$ `[ISW21 Def 3.4]`. In words: whatever valid ciphertext $\mathcal A$ outputs decrypts to a linear combination of the plaintexts it was given, and $\mathcal E$ can say which one without the secret key. #supplemented

> [!remark] Strict or affine
> `[ISW21 Remark 3.5]` contrasts this with the weaker notion of earlier work, where the extractor may explain the output of $\mathcal A$ by an *affine* function of the plaintexts. "Strictly" refers to the absence of the constant term. #supplemented

## Variant

- [[Strictly Linear Targeted Malleability]] — your stub, from [[LUNA]]; a two-world (simulator-style) comparison whose target is a vector of decryptions. Moved to its own note; still incomplete.

## Related

### Constructions
- [[LUNA]] — a designated-verifier SNARG whose soundness rests on a linear-only encryption

### Siblings
- [[Strictly Linear Targeted Malleability]] — the two-world version of the same idea
- [[Circuit Privacy]] — the other property asked of the same primitive; one protects the evaluator, the other the verifier's view of $\mathsf{Add}$

### Prerequisites
- [[Vector Encryption]], [[Security Game]], [[Adversary]]
