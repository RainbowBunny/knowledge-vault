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
> - $(H, y^{\perp}) \in \mathbb F^{(n - k) \times n} \times \mathbb F^{(n - k)} \xleftarrow{\$} \text{SD}(n, k, w)$
> ---
> ### Output
> 

