Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.3.1: Arithmetization.

## Definition

> [!definition] Arithmetization of a Boolean Formula
> ### Scope
> A [[Boolean Formula]] $\varphi$ over $u_1, \dots, u_n$ and a [[Field]] $\mathbb F$.
> 
> ---
> ### Construction
> - $u_i \mapsto X_i$
> - $\lnot \varphi \mapsto 1 - P_\varphi$
> - $\varphi \land \psi \mapsto P_\varphi \cdot P_\psi$
> - $\varphi \lor \psi \mapsto P_\varphi + P_\psi - P_\varphi P_\psi$
> 
> ---
> ### Property
> $P_\varphi \in \mathbb F[X_1, \dots, X_n]$ and $P_\varphi(a) = \varphi(a)$ for every $a \in \{0,1\}^n$.

