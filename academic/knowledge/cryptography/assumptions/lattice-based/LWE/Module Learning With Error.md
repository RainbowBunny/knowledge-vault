## Assumption

> [!conjecture] MLWE Assumption
> For any adversary $\mathcal A$, the following advantage is negligible:
> $$\text{Adv}_{m, k, \eta}^{\text{mlwe}} = \left|\; 
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

