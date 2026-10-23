Reference:
- `[ABDGZ18]` — C. Aguilar-Melchor, O. Blazy, J.-C. Deneuville, P. Gaborit, G. Zémor, _Efficient Encryption from Random Quasi-Cyclic Codes_, IEEE Trans. Inf. Theory 64(5), 2018; arXiv:1612.05572: https://arxiv.org/abs/1612.05572 (Definitions 8–10).
- `[HQC25]` — P. Gaborit, C. Aguilar-Melchor, N. Aragon et al., _Hamming Quasi-Cyclic (HQC)_, specification, 22 August 2025: https://www.pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf (§2.3, Definitions 2.3.1–2.3.3).
- `[BMvT78]` — E. Berlekamp, R. McEliece, H. van Tilborg, _On the Inherent Intractability of Certain Coding Problems_, IEEE Trans. Inf. Theory 24(3), 1978: http://authors.library.caltech.edu/5607/1/BERieeetit78.pdf
- `[AIK09]` — B. Applebaum, Y. Ishai, E. Kushilevitz, _Cryptography with Constant Input Locality_, J. Cryptology 22(4), 2009: https://link.springer.com/article/10.1007/s00145-009-9039-0

## Definition

> [!definition] Parameters
> - [[Syndrome Decoding Problem]]: Import $(n, k, w, \mathbb{F}_2, \mathsf{wt}_\mathsf{H})$.
> - $\mathcal A$: an [[Adversary]], one stateful interactive machine ([[Security Game]]).

### Distribution

> [!definition] Syndrome Decoding Distribution
> ### Distribution
> Sampling experiment: $\text{SD}(n, k, w)$ `[HQC25 Def 2.3.1]`, `[ABDGZ18 Def 8]`
> 1. $\mathbf{H} \xleftarrow{\$} \mathbb{F}_2^{(n - k) \times n}$ ([[Linear Code#Generator Matrix and Parity-Check Matrix|Parity-Check Matrix]]).
> 2. $\mathbf{x} \xleftarrow{\$} \mathcal{S}^n_w(\mathbb{F}_2)$ ([[Hamming Sphere]]), so $\mathsf{wt}_\mathsf{H}(\mathbf x) = w$.
> 3. Output $(\mathbf{H}, \sigma(\mathbf{x}) = \mathbf{H}\mathbf{x}^{T})$.

## Problem

### Search Variant

> [!definition] Search Syndrome Decoding Problem Advantage
> Reference Name: $\text{SSD}(n, k, w)$
> 
> ---
> A search game: find an error of weight $w$ with the given syndrome. `[ABDGZ18 Def 9]`, `[HQC25 Def 2.3.2]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathbf H, \mathbf y^T) \leftarrow \text{SD}(n, k, w)$ | $\xrightarrow{\ (\mathbf H,\, \mathbf y)\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x'\ }$ | outputs a candidate error $\mathbf x' \in \mathbb F_2^n$ |
> | 3 | checks $\mathbf H \mathbf x'^T = \mathbf y^T$<br>checks $\mathsf{wt}_\mathsf{H}(\mathbf x') = w$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $\mathbf H \mathbf x'^T = \mathbf y^T$;
> - $\mathsf{wt}_\mathsf{H}(\mathbf x') = w$.
>
> $$\text{Adv}^\text{search}_\text{SD}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
>
> - **Search SD assumption** — $\text{Adv}^\text{search}_\text{SD}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$.

### Decision Variant

> [!definition] Decision Syndrome Decoding Problem Advantage
> Reference Name: $\text{DSD}(n, k, w)$
> 
> ---
> A distinguishing game: an SD sample against a uniform pair; the two branches differ in row 1 only. `[ABDGZ18 Def 10]`, `[HQC25 Def 2.3.3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | **Game 0**: $(\mathbf H, \mathbf y^T) \leftarrow \text{SD}(n, k, w)$<br>**Game 1**: $(\mathbf H, \mathbf y^T) \xleftarrow{\$} \mathbb F_2^{(n - k) \times n} \times \mathbb F_2^{n - k}$ | $\xrightarrow{\ (\mathbf H,\, \mathbf y)\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> $$\text{Adv}^\text{decide}_\text{SD}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
>
> - **Decision SD assumption** — $\text{Adv}^\text{decide}_\text{SD}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$.

> [!remark] Notation in the literature
> - `[ABDGZ18 Def 8–10]` state the three definitions over a field $\mathbb F$ and write the weight as $\omega(\mathbf x)$; `[HQC25 Def 2.3.1–2.3.3]` fix $\mathbb F = \mathbb F_2$ and write the weight bound as $\omega$ too. Here the weight is $\mathsf{wt}_\mathsf{H}$ and the bound is $w$, as in [[Syndrome Decoding Problem]].
> - Both sources state the decision problem as "decide with non-negligible advantage whether $(\mathbf H, \mathbf y^T)$ came from $\text{SD}(n, k, w)$ or from the uniform distribution"; the advantage above is that difference written out.

## Claim

> [!remark]
> - With $\mathsf{wt}_\mathsf{H}$ the Hamming weight, the syndrome decoding problem is NP-complete `[BMvT78]`; see [[Syndrome Decoding Problem]].
> - It can be seen as LPN with a fixed number of samples.
> - NP-completeness is a worst-case statement and does not imply that the average-case games above are hard: for codes no worst-case to average-case reduction is known, unlike for lattices ([[Note Layouts]] § 9).

> [!remark]
> The decision variant is polynomially equivalent to the search variant `[AIK09]`; `[HQC25 §2.3]` states the same.
