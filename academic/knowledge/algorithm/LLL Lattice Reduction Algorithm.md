## Gaussian Lattice Reduction

> [!algorithm] Gaussian Lattice Reduction (2D)
> **Input:**  
> A two-dimensional lattice $L \subset \mathbb{R}^2$ with basis vectors
> $(v_1, v_2)$
>
> **Output:**  
> A reduced basis $(v_1, v_2)$ for $L$, where $v_1$ is a shortest nonzero lattice vector. Further, the angle $\theta$ between $v_1$ and $v_2$ satisfies $|\cos \theta| \leq \frac{||v_1||}{||2v_2||}$, so in particular, $\frac{\pi}{3} \leq \theta \leq \frac{2\pi}{3}$
>
> ---
>
> 1. Loop:
>
>    1.1. If
>    $$\|v_2\| < \|v_1\|,$$
>    then swap $v_1$ and $v_2$.
>
>    1.2. Compute:
>    $$m \gets \left\lfloor \frac{\langle v_1, v_2 \rangle}{\|v_1\|^2} \right\rceil.$$
>
>    1.3. If $m = 0$, return the basis $(v_1, v_2)$.
>
>    1.4. Replace:
>    $$v_2 \gets v_2 - m v_1.$$
>
>    1.5. Continue the loop.

## LLL Reduced

> [!definition] LLL Reduced
> Let $\mathcal B = \{v_1, v_2, \dots, v_n\}$ be a basis for a lattice $L$ and let $\mathcal B^* = \{v_1^*, v_2^*, \dots, v_n^*\}$ be the associated Gram-Schmidt orthogonal basis. The basis $\mathcal B$ is said to be **LLL reduced** if it satisfies the two following two conditions:
> - (**Size Condition**): $|\mu_{i, j}| = \frac{|v_i \cdot v_j^*|}{||v_j^*||^2} \leq \frac{1}{2}$ for all $1 \leq j < i \leq n$. (Gram Schmidt coefficient is small).
> - (**Lovasz Condition**): $||v_i^*||^2 \geq (\frac{3}{4} - \mu_{i, i - 1}^2) ||v_{i - 1}^*||^2$ for all $1 < i \leq n$. (because $||v_i||$ is decreased, so we want it to not decreasing two fast).

> [!theorem]
> Let $L$ be a lattice of dimension $n$. Any LLL reduced basis $\{v_1, v_2, \dots, v_n\}$ for $L$ has the following two properties: $$\begin{align}
> \prod_{i = 1}^n ||v_i|| &\leq 2^{n(n - 1)/4} \det L, \\
> ||v_j|| &\leq 2^{(i - 1)/2} ||v_i^*|| \forall 1 \leq j \leq i \leq n.
> \end{align}$$
> Further, the initial vector in an LLL reduced satisfies $$||v_1|| \leq 2^{(n - 1)/4} |\det L|^{1/n} \quad \text{and} \quad ||v_1|| \leq 2^{(n - 1)/2} \min_{0 \neq v \in L} ||v||.$$ Thus an LLL reduced basis solves $\text{apprSVP}$ to within a factor of $2^{(n - 1)/2}$.

## LLL Lattice Reduction Algorithm

