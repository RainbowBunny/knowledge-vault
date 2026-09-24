## Definition

> [!definition] Parameters
> - [[Syndrome Decoding Problem]]: Import $(n, k, w, \mathbb{F}_2, \mathsf{wt}_\mathsf{H})$.

### Distribution

> [!definition] Syndrome Decoding Distribution
> ### Distribution
> Sampling experiment: $\text{SD}(n, k, w)$
> 1. $\mathbf{H} \xleftarrow{\$} \mathbb{F}_2^{(n - k) \times n}$ ([[Linear Code#Generator Matrix and Parity-Check Matrix|Parity-Check Matrix]]).
> 2. $\mathbf{x} \xleftarrow{\$} \mathcal{S}^n_w(\mathbb{F}_2)$ ([[Hamming Sphere]]).
> 3. Output $(\mathbf{H}, \sigma(\mathbf{x}) = \mathbf{H}\mathbf{x}^{T})$.

## Problem

### Search Variant

> [!definition] Search Syndrome Decoding Problem Advantage
> Reference Name: $\text{SSD}(n, k, w)$
> 
> ---
> For any adversary $\mathcal A_\text{search}$, we define the following advantage:
> $$\text{Adv}^\text{search}_\text{SD}(\mathcal A_\text{search}) = \Pr\!\left[ 
> \begin{array}{l}
> Hx^T = y^T \\
> \omega(x) = w
> \end{array} 
> \;\middle |\; 
> \begin{array}{l}
> (H, y^T) \xleftarrow{\$} \text{SD}(n, k, w) \\
> x \leftarrow \mathcal A_\text{search}(H, y^T)
> \end{array} \right] 
> $$

### Decision Variant

> [!definition] Decision Syndrome Decoding Problem Advantage
> Reference Name: $\text{DSD}(n, k, w)$
> 
> ---
> For any adversary $\mathcal A_\text{decide}$, we define the following advantage:
> $$\text{Adv}^\text{decide}_\text{SD}(\mathcal A_\text{decide}) = 
> \left|\; \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (H, y^T) \xleftarrow{\$} \text{SD}(n, k, w) \\
> b \leftarrow \mathcal A_\text{decide}(H, y^T)
> \end{array} \right] 
> \;- 
> \Pr\!\left[
> \begin{array}{l}
> b = 1
> \end{array}
> \;\middle |\; 
> \begin{array}{l}
> (H, y^T) \xleftarrow{\$} \mathbb F^{(n - k) \times n} \times \mathbb F^{(n - k)} \\
> b \leftarrow \mathcal A_\text{decide}(H, y^T)
> \end{array} \right] 
> \right|.
> $$


## Claim

> [!remark]
> With $\omega$ is the Hamming distance, the syndrome decoding problem has been proven in NP-complete.
> Link: http://authors.library.caltech.edu/5607/1/BERieeetit78.pdf
> And we can see this problem as LPN with a fixed number of samples.

> [!remark]
> Decision variant has been shown to be polynomial equivalent to the search variant.
> Link: https://link.springer.com/article/10.1007/s00145-009-9039-0


