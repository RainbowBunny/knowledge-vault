## Parameters

> [!definition] Parameters
> - $d$: Degree of polynomial, NTT friendly.
> - $k$: Module rank.
> - $q$: Modulus.
> - $\chi_s$: Secret distribution.
> - $\chi_e$: Error distribution.
> - $m$: Number of samples.

## Distribution

> [!definition] Module Learning With Error Distribution
> ### Distribution
> Sampling Experiment: $\text{MLWE}(d, k, q, \chi_s, \chi_e, m)$

## Module Learning With Error

> [!definition] Module Learning With Error
> Module LWE (MLWE) ($k, l, q, n, \eta$) so $R_q = \mathbb Z_q [x] / (x^n + 1)$
Let $A \in_R R^{k \times l}_q, S \in_R R_q^l, e \in_R S_\eta^k$ and $t = As + e \in R^k_q$. Given $(A, t)$, determine $s$.

> [!remark]
> 1. MLWE generalizes LWE (set $n = 1$, get LWE)
> 2. Also, MLWE is a special "structured" version of LWE.
> 3. No one knows any method to solve MLWE that is faster than the best algorithm known for solving LWE.

### MLWE Assumption

> [!algorithm] MLWE Adversary
> For integers $m, k$, and a probability distribution $D: R_q \rightarrow [0, 1]$, we say that the advantage of algorithm $A$ in solving the decisional $\text{MLWE}_{m, k, D}$

### Decision Module Learning With Error

> [!definition]
> DMLWE$(k, l, q, n, \eta)$.


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

