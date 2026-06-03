
## Argument of Knowledge

> [!algorithm] Argument of Knowledge
> The argument system $(\text{Gen}, \text{P}, \text{V})$ is called an argument of knowledge for the relation $R$ if it is complete and knowledge-sound:
> - **Knowledge Sound**: For any $2^{o(\lambda)}$ time prover $\text{P}^*$, there exists an extractor $\mathcal E$ with expected run-time polynomial in $\lambda$ and the run-time of $\text{P}^*$, such that for all PPT adversaries $\mathcal A$: 
> $$P\left[  
> \begin{array}{c|c}  
> \text{crs} \leftarrow \text{Gen}(1^\lambda), &\\ (x, s) \leftarrow \mathcal A(crs), &\\ \pi^* \leftarrow \text{P}^*(\text{crs}, x, s), &(x, w) \notin R \land b = \text{accept}\\ b \leftarrow \text{V}(\text{crs}, x, \pi^*), & \\ w \leftarrow \mathcal E^{\text{P}^*(\text{crs}, x, \pi^*, b)}
> \end{array}  
> \right] \leq 2^{-\ohm(\lambda)}.$$
> 
> If an argument of knowledge is also non-interactive zero knowledge, it is termed as a non-interactive zero knowledge argument of knowledge, abbreviated as $\text{NIZKAoK}$.

