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