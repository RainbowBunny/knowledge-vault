
## Sine and Cosine

> [!proposition] Fundamental Properties of the Sine and Cosine
> 1. **Domain of Definition**: The sine and cosine functions are defined everywhere on the real line.
> 2. **Special values**: We have $\cos 0 = \sin \frac{1}{2} \pi = 1, \cos \pi = -1$.
> 3. **Cosine of a Difference**: For all $x$ and $y$, we have $$\cos(y - x) = \cos y \cos x + \sin y \sin x.$$
> 4. **Fundamental Inequalities**: For $0 < x < \frac{1}{2} \pi$, we have $$0 < \cos x < \frac{\sin x}{x} < \frac{1}{\cos x}.$$


| Property                          | Description                                                                                                                                                                                                                                                                              |
| --------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Pythagorean identity              | $\sin^2 x + \cos^2 x = 1 \forall x$.                                                                                                                                                                                                                                                     |
| Special values                    | $\sin 0 = \cos \frac{1}{2} \pi = \sin \pi = 0$.<br>$\sin \frac{1}{6} \pi = \frac{1}{2}, \cos \frac{1}{6} \pi = \frac{1}{2} \sqrt{3}$<br>$\sin \frac{1}{3}\pi = \frac{1}{2} \sqrt{3}, \cos \frac{1}{3} \pi = \frac{1}{2}$<br>$\sin \frac{1}{4} = \cos \frac{1}{4} = \frac{1}{2} \sqrt{2}$ |
| Even and odd properties           | The cosine is an even function and the sine is an odd function. That is, for all $x$ we have $$\cos(-x) = \cos x, \quad \sin(-x) = -\sin x.$$                                                                                                                                            |
| Co-relations                      | For all $x$, we have $$\sin(\frac{1}{2} \pi + x) = \cos x, \quad \cos(\frac{1}{2} \pi + x) = -\sin x.$$                                                                                                                                                                                  |
| Periodicity                       | For all $x$, we have $\sin(x + 2\pi) = \sin x, \cos(x + 2\pi) = \cos x$.                                                                                                                                                                                                                 |
| Addition formulas                 | For all $x$ and $y$, we have $$\begin{align}\cos(x + y) = \cos x \cos y - \sin x \sin y, \\ \sin(x + y) = \sin x \cos y + \cos x \sin y.\end{align}$$                                                                                                                                    |
| Difference formulas               | For all $a$ and $b$, we have $$\begin{align}\sin a - \sin b = 2 \sin {\frac{a - b}{2}} \cos {\frac{a + b}{2}}, \\ \cos a - \cos b = -2 \sin {\frac{a - b}{2}} \sin {\frac{a + b}{2}}. \end{align}$$                                                                                      |
| Monotonicity                      | In the interval $[0, \frac{1}{2} \pi]$, the sine is strictly increasing and the cosine is strictly decreasing.                                                                                                                                                                           |
| Double-angle/Duplication Formulas | $\sin 2x = 2 \sin x \cos x$<br>$\cos 2x = \cos^2x - \sin^2x = 1 - 2\sin^2 x = 2\cos^2x - 1$<br>$\sin 3x = 3 \sin x - 4 \sin^3 x$, $\cos 3x = 4\cos^3 x - 3 \cos x$                                                                                                                       |
|                                   | If $0 < a \leq \frac{1}{2} \pi$ and $n \geq 1$, we have $$\frac{a}{n} \sum_{k = 1}^n \cos \frac{ka}{n} < \sin a < \frac{a}{n} \sum_{k = 0}^{n - 1} \cos \frac{ka}{n}$$                                                                                                                   |
|                                   | $\tan x = \frac{\sin x}{\cos x}, \cot x = \frac{\cos x}{\sin x}, \sec x = \frac{1}{\cos x}, \csc x = \frac{1}{\sin x}$                                                                                                                                                                   |
|                                   |                                                                                                                                                                                                                                                                                          |
Useful formula

