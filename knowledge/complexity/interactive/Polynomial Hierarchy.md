# Polynomial Hierarchy

The polynomial hierarchy (PH) generalizes NP and coNP into an infinite hierarchy of classes, each gaining power by another quantifier alternation.

## Definition (via Quantifier Alternation)

> [!definition] Polynomial Hierarchy
> Define classes $\Sigma_k^p$ and $\Pi_k^p$ recursively:
> - $\Sigma_0^p = \Pi_0^p = \text{P}$.
> - $\Sigma_{k+1}^p = \text{NP}^{\Sigma_k^p}$ (NP with an oracle for a $\Sigma_k^p$-complete problem).
> - $\Pi_{k+1}^p = \text{coNP}^{\Sigma_k^p}$.
>
> The **polynomial hierarchy** is $\text{PH} = \bigcup_k \Sigma_k^p = \bigcup_k \Pi_k^p$.

Equivalently:
- $\Sigma_k^p$ = languages decidable by a poly-time machine with $k$ alternating $\exists / \forall$ quantifiers over polynomial-length strings, starting with $\exists$.
- $\Pi_k^p$ = same, starting with $\forall$.

Layer-by-layer:
- $\Sigma_1^p = \text{NP}$, $\Pi_1^p = \text{coNP}$
- $\Sigma_2^p$, $\Pi_2^p$ — two quantifier alternations.
- …

## Key Properties

$$\text{P} \subseteq \text{NP} \subseteq \Sigma_2^p \subseteq \cdots \subseteq \text{PH} \subseteq \text{PSPACE}.$$

> [!theorem] Collapse of PH
> If $\Sigma_k^p = \Pi_k^p$ for some $k$, then $\text{PH} = \Sigma_k^p$ (the hierarchy collapses to its $k$-th level).

The widely-believed conjecture: PH does *not* collapse — i.e., the levels are all distinct. This is stronger than $\text{P} \neq \text{NP}$.

## Related

- [[Time Complexity#Class NP|NP]] = $\Sigma_1^p$
- [[Oracle Machines]] — the recursive definition uses oracle TMs
- [[Alternating Turing Machine]] — alternating TMs uniformly capture PH levels
- [[Conjectures MOC|conjectures]] — "PH does not collapse" is a major open problem
