Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.1.3: Interactive proof for graph nonisomorphism.

## Definition

> [!definition] Quadratic Residue
> Reference Name: $\mathsf{QR}$
> 
> ---
> Input:
> - $a$: Number.
> - $p$: Prime.
> 
> ---
> Output: Decides if $a$ is a quadratic residue mod $p$.
> 
> ---
> Certificate: For prime and the root $x$ such that $x^2 \equiv a \bmod p$.

### Complement

> [!definition] Quadratic Non-Residue
> Requires:: [[Complement Class]]
> Member of:: [[Class coNP]], [[Class IP]]
> 
> ---
> $\mathsf{QNR} = \overline{\mathsf{QR}}$.
