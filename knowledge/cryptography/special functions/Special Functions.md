## Basic Definition

> [!definition] Functions Family
> A collection of function families $\mathbb F = \{\mathcal F\}_\lambda$ where each $\mathcal F$ is a function family $\mathcal F = \{f : \{0, 1\}^{q(\lambda)} \rightarrow \{0, 1\}^{\ell(\lambda)}\}$ is called compression if it satisfies the compressing property.

## Property

### Efficient

> [!definition] Efficient
> The function $q(\lambda)$ and $\ell(\lambda)$ are polynomially-bounded; furthermore, given $\lambda$ and $x \in \{0, 1\}^{q(\lambda)}$ the value $d(x)$ can be computed in $\text{poly}(\lambda)$ time.

### Compressing

> [!definition] Compressing
> For all $\lambda$, we have that $q(\lambda) > \ell(\lambda)$.

## Security

### Collision Resistant

> [!definition] Collision Resistant Advantage
> For all [[PPT]] algorithms $\mathcal A^\text{find}$, we define the collision resistant advantage for function $f$ with parameter $\lambda$:
> $$\text{Adv}_\text{f}^\text{CR}(\mathcal A) = 
> \; \Pr\!\left[
> \begin{array}{l}
> x \neq x' \\
> f(x) = f(x')
> \end{array}
> \; \middle | \; 
> \begin{array}{l}
> (x, x') = \mathcal A^\text{find}()
> \end{array} \right]$$

