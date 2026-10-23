Reference:
- `[Ksc22]` — F. R. Kschischang, _Kronecker Product and Vectorization_ (University of Toronto, 2022), §2: https://www.comm.utoronto.ca/frank/notes/vec.pdf

## Definition

> [!definition] Parameters
> - $\mathbb F$: a [[Field]].
> - $A = (a_{ij})$: an $m \times n$ [[Matrix]] over $\mathbb F$.
> - $B$: a $p \times q$ matrix over $\mathbb F$.

> [!definition] Kronecker Product (Tensor Product)
> Given a $m \times n$ matrix $A$ and $p \times q$ matrix $B$, then the Kronecker product $A \otimes B$ is the $pm \times qn$ block matrix:
> $$A \otimes B = \begin{bmatrix}
> a_{11} B & \cdots & a_{1n} B \\
> \vdots   & \ddots & \vdots   \\
> a_{m1} B & \cdots & a_{mn} B
> \end{bmatrix}$$
>
> `[Ksc22 §2]`

## Related

### Prerequisites
- [[Matrix]] — the factors and the block layout
