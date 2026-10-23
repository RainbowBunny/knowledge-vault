---
aliases: [Strictly Linear-Only, Linear-Only, Linear-Only Vector Encryption]
---
Reference:
- `[ISW21]` — Y. Ishai, H. Su, D. J. Wu, _Shorter and Faster Post-Quantum Designated-Verifier zkSNARKs from Lattices_, ACM CCS 2021; full version ePrint 2021/977: https://eprint.iacr.org/2021/977.pdf
- `[BISW17]` — D. Boneh, Y. Ishai, A. Sahai, D. J. Wu, _Lattice-Based SNARGs and Their Application to More Efficient Obfuscation_, EUROCRYPT 2017; ePrint 2017/240: https://eprint.iacr.org/2017/240.pdf
- `[BCI+13]` — N. Bitansky, A. Chiesa, Y. Ishai, R. Ostrovsky, O. Paneth, _Succinct Non-Interactive Arguments via Linear Interactive Proofs_, TCC 2013; ePrint 2012/718: https://eprint.iacr.org/2012/718.pdf

## Definition

> [!definition] Parameters
> - [[Vector Encryption]]: Import $(\lambda, \ell, \mathbb F, \mathrm{pp}, \mathrm{sk})$ and the algorithms $(\mathsf{Setup}, \mathsf{Enc}, \mathsf{Dec})$.
> - $m$: the number of ciphertexts $\mathcal A$ receives. $k$: the number of ciphertexts it outputs.
> - $\mathcal M$: an efficient plaintext generator; on input $(1^\lambda, \mathrm{pp})$ it outputs $\mathbf v_1, \dots, \mathbf v_m \in \mathbb F^\ell$.
> - $z \in \{0, 1\}^{\mathrm{poly}(\lambda)}$: the auxiliary input of $\mathcal A$.
> - $\mathcal E$: the extractor, of polynomial size. $\boldsymbol\Pi \in \mathbb F^{k \times m}$: the matrix it outputs. $\mathbf V' = \boldsymbol\Pi \cdot [\mathbf v_1 \mid \cdots \mid \mathbf v_m]^\top \in \mathbb F^{k \times \ell}$, with rows $\mathbf v'_1, \dots, \mathbf v'_k$.
>
> `[ISW21 Def 3.4]`

