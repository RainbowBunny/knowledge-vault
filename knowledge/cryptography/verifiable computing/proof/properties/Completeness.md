## Definition

> [!remark]
> Completeness means a true statement can be proven.

### Non-Interactive Proof Systems Variant

> [!definition] Completeness of Non-Interactive Proof System
> Given a [[Non-Interactive Proof Systems]] $\Pi_\mathsf{NIPS}$. For any [[Adversary]] $\mathcal{A} = (\mathcal{A}_\mathsf{find})$, we define the completeness advantage (sometimes refer as completeness error $\varepsilon_c$):
>  $$\mathsf{Adv}_\mathsf{NIPS}^\mathsf{cmp}(\mathcal{A}) = 
\Pr\!\left[ 
\begin{array}{l}
(\mathbf{x}, \mathbf{w}) \in \mathcal{R} \\
\mathsf{Verify}(\mathrm{st}, \mathbf{x}, \pi) = 1
\end{array} 
\;\middle |\; 
\begin{array}{l}
(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal{r}) \\
(\mathbf{x}, \mathbf{w}) \leftarrow \mathcal{A}_\mathsf{find}(\mathrm{crs}, \mathrm{st}) \\
\pi \leftarrow \mathsf{Prove}(\mathrm{crs}, \mathbf{x}, 
\mathbf{w})
\end{array} \right]$$

