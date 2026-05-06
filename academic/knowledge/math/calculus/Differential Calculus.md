
## Derivative of a function

> [!definition] Derivative
> The **derivative** $f'(x)$ is defined by the equation $$f'(x) = \lim_{h \rightarrow 0} \frac{f(x + h) - f(x)}{h},$$ provided the limit exists. The number $f'(x)$ is also called the rate of change of $f$ at $x$.

> [!remark]
> The process of calculating $f'$ from a given function $f$ is called **differentiation** and $f'$ is called the **first derivative** of $f$. If we can compute the derivative of $f'$ denote by $f''$, we called it the **second derivative**. Similarly, the $n$th derivative of $f$ denoted by $f^{(n)}$ is defined to be the first derivative of $f^{(n - 1)}$.

> [!proposition] Continuity of functions having derivaties
> If a function $f$ has a derivative at a point $x$, then it is also continuous at $x$.


## Property

| Condition                                                                | Description                                                  |
| ------------------------------------------------------------------------ | ------------------------------------------------------------ |
|                                                                          | $(f + g)' = f' + g'$                                         |
|                                                                          | $(f - g)' = f' - g'$                                         |
|                                                                          | $(f \cdot g)' = f \cdot g' + g \cdot f'$                     |
| At points $x$ where $g(x) \neq 0$.                                       | $(\frac{f}{g})' = \frac{g \cdot f' - f \cdot g'}{g^2}$       |
| Real numbers $c_1, c_2$.                                                 | $(c_1 f' + c_2 g)' = c_1 f' + c_2 g'$                        |
|                                                                          | $(\frac{1}{g})' = -\frac{g'}{g^2}$                           |
| For $g = f_1 \cdots f_n$                                                 | $\frac{g'(x)}{g(x)} = \sum_{i = 1}^n \frac{f_i'(x)}{f_i(x)}$ |
| $f$ strictly increasing and continuous on $[a, b]$<br>$g$ inverse of $f$ | $g'(y) = \frac{1}{f'(x)}$                                    |
|                                                                          |                                                              |

## Chain Rule for Differentiating Composite Functions

> [!theorem] Chain Rule
> Let $f$ be the composition of two functions $u$ and $v$, say $f = u \circ v$. Suppose that both derivatives $v'(x)$ and $u'(y)$ exist, where $y = v(x)$. Then the derivative $f'(x)$ also exists and is given by the formula $$f'(x) = u'(y) \cdot v'(x).$$

> [!example] Implicit Differentiation
> 

## Extreme values of function

> [!definition] Relative Maximum
> A function $f$, defined on a set $S$, is said to have a **relative maximum** at a point $c$ in $S$ if there is some open interval $I$ containing $c$ such that $$f(x) \leq f(c) \; \forall x \in I \cap S.$$
> The concept of **relative minimum** is similarly defined by reversing the inequality.

> [!definition] Extremum
> A number which is either a relative maximum or a relative minimum of a function $f$
 is called an **extreme value** or an extremum of $f$.

> [!definition] Vanish of the Derivative at an Interior Extremum
> Let $f$ be defined on an open interval $I$, and assume that $f$ has a relative maximum or a relative minimum at an interior point $c$ of $I$. If the derivative $f'(c)$ exists, then $f'(c) = 0.$

## Mean-Value Theorem

> [!theorem] Rolle's Theorem
> Let $f$ be a function which is continuous everywhere on a closed interval $[a, b]$ and has a derivative at each point of the open interval $(a, b)$. Also, assume that $$f(a) = f(b).$$ Then there is at least one point $c$ in the open interval $(a, b)$ such that $f'(c) = 0$.

> [!theorem] Mean-Value Theorem for Derivaties
> Assume that $f$ is continuous everywhere on a closed interval $[a, b]$ and has a derivative at each point of the open interval $(a, b)$. Then there is at least one interior point $c$ of $(a, b)$ for which $$f(b) - f(a) = f'(c) (b - a).$$

> [!remark]
> $h(x) = f(x) (b - a) - x [f(b) - f(a)]$

> [!theorem] Cauchy's Mean-Value Formula
> Let $f$ and $g$ be two functions continuous on a closed interval $[a, b]$ and having derivatives in the open interval $(a, b)$. Then, for some $c$ in $(a, b)$, we have $$f'(c)[g(b) - g(a)] = g'(c) [f(b) - f(a)].$$

> [!remark]
> $h(x) = f(x) [g(b) - g(a)] - g(x) [f(b) - f(a)]$

> [!example]
> The mean-value formula can be expressed in the form $$f(x + h) = f(x) + hf'(x + \theta h) \quad \text{where} \; 0 < \theta < 1.$$

> [!example]
> A function $f$, continuous on $[a, b]$, has a second derivative $f''$ everywhere on the open interval $(a, b)$. The line segment joining $(a, f(a))$ and $(b, f(b))$ intersects the graph of $f$ at a third point $(c, f(c))$, where $a < c < b$. Then, $f''(t) = 0$ for at least one point $t$ in $(a, b)$.

## Application of the Mean-Value Theorem

> [!theorem]
> Let $f$ be a function which is continuous on a closed interval $[a, b]$ and assume $f$ has a derivative at each point of the open interval $(a, b)$. Then we have:
> 1. If $f'(x) > 0$ for every $x$ in $(a, b)$, $f$ is strictly increasing on $[a, b]$;
> 2. If $f'(x) < 0$ for every $x$ in $(a, b)$, $f$ is strictly decreasing on $[a, b]$;
> 3. If $f'(x) = 0$ for every $x$ in $(a, b)$, $f$ is constant throughout $[a, b]$.

