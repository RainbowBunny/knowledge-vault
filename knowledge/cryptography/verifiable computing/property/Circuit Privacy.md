Reference:
- `[ISW21 x]` — Ishai, Su, Wu, _Shorter and Faster Post-Quantum Designated-Verifier zkSNARKs from Lattices_, CCS 2021 (ePrint 2021/977): https://eprint.iacr.org/2021/977.pdf. Definition 3.7 and Remark 3.8 were read through a summarizer, not verbatim.
- `#supplemented` marks what I added to your text; its source is on this line. Delete the tag once you have read it.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - [[Vector Encryption]]: Import $(\lambda, \ell, \mathbb F, \mathrm{pp}, \mathrm{sk})$.
> - $k$: the number of plaintext vectors $\mathbf v_i \in \mathbb F^\ell$ and of coefficients $y_i \in \mathbb F$.
> - $\mathcal S$: the simulator, an efficient algorithm.
> - $\mathcal Y \subseteq \mathbb F^k$: the set the coefficients must come from, in the restricted variant.

> [!definition] Circuit Privacy
> ### Scope
> A [[Vector Encryption]] $\Pi_\mathsf{Enc}$, an efficient [[Adversary]] $\mathcal A = (\mathcal A_\mathsf{pt}, \mathcal A_\mathsf{coef}, \mathcal A_\mathsf{guess})$ and a simulator $\mathcal S$. The three phases of $\mathcal A$ share memory.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pp}$ **and** $\mathrm{sk}$, then the ciphertexts of its own vectors. There is no oracle.
> - **Promise** — the ciphertexts are honest encryptions of the vectors $\mathcal A$ chose; the coefficients are any $y_i \in \mathbb F$.
> - **Quantifier** — $\exists \mathcal S\ \forall \mathcal A$: the simulator is fixed first, and sees only $(1^\lambda, \mathrm{pp}, \mathrm{sk})$ and the plaintext $\sum_i y_i \mathbf v_i$, never the coefficients.
> - **Adaptivity** — the vectors come first; the coefficients are chosen after $\mathcal A$ has seen the ciphertexts. #supplemented
>
> ---
> ### Experiment
> An interaction between a challenger $\mathcal C$ and $\mathcal A$, played in two branches that differ in step 5 only: **Game 0** (real) and **Game 1** (simulated).
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$ | $\xrightarrow{\ \mathrm{pp},\, \mathrm{sk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf v_1, \dots, \mathbf v_k\ }$ | $(\mathbf{v}_1, \dots, \mathbf{v}_k) \leftarrow \mathcal{A}_{\mathsf{pt}}(\mathrm{pp}, \mathrm{sk})$ with $\mathbf{v}_i \in \mathbb{F}^\ell \; \forall i \in [k]$ |
> | 3 | $\mathrm{ct}_i \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf{v}_i) \; \forall i \in [k]$ | $\xrightarrow{\ \mathrm{ct}_1, \dots, \mathrm{ct}_k\ }$ | |
> | 4 #supplemented | | $\xleftarrow{\ y_1, \dots, y_k\ }$ | $(y_1, \dots, y_k) \leftarrow \mathcal{A}_\mathsf{coef}(\mathrm{ct}_1, \dots, \mathrm{ct}_k)$ |
> | 5 #supplemented | **Game 0**: $\mathrm{ct}^* \leftarrow \mathsf{Add}(\mathrm{pp}, \{\mathrm{ct}_i\}_{i \in [k]}, \{y_i\}_{i \in [k]})$<br>**Game 1**: $\mathrm{ct}^* \leftarrow \mathcal S(1^\lambda, \mathrm{pp}, \mathrm{sk}, \sum_{i \in [k]} y_i \mathbf v_i)$ | $\xrightarrow{\ \mathrm{ct}^*\ }$ | |
> | 6 #supplemented | | $\xleftarrow{\ b'\ }$ | $b' \leftarrow \mathcal{A}_\mathsf{guess}(\mathrm{ct}^*)$ |
>
> **Target** — one bit: $\mathsf{Expt}_b^\mathsf{CP}(\mathcal A, \mathcal S)$ is the bit $b'$ that $\mathcal A$ outputs in Game $b$.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{CP}}_{\Pi_\mathsf{Enc}}(\mathcal A, \mathcal S) = \Big|\Pr\big[\mathsf{Expt}_0^\mathsf{CP}(\mathcal A, \mathcal S) = 1\big] - \Pr\big[\mathsf{Expt}_1^\mathsf{CP}(\mathcal A, \mathcal S) = 1\big]\Big|.$$
> $\Pi_\mathsf{Enc}$ is **$\varepsilon$-circuit private** if some efficient $\mathcal S$ has $\mathsf{Adv}^{\mathsf{CP}}(\mathcal A, \mathcal S) \leq \varepsilon$ for every efficient $\mathcal A$, and **circuit private** if $\varepsilon$ is negligible in $\lambda$ `[ISW21 Def 3.7]`. It is a *distinguishing* game, see [[Security Game]]. #supplemented

