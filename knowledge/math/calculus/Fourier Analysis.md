## Basic Definition

> [!definition] Fourier Transform
> For a nice function $f: \mathbb R^n \rightarrow \mathbb C$, we define its Fourier transform $\hat{f}: \mathbb R^n \rightarrow \mathbb C$ as
> $$\hat{f}(y) = \int_{\mathbb R^n} f(x) e^{-2 \pi i \langle x, y \rangle} dx$$
> If $f, \hat{f}$ are nice and $f$ is continuous, we can recover function from its Fourier transform using the inverse formula:
> $$f(x) = \int_{\mathbb R^n} \hat{f}(y) e^{2 \pi i \langle x, y \rangle} dx$$

