Reference:
- https://eprint.iacr.org/2016/260.pdf

## Syntax

> [!definition] Split Non-Interactive Linear Proof
> Extends: [[Non-Interactive Linear Proofs]]
> - $\mathsf{Setup}$: $\mathrm{crs}$ is now $(\mathrm{crs}_1, \mathrm{crs}_2) \in \mathbb{F}^{m_1} \times \mathbf{F}^{m_2}$.
> - $\mathsf{Prove}$: 
> 	1. $\Pi$ is now $\begin{pmatrix}\Pi_1 & 0 \\ 0 & \Pi_2\end{pmatrix}$ where $\Pi_1 \in \mathbb{F}^{k_1 \times m_1}$ and $\Pi_2 \in \mathbb{F}^{k_2 \times m_2}$.
> 	2. $\boldsymbol{\pi}_1 = \Pi_1 \mathrm{crs}_1, \boldsymbol{\pi}_2 = \Pi_2 \mathrm{crs}_2$
> - $\mathsf{Verify}$:
> 	1. The arithmetic circuit is now $t: \mathbb{F}^{m_1 + k_1 + m_2 + k_2} \rightarrow \mathbb{F}^\eta$ corresponding to matrices $T_1, \dots, T_\eta \in \mathbb{F}^{(m_1 + k_1) \times (m_2 + k_2)}$.
> 	2. We now accept if
> 	$$\begin{pmatrix}\mathrm{crs}_1 \\ \boldsymbol{\pi}_1\end{pmatrix} \cdot T_i \begin{pmatrix}\mathrm{crs}_2 \\ \boldsymbol{\pi}_2\end{pmatrix} = 0.$$

## Property

### 