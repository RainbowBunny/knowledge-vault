## Definition

> [!definition] Uniform Distribution
> A continuous random variable $X$ is said to have **uniform** distribution over the interval $[a, b]$, shown as $X \sim \text{Uniform}(a, b)$, if its PDF is given by $$f_X(x) = \begin{cases} \frac{1}{b - a} & a < x < b \\ 0 & x < a \text{ or } x > b \end{cases}$$

## Property

> [!proposition] Properties of Uniform
> Let $X \sim \mathrm{Uniform}(a, b)$
> - $E[X] = \frac{a + b}{2}.$
> - $\mathsf{Var}(X) = \frac{(b - a)^2}{12}.$
> - Median $m = \frac{a + b}{2}$

> [!proposition]
> Let $U \sim \text{Uniform}(0, 1)$ and $X = -\ln(1 - U)$. Then $X \sim \text{Exponential}(1)$.
