Reference:
- `[Pei16]` — C. Peikert, _A Decade of Lattice Cryptography_, Foundations and Trends in Theoretical Computer Science 10(4), 2016; ePrint 2015/939: https://web.eecs.umich.edu/~cpeikert/pubs/lattice-survey.pdf
- `[ACPS09]` — B. Applebaum, D. Cash, C. Peikert, A. Sahai, _Fast Cryptographic Primitives and Circular-Secure Encryption Based on Hard Learning Problems_, CRYPTO 2009: https://web.eecs.umich.edu/~cpeikert/pubs/kdm-learning.pdf

## Parameters

> [!definition] Parameters
> - $n$: Number of variables.
> - $m$: Number of equations.
> - $q$: Modulus.
> - $\chi$: Error distribution, usually interval $[-B, \dots, B]$.

## Distribution

> [!definition] Short-Secret Learning With Error
> ### Distribution
> Sampling Experiment: $\text{ss-LWE}(n, m, q, \chi)$
> 1. $A \xleftarrow{\$} \mathbb Z_q^{m \times n}$
> 2. $s \leftarrow \chi^n$
> 3. $e \leftarrow \chi^m$
> 4. Output $(A, b = As + e)$

> [!remark]
> - We should choose $B \ll q/2$.
> - We don't need $m \gg n$ for unique solutions.

## Problem

### Search Variant

> [!definition] Search Short Secret Learning With Error Problem Advantage
> Reference Name: $\text{Sss-LWE}(n, m, q, \chi)$
> 
> ---
> A search game: Search-LWE `[Pei16 Def 4.2.2]` with the secret drawn from the error distribution, the *normal form* of `[Pei16 §4.2.1]`.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $A \xleftarrow{\$} \mathbb Z_q^{m \times n}$<br>$s \leftarrow \chi^n$<br>$e \leftarrow \chi^m$<br>$b = As + e$ | $\xrightarrow{\ (A,\, b)\ }$ | |
> | 2 | | $\xleftarrow{\ s'\ }$ | outputs a candidate secret $s'$ |
>
> **Goal** — $\mathcal A$ wins iff:
> - $s' = s$.
>
> $$\text{Adv}_\text{ss-LWE}^\text{search}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$

> [!proposition]
> ss-LWE and LWE are equivalent.
> - $\text{Sss-LWE}(n, m, q, \chi) \leq \text{SLWE}(n, m, q, \chi)$ 
> - $\text{SLWE}(n, m, q, \chi) \leq \text{Sss-LWE}(n, m - n, q, \chi)$: $n$ of the $m$ samples are spent to turn the uniform secret into a $\chi^n$-distributed one `[ACPS09 Lemma 2]`, `[Pei16 §4.2.1]`.

### Decision Variant

> [!definition] Decision Short Secret Learning With Error Problem Advantage
> Reference Name: $\text{Dss-LWE}(n, m, q, \chi)$
> 
> ---
> A distinguishing game: Decision-LWE `[Pei16 Def 4.2.3]` with the secret drawn from $\chi^n$ `[Pei16 §4.2.1]`; the two branches differ in row 1 only.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | **Game 0**: $(A, b) \leftarrow \text{ss-LWE}(n, m, q, \chi)$<br>**Game 1**: $(A, b) \xleftarrow{\$} \mathbb Z_q^{m \times n} \times \mathbb Z_q^m$ | $\xrightarrow{\ (A,\, b)\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_i(\mathcal A)$, the bit $b'$ in Game $i$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> $$\text{Adv}^\text{decide}_\text{ss-LWE}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
