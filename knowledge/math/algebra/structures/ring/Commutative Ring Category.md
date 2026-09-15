## Definition

> [!definition] Commutative Ring Category
> Let $A = \{a_1, \dots, a_n\}$ be a [[Set]] of order $n$.
> Category $\mathcal{R}_A$:
> - $\mathsf{Obj}(\mathcal{R}_A)$ consists of all pairs $(j, R)$ where $R$ is a [[Commutative Ring]] and 
> $$j: A \rightarrow R$$
> is a [[Function]].
> - For two objects $(j_1, R_1)$ and $(j_2, R_2)$, $\mathsf{Hom}_{\mathcal{R}_A}((j_1, R_1), (j_2, R_2))$ is the set of $\varphi: R_1 \rightarrow R_2$ is a [[Ring Homomorphism]], the diagram
> $$\begin{CD}
> R_1 @>\varphi>> R_2 \\
> @Aj_1AA @AAj_2A \\
> A @= A
> \end{CD}$$
> is commutative.

## Property

> [!proposition]
> $(i, \mathbb{Z}[x_1, \dots, x_n])$ is [[Universal Property|Initial]] in $\mathcal{R}_A$.
