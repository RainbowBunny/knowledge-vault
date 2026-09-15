Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 1: The computational model —and why it doesn’t matter, Section 1.5.1: The Halting problem (first encounter with reductions).

## Definition

> [!definition] Halting Function
> The function $\mathsf{HALT}$ takes as input a pair $\langle \alpha, x \rangle$ and outputs $1$ if and only if the [[Turing Machine]] $M_\alpha$ ([[Machine Encoding]] of $\alpha$) halts on input $x$ within finite number of steps.

## Property

> [!theorem]
> $\mathsf{HALT}$ is not computable by any [[Turing Machine]].
> 
> ---
> If there was a TM $M_\mathsf{HALT}$ computing $\mathsf{HALT}$ within finite number of steps.
> We can define the $M_\mathsf{UC}$:
> - On input $\alpha$:
> 	1. $M_\mathsf{UC}$ runs $M_\mathsf{HALT}(\alpha, \alpha)$.
> 	2. If the results is $0$, then $M_\mathsf{UC}$ outputs 1.
> 	3. Otherwise, $M_\mathsf{UC}$ uses the [[Universal Turing Machine]] $\mathcal{U}$ to compute $b = M_\alpha(\alpha)$.
> 	4. Returns $\overline{b}$.
>
> Then, TM $M_\mathsf{UC}(\alpha)$ will output $\mathsf{UC}(\alpha)$. 
