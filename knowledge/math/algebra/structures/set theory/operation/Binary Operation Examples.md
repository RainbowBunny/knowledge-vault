Reference:
- https://en.wikipedia.org/wiki/Binary_operation

## Total

> [!example] Arithmetic
> $+$ and $\times$ on $\mathbb Z$ — together they make it a [[Ring]]. Each alone makes it a [[Monoid]]; $+$ alone makes it an [[Abelian Group]].

> [!example] Sets
> $\cup$ and $\cap$ on the power set $\mathcal P(S)$ — see [[Set]]. Both are [[Idempotence|idempotent]], which arithmetic is not.

> [!example] Concatenation
> Concatenation on strings over an alphabet: [[Associativity|associative]], with the empty string as [[Identity Element|identity]], and no inverses — a [[Monoid]] and not a [[Group]].

## Not an operation

> [!example] Subtraction on $\mathbb N$
> $2 - 5 \notin \mathbb N$, so $-$ is not a binary operation on $\mathbb N$. It is one on $\mathbb Z$. The failure is of the *codomain*, which is why this is a typing question and not a [[Closure]] question.

## Partial

> [!example] Division
> $/$ on $\mathbb R$ is a [[Binary Operation#Partial Operation|partial operation]] — $x/0$ is undefined. On $\mathbb R \setminus \{0\}$ it is total.

## Indexed

> [!example] Matrix multiplication
> $\mathbf{A}\mathbf{B}$ is defined only when the inner dimensions agree:
> $$\cdot: \mathbb F^{m \times n} \times \mathbb F^{n \times p} \rightarrow \mathbb F^{m \times p}$$
> This is an [[Binary Operation#Indexed Composition|indexed operation]], not merely a partial one — definedness is decided by the shapes, and the identity is $I_n$, one per dimension. The matrices over $\mathbb F$ form a [[Category]] whose objects are the natural numbers. Restricting to one dimension gives the total case: $\mathbb F^{n \times n}$ is a [[Monoid]], and its invertible elements a [[Group]] — see [[Matrix]].

> [!example] Composition of morphisms
> The motivating case; see [[Category]].

## Non-associative

> [!example] Subtraction
> $(a - b) - c \neq a - (b - c)$ on $\mathbb Z$ — a binary operation with no [[Associativity]].

> [!example] Octonions
> Neither [[Commutativity|commutative]] nor [[Associativity|associative]], but [[Alternativity|alternative]]. See [[Algebra Structure]].

## External

> [!example] Scalar multiplication
> $\mathbb F \times V \rightarrow V$ in [[Vector Spaces]].