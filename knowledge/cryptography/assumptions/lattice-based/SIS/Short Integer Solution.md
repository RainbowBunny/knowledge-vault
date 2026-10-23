Reference:
- `[Pei16]` — C. Peikert, _A Decade of Lattice Cryptography_, Foundations and Trends in Theoretical Computer Science 10(4), 2016; ePrint 2015/939: https://eprint.iacr.org/2015/939 (§4.1.1, Definition 4.1.1).

## Parameters

> [!definition] Parameters
> 
> - $n$: Number of rows of $A$ (equations), the main hardness parameter.
> - $m$: Number of columns of $A$ (unknowns): the number of uniform vectors $a_i \in \mathbb Z_q^n$.
> - $q$: Modulus.
> - $\beta$: Norm bound on the solution, $0 < \beta < q$; $\lVert \cdot \rVert$ is the Euclidean norm unless stated otherwise.
> - $\mathcal A$: an [[Adversary]], one stateful interactive machine ([[Security Game]]).

## Problem

### Search Variant

> [!definition] Search Short Integer Solution Problem Advantage
> Reference Name: $\text{SIS}_{n, q, \beta, m}$
>
> ---
> A search game: find a short nonzero vector in the kernel of a uniform matrix. `[Pei16 Def 4.1.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $A \xleftarrow{\$} \mathbb Z_q^{n \times m}$ | $\xrightarrow{\ A\ }$ | |
> | 2 | | $\xleftarrow{\ z\ }$ | outputs a candidate $z \in \mathbb Z^m$ |
> | 3 | checks $z \neq 0$<br>checks $\lVert z \rVert \leq \beta$<br>checks $Az = 0 \in \mathbb Z_q^n$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $z \neq 0$;
> - $\lVert z \rVert \leq \beta$;
> - $Az = 0 \pmod q$.
>
> $$\text{Adv}_{\text{SSIS}}^\text{search}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
>
> - **SIS assumption** — $\text{Adv}_{\text{SSIS}}^\text{search}(\mathcal A)$ is negligible in $n$ for every probabilistic polynomial-time $\mathcal A$.

> [!remark] Why each condition is there `[Pei16 §4.1.1]`
> - Without $z \neq 0$, the vector $z = 0$ always wins; without the norm bound, Gaussian elimination finds a solution.
> - $\beta < q$, otherwise $z = (q, 0, \dots, 0)$ is always a solution.
> - A solution exists once $m \geq \bar m$ and $\beta \geq \sqrt{\bar m}$, where $\bar m$ is the smallest integer above $n \log q$: by pigeonhole, two distinct $x, x' \in \{0, 1\}^{\bar m}$ have $Ax = Ax'$, and $z = x - x'$.

> [!remark] Relation to [[Short Integer Solution Problem]]
> Both notes describe SIS with a uniform matrix; that note adds the $\ell_\infty$ form $z \in [-B, B]^m$, the inhomogeneous ISIS, the one-more-ISIS assumption and Lyubashevsky's distributional SIS.