> [!definition] Linear-Only Security
> ### Scope
> A [[Vector Encryption]] $\Pi_\mathsf{Enc}$, a polynomial-size [[Adversary]] $\mathcal A$, an extractor $\mathcal E$, a plaintext generator $\mathcal M$ and an auxiliary input $z$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pp}$ and the ciphertexts, and holds $z$ from the start; it never sees $\mathrm{sk}$ and has no oracle. $\mathcal E$ receives the same $(\mathrm{pp}, \mathrm{ct}_1, \dots, \mathrm{ct}_m; z)$ — not $\mathrm{sk}$, not the plaintexts, not $\mathcal M$.
> - **Promise** — the ciphertexts are honest encryptions of the vectors $\mathcal M$ outputs.
> - **Quantifier** — $\forall \mathcal A\ \exists \mathcal E$, both of polynomial size, such that the bound holds for every $\lambda$, every $z$ and every efficient $\mathcal M$: since $\mathcal M$ is quantified after $\mathcal E$, the extractor may not depend on it.
> - **Adaptivity** — none: $\mathcal A$ speaks once, after receiving the ciphertexts.
>
> ---
> ### Experiment
> $\mathsf{ExptLinearExt}$, a search game: one branch, and the challenger runs $\mathcal E$ after $\mathcal A$ has spoken. `[ISW21 Def 3.4]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$<br>$(\mathbf v_1, \dots, \mathbf v_m) \leftarrow \mathcal M(1^\lambda, \mathrm{pp})$<br>$\mathrm{ct}_i \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf v_i)$ for $i \in [m]$ | $\xrightarrow{\ \mathrm{pp},\, \mathrm{ct}_1, \dots, \mathrm{ct}_m\ }$ | |
> | 2 | | $\xleftarrow{\ \mathrm{ct}'_1, \dots, \mathrm{ct}'_k\ }$ | outputs ciphertexts $\mathrm{ct}'_1, \dots, \mathrm{ct}'_k$ |
> | 3 | $\boldsymbol\Pi \leftarrow \mathcal E(\mathrm{pp}, \mathrm{ct}_1, \dots, \mathrm{ct}_m; z)$<br>$\mathbf V' \leftarrow \boldsymbol\Pi \cdot [\mathbf v_1 \mid \cdots \mid \mathbf v_m]^\top$ | | |
>
> **Goal** — $\mathcal A$ wins iff some output is valid but unexplained: there is an $i \in [k]$ with both
> - $\mathsf{Dec}(\mathrm{sk}, \mathrm{ct}'_i) \neq \perp$, and
> - $\mathsf{Dec}(\mathrm{sk}, \mathrm{ct}'_i) \neq \mathbf v'_i$.
>
> ---
> ### Property
> $$\mathsf{Adv}^\mathsf{lo}_{\Pi_\mathsf{Enc}}(\mathcal A, \mathcal E) = \Pr[\mathcal A \text{ wins}].$$
> - $\Pi_\mathsf{Enc}$ is **strictly linear-only** if for every polynomial-size $\mathcal A$ there is a polynomial-size $\mathcal E$ with $\mathsf{Adv}^\mathsf{lo}_{\Pi_\mathsf{Enc}}(\mathcal A, \mathcal E) = \mathsf{negl}(\lambda)$ for all $\lambda$, $z$ and efficient $\mathcal M$. `[ISW21 Def 3.4]`
>
> It is a *search* game, see [[Security Game]].

> [!remark] Strict or affine
> Every strategy that produces a valid ciphertext must be a *linear* combination of the given ciphertexts. Earlier definitions `[BCI+13, BISW17]` let the extractor explain $\mathcal A$ by an *affine* function. In the public-key setting that is the best possible, since the adversary can encrypt a vector of its choice and add it; in the secret-key setting it is plausible that the adversary cannot produce fresh ciphertexts at all. ISW21 call the stronger notion *strict* linear-only. `[ISW21 Remark 3.5]` `[BISW17]` writes "linear-only" for "affine-only", following `[BCI+13]` `[BISW17 §1.1, fn. 4]`.

> [!remark] Auxiliary inputs
> Requiring $\mathcal E$ to succeed for every $z$ may be too strong — $z$ can encode a hard problem the extractor would have to solve. It suffices to require the definition for "benign" auxiliary-input distributions, e.g. uniform $z$. `[ISW21 Remark 3.6]`

> [!remark] Notation in the literature
> `[ISW21]` writes $\mathsf{Encrypt}$, $\mathsf{Decrypt}$ for $\mathsf{Enc}$, $\mathsf{Dec}$, and calls the experiment $\mathsf{ExptLinearExt}_{\Pi_\mathsf{Enc}, \mathcal A, \mathcal M, \mathcal E, z}(1^\lambda)$; there $\mathcal A$ is run as $\mathcal A(\mathrm{pp}, \mathrm{ct}_1, \dots, \mathrm{ct}_m; z)$ — here it is one interactive machine that receives row 1 and holds $z$.

## Property

> [!theorem] SNARKs from linear-only vector encryption — a linear PCP and a strictly linear-only scheme give a designated-verifier SNARK
> If a [[Linear Probabilistically Checkable Proofs|linear PCP]] is statistically sound against linear provers, and $\Pi_\mathsf{Enc}$ is CPA-secure (for up to $m$ messages) and strictly linear-only, then the compiled SNARK is a designated-verifier succinct argument of knowledge for R1CS in the preprocessing model. `[ISW21 Thm 3.21]`, after `[BCI+13, BISW17]`

## Variant

- [[Strictly Linear Targeted Malleability]] — the simulation-based counterpart: a simulator, possibly inefficient, replaces the extractor; it gives soundness rather than knowledge soundness `[BISW17 Def 4.2, Remark 4.9]`.

## Related

### Instantiations
- `[ISW21]`'s own lattice-based vector encryption (Construction 3.11) is conjectured strictly linear-only `[ISW21 Conj 3.15]`
- [[Module HGSW]] — `[LUNA]` assumes the weaker [[Strictly Linear Targeted Malleability|strict linear targeted malleability]] for it instead

### Siblings
- [[Strictly Linear Targeted Malleability]]
- [[Circuit Privacy]] — the other property asked of the same primitive

### Prerequisites
- [[Vector Encryption]], [[Security Game]], [[Adversary]]
