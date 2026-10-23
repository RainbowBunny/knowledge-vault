Reference:
- `[RQC20]` — C. Aguilar-Melchor, N. Aragon, S. Bettaieb, L. Bidoux, O. Blazy, M. Bros, A. Couvreur, J.-C. Deneuville, P. Gaborit, A. Hauteville, G. Zémor, _Rank Quasi-Cyclic (RQC)_, NIST second-round specification, 21 April 2020: https://pqc-rqc.org/doc/rqc-specification_2020-04-21.pdf (§2.1.1, Definitions 2.1.2 and 2.1.4; §2.1.4, Definitions 2.1.13–2.1.15).
- `[ABDGZ18]` — C. Aguilar-Melchor, O. Blazy, J.-C. Deneuville, P. Gaborit, G. Zémor, _Efficient Encryption from Random Quasi-Cyclic Codes_, IEEE Trans. Inf. Theory 64(5), 2018; arXiv:1612.05572: https://arxiv.org/abs/1612.05572 (§II-B, rank metric).

## Parameters

> [!definition] Parameters
> - $n$: Length of the code.
> - $k$: Dimension of the code.
> - $w$: Rank weight of the error.
> - $q$: Prime power.
> - $m$: Extension degree; $\mathbb F_{q^m}$ is the field of the code.
> - $\omega$: Rank metric. For $\mathbf x \in \mathbb F_{q^m}^n$, $M(\mathbf x) \in \mathbb F_q^{m \times n}$ writes each coordinate in a basis of $\mathbb F_{q^m}$ over $\mathbb F_q$, and $\omega(\mathbf x) = \operatorname{Rank} M(\mathbf x)$, the dimension of the support of $\mathbf x$ `[RQC20 Def 2.1.2, 2.1.4]`.
> - $\mathcal A$: an [[Adversary]], one stateful interactive machine ([[Security Game]]).

## Distribution

> [!definition] Rank Syndrome Decoding Distribution
> ### Distribution
> Sampling Experiment: $\text{RSD}(n, k, w)$ `[RQC20 Def 2.1.13]`
> 1. $\mathbf H \xleftarrow{\$} \mathbb F_{q^m}^{(n - k) \times n}$
> 2. $\mathbf x \xleftarrow{\$} \mathbb F_{q^m}^n$ with $\omega(\mathbf x) = w$
> 3. Output $(\mathbf H, \mathbf H\mathbf x^\top)$

## Problem

### Search Variant

> [!definition] Search Rank Syndrome Decoding Problem Advantage
> Reference Name: $\text{SRSD}(n, k, w)$
> 
> ---
> A search game: find an error of rank weight $w$ with the given syndrome. `[RQC20 Def 2.1.14]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathbf H, \mathbf y^\top) \leftarrow \text{RSD}(n, k, w)$ | $\xrightarrow{\ (\mathbf H,\, \mathbf y)\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x'\ }$ | outputs a candidate error $\mathbf x' \in \mathbb F_{q^m}^n$ |
> | 3 | checks $\mathbf H \mathbf x'^\top = \mathbf y^\top$<br>checks $\omega(\mathbf x') = w$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $\mathbf H \mathbf x'^\top = \mathbf y^\top$;
> - $\omega(\mathbf x') = w$.
>
> $$\text{Adv}^\text{search}_\text{RSD}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
>
> - **Search RSD assumption** — $\text{Adv}^\text{search}_\text{RSD}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$.

### Decision Variant

> [!definition] Decision Rank Syndrome Decoding Problem Advantage
> Reference Name: $\text{DRSD}(n, k, w)$
> 
> ---
> A distinguishing game: an RSD sample against a uniform pair; the two branches differ in row 1 only. `[RQC20 Def 2.1.15]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | **Game 0**: $(\mathbf H, \mathbf y^\top) \leftarrow \text{RSD}(n, k, w)$<br>**Game 1**: $(\mathbf H, \mathbf y^\top) \xleftarrow{\$} \mathbb F_{q^m}^{(n - k) \times n} \times \mathbb F_{q^m}^{(n - k)}$ | $\xrightarrow{\ (\mathbf H,\, \mathbf y)\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> $$\text{Adv}^\text{decide}_\text{RSD}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
>
> - **Decision RSD assumption** — $\text{Adv}^\text{decide}_\text{RSD}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$.

> [!remark] Notation in the literature
> - `[RQC20]` writes the rank weight as $\lVert \mathbf x \rVert$; `[ABDGZ18 §II-B]` writes $\omega(\mathbf x)$ for both the Hamming and the rank weight and obtains RSD as the syndrome decoding problem of [[Syndrome Decoding Assumption]] with the rank metric.
> - `[RQC20 Def 2.1.15]` states the decision problem as "decide with non-negligible advantage" between the two distributions; the advantage above is that difference written out.
