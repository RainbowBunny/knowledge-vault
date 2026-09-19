Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 8: Interactive Proofs, Section 8.1.2: The Class IP: Probabilistic verifier.

## Definition

> [!definition] Class IP
> The class $\mathsf{IP}[k]$ contains all [[Language]] with a $k$-round [[Probabilistic Interactive Proof System]].
> $\mathsf{IP} = \cup_{c \geq 1} \mathsf{IP}(n^c)$.

## Property

> [!lemma]
> Requires:: [[Probabilistic Interactive Proof System]]
> 
> ---
> The class $\mathsf{IP}$ is unchanged if we replaced:
> - Completeness parameter $\frac{2}{3}$ by $1 - 2^{-n^s}$.
> - Soundness parameter $\frac{1}{3}$ by $2^{-n^s}$
> 
> for any fixed constant $s > 0$.

### Relation with Other Classes

> [!proposition]
> Requires:: [[Class PSPACE]]
> 
> ---
> $\mathsf{IP} \subseteq \mathsf{PSPACE}$.



