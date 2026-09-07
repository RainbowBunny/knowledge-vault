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
> 3. Output $(H, Hx^T)$

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

> [!definition] 

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
