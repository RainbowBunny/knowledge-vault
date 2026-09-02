Reference:
- https://en.wikipedia.org/wiki/Binary_operation
- https://en.wikipedia.org/wiki/Semigroupoid

## Basic Definition

> [!definition] Binary Operation
> A **binary operation** on a set $S$ is a [[Function|Function]]
> $$\star: S \times S \rightarrow S$$
> mapping every pair of elements of $S$ to an element of $S$.

> [!remark] Closure is in the type
> Totality and closure are not axioms here — $x \star y$ is defined for every $x, y \in S$ and lies in $S$ because the codomain says so. [[Closure]] states the version that is *not* automatic: that a **subset** $A \subseteq S$ is closed under $\star$.

## Variant

Each variant relaxes one clause of the definition above. They are not siblings — many-sorted subsumes the other two.

### Partial Operation

> [!definition] Partial Operation
> Relaxes *total*. A **partial binary operation** on $S$ is a function $\star: D \rightarrow S$ defined on a subset $D \subseteq S \times S$. Axioms are then read only over tuples for which both sides are defined.

### External Operation

> [!definition] Left / Right External Operation
> Relaxes *both arguments from $S$*. Given a second set $R$, the **operator domain**:
> - a **left external operation** on $S$ over $R$ is a map $R \times S \rightarrow S$;
> - a **right external operation** on $S$ over $R$ is a map $S \times R \rightarrow S$.
> 
> The two coincide when the operator domain is commutative, which is why scalar multiplication over a [[Field]] is written one way only. Over a non-commutative ring they are genuinely different — this is the left/right module distinction.


## Property

Axioms an operation may satisfy: 
- [[Associativity]], [[Commutativity]], [[Identity Element]], [[Inverse Element]], [[Idempotence]], [[Alternativity]].
- [[Distributivity]] for a pair of operations.
- [[Closure]] for a subset.

## Example

- [[Binary Operation Examples]]