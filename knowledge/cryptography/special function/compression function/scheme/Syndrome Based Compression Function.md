## Syntax

> [!definition] Parameters
> - [[Syndrome Decoding Problem]]: Import $(n, k, w, \mathbb{F}_2, \mathsf{wt}_\mathsf{H})$.
> - Function input size $l = \log_2{\binom{n}{w}}$

> [!scheme] Syndrome Based Compression Function
> - $h \leftarrow \mathsf{Hash}(m \in \mathbb{F}_2^s) \in \mathbb{F}_2^k$:
> 	1. Encodes $m$ into $\mathbf{x} \leftarrow \mathcal{S}_w^n(\mathbb{F}_2)$ ([[Hamming Sphere]]).
> 	2. Generates $\mathbf{H} \xleftarrow{\$} \mathbb{F}_2^{k \times n}$.
> 	3. Returns $\mathbf{H} \mathbf{x}^T$.

