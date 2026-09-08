## Hyper-Elliptic Curve Discrete Logarithm Problem

> [!definition] Hyperelliptic Curve
> A curve in the form $$y^2 = f(x) = ax^{2n + 2} + ...$$ is a hyperelliptic curve of genus $n$. The group of these curve is **not points**, but the **Jacobian** $J(C)$.

> [!definition] Mumford Representations
> On a genus-2 curve, group element are **reduced divisors** and represented in **Mumford form**: $$(u(x), v(x))$$ where:
> - $u(x)$ is monic and $\deg u(x) \leq 2$ 
> - $v(x)^2 \equiv f(x) \pmod {u(x)}$

> [!remark]
> For some situations, like with hyperelliptic curve, the order of the group might not be available, but we can guess the order of the element $g$ and check: $$\text{order} \cdot g = 1.$$
