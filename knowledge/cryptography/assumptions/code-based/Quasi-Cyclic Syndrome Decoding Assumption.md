Reference:
- `[HQC25]` — P. Gaborit, C. Aguilar-Melchor, N. Aragon et al., _Hamming Quasi-Cyclic (HQC)_, specification, 22 August 2025: https://www.pqc-hqc.org/doc/hqc_specifications_2025_08_22.pdf (§2.1 ring notation; §2.3, Definitions 2.3.4–2.3.9).
- `[ABDGZ18]` — C. Aguilar-Melchor, O. Blazy, J.-C. Deneuville, P. Gaborit, G. Zémor, _Efficient Encryption from Random Quasi-Cyclic Codes_, IEEE Trans. Inf. Theory 64(5), 2018; arXiv:1612.05572: https://arxiv.org/abs/1612.05572 (Definitions 7, 11–13).

## Parameters

> [!definition] Parameters
> - [[Syndrome Decoding Problem]]: Import $(\mathbb F_2, \mathsf{wt}_\mathsf{H})$.
> - $n$: length of one block; the code has length $sn$. In HQC $n$ is a prime with $(X^n - 1)/(X - 1)$ irreducible over $\mathbb F_2$.
> - $w$: Hamming weight of each error block.
> - $s$: index of the code (how coarse is the ring structure): the number of blocks.
> - $\mathcal R = \mathbb F_2[X]/(X^n - 1)$: the ring; a vector of $\mathbb F_2^n$ and a polynomial of $\mathcal R$ are the same thing, and $\mathrm{rot}(\mathbf h)$ is the circulant matrix with first column $\mathbf h$ `[HQC25 §2.1]`.
> - $\mathcal C$: [[Code Properties#Systematic|systematic]] [[Code Properties#Cyclic and Quasi-Cyclic|Quasi-Cyclic]] code of index $s$ and rate $1/s$, with parity-check matrix $\mathbf H \in \mathbb F_2^{(sn - n) \times sn}$. For $s = 2$, $\mathbf H = (\mathbf I_n \ \ \mathrm{rot}(\mathbf h))$.
> - $b_1, b_2 \in \{0, 1\}$: parity bits, in the decision variant only.
> - $\mathcal A$: an [[Adversary]], one stateful interactive machine ([[Security Game]]).

## Distribution

> [!definition] Quasi-Cyclic Syndrome Decoding Distribution
> ### Distribution
> Sampling Experiment: $s\text{-QCSD}(n, w)$ `[HQC25 Def 2.3.4]`, `[ABDGZ18 Def 11]`
> 1. $\mathbf H \xleftarrow{\$}$ parity-check matrices of $\mathcal C$, so $\mathbf H \in \mathbb F_2^{(sn - n) \times sn}$.
> 2. $\mathbf x = (\mathbf x_1, \dots, \mathbf x_s) \xleftarrow{\$} \mathbb F_2^{sn}$ with $\mathsf{wt}_\mathsf{H}(\mathbf x_i) = w$ for $i = 1, \dots, s$.
> 3. Outputs $(\mathbf H, \mathbf y^T = \mathbf H \mathbf x^T)$.

## Problem

### Search Variant

> [!definition] Search Syndrome Decoding Problem Advantage
> Reference Name: $s\text{-QCSD}(n, w)$
>
> ---
> A search game: find an error with $s$ blocks of weight $w$ and the given syndrome. `[ABDGZ18 Def 12]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathbf H, \mathbf y^T) \leftarrow s\text{-QCSD}(n, w)$ | $\xrightarrow{\ (\mathbf H,\, \mathbf y)\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x'\ }$ | outputs a candidate error $\mathbf x' = (\mathbf x'_1, \dots, \mathbf x'_s) \in \mathbb F_2^{sn}$ |
> | 3 | checks $\mathbf H \mathbf x'^T = \mathbf y^T$<br>checks $\mathsf{wt}_\mathsf{H}(\mathbf x'_i) = w$ for $i = 1, \dots, s$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $\mathbf H \mathbf x'^T = \mathbf y^T$;
> - $\mathsf{wt}_\mathsf{H}(\mathbf x'_i) = w$ for every $i = 1, \dots, s$.
>
> $$\text{Adv}^\text{search}_{s\text{-QCSD}}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
>
> - **Search $s$-QCSD assumption** — $\text{Adv}^\text{search}_{s\text{-QCSD}}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$.

### Decision Variant

> [!definition] Parity-Restricted Uniform Distribution
> The sets of vectors and of parity-check matrices of a given parity `[HQC25 §2.3]`:
> - $\mathbb F_{2, b}^{\,n} = \{\, \mathbf h \in \mathbb F_2^{\,n} : \mathbf h(1) = b \bmod 2 \,\}$, the vectors whose coefficients sum to $b$;
> - $\mathbb F_{2, b_1}^{\,n \times 2n} = \{\, \mathbf H = (\mathbf I_n \ \ \mathrm{rot}(\mathbf h)) : \mathbf h \in \mathbb F_{2, b_1}^{\,n} \,\}$.
>
> Sampling Experiment: $2\text{-QCSD-P}(n, w, b_1, b_2)$, with $b_2 = w + b_1 w \bmod 2$ `[HQC25 Def 2.3.6]`
> 1. $\mathbf H \xleftarrow{\$} \mathbb F_{2, b_1}^{\,n \times 2n}$.
> 2. $\mathbf x = (\mathbf x_1, \mathbf x_2) \xleftarrow{\$} \mathbb F_2^{2n}$ with $\mathsf{wt}_\mathsf{H}(\mathbf x_1) = \mathsf{wt}_\mathsf{H}(\mathbf x_2) = w$.
> 3. Outputs $(\mathbf H, \mathbf y^T = \mathbf H \mathbf x^T) \in \mathbb F_{2, b_1}^{\,n \times 2n} \times \mathbb F_{2, b_2}^{\,n}$.
>
> **Note:** the parity of $\mathbf h$ is fixed to $b_1$ in both games and the syndrome lies in $\mathbb F_{2, b_2}^{\,n}$ in both games: $\mathbf y = \mathbf x_1 + \mathbf h \mathbf x_2$ in $\mathcal R$, so $\mathbf y(1) = w + b_1 w \bmod 2$ is *publicly computable*.

> [!definition] Decision s-QCSD Advantage
> Reference Name: $2\text{-DQCSD-P}(n, w, b_1, b_2)$
>
> ---
> A distinguishing game: a $2$-QCSD-P sample against a uniform pair of the same parities; the two branches differ in row 1 only. `[HQC25 Def 2.3.7]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | **Game 0**: $(\mathbf H, \mathbf y^T) \leftarrow 2\text{-QCSD-P}(n, w, b_1, b_2)$<br>**Game 1**: $(\mathbf H, \mathbf y^T) \xleftarrow{\$} \mathbb F_{2, b_1}^{\,n \times 2n} \times \mathbb F_{2, b_2}^{\,n}$ | $\xrightarrow{\ (\mathbf H,\, \mathbf y)\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> $$\mathsf{Adv}^{\mathsf{decide}}_{2\text{-}\mathsf{QCSD}\text{-}\mathsf{P}}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
>
> - **Decision $2$-QCSD-P assumption** — $\mathsf{Adv}^{\mathsf{decide}}_{2\text{-}\mathsf{QCSD}\text{-}\mathsf{P}}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$.

> [!remark] Why the parity restriction is mandatory
> - `[HQC25 Def 2.3.5]` and `[ABDGZ18 Def 13]` also state a decision problem $s$-DQCSD without parity: Game 1 samples $(\mathbf H, \mathbf y)$ uniformly from $\mathbb F_2^{(sn - n) \times sn} \times \mathbb F_2^{sn - n}$.
> - Against that uniform distribution the assumption is trivially false: the planted syndrome's parity is a deterministic, public function of $(\mathbf H, w)$, while a uniform $\mathbf y$ has a uniform parity bit. For $s = 2$, the distinguisher "output 1 iff $\mathbf y(1) = w + \mathbf h(1) w \bmod 2$" has $\Pr[\mathsf{Expt}_0 = 1] = 1$ and $\Pr[\mathsf{Expt}_1 = 1] = 1/2$, so advantage $\tfrac12$, in constant time.
> - `[HQC25 §2.3]`: "In order to avoid trivial distinguishers, an additional condition on the parity of the syndrome is added to the problem"; the condition costs at most one bit of security. The repair restricts the ideal world to the correct parities, the largest ideal world the planted distribution can plausibly be confused with. (Same repair pattern as the statistical-ceiling discussion: locate the efficiently computable statistic that separates the worlds, and restrict the ideal world to match it.)
> - For $s = 3$, `[HQC25 Def 2.3.8–2.3.9]` define $3$-QCSD-PT and $3$-DQCSD-PT: both $\mathbf h_1, \mathbf h_2$ have fixed parities, the first syndrome block has parity $b_3 = w + b_1 w \bmod 2$, and the second block is truncated to $n - \ell$ coordinates.

> [!remark] Notation in the literature
> - `[ABDGZ18 Def 11–13]` work over a field $\mathbb F$ and write the Hamming weight as $\omega$; `[HQC25]` fixes $\mathbb F_2$, writes the weight bound as $\omega$ and numbers the blocks $\mathbf x_0, \dots, \mathbf x_{s-1}$.
> - `[ABDGZ18 Def 12]` states the search problem with a uniform syndrome $\mathbf y$; here $(\mathbf H, \mathbf y)$ comes from $s\text{-QCSD}(n, w)$, as in the search SD problem of [[Syndrome Decoding Assumption]], so that a solution exists. `[HQC25]` gives no separate search definition.
