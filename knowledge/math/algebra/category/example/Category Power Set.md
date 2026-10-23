Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter I: Preliminaries: Set theory and categories, Section 3.2: Examples.
- `[Rie]` — E. Riehl, _Category Theory in Context_ (2016): https://math.jhu.edu/~eriehl/context.pdf — Example 1.1.4(iii) (read at the mirror https://www.math.ucla.edu/~mopie/context.pdf).

## Definition

> [!definition] Parameters
> - $S$: a [[Set]].

> [!definition] Category $\hat{\mathsf{S}}$
> Instantiates:: [[Category]].
>
> ---
> Category $\hat{\mathsf{S}}$ consists of
> - Object: $\mathcal{P}(S)$, the [[Power Set]] of $S$.
> - For $A, B \subseteq S$, we define
> $$\mathsf{Hom}_{\hat{\mathsf{S}}}(A, B) = \begin{cases}
> \{(A, B)\} &\text{if } A \subseteq B\\
> \emptyset &\text{otherwise}
> \end{cases}$$
>
> `[Alu I.3.2]`

## Property

> [!proposition] Poset category — $\hat{\mathsf S}$ is the poset $(\mathcal P(S), \subseteq)$ regarded as a category
> There is a unique morphism $A \to B$ exactly when $A \subseteq B$, and none otherwise: $\hat{\mathsf S}$ is the [[Partial Order|poset]] $(\mathcal P(S), \subseteq)$ regarded as a category. `[Rie Ex 1.1.4(iii)]`

## Related

### Siblings
- [[Equivalence Category]] — the same construction for any reflexive and transitive relation; $\hat{\mathsf S}$ is the case of $\subseteq$ on $\mathcal P(S)$.