> [!theorem]
> Assume $f$ is continuous on a closed interval $[a, b]$ and assume that the derivative $f'$ exists everywhere in the open interval $(a, b)$, except possibly at a point $c$.
> 1. If $f'(x)$ is positive for all $x < c$ and negative for all $x > c$, then $f$ has a relative maximum at $c$.
> 2. If, on the other hand, $f'(x)$ is negative for all $x < c$ and positive for all $x > c$, then $f$ has a relative minimum at $c$.

## Second-derivative Test for Extrema

> [!definition] Critical Point
> For a function $f$ is continuous on a closed interval $[a, b]$, if $f$ has a derivative at each interior point, then the only places where extrema can occur are:
> 1. At the endpoints $a$ and $b$;
> 2. At those interior points $x$ where $f'(x) = 0$ (**Critical Points**).

> [!theorem] Second-Derivative Test for an Extremum at a Critical Point
> Let $c$ be a critical point of $f$ in an open interval $(a, b)$; that is, assume $a < c < b$ and $f'(c) = 0$. Assume also that the second derivative $f''$ exists in $(a, b)$. Then we have the following:
> 1. If $f''$ is negative in $(a, b)$, $f$ has a relative maximum at $c$.
> 2. If $f''$ is positive in $(a, b)$, $f$ has a relative minimum at $c$.

## Partial Derivatives

> [!definition] Partial Derivative
> Consider a surface described by an equation of the form $z = f(x, y)$. For a point $(x_0, y_0)$, the **partial derivative** of $f$ with respect to $x$ at $(x_0, y_0)$ is defined as $$f'_x(x_0, y_0) = \lim_{h \rightarrow 0} \frac{f(x_0 + h, y_0) - f(x_0, y_0)}{h}.$$ Similarly, the **partial derivative** of $f$ with respect to $y$ at $(x_0, y_0)$ is defined by the equation $$f'_y(x_0, y_0) = \lim_{k \rightarrow 0} \frac{f(x_0, y_0 + k) - f(x_0, y_0)}{k}.$$

## The zero-derivative theorem

> [!theorem] Zero-Derivative Theorem
> If $f'(x) = 0$ for each $x$ in an open interval $I$, then $f$ is constant on $I$.



## Common Derivative

| Condition                | Function                        | Derivative                                |
| ------------------------ | ------------------------------- | ----------------------------------------- |
|                          | $f(x) = c$                      | $f'(x) = 0$                               |
|                          | $f(x) = mx + b$                 | $f'(x) = m$                               |
|                          | $s(x) = \sin x$                 | $s'(x) = \cos x$                          |
|                          | $c(x) = \cos x$                 | $c'(x) = -\sin x$                         |
| $n \in \mathbb Z^+$      | $f(x) = \sum_{k = 0}^n c_k x^k$ | $f'(x) = \sum_{k = 0}^n k c_k x^{k - 1}$  |
| $r \in \mathbb Q \neq 0$ | $f(x) = x^r$                    | $f'(x) = r x^{r - 1}$                     |
|                          | $f(x) = \tan x$                 | $f'(x) = \sec^2 x$                        |
|                          | $f(x) = \cot x$                 | $f'(x) = -\csc^2 x$                       |
|                          | $f(x) = \sec x$                 | $f'(x) = \tan x \sec x$                   |
|                          | $f(x) = \csc x$                 | $f'(x) = -\cot x \csc x$                  |
|                          | $g(x) = \ln \|f(x)\|$           | $g'(x) = \frac{f'(x)}{f(x)}$              |
|                          | $f(x) = \sinh x$                | $f'(x) = \cosh x$                         |
|                          | $f(x) = \cosh x$                | $f'(x) = \sinh x$                         |
|                          | $f(x) = \tanh x$                | $f'(x) = \text{sech}^2 x$                 |
|                          | $f(x) = \coth x$                | $f'(x) = -\text{csch}^2 \text{ } x$       |
|                          | $f(x) = \text{sech } x$         | $f'(x) = -\text{sech } x \tanh x$         |
|                          | $f(x) = \text{csch } x$         | $f'(x) = -\text{csch } x \coth x$         |
|                          | $f(x) = \arcsin x$              | $f'(x) = \frac{1}{\sqrt{1 - x^2}}$        |
| $-1 < x < 1$             | $f(x) = \arccos x$              | $f'(x) = \frac{-1}{\sqrt{1 - x^2}}$       |
|                          | $f(x) = \arctan x$              | $f'(x) = \frac{1}{1 + x^2}$               |
|                          | $f(x) = \text{arccot } x$       | $f'(x) = \frac{-1}{1 + x^2}$              |
| $\|x\| > 1$              | $f(x) = \text{arcsec } x$       | $f'(x) = \frac{1}{\|x\| \sqrt{x^2 - 1}}$  |
| $\|x\| > 1$              | $f(x) = \text{arccsc } x$       | $f'(x) = \frac{-1}{\|x\| \sqrt{x^2 - 1}}$ |
|                          |                                 |                                           |
|                          |                                 |                                           |
|                          |                                 |                                           |
