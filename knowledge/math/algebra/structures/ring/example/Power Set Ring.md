Reference:
- `[Alu]` — [[Book Reference|Algebra: Chapter 0]] (P. Aluffi), Chapter III: Rings and Modules, Exercise 1.2.
- `[Jud]` — T. W. Judson, _Abstract Algebra: Theory and Applications_ (2025): https://abstract.ups.edu/aata/ — §19.2 Boolean Algebras; Exercise 19.5.17 (read at the mirror https://judsonbooks.org/aata-files/aata-html/; item numbers as there).
- `[WP]` — Wikipedia, _Boolean ring_: https://en.wikipedia.org/wiki/Boolean_ring (read 2026-10-20).

## Definition

> [!definition] Parameters
> - $S$: a [[Set]].
> - $A$: a subset of $S$.
> - $B$: a subset of $S$.

> [!definition] Power Set Ring
> Instantiates:: [[Boolean Ring]].
>
> ---
> Let $S$ be a set. We define the power set $(\mathcal{P}(S), +, \cdot)$:
> - Elements of the ring are the set of all subsets $\mathcal{P}(S) = 2^S$ (the [[Power Set]]).
> - Operations of the ring:
> 	- $A + B = A \, \Delta \, B$.
> 	- $A \cdot B = A \cap B$.
> - Identities:
> 	- For $+$: $\emptyset$.
> 	- For $\cdot$: $S$.
>
> `[Alu III Ex 1.2]` `[WP]`

> [!remark] The same ring in `[Jud]`
> `[Jud §19.2]` takes $\mathcal P(S)$ as the prototype Boolean algebra, and `[Jud Ex 19.5.17]` turns any Boolean algebra into a ring by $a + b = (a \wedge b') \vee (a' \wedge b)$ and $a \cdot b = a \wedge b$. On $\mathcal P(S)$ this sum is $(A \cap B') \cup (A' \cap B) = A \, \Delta \, B$ and the product is $A \cap B$.

> [!proposition] Power set ring is Boolean — every subset is idempotent under $\cap$
> Every element is [[Idempotence|idempotent]] ($A \cap A = A$), so the power set ring is a [[Boolean Ring]].
>
> `[WP]` `[Jud Ex 19.5.17]`

## Related

### Siblings
- [[Hamming Weight#Property|Support]] — the support of a vector in $\mathbb F_2^n$ is a subset of $\{1, \dots, n\}$, and it turns $+$ in $\mathbb F_2^n$ into $\Delta$.

### Prerequisites
- [[Power Set]], [[Boolean Ring]].
