## Elliptic Curves

> [!definition] Elliptic Curve
> An **elliptic curve** $E$ is the set of solutions to a Weierstrass equation $$E: Y^2 = X^3 + AX + B,$$ together with an extra point $\mathcal O$, where the constants $A$ and $B$ must satisfy $$4A^3 + 27B^2 \neq 0.$$

> [!definition] Discriminant
> The quantity $\Delta_E = 4A^3 + 27B^2$ is called the **discriminant** of $E$. The condition $\Delta_E \neq 0$ is equivalent to the condition that the cubic polynomial $X^3 + AX + B$ have no repeated roots.

> [!proposition] Addition Law
> The **addition law** on $E$ is defined as follows. Let $P$ and $Q$ be two points on $E$. Let $L$ be the line connecting $P$ and $Q$, or the tangent line to $E$ at $P$ if $P = Q$. Then the intersection of $E$ and $L$ consists of three points $P$, $Q$ and $R$, counted with appropriate multiplicities and with the understanding that $\mathcal O$ lies on every vertical line. Writing $R = (a, b)$, the sum of $P$ and $Q$ is defined to be the reflection $R' = (a, -b)$ of $R$ across the $X$-axis. This sum is denoted by $P \oplus Q$, or simply by $P + Q$.
> 
> If $P = (a, b)$, we denoted the reflected point by $\ominus P = (a, -b)$, or simply by $-P$; and we define $P \ominus Q$ (or $P - Q$) to be $P \oplus (\ominus Q)$. Similarly, repeated addition is represented as multiplication of a point by an integer, $$nP = \underbrace{P + P + P + \cdots + P}_{n \text{ copies}}$$

> [!remark]
> Curves with $\Delta_E = 0$ have singular points. The addition law does not work well on these curves. That is why we include the requirement that $\Delta_E \neq 0$ in the definition of an elliptic curve.

> [!theorem] 
> Let $E$ be an elliptic curve. The addition law makes the point of $E$ into an [[Algebra Structure#Group|Abelian Group]]

> [!algorithm] Elliptic Curve Addition Algorithm
> **Input:**  
> An elliptic curve
> $$E : y^2 = x^3 + A x + B$$
> and two points $P_1, P_2 \in E$
>
> **Output:**  
> The point $P_1 + P_2 \in E$
>
> ---
>
> 1. If $P_1 = \mathcal{O}$, return $P_2$.
>
> 2. If $P_2 = \mathcal{O}$, return $P_1$.
>
> 3. Write
>    $$P_1 = (x_1, y_1), \qquad P_2 = (x_2, y_2).$$
>
> 4. If
>    $$x_1 = x_2 \quad \text{and} \quad y_1 = -y_2,$$
>    return $\mathcal{O}$.
>
> 5. Compute the slope $\lambda$:
>    $$\lambda =
>    \begin{cases}
>      \dfrac{y_2 - y_1}{x_2 - x_1}, & \text{if } P_1 \ne P_2, \\
>      \dfrac{3x_1^2 + A}{2y_1}, & \text{if } P_1 = P_2.
>    \end{cases}$$
>
> 6. Compute:
>    $$\begin{aligned}
>    x_3 &\gets \lambda^2 - x_1 - x_2, \\
>    y_3 &\gets \lambda(x_1 - x_3) - y_1.
>    \end{aligned}$$
>
> 7. Return:
>    $$P_1 + P_2 \gets (x_3, y_3).$$
