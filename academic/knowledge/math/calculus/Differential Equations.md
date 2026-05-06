
## First-order differential equation

### A first-order differential equation for the exponential function

> [!theorem]
> If $C$ is a given real number, there is one and only one function $f$ which satisfies the differential equation $$f'(x) = f(x)$$ for all real $x$ and which also satisfies the initial condition $f(0) = C$. This function is given by the formula $$f(x) = Ce^x.$$

### First-order linear differential equations

> [!definition] First-order Linear Differential Equation
> Equation in the form $$y' + P(x) y = Q(x).$$

> [!theorem] Homogeneous Linear Differential Equation
> Assume $P$ is continuous on an open interval $I$. Choose any point $a$ in $I$ and let $b$ be any real number. Then there is one and only one function $y = f(x)$ which satisfies the initial-value problem $$y' + P(x) y = 0$$ on the interval $I$. This function is given by the formula $$f(x) = be^{-A(x)}, \quad \text{where} \quad A(x) = \int_a^x P(t) dt.$$

> [!theorem]
> Assume $P$ and $Q$ are continuous on an open interval $I$. Choose any point $a$ in $I$ and let $b$ be any real number. Then there is one and only one function $y = f(x)$ which satisfies the initial-value problem $$y' + P(x) y = Q(x), \quad \text{with} \quad f(a) = b,$$ on the interval $I$. This function is given by the formula $$f(x) = b e^{-A(x)} + e^{-A(x)} \int_a^x Q(t) e^{A(t)} dt,$$ where $A(x) = \int_a^x P(t) dt$.

> [!definition] Bernoulli Equation
> A differential equation of the form $y' + P(x) y = Q(x) y^n$, where $n$ is not $0$ and $1$, is called **Bernoulli equation**. This equation is nonlinear because of the presence of $y^n$.

> [!theorem]
> Let $k$ be a nonzero constant. Assume $P$ and $Q$ are continuous on an interval $I$. If $a \in I$ and $b$ is any real number, let $v = g(x)$ be the unique solution of the initial-value problem $v' + k P(x) v = k Q(x)$ on $I$, with $g(a) = b$. If $n \neq 1$ and $k = 1 - n$, a function $y = f(x)$, which is never zero on $I$, is a solution of the initial-value problem $$y' + P(x) y = Q(x) y^n \quad \text{on} \quad I, \quad \text{with} \quad f(a)^k = b$$ if and only if the $k$th power of $f$ is equal to $g$ on $I$.

> [!theorem] Riccati Equation
> An equation of the form $y' + P(x)y + Q(x) y^2 = R(x)$ is called a **Riccati equation**. Then, if $u$ is a known solution of this equation, then there are further solutions of the form $y = u + 1/v$, for $v$ satisfies $$v' - (P + 2Qu) v = Q$$

## Second order differential equation

### Linear Equation of Second order with Constant Coefficient 

> [!definition] Linear Equation of Second Order
> A differential equation of the form $$y'' + P_1(x) y' + P_2(x) y = R(x)$$ is said to be a **linear equation of second order**.

### Case $y'' + by = 0$

> [!theorem] Reduction of the general equation to the special case $y'' + by = 0$
> Let $y$ and $u$ be two functions such that $y = ue^{-ax / 2}$. Then, on the interval $(-\infty, +\infty)$, $y$ satisfies the differential equation $y'' + a y' + by = 0$ if and only if $u$ satisfies the differential equation $$u'' + \frac{4b - a^2}{4} u = 0$$

> [!theorem] Uniqueness theorem for the equation $y'' + by = 0$
> Assume two functions $f$ and $g$ satisfy the differential equation $y'' + by = 0$ on $(-\infty, +\infty)$. Assume also that $f$ and $g$ satisfy the initial conditions $$f(0) = g(0), \quad f'(0) = g'(0).$$ Then $f(x) = g(x)$ for all $x$.

> [!theorem] Solution of the equation $y'' + by = 0$
> Given a real number $b$, define two functions $u_1$ and $u_2$ on $(-\infty, +\infty)$ as follows:
> 1. If $b = 0$, let $u_1(x) = 1, u_2(x) = x$.
> 2. If $b < 0$, write $b = -k^2$ and define $u_1(x) = e^{kx}, u_2(x) = e^{-kx}$
> 3. If $b > 0$, write $b = k^2$ and define $u_1(x) = \cos kx, u_2(x) = \sin kx$.
> Then every solution of the differential equation $y'' + by = 0$ on $(-\infty, +\infty)$ has the form $$y = c_1 u_1(x) + c_2 u_2(x),$$ where $c_1$ and $c_2$ are constants.

### Case  $y'' + ay' + by = 0$

> [!theorem]
> Let $d = a^2 - 4b$ be the discriminant of the linear differential equation $y'' + a y' + by = 0$. Then every solution of this equation on $(-\infty, +\infty)$ has the form $$y = e^{-ax/2}[c_1 u_1(x) + c_2 u_2(x)],$$ where $c_1$ and $c_2$ are constants, and the functions $u_1$ and $u_2$ are determined according to the algebraic sign of the discriminant as follows:
> 1. If $d = 0$, then $u_1(x) = 1$ and $u_2(x) = x$.
> 2. If $d > 0$, then $u_1(x) = e^{kx}$ and $u_2(x) = e^{-kx}$, where $k = \frac{1}{2} \sqrt{d}$.
> 3. If $d < 0$, then $u_1(x) = \cos kx$ and $u_2(x) = \sin kx$, where $k = \frac{1}{2} \sqrt{-d}$.

