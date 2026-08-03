## Short Vectors in Lattices

> [!definition] Approximate Shortest Vector Problem ($\text{apprSVP}$)
> Let $\psi(n)$ be a function of $n$. In a lattice $L$ of dimension $n$, find a nonzero vector that is no more than $\psi(n)$ times longer than a shortest nonzero vector. In other words, if $\textbf{v}_{\text{shortest}}$ is a shortest nonzero vector in $L$, find a nonzero vector $\textbf{v} \in L$ satisfying $$||\textbf{v}|| \leq \psi(n)||\textbf{v}_{\text{shortest}}||.$$ Each choice of function $\psi(n)$ gives a different $\text{apprSVP}$. As specific examples, one might ask for an algorithm that finds a nonzero $\textbf{v} \in L$ satisfying $$||\textbf{v}|| \leq 3 \sqrt{n} ||\textbf{v}_{\text{shortest}}|| \quad \text{or} \quad ||\textbf{v}|| \leq 2^{n / 2} ||\textbf{v}_{\text{shortest}}||.$$ 

> [!remark]
> 1. If $\gamma_1 \geq \gamma_2$ then $\text{SVP}_{\gamma_1} \leq \text{SVP}_{\gamma_2}$.
> 2. $\text{SVP}_\gamma$ is NP-hard for constant $\gamma$.
> 3. If $\gamma > 2^{\frac{n \log \log n}{\log n}}$, then $\text{SVP}_\gamma$, then $\text{SVP}_\gamma$ can be efficiently solved (using LLL-BKZ).

> [!definition] The Shortest Independent Vector Problem
> Given $L \subseteq \mathbb R^n$, find $n$ linearly independent lattice vectors, each of length $\leq \lambda_n(L)$.

> [!definition] Approximate Shortest Independent Vector Problem (Approx-SIVP)
> Given $L \subset \mathbb R^n$ and $\gamma \geq 1$, find $n$ linear independent lattice vectors of length $\leq \gamma \lambda_n(L)$.

## Hermite's Theorem

> [!theorem] Hermite's Theorem
> Every lattice $L$ of dimension $n$ contains a nonzero vector $\textbf{v} \in L$ satisfying $$||\textbf{v}|| \leq \sqrt{n} \det(L)^{1/n}.$$

> [!remark]
> For a given dimension $n$, Hermite's constant $\gamma_n$ is the smallest value such that every lattice $L$ of dimension $n$ contains a nonzero vector $\textbf{v} \in L$ satisfying $$||\textbf{v}||^2 \leq \gamma_n \det(L)^{2/n}.$$ It is known that $$\frac{n}{2\pi e} \leq \gamma_n \leq \frac{n}{\pi e}$$

> [!theorem] Hermite's Theorem for $n$-Dimension Lattice
> $n$-dimension lattice $L$ always has a basis $\textbf{v}_1, \dots, \textbf{v}_n$ satisfying $$||\textbf{v}_1|| \; ||\textbf{v}_2|| \cdots ||\textbf{v}_n|| \leq n^{n/2} (\det L).$$

> [!definition] Hadamard Ratio of the Basis 
> We define the **Hadamard ratio of the basis** $\mathcal B = \{\text{v}_1, \cdots, \text{v}_n\}$ to be the quantity $$\mathcal H(\mathcal B) = (\frac{\det L}{||\textbf{v}_1|| \; ||\textbf{v}_2|| \cdots ||\textbf{v}_n||})^{1/n}.$$ By the Hermite's Theorem, $0 < \mathcal H(\mathcal B) < 1$, and the closer that value is to $1$, the more orthogonal are the vectors in the basis.

## Minkowski's Theorem

> [!definition] Closed Ball
> For any $a \in \mathbb R^n$ and any $R > 0$, the **(closed) ball** of radius $R$ centered at $a$ is the set $$\mathbb B_R(a) = \{x \in \mathbb R^n: ||x - a|| \leq R\}.$$

