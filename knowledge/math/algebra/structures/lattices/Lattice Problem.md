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
