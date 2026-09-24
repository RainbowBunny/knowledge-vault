## Distribution

> [!definition] Regular Syndrome Decoding Distribution
> ### Distribution
> Sampling experiment: $\text{SD}(n, k, w)$
> 1. $\mathbf{H} \xleftarrow{\$} \mathbb{F}_2^{(n - k) \times n}$ ([[Linear Code#Generator Matrix and Parity-Check Matrix|Parity-Check Matrix]]).
> 2. $\mathbf{x}_1, \dots, \mathbf{x}_w \xleftarrow{\$} \mathcal{S}^{n / w}_1(\mathbb{F}_2)$ ([[Hamming Sphere]]).
> 3. $\mathbf{x} = (\mathbf{x}_1 \mid \dots \mid \mathbf{x}_w)$.
> 4. Output $(\mathbf{H}, \sigma(\mathbf{x}) = \mathbf{H}\mathbf{x}^{T})$.
