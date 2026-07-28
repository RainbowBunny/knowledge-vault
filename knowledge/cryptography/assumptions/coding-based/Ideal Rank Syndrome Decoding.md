## Parameters

> [!definition] Parameters
> - $n$: Length of the code.
> - $w$: Weight of the codeword.
> - $s$: Index of the code (how coarse is the ring structure)
> - $q$: Prime power.
> - $\mathbb F$: Field
> - $\omega$: Rank metric.

## Distribution

> [!definition] Ideal Rank Syndrome Decoding Distribution
> ### Distribution
> Sampling Experiment: $s\text{-IRSD}(n, w)$
> 1. $H \xleftarrow{\$} \mathbb F_{q^m}^{(sn - n) \times sn}$: Parity check matrix $H$ of an $s$-ideal code $\mathcal C$.
> 2. $x = (x_1, \dots, x_s) \xleftarrow{\$} \mathbb F_{q^m}^{sn}$ with $\omega(x) = w$
> 3. Output $(H, Hx^\top)$

## Problem

### Search Variant

> [!definition] Search Ideal Rank Syndrome Decoding Problem Advantage
> Reference Name: $s\text{-SIRSD}(n, k, w)$
> 
> ---
> For any adversary $\mathcal A_\text{search}$, we define the following advantage:
> $$\text{Adv}^\text{search}_\text{IRSD}(\mathcal A_\text{search}) = \Pr\!\left[ 
> \begin{array}{l}
> Hx^T = y^T \\
> \omega(x) = w
> \end{array} 
> \;\middle |\; 
> \begin{array}{l}
> (H, y^T) \xleftarrow{\$} s\text{-IRSD}(n, k, w) \\
> x \leftarrow \mathcal A_\text{search}(H, y^T)
> \end{array} \right] 
> $$

### Decision Variant

> [!definition] Parity-Restricted Uniform Distribution
> For a bit $b$, let $\mathbb F_{q^m, b}^{\,sn - n} = \{\, y \in \mathbb F_{q^m}^{\,sn-n} : \textstyle\sum_i y_i = b \,\}$ denote the vectors of parity $b$, and let $\mathcal U_b$ sample $H$ as in $s\text{-IRSD}(n, w)$ and $y \xleftarrow{\$} \mathbb F_{q^m, b}^{\,sn-n}$, outputting $(H, y^\top)$.
> **Note:** $H$ is sampled identically in both worlds — only $y$ differs. The planted syndrome's parity is *publicly computable* from $(H, w)$ (over $\mathbb F_2$, each block of $y = xH^\top$ has parity determined by $w$ and the row-sums of $H$'s circulant blocks), and $b$ is set to exactly that value.

> [!definition] Decision Ideal Rank Syndrome Decoding Problem Advantage
> Reference Name: $\text{DIRSD}(n, k, w)$
> 
> ---
> For any adversary $\mathcal A_\text{decide}$, we define the following advantage:
> $$\text{Adv}^\text{decide}_\text{IRSD}(\mathcal A_\text{decide}) = 
> \left|\; \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (H, y^T) \xleftarrow{\$} s\text{-IRSD}(n, k, w) \\
> b \leftarrow \mathcal A_\text{decide}(H, y^T)
> \end{array} \right] 
> \;- 
> \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (H, y^T) \xleftarrow{\$} \mathcal U_b \\
> b \leftarrow \mathcal A_\text{decide}(H, y^T)
> \end{array} \right] 
> \right|.
> $$