> [!definition] The Wronskian
> Given two function $u_1$ and $u_2$, the function $W$ defined by $W(x) = u_1(x) u'_2(x) - u_2(x) u'_1(x)$ is called their **Wronskian**.

> [!proposition] Properties of the Wronskian
> 1. If the Wronskian $W(x)$ of $u_1$ and $u_2$ is zero for all $x$ in an open interval $I$, quotient $\frac{u_2}{u_1}$ is constant on $I$.
> 2. Derivative $W' = u_1 u_2'' - u_2 u_1''$.

> [!proposition]
> Let $W$ be the Wronskian of two solutions $u_1, u_2$ of the differential equation $y'' + ay' + by = 0$, where $a$ and $b$ are constants.
> 1. $W$ satisfies the first-order equation $W' + aW = 0$ and hence $W(x) = W(0) e^{-ax}$.
> 2. Assume $u_1$ is not identically zero, then $W(0) = 0 \leftrightarrow W(x) = 0 \leftrightarrow u_2/u_1$ is constant.

> [!example]
> Let $v_1$ and $v_2$ be any solutions of the differential equation $y'' + ay' + by = 0$ such that $v_2/v_1$ is not constant.
> 1. Let $f(x)$ be any solution of the differential equation, constants $c_1$ and $c_2$ exist such that $$c_1 v_1(0) + c_2 v_2(0) = f(0), \quad c_1 v_1'(0) + c_2 v_2'(0) = f'(0).$$
> 2. Every solution has the form $y = c_1 v_1 + c_2 v_2$.

### Non-homogeneous linear equation of second order with constant coefficients

> [!remark]
> For these following theorem, we will analyze the solution of $$y'' + ay' + by = R$$ by defining an operator $L$: $$L(f) = f'' + af' + bf.$$

> [!theorem]
> If $y_1$ is a particular solution of the nonhomogeneous equation $L(y) = R$, the general solution is obtained by adding to $y_1$ the general solution of the corresponding homogeneous equation $L(y) = 0$.

> [!theorem]
> Let $v_1$ and $v_2$ be the solutions of the equation $L(y) = 0$. Then, the non-homogenous equation $L(y) = R$ has a particular solution $y_1$ given by the formula $$y_1(x) = t_1(x) v_1(x) + t_2(x) v_2(x),$$ where $$t_1(x) = -\int v_2(x) \frac{R(x)}{W(x)}, \quad t_2(x) = \int v_1(x) \frac{R(x)}{W(x)} dx.$$

> [!remark]
> 1. Imagine that when working in the field of function, knowing constant $R(x)$ behaves just like a numeric constant. 
> 2. Thus, if $v_1(x)$ and $v_2(x)$ is somewhat linear independent, we can assume that $y_1 = t_1 v_1 + t_2 v_2$ and reduce the problem to solve the system of equations: $$\begin{cases}v_1 t_1' + v_2 t_2' = 0 \\ v_1' t_1' + v_2 t_2' = 0\end{cases}$$ And thus we have the determinant calculated by the Wronskian: $$W(x) = \det \begin{bmatrix} v_1 & v_2 \\ v_1' & v_2' \end{bmatrix}$$

### Special methods for determining a particular solution of the non-homogenous equation $y'' + ay' + by = R$

> [!proposition] $R(x)$ is a polynomial
> If $R(x)$ is a polynomial degree $n$ then we can guess that: $$y_1(x) = \sum_{k = 0}^n a_k x^k$$ and determine the coefficients.

> [!proposition] $R(x) = p(x) e^{mx}$ with $p$ is a polynomial and $m$ is a constant. 
> In this case, we can guess $$y_1(x) = u(x) e^{mx}$$ to eliminate the exponent component.

> [!proposition]
> If $k$ is a nonzero constant, then then equation $y'' - k^2 y = R(x)$ has a particular solution $y_1$ given by $$y_1 = \frac{1}{k} \int_0^x R(t) \sinh(k(x - t)) dt$$

### First-order separable equations

> [!definition] Separable Equation
> Each separable equation can be expressed in the form $$y' = Q(x) R(y),$$ where $Q$ and $R$ are given functions.

> [!theorem]
> Let $y = Y(x)$ be any solution of the separable differential equation $$A(y) y' = Q(x)$$ such that $Y'$ is continuous on an open interval $I$. Assume that both $Q$ and the composite function $A \circ Y$ are continuous on $I$. Let $G$ be any primitive of $A$, that is, any function such that $G' = A$. Then the solution $Y$ satisfies the implicit formula $$G(Y) = \int Q(x) dx + C$$ for some constant $C$. 

### Homogenous first-order equation




## Integral Curves and Direction Fields

> [!definition] Envelope
> The envelope of a family of functions is a curve that each of its point it is tangent to one member of the family.

> [!definition] Direction Field
> A **direction field** of a differential equation is a collection of short line segments drawn tangent to the various integral curves.

 > [!definition] Isocline
 > For a first-order ODE, $$y' = F(x, y)$$ an **isocline** corresponding to slope $C$ is the curve defined by $$F(x, y) = C.$$