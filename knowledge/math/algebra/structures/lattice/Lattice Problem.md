Reference:
- `[HPS]` — J. Hoffstein, J. Pipher, J. H. Silverman, _An Introduction to Mathematical Cryptography_ (2nd ed., Springer 2014), chapter on lattices: https://link.springer.com/book/10.1007/978-1-4939-1711-2
- `[Pei16]` — C. Peikert, _A Decade of Lattice Cryptography_ (2016), §2.2.2 Computational Problems (Def 2.2.2–2.2.4): https://eprint.iacr.org/2015/939.pdf
- `[HR12]` — I. Haviv, O. Regev, _Tensor-based Hardness of the Shortest Vector Problem to within Almost Polynomial Factors_, Theory of Computing 8 (2012), §1: https://arxiv.org/abs/1806.04087

## Definition

> [!definition] Parameters
> - $L \subset \mathbb R^n$: a lattice of dimension $n$ ([[Lattices]]).
> - $\psi(n) \geq 1$: the approximation factor, a function of $n$; also written $\gamma$, and $\text{SVP}_\gamma$ is $\text{apprSVP}$ with $\psi(n) = \gamma$ `[Pei16 Def 2.2.2]`.
> - $\textbf{v}_{\text{shortest}}$: a shortest nonzero vector of $L$, of length $\lambda_1(L)$ ([[Lattices#Successive Minima]]).
> - $\lambda_n(L)$: the $n$-th successive minimum of $L$.

### Short Vectors in Lattices

> [!definition] Approximate Shortest Vector Problem ($\text{apprSVP}$)
> Let $\psi(n)$ be a function of $n$. In a lattice $L$ of dimension $n$, find a nonzero vector that is no more than $\psi(n)$ times longer than a shortest nonzero vector. In other words, if $\textbf{v}_{\text{shortest}}$ is a shortest nonzero vector in $L$, find a nonzero vector $\textbf{v} \in L$ satisfying $$||\textbf{v}|| \leq \psi(n)||\textbf{v}_{\text{shortest}}||.$$ Each choice of function $\psi(n)$ gives a different $\text{apprSVP}$. As specific examples, one might ask for an algorithm that finds a nonzero $\textbf{v} \in L$ satisfying one of
> - $$||\textbf{v}|| \leq 3 \sqrt{n} ||\textbf{v}_{\text{shortest}}||$$
> - $$||\textbf{v}|| \leq 2^{n / 2} ||\textbf{v}_{\text{shortest}}||.$$
>
> `[HPS]` `[Pei16 Def 2.2.2]`

> [!definition] The Shortest Independent Vector Problem
> Given $L \subseteq \mathbb R^n$, find $n$ linearly independent lattice vectors, each of length $\leq \lambda_n(L)$.
>
> `[Pei16 Def 2.2.4]` (with $\gamma = 1$)

> [!definition] Approximate Shortest Independent Vector Problem (Approx-SIVP)
> Given $L \subset \mathbb R^n$ and $\gamma \geq 1$, find $n$ linear independent lattice vectors of length $\leq \gamma \lambda_n(L)$.
>
> `[Pei16 Def 2.2.4]`

## Claim

> [!remark] Hardness and algorithms
> 1. If $\gamma_1 \geq \gamma_2$ then $\text{SVP}_{\gamma_1} \leq \text{SVP}_{\gamma_2}$.
> 2. $\text{SVP}_\gamma$ is NP-hard for every constant $\gamma$, under randomized reductions (Khot) `[HR12 §1]`.
> 3. For $\gamma = 2^{\Theta(n \log \log n / \log n)}$, $\text{SVP}_\gamma$ can be efficiently solved (using LLL-BKZ) `[Pei16 §2.2.2]`.

## Related

### Prerequisites
- [[Lattices]] — the successive minima $\lambda_1, \lambda_n$; facts about exact SVP in [[Lattices#Shortest Vectors]]
- [[Lattice Bounds]] — Hermite's theorem and the Gaussian heuristic estimate $\lambda_1(L)$

### Constructions
- [[LLL Lattice Reduction Algorithm]] — solves $\text{apprSVP}$ within $2^{(n-1)/2}$
- [[LLL-Based Approximate CVP algorithm]] — the closest-vector analogue, within $C^n$
