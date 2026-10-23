Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (2nd ed., Springer 2014), chapter on lattices: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[Reg04]` — O. Regev, _Lattices in Computer Science_, lecture notes (Tel Aviv University, Fall 2004), L1 Introduction (Thm 8, Thm 9, Cor 2): https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/introduction.pdf
- `[Gal12]` — S. D. Galbraith, _Mathematics of Public Key Cryptography_ (CUP 2012), Chapter 16 Lattices (Def 16.1.16, Ex 16.1.15, Ex 16.1.19, Thm 16.2.1–16.2.3, Def 16.2.7, Thm 16.2.9): https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch16.pdf
- `[Wei]` — E. W. Weisstein, _Pick's Theorem_, MathWorld: https://mathworld.wolfram.com/PicksTheorem.html
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

### Hadamard Ratio

> [!definition] Parameters
> - $L$: a lattice of dimension $n$ ([[Lattices]]).
> - $\mathcal B = \{\textbf{v}_1, \cdots, \textbf{v}_n\}$: a basis of $L$.

> [!definition] Hadamard Ratio of the Basis
> We define the **Hadamard ratio of the basis** $\mathcal B = \{\text{v}_1, \cdots, \text{v}_n\}$ to be the quantity $$\mathcal H(\mathcal B) = (\frac{\det L}{||\textbf{v}_1|| \; ||\textbf{v}_2|| \cdots ||\textbf{v}_n||})^{1/n}.$$ By [[Lattices#Determinant|Hadamard's inequality]], $0 < \mathcal H(\mathcal B) \leq 1$, with equality exactly for an orthogonal basis, and the closer that value is to $1$, the more orthogonal are the vectors in the basis.
>
> `[HPS]` `[Gal12 Def 16.1.16, Ex 16.1.15]` — [Gal12] uses the orthogonality defect $\prod \|\mathbf v_i\| / \det L = \mathcal H(\mathcal B)^{-n}$.

### Convex Sets

> [!definition] Parameters
> - $a \in \mathbb R^n$: the center.
> - $R > 0$: the radius.

> [!definition] Closed Ball
> For any $a \in \mathbb R^n$ and any $R > 0$, the **(closed) ball** of radius $R$ centered at $a$ is the set $$\mathbb B_R(a) = \{x \in \mathbb R^n: ||x - a|| \leq R\}.$$
>
> `[HPS]`

> [!definition] Parameters
> - $S \subseteq \mathbb R^n$: a subset.

> [!definition] Bounded, Symmetric, Convex and Closed Sets
> Let $S$ be a subset of $\mathbb R^n$.
> 1. $S$ is **bounded** if the lengths of the vectors in $S$ are bounded. Equivalently, $S$ is bounded if there is a radius $R$ such that $S$ is contained within the ball $\mathbb B_R(0)$.
> 2. $S$ is **symmetric** if for every point $a$ in $S$, the negation $-a$ is also in $S$.
> 3. $S$ is **convex** if whenever two points $a$ and $b$ are in $S$, then the entire line segment connecting $a$ to $b$ lies completely in $S$.
> 4. $S$ is **closed** if it has the following property: If $a \in \mathbb R^n$ is a point such that every ball $\mathbb B_R(a)$ contains a point in $S$, then $a$ is in $S$.
>
> `[HPS]`

### Gaussian heuristic

> [!definition] Parameters
> - $L$: a lattice of dimension $n$.

> [!definition] Gaussian Expected Shortest Length
> Let $L$ be a lattice of dimension $n$. The **Gaussian expected shortest length** is $$\sigma (L) = \sqrt{\frac{n}{2 \pi e}} (\det L)^{1/n}.$$ The **Gaussian heuristic** says that a shortest nonzero vector in a "randomly chosen lattice" will satisfy $$||\textbf{v}_{shortest}|| \approx \sigma (L).$$
>
> `[HPS]` `[Gal12 Ch. 16]`

## Property

### Hermite's Theorem

> [!theorem] Hermite's Theorem — every $n$-dimensional lattice has a nonzero vector of length at most $\sqrt n \det(L)^{1/n}$
> Every lattice $L$ of dimension $n$ contains a nonzero vector $\textbf{v} \in L$ satisfying $$||\textbf{v}|| \leq \sqrt{n} \det(L)^{1/n}.$$
>
> `[HPS]` `[Gal12 Thm 16.2.3]` `[Reg04 L1 Cor 2]`, where it is called Minkowski's first theorem.

> [!remark] Hermite's constant
> For a given dimension $n$, Hermite's constant $\gamma_n$ is the smallest value such that every lattice $L$ of dimension $n$ contains a nonzero vector $\textbf{v} \in L$ satisfying $$||\textbf{v}||^2 \leq \gamma_n \det(L)^{2/n}.$$ For large $n$ it is known that, up to factors $1 + o(1)$, $$\frac{n}{2\pi e} \leq \gamma_n \leq \frac{n}{\pi e}$$
>
> `[HPS]` `[Gal12 Def 16.2.7]`

> [!theorem] Hermite's Theorem for $n$-Dimension Lattice — every $n$-dimensional lattice has a basis with $\prod \|\mathbf v_i\| \leq n^{n/2} \det L$
> $n$-dimension lattice $L$ always has a basis $\textbf{v}_1, \dots, \textbf{v}_n$ satisfying $$||\textbf{v}_1|| \; ||\textbf{v}_2|| \cdots ||\textbf{v}_n|| \leq n^{n/2} (\det L).$$
>
> `[HPS]`
> ⚠️ CLAUDE – verify: the free sources I read give this bound only for the successive minima, $\lambda_1 \cdots \lambda_n \leq n^{n/2} \det L$ (Minkowski's second theorem, [Gal12 Thm 16.2.9]); a basis whose lengths are the $\lambda_i$ need not exist [Gal12 Ex 16.1.19], so the basis version needs its own reference.

### Minkowski's Theorem

> [!theorem] Minkowski's Theorem — a symmetric convex set of volume more than $2^n \det L$ contains a nonzero lattice vector
> Let $L \subset \mathbb R^n$ be a lattice of dimension $n$ and let $S \subset \mathbb R^n$ be a symmetric convex set whose volume satisfies $$\text{Vol}(S) > 2^n \det (L).$$ Then $S$ contains a nonzero lattice vector.
> If $S$ is also closed, then it suffices to take $\text{Vol}(S) \geq 2^n \det(L)$.
>
> `[HPS]` `[Reg04 L1 Thm 9]` `[Gal12 Thm 16.2.2]`

> [!theorem] Volume of a ball — $\text{Vol}(\mathbb B_R(a)) = \pi^{n/2} R^n / \Gamma(1 + n/2)$
> Let $\mathbb B_R(a)$ be a ball of radius $R$ in $\mathbb R^n$. Then the volume of $\mathbb B_R(a)$ is $$\text{Vol}(\mathbb B_R(a)) = \frac{\pi^{n / 2} R^n}{\Gamma (1 + n/2)}.$$ For large values of $n$, the volume of the ball $\mathbb B_R(a) \subset \mathbb R^n$ is approximately given by $$\text{Vol}(\mathbb B_R(a))^{1/n} \approx \sqrt{\frac{2 \pi e}{n}} R.$$
>
> `[HPS]`

### Blichfeldt's Theorem

> [!theorem] Blichfeldt's Theorem — a set of volume more than $\det L$ contains two distinct points whose difference lies in $L$
> Let $L \subset \mathbb R^n$ be a lattice of dimension $n$ and let $S \subseteq \mathbb R^n$ be a measurable set with $$\text{Vol}(S) > \det(L).$$ Then there exist two distinct points $\mathbf z_1, \mathbf z_2 \in S$ with $\mathbf z_1 - \mathbf z_2 \in L$.
>
> `[Reg04 L1 Thm 8]` `[Gal12 Thm 16.2.1]`

### Pick's Theorem

> [!theorem] Pick's Theorem — the area of a lattice polygon is $I + B/2 - 1$
> Let $P$ be a simple closed polygon whose vertices lie in $\mathbb Z^2$, let $I$ be the number of points of $\mathbb Z^2$ in the interior of $P$, and let $B$ be the number of points of $\mathbb Z^2$ on its edges. Then $$\text{Area}(P) = I + \tfrac{1}{2} B - 1.$$
>
> `[Wei]`

## Related

### Prerequisites
- [[Lattices]] — $\det L$, fundamental domains, Hadamard's inequality

### Siblings
- [[Lattice Smoothing]] — transference bounds, relating the successive minima of $L$ and of its dual
