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