> [!algorithm] LLL Lattice Reduction Algorithm
> **Input:**  
> A basis $(v_1, v_2, \ldots, v_n)$ for a lattice $L$
>
> **Output:**  
> An LLL-reduced basis $(v_1, v_2, \ldots, v_n)$ for $L$
>
> ---
>
> 1. Set:
>    $$k \gets 2.$$
>
> 2. Set:
>    $$v_i^{*} \gets v_i \quad \text{for } i = 1, \ldots, n,$$
>    where $(v_1^{*}, \ldots, v_n^{*})$ are the Gram–Schmidt orthogonalized
>    vectors.
>
> 3. While $k \le n$, do:
>
>    3.1. (**Size reduction**)  
>    For $j = k-1, k-2, \ldots, 1$, set:
>    $$v_k \gets v_k - \left\lfloor \mu_{k j} \right\rceil v_j,$$
>    where
>    $$\mu_{k j} = \frac{\langle v_k, v_j^{*} \rangle}{\langle v_j^{*}, v_j^{*} \rangle}.$$
>
>    3.2. (**Lovász condition**)  
>    If
>    $$\|v_k^{*}\|^2 \ge \left(\frac{3}{4} - \mu_{k,k-1}^2\right)\|v_{k-1}^{*}\|^2,$$
>    then set:
>    $$k \gets k + 1.$$
>
>    3.3. (**Swap step**)  
>    Otherwise:
>    - Swap $v_{k-1}$ and $v_k$.
>    - Set:
>      $$k \gets \max(k-1, 2).$$  
>
> 4. Return the LLL-reduced basis $(v_1, v_2, \ldots, v_n)$.

> [!theorem]
> Let $\{v_1, \dots, v_n\}$ be a basis for a lattice $L$. The algorithm terminates in a finite number of steps and returns an LLL reduced basis for $L$.
> More precisely, let $B = \max ||v_i||$. Then the algorithm executes the main $k$ loop no more than $\mathcal O(n^2 \log n + n^2 \log B)$ times. In particular, the LLL algorithm is a polynomial-time algorithm.

As with Gauss, its simple to find a lattice basis $B = [b_1, \dots, b_n]$, for which $|\mu_{i, j}| \leq \frac{1}{2}$. The new basis vectors are nearly orthogonal, but not necessarily short. For a randomly selected $B$, we expect the GS vectors $b_1^*, \cdots, b_n^*$ to decrease in length very quickly.
The LLL algorithm repeated "swaps" two basis vectors, to reduce the rate at since $vol(L)$ is a lattice invariant, and $\text{vol}(L) = \prod_{i = 1}^n ||b_i^*||$.

## Korkin-Zolotarev (KZ) Reduced

> [!definition] Projection Map
> For any list of vectors $v_1, v_2, \dots$ and any $i \geq 1$, let $v_1^*, v_2^*, \dots$ denote the associated Gram-Schmidt orthogonalized vectors and define a map $$\pi: L \rightarrow \mathbb R^n, \quad \pi_i(v) = v - \sum_{j = 1}^i \frac{v \cdot v_j^*}{||v_j^*||^2} v_j^*.$$ Geometrically, we may describe $\pi_i$ as the projection map $$\pi_i : L \rightarrow \text{Span}(v_1, \dots, v_i)^{\perp} \subset \mathbb R^n$$ from $L$ onto the orthogonal complement of the space spanned by $v_1, \dots, v_i$.

> [!definition] Korkin-Zolotarev Reduced
> Let $L$ be a lattice. A basis $v_1, \dots, v_n$ for $L$ is called **Korkin-Zolotarev (KZ) reduced** if it satisfies the following three conditions:
> 1. $v_1$ is a shortest nonzero vector in $L$.
> 2. For $i = 2, 3, \dots, n,$ the vector $v_i$ is chosen such that $\pi_{i - 1}(v_i)$ is the shortest nonzero vector in $\pi_{i - 1}(L)$.
> 3. For all $1 \leq i < j \leq n,$ we have $|\pi_{i - 1}(v_i) \cdot \pi_{i - 1}(v_j)| \leq ||\pi_{i - 1}(v_i)||^2$.

> [!definition] Block Korkin-Zolotarev
> Work with a block of vectors of length $\beta$, the KZ version is $\beta = 2$.

> [!theorem]
> If the BKZ-LLL algorithm is run on a lattice $L$ of dimension $n$ using blocks of size $\beta$, then the algorithm is guaranteed to terminate in no more than $O(\beta^{c \beta} n^d)$ steps, where $c$ and $d$ are small constants. Further, the smallest vector $v_1$ found by the algorithm is guaranteed to satisfy $$||v_1|| \leq (\frac{\beta}{\pi e})^{\frac{n - 1}{\beta - 1}} \min_{0 \neq v \in L} ||v||$$

