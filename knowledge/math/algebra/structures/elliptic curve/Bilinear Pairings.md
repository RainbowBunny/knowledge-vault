Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (Springer), chapter on elliptic curves, sections on bilinear pairings: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[Gal12]` — S. D. Galbraith, _Mathematics of Public Key Cryptography_ (CUP 2012): Chapter 7 (Def 7.6.1, Def 7.6.3, Def 7.7.2, Cor 7.7.13, Cor 7.7.14, Thm 7.9.8), Chapter 9 (Def 9.1.2), Chapter 26 Pairings on elliptic curves (Def 26.2.2, eq. (26.1), Thm 26.2.3, §26.3, Thm 26.3.3, Def 26.3.4, Ex 26.3.5, Algorithm 29): https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch7.pdf · https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch9.pdf · https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch26.pdf
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

### Torsion Points

> [!definition] Parameters
> - $E$: an [[Elliptic Curve]] over a field $K$; points are taken over an algebraic closure of $K$, and $E(K)[m] = E[m] \cap E(K)$.
> - $m \geq 1$: an integer.

> [!definition] Torsion Points
> Requires:: [[Elliptic Curve]].
>
> ---
> Let $m \geq 1$ be an integer. A point $P \in E$ satisfying $mP = \mathcal O$ is called an **$m$-torsion point** in the group $E$; its order divides $m$ ([HPS] says *point of order $m$*). We denote the set of $m$-torsion points by $$E[m] = \{P \in E: [m]P = \mathcal O\}.$$
> Points $P$ with $mP = \mathcal O$ for some $m \geq 1$ are called **points of finite order** or **torsion points**.
>
> `[HPS]` `[Gal12 Def 9.1.2]`

> [!remark]
> $E[m]$ is a subgroup of $E$.

### Rational functions and divisors on elliptic curves

> [!definition] Parameters
> - $E$: an elliptic curve.
> - $n_P \in \mathbb Z$: coefficients, all but finitely many equal to $0$.
> - $f(X, Y)$: a nonzero rational function on $E$.
> - $\operatorname{ord}_P(f) \in \mathbb Z$: the order of $f$ at $P$ — the multiplicity of a zero, or minus the multiplicity of a pole.

> [!definition] Divisor on an elliptic curve
> A **divisor** on $E$ is a formal sum $$D = \sum_{P \in E} n_P[P]$$ with $n_P \in \mathbb Z$ and only finitely many $n_P \neq 0$. Let $f(X, Y)$ be a nonzero rational function of two variables on $E$ (the domain of the function is $E$). Then $f$ has an associated divisor $$\text{div}(f) = \sum_{P \in E} \operatorname{ord}_P(f)[P],$$ called the **divisor of** $f$, or a **principal divisor**.
>
> `[Gal12 Def 7.6.1, Def 7.7.2]` `[HPS]`

> [!definition] Degree and Sum of a divisor
> The **degree of a divisor** is the sum of its coefficients, $$\deg(D) = \deg(\sum_{P \in E} n_P[P]) = \sum_{P \in E} n_P.$$
> The **sum of a divisor** is defined by dropping the square brackets: $$\text{Sum}(D) = \text{Sum}(\sum_{P \in E} n_P [P]) = \sum_{P \in E} n_P P.$$
>
> `[HPS]` `[Gal12 Def 7.6.3]`

### Miller's Algorithm

> [!definition] Parameters
> - $E$: an elliptic curve.
> - $g_{T, P}$: for points $T, P \in E$, the line through $T$ and $P$ (the tangent line at $T$ if $T = P$) divided by the vertical line through $T + P$, so that $\text{div}(g_{T,P}) = [T] + [P] - [T + P] - [\mathcal O]$ `[Gal12 Ex 26.3.5]`.

> [!algorithm] Miller’s Algorithm for Elliptic Curves
> - $f_P \leftarrow \mathsf{Miller}(E, P, m)$: Deterministic computation of a function with prescribed divisor.
>     - **Input**: an elliptic curve $E$; a point $P \in E$; an integer $m \ge 1$ with binary expansion $$m = m_0 + m_1 2 + m_2 2^2 + \cdots + m_{n-1} 2^{n-1},$$ where $m_i \in \{0,1\}$ and $m_{n-1} = 1$.
>     - **Output**: a rational function $f_P$ satisfying $$\operatorname{div}(f_P) = m[P] - [mP] - (m-1)[\mathcal{O}].$$
>     - **Steps**:
>         1. Initialize: $$T \gets P,$$ $$f \gets 1.$$
>         2. For $i = n-2, n-3, \ldots, 0$, do:
>             1. Set: $$f \gets f^2 \cdot g_{T,T},$$ where $g_{T,T}$ is the function associated with the tangent line at $T$.
>             2. Set: $$T \gets 2T.$$
>             3. If $m_i = 1$, then set $$f \gets f \cdot g_{T,P},$$ where $g_{T,P}$ is the function associated with the line through $T$ and $P$, and then set $$T \gets T + P.$$
>         3. Return the function $f$.
>
> `[HPS]` `[Gal12 Def 26.3.4, Algorithm 29]`

### Weil pairing

> [!definition] Parameters
> - $m \geq 1$: an integer, not divisible by the characteristic of the field.
> - $P, Q \in E[m]$: two $m$-torsion points.
> - $f_P$, $f_Q$: rational functions on $E$ with the divisors below.
> - $S \in E$: an auxiliary point with $S \notin \{\mathcal O, P, -Q, P - Q\}$.

> [!definition] Weil pairing
> Let $P, Q \in E[m]$, i.e., $P$ and $Q$ are $m$-torsion points in the group $E$. Let $f_P$ and $f_Q$ be rational functions on $E$ satisfying
> $$\text{div}(f_P) = m[P] - m[\mathcal O]$$
> $$\text{div}(f_Q) = m[Q] - m[\mathcal O].$$
> The **Weil pairing** of $P$ and $Q$ is the quantity $$e_m(P, Q) = \frac{f_P(Q + S)}{f_P(S)} \Bigg / \frac{f_Q(P - S)}{f_Q(-S)},$$ where $S \in E$ is any point satisfying $S \notin \{\mathcal O, P, -Q, P - Q\}$.
>
> `[HPS]`

> [!remark] Normalization
> [Gal12 eq. (26.1)] writes $e_m(P, Q) = f_Q(D_P) / f_P(D_Q)$ with $\text{div}(f_P) = m D_P$, $\text{div}(f_Q) = m D_Q$ for divisors $D_P \sim [P] - [\mathcal O]$, $D_Q \sim [Q] - [\mathcal O]$ of disjoint support. The formula above evaluates $f_P$ at $D_Q = [Q + S] - [S]$ and $f_Q$ at $D_P = [P - S] - [-S]$, i.e. it is $f_P(D_Q) / f_Q(D_P)$, the inverse of [Gal12]'s; [Gal12 §26.2, footnote 1] notes that sources differ by this inversion.

### Tate Pairing

> [!definition] Parameters
> - $q$: a prime power.
> - $E$: an elliptic curve over $\mathbb F_q$.
> - $\ell$: a [[Prime]].
> - $P \in E(\mathbb F_q)[\ell]$, $Q \in E(\mathbb F_q)$: points.
> - $f_P$: a rational function on $E$ with $\text{div}(f_P) = \ell [P] - \ell [\mathcal O]$.
> - $S \in E(\mathbb F_q)$: an auxiliary point.

> [!definition] Tate Pairing
> Let $E$ be an elliptic curve over $\mathbb F_q$, let $\mathcal \ell$ be a prime, let $P \in E(\mathbb F_q)[\ell]$, and let $Q \in E(\mathbb F_q)$. Choose a rational function $f_P$ on $E$ with $$\text{div}(f_P) = \ell [P] - \ell [\mathcal O].$$
> The **Tate pairing** of $P$ and $Q$ is the quantity $$\tau(P, Q) = \frac{f_P(Q + S)}{f_P(S)} \in \mathbb F_q^*$$ where $S$ is any point in $E(\mathbb F_q)$ such that $f_P(Q + S)$ and $f_P(S)$ are defined and nonzero. It turns out that the value of the Tate pairing is well-defined only up to multiplying it by the $l^{\text{th}}$ power of an element of $\mathbb F_q^*$. If $q \equiv 1 \pmod l$, we defined the **(modified) Tate pairing** of $P$ and $Q$ to be $$\hat \tau (P, Q) = \tau (P, Q)^{(q - 1) / l} = (\frac{f_P(Q + S)}{f_P(S)})^{(q - 1) / l} \in \mathbb F_q^*.$$
>
> `[HPS]` `[Gal12 §26.3]` — [Gal12] defines $t_\ell : E(\mathbb F_q)[\ell] \times E(\mathbb F_q)/\ell E(\mathbb F_q) \rightarrow \mathbb F_q^*/(\mathbb F_q^*)^\ell$ and calls $\hat\tau$ the reduced Tate pairing, the exponentiation the final exponentiation.

## Property

### Structure of the torsion

> [!proposition] Structure of $E[m]$ — two copies of $\mathbb Z/m\mathbb Z$ when the characteristic does not divide $m$
> Let $m \geq 1$ be an integer.
> 1. Let $E$ be an elliptic curve over $\mathbb Q$ or $\mathbb R$ or $\mathbb C$. Then $$E(\mathbb C)[m] \cong \mathbb Z/m\mathbb Z \times \mathbb Z / m \mathbb Z$$ is a product of two cyclic groups of order $m$.
> 2. Let $E$ be an elliptic curve over $\mathbb F_p$ and assume that $p$ does not divides $m$. Then there exists a value of $k$ such that $$E(\mathbb F_{p^{jk}})[m] \cong \mathbb Z/m\mathbb Z \times \mathbb Z / m \mathbb Z \quad \forall j \geq 1.$$
>
> `[HPS]`

### Principal divisors

> [!theorem] Principal divisors — $\text{div}(f)$ determines $f$ up to a constant, and $D$ is principal iff $\deg D = 0$ and $\text{Sum}(D) = \mathcal O$
> Let $E$ be an elliptic curve.
> 1. Let $f$ and $f'$ be rational functions on $E$. If $\text{div}(f) = \text{div}(f')$, then there is a nonzero constant $c$ such that $f = c f'$.
> 2. Let $D = \sum_{P \in E} n_P [P]$ be a divisor on $E$. Then $D$ is the divisor of a rational function on $E$ if and only if both
>     - $\deg(D) = 0$
>     - $\text{Sum}(D) = \mathcal O$.
>
> In particular, if a rational function on $E$ has no zeros or no poles, then it is constant.
>
> `[HPS]` `[Gal12 Cor 7.7.13, Cor 7.7.14, Thm 7.9.8]`

### Properties of the Weil pairing

> [!theorem] Properties of the Weil pairing — values are $m$-th roots of unity; bilinear, alternating, non-degenerate
> 1. The values of the Weil pairing satisfy $$e_m(P, Q)^m = 1 \quad \forall P, Q \in E[m].$$ In other words, $e_m(P, Q)$ is an $m^{th}$ root of unity.
> 2. The Weil pairing is bilinear, which means that
>     - $$e_m(P_1 + P_2, Q) = e_m(P_1, Q) e_m (P_2, Q) \quad \forall P_1, P_2, Q \in E[m],$$
>     - $$e_m(P, Q_1 + Q_2) = e_m(P, Q_1) e_m(P, Q_2) \quad \forall P, Q_1, Q_2 \in E[m].$$
> 3. The Weil pairing is alternating, which means that $$e_m(P, P) = 1 \quad \forall P \in E[m].$$ This implies that $$e_m(P, Q) = e_m(Q, P)^{-1} \quad \forall P, Q \in E[m].$$
> 4. The Weil pairing is nondegenerate, which means that $$\text{if } e_m(P, Q) = 1 \quad \forall Q \in E[m], \text{then } P = \mathcal O.$$
>
> `[HPS]` `[Gal12 Thm 26.2.3]`

### Properties of the Tate pairing

> [!theorem] Properties of Tate pairing — bilinear, and $\hat\tau(P, P)$ is a primitive $\ell$-th root of unity
> Let $E$ be an elliptic curve over $\mathbb F_q$ and let $\ell$ be a prime with
> - $q \equiv 1 \pmod \ell$,
> - $E(\mathbb F_q)[\ell] \cong \mathbb Z / \ell \mathbb Z$.
>
> Then the modified Tate pairing gives a well-defined map $$\hat \tau : E(\mathbb F_q)[\ell] \times E(\mathbb F_q)[l] \rightarrow \mathbb F_q^*$$ having the following properties:
> 1. Bilinearity:
>     - $$\hat \tau (P_1 + P_2, Q) = \hat \tau (P_1, Q) \hat \tau (P_2, Q)$$
>     - $$\hat \tau (P, Q_1 + Q_2) = \hat \tau (P, Q_1) \hat \tau (P, Q_2).$$
> 2. Nondegeneracy: $$\hat \tau (P, P) \; \text{is a primitive } l^{\text{th}} \text{root of unity for all nonzero } P \in E(\mathbb F_q)[\ell]$$
>
> `[HPS]` `[Gal12 Thm 26.3.3]`
> ⚠️ CLAUDE – verify: if the $\ell$-part of $E(\mathbb F_q)$ is cyclic of order $\ell^2$ (allowed by the hypotheses), every $P \in E(\mathbb F_q)[\ell]$ is $\ell Q$ for some $Q \in E(\mathbb F_q)$, and bilinearity gives $\hat\tau(P, P) = \hat\tau(P, Q)^\ell = 1$. Item 2 seems to need also $\ell^2 \nmid \#E(\mathbb F_q)$; [Gal12 Thm 26.3.3] states non-degeneracy only for the pairing on $E(\mathbb F_q)[\ell] \times E(\mathbb F_q)/\ell E(\mathbb F_q)$.

## Example

> [!example] The Weil pairing in coordinates
> Let $P_1, P_2$ is a basis in a 2-dimensional "vector space" in $E[m]$, let $\zeta = e_m(P_1, P_2)$, and write $P = a_P P_1 + b_P P_2$ and $Q = a_Q P_1 + b_Q P_2$. We have $$e_m(P, Q) = \zeta^{\det(\begin{matrix}a_P & a_Q \\ b_P & b_Q\end{matrix})} = \zeta^{a_P b_Q - a_Q b_P}.$$

## Related

### Constructions
- [[Bilinear Group]] — the abstract interface that the Weil and Tate pairings instantiate
- [[Weil Pairing over Prime Power Fields]] — embedding degree, distortion maps and the modified Weil pairing

### Prerequisites
- [[Elliptic Curve]] — the group law
- [[Bilinearity]] — the property item 2 of the Weil and item 1 of the Tate pairing state
