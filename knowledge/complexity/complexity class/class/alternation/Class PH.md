Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 5: The polynomial hierarchy and alternations, Section 5.2: The Polynomial Hierarchy; Section 5.2.1: Properties of the polynomial hierarchy; Section 5.2.2: Complete problems for levels of PH.
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 6: Boolean circuits, Section 6.4: P/poly and NP.

## Definition

> [!definition] Class Polynomial Hierarchy
> Requires:: [[Level Polynomial Hierarchy]]
> 
> ---
> $\mathsf{PH} = \cup_i \Sigma_i^p$.

## Property

### Relation to Other Classes

> [!proposition]
> Requires:: [[Level Polynomial Hierarchy]]
> 
> ---
> $\mathsf{PH} = \cup_{i > 0} \Pi_i^p$.

> [!theorem]
> Requires:: [[Class P]], [[Class NP]].
> 
> ---
> 1. For every $i \geq 1$, if $\Sigma_i^p = \Pi_i^p$ then $\mathsf{PH} = \Sigma_i^p$; that is, the hierarchy collapses to the $i$-th level.
> 2. If $\mathsf{P} = \mathsf{NP}$ then $\mathsf{PH} = \mathsf{P}$; that is, the hierarchy collapses to $\mathsf{P}$.

> [!proposition]
> [[Hardness and Completeness|Completeness]]
> 
> ---
> If there exists a [[Language]] $\mathcal{L}$ that is $\mathsf{PH} \mbox{-} \mathsf{complete}$, then there exists an $i$ such that $\mathsf{PH} = \Sigma_i^p$ (and hence the hierarchy collapses to its $i$-th level).

> [!theorem] Karp-Lipton Theorem
> Requires:: [[Class NP]], [[Class Ppoly]], [[Level Polynomial Hierarchy]]
> 
> ---
> If $\mathsf{NP} \subseteq \mathsf{P_{/\mathsf{poly}}}$, then $\mathsf{PH} = \Sigma_2^p$.

### Language in Class

> [!theorem]
> Requires:: [[Direct Connect Uniform Circuit Family]]
> 
> ---
> $\mathcal{L} \in \mathsf{PH}$ iff $\mathcal{L}$ can be computed by a [[Direct Connect Uniform Circuit Family]] $\{C_n\}$ that:
> - Uses $\mathsf{AND}, \mathsf{OR}, \mathsf{NOT}$ gates.
> - Has size $2^{n^{O(1)}}$ and constant depth.
> - Its gates can have unbounded (exponential) fan-in.
> - Its $\mathsf{NOT}$ gates appear only at the input level.