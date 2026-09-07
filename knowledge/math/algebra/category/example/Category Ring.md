## Syntax

> [!definition] Category $\mathsf{Ring}$
> Category $\mathsf{Ring}$ consists of
> - $\mathsf{Obj}(\mathsf{Ring})$ is the class of all [[Ring]].
> - For $R, S$ rings, we define
> $$\mathsf{Hom}_\mathsf{Ring}(R, S)$$
> to be the set of ring [[Homomorphism]] $R \rightarrow S$.

## Property

### Universal Property

> [!proposition] Initial Object
> The category $\mathsf{Ring}$ has an initial object which is the ring of integers $\mathbb{Z}$ (with the usual operations $+, \cdot$). 
> - For every ring $R$ we can define a unique [[Group Homomorphism]] $\varphi: \mathbb{Z} \rightarrow R$ by
> $$(\forall n \in \mathbb{Z}): \varphi(n) = n \cdot 1_R$$
