## Definition

> [!remark]
> Knowledge Soundness means to proof a statement, you need to know the witness.

### Non-Interactive Proof Systems Variant

> [!definition] Knowledge Soundness
> Given a [[Non-Interactive Proof Systems]] $\Pi_\mathsf{NIPS}$. For any adversary $\mathcal{A} = (\mathcal{A}_\mathsf{find})$ and an efficient extractor $\mathcal{E} = (\mathcal{E}_\mathsf{NIPS})$, we define the non-adaptive knowledge soundness advantage:
> $$\mathsf{Adv}_\mathsf{NIPS}^{\mathsf{ks}}(\mathcal{A}, \mathcal{E}) = 
\Pr\!\left[ 
\begin{array}{l}
(\mathbf{x}, \mathbf{w}) \notin \mathcal{R}\\
\mathsf{Verify}(st, \mathbf{x}, \boldsymbol{\pi}^*) = 1
\end{array} 
\;\middle |\; 
\begin{array}{l}
(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal{R}) \\
(\mathbf{x}, \boldsymbol{\pi}^*) \leftarrow \mathcal{A}_\mathsf{find}(\mathcal{R}, \mathrm{crs}, \mathrm{st}) \\
\mathbf{w} \leftarrow \mathcal{E}_\mathsf{find}(1^\lambda, \mathcal{R}, \mathrm{crs}, \mathrm{st}, \mathbf{x})
\end{array} \right]$$

> [!remark]
> The extractor also knows the internal randomness of the prover and thus there is no adaptive variant here (the extractor can impersonate the prover).
