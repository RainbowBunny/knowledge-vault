---
dg-publish: true
---
Reference:
- https://eprint.iacr.org/2025/373.pdf

## Syntax

> [!definition] Split Prover
> Let $\Pi_\mathsf{NIPS} = (\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify})$ be a [[Non-Interactive Proof Systems]] for a relation $\mathcal{R}$ **decided by a circuit $\mathbf{C}$**, we say that $\Pi$ admits a **split prover** if there exist algorithms $\Pi_\mathsf{split} = (\mathsf{Setup}_\mathsf{split}, \mathsf{Prove}_{I}, \mathsf{Prove}_{II})$:
> - $(\mathrm{srs}_{I}, \mathrm{srs}_{II}, \widetilde{\mathrm{st}}) \leftarrow \mathsf{Setup}_\mathsf{split}(1^\lambda, \mathcal R, \mathcal{X}_{II}, \mathcal{W}_{II})$: On indexed sets $\mathcal{X}_{II}, \mathcal{W}_{II}$ specifying the phase-$II$ portions of statement and witness, outputs the split reference string for each phase and the verification state $\widetilde{\mathrm{st}}$.
> - $\mathrm{aux}_\mathsf{split} \leftarrow \mathsf{Prove}_{I}(\mathrm{srs}_{I}, \mathbf{x}_I, \mathbf{w}_I)$: On the phase $I$ split reference string and the phase-$I$ portion of statement and witness, outputs auxiliary information for phase-$II$.
> - $\boldsymbol{\pi^*} \leftarrow \mathsf{Prove}_{II}(\mathrm{srs}_{II}, \mathbf{x}_{II}, \mathbf{w}_{II}, \mathrm{aux}_\mathsf{split})$: On the phase $II$ split reference string, phase-$II$ portion of statement and witness and auxiliary information, outputs a proof.
> 
> Also, we can write $\mathbf{C} = \mathbf{C}_{II}(\mathbf{x}_{II}, \mathbf{w}_{II}, \mathbf{C}_{I}(\mathbf{x}_I, \mathbf{w}_I))$

> [!remark] Naming
> $\mathrm{aux}_\mathsf{split}$ is the hand-off from $\mathsf{Prove}_{I}$ to $\mathsf{Prove}_{II}$. The plain $\mathrm{aux}$ is reserved for the context returned by the relation generator, see [[Non-Interactive Proof Systems]].

> [!remark] View of Each Party
> **Public View**: $\mathcal{R}, \mathbf{C}, \mathcal{X}_{II}, \mathcal{W}_{II}$.
> **Prover I**: $\mathrm{srs}_I, \mathbf{x}_I, \mathbf{w}_I$.
> **Prover II**: $\mathrm{srs}_{II}, \mathbf{x}_{II}, \mathbf{w}_{II}, \mathrm{aux}_\mathsf{split}$. 
> **Verifier**: $\tilde{\mathrm{st}}, \mathbf{x}, \mathbf{\pi}$.

## Property
 
### Split Correctness

> [!definition] Split Correctness
> For any adversary $\mathcal{A} = (\mathcal{A}_\mathsf{find})$, we define the split correctness advantage:
> $$\mathsf{Adv}_{\Pi_\mathsf{NIPS}, \Pi_\mathsf{split}}^\mathsf{scmp}(\mathcal{A}) = 
\Pr\!\left[ 
\begin{array}{l}
\mathsf{Verify}(\mathrm{st}, \mathbf{x}, \boldsymbol{\pi}) = \mathsf{Verify}(\widetilde{\mathrm{st}}, \mathbf{x}, \boldsymbol{\pi}')
\end{array} 
\;\middle |\; 
\begin{array}{l}
(\mathcal{X}_{II}, \mathcal{W}_{II}, \mathbf{x}, \mathbf{w}) \leftarrow \mathcal{A}_\mathsf{find}(\mathcal{R}) \\
(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal{R}); (\mathrm{srs}_I, \mathrm{srs}_{II}, \widetilde{\mathrm{st}}) \leftarrow \mathsf{Setup}_\mathsf{split}(1^\lambda, \mathcal{R}, \mathcal{X}_{II}, \mathcal{W}_{II}) \\
\mathbf{x} = (\mathbf{x}_I || \mathbf{x}_{II}); \mathbf{w} = (\mathbf{w}_I || \mathbf{w}_{II}) \\
\boldsymbol{\pi} \leftarrow \mathsf{Prove}(\mathrm{crs}, \mathbf{x}, \mathbf{w}) \\
\mathrm{aux}_\mathsf{split} \leftarrow \mathsf{Prove}_{I}(\mathrm{srs}_I, \mathbf{x}_{I}, \mathbf{w}_{I});
\boldsymbol{\pi}' \leftarrow \mathsf{Prove}_{II}(\mathrm{srs}_{II}, \mathbf{x}_{II}, \mathbf{w}_{II}, \mathrm{aux}_\mathsf{split})
\end{array} \right]$$

## Security

### Split Zero-Knowledge

> [!definition] Split Zero-Knowledge
> For any adversary $\mathcal{A} = (\mathcal{A}_\mathsf{choose}, \mathcal{A}_\mathsf{guess})$and simulator $\mathcal{S} = (\mathcal{S}_\mathsf{setup})$, we define the zero-knowledge advantage:
> $$\mathsf{Adv}_{\Pi_\mathsf{NIPS}, \Pi_\mathsf{split}}^{\mathsf{szk}}(\mathcal{A}) = \left|\; \Pr\!\left[
\begin{array}{l}
b' = 1
\end{array}
\;\middle |\; 
\begin{array}{l}
(\mathbf{x}, \mathbf{w}) \leftarrow \mathcal{A}_\mathsf{choose}(1^\lambda, \mathcal{R}, \mathcal{X}_{II}, \mathcal{W}_{II}) \\
(\mathrm{srs}_{I}, \mathrm{srs}_{II}, \widetilde{\mathrm{st}}) \leftarrow \mathsf{Setup}_{\mathsf{split}}(1^\lambda, \mathcal{R}, \mathcal{X}_{II}, \mathcal{W}_{II}) \\
\mathrm{aux}_\mathsf{split} \leftarrow \mathsf{Prove}_{I}(\mathrm{srs}_{I}, \mathbf{x}_{I}, \mathbf{w}_{I}) \\
b' \leftarrow \mathcal{A}_\mathsf{guess}(\mathrm{srs}_{I}, \mathrm{srs}_{II}, \widetilde{\mathrm{st}}, \mathrm{aux}_\mathsf{split})
\end{array} \right] 
\;- 
\Pr\!\left[
\begin{array}{l}
b' = 1
\end{array}
\;\middle |\; 
\begin{array}{l}
(\mathbf{x}, \mathbf{w}) \leftarrow \mathcal{A}_\mathsf{choose}(1^\lambda, \mathcal{R}, \mathcal{X}_{II}, \mathcal{W}_{II}) \\
(\mathrm{srs}_{I}, \mathrm{srs}_{II}, \widetilde{\mathrm{st}}, \mathrm{aux}_\mathsf{split}) \leftarrow \mathcal{S}_{\mathsf{setup}}(1^\lambda, \mathcal{R}, \mathcal{X}_{II}, \mathcal{W}_{II}, \mathbf{x}, \mathbf{C}_I(\mathbf{x}_I, \mathbf{w}_I)) \\
\\
b' \leftarrow \mathcal{A}_\mathsf{guess}(\mathrm{srs}_{I}, \mathrm{srs}_{II}, \widetilde{\mathrm{st}}, \mathrm{aux}_\mathsf{split})
\end{array} \right] 
\right|.$$