> [!remark] What the property says
> A ciphertext produced by $\mathsf{Add}$ can be simulated from the plaintext $\sum_i y_i \mathbf v_i$ alone, even for a party that holds $\mathrm{sk}$: the output hides which coefficients $y_i$ produced it. #supplemented

> [!remark] The phases share memory
> $\mathcal A_\mathsf{pt}$, $\mathcal A_\mathsf{coef}$ and $\mathcal A_\mathsf{guess}$ are phases of one stateful adversary `[ISW21 Def 3.7]`. In particular $\mathcal A_\mathsf{guess}$ knows $\mathbf v_i$ and $y_i$, so it can compute the plaintext $\sum_i y_i \mathbf v_i$ itself. #supplemented

> [!remark] Differences from your draft and from the source
> - Your draft wrote $\mathcal A_\mathsf{coef}()$ with no input. The source lets $\mathcal A$ choose the coefficients after seeing the ciphertexts, so I wrote $\mathcal A_\mathsf{coef}(\mathrm{ct}_1, \dots, \mathrm{ct}_k)$.
> - Your draft wrote $\mathsf{Encrypt}$; the vault's [[Vector Encryption]] calls it $\mathsf{Enc}$ and drops the index. [[Module HGSW]] encrypts with an index $i$.
> - `[ISW21 Def 3.7]` draws a bit $b$, hands $\mathcal A$ the real or the simulated ciphertext, and asks for $\Pr[b' = b] \leq 1/2 + \varepsilon$. `⚠️ CLAUDE – verify:` $\Pr[b' = b] = \tfrac12 + \tfrac12\big(\Pr[\mathsf{Expt}_1 = 1] - \Pr[\mathsf{Expt}_0 = 1]\big)$, so the difference above is twice the source's margin: $\mathsf{Adv}^\mathsf{CP} = 2\,\lvert\Pr[b' = b] - \tfrac12\rvert$. This is my computation, not a statement in the source; check it before comparing numbers across papers.

## Variant

> [!definition] Circuit privacy with respect to a set `[ISW21 Def 3.7]`
> The same experiment, but $\mathcal A_\mathsf{coef}$ must output $(y_1, \dots, y_k) \in \mathcal Y$. #supplemented

> [!definition] Multiple evaluations `[ISW21 Remark 3.8]`
> $\mathcal A$ may submit several collections of coefficients, adaptively, and receive in each answer a real or a simulated ciphertext (all in the same branch). The source says this follows from the single-evaluation notion by a hybrid argument. #supplemented

> [!remark] Computational or statistical
> Circuit privacy is computational when $\mathcal A$ is efficient and statistical when $\mathcal A$ is unbounded. `[ISW21 Thm 3.23]` derives computational zero knowledge of the zkSNARK from computational circuit privacy, and statistical zero knowledge from statistical circuit privacy. #supplemented

## Related

### Constructions
- [[Zero Knowledge]] — the property that circuit privacy of the vector encryption feeds into in `[ISW21 Thm 3.23]`

### Siblings
- `⚠️ CLAUDE – verify:` circuit privacy for [[Homomorphic Encryption]] has the same shape (an evaluated ciphertext hides the circuit); I did not check that note's wording or a source for it.

### Prerequisites
- [[Vector Encryption]], [[Security Game]], [[Adversary]]
