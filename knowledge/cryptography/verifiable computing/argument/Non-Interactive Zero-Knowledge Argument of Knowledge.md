---
dg-publish: true
---
Reference: 
- https://www.di.ens.fr/~nitulesc/files/Survey-SNARKs.pdf

## Syntax

> [!definition] Non-Interactive Zero-Knowledge Argument of Knowledge
> For pairs $(x, w)$ of an [[Effective Relation#Basic Definition|Effective Relation]] $R$ where $x$ is the statement and $w$ is the witness. A non-interactive zero-knowledge argument $\mathsf{NIZKAoK}$ for $R$ is a quadruple of efficient algorithms $(\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify}, \mathsf{Sim})$:
> - $(\sigma, \tau) \leftarrow \mathsf{Setup}(R)$: The setup algorithm that base on a relation $R$, returns a common reference string $\sigma$ and a simulation trapdoor $\tau$.
> - $\pi \leftarrow \mathsf{Prove}(\sigma, x, w)$: The prover algorithm that takes as input a common reference string $\sigma$ for a relation $R$ and $(x, w) \in R$ and returns an argument $\pi$.
> - $\{0, 1\} \leftarrow \mathsf{Verify}(\sigma, x, \pi)$: The verification algorithm takes as input a common reference string, a statement $u$ and an argument $\pi$ and returns 0 (rejects) or 1 (accepts).
> - $\pi \leftarrow \mathsf{Sim}(\tau, u)$: The simulator takes as input a simulation trapdoor and a statement $x$ and returns an argument $\pi$.

## Property

### Completeness

> [!definition] Completeness
> For any adversary $\mathcal A = (\mathcal A_\mathsf{find})$, we define the completeness advantage (sometimes refer as completeness error $\varepsilon_c$):
>  $$\mathsf{Adv}_\mathsf{NIZKAoK}^\mathsf{com}(\mathcal A) = 
\Pr\!\left[ 
\begin{array}{l}
(x, w) \in R \\
\mathsf{Verify}(\sigma, x, \pi) = 1
\end{array} 
\;\middle |\; 
\begin{array}{l}
(\sigma, \tau) \leftarrow \mathsf{Setup}(R) \\
(x, w) \leftarrow \mathcal A_\mathsf{find}(\sigma, \tau) \\
\pi \leftarrow \mathsf{Prove}(\sigma, x, w)
\end{array} \right] 
$$

## Security

### Soundness

