Reference:
- `[ISW21 x]` — Ishai, Su, Wu, _Shorter and Faster Post-Quantum Designated-Verifier zkSNARKs from Lattices_, CCS 2021 (ePrint 2021/977): https://eprint.iacr.org/2021/977.pdf. Definition 3.7 and Remark 3.8 were read through a summarizer, not verbatim.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - [[Vector Encryption]]: Import $(\lambda, \ell, \mathbb F, \mathrm{pp}, \mathrm{sk})$ and the algorithms $(\mathsf{Setup}, \mathsf{Enc}, \mathsf{Add})$.
> - $k$: the number of plaintext vectors $\mathbf v_i \in \mathbb F^\ell$ and of coefficients $y_i \in \mathbb F$.
> - $\mathcal S$: the simulator, an efficient algorithm that may depend on $\mathcal A$.
> - $\mathcal Y \subseteq \mathbb F^k$: the set the coefficients must come from, in the restricted variant.
> - $\mathbb A$: the class of efficient [[Adversary|adversaries]] (unbounded, for statistical circuit privacy). $\varepsilon$: the bound of `[ISW21 Def 3.7]`.

> [!definition] Circuit Privacy
> ### Scope
> A [[Vector Encryption]] $\Pi_\mathsf{Enc}$, the adversary class $\mathbb A$ of Parameters and a simulator $\mathcal S$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pp}$ **and** $\mathrm{sk}$, then the ciphertexts of its own vectors. There is no oracle.
> - **Promise** — the ciphertexts are honest encryptions of the vectors $\mathcal A$ chose; the coefficients are any $y_i \in \mathbb F$.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A\ \exists \mathcal S$: the simulator may depend on the adversary `[ISW21 Def 3.7]`. It sees only $(1^\lambda, \mathrm{pp}, \mathrm{sk})$ and the plaintext $\sum_i y_i \mathbf v_i$, never the coefficients.
> - **Adaptivity** — the vectors come first, after $(\mathrm{pp}, \mathrm{sk})$; the coefficients are chosen after $\mathcal A$ has seen the ciphertexts. One evaluation.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in row 5 only, **Game 0** (real) and **Game 1** (simulated). `[ISW21 Def 3.7]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$ | $\xrightarrow{\ \mathrm{pp},\, \mathrm{sk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf v_1, \dots, \mathbf v_k\ }$ | chooses vectors $\mathbf v_1, \dots, \mathbf v_k \in \mathbb F^\ell$ |
> | 3 | $\mathrm{ct}_i \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf v_i)$ for $i \in [k]$ | $\xrightarrow{\ \mathrm{ct}_1, \dots, \mathrm{ct}_k\ }$ | |
> | 4 | | $\xleftarrow{\ y_1, \dots, y_k\ }$ | chooses coefficients $y_1, \dots, y_k \in \mathbb F$ |
> | 5 | **Game 0**: $\mathrm{ct}^* \leftarrow \mathsf{Add}(\mathrm{pp}, \{\mathrm{ct}_i\}_{i \in [k]}, \{y_i\}_{i \in [k]})$<br>**Game 1**: $\mathrm{ct}^* \leftarrow \mathcal S(1^\lambda, \mathrm{pp}, \mathrm{sk}, \sum_{i \in [k]} y_i \mathbf v_i)$ | $\xrightarrow{\ \mathrm{ct}^*\ }$ | |
> | 6 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b^\mathsf{CP}(\mathcal A, \mathcal S)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0^\mathsf{CP}(\mathcal A, \mathcal S) = 1]$ and $\Pr[\mathsf{Expt}_1^\mathsf{CP}(\mathcal A, \mathcal S) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{CP}}_{\Pi_\mathsf{Enc}}(\mathcal A, \mathcal S) = \Big|\Pr\big[\mathsf{Expt}_0^\mathsf{CP}(\mathcal A, \mathcal S) = 1\big] - \Pr\big[\mathsf{Expt}_1^\mathsf{CP}(\mathcal A, \mathcal S) = 1\big]\Big|.$$
> - $\Pi_\mathsf{Enc}$ is **$\varepsilon$-circuit private** if for every $\mathcal A \in \mathbb A$ there is an efficient $\mathcal S$ with $\mathsf{Adv}^{\mathsf{CP}}_{\Pi_\mathsf{Enc}}(\mathcal A, \mathcal S) \leq 2\varepsilon$ `[ISW21 Def 3.7]`; the factor $2$ is explained in the remark below.
> - $\Pi_\mathsf{Enc}$ is **circuit private** if $\varepsilon$ is negligible in $\lambda$.
>
> It is a *distinguishing* game, see [[Security Game]].

> [!remark] What the property says
> A ciphertext produced by $\mathsf{Add}$ can be simulated from the plaintext $\sum_i y_i \mathbf v_i$ alone, even for a party that holds $\mathrm{sk}$: the output hides which coefficients $y_i$ produced it.

> [!remark] Notation in the literature
> - `[ISW21 Def 3.7]` writes $\mathsf{Encrypt}$ for $\mathsf{Enc}$, and calls the adversary *efficient and stateful*: one machine that chooses the vectors, then the coefficients, then the guess. It therefore knows $\mathbf v_i$ and $y_i$ when it guesses, and can compute $\sum_i y_i \mathbf v_i$ itself. [[Module HGSW]] encrypts with an extra index $i$.
> - The source computes both $\mathrm{ct}^*_0 \leftarrow \mathsf{Add}(\dots)$ and $\mathrm{ct}^*_1 \leftarrow \mathcal S(\dots)$, draws a bit $b$, sends $\mathrm{ct}^*_b$ and asks $\Pr[b' = b] \leq \tfrac12 + \varepsilon$. Since
>   $$\Pr[b' = b] = \tfrac12 + \tfrac12\big(\Pr[\mathsf{Expt}^\mathsf{CP}_1 = 1] - \Pr[\mathsf{Expt}^\mathsf{CP}_0 = 1]\big),$$
>   and $\mathcal A$ can flip its output, the bound $\varepsilon$ on the bit-guessing margin is the bound $2\varepsilon$ on the difference used here; see [[Indistinguishability under Chosen-Plaintext Attack#Bit-guessing form]].

## Variant

> [!definition] Circuit privacy with respect to a set `[ISW21 Def 3.7]`
> The same experiment, but in row 4 $\mathcal A$ must choose $(y_1, \dots, y_k) \in \mathcal Y$.

> [!definition] Multiple evaluations `[ISW21 Remark 3.8]`
> $\mathcal A$ submits several collections of coefficients, adaptively, and every answer is real in Game 0 and simulated in Game 1. The source says this follows from the single-evaluation notion by a hybrid argument.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$ | $\xrightarrow{\ \mathrm{pp},\, \mathrm{sk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf v_1, \dots, \mathbf v_k\ }$ | chooses vectors $\mathbf v_1, \dots, \mathbf v_k \in \mathbb F^\ell$ |
> | 3 | $\mathrm{ct}_i \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf v_i)$ for $i \in [k]$ | $\xrightarrow{\ \mathrm{ct}_1, \dots, \mathrm{ct}_k\ }$ | |
> | 4 | | $\xleftarrow{\ y^{(j)}_1, \dots, y^{(j)}_k\ }$ | **Evaluation queries** (repeated, adaptive, polynomially many times): chooses coefficients $y^{(j)}_1, \dots, y^{(j)}_k \in \mathbb F$ |
> | | **Game 0**: $\mathrm{ct}^*_j \leftarrow \mathsf{Add}(\mathrm{pp}, \{\mathrm{ct}_i\}_{i \in [k]}, \{y^{(j)}_i\}_{i \in [k]})$<br>**Game 1**: $\mathrm{ct}^*_j \leftarrow \mathcal S(1^\lambda, \mathrm{pp}, \mathrm{sk}, \sum_{i \in [k]} y^{(j)}_i \mathbf v_i)$ | $\xrightarrow{\ \mathrm{ct}^*_j\ }$ | |
> | 5 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |

> [!remark] Computational or statistical
> Circuit privacy is computational when $\mathcal A$ is efficient and statistical when $\mathcal A$ is unbounded. `[ISW21 Thm 3.23]` derives computational zero knowledge of the zkSNARK from computational circuit privacy, and statistical zero knowledge from statistical circuit privacy.

## Related

### Constructions
- [[Zero Knowledge]] — the property that circuit privacy of the vector encryption feeds into in `[ISW21 Thm 3.23]`

### Siblings
- `⚠️ CLAUDE – verify:` circuit privacy for [[Homomorphic Encryption]] has the same shape (an evaluated ciphertext hides the circuit); I did not check that note's wording or a source for it.

### Prerequisites
- [[Vector Encryption]], [[Security Game]], [[Adversary]]
