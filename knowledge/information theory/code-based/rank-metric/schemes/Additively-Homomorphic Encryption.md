
Link: https://eprint.iacr.org/2023/1798.pdf
## Scheme

> [!scheme] Additively-Homomorphic Encryption
> Reference Name: $\text{AHE}$
> 
> ---
> ### Parameters
> - $q$: Base field cardinality.
> - $m$: Dimension of the field extension.
> - $n$: Length of the vectors.
> - $w$: Rank weight of the error ($w < m$).
> 
> ---
> ### Building Block
> - Here, the dot product of two vectors is polynomial ring multiplication in $\mathbb F_{q^m}[X] / \langle Q \rangle$ with $Q$ is a degree $n - 1$ polynomial.
> - $\text{vec}: \mathbb F_{q^m} \rightarrow \mathbb F_q^m$
> - $\text{Mat}$: Convert an array of vector into a matrix (each vector corresponds to a column).
> 
> ---
> ### Algorithms
> - $sk \leftarrow \text{KeyGen}()$
> 	1. Generates secret noise room $f = (f_1, \dots, f_w)$ of $\mathbb F_{q^m}$.
> 	2. Generates the message space $g = (g_1, \dots, g_{m - w})$ of $\mathbb F_{q^m}$ such that $(f_1, \dots, f_w, g_1, \dots, g_{m - w})$ is a basis of $\mathbb F_{q^m}$.
> 	3. $D = (g_1^*, \dots, g_{m - w}^*)$ where $(f_1^*, \dots, g_{m - w}^*)$ is the dual basis (Calculate by $(\text{Mat}(b)^{-1})^T$).
> 	4. Generates masking secret $s \xleftarrow{\$} F^n$ with $F = \text{supp}(f)$.
> 	5. Returns $(f, g, D, s)$
> - $c \leftarrow \text{Encrypt}(k, m \in \mathbb F_q^n; r = (r_1, R_2) \in \mathbb F_{q^m}^n \times \mathcal M_{w, n}(\mathbb F_q))$:
> 	1. Generates public random $u = r_1$.
> 	2. Sample uniform random noise inside $F^n$: $e = f R_2$.
> 	3. Sets $v = s \cdot u + e + \hat{m}$ with $\hat{m} = g^{(1)} \star m \in \mathbb F_{q^m}^n$.
> 	4. Returns $(u, v)$.
> - $m \leftarrow \text{Decrypt}(k, c)$:
> 	1. Returns $d^T \text{Mat}(v - s \cdot u)$ with $d = D^{(1)}$.

