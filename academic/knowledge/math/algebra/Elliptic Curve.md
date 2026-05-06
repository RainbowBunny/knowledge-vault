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

## Elliptic Curves over Finite Fields

> [!definition] Elliptic Curve over $\mathbb F_p$
> An **elliptic curve over** $\mathbb F_p$ is an equation of the form $$E: Y^2 = X^3 + AX + B \qquad \text{with } A, B \in \mathbb F_p \text{ satisfying } 4A^3 + 27B^2 \neq 0,$$ and then we look at the points on $E$ with coordinates in $\mathbb F_p$, which we denote by $$E(\mathbb F_p) = \{(x, y): x, y \in \mathbb F_p \text{ satisfy } y^2 = x^3 + Ax + B\} \cup \{\mathcal O\}.$$

> [!theorem]
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $P$ and $Q$ be points in $E(\mathbb F_p).$
> 1. The elliptic curve addition algorithm applied to $P$ and $Q$ yields a point in $E(\mathbb F_p)$. We denote this point by $P + Q$.
> 2. This addition law makes $E(\mathbb F_p)$ into a [[Algebra Structure#Group|Finite Group]].

> [!theorem] Hasse
> Let $E$ be an elliptic curve over $\mathbb F_p$. Then $$\#(\mathbb F_p) = p + 1 - t_p \quad \text{with } t_p \text{ satisfying } |t_p| \leq 2 \sqrt{p}.$$
> Let $E$ be an elliptic curve over $\mathbb F_{p^k}$. Then $$\#(\mathbb F_{p^k}) = p^k + 1 - t_{p^k} \quad \text{with } t_{p^k} \text{ satisfying } |t_{p^k}| \leq 2p^{k/2}.$$

> [!definition] Trace of Frobenius
> The quantity $$t_p = p + 1 - \#(\mathbb F_p)$$ is called the **trace of Frobenius** for $E / \mathbb F_p$.

> [!algorithm] Double-and-Add Algorithm for Elliptic Curves
> **Input:**  
> A point $P \in E(\mathbb{F}_p)$ and an integer $n \ge 1$
>
> **Output:**  
> The point $nP \in E(\mathbb{F}_p)$
>
> ---
>
> 1. Initialize:
>    $$Q \gets P, \qquad R \gets \mathcal{O}.$$
>
> 2. While $n > 0$, do:
>
>    2.1. If
>    $$n \equiv 1 \pmod 2,$$
>    then set:
>    $$R \gets R + Q.$$
>
>    2.2. Set:
>    $$Q \gets 2Q.$$
>
>    2.3. Set:
>    $$n \gets \lfloor n / 2 \rfloor.$$
>
> 3. Return $R$, which equals $nP$.
> ---
> **Complexity of the algorithm**: $2 \log_2 n$ point operations

> [!remark]
> The fastest known algorithm to solve ECDLP in $E(\mathbb F_p)$ takes approximately $\sqrt{p}$ steps.

## Generalized Version of Elliptic Curve

> [!definition] Generalized Elliptic Curve
> An **elliptic curve** $E$ is the set of solutions to a **generalized** Weierstrass equation $$E: Y^2 + a_1 XY + a_3 Y = X^3 + a_2 X^2 + a_4 X + a_6$$ together with an extra point $\mathcal O$. The coefficients $a_1, \dots, a_6$ are required to satisfy $\Delta \neq 0$, where the **discriminant** $\Delta$ is defined in terms of certain quantities $b_2, b_4, b_6, b_8$ as follows: 
> $$b_2 = a_1^2 + 4a_2, \quad b_4 = 2a_4 + a_1 a_3, \quad b_6 = a_3^2 + 4a_6$$
> $$b_8 = a_1^2 a_6 + 4 a_2 a_6 - a_1 a_3 a_$ + a_2 a_3^2 - a_4^2$$ 
> $$\Delta = -b_2^2 b_8 - 8b_4^3 - 27b_6^2 + 9 b_2 b_4 b_6.$$

> [!algorithm] Exercise 5.19: Point Addition on a Generalized Weierstrass Curve
> **Input**
> - An elliptic curve
>   $$
>   E : Y^2 + a_1 X Y + a_3 Y = X^3 + a_2 X^2 + a_4 X + a_6
>   $$
> - Two points $P_1 = (x_1, y_1)$ and $P_2 = (x_2, y_2)$ on $E$
>
> **Output**
> - The sum $P_3 = P_1 + P_2$
>
> ---
>
> **Step 1: Check for the Point at Infinity**
> 1. If $x_1 = x_2$ and
>    $$y_1 + y_2 + a_1 x_2 + a_3 = 0,$$
>    then
>    $$P_1 + P_2 = \mathcal{O}.$$
>
> **Step 2: Compute $\lambda$ and $\nu$**
> 2. If $x_1 \neq x_2$, define
>    $$\lambda = \frac{y_2 - y_1}{x_2 - x_1},
>    \qquad
>    \nu = \frac{y_1 x_2 - y_2 x_1}{x_2 - x_1}.$$
>
> 3. If $x_1 = x_2$, define
>    $$\lambda = \frac{3x_1^2 + 2a_2 x_1 + a_4 - a_1 y_1}
>                    {2y_1 + a_1 x_1 + a_3},$$
>    $$\nu = \frac{-x_1^3 + a_4 x_1 + 2a_6 - a_3 y_1}
>               {2y_1 + a_1 x_1 + a_3}.$$
>
> **Step 3: Compute the Sum**
> 1. Set
>    $$x_3 = \lambda^2 + a_1 \lambda - a_2 - x_1 - x_2,$$
>    $$y_3 = -(\lambda + a_1) x_3 - \nu - a_3.$$
>
> 2. Output
>    $$P_3 = (x_3, y_3).$$


> [!definition] p-power Frobenius map
> The (p-power) Frobenius map $\tau$ is the map from the field $\mathbb F_{p^k}$ to itself defined by the simple rule $$\tau: \mathbb F_{p^k} \rightarrow \mathbb F_{p^k}, \quad \tau(\alpha) = \alpha^p.$$

> [!proposition] Property of p-power Frobenius map
> The map preserves addition and multiplication: $$\tau(\alpha + \beta) = \tau(\alpha) + \tau(\beta) \quad \text{and} \quad \tau(\alpha \cdot \beta) = \tau(\alpha) \cdot \tau(\beta)$$

> [!theorem]
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $$t = p + 1 - \# E(\mathbb F_p).$$
> 1. Let $\alpha$ and $\beta$ be the complex roots of the quadratic polynomial $Z^2 - tZ + p$. Then $|\alpha| = |\beta| = \sqrt{p}$, and for every $k \geq 1$ we have $$\# E(\mathbb F_{p^k}) = p^k + 1 - \alpha^k - \beta^k.$$
> 2. Let $$\tau: E(\mathbb F_{p^k}) \rightarrow E(\mathbb F_{p^k}), \qquad (x, y) \rightarrow (x^p, y^p),$$ be the Frobenius map. Then for every point $Q \in E(\mathbb F_{p^k})$ we have $$\tau^2(Q) - t \tau(Q) + p \cdot Q = 0,$$ where $\tau^2(Q)$ denotes the composition $\tau(\tau(Q))$.

## Koblitz Curve

> [!definition] Koblitz Curve
> A **Koblitz curve** is an elliptic curve defined over $\mathbb F_2$ by an equation of the form $$E_a : Y^2 + XY = X^3 + aX + 1$$ with $a \in \{0, 1\}$. The discriminant of $E_a$ is $\Delta = 1$.

> [!example]
> For **Koblitz curve** $E_0$ over $\mathbb F_2$ is $\{(1, 0), (0, 1), (1, 1), \mathcal O\}$, we have the Frobenius map $\tau$ for $E(\mathbb F_{2^k})$ satisfies the equation $\tau^2 + \tau + 2$. The equation has root $\{\frac{-1 + \sqrt{-7}}{2}, \frac{-1 - \sqrt{-7}}{2}\}$, and we have $$E_0(\mathbb F_{2^k}) = 2^k + 1 - (\frac{-1 + \sqrt{-7}}{2})^k - (\frac{-1 - \sqrt{-7}}{2})^k$$

> [!algorithm] $\tau$-adic Expansion with $\tau^2 = -2 - \tau$
> **Input**
> - A positive integer $n$
> - An element $\tau$ satisfying $\tau^2 = -2 = \tau$
>
> **Output**
> - Coefficients $v_i \in \{-1,0,1\}$ such that
>   $$n = v_0 + v_1 \tau + v_2 \tau^2 + \cdots + v_\ell \tau^\ell$$
>
> ---
>
> 1. Set $n_0 = n$, $n_1 = 0$, and $i = 0$.
>
> 2. While $n_0 \neq 0$ or $n_1 \neq 0$, do:
>
>    2.1 If $n_0$ is odd, then:
>    $$v_i = 2 - \bigl((n_0 - 2n_1) \bmod 4\bigr)$$
>    $$n_0 = n_0 - v_i$$
>
>   2.2 Else:
>    $$v_i = 0$$
>
>   2.3 Set:
>    $$i = i + 1$$
>
>   2.4 Update:
>    $$(n_0, n_1) = \left(n_1 - \tfrac{1}{2} n_0,\; -\tfrac{1}{2} n_0\right)$$
>
> 3. Output the coefficients $v_0, v_1, \ldots, v_\ell$.
> ---
> 
> **Properties**
> 1. At most one-third of the coefficients $v_i$ are nonzero.
> 2. The length satisfies $\ell \le \log(n)$.


## Bilinear Pairings on Elliptic Curve

### Torsion Points

> [!definition] Torsion Points
> Let $m \geq 1$ be an integer. A point $P \in E$ satisfying $mP = \mathcal O$ is called a **point of order** $m$ in the group $E$. We denote the set of points of order $m$ by $$E[m] = \{P \in E: [m]P = \mathcal O\}.$$
> Such points are called **points of finite order** or **torsion points**.

> [!remark]
> $E[m]$ is a subgroup of $E$.

> [!proposition]
> Let $m \geq 1$ be an integer.
> 1. Let $E$ be an elliptic curve over $\mathbb Q$ or $\mathbb R$ or $\mathbb C$. Then $$E(\mathbb C)[m] \cong \mathbb Z/m\mathbb Z \times \mathbb Z / m \mathbb Z$$ is a product of two cyclic groups of order $m$.
> 2. Let $E$ be an elliptic curve over $\mathbb F_p$ and assume that $p$ does not divides $m$. Then there exists a value of $k$ such that $$E(\mathbb F_{p^{jk}})[m] \cong \mathbb Z/m\mathbb Z \times \mathbb Z / m \mathbb Z \quad \forall j \geq 1.$$

### Rational functions and divisors on elliptic curves

> [!definition] Divisor on an elliptic curve 
> Let $f(X, Y)$ is a rational function of two variables on $E$ (the domain of the function is $E$). Then, $f$ has an associated divisor $$D = \text{div}(f) = \sum_{P \in E} n_P[P].$$ This is called the **divisor on** $E$.
> 

> [!definition] Degree and Sum of a divisor
> The **degree of a divisor** is the sum of its coefficients, $$\deg(D) = \deg(\sum_{P \in E} n_P[P]) = \sum_{P \in E} n_P.$$
> The **sum of a divisor** is defined by dropping the square brackets: $$\text{Sum}(D) = \text{Sum}(\sum_{P \in E} n_P [P]) = \sum_{P \in E} n_P P.$$

> [!theorem] 
> Let $E$ be an elliptic curve.
> 1. Let $f$ and $f'$ be rational functions on $E$. If $\text{div}(f) = \text{div}(f')$, then there is a nonzero constant $c$ such that $f = c f'$.
> 2. Let $D = \sum_{P \in E} n_P [P]$ be a divisor on $E$. Then $D$ is the divisor of a rational function on $E$ if and only if $$\deg(D) = 0 \quad \text{and} \quad \text{Sum}(D) = \mathcal O.$$
>
> In particular, if a rational function on $E$ has no zeros or no poles, then it is constant.

> [!algorithm] Miller’s Algorithm for Elliptic Curves
> **Input:**  
> - An elliptic curve $E$  
> - A point $P \in E$  
> - An integer $m \ge 1$ with binary expansion
>   $$m = m_0 + m_1 2 + m_2 2^2 + \cdots + m_{n-1} 2^{n-1},
>   \quad m_i \in \{0,1\}$$
>
> **Output:**  
> A rational function $f_P$ satisfying
> $$\operatorname{div}(f_P) = m[P] - [mP] - (m-1)[\mathcal{O}].$$
>
> ---
>
> 1. Initialize:
>    $$T \gets P, \qquad f \gets 1.$$
>
> 2. For $i = n-2, n-3, \ldots, 0$, do:
>
>    2.1. Set:
>    $$f \gets f^2 \cdot g_{T,T},$$
>    where $g_{T,T}$ is the function associated with the tangent line at $T$.
>
>    2.2. Set:
>    $$T \gets 2T.$$
>
>    2.3. If $m_i = 1$, then:
>    - Set:
>      $$f \gets f \cdot g_{T,P},$$
>      where $g_{T,P}$ is the function associated with the line through $T$ and $P$.
>    - Set:
>      $$T \gets T + P.$$
>
> 3. Return the function $f$.

### Weil pairing

> [!definition] Weil pairing
> Let $P, Q \in E[m]$, i.e., $P$ and $Q$ are points of order $m$ in the group $E$. Let $f_P$ and $f_Q$ be rational functions on $E$ satisfying $$\text{div}(f_P) = m[P] - m[\mathcal O] \quad \text{and} \quad \text{div}(f_Q) = m[Q] - m[\mathcal O].$$
> The **Weil pairing** of $P$ and $Q$ is the quantity $$e_m(P, Q) = \frac{f_P(Q + S)}{f_P(S)} \Bigg / \frac{f_Q(P - S)}{f_Q(-S)},$$ where $S \in E$ is any point satisfying $S \notin \{\mathcal O, P, -Q, P - Q\}$.

> [!theorem] Properties of the Weil pairing
> 1. The values of the Weil pairing satisfy $$e_m(P, Q)^m = 1 \quad \forall P, Q \in E[m].$$ In other words, $e_m(P, Q)$ is an $m^{th}$ root of unity.
> 2. The Weil pairing is bilinear, which means that $$e_m(P_1 + P_2, Q) = e_m(P_1, Q) e_m (P_2, Q) \quad \forall P_1, P_2, Q \in E[m],$$ and $$e_m(P, Q_1 + Q_2) = e_m(P, Q_1) e_m(P, Q_2) \quad \forall P, Q_1, Q_2 \in E[m].$$
> 3. The Weil pairing is alternating, which means that $$e_m(P, P) = 1 \quad \forall P \in E[m].$$ This implies that $e_m(P, Q) = e_m(Q, P)^{-1} \quad \forall P, Q \in E[m].$
> 4. The Weil pairing is nondegenerate, which means that $$\text{if } e_m(P, Q) = 1 \quad \forall Q \in E[m], \text{then } P = \mathcal O.$$

> [!example]
> Let $P_1, P_2$ is a basis in a 2-dimensional "vector space" in $E[m]$, let $\zeta = e_m(P_1, P_2)$, we have $$e_m(P, Q) = \zeta^{\det(\begin{matrix}a_P & a_Q \\ b_P & b_Q\end{matrix})} = \zeta^{a_P b_Q - a_Q b_P}.$$

### Tate Pairing

> [!definition] Tate Pairing
> Let $E$ be an elliptic curve over $\mathbb F_q$, let $\mathcal \ell$ be a prime, let $P \in E(\mathbb F_q)[\ell]$, and let $Q \in E(\mathbb F_q)$. Choose a rational function $f_P$ on $E$ with $$\text{div}(f_P) = \ell [P] - \ell [\mathcal O].$$
> The **Tate pairing** of $P$ and $Q$ is the quantity $$\tau(P, Q) = \frac{f_P(Q + S)}{f_P(S)} \in \mathbb F_q^*$$ where $S$ is any point in $E(\mathbb F_q)$ such that $f_P(Q + S)$ and $f_P(S)$ are defined and nonzero. It turns out that the value of the Tate pairing is well-defined only up to multiplying it by the $l^{\text{th}}$ power of an element of $\mathbb F_q^*$. If $q \equiv 1 \pmod l$, we defined the **(modified) Tate pairing** of $P$ and $Q$ to be $$\hat \tau (P, Q) = \tau (P, Q)^{(q - 1) / l} = (\frac{f_P(Q + S)}{f_P(S)})^{(q - 1) / l} \in \mathbb F_q^*.$$

> [!theorem] Properties of Tate pairing
> Let $E$ be an elliptic curve over $\mathbb F_q$ and let $\ell$ be a prime with $$q \equiv 1 \pmod \ell \quad \text{and} \quad E(\mathbb F_q)[\ell] \cong \mathbb Z / \ell \mathbb Z.$$
> Then the modified Tate pairing gives a well-defined map $$\hat \tau : E(\mathbb F_q)[\ell] \times E(\mathbb F_q)[l] \rightarrow \mathbb F_q^*$$ having the following properties:
> 1. Bilinearity: $$\hat \tau (P_1 + P_2, Q) = \hat \tau (P_1, Q) \hat \tau (P_2, Q) \quad \text{and} \quad \hat \tau (P, Q_1 + Q_2) = \hat \tau (P, Q_1) \hat \tau (P, Q_2).$$
> 2. Nondegeneracy: $$\hat \tau (P, P) \; \text{is a primitive } l^{\text{th}} \text{root of unity for all nonzero } P \in E(\mathbb F_q)[\ell]$$

## The Weil Pairing over Fields of Prime Power Order

### Embedding degree

> [!definition] Embedding degree
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $m \geq 1$ be an integer with $p \nmid m$. The **embedding degree** of $E$ with respect to $m$ is the smallest value of $k$ such that $$E(\mathbb F_{p^k})[m] \cong \mathbb Z / m \mathbb Z \times \mathbb Z / m \mathbb Z.$$

> [!proposition]
> Let $E$ be an elliptic curve over $\mathbb F_p$ and let $\ell \neq p$ be a prime. Assume that $E(\mathbb F_p)$ contains a point of order $\ell$. Then the embedding degree of $E$ with respect to $\ell$ is given by one of the following cases:
> 1. The embedding degree of $E$ is $1$. (This cannot happen if $\ell > \sqrt{p} + 1$)
> 2. $p \equiv 1 \pmod \ell$ and the embedding degree is $\ell$.
> 3. $p \not\equiv 1 \pmod \ell$ and the embedding degree is the smallest value of $k \leq 2$ such that $$p^k \equiv 1 \pmod \ell.$$

### Distortion Maps and a Modified Weil Pairing

> [!definition] Distortion Map
> Let $\ell \geq 3$ be a prime, let $E$ be an elliptic curve, let $P \in E[\ell]$ be a point of order $\ell$, and let $\phi: E \rightarrow E$ be a map from $E$ to itself. We say that $\phi$ is a $\ell$-**distorsion map** for $P$ if it has the following two properties:
> 1. $\phi(n P) = n \phi(P) \quad \forall n \geq 1.$
> 2. The number $e_{\ell}(P, \phi(P))$ is a primitive $l^{\text{th}}$ root of unity. This means that $$e_{\ell}(P, \phi(P))^r = 1 \qquad \text{if and only if} \qquad r \text{ is a multiple of } \ell.$$

> [!proposition]
> Let $E$ be an elliptic curve, let $\ell \geq 3$ be a prime, and view $E[\ell] = \mathbb Z / \ell \mathbb Z \times \mathbb Z / \ell \mathbb Z$ as a 2-dimensional vector space over the field $\mathbb Z / \ell \mathbb Z$. Let $P, Q \in E[\ell]$. Then the following are equivalent:
> 1. $P$ and $Q$ form a basis for the vector space $E[\ell]$.
> 2. $P \neq \mathcal O$ and $Q$ is not a multiple of $P$.
> 3. $e_{\ell}(P, Q)$ is a primitive $l^{\text{th}}$ root of unity.
> 4. $e_{\ell}(P, Q) \neq 1$.

> [!definition] Modified Weil Pairing
> Let $E$ be an elliptic curve, let $P \in E[\ell]$, and let $\phi$ be an $\ell$-distortion map for $P$. The modified Weil pairing $\hat e_\ell$ on $E[\ell]$ (relative to $\phi$) is defined $$\hat e_\ell(Q, Q') = e_{\ell}(Q, \phi(Q')).$$

