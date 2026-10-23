Reference:
- `[Pei16]` — C. Peikert, _A Decade of Lattice Cryptography_, Foundations and Trends in Theoretical Computer Science 10(4), 2016; ePrint 2015/939: https://eprint.iacr.org/2015/939 (§4.1.1).
- `[Lyu12]` — V. Lyubashevsky, _Lattice Signatures Without Trapdoors_, EUROCRYPT 2012: https://www.iacr.org/archive/eurocrypt2012/72370731/72370731.pdf (§2, Definitions 2.1–2.4, Theorem 2.5, Lemmas 2.6–2.7); full version ePrint 2011/537: https://eprint.iacr.org/2011/537
- `[AKSY22]` — S. Agrawal, E. Kirshanova, D. Stehlé, A. Yadav, _Practical, Round-Optimal Lattice-Based Blind Signatures_, ACM CCS 2022; ePrint 2021/1565: https://eprint.iacr.org/2021/1565 (Definitions 2.12, 2.13, 5.1).
- `[carried]` — kept from the previous version of this note; its source was not identified in this pass.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Short Integer Solutions Problem

> [!definition] Shortest Integer Solutions (SIS) problem
> `[carried]` Given $A \in \mathbb Z_q^{n \times m}$, find $z \in \mathbb Z^m$ such that:
> - $Az = 0 \pmod q$;
> - $z \neq 0$;
> - $z \in [-B, B]^m$ (and $B \ll q/2$).
>
> Denote an instance of this problem by $A$ for $\text{SIS}(n, m, q, B)$. With $A$ uniform, this is the search game of [[Short Integer Solution#Search Variant|SIS]] with the $\ell_\infty$ norm and $\beta = B$.

> [!definition] Parameters
> - [[Short Integer Solution]]: Import $(n, m, q, \beta)$.
> - $\lambda$: the security parameter; $q, n, m, \beta$ are functions of $\lambda$.
> - $\mathcal A$: an [[Adversary]], one stateful interactive machine ([[Security Game]]).

> [!definition] $\ell_2$-SIS Problem
> A search game: an instance of $\text{SIS}_{q, n, m, \beta}$ is a uniform matrix, a solution is a short nonzero vector in its kernel. `[AKSY22 Def 2.12]`, `[Lyu12 Def 2.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $A \xleftarrow{\$} \mathbb Z_q^{n \times m}$ | $\xrightarrow{\ A\ }$ | |
> | 2 | | $\xleftarrow{\ v\ }$ | outputs a candidate $v \in \mathbb Z^m$ |
> | 3 | checks $v \neq 0$<br>checks $\lVert v \rVert \leq \beta$<br>checks $A \cdot v = 0 \bmod q$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $v \neq 0$;
> - $\lVert v \rVert \leq \beta$;
> - $A \cdot v = 0 \bmod q$.
>
> $$\text{Adv}^{\ell_2\text{-SIS}}_{q, n, m, \beta}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
>
> - **$\ell_2$-SIS assumption** — $\text{Adv}^{\ell_2\text{-SIS}}_{q, n, m, \beta}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$; the same game as [[Short Integer Solution#Search Variant]] `[Pei16 Def 4.1.1]`.

> [!proposition] Existence of an SIS solution
> For an instance $\text{SIS}(n, m, q, B, A)$:
> 1. Consider $n \geq m$, then $Az = 0$ has at most one unique solution thus only consider $n < m$.
> 2. If $(B + 1)^m > q^n$ then by pigeonhole principle there must exist $z_1, z_2 \in [-B/2, B/2]^m$ such that $z_1 \neq z_2$ and $Az_1 \equiv Az_2 \pmod q$, thus $z = z_1 - z_2$ is a solution to the problem. Thus, we assume $m > (n \log q) / \log(B + 1)$
> 3. The SIS solution is not unique.

### Distribution Variant

> [!definition] Parameters
> - [[Short Integer Solution]]: Import $(n, m, q)$.
> - $d$: the coefficient bound of the secret $s \in \{-d, \dots, 0, \dots, d\}^m$.
> - $\mathcal A$: an [[Adversary]], one stateful interactive machine ([[Security Game]]).

> [!definition] SIS Distribution
> ### Distribution
> Sampling experiment: $\text{SIS}_{q, n, m, d}$ `[Lyu12 Def 2.2]`
> 1. $A \xleftarrow{\$} \mathbb Z_q^{n \times m}$
> 2. $s \xleftarrow{\$} \{-d, \dots, 0, \dots, d\}^m$
> 3. Output $(A, t = As)$

### Search Variant

> [!definition] SIS Search Problem
> A search game: given an SIS sample, recover a secret of the right range. `[Lyu12 Def 2.3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(A, t) \leftarrow \text{SIS}_{q, n, m, d}$ | $\xrightarrow{\ (A,\, t)\ }$ | |
> | 2 | | $\xleftarrow{\ s'\ }$ | outputs a candidate $s' \in \mathbb Z^m$ |
> | 3 | checks $s' \in \{-d, \dots, 0, \dots, d\}^m$<br>checks $As' = t$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $s' \in \{-d, \dots, 0, \dots, d\}^m$;
> - $As' = t$.
>
> $$\text{Adv}^{\text{search}}_{\text{SIS}_{q, n, m, d}}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
>
> - **Search SIS assumption** — $\text{Adv}^{\text{search}}_{\text{SIS}_{q, n, m, d}}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$.

### Decision Variant

> [!definition] SIS Decision Problem
> A distinguishing game: an SIS sample against a uniform pair; the two branches differ in row 1 only. `[Lyu12 Def 2.4]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | **Game 0**: $(A, t) \leftarrow \text{SIS}_{q, n, m, d}$<br>**Game 1**: $(A, t) \xleftarrow{\$} \mathbb Z_q^{n \times m} \times \mathbb Z_q^n$ | $\xrightarrow{\ (A,\, t)\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> $$\text{Adv}^{\text{decide}}_{\text{SIS}_{q, n, m, d}}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
>
> - **Decision SIS assumption** — $\text{Adv}^{\text{decide}}_{\text{SIS}_{q, n, m, d}}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$. `[Lyu12 Def 2.4]` phrases the problem as "decide, with non-negligible advantage" which distribution $(A, t)$ came from.

### Relation between Variants

> [!theorem]
> If $d$ is polynomial in $n$, then there is a polynomial-time reduction from the $\text{SIS}_{q, n, m, d}$ search problem to the $\text{SIS}_{q, n, m, d}$ decision problem. `[Lyu12 Thm 2.5]`, which attributes it to Impagliazzo and Naor, generalized by Micciancio and Mol.

> [!lemma]
> For any non-negative integer $\alpha$ such that $\gcd(2 \alpha + 1, q) = 1$, there is a polynomial-time reduction from the $\text{SIS}_{q, n, m, d}$ decision problem to the $\text{SIS}_{q, n, m, (2 \alpha + 1)d + \alpha}$ decision problem. `[Lyu12 Lemma 2.6]`

> [!lemma]
> If $m = 2n$ and $4d \beta \sqrt{m} \leq q$, then there is a polynomial-time reduction from solving the $\text{SIS}_{q, n, m, d}$ decision problem to the $\ell_2 \text{-SIS}_{q, n, m, \beta}$ problem. `[Lyu12 Lemma 2.7]`, called folklore there.
>
> `⚠️ CLAUDE – verify:` the text of the EUROCRYPT version, as extracted, reads $4 d \beta \leq q$ with no $\sqrt m$; the full version could not be opened. The factor $\sqrt m$ is what the usual argument needs: an $\ell_2$-SIS solution $v$ with $\lVert v \rVert \leq \beta$ gives $\lvert \langle v, s \rangle \rvert \leq \beta \cdot d \sqrt m$. Check the PDF.

## Inhomogeneous Short Integer Solutions Problem

> [!definition] Inhomogeneous Short Integer Solutions (ISIS) Problem
> `[carried]` Given $A \in \mathbb Z_q^{n \times m}$ and $b \in \mathbb Z_q^n$, find $z \in \mathbb Z^m$ such that:
> - $Az \equiv b \pmod q$;
> - $z \in [-B, B]^m$.
>
> Denote an instance of this problem by $(A, b)$ for $\text{ISIS}(n, m, q, B)$.

> [!definition] Parameters
> - [[Short Integer Solution]]: Import $(n, m, q, \beta)$.
> - $\lambda$: the security parameter; $q, n, m, \beta$ are functions of $\lambda$.
> - $\mathcal A$: an [[Adversary]], one stateful interactive machine ([[Security Game]]).

> [!definition] Inhomogeneous Short Integer Solution (ISIS) Problem
> A search game: a short preimage of a uniform syndrome. `[AKSY22 Def 2.13]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $A \xleftarrow{\$} \mathbb Z_q^{n \times m}$<br>$t \xleftarrow{\$} \mathbb Z_q^n$ | $\xrightarrow{\ (A,\, t)\ }$ | |
> | 2 | | $\xleftarrow{\ v\ }$ | outputs a candidate $v \in \mathbb Z^m$ |
> | 3 | checks $\lVert v \rVert \leq \beta$<br>checks $A \cdot v = t \bmod q$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $\lVert v \rVert \leq \beta$;
> - $A \cdot v = t \bmod q$.
>
> $$\text{Adv}^{\text{ISIS}}_{q, n, m, \beta}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
>
> - **ISIS assumption** — $\text{Adv}^{\text{ISIS}}_{q, n, m, \beta}(\mathcal A)$ is negligible for every probabilistic polynomial-time $\mathcal A$.
>
> Unlike SIS, $v$ need not be nonzero: $v = 0$ wins only when $t = 0$.

> [!remark]
> For an instance $\text{ISIS}(n, m, q, B, A, b)$:
> 1. Also consider $n < m$.
> 2. If $(2B + 1)^m \gg q^n$, then an ISIS solution is likely to exist (prove?).

> [!proposition]
> $\text{ISIS}$ and $\text{SIS}$ are equivalent. `[Pei16 §4.1.1]` says "essentially equivalent" for typical parameters.

### One-More-ISIS Assumption

> [!definition] Parameters
> - [[Short Integer Solution]]: Import $(n, m, q, \beta)$.
> - $\lambda$: the security parameter; $q, n, m, \sigma, \beta$ are functions of $\lambda$.
> - $\sigma$: the width of the discrete Gaussian $D_{\mathbb Z^m, \sigma}$ from which preimages are sampled.
> - $S$: the set of syndromes the challenger has sent. $\ell$: the number of preimage queries.
> - $\mathbb A$: adversaries running in time $2^{o(\lambda)}$ with at most $\lambda^{O(1)}$ preimage queries and $2^{o(\lambda)}$ syndrome queries.

> [!definition] One-More-ISIS Assumption
> ### Scope
> The matrix of $\text{one-more-ISIS}_{q, n, m, \sigma, \beta}$ and the [[Adversary]] class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — two oracles, in any order: syndrome queries (a fresh uniform target) and preimage queries (a short Gaussian preimage of any target $\mathcal A$ chooses).
> - **Promise** — none.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — fully adaptive: each query may depend on all earlier answers.
>
> ---
> ### Experiment
> A search game: after $\ell$ preimage queries, produce $\ell + 1$ preimages of syndromes from $S$. `[AKSY22 Def 5.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $C \xleftarrow{\$} \mathbb Z_q^{n \times m}$<br>$S = \emptyset$<br>$\ell = 0$ | $\xrightarrow{\ C\ }$ | |
> | 2 | | $\xleftarrow{\ \text{query}\ }$ | **Syndrome queries** (repeated, adaptive, interleaved with row 3): requests a challenge vector |
> | | $t \xleftarrow{\$} \mathbb Z_q^n$<br>$S \leftarrow S \cup \{t\}$ | $\xrightarrow{\ t\ }$ | |
> | 3 | | $\xleftarrow{\ t'\ }$ | **Preimage queries** (repeated, adaptive, interleaved with row 2): sends $t' \in \mathbb Z_q^n$ |
> | | $y' \leftarrow D_{\mathbb Z^m, \sigma}$ with $Cy' = t'$<br>$\ell \leftarrow \ell + 1$ | $\xrightarrow{\ y'\ }$ | |
> | 4 | | $\xleftarrow{\ \{(y_j,\, t_j)\}_{j \in [\ell + 1]}\ }$ | outputs $\ell + 1$ pairs $\{(y_j, t_j)\}_{j \in [\ell + 1]}$ |
> | 5 | checks $Cy_j = t_j$ for all $j \in [\ell + 1]$<br>checks $\lVert y_j \rVert \leq \beta$ for all $j \in [\ell + 1]$<br>checks $t_j \in S$ for all $j \in [\ell + 1]$ | | |
>
> **Goal** — $\mathcal A$ wins iff, for all $j \in [\ell + 1]$, all of:
> - $Cy_j = t_j$;
> - $\lVert y_j \rVert \leq \beta$;
> - $t_j \in S$.
>
> ---
> ### Property
> $$\text{Adv}^{\text{omisis}}_{q, n, m, \sigma, \beta}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
> - The $\text{one-more-ISIS}_{q, n, m, \sigma, \beta}$ assumption states that for every adversary $\mathcal A$ running in time $2^{o(\lambda)}$ making at most $\lambda^{O(1)}$ preimage queries and $2^{o(\lambda)}$ syndrome queries, the probability (over the randomness of $\mathcal A$ and $\mathcal C$) that $\mathcal A$ wins is $2^{-\Omega(\lambda)}$.

> [!remark] Notation in the literature
> - `[AKSY22 Def 5.1]` writes the experiment as a numbered list of steps; the table above is the same experiment.
> - `⚠️ CLAUDE – verify:` the source writes the output as a set $\{(y_j, t_j)\}$, so the $\ell + 1$ pairs are distinct; otherwise one preimage query on some $t \in S$ followed by repeating the answer would win. The end of the assumption sentence (time and query bounds, success $2^{-\Omega(\lambda)}$) is carried from the previous version: the readable copy of the source was cut off there.
 
## Normal Form Inhomogeneous Short Integer Solutions Problem

> [!definition] Normal Form Inhomogeneous Short Integer Solutions (nf-ISIS) Problem 
> `[carried]` Given $A \in \mathbb Z_q^{n \times m}$ and $b \in \mathbb Z_q^n$, find $z \in \mathbb Z^{m + n}$ such that:
> - $[A | I_n] z = b \pmod q$;
> - $z \in [-B, B]^{m + n}$.
>
> Denote an instance of this problem by $(A, b)$ for $\text{nf-ISIS}(n, m, q, B)$. Compare the normal form of SIS in [[Normal Form Short Integer Solution]], where `[Pei16]` puts the identity block first.

> [!proposition]
> $\text{nf-ISIS}(n, m, q, B)$ and $\text{ISIS}(n, m + n, q, B)$ are equivalent.

## Application

> [!example] Collision-resistant Hash Function
> Let $A \in \mathbb Z_q^{n \times m}$, where $m > n \log q$. Define hash function $H_A : \{0, 1\}^m \rightarrow \mathbb Z^n_q$ by $H_A(z) \equiv Az \pmod q$. We have the following properties:
> 1. **Compression**: Since $m > n \log q$, we have $2^m > q^n$.
> 2. **Collision resistance**: Assume that there exist an algorithm can effectively find a $z_1, z_2 \in \{0, 1\}^m$ with $z_1 \neq z_2$ and $H_A(z_1) = H_A(z_2)$. Then, we can verify that $A(z_1 - z_2) \equiv 0 \pmod q$ so we find a solution to $\text{SIS}(n, m, q, 1, A)$.
>
> `[Pei16 §4.1.1]` makes the same observation for $f_A : \{0, 1\}^m \to \mathbb Z_q^n$.
