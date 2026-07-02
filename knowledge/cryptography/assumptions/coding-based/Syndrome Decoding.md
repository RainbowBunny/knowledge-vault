## Distribution

> [!definition] Syndrome Decoding Distribution
> ### Parameters
> - $n$: Length of the code.
> - $k$: Dimension of the subspace.
> - $w$: Weight of the codeword.
> 
> ---
> ### Distribution
> Sampling experiment: $\text{SD}(n, k, w)$
> 1. $H \xleftarrow{\$} \mathbb F^{(n - k) \times n}$
> 2. $x \xleftarrow{\$} \mathbb F^n$ with $\omega(x) = w$
> 3. Output $(H, \sigma(x) = Hx^{\perp})$

## Problem

### Search Variant

> [!definition] Search SD Problem
> ### Parameters
> - $n$: Length of the code.
> - $k$: Dimension of the subspace.
> - $w$: Weight of the codeword.
> - $\mathbb F$: Field
> - $\omega$: Norm over $\mathcal R$
> 
> ---
> ### Input
> - $(H, y^{\top}) \xleftarrow{\$} \text{SD}(n, k, w)$
> ---
> 
> ### Output
> - Find $x \in \mathbb F^n$ such that:
> 	- $Hx^\top = y^\top$
> 	- $\omega(x) = w$

### Decision Variant

> [!definition] Decision SD Problem
> ### Parameters
> - $n$: Length of the code.
> - $k$: Dimension of the subspace.
> - $w$: Weight of the codeword.
> - $\mathbb F$: Field
> - $\omega$: Norm over $\mathcal R$
> ---
> ### Input
> - $(H, y^\top) \xleftarrow{\$} \mathbb F^{(n - k) \times n} \times \mathbb F^{(n - k)}$
> ---
> ### Output
> - Decide whether $(H, y^\top)\xleftarrow{\$} \text{SD}(n, k, w)$
	
> [!definition] Decision SD Problem  
The **Decision SD problem** DSD(n, k, w) is to distinguish the distributions DSD(n,k,w)\mathcal D_{\text{SD}}(n,k,w) DSD​(n,k,w) and Dunif(n,k)\mathcal D_{\text{unif}}(n,k) Dunif​(n,k). For an algorithm A\mathcal A A, define  
> $$\text{Adv}^{\text{dsd}}_{n,k,w}(\mathcal A) = \Big|\Pr_{z \leftarrow \mathcal D_{\text{SD}}}[\mathcal A(z) = 1] - \Pr_{z \leftarrow \mathcal D_{\text{unif}}}[\mathcal A(z) = 1]\Big|$$
