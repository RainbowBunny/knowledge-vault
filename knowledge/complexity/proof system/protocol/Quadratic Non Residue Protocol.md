Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.1.3: Interactive proof for graph nonisomorphism.

## Definition

> [!definition] Parameters
> - $a$: Integers.
> - $p$: Prime.

> [!definition] Statement
> The prover $\mathcal{P}$ wants to convince the verifier $\mathcal{V}$:
> $$\left( \frac{a}{p} \right) = -1$$

> [!scheme] Quadratic Non-Residue Protocol
> - $\{0, 1\} \leftarrow \mathsf{Guess}(c, p)$: 
> 	- **Input**: Two value $c$ and prime $p$.
> 	- **Output**: 0 if $c$ is a quadratic nonresidue and 1 otherwise.
> 
> ---
> $$\begin{array}{llcl} 
\mathcal{P} & & \mathcal{V} \\[4pt] 
 & & r \xleftarrow{\$} \mathbb{Z}_p^*; b \xleftarrow{\$} \{0, 1\} \\
 & \xleftarrow{c} & c = a^b r^2 \bmod p\\
b' \leftarrow \mathsf{Guess}(c, p) & \xrightarrow{b'} & b \stackrel{?}{=} b'
\end{array}$$