| Condition                          | Formula                                                                                                                                                                                                  |
| ---------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|                                    | $2 \sin \frac{1}{2} x \cos kx = \sin (k + \frac{1}{2})x - \sin (k - \frac{1}{2})x$<br>$2 \sin\frac{1}{2} x \sum_{k = 1}^n \cos kx = \sin(n + \frac{1}{2})x - \sin \frac{1}{2}x$                          |
|                                    | For every real $a$, $b$: $$\begin{align} \int_a^b \cos x dx = \sin x \|^b_a, \\ \int_a^b \sin x dx = -\cos x \|^b_a. \end{align}$$                                                                       |
|                                    | $\sin(x + \pi) = -\sin x$, $\cos(x + \pi) = -\cos x$                                                                                                                                                     |
| $\tan x \tan y \neq -1$            | $\tan(x - y) = \frac{\tan x - \tan y}{1 + \tan x \tan y}$                                                                                                                                                |
| $\tan x \tan y \neq 1$             | $\tan(x + y) = \frac{\tan x + \tan y}{1 - \tan x \tan y}$                                                                                                                                                |
| $\cot x + \cot y \neq 0$           | $\cot(x + y) = \frac{\cot x \cot y - 1}{\cot x + \cot y}$                                                                                                                                                |
| $\tan x \neq \tan y$               | $\cot(x - y) = \frac{1 + \tan x \tan y}{\tan x - \tan y}$                                                                                                                                                |
|                                    | $2 \cos x \cos y = \cos (x - y) + \cos (x + y)$<br>$2 \sin x \sin y = \cos(x - y) - \cos(x - y)$<br>$2 \sin x \cos y = \sin(x - y) + \sin (x + y)$                                                       |
| Integer $n \neq 0$                 | $\int_0^{2\pi} \sin nx dx = \int_0^{2\pi} \cos nx dx = 0$<br>$\int_0^{2\pi} \sin^2 nx dx = \int_0^{2\pi} \cos^2 nx dx = \pi$                                                                             |
| Integer $n, m$ that $n^2 \neq m^2$ | $\int_0^{2\pi} \sin nx \cos mx dx = \int_0^{2\pi} \sin nx \sin mx dx = \int_0^{2\pi} \cos nx \cos mx dx = 0$                                                                                             |
| $x \neq 2 m \pi$                   | $\sum_{k = 1}^n \cos kx = \frac{\sin \frac{1}{2} nx \cos \frac{1}{2} (n + 1)x}{\sin \frac{1}{2} x}$<br>$\sum_{k = 1}^n \sin kx = \frac{\sin \frac{1}{2}nx \sin \frac{1}{2} (n + 1)x}{\sin \frac{1}{2}x}$ |
|                                    | $\text{arccot } x = \frac{\pi}{2} - \arctan x$                                                                                                                                                           |
| $\|x\| \geq 1$                     | $\text{arcsec } x = \arccos \frac{1}{x}$                                                                                                                                                                 |
| $\|x\| \geq 1$                     | $\text{arccsc } x = \arcsin \frac{1}{x}$                                                                                                                                                                 |

## Hyperbolic Version

| Property | Description                                                             |
| -------- | ----------------------------------------------------------------------- |
|          | $\sinh x = \frac{e^x - e^{-x}}{2}$                                      |
|          | $\cosh x = \frac{e^x + e^{-x}}{2}$                                      |
|          | $\tanh x = \frac{\sinh x}{\cosh x} = \frac{e^x - e^{-x}}{e^x + e^{-x}}$ |
|          | $\text{csch } x = \frac{1}{\sinh x}$                                    |
|          | $\text{sech } x = \frac{1}{\cosh x}$                                    |
|          | $\coth x = \frac{1}{\tanh x}$                                           |

Useful formula 


| Condition   | Formula                                             |
| ----------- | --------------------------------------------------- |
|             | $\cosh^2 x - \sinh^2 x = 1$                         |
|             | $\sinh (-x) = -\sinh x$                             |
|             | $\cosh(-x) = \cosh(x)$                              |
|             | $\tanh(-x) = -\tanh(x)$                             |
|             | $\sinh(x + y) = \sinh x \cosh y + \cosh x \sinh y$  |
|             | $\cosh(x + y) = \cosh x \cosh y + \sinh x \sinh y$  |
|             | $\sinh 2x = 2 \sinh x \sinh y$                      |
|             | $\cosh 2x = \cosh^2 x + \sinh^2 x$                  |
|             | $\cosh x + \sinh x = e^x$                           |
|             | $\cosh x - \sinh x = e^{-x}$                        |
| Integer $n$ | $(\cosh x + \sinh x)^n = \cosh nx + \sinh nx$       |
|             | $2 \sinh^2 \frac{1}{2} x = \cosh x - 1$             |
|             | $2 \cosh^2 \frac{1}{2} x = \cosh x + 1$             |
|             | $\tanh^2 x + \text{sech}^2 x = 1$                   |
|             | $\coth^2 x - \text{csch}^2 x = 1$                   |
|             | $\cos(iy) = \cosh y$                                |
|             | $\sin(iy) = i \sinh y$                              |
|             | $\cos (x + iy) = \cos x \cosh y - i \sin x \sinh y$ |
|             | $\sin (x + iy) = \sin x \cosh y + i \cos x \sinh y$ |

## Inverse Version

$\arcsin, \arccos, \arctan$
$\text{arccot}, \text{arccsc}, \text{arcsec}$
