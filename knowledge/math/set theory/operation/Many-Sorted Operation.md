Reference:
- https://en.wikipedia.org/wiki/Binary_operation
- https://en.wikipedia.org/wiki/Semigroupoid

## Basic Definition

> [!definition] Many-Sorted Operation
> Given a family of sets $(S_i)_{i \in I}$ — the **sorts** — an operation of **arity** $(i_1, \dots, i_n) \rightarrow j$ is a map
> $$S_{i_1} \times \cdots \times S_{i_n} \rightarrow S_j$$

> [!remark] Specialisations
> - One sort, arity $2$ — a [[Binary Operation]].
> - Two sorts, arity $(R, S) \rightarrow S$ — a [[Binary Operation#External Operation|left external operation]].
> - Sorts $= \mathsf{Obj} \times \mathsf{Obj}$, arity $(B, C), (A, B) \rightarrow (A, C)$ — composition in a [[Category]].

> [!remark] Sorting is not partiality
> When definedness is decided by the sorts rather than by an arbitrary subset of the domain, every composite the axioms mention exists — the caveat under [[Binary Operation#Partial Operation]] is not needed. An identity is then required per sort: some $1_A \in \mathsf{Hom}(A, A)$ for each object, not a single $e$.
