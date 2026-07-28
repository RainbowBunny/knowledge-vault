## Parameters

> [!definition] Parameters
> 
> - $n$: Number of variables.
> - $m$: Number of equations.
> - $q$: Modulus.
> - $\chi$: Solution distribution, usually interval $[-B, \dots, B]$.

## Distribution

> [!definition] Short Integer Solution Distribution
> ### Distribution
> Sampling Experiment: $\text{SIS}(n, m, q, \chi)$
> 1. $A \xleftarrow{\$} \mathbb Z_q^{m \times n}$
> 2. $s \leftarrow \mathbb \chi^n$
> 3. $e \leftarrow \chi^m$
> 4. Output $(A, b = As + e)$
