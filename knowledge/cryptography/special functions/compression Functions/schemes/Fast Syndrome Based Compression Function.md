## Syntax

> [!definition] Parameters
> - [[Regular Syndrome Decoding Problem]]: Import $(n, k, w, \mathbb{F}_2, \mathsf{wt}_\mathsf{H})$.
> - Function input size $l = w \log_2(n / w)$.

> [!scheme] Fast Syndrome Based Compression Function
> - $h \leftarrow \mathsf{Hash}(m \in \mathbb{F}_2^l) \in \mathbb{F}_2^k$:
> 	1. Splits $m$ into $w$ parts $m_1, \dots, m_w$ of $\log_2(n / w)$ bits.
> 	2. Converts $m_i$ to an integer between $1$ and $\frac{n}{w}$.
> 	3. Generates $\mathbf{x}_i$ is the vector where the only non-zero coordinates is $\mathbf{x}_i^{(m_i)} = 1$.
> 	4. Generates $\mathbf{H} \xleftarrow{\$} \mathbb{F}_2^{k \times n}$.
> 	5. Returns $\mathbf{H} \mathbf{x}^T$ ($\mathbf{x} = (\mathbf{x}_1, \dots, \mathbf{x}_w)$).
