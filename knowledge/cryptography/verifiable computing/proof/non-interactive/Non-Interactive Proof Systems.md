## Syntax

> [!definition] Non-Interactive Proof Systems
> Let $\mathcal{R}$ be an [[Effective Relation]]. A non-interactive proof system for $\mathcal{R}$ is a tuple $\Pi_\mathsf{NIPS} = (\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify})$ with the following properties:
> - $(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal{R})$: On input the security parameter $\lambda$ and $\mathcal{R}$, the setup algorithm outputs a common reference string $\mathrm{crs}$ and verification state $\mathrm{st}$.
> - $\boldsymbol{\pi} \leftarrow \mathsf{Prove}(\mathrm{crs}, \mathbf{x}, \mathbf{w})$: On input a common reference string $\mathrm{crs}$, a statement $\mathbf{x}$ and a witness $\mathbf{w}$, the prove algorithms outputs a proof $\boldsymbol{\pi}$.
> - $b \leftarrow \mathsf{Verify}(\mathrm{st}, \mathbf{x}, \boldsymbol{\pi})$: On input the verification state $\mathrm{st}$, a statement $\mathbf{x}$ and a proof $\boldsymbol{\pi}$, the verification algorithm outputs a bit $b \in \{0, 1\}$.

## Relation

|                                        | Completeness | Soundness     | Knowledge | Succinct | ZK  |
| -------------------------------------- | ------------ | ------------- | --------- | -------- | --- |
| [[Non-Interactive Proof Systems\|NIP]] | ✓            | statistical   | —         | —        | —   |
| NARG                                   | ✓            | computational | —         | —        | —   |
| NARK                                   | ✓            | computational | ✓         | —        | —   |
| SNARG                                  | ✓            | computational | —         | ✓        | —   |
| SNARK                                  | ✓            | computational | ✓         | ✓        | —   |
| zk-SNARG                               | ✓            | computational | —         | ✓        | ✓   |
| zk-SNARK                               | ✓            | computational | ✓         | ✓        | ✓   |
