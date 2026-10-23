Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (Springer), chapter on elliptic curves: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[Sut17]` — A. V. Sutherland, _18.783 Elliptic Curves_, Lecture 1 (MIT, 2017): https://math.mit.edu/classes/18.783/2017/Lecture1.pdf
- `[Sut21]` — A. V. Sutherland, _18.783 Elliptic Curves_, Lecture 2: The Group Law, Weierstrass, and Edwards Equations (MIT OCW, 2021): https://ocw.mit.edu/courses/18-783-elliptic-curves-spring-2021/597144daafd05ed68ba5145a505148cc_MIT18_783S21_notes2.pdf

## Definition

> [!definition] Parameters
> - $K$: a [[Field]] of characteristic $\neq 2$. Over a field of characteristic $\neq 2, 3$ every elliptic curve can be written in the form below `[Sut17]`; in characteristic $2$ and $3$ use [[Generalized Elliptic Curves]].
> - $A, B \in K$: the coefficients.
> - $\mathcal O$: the point at infinity.

> [!definition] Elliptic Curve
> Requires:: [[Field]].
>
> ---
> An **elliptic curve** $E$ is the set of solutions to a Weierstrass equation $$E: Y^2 = X^3 + AX + B,$$ together with an extra point $\mathcal O$, where the constants $A$ and $B$ must satisfy $$4A^3 + 27B^2 \neq 0.$$
>
> `[HPS]` `[Sut17]`

### Discriminant

> [!definition] Discriminant
> The quantity $\Delta_E = -16(4A^3 + 27B^2)$ is called the **discriminant** of $E$; [HPS] calls $4A^3 + 27B^2$ itself the discriminant, and the factor $-16$ does not change whether it vanishes. The condition $\Delta_E \neq 0$ is equivalent to the condition that the cubic polynomial $X^3 + AX + B$ have no repeated roots.
>
> `[Sut17]` `[HPS]`

> [!remark]
> Curves with $\Delta_E = 0$ have singular points. The addition law does not work well on these curves. That is why we include the requirement that $\Delta_E \neq 0$ in the definition of an elliptic curve.

### Addition Law

> [!definition] Parameters
> - $P, Q \in E$: two points.
> - $L$: the line through $P$ and $Q$, or the tangent line at $P$ if $P = Q$.
> - $R = (a, b)$: the third point of $E \cap L$.
> - $n \geq 1$: an integer.

> [!definition] Addition Law
> The **addition law** on $E$ is defined as follows. Let $P$ and $Q$ be two points on $E$. Let $L$ be the line connecting $P$ and $Q$, or the tangent line to $E$ at $P$ if $P = Q$. Then the intersection of $E$ and $L$ consists of three points $P$, $Q$ and $R$, counted with appropriate multiplicities and with the understanding that $\mathcal O$ lies on every vertical line. Writing $R = (a, b)$, the sum of $P$ and $Q$ is defined to be the reflection $R' = (a, -b)$ of $R$ across the $X$-axis. This sum is denoted by $P \oplus Q$, or simply by $P + Q$.
>
> If $P = (a, b)$, we denoted the reflected point by $\ominus P = (a, -b)$, or simply by $-P$; and we define $P \ominus Q$ (or $P - Q$) to be $P \oplus (\ominus Q)$. Similarly, repeated addition is represented as multiplication of a point by an integer, $$nP = \underbrace{P + P + P + \cdots + P}_{n \text{ copies}}$$
>
> `[HPS]` `[Sut17]`

> [!algorithm] Elliptic Curve Addition Algorithm
> - $P_3 \leftarrow \mathsf{Add}(P_1, P_2)$: Deterministic point addition.
>     - **Input**: an elliptic curve $$E : y^2 = x^3 + A x + B$$ and two points $P_1, P_2 \in E$.
>     - **Output**: the point $P_1 + P_2 \in E$.
>     - **Steps**:
>         1. If $P_1 = \mathcal{O}$, return $P_2$.
>         2. If $P_2 = \mathcal{O}$, return $P_1$.
>         3. Write $$P_1 = (x_1, y_1),$$ $$P_2 = (x_2, y_2).$$
>         4. If both
>             - $x_1 = x_2$
>             - $y_1 = -y_2$
>
>             return $\mathcal{O}$.
>         5. Compute the slope $\lambda$: $$\lambda = \begin{cases} \dfrac{y_2 - y_1}{x_2 - x_1}, & \text{if } P_1 \ne P_2, \\ \dfrac{3x_1^2 + A}{2y_1}, & \text{if } P_1 = P_2. \end{cases}$$
>         6. Compute: $$\begin{aligned} x_3 &\gets \lambda^2 - x_1 - x_2, \\ y_3 &\gets \lambda(x_1 - x_3) - y_1. \end{aligned}$$
>         7. Return: $$P_1 + P_2 \gets (x_3, y_3).$$
>
> `[HPS]` `[Sut21]`

## Property

> [!theorem] Group law — the addition law makes the points of $E$ into an abelian group
> Let $E$ be an elliptic curve. The addition law makes the points of $E$ into an [[Abelian Group]].
>
> `[HPS]` `[Sut17]`

## Related

### Descendants
- [[Elliptic Curves over Finite Fields]] — $K = \mathbb F_p$: Hasse's bound, double-and-add
- [[Generalized Elliptic Curves]] — the generalized Weierstrass equation, which works in every characteristic

### Constructions
- [[Bilinear Pairings]] — the Weil and Tate pairings on the torsion points of $E$
