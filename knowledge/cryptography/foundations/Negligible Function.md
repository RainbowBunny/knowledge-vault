Reference:
- https://toc.cryptobook.us/

## Basic Definition

> [!definition] Negligible Function
> A function $\varepsilon: \mathbb N \rightarrow \mathbb R_{\geq 0}$ is **negligible** if for every polynomial $p$ there exists $\lambda_0$ such that
> $$\forall \lambda > \lambda_0: \quad \varepsilon(\lambda) < \frac{1}{p(\lambda)}$$

## Property

> [!proposition] Closure
> If $\varepsilon_1, \varepsilon_2$ are negligible and $q$ is a polynomial, then $\varepsilon_1 + \varepsilon_2$ and $q(\lambda) \cdot \varepsilon_1(\lambda)$ are negligible.

> [!remark]
> The polynomial closure is what makes [[Security Game|game]] hops compose: a [[daily/Temp/PPT]] reduction can lose a polynomial factor and preserve negligibility. Against this, a hybrid argument over *super-polynomially many* hybrids proves nothing.