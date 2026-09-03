## Definition

> [!definition] Fourier Transform
> For a nice function $f: \mathbb R^n \rightarrow \mathbb C$, we define its Fourier transform $\hat{f}: \mathbb R^n \rightarrow \mathbb C$ as
> $$\hat{f}(y) = \int_{\mathbb R^n} f(x) e^{-2 \pi i \langle x, y \rangle} dx$$
> If $f, \hat{f}$ are nice and $f$ is continuous, we can recover function from its Fourier transform using the inverse formula:
> $$f(x) = \int_{\mathbb R^n} \hat{f}(y) e^{2 \pi i \langle x, y \rangle} dx$$

### Gamma

> [!definition] Gamma Function
> The **gamma function** $\Gamma(\alpha)$ is defined for $\alpha > 0$ by the integral $$\Gamma(\alpha) = \int_{0}^{\infty} x^{\alpha - 1} e^{-x} dx$$

> [!proposition] Properties of the Gamma Function 
> For any positive real number $\alpha$:
> 1. $\int_0^{\infty} x^{\alpha - 1} e^{-\lambda x} dx = \frac{\Gamma(\alpha)}{\lambda^{\alpha}},$ for $\lambda > 0$;
> 2. $\Gamma(1) = 1$ and $\Gamma(\alpha + 1) = \alpha \Gamma(\alpha)$;
> 3. $\Gamma(n) = (n - 1)!$, for $n = 1, 2, 3, \cdots;$
> 4. $\Gamma(\frac{1}{2}) = \sqrt{\pi}$
> 5. **Stirling's formula**: For large values of $s$ we have $$\Gamma(1 + s)^{1/s} \approx \frac{s}{e}$$ (More precisely, $\ln \Gamma(1 + s) = \ln(s/e)^s + \frac{1}{2} \ln (2 \pi s) + O(1)$ as $s \rightarrow \infty$.)

### Bessel Function

> [!definition] Bessel Function of the first kind
> The function $J_0$ and $J_1$ defined by the series $$J_0(x) = \sum_{n = 0}^\infty (-1)^n \frac{x^{2n}}{(n!)^2 2^{2n}}, \quad J_1(x) = \sum_{n = 0}^\infty (-1)^n \frac{x^{2n + 1}}{n!(n + 1)! 2^{2n + 1}}$$ are called **Bessel functions of the first kind** of orders zero and one, respectively.

> [!proposition] Properties of the Bessel Function
> 1. $J_0$ and $J_1$ converge for all real $x$;
> 2. $J'_0(x) = -J_1(x)$
> 3. $j_0(x) = j'_1(x)$, where $j_0(x) = xJ_0(x)$ and $j_1(x) = x J_1(x)$.

> [!definition] Bessel's Equation
> The differential equation $$x^2 y'' + xy' + (x^2 - n^2)y = 0$$ is called **Bessel's equation**. Then, $J_0$ and $J_1$ are solutions when $n = 0$ and $1$, respectively.

### Dirac Delta Function

> [!definition] Unit Step Function
> The unit step function $u(x)$ defined by $$u(x) = \begin{cases}1 \quad &x \geq 0 \\ 0 & \text{otherwise}\end{cases}.$$ 
> 

> [!proposition] 
> To remove the jump, define for any $\alpha > 0$ the function $u_\alpha$ as $$u_\alpha (x) = \begin{cases}1 & x > \frac{\alpha}{2} \\ \frac{1}{\alpha} (x + \frac{\alpha}{2}) & -\frac{\alpha}{2} \leq x \leq \frac{\alpha}{2} \\ 0 & x < -\frac{\alpha}{2}\end{cases}$$
> Because $u_\alpha(x)$ is a continuous function, we can define the derivative of $u_\alpha(x)$ whenever it exists: $$\delta_\alpha(x) = \frac{du_\alpha(x)}{dx} = \begin{cases}\frac{1}{\alpha} &|x| < \frac{\alpha}{2} \\ 0 &|x| > \frac{\alpha}{2} \end{cases}$$

> [!definition] Dirac Delta Function
> We notice that $$u(x) = \lim_{\alpha \rightarrow 0} u_\alpha(x),$$ Then we can define $$\delta(x) = \lim_{\alpha \rightarrow 0} \delta_\alpha(x)$$

> [!lemma]
> Let $g: \mathbb R \rightarrow \mathbb R$ be a continuous function. We have $$\int_{-\infty}^\infty g(x) \delta(x - x_0) dx = g(x_0).$$

> [!definition] Properties of the delta function
> We define the delta function $\delta(x)$ as an object with the following properties:
> 1. $\delta(x) = \begin{cases}\infty &x = 0 \\ 0 &\text{otherwise}\end{cases}$
> 2. $\delta(x) = \frac{d}{dx} u(x)$, where $u(x)$ is the unit step function;
> 3. $\int_{-\epsilon}^\epsilon \delta(x) dx = 1$, for any $\epsilon > 0$;
> 4. For any $\epsilon > 0$ and any function $g(x)$ that is continuous over $(x_0 - \epsilon, x_0 + \epsilon)$, we have $$\int_{-\infty}^\infty g(x) \delta(x - x_0) dx = \int_{x_0 - \epsilon}^{x_0 + \epsilon} g(x) \delta(x - x_0) dx = g(x_0).$$

