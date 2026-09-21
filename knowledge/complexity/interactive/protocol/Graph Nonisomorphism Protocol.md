Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.1.3: Interactive proof for graph nonisomorphism.
Instantiates:: [[Probabilistic Interactive Proof System]]

## Definition

> [!definition] Parameters
> - $G_1, G_2$: Graph.

> [!definition] Statement
> The prover $\mathcal{P}$ wants to convince the verifier $\mathcal{V}$:
> $$G_1 \ncong G_2$$

> [!scheme] Private-coin Graph Non-isomorphism
> - $H \leftarrow \mathsf{Permute}(G_i)$: 
> 	- **Input**: Takes input a graph $G_i$.
> 	- **Output**: Returns a permutation $H$ of $G_i$.
> - $\{1, 2\} \leftarrow \mathsf{Guess}(H, G_1, G_2)$: 
> 	- **Input**: Takes input of a target graph $H$ and two graphs $G_1, G_2$.
> 	- **Output**: Returns which graph was the permutation of $H$.
> ---
> 
> $$\begin{array}{llcl} 
\mathcal{P} & & \mathcal{V} \\[4pt] 
 &  & i \xleftarrow{\$} \{1, 2\} \\
 & \xleftarrow{H} & H \leftarrow \mathsf{Permute}(G_i)\\
j \leftarrow \mathsf{Guess}(H, G_1, G_2) & \xrightarrow{j} & i \stackrel{?}{=} j\\
\end{array}$$
