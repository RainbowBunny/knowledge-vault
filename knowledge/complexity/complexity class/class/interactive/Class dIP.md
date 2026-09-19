Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.1.1: Warmup: Interactive proofs with deterministic verifier and prover.

## Definition

> [!definition] Class dIP
> The class $\mathsf{dIP}$ contains all [[Language]] with a $k(n)$-round [[Deterministic Interactive Proof System]] where $k(n)$ is polynomial in $n$.

## Property

### Relation with Other Classes

> [!lemma]
> Requires:: [[Class NP]]
> 
> ---
> $\mathsf{dIP} = \mathsf{NP}$.
> 
> ---
> $\impliedby$: $\mathcal{L} \in \mathsf{NP}$ then $\mathcal{L}$ has a 1 round [[Deterministic Interactive Proof System]].
> $\implies$: $\mathcal{L} \in \mathsf{dIP}$ then $\mathcal{L}$ has a certificate which is the transcript and polynomial time verifier.