> [!proposition]
> Let $E$ be an elliptic curve, let $P \in E[\ell]$, let $\phi$ be an $\ell$-distorsion map for $P$, and let $\hat e_l$ be the modified Weil pairing relative to $\phi$. Let $Q$ and $Q'$ be multiples of $P$. Then $$\hat e_\ell(Q, Q') = 1 \quad \text{if and only if} \quad Q = \mathcal O \text{ or } Q' = \mathcal O.$$

### A distortion map on $y^2 = x^3 + x$

> [!proposition]
> Let $E$ be the elliptic curve $$E: y^2 = x^3 + x$$ over a field $K$ and suppose that $K$ has an element $\alpha \in K$ satisfying $\alpha^2 = -1$. Define a map $\phi$ by $$\phi(x, y) = (-x, \alpha y) \quad \text{and} \quad \phi(\mathcal O) = \mathcal O.$$
> 1. Let $P \in E(K)$. Then $\phi(P) \in E(K)$, so $\phi$ is a map from $E(K)$ to itself.
> 2. The map $\phi$ respects the addition law on $E$, $$\phi(P_1 + P_2) = \phi(P_1) + \phi(P_2) \quad \forall P_1, P_2 \in E(K).$$
> In particular, $\phi(nP) = n\phi(P) \forall P \in E(K) \text{ and all } n \geq 1.$

> [!proposition] 
> Fix the following quantities
> - A prime $p$ satisfying $p \equiv 3 \pmod 4$.
> - The elliptic curve $E: y^2 = x^3 + x$.
> - An element $\alpha \in \mathbb F_{p^2}$ satisfying $\alpha^2 = -1$.
> - The map $\phi(x, y) = (-x, \alpha y)$.
> - A prime $\ell \geq 3$ such that there exists a nonzero point $P \in E(\mathbb F_p)[\ell]$.
> 
> Then $\phi$ is an $l$-distortion map for $P$, i.e., the quantity $$\hat e_{\ell}(P, P) = e_{\ell}(P, \phi (P))$$ is a primitive $\ell^{\text{th}}$ root of unity.


