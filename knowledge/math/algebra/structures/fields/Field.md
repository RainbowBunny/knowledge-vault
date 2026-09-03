## Definition

> [!definition] Field
> A field is a [[Commutative Ring]] with $1 \neq 0$ in which every nonzero element has a multiplicative [[Inverse Element|inverse]] (or being a [[knowledge/math/algebra/structures/rings/Ring#Unit|Unit]]).

> [!proposition]
> Every field is an [[Integral Domain]].

| Property                            | Description                                                                                                                                                                                                                                                   |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Cancellation Law for Addition       | $a + b = a + c$, then $b = c$                                                                                                                                                                                                                                 |
| Possibility of Subtraction          | Given $a$ and $b$, there is exactly one $x$ such that $a + x = b$. This $x$ is denoted by $b - a$. In particular, $0 - a$ is written simply $-a$ and is called the negative of $a$.                                                                           |
|                                     | $b - a = b + (-a)$                                                                                                                                                                                                                                            |
|                                     | $-(-a) = a$                                                                                                                                                                                                                                                   |
|                                     | $a(b - c) = ab - ac$                                                                                                                                                                                                                                          |
|                                     | $0 \cdot a = a \cdot 0 = 0$                                                                                                                                                                                                                                   |
| Cancellation Law for Multiplication | If $ab = ac$ and $a \neq 0$, then $b = c$                                                                                                                                                                                                                     |
| Possibility of Division             | Given $a$ and $b$ with $a \neq 0$, there is exactly one $x$ such that $ax = b$. This $x$ is denoted by $b / a$ or $\frac{b}{a}$ and is called the quotient of $b$ and $a$. In particular, $1/a$ is also written $a^{-1}$ and is called the reciprocal of $a$. |
|                                     | If $a \neq 0$, then $b / a = b \cdot a^{-1}$                                                                                                                                                                                                                  |
|                                     | If $a \neq 0$, then $(a^{-1})^{-1} = a$                                                                                                                                                                                                                       |
|                                     | If $ab = 0$, then $a = 0$ or $b = 0$                                                                                                                                                                                                                          |
|                                     | $(-a)b = -(ab)$ and $(-a)(-b) = ab$                                                                                                                                                                                                                           |
|                                     | $(a/b) + (c/d) = (ad + bc)/(bd)$ if $b \neq 0$ and $d \neq 0$                                                                                                                                                                                                 |
|                                     | $(a/b)/(c/d) = (ad)/bc$ if $b \neq 0$, $c \neq 0$ and $d \neq 0$                                                                                                                                                                                              |
|                                     | $-0 = 0$                                                                                                                                                                                                                                                      |
|                                     | $0$ has no reciprocal                                                                                                                                                                                                                                         |
|                                     | $-(a + b) = -a - b$                                                                                                                                                                                                                                           |
|                                     | $-(a - b) = -a + b$                                                                                                                                                                                                                                           |
|                                     | $(a - b) + (b - c) = (a - c)$                                                                                                                                                                                                                                 |
|                                     | If $a \neq 0$ and $b \neq 0$, then $(ab)^{-1} = a^{-1} b^{-1}$                                                                                                                                                                                                |
|                                     | $-(a/b) = (-a/b) = a/(-b)$ if $b \neq 0$                                                                                                                                                                                                                      |
|                                     | $(a/b) - (c/d) = (ad-bc)/(bd)$ if $b \neq 0$ and $d \neq 0$                                                                                                                                                                                                   |

## Characteristic 

> [!definition] 
> The characteristic of a ring $R$ is the least positive integer $n$ s.t $nr = 0$ for all $r \in R$

> [!theorem]
> The characteristic of an integral domain is either prime or zero

## Finite Fields

> [!theorem]
> $\mathbb Z_m$ is a field if and only if $m$ is a prime.

> [!theorem]
> Let $\mathbb F_p$ be a finite field.
> 1. For every $d \geq 1$ there exists an irreducible polynomial $m \in \mathbb F_p[x]$ of degree $d$.
> 2. For every $d \geq 1$ there exists a finite field with $p^d$ elements.
> 3. If $\mathbb F$ and $\mathbb F'$ are finite fields with the same number of elements, then $\mathbb F$ and $\mathbb F'$ are isomorphic.

> [!theorem] 
> Let $\mathbb F$ be a finite field having $q$ elements. Then $\mathbb F$ has a primitive root, i.e., there is an element $g \in \mathbb F$ such that $$\mathbb F^* = \{1, g, g^2, g^3, \dots, g^{q - 2}\}.$$

> [!example]
> If $p \equiv 3 \pmod 4$, then the field with $p^2$ elements looks like $$\mathbb F_{p^2} = \{a + bi : a, b \in \mathbb F_p\},$$ where $i$ satisfies $i^2 = -1$.

> [!definition] Characteristic of the field
> Based on the previous definition of characteristic [[Field#Characteristic]], one can derive the characteristic for finite field $\mathbb{F}_p$ is $p$

> [!lemma]
> For every element $\beta$ of a finite field $\mathbb F$ with $q$ elements, we have $\beta^q = \beta$.

> [!corollary]
> Let $F$ be a subfield of $E$ with $|F| = q$. Then an elements $\beta$ of $E$ lies in $F$ if and only if $\beta^q = \beta$.
 
> [!definition] Galois Fields
> We write $\mathbb F_{p^d}$ for a field with $p^d$ elements. We know that any two fields with $p^d$ elements are essentially the same. These fields are also sometimes called **Galois fields** and denoted by $\text{GF}(p^d)$.

> [!definition] Order
> The **order** of a nonzero element $\alpha \in \mathbb F_q$, denoted by $\text{ord}(\alpha)$, is the smallest positive integer $k$ such that $\alpha^k = 1$.

> [!lemma]
> 1. The order $\text{ord}(\alpha)$ divides $q - 1$ for every $\alpha \in \mathbb F_q^*$.
> 2. For two nonzero elements $\alpha, \beta \in \mathbb F_q^*$, if $\gcd(\text{ord}(\alpha), \text{ord}(\beta)) = 1$, then $\text{ord}(\alpha \beta) = \text{ord}(\alpha) \times \text{ord}(\beta)$.

### Extension FIeld

> [!definition] Trace Function
> $\text{Tr}(x) = \sum_{l = 0}^{m - 1} x^{q^l}, x \in \mathbb F_{q^m}$.

## Complex Field

> [!definition] Complex Number
> A **complex number** is an ordered pair $(a, b)$, where $a, b \in \mathbb R$, but we will write this as $a + bi$ where $i^2 = -1$. The set of all complex numbers is denoted by $\mathbb C$: $$\mathbb C = \{a + bi : a, b \in \mathbb R\}.$$

> [!proposition]
> Addition and multiplication on $\mathbb C$ are defined by:
> $$\begin{align}(a + bi) + (c + di) = (a + c) + (b + d) i \\ (a + bi)(c + di) = (ac - bd) + (ad + bc)i \end{align}$$

> [!definition] Real Part, Imaginary Part
> Suppose $z = a + bi$, where $a$ and $b$ are real numbers. Then $a$ is called the **real part** of $z$, denoted $\text{Re } z$, and $b$ is called the **imaginary part** of $z$, denoted $\text{Im } z$. Thus for every complex number $z$, we have $$z = \text{Re } z + (\text{Im } z) i.$$

> [!definition] Complex Conjugate
> The **complex conjugate** of $z \in \mathbb C$, denoted by $\overline z$, is defined by $$\overline z = \text{Re } z - (\text{Im } z) i.$$

> [!definition] Polar Coordinates
> If point $(x, y) \neq (0, 0)$, we can express $x$ and $y$ in polar coordinates, $$x = r \cos \theta, \quad y = r \sin \theta$$ and we obtain $$x + iy = r(\cos \theta + i \sin \theta).$$ And thus we have the **modulus** or **absolute value** $$|x + iy| = \sqrt{x^2 + y^2}.$$ And the polar angle $\theta$ is the **argument** of $x + iy$.

> [!proposition]
> Let $w = (az + b) / (cz + d)$, where $a, b, c$ and $d$ are real. Then, $$w - \overline{w} = (ad - bc)(z - \overline{z})/|cz + d|^2.$$ If $ad - bc > 0$, then the imaginary parts of $z$ and $w$ have the same sign.

### Complex Exponentials

> [!definition] Complex Exponential
> If $z = x + iy$, we define $e^z$ to be the complex number given by the equation $$e^z = e^x (\cos y + i \sin y).$$

> [!theorem]
> If $a$ and $b$ are complex numbers, we have $$e^a e^b = e^{a + b}.$$

> [!theorem]
> Every complex number $z \neq 0$ can be expressed in the form $$z = r e^{i \theta}$$ where $r = |z|$ and $\theta = \text{arg}(z) + 2n \pi$, $n$ being any integer. This representation is called the polar form of $z$.

### Complex-valued Functions

> [!definition] Derivative, Integral of Complex-valued Function
> If $f = u + iv$, we say $f$ is continuous at a point if both $u$ and $v$ are continuous at that point. The derivative of $f$ is defined by the equation $$f'(x) = u'(x) + iv'(x)$$ whenever both derivatives $u'(x)$ and $v'(x)$ exist. Similarly, we define the integral of $f$ by the equation $$\int_a^b f(x) dx = \int_a^b u(x) dx + i \int_a^b v(x) dx$$ whenever both integrals on the right exist.

> [!theorem]
> If $f(x) = e^{tx}$ for all real $x$ and a fixed complex $t$, then $f'(x) = te^{tx}$.

> [!theorem]
> Consider the differential equation $$y'' + ay' + by = 0,$$ where $a$ and $b$ are real constants. The real and imaginary parts of the function $f$ defined on $(-\infty, +\infty)$ by the equation $f(x) = e^{tx}$ are solutions of the differential equation if and only if $t$ is a root of the characteristic equation $$t^2 + at + b = 0.$$

### Complex Fomula


| Condition           | Property           | Description                                                                                          |
| ------------------- | ------------------ | ---------------------------------------------------------------------------------------------------- |
| If $\theta$ is real |                    | $\cos \theta = \frac{e^{i\theta} + e^{-i\theta}}{2}$, $\sin \theta = \frac{e^{i \theta} - e^{}}{2i}$ |
| If $\theta$ is real | DeMoivre's Theorem | $(\cos \theta + i \sin \theta)^n = \cos n\theta + i \sin n\theta$                                    |
|                     |                    |                                                                                                      |
