# Dimension

- $\propto$: equality except perhaps for a factor with dimensions,
- $\sim$: equality except perhaps for a factor without dimensions,
- $\approx$: equality except perhaps for a factor close to 1.
Problem: Guessing integrals
$\int_{-\infty}^{\infty} e^{-\alpha x^2} dx$ 
**Step 1**: **Assigning dimensions to** $\alpha$.
	Idea: Exponent is dimensionless ($a^b$ means the product of $b$ terms $a$). Then $-ax^2$ is dimensionless.
	Let $[x]$ be the dimensions of $x$, thus $[\alpha] [x]^2 = 1$ or $[\alpha] = [x]^{-2}$.
**Step 2**: **Dimensions of the integral**.
	$[x] = L$ 
	$[\alpha] = L^{-2}$ 
	$[dx] = L$
	$[\int e^{-a x^2} dx] = L$.
**Step 3: Making an $f(\alpha)$ with correct dimensions**.
	We know $[\int e^{-a x^2} dx] = f(\alpha)$ then $f(\alpha) \propto \alpha^{-\frac{1}{2}}$.
	And we can calculate dimensionless constant by $f(1)$.
Note:
- $d, \int$ is dimensionless.
- $\nabla$: $L^{-1}$

# Easy Cases

To find dimensionless constant, we can try some special but easy to solve cases.

# Lumping

**Estimating integrals**:
- **$\frac{1}{e}$ heuristic** (For exponentials): We estimate the integral by a rectangle with height is the maximum of the function and:
	- For a decaying function like $f(x) = e^{-ax}$, then we calculate the distance between the maximum point and the dropped $\frac{1}{e}$ point as the width.
	- For a peaked function, we calculate the distance between two dropped $\frac{1}{e}$ point as the width.
- **Full width at half maximum** (For peaks/pulses where tail dropped significantly): Similarly, instead of the $\frac{1}{e}$ point, we find the dropped $\frac{1}{2}$ point.
- **Stirling's approximation**: $n! \equiv \int_0^{\infty} t^n e^{-t} dt \approx n^n e^{-n} \sqrt{2 \pi n}$  

**Estimating derivatives**:
- **Secant approximation**: $\frac{df}{dx} = \frac{f(x) - f(0)}{x}$.
- **Significant-change approximation**: $\frac{df}{dx} \approx \frac{f(x + \Delta x) - f(x)}{\Delta x}$ where $\Delta x$ small.


