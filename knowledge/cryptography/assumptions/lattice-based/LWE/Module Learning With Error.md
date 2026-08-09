Reference: https://eprint.iacr.org/2022/1690.pdf

## Parameters

> [!definition] Parameters
> - $d$: Degree of polynomial, NTT friendly.
> - $k$: Module rank.
> - $m$: Number of equations.
> - $q$: Modulus.
> - $\chi_s$: Secret distribution.
> - $\chi_e$: Error distribution.
> - $R = \mathbb Z[X]/(X^d + 1), R_q = R / qR$: Polynomials ring.

## Distribution

> [!definition] Module Learning With Error Distribution
> ### Distribution
> Sampling Experiment: $\text{MLWE}(d, k, m, q, \chi_s, \chi_e)$
> 1. $A \xleftarrow{\$} R_q^{m \times k}$
> 2. $s \leftarrow \chi_s^k$
> 3. $e \leftarrow \chi_e^m$
> 4. $b = As + e \bmod q$
> 5. Output $(A, b)$

## Problem

### Search Variant

> [!definition] Search Module Learning With Error Problem Advantage
> Reference Name: $\text{SMLWE}(d, k, m, q, \chi_s, \chi_e)$
> 
> ---
> For any adversary $\mathcal A = (\mathcal A_\text{search})$, we define the following advantage:
> $$\text{Adv}_\text{MLWE}^\text{search}(\mathcal A) = 
> \Pr\!\left[ 
> \begin{array}{l}
> s \in \chi_s^k \\
> (b - As \bmod q) \in \chi_e^m
> \end{array} 
> \;\middle |\; 
> \begin{array}{l}
> (A, b) \leftarrow \text{MLWE}(d, k, m, q, \chi_s, \chi_e) \\
> s \leftarrow \mathcal A_\text{search}(A, b)
> \end{array} \right] 
> $$

> [!remark]
> 1. MLWE generalizes LWE (set $d = 1$, get LWE)
> 2. Also, MLWE is a special "structured" version of LWE.
> 3. No one knows any method to solve MLWE that is faster than the best algorithm known for solving LWE.


### Decision Module Learning With Error

> [!definition] Decision Learning With Error Problem Advantage
> Reference Name: $\text{DMLWE}(d, k, m, q, \chi_s, \chi_e)$
> 
> ---
> For any adversary $\mathcal A = (\mathcal A_\text{decide})$, we define the following advantage:
> $$\text{Adv}^\text{decide}_\text{MLWE}(\mathcal A) = 
> \left|\; \Pr\!\left[
> \begin{array}{l}
> b' = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (A, b) \leftarrow \text{MLWE}(d, k, m, q, \chi_s, \chi_e) \\
> b' \leftarrow \mathcal A_\text{decide}(A, b)
> \end{array} \right] 
> \;- 
> \Pr\!\left[
> \begin{array}{l}
> b' = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (A, b) \xleftarrow{\$} R_q^{m \times k} \times R_q^{m} \\
> b' \leftarrow \mathcal A_\text{decide}(A, b)
> \end{array} \right] 
> \right|.
> $$

## Assumption

> [!conjecture] MLWE Assumption
> For any adversary $\mathcal A$, the following advantage is negligible:
> $$\text{Adv}_{m, k, \eta}(\mathcal A)^{\text{mlwe}} = \left|\; 
> \Pr\!\left[ b' = 1 \;\middle | \; 
> \begin{array}{l} 
> A \leftarrow R_q^{m \times k}; (s, e) \leftarrow \chi^k \times \chi^m; \\
> b = As + e; b' \leftarrow \mathcal A(A, b)
> \end{array} \right] 
> \;-\; 
> \Pr\!\left[ b' = 1 \;\middle|\; 
> \begin{array}{l} 
> A \leftarrow R_q^{m \times k}; b \leftarrow R_q^m; b' \leftarrow \mathcal A(A, b)
> \end{array} \right] \;
> \right|.$$
> where $R_q$ denotes the ring $\mathbb Z_q[X] / (X^n + 1)$ and $\chi$ is a bounded small space.

