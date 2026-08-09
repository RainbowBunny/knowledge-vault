## Syntax

> [!definition] Non-Interactive Proof Systems
> A non-interactive proof system for [[Effective Relation]] $R \subset \mathcal X \times \mathcal W$ consists of a tuple of efficient algorithms $\text{NIPS} = (\text{Setup}, \text{Prove}, \text{Verify})$:
> - $\text{crs} \leftarrow \text{Setup}(1^\lambda)$: The setup algorithm takes as input the security parameter $\lambda$, and outputs a common reference string $\text{crs}$ based on context.
> - $\pi \leftarrow \text{Prove}(\text{crs}, x, w)$: The proving algorithm takes as input the $\text{crs}$, public input $x$ and witness $w$ to generate a proof $\pi$.
> - $\{0, 1\} \leftarrow \text{Verify}(\text{crs}, x, \pi)$: The verification algorithm takes as input the $\text{crs}$, public input $x$ and the proof $\pi$ to output $1$ as $\text{accept}$ and $0$ as $\text{reject}$.

## Property

### Completeness

> [!definition] Completeness
> 