## Basic Definition

> [!algorithm] The $g^{-1}_{\mathrm{rand}}$ Algorithm
> ### Parameters
> - $d$: Degree of polynomial, NTT friendly.
> - $\beta \geq 2 \in \mathbb Z$: Decomposition base.
> - $q$: Modulus.
> - $m_q = \lceil \log_\beta q \rceil$: Number of base-$\beta$ digits needed for $\mathbb Z_q$.
> - $R = \mathbb Z[X]/(X^d + 1), R_q = R / qR$: Polynomials ring.
> - $L$: Total width; must satisfy $m_q \; | \; L$.
> - $\rho = L / m_q \in \mathbb Z$: Number of blocks.
> - $r > 0 \in \mathbb R$: Gaussian width.
> 
> ---
> ### Algorithms
> Efficiently Computable Function $g_{\mathrm{rand}}^{-1}(\mathbf{a}): R_q^\rho \rightarrow R^{1 \times L}$
> 1. $g^T = (1, \beta, \dots, \beta^{m_q - 1}) \in R_q^{1 \times m_q}$.
> 2. $G = I_\rho \otimes g \in R_q^{L \times \rho}$ (Kronecker Product)
> 3. Generates $\mathbf{c} \in R^L$ is a fixed vector satisfying $\mathbf{c}^T G = \mathbf{a} \bmod q$.
> 4. Samples $\mathbf{x} \leftarrow \mathcal D_{\Lambda_q^\perp(G) + \mathbf{c}, r}$ ([[Discrete Gaussian Distribution#Basic Definition|Discrete Gaussian]] of [[Lattices#$q$-ary Lattices|q-ary Lattices]]).
> 5. Output $\mathbf{x}^T$ which satisfies $\mathbf{x}^T G = \mathbf{a} \bmod q$ with $\mathbf{x}$ sub-gaussian of parameter $r$.

