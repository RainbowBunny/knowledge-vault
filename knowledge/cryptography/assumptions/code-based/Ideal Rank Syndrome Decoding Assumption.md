Reference:
- `[RQC20]` — C. Aguilar-Melchor, N. Aragon, S. Bettaieb, L. Bidoux, O. Blazy, M. Bros, A. Couvreur, J.-C. Deneuville, P. Gaborit, A. Hauteville, G. Zémor, _Rank Quasi-Cyclic (RQC)_, NIST second-round specification, 21 April 2020: https://pqc-rqc.org/doc/rqc-specification_2020-04-21.pdf (§2.1.2, Definitions 2.1.1 and 2.1.5; §2.1.4, Definitions 2.1.16–2.1.18 and Assumption 1).

## Parameters

> [!definition] Parameters
> - [[Rank Syndrome Decoding Assumption]]: Import $(q, m, \omega)$.
> - $n$: Length of one block; the code has length $sn$.
> - $w$: Rank weight of the whole error $\mathbf x = (\mathbf x_1, \dots, \mathbf x_s)$.
> - $s$: Index of the code (how coarse is the ring structure).
> - $P \in \mathbb F_q[X]$: an irreducible polynomial of degree $n$; $\mathbf u \mathbf v$ is the product of $\mathbf u, \mathbf v \in \mathbb F_{q^m}^n$ read as polynomials modulo $P$.
> - $\mathcal C$: an $s$-ideal code, the $[sn, n]_{q^m}$ code $\{(\mathbf u, \mathbf u \mathbf g_1, \dots, \mathbf u \mathbf g_{s-1})\}$ with $\mathbf g_i \in \mathbb F_{q^m}^n$ `[RQC20 Def 2.1.5]`.
> - $\mathcal S(n, s)$: the set of systematic parity-check matrices $\mathbf H \in \mathbb F_{q^m}^{(sn - n) \times sn}$ of $s$-ideal codes.
> - $\mathcal A$: an [[Adversary]], one stateful interactive machine ([[Security Game]]).

## Distribution

> [!definition] Ideal Rank Syndrome Decoding Distribution
> ### Distribution
> Sampling Experiment: $s\text{-IRSD}(n, w)$ `[RQC20 Def 2.1.16]`
> 1. $\mathbf H \xleftarrow{\$} \mathcal S(n, s)$: Parity check matrix $\mathbf H$ of an $s$-ideal code $\mathcal C$.
> 2. $\mathbf x = (\mathbf x_1, \dots, \mathbf x_s) \xleftarrow{\$} \mathbb F_{q^m}^{sn}$ with $\omega(\mathbf x) = w$
> 3. Output $(\mathbf H, \mathbf H\mathbf x^T)$
>
> The weight is that of the whole vector $\mathbf x$, whose support is spanned by the coordinates of all $s$ blocks, not a weight per block as in [[Quasi-Cyclic Syndrome Decoding Assumption]].

## Problem

### Search Variant

> [!definition] Search Ideal Rank Syndrome Decoding Problem Advantage
> Reference Name: $s\text{-IRSD}(n, w)$
> 
> ---
> A search game: find an error of rank weight $w$ with the given syndrome. `[RQC20 Def 2.1.17]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathbf H, \mathbf y^T) \leftarrow s\text{-IRSD}(n, w)$ | $\xrightarrow{\ (\mathbf H,\, \mathbf y)\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x'\ }$ | outputs a candidate error $\mathbf x' \in \mathbb F_{q^m}^{sn}$ |
> | 3 | checks $\mathbf H \mathbf x'^T = \mathbf y^T$<br>checks $\omega(\mathbf x') = w$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $\mathbf H \mathbf x'^T = \mathbf y^T$;
> - $\omega(\mathbf x') = w$.
>
> $$\text{Adv}^\text{search}_\text{IRSD}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
>
> - **Search $s$-IRSD assumption** — $\text{Adv}^\text{search}_\text{IRSD}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$.

### Decision Variant

> [!definition] Decision Ideal Rank Syndrome Decoding Problem Advantage
> Reference Name: $s\text{-DIRSD}(n, w)$
> 
> ---
> A distinguishing game: an $s$-IRSD sample against a uniform syndrome for a matrix of the same shape; the two branches differ in row 1 only. `[RQC20 Def 2.1.18]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | **Game 0**: $(\mathbf H, \mathbf y^T) \leftarrow s\text{-IRSD}(n, w)$<br>**Game 1**: $(\mathbf H, \mathbf y^T) \xleftarrow{\$} \mathcal S(n, s) \times \mathbb F_{q^m}^{sn - n}$ | $\xrightarrow{\ (\mathbf H,\, \mathbf y)\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> $$\text{Adv}^\text{decide}_\text{IRSD}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
>
> - **Decision $s$-IRSD assumption** — $\text{Adv}^\text{decide}_\text{IRSD}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$.

> [!remark] Notation in the literature
> - `[RQC20]` writes the rank weight as $\lVert \mathbf x \rVert$ and the set of matrices as $\mathcal S(n, s)$.
> - `[RQC20 Def 2.1.17]` writes the search instance with a uniform syndrome $\mathbf y \leftarrow \mathbb F_{q^m}^{sn - n}$; here $(\mathbf H, \mathbf y)$ comes from $s\text{-IRSD}(n, w)$, as in `[RQC20 Def 2.1.14]` for RSD, so that a solution exists.
> - In the decision game the matrix stays structured in Game 1: only the syndrome is uniform.

## Claim

> [!remark]
> `[RQC20 §2.1.4, Assumption 1]`: no general complexity result is known for ideal codes, and no generic attack is known that exploits their structure. No reduction from the search to the decision version of $s$-IRSD is known, so the decision variant is assumed separately.
