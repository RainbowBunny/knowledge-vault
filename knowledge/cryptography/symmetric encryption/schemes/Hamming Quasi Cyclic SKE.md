## Syntax

> [!scheme] HQC SKE
> Reference Name: $\text{HQC.SKE}$
> ### Parameters
> 
> ---
> ### Building Block
> - $\mathcal C$: Code
> 
> ---
> ### Algorithms
> ---
> - $k \leftarrow \text{KeyGen}()$:
> 	1. Samples the generator matrix $G \in \mathbb F_2^{k \times n}$ of $\mathcal C$
> 	2. Returns $(x, y) \leftarrow S_w^n(\mathbb F_2)$
> - $c \leftarrow \text{Enc}(k, m)$:
> 	1. Generates $h \xleftarrow{\$} \mathbb F_2^n, e \xleftarrow{\$} S_{w_e}^n, r = (r_1, r_2) \xleftarrow{\$} S_{w_r}^n(\mathbb F_2) \times  S_{w_r}^n(\mathbb F_2)$
> 	2. Calculate $s \leftarrow x + h \cdot y$
> 	3. $u = r_1 + h \cdot r_2$
> 	4. $v = mG + s \cdot r_2 + e$
> 	5. Return $(u, v)$
> - $m \leftarrow \text{Dec}(k, c)$:
> 	1. Return $m' \leftarrow \mathcal C.\text{Decode}(v - u \cdot y)$

> [!scheme] HQC SKE 2
> Reference Name: $\text{HQC.SKE2}$
> ### Parameters
> 
> ---
> ### Building Block
> 
> ---
> ### Algorithms
> ---
> - $k \leftarrow \text{KeyGen}()$:
> 	1. Samples $h \xleftarrow{\$} \mathbb F_2^n$,
> 	2. Samples the generator matrix $G \in \mathbb F_2^{k \times n}$ of $\mathcal C$,
> 	3. $(x, y) \xleftarrow{\$} S_w^n(\mathbb F_2) \times S_w^n(\mathbb F_2)$, $\cdot$ is polynomial multiplication mod $X^n - 1$
> 	4. $(h, s = x + h \cdot y) \in \mathbb F_2^n \times \mathbb F_2^n$
> 	5. returns $(h, s, y)$
> - $c \leftarrow \text{Enc}(k, m)$:
> 	1. Generates $e \xleftarrow{\$} S_{w_e}^n$
> 	2. Generates $r = (r_1, r_2) \xleftarrow{\$} S_{w_r}^n(\mathbb F_2) \times  S_{w_r}^n(\mathbb F_2)$
> 	3. $u = r_1 + h \cdot r_2$
> 	4. $v = mG + s \cdot r_2 + e$
> 	5. Return $(u, v)$
> - $m \leftarrow \text{Dec}(k, c)$:
> 	1. Return $m' \leftarrow \mathcal C.\text{Decode}(v - u \cdot y)$
