Reference:
- https://eprint.iacr.org/2016/260.pdf

## Syntax

> [!definition] Non-Interactive Linear Proof
> Let $\mathcal R$ be an [[Effective Relation]] over $\mathbb F$. A NILP for $\mathcal R$ with $\mathrm{crs}$ length $m$, proof length $k$, and $\eta$ tests of degree $d$ is a tuple $\Pi_\mathsf{NILP} = (\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify})$ with two support algorithms $(\mathsf{ProofMatrix}, \mathsf{Test})$:
> - $(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal{R})$: The setup algorithm outputs a vector $\mathrm{crs} \in \mathbb{F}^m$ with $1$ as an entry and a verification state $\mathrm{st}$. 
> - $\boldsymbol{\pi} \leftarrow \mathsf{Prove}(\mathcal{R}, \mathbf{x}, \mathbf{w})$: On input statement $\mathbf{x}$ and witness $\mathbf{w}$, the prove algorithm outputs a proof matrix $\boldsymbol{\Pi} \in \mathbb{F}^{k \times m}$.
> 	1. $\Pi \leftarrow \mathsf{ProofMatrix}(\mathcal{R}, \mathbf{x}, \mathbf{w}) \in \mathbb{F}^{k \times m}$.
> 	2. Returns $\Pi \; \mathrm{crs} \in \mathbb{F}^{k}$.
> - $b \leftarrow \mathsf{Verify}(\mathcal{R}, \mathrm{st}, \mathbf{x}, \boldsymbol{\pi})$:
> 	1. Runs $t \leftarrow \mathsf{Test}(\mathcal{R}, \mathbf{x}, \mathrm{st})$ to get the arithmetic circuit $\mathbf{t}: \mathbb{F}^{k} \rightarrow \mathbf{F}^\eta$ corresponding to the evaluation of $\eta$ polynomials.
> 	2. Accepts if $t(\boldsymbol{\pi}) = 0$.

> [!definition] Linear Evaluation
> For $\boldsymbol{\Pi} \in \mathbb{F}^{k \times m}$ and $\mathrm{crs} \in \mathbb{F}^m$, write $\boldsymbol{\pi}_{\Pi, \mathrm{crs}} = \boldsymbol{\Pi} \mathrm{crs} \in \mathbb{F}^k$. Every proof — honest or adversarial — is of this form: the prover chooses only the coefficient matrix, never the field elements.

