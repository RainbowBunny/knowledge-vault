Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 3: Diagonalization, Section 3.4: Oracle Machines and the Limits of Diagonalization.

## Definition

> [!definition] $P^O$
> For every $O \subseteq \{0, 1\}^*$, $\mathsf{P}^O$ is the set containing every language that can be decided by a deterministic [[Oracle Turing Machine]] with oracle access to $O$ 
> 

> [!definition] $NP^O$
> $\mathsf{NP}^O$ is the set of every language that can be decided by a polynomial-time non-deterministic [[Oracle Turing Machine]] with oracle access to $O$.

## Property

> [!theorem] Baker, Gill, Solovay
> There exist oracles $A, B$ such that: 
> - $\mathsf{P}^A = \mathsf{NP}^A$.
> - $\mathsf{P}^B \neq \mathsf{NP}^B$.