> [!definition]
> Let $S$ be a subset of $\mathbb R^n$.
> 1. $S$ is **bounded** if the lengths of the vectors in $S$ are bounded. Equivalently, $S$ is bounded if there is a radius $R$ such that $S$ is contained within the ball $\mathbb B_R(0)$.
> 2. $S$ is **symmetric** if for every point $a$ in $S$, the negation $-a$ is also in $S$.
> 3. $S$ is **convex** if whenever two points $a$ and $b$ are in $S$, then the entire line line segment connecting $a$ to $b$ lies completely in $S$.
> 4. $S$ is **closed** if it has the following property: If $a \in \mathbb R^n$ is a point such that every ball $\mathbb B_R(a)$ contains a point in $S$, then $a$ is in $S$.

> [!theorem] Minkowski's Theorem
> Let $L \subset \mathbb R^n$ be a lattice of dimension $n$ and let $S \subset \mathbb R^n$ be a symmetric convex set whose volume satisfies $$\text{Vol}(S) > 2^n \det (L).$$ Then $S$ contains a nonzero lattice vector.
> If $S$ is also closed, then it suffices to take $\text{Vol}(S) \geq 2^n \det(L)$.

> [!theorem]
> Let $\mathbb B_R(a)$ be a ball of radius $R$ in $\mathbb R^n$. Then the volume of $\mathbb B_R(a)$ is $$\text{Vol}(\mathbb B_R(a)) = \frac{\pi^{n / 2} R^n}{\Gamma (1 + n/2)}.$$ For large values of $n$, the volume of the ball $\mathbb B_R(a) \subset \mathbb R^n$ is approximately given by $$\text{Vol}(\mathbb B_R(a))^{1/n} \approx \sqrt{\frac{2 \pi e}{n}} R.$$

## Gaussian heuristic

> [!definition]
> Let $L$ be a lattice of dimension $n$. The **Gaussian expected shortest length** is $$\sigma (L) = \sqrt{\frac{n}{2 \pi e}} (\det L)^{1/n}.$$ The **Gaussian heuristic** says that a shortest nonzero vector in a "randomly chosen lattice" will satisfy $$||\textbf{v}_{shortest}|| \approx \sigma (L).$$

## Blichfeldt's Theorem


## Pick's Theorem

## Babai's Algorithm

> [!algorithm] Babai’s Closest Vertex Algorithm
> **Input:**  
> - A lattice $L \subset \mathbb{R}^n$ with basis $(v_1, v_2, \ldots, v_n)$  
> - A target vector $w \in \mathbb{R}^n$
>
> **Output:**  
> A lattice vector $v \in L$ approximating the closest lattice vector to $w$
>
> ---
>
> 1. Express the target vector in the basis:
>    $$w = t_1 v_1 + t_2 v_2 + \cdots + t_n v_n,$$
>    where $t_1, t_2, \ldots, t_n \in \mathbb{R}$.
>
> 2. For each $i = 1, 2, \ldots, n$, set:
>    $$a_i \gets \lfloor t_i \rceil,$$
>    where $\lfloor \cdot \rceil$ denotes rounding to the nearest integer.
>
> 3. Return the lattice vector:
>    $$v \gets a_1 v_1 + a_2 v_2 + \cdots + a_n v_n.$$

### LLL-Based Approximate CVP Algorithm

> [!algorithm] LLL-Based Approximate CVP Algorithm
> **Input:**  
> - A lattice $L \subset \mathbb{R}^n$ given by a basis $(v_1, v_2, \ldots, v_n)$  
> - A target vector $w \in \mathbb{R}^n$
>
> **Output:**  
> A lattice vector $v \in L$ such that
> $$\|w - v\| \le C^n \cdot \min_{u \in L} \|w - u\|,$$
> for some absolute constant $C > 1$
>
> ---
>
> 1. Apply the LLL lattice reduction algorithm to the basis
>    $$(v_1, v_2, \ldots, v_n)$$
>    to obtain an LLL-reduced basis.
>
> 2. Using the LLL-reduced basis, apply Babai’s closest vertex algorithm
>    to compute a lattice vector $v \in L$ close to the target vector $w$.
>
> 3. Return the lattice vector $v$.

