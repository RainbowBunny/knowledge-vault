## Parameters

> [!definition] Parameters
> - $n$: Length of the code.
> - $k$: Dimension of the subspace.
> - $w$: Weight of the codeword.
> - $\mathbb F$: Field
> - $\omega$: Norm over $\mathcal R$

## Distribution

> [!definition] Syndrome Decoding Distribution
> ### Distribution
> Sampling experiment: $\text{SD}(n, k, w)$
> 1. $H \xleftarrow{\$} \mathbb F^{(n - k) \times n}$
> 2. $x \xleftarrow{\$} \mathbb F^n$ with $\omega(x) = w$
> 3. Output $(H, \sigma(x) = Hx^{\perp})$

## Problem

### Search Variant

> [!definition] Search Syndrome Decoding Problem Advantage
> For any adversary $\mathcal A_\text{search}$, we define the following advantage:
> $$\text{Adv}^\text{search}_\text{SDP}(\mathcal A) = \Pr\!\left[ 
> \begin{array}{l}
> Hx^\top = y^\top \\
> \omega(x) = w
> \end{array} 
> \;\middle |\; 
> \begin{array}{l}
> (H, y^\top) \xleftarrow{\$} \text{SD}(n, k, w) \\
> x \leftarrow \mathcal A_\text{search}(H, y^\top)
> \end{array} \right] 
> $$

### Decision Variant

> [!definition] Decision Syndrome Decoding Problem Advantage
> For any adversary $\mathcal A_\text{decide}$, we define the following advantage:
> $$\text{Adv}^\text{decide}_\text{SDP}(\mathcal A_\text{decide}) = 
> \left|\; \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (H, y^\top) \xleftarrow{\$} \text{SD}(n, k, w) \\
> b \leftarrow \mathcal A_\text{decide}(H, y^\top)
> \end{array} \right] 
> \;- 
> \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (H, y^\top) \xleftarrow{\$} \mathbb F^{(n - k) \times n} \times \mathbb F^{(n - k)} \\
> b \leftarrow \mathcal A_\text{decide}(H, y^\top)
> \end{array} \right] 
> \right|.
> $$

