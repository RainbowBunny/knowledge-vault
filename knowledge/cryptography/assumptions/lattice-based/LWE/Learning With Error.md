Reference:
- `[Pei16]` — C. Peikert, _A Decade of Lattice Cryptography_, Foundations and Trends in Theoretical Computer Science 10(4), 2016; ePrint 2015/939: https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf
- `[AKSY22]` — S. Agrawal, E. Kirshanova, D. Stehlé, A. Yadav, _Practical, Round-Optimal Lattice-Based Blind Signatures_, ACM CCS 2022; ePrint 2021/1565: https://eprint.iacr.org/2021/1565

## Parameters

> [!definition] Parameters
> - $n$: Number of variables.
> - $m$: Number of equations.
> - $q$: Modulus.
> - $\chi$: Error distribution, usually interval $[-B, \dots, B]$.

## Distribution

> [!definition] Learning With Error Distribution
> ### Distribution
> Sampling Experiment: $\text{LWE}(n, m, q, \chi)$
> 1. $A \xleftarrow{\$} \mathbb Z_q^{m \times n}$
> 2. $s \leftarrow \mathbb Z_q^n$
> 3. $e \leftarrow \chi^m$
> 4. Output $(A, b = As + e)$

> [!remark] Choosing LWE parameter $B$
> 1. If $B = 0$, then $As = b \pmod q$ can be solved efficiently.
> 2. If $B = (q - 1)/2$, then every $s$ can be the solution. Thus, assume $B < q / 4$.
> 3. **Arora-Ge**: If $B < \mathcal O(\sqrt{n})$, then LWE can be solved in [[Class DTIME|sub-exponential]] time for sufficiently large $m \gg n$.

> [!remark]
> For $m \gg n$, one expects there is a unique LWE solution $(s, e)$.
> Imagine we are placing balls from one space ($s$ space) into another ($e$ space).

> [!definition] Learning With Error (LWE) Problem Distribution Version
> Let $q, n, m, \alpha$ be functions of a parameter $\lambda$. For a secret $s \in \mathbb Z_q^n$, the distribution $A_{q, n, \alpha, s}$ over $\mathbb Z_q^n \times \mathbb Z_q$ is obtained by sampling $a \leftarrow \mathbb Z_q^n$ and an $e \leftarrow \mathcal D_{\mathbb Z, \alpha q}$, and returning $(a, \langle a, s \rangle + e) \in \mathbb Z_q^{n + 1}$. The Learning With Errors problem $\text{LWE}_{q, n, m, \alpha}$ is the following distinguishing game; the two branches differ in row 1 only. `[AKSY22 Def 2.11]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $s \xleftarrow{\$} \mathbb Z_q^n$<br>**Game 0**: $X \leftarrow D_1(s) = (A_{q, n, \alpha, s})^m$<br>**Game 1**: $X \leftarrow D_0(s) = U(\mathbb Z_q^{m \times (n + 1)})$ | $\xrightarrow{\ X\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_i(\mathcal A)$, the bit $b'$ in Game $i$.
> - **Measure** — for the secret $s$ of row 1, how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1 \mid s]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1 \mid s]$ are, over the random coins of $\mathcal A$ and the randomness of the samples.
>
> The source names the uniform branch $D_0(s)$ and the LWE branch $D_1(s)$; here the real branch comes first. We say that a $2^{o(\lambda)}$-time algorithm $\mathcal A$ solves $\text{LWE}_{q, n, m, \alpha}$ if it distinguishes $D_0(s)$ and $D_1(s)$ with $2^{-\omega(\lambda)}$ advantage, with $2^{-\omega(\lambda)}$ probability over the randomness of $s$.

## Problem

### Search Variant

> [!definition] Search Learning With Error Problem Advantage
> Reference Name: $\text{SLWE}(n, m, q, \chi)$
> 
> ---
> A search game: recover the secret of $m$ LWE samples. `[Pei16 Def 4.2.2]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $A \xleftarrow{\$} \mathbb Z_q^{m \times n}$<br>$s \xleftarrow{\$} \mathbb Z_q^n$<br>$e \leftarrow \chi^m$<br>$b = As + e$ | $\xrightarrow{\ (A,\, b)\ }$ | |
> | 2 | | $\xleftarrow{\ s'\ }$ | outputs a candidate secret $s' \in \mathbb Z_q^n$ |
>
> **Goal** — $\mathcal A$ wins iff:
> - $s' = s$.
>
> $$\text{Adv}_\text{LWE}^\text{search}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$

### Decision Variant

> [!definition] Decision Learning With Error Problem Advantage
> Reference Name: $\text{DLWE}(n, m, q, \chi)$
> 
> ---
> A distinguishing game: LWE samples against uniform ones; the two branches differ in row 1 only. `[Pei16 Def 4.2.3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | **Game 0**: $(A, b) \leftarrow \text{LWE}(n, m, q, \chi)$<br>**Game 1**: $(A, b) \xleftarrow{\$} \mathbb Z_q^{m \times n} \times \mathbb Z_q^m$ | $\xrightarrow{\ (A,\, b)\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_i(\mathcal A)$, the bit $b'$ in Game $i$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> $$\text{Adv}^\text{decide}_\text{LWE}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$

> [!proposition]
> SLWE and DLWE are equivalent.

## Definition

> [!remark]
> Regeus worst case to average-case reduction (2005)
> Definition: Let $L \subseteq \mathbb R^n$ be a lattice, and let $1 \leq i \leq n$. The $i^{th}$ successive minimum of $L$ is the smallest real number $\lambda_i(L)$ such that $L$ has $i$ linearly independent vectors, each of length $\leq \lambda_i(L)$.
> Note: $\lambda_1(L) \leq \lambda_2(L) \leq \cdots \leq \lambda_n(L)$.
> If LWE can be efficiently solved on average then $\text{SIVP}_\gamma$ can be efficiently solved in the worst case with a quantum algorithm.
> Corollary: If we believe that $\text{SIVP}_\gamma$ is hard in the worst case, then we must believe that LWE is also hard in the average case.
> Problem This is a highly asymptotic statement.

## LWE Lattice

> [!theorem]
> $L_A: \{y \in \mathbb Z^m: L y = Az \pmod q \text{ for some } z \in \mathbb Z^n\} \subseteq \mathbb Z^m$ is a full rank integer lattice of volume $q^{m - n}$.

## Bounded Distance Decoding Problem

> [!definition] Bounded Distance Decoding Problem $\text{BDD}_{\alpha}$
> Given $L = L(D) \subseteq \mathbb R^m$ and be $\mathbb R^m$ with the guarantee that is a unique $y \in L$ within distance $\alpha$ of $b$.

Assumption: $\alpha < \lambda_1(L) / \sqrt{2}$
