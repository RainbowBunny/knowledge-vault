## Basic Definition

> [!remark] Soundness
> Soundness means false statement can not be proven.

### Non-Interactive Proof Systems Variant

> [!definition] Non-Adaptive Soundness
> Given a [[Non-Interactive Proof Systems]] $\Pi_\mathsf{NIPS}$. For any [[Adversary]] $\mathcal{A} = (\mathcal{A}_\mathrm{find})$, we define the soundness advantage:
> $$\mathsf{Adv}_\mathsf{NIPS}^{\mathsf{snd}\mbox{-}\mathsf{na}}(\mathcal{A}) =  
\Pr\!\left[ 
\begin{array}{l}
\mathbf{x} \notin \mathcal{L}_\mathcal{R} \\
\mathsf{Verify}(st, \mathbf{x}, \boldsymbol{\pi}) = 1
\end{array} 
\;\middle |\; 
\begin{array}{l}
(\mathbf{x}, \boldsymbol{\pi}^*) \leftarrow \mathcal{A}_\mathrm{find}(\mathcal{R}) \\
(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal{R})
\end{array} \right]$$

> [!definition] Adaptive Soundness
> Given a [[Non-Interactive Proof Systems]] $\Pi_\mathsf{NIPS}$. For any [[Adversary]] $\mathcal{A} = (\mathcal{A}_\mathrm{find})$, we define the soundness advantage:
> $$\mathsf{Adv}_\mathsf{NIPS}^{\mathsf{snd}\mbox{-}\mathsf{a}}(\mathcal{A}) =  
\Pr\!\left[ 
\begin{array}{l}
\mathbf{x} \notin \mathcal{L}_\mathcal{R} \\
\mathsf{Verify}(st, \mathbf{x}, \mathbf{Q}^T \boldsymbol{\pi}^*) = 1
\end{array} 
\;\middle |\; 
\begin{array}{l}
(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal{R}) \\
(\mathbf{x}, \boldsymbol{\pi}^*) \leftarrow \mathcal{A}_\mathrm{find}(\mathcal{R}, \mathrm{crs}, \mathrm{st})
\end{array} \right]$$
