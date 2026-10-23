Reference:
- `[Pei16]` — C. Peikert, _A Decade of Lattice Cryptography_, Foundations and Trends in Theoretical Computer Science 10(4), 2016; ePrint 2015/939: https://eprint.iacr.org/2015/939 (§4.1.1, "normal form", p. 19).

## Parameters

> [!definition] Parameters
> 
> - [[Short Integer Solution]]: Import $(n, m, q, \beta)$.
> - $\bar A \in \mathbb Z_q^{n \times (m - n)}$: the non-identity part of the matrix.
> - $\mathcal A$: an [[Adversary]], one stateful interactive machine ([[Security Game]]).

## Problem

### Search Variant

> [!definition] Normal-Form Search Short Integer Solution Problem Advantage
> Reference Name: $\text{nf-SIS}_{n, q, \beta, m}$
>
> ---
> A search game: SIS for a matrix whose first $n$ columns are the identity. `[Pei16 §4.1.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\bar A \xleftarrow{\$} \mathbb Z_q^{n \times (m - n)}$<br>$A = [I_n \mid \bar A]$ | $\xrightarrow{\ \bar A\ }$ | |
> | 2 | | $\xleftarrow{\ z\ }$ | outputs a candidate $z \in \mathbb Z^m$ |
> | 3 | checks $z \neq 0$<br>checks $\lVert z \rVert \leq \beta$<br>checks $Az = 0 \in \mathbb Z_q^n$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $z \neq 0$;
> - $\lVert z \rVert \leq \beta$;
> - $Az = 0 \pmod q$.
>
> $$\text{Adv}_{\text{nf-SSIS}}^\text{search}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
>
> - **Normal-form SIS assumption** — $\text{Adv}_{\text{nf-SSIS}}^\text{search}(\mathcal A)$ is negligible in $n$ for every probabilistic polynomial-time $\mathcal A$.

> [!lemma]
> Normal-form SIS is as hard as [[Short Integer Solution#Search Variant|SIS]]. `[Pei16 §4.1.1]`: write a uniform $A = [A_1 \mid A_2]$ with $A_1 \in \mathbb Z_q^{n \times n}$ invertible (without loss of generality). Then $A_1^{-1} A = [I_n \mid \bar A]$ with $\bar A = A_1^{-1} A_2$ uniform, and $A$ and $A_1^{-1} A$ have exactly the same short solutions. The identity block is left implicit, which compresses the instance by $n$ columns.

> [!remark] Notation in the literature
> `[Pei16]` puts the identity first, $[I_n \mid \bar A]$, and compares it with a systematic generator matrix of a code and with the Hermite normal form of a lattice.
