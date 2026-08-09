## Syntax

> [!scheme] Additive-Homomorphic Encryption
> Reference Name: AHE
> ### Parameters
> 
> ---
> ### Building Block
> 
> ---
> ### Algorithms
> - $k \leftarrow \text{Gen}()$:
> 	1. Samples $f = (f_1, \dots, f_w) \xleftarrow{\$} \mathcal S_w^w(\mathbb F_{q^m})$ (Secret Support).
> 	2. Extends $f$ into a basis $b = (f_1, \dots, f_w, g_1, \dots, g_{m - w}) \in \mathcal S_m^m(\mathbb F_{q^m})$.
> 	3. Defines $g = (g_1, \dots, g_{m - w})$.
> 	4. Compute $B = \text{Mat}(b) = \begin{pmatrix}f_1 & f_2 &\cdots g_{m - w}\end{pmatrix}$ (Basis Matrix).
> 	5. Defines $D$ as the last $m - w$ columns of its transposed inverse $(B^{-1})^T$ (Dual Basis)
> 	6. Samples $s \xleftarrow{\$} F^n$ with $F = \text{supp}(f)$.
> 	7. Return $k = (f, g, D, s)$.
> - $c \leftarrow \text{Encrypt}(k, m, r)$:
> - $m \leftarrow \text{Decrypt}(k, c)$:
