Reference:
- https://web.cs.ucla.edu/~rafail/PUBLIC/79.pdf

## Scheme

> [!scheme] Efficient Arguments from Linear MIPs
> ### Parameters
> - $\ell$: Number of provers.
> - $\mathbb F$: Finite field.
> 
> ---
> ### Building Block
> - $\langle P, V \rangle$: [[Linear Multi-Prover Interactive Proofs#Syntax|Linear MIPs]].
> - $\langle \mathcal R, \mathcal S \rangle$: [[Parallel Commitments with Linear Decommitments#Scheme|Multi Commit Scheme]].
> 
> ---
> ### Algorithms
> $$\begin{array}{lcl} 
\mathcal P & & \mathcal V \\[4pt] 
(\pi_i: \mathbb F^n \rightarrow \mathbb F) & & \\[6pt] 
& \xleftarrow{(q_1, \dots, q_\ell)} & q_1, \dots, q_\ell \in \mathbb F^n \\[6pt]
& \xrightarrow{(\pi_1(q_1), \dots, \pi_\ell(q_\ell))} &\\[6pt] 
& &
\end{array}$$

