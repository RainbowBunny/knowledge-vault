Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.3: IP = PSPACE.

## Definition

> [!definition] $\# \mathsf{SAT}_D$
> $\# \mathsf{SAT}_D = \{\langle \phi, K \rangle: \phi \text{ is a 3CNF formula and it has exactly } K \text{ satisfying assignments}\}$

## Property

> [!theorem]
> Requires:: [[Class IP]], [[Arithmetization of a Boolean formula]], [[Sum-Check Protocol]].
> 
> ---
> $\# \mathsf{SAT}_\mathsf{D} \in \mathsf{IP}$. 
> 
> ---
> Given input $\langle \phi, K \rangle$, where $\phi$ is a 3CNF formula of $n$ variables and $m$ clauses.
> Choose a finite field $\mathbb{F}$. We can construct $P_\phi$ by [[Arithmetization of a Boolean formula]], then:
> $$K = \sum_{b_1 \in \{0, 1\}} \cdots \sum_{b_n \in \{0, 1\}} P_\phi(b_1, \dots, b_n).$$
> And we have an [[Probabilistic Interactive Proof System]] by [[Sum-Check Protocol]].


