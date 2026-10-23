Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (2nd ed., Springer 2014), chapter on lattices: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[Reg04]` — O. Regev, _Lattices in Computer Science_, lecture notes (Tel Aviv University, Fall 2004), L2 The LLL algorithm (Def 1–2, Claim 1, Remark 4, §2–3): https://cims.nyu.edu/~regev/teaching/lattices_fall_2004/ln/lll.pdf
- `[Gal12]` — S. D. Galbraith, _Mathematics of Public Key Cryptography_ (CUP 2012), Chapter 17 Lattice Reduction (Def 17.1.1, Thm 17.1.2, Def 17.2.4, Lem 17.2.8, Thm 17.2.12, Algorithm 25, Thm 17.5.1); Chapter 18 (Def 18.5.1): https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch17.pdf · https://www.math.auckland.ac.nz/~sgal018/crypto-book/ch18.pdf
- `[HaPS11]` — G. Hanrot, X. Pujol, D. Stehlé, _Analyzing Blockwise Lattice Algorithms using Dynamical Systems_ (CRYPTO 2011), §1–2: https://www.iacr.org/archive/crypto2011/68410441/68410441.pdf
- `[Wal20]` — M. Walter, _Lattice Blog Reduction – Part I: BKZ_, Simons Institute blog (2020): https://blog.simons.berkeley.edu/?p=146

## Definition

### Gaussian Lattice Reduction

> [!algorithm] Gaussian Lattice Reduction (2D)
> - $(v_1, v_2) \leftarrow \mathsf{GaussReduce}(v_1, v_2)$: Deterministic two-dimensional lattice reduction.
>     - **Input**: a basis $(v_1, v_2)$ of a two-dimensional lattice $L \subset \mathbb{R}^2$.
>     - **Output**: a reduced basis $(v_1, v_2)$ for $L$, where $v_1$ is a shortest nonzero lattice vector. Further, the angle $\theta$ between $v_1$ and $v_2$ satisfies
>         - $|\cos \theta| \leq \frac{\|v_1\|}{2\|v_2\|}$,
>         - so in particular, $\frac{\pi}{3} \leq \theta \leq \frac{2\pi}{3}$.
>     - **Steps**:
>         1. Loop:
>             1. If $$\|v_2\| < \|v_1\|,$$ then swap $v_1$ and $v_2$.
>             2. Compute: $$m \gets \left\lfloor \frac{\langle v_1, v_2 \rangle}{\|v_1\|^2} \right\rceil.$$
>             3. If $m = 0$, return the basis $(v_1, v_2)$.
>             4. Replace: $$v_2 \gets v_2 - m v_1.$$
>             5. Continue the loop.
>
> `[HPS]` `[Gal12 Def 17.1.1, Thm 17.1.2]` — [Gal12] calls the output Lagrange–Gauss reduced and shows $\|v_1\| = \lambda_1$, $\|v_2\| = \lambda_2$.

### LLL Reduced

> [!definition] Parameters
> - $L$: a lattice of dimension $n$.
> - $\mathcal B = \{v_1, v_2, \dots, v_n\}$: a basis of $L$.
> - $\mathcal B^* = \{v_1^*, v_2^*, \dots, v_n^*\}$: its Gram–Schmidt orthogonal basis.
> - $\mu_{i,j} = \frac{v_i \cdot v_j^*}{\|v_j^*\|^2}$: the Gram–Schmidt coefficients, $1 \leq j < i \leq n$.

> [!definition] LLL Reduced
> Let $\mathcal B = \{v_1, v_2, \dots, v_n\}$ be a basis for a lattice $L$ and let $\mathcal B^* = \{v_1^*, v_2^*, \dots, v_n^*\}$ be the associated Gram-Schmidt orthogonal basis. The basis $\mathcal B$ is said to be **LLL reduced** if it satisfies the two following two conditions:
> - (**Size Condition**): $|\mu_{i, j}| = \frac{|v_i \cdot v_j^*|}{||v_j^*||^2} \leq \frac{1}{2}$ for all $1 \leq j < i \leq n$. (Gram Schmidt coefficient is small).
> - (**Lovasz Condition**): $||v_i^*||^2 \geq (\frac{3}{4} - \mu_{i, i - 1}^2) ||v_{i - 1}^*||^2$ for all $1 < i \leq n$. (because $||v_i||$ is decreased, so we want it to not decreasing too fast).
>
> `[HPS]` `[Reg04 L2 Def 2]` `[Gal12 Def 17.2.4]` — both with a parameter $\delta$ in place of $\frac34$; $\delta = \frac34$ is the traditional choice.

### LLL Lattice Reduction Algorithm

> [!algorithm] LLL Lattice Reduction Algorithm
> - $(v_1, \dots, v_n) \leftarrow \mathsf{LLL}(v_1, \dots, v_n)$: Deterministic lattice basis reduction.
>     - **Input**: a basis $(v_1, v_2, \ldots, v_n)$ for a lattice $L$.
>     - **Output**: an LLL-reduced basis $(v_1, v_2, \ldots, v_n)$ for $L$.
>     - **Steps**: throughout, $(v_1^*, \ldots, v_n^*)$ are the Gram–Schmidt vectors of the *current* basis and $\mu_{k j} = \frac{\langle v_k, v_j^{*} \rangle}{\langle v_j^{*}, v_j^{*} \rangle}$; they are updated whenever the basis changes.
>         1. Set: $$k \gets 2.$$
>         2. Set: $$v_1^{*} \gets v_1.$$
>         3. While $k \le n$, do:
>             1. (**Size reduction**) For $j = k-1, k-2, \ldots, 1$, set: $$v_k \gets v_k - \left\lfloor \mu_{k j} \right\rceil v_j.$$
>             2. (**Lovász condition**) If $$\|v_k^{*}\|^2 \ge \left(\frac{3}{4} - \mu_{k,k-1}^2\right)\|v_{k-1}^{*}\|^2,$$ then set: $$k \gets k + 1.$$
>             3. (**Swap step**) Otherwise: swap $v_{k-1}$ and $v_k$, and set: $$k \gets \max(k-1, 2).$$
>         4. Return the LLL-reduced basis $(v_1, v_2, \ldots, v_n)$.
>
> `[HPS]` `[Reg04 L2 §2]` `[Gal12 Algorithm 25]`

### Korkin-Zolotarev (KZ) Reduced

> [!definition] Parameters
> - $v_1, v_2, \dots$: a list of vectors in $\mathbb R^n$, spanning a lattice $L$.
> - $v_1^*, v_2^*, \dots$: the associated Gram–Schmidt vectors.
> - $i \geq 1$: an index.

> [!definition] Projection Map
> For any list of vectors $v_1, v_2, \dots$ and any $i \geq 1$, let $v_1^*, v_2^*, \dots$ denote the associated Gram-Schmidt orthogonalized vectors and define a map
> $$\pi_i: L \rightarrow \mathbb R^n,$$
> $$\pi_i(v) = v - \sum_{j = 1}^i \frac{v \cdot v_j^*}{||v_j^*||^2} v_j^*.$$
> Geometrically, we may describe $\pi_i$ as the projection map $$\pi_i : L \rightarrow \text{Span}(v_1, \dots, v_i)^{\perp} \subset \mathbb R^n$$ from $L$ onto the orthogonal complement of the space spanned by $v_1, \dots, v_i$.
>
> `[HPS]`

> [!definition] Korkin-Zolotarev Reduced
> Let $L$ be a lattice. A basis $v_1, \dots, v_n$ for $L$ is called **Korkin-Zolotarev (KZ) reduced** if it satisfies the following three conditions:
> 1. $v_1$ is a shortest nonzero vector in $L$.
> 2. For $i = 2, 3, \dots, n,$ the vector $v_i$ is chosen such that $\pi_{i - 1}(v_i)$ is the shortest nonzero vector in $\pi_{i - 1}(L)$.
> 3. For all $1 \leq i < j \leq n,$ we have $|\pi_{i - 1}(v_i) \cdot \pi_{i - 1}(v_j)| \leq \frac{1}{2} ||\pi_{i - 1}(v_i)||^2$.
>
> `[HPS]` `[Gal12 Def 18.5.1]` — condition 3 is the size condition $|\mu_{j,i}| \leq \frac12$, since $\pi_{i-1}(v_i) = v_i^*$.

> [!definition] Block Korkin-Zolotarev
> Work with a block of vectors of length $\beta$: BKZ slides a window of $\beta$ consecutive vectors along the basis and calls an SVP (KZ) solver on each projected block; a full pass is a *tour*, repeated until the basis no longer changes. Block size $\beta = 2$ gives (a version of) LLL; $\beta = n$ solves SVP in the whole lattice.
>
> `[HPS]` `[Wal20]`

## Property

### Bounds for an LLL-reduced basis

> [!theorem] LLL bounds — an LLL-reduced basis is nearly orthogonal and $v_1$ solves $\text{apprSVP}$ within $2^{(n-1)/2}$
> Let $L$ be a lattice of dimension $n$. Any LLL reduced basis $\{v_1, v_2, \dots, v_n\}$ for $L$ has the following two properties: $$\begin{align}
> \prod_{i = 1}^n ||v_i|| &\leq 2^{n(n - 1)/4} \det L, \\
> ||v_j|| &\leq 2^{(i - 1)/2} ||v_i^*|| \quad \forall 1 \leq j \leq i \leq n.
> \end{align}$$
> Further, the initial vector in an LLL reduced satisfies
> - $$||v_1|| \leq 2^{(n - 1)/4} |\det L|^{1/n}$$
> - $$||v_1|| \leq 2^{(n - 1)/2} \min_{0 \neq v \in L} ||v||.$$
>
> Thus an LLL reduced basis solves $\text{apprSVP}$ to within a factor of $2^{(n - 1)/2}$.
>
> `[HPS]` `[Gal12 Lem 17.2.8, Thm 17.2.12]` `[Reg04 L2 Claim 1, Rem 4]`

### Running time

> [!theorem] LLL runs in polynomial time — the main loop runs $\mathcal O(n^2 \log n + n^2 \log B)$ times
> Let $\{v_1, \dots, v_n\}$ be a basis for a lattice $L$. The algorithm terminates in a finite number of steps and returns an LLL reduced basis for $L$.
> More precisely, let $B = \max ||v_i||$. Then the algorithm executes the main $k$ loop no more than $\mathcal O(n^2 \log n + n^2 \log B)$ times. In particular, the LLL algorithm is a polynomial-time algorithm.
>
> `[HPS]` `[Reg04 L2 §3]` — [Gal12 Thm 17.5.1] gives $\mathcal O(n^2 \log X)$ iterations when every $\|v_i\|^2 \leq X$.

> [!remark] Intuition
> As with Gauss, its simple to find a lattice basis $B = [b_1, \dots, b_n]$, for which $|\mu_{i, j}| \leq \frac{1}{2}$. The new basis vectors are nearly orthogonal, but not necessarily short. For a randomly selected $B$, we expect the GS vectors $b_1^*, \cdots, b_n^*$ to decrease in length very quickly.
> The LLL algorithm repeated "swaps" two basis vectors, to reduce the rate at since $vol(L)$ is a lattice invariant, and $\text{vol}(L) = \prod_{i = 1}^n ||b_i^*||$.

### Block Korkin-Zolotarev

> [!theorem] BKZ approximation factor — the first vector is within $\gamma_\beta^{(n-1)/(\beta-1)}$ of the shortest
> If the BKZ-LLL algorithm is run on a lattice $L$ of dimension $n$ using blocks of size $\beta$ until it terminates, the smallest vector $v_1$ found by the algorithm satisfies $$||v_1|| \leq \gamma_\beta^{\frac{n - 1}{\beta - 1}} \min_{0 \neq v \in L} ||v||,$$ where $\gamma_\beta$ is Hermite's constant ([[Lattice Bounds#Hermite's Theorem]]). For large $\beta$, $\gamma_\beta \lesssim \beta/(\pi e)$, which gives the form $(\frac{\beta}{\pi e})^{\frac{n-1}{\beta-1}}$.
> No reasonable bound is known on the number of calls to the $\beta$-dimensional SVP solver before BKZ terminates, and in practice it does not seem to be polynomially bounded; a variant stopped after polynomially many tours keeps a comparable guarantee.
>
> `[Wal20]` `[HaPS11 §1]`; the asymptotic bound on $\gamma_\beta$ is `[Gal12 Def 16.2.7]`.

## Related

### Constructions
- [[LLL-Based Approximate CVP algorithm]] — runs [[Babai's Algorithm]] on the LLL-reduced basis

### Prerequisites
- [[Lattices]] — bases, $\det L$
- [[Lattice Bounds]] — Hermite's constant $\gamma_\beta$ in the BKZ bound
- [[Lattice Problem]] — $\text{apprSVP}$, which LLL solves within $2^{(n-1)/2}$
