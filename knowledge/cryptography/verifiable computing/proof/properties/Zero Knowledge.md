## Basic Definition

### Non-Interactive Proof System

> [!definition] Zero-Knowledge
> Given a [[Non-Interactive Proof Systems]] $\Pi_{NIPS}$. For any adversary $\mathcal{A} = (\mathcal{A}_\mathsf{find}, \mathcal{A}_\mathsf{guess})$ and simulator $\mathcal{S} = (\mathcal{S}_\mathsf{setup}, \mathcal{S}_\mathsf{prove})$, we define the zero-knowledge advantage:
> $$\mathsf{Adv}_\mathsf{NIPS}^\mathsf{zk}(\mathcal{A}, \mathcal{S}) = 
\left|\; \Pr\!\left[
\begin{array}{l}
b = 1
\end{array}
\;\middle |\; 
\begin{array}{l}
(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal{R}) \\
(\mathbf{x}, \mathbf{w}) \leftarrow \mathcal{A}_\mathsf{find}(\mathcal{R}, \mathrm{crs}, \mathrm{st}) \\
\boldsymbol{\pi} \leftarrow \mathsf{Prove}(\mathrm{crs}, \mathbf{x}, \mathbf{w}) \\
b \leftarrow \mathcal{A}_\mathsf{guess}(\boldsymbol{\pi})
\end{array} \right] 
\;- 
\Pr\!\left[
\begin{array}{l}
b = 1
\end{array}
\;\middle |\; 
\begin{array}{l}
(\widetilde{\mathrm{crs}}, \widetilde{\mathbf{st}}, \mathrm{st}_\mathcal{S}) \leftarrow \mathcal{S}_\mathsf{setup}(1^\lambda, \mathcal{R}) \\
(\mathbf{x}, \mathbf{w}) \leftarrow \mathcal{A}_\mathsf{find}(\mathcal{R}, \widetilde{\mathrm{crs}}, \widetilde{\mathbf{st}}) \\
\widetilde{\boldsymbol{\pi}} \leftarrow \mathcal{S}_\mathsf{prove}(\mathrm{st}_\mathcal{S}, \mathbf{x}) \\
b \leftarrow \mathcal{A}_\mathsf{guess}(\widetilde{\boldsymbol{\pi}})
\end{array} \right] 
\right|.$$

> [!remark]
> There is a Leakage variant.