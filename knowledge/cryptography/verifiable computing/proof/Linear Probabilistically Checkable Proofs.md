---
dg-publish: true
---
Reference:
- https://eprint.iacr.org/2022/1690.pdf

## Syntax

> [!definition] Linear PCP
> Let $\mathbb F$ be a finite field and $\mathcal{CS} = (n, N_g, N_w, \{a_i, b_i, c_i\}_{i \in [N_g]})$ an [[Rank-1 Constraint Statisfiability#Basic Definition|R1CS]] over $\mathbb F$. A **$k$-query input-independent linear PCP** for $\mathcal{CS}$ with query length $m$ is a tuple of algorithms $\Pi_{\mathsf{LPCP}} = (\mathsf{Query}, \mathsf{Prove}, \mathsf{Verify})$:
> - $(st, Q) \leftarrow \mathsf{Query}(\mathcal {CS})$: The query generation algorithms outputs a query matrix $Q \in \mathbb F^{m \times k}$ and a verification state $\mathrm{st}$. 
> - $\boldsymbol{\pi} \leftarrow \mathsf{Prove}(\mathcal{CS}, \mathbf{x}, \mathbf{w})$: On statement $\mathbf{x} \in \mathbb F^n$ and a witness $\mathbf{w} \in \mathbb F^{N_w}$, the prove algorithm outputs a proof $\boldsymbol{\pi} \in \mathbb F^m$.
> - $b \leftarrow \mathsf{Verify}(st, \mathbf{x}, \mathbf{a})$: On input the verification state $\mathrm{st}$, the statement $\mathbf{x} \in \mathbb F^n$, and a vector of responses $\mathbf{a} \in \mathbb F^k$, the verification algorithm outputs a bit $b \in \{0, 1\}$.

## Property

### Completeness

> [!definition] (Perfect) Completeness
> For every $\mathbf{x} \in \mathbb F^n$ and $\mathbf{w} \in \mathbb F^{N_w}$ with $\mathcal{CS}(\mathbf{x}, \mathbf{w}) = 1$:
>  $$
> \Pr\!\left[ \mathsf{Verify}(st, \mathbf{x}, Q^T \boldsymbol{\pi}) = 1 \;\middle |\; 
> \begin{array}{l}
> (st, Q) \leftarrow \mathsf{Query}(\mathcal{CS}) \\
> \pi \leftarrow \mathsf{Prove}(\mathcal{CS}, \mathbf{x}, \mathbf{w})
> \end{array} \right] = 1$$

> [!definition] Completeness
> 

## Security

### Soundness

> [!definition] Soundness
> For any adversary $\mathcal{A} = (\mathcal{A}^\mathrm{find})$, we define the soundness advantage:
> $$\mathsf{Adv}_\mathsf{LPCP}^\mathsf{snd}(\mathcal{A}) =  
  \Pr\!\left[ 
  \begin{array}{l}
  \mathbf{x} \notin \mathcal{L}_\mathcal{CS} \\
  \mathsf{Verify}(st, \mathbf{x}, \mathbf{Q}^T \boldsymbol{\pi}^*) = 1
  \end{array} 
  \;\middle |\; 
  \begin{array}{l}
  (\mathbf{x}, \boldsymbol{\pi}^*) \leftarrow \mathcal A(\mathcal{CS}) \\
  (st, \mathbf{Q}) \leftarrow \mathsf{Query}(\mathcal{CS})
  \end{array} \right] 
 $$

### Knowledge Soundness

