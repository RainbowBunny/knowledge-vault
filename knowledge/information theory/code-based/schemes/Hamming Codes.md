## Syntax

> [!scheme] Hamming Codes
> Reference Name: $\mathcal H_r, \mathcal H_{q, r}$
> 
> ---
> ### Parameters
> - $n = 2^r - 1$, with $r \geq 2$ is the code length.
> 
> ---
> ### Construction
> - The parity check matrix $H_r$ on the binary code $[n = 2^r - 1, k = n - r]$ has each columns are numbers $1, 2, \dots, 2^r - 1$ written as binary numerals. Any rearrangement of columns of $H_r$ gives an equivalent code, and hence any one of these equivalent codes will be called the binary Hamming code of length $n = 2^r - 1$.
> - The code can be extended into $q$-nary code, the different is that now for numbers from $1, 2, \dots, q^r - 1$, there are equivalent number different by scalar in $\mathbb F_q$. Thus, now we have length $(q^r - 1) / (q - 1)$.

## Property

> [!theorem]
> Any $[2^r - 1, 2^r - 1 - r, 3]$ binary code is equivalent to the binary Hamming Code $\mathcal H_r$.

> [!theorem]
> Any $[(q^r - 1) / (q - 1), (q^r - 1) / (q - 1) - r, 3]$ code over $\mathbb F_q$ is monomially equivalent to the Hamming code $\mathcal H_{q, r}$.

> [!theorem]
> The nonzero codewords of the $[(q^r - 1) / (q - 1), r]$ simplex code over $\mathbb F_q$ all have weights $q^{r - 1}$.



