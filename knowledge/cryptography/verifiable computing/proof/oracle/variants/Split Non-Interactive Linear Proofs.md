Reference:
- https://eprint.iacr.org/2016/260.pdf

## Syntax

> [!definition] Non-Interactive Linear Proof
> Let $\mathcal R$ be an [[Effective Relation]] over $\mathbb F$. A NILP for $\mathcal R$ with $\mathrm{crs}$ length $m$, verification state length $n$, proof length $k$, and $\eta$ tests of degree $d$ is a tuple $\Pi_\mathsf{NILP} = (\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify})$ with two support algorithms $(\mathsf{ProofMatrix}, \mathsf{Test})$:
> - $(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal{R})$: The setup algorithm outputs a vector $\mathrm{crs} = (\mathrm{crs}_1, \mathrm{crs}_2) \in \mathbb{F}^{m_1} \times \mathbf{F}^{m_2}$ with $1$ as an entry and a verification state $\mathrm{st} \in \mathbb{F}^n$. 
> - $\boldsymbol{\pi} \leftarrow \mathsf{Prove}(\mathcal{R}, \mathbf{x}, \mathbf{w})$: On input statement $\mathbf{x}$ and witness $\mathbf{w}$, the prove algorithm generates a proof matrix $\boldsymbol{\Pi} \in \mathbb{F}^{k \times m}$ and generate the proof.
> 	1. $\Pi = \begin{pmatrix}\Pi_1 & 0 \\ 0 & \Pi_2\end{pmatrix} \leftarrow \mathsf{ProofMatrix}(\mathcal{R}, \mathbf{x}, \mathbf{w})$ where $\Pi_1 \in \mathbb{F}^{k_1 \times m_1}$ and $\Pi_2 \in \mathbb{F}^{k_2 \times m_2}$.
> 	2. Returns $\Pi \; \mathrm{crs} \in \mathbb{F}^{k}$.
> - $b \leftarrow \mathsf{Verify}(\mathcal{R}, \mathrm{st}, \mathbf{x}, \boldsymbol{\pi})$:
> 	1. Runs $\mathbf{t} \leftarrow \mathsf{Test}(\mathcal{R}, \mathbf{x}, \mathrm{st})$ to get the arithmetic circuit $\mathbf{t}: \mathbb{F}^{k} \rightarrow \mathbf{F}^\eta$ corresponding to the evaluation of $\eta$ polynomials.
> 	2. Accepts if $t(\boldsymbol{\pi}) = 0$.
