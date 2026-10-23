Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter I: Preliminaries: Set theory and categories, Section 3.2: Examples.
- `[Rie]` — E. Riehl, _Category Theory in Context_ (2016): https://math.jhu.edu/~eriehl/context.pdf — Example 1.1.4(iii) and its footnote 10 (read at the mirror https://www.math.ucla.edu/~mopie/context.pdf).

## Definition

> [!definition] Parameters
> - $S$: a [[Set]].
> - $\sim$: a [[Relation]] on $S$ satisfying [[Reflexivity]] and [[Transitivity]], i.e. a [[Preorder]].

> [!definition] Equivalence Category
> Instantiates:: [[Category]].
>
> ---
> Suppose $S$ is a set and $\sim$ is a relation on $S$ satisfies [[Reflexivity]] and [[Transitivity]].
> Equivalence category consists of
> - Object: $S$.
> - For $a, b \in S$, we define
> $$\mathsf{Hom}(a, b) = \begin{cases}
> \{(a, b)\} &\text{if } a \sim b\\
> \emptyset &\text{otherwise}
> \end{cases}$$
>
> `[Alu I.3.2]` `[Rie Ex 1.1.4(iii)]`

## Property

> [!remark] A preorder, not necessarily an equivalence relation
> $\sim$ need not be symmetric: this is the [[Preorder]] $(S, \sim)$ regarded as a category, with a unique morphism $a \to b$ exactly when $a \sim b$ `[Rie Ex 1.1.4(iii)]`. When $\sim$ is an [[Equivalence Relation]], the morphism $a \to b$ has the inverse $b \to a$, so the category is a [[Groupoid]].

## Related

### Siblings
- [[Category Power Set]] — the case of $\subseteq$ on a power set.

### Prerequisites
- [[Preorder]] — the relation $\sim$.
