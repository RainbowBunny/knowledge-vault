## Parameters

> [!definition] Parameters
> - $n$: Length of the code.
> - $k$: Dimension of the subspace.
> - $w$: Weight of the codeword.
> - $q$: Prime power.
> - $\mathbb F$: Field
> - $\omega$: Rank metric.

## Distribution

> [!definition] Rank Syndrome Decoding Distribution
> ### Distribution
> Sampling Experiment: $\text{RSD}(n, k, w)$
> 1. $H \xleftarrow{\$} \mathbb F_{q^m}^{(n - k) \times n}$
> 2. $x \xleftarrow{\$} \mathbb F_{q^m}$ with $\omega(x) = w$
> 3. Output $(H, Hx^\top)$

## Problem

### Search Variant

> [!definition] Search Rank Syndrome Decoding Problem Advantage
> Reference Name: $\text{SRSD}(n, k, w)$
> 
> ---
> For any adversary $\mathcal A_\text{search}$, we define the following advantage:
> $$\text{Adv}^\text{search}_\text{RSD}(\mathcal A_\text{search}) = \Pr\!\left[ 
> \begin{array}{l}
> Hx^T = s^T \\
> \omega(x) = w
> \end{array} 
> \;\middle |\; 
> \begin{array}{l}
> (H, y^T) \xleftarrow{\$} \text{RSD}(n, k, w) \\
> x \leftarrow \mathcal A_\text{search}(H, y^T)
> \end{array} \right] 
> $$

### Decision Variant

> [!definition] Decision Rank Syndrome Decoding Problem Advantage
> Reference Name: $\text{DRSD}(n, k, w)$
> 
> ---
> For any adversary $\mathcal A_\text{decide}$, we define the following advantage:
> $$\text{Adv}^\text{decide}_\text{RSD}(\mathcal A_\text{decide}) = 
> \left|\; \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (H, y^T) \xleftarrow{\$} \text{RSD}(n, k, w) \\
> b \leftarrow \mathcal A_\text{decide}(H, y^T)
> \end{array} \right] 
> \;- 
> \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (H, y^T) \xleftarrow{\$} \mathbb F_{q^m}^{(n - k) \times n} \times \mathbb F_{q^m}^{(n - k)} \\
> b \leftarrow \mathcal A_\text{decide}(H, y^T)
> \end{array} \right] 
> \right|.
> $$
