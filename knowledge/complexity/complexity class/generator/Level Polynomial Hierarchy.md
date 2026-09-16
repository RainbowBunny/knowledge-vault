Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 5: The polynomial hierarchy and alternations, Section 5.1: The Class $\Sigma_2^p$; Section 5.2: The Polynomial Hierarchy; Section 5.3: Alternating Turing Machines..

## Definition

> [!definition] Class $\Sigma_2^p$
> The class $\Sigma_2^p$ is the set of all [[Language]] $\mathcal{L}$ for which there exists a polynomial-time [[Turing Machine]] $M$ and a polynomial $q$ such that:
> $$\forall x \in \{0, 1\}^*: x \in \mathcal{L} \iff \exists u \in \{0, 1\}^{q(|x|)} \; \forall v \in \{0, 1\}^{q(|x|)} M(x, u, v) = 1$$

> [!definition] Class $\Sigma_i^p$
> For $i \geq 1$, a [[Language]] $\mathcal{L} \in \Sigma_i^p$ if there exist a polynomial time [[Turing Machine]] $M$ and a polynomial $q$ such that:
> $$x \in L \iff \exists u_1 \in \{0, 1\}^{q(|x|)} \; \forall u_2 \in \{0, 1\}^{q(|x|)} \cdots Q_i u_i \in \{0, 1\}^{q(|x|)} M(x, u_1, \dots, u_i) = 1$$
> where $Q_i$ denotes $\forall$ or $\exists$ depending on whether $i$ is even or odd, respectively.

> [!definition] Class $\Pi_i^p$
> Requires:: [[Complement Class]]
> 
> ---
> For every $i$, define $\Pi_i^p = \mathsf{co} \mbox{-} \Sigma_i^p$

## Property

> [!proposition]
> Requires:: [[Class NP]], [[Class coNP]]
> 
> ---
> - $\Sigma_1^p = \mathsf{NP}$.
> - $\Pi_1^p = \mathsf{coNP}$.
> - $\Sigma_i^p \subseteq \Pi_{i + 1}^p \subseteq \Sigma_{i + 2}^p$.

> [!proposition]
> Requires:: [[Class PiTIME]], [[Class SigmaTIME]]
> 
> ---
> For every $i \in \mathbb{N}$:
> - $\Sigma_i^p = \cup_c \Sigma_i \mathsf{TIME}(n^c)$.
> - $\Pi_i^p = \cup_c \Pi_i \mathsf{TIME}(c^c)$.

