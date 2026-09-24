## Definition

> [!definition] $\Sigma_i$SAT
> For every $i \geq 1$, $\Sigma_i \mathsf{SAT}$ is the class of [[Quantified Boolean Formula]] of the following type with a limited number of alternations:
> $$\exists u_1 \forall u_2 \exists \cdots Q_i u_i \varphi(u_1, u_2, \dots, u_i) = 1$$
> where $u_1, \dots, u_i$ are now vectors, and $Q_i$ is $\forall$ or $\exists$ depending on whether $i$ is even or odd respectively.

## Property

> [!proposition]
> Requires:: [[Hardness and Completeness]]
> Complete for:: [[Level Polynomial Hierarchy|Sigma]] under [[Polynomial-time Karp Reducibility]]
> 
> ---
> $\Sigma_i \mathsf{SAT}$ is $\Sigma_i^p \mbox{-} \mathsf{complete}$
