# Algebra MOC

Index for `math/algebra/`. Organised by **what kind of thing** a note defines: an axiom, a structure built from axioms, a map between structures, or a categorical abstraction over all of them.

## Axioms

- [[Math Properties MOC]] — the axiom library in `math/properties/`. Structures below are *defined by linking into it*, not by restating it

## Structures

`structures/` — one folder per family.

| folder | notes |
| --- | --- |
| `set theory/` | [[Set]], [[Set Foundation]], [[Function]], `relations/`, `functions/` — see [Set theory](#set-theory) |
| **[[Groups MOC\|`groups/`]]** | [[Group]] and its 13-note subtree |
| `rings/` | [[Ring]], [[Commutative Ring]] |
| `fields/` | [[Field]] — axioms, integral domains, characteristic, finite fields |
| `polynomial/` | [[Polynomial]], [[Multivariate Polynomial]], [[Vanishing Polynomial]], [[Lagrange Interpolation]] |
| `lattices/` | see [Lattices](#lattices) |
| `elliptic curve/` | [[Elliptic Curve MOC]] |

### The closure hierarchy

Each row adds one axiom to the row above.

|  | [[Closure\|closure]] | [[Associativity\|assoc]] | [[Identity Element\|ident]] | [[Inverse Element\|inv]] | [[Commutativity\|comm]] |
| --- | :-: | :-: | :-: | :-: | :-: |
| [[Magma\|magma]] | ✓ |  |  |  |  |
| [[Semigroup\|semigroup]] | ✓ | ✓ |  |  |  |
| [[Monoid\|monoid]] | ✓ | ✓ | ✓ |  |  |
| [[Group\|group]] | ✓ | ✓ | ✓ | ✓ |  |
| [[Abelian Group\|abelian group]] | ✓ | ✓ | ✓ | ✓ | ✓ |

Two operations: a [[Ring]] is an [[Abelian Group|abelian group]] under $+$, a [[Monoid|monoid]] under $\star$, plus [[Distributivity]]. A [[Commutative Ring]] adds [[Commutativity]] for $\star$. A [[Field|field]] adds multiplicative [[Inverse Element|inverses]] for every nonzero element.

Outside the hierarchy: [[Algebra Structure]] — quaternions, octonions, the Frobenius theorem, and the [[Alternativity]] that the octonions satisfy in place of associativity.

### Set theory

- [[Set]] — objects, notation, operations, the algebra of $\cup$ / $\cap$
- [[Set Foundation]] — cardinality, countability, Russell's paradox
- [[Function]] — image, restriction, composition, injective / surjective / bijective, and the proof that in $\mathsf{Set}$ injective ⟺ mono and surjective ⟺ epi
- `relations/` — [[Relation]], [[Equivalence Relation]], [[Quotient Relation]], [[Preorder]], [[Partial Order]], [[Total Order]]
- `functions/` — [[Identity Function]], [[Unnormalized Gaussian Function]]

### Lattices

The geometric lattice — a discrete additive subgroup of $\mathbb R^n$ — not the order-theoretic one.

- [[Lattices]] — definition, bases, determinant
- [[Lattice Problem]] — apprSVP, SIVP, Approx-SIVP
- [[Lattice Bounds]] — Hermite, Hadamard ratio, Minkowski, the Gaussian heuristic
- [[Babai's Algorithm]], [[LLL-Based Approximate CVP algorithm]]
- [[Lattice Gadget Algorithm]], [[Lattice Smoothing]]

Downstream: [[Lattice]] and [[LLL Lattice Reduction Algorithm]] in `cryptography/post-quantum cryptography/`, and the whole of `assumptions/lattice-based/`.

## Linear structures

- [[Linear Algebra MOC]] — [[Vector Spaces]], [[Linear Maps]], [[Eigenvalues and Eigenvectors]], [[Inner-Product Spaces]], [[Operators]], [[Trace, Determinant, and Volume]], [[Vector Spaces Over Finite Fields]], [[Examples]]
- [[Vector Algebra]], [[Matrix]], [[Kronecker Product]]
- [[Metric Space]] — norm and distance, composed from the [[Math Properties MOC|norm axioms]]

## Category theory

`category/` — the abstraction that makes "structure + structure-preserving map" one idea.

- [[Category]] — objects, $\mathrm{Hom}$-sets, composition. Axioms 3 and 4 are [[Associativity]] and [[Identity Element]] for a **partial** operation
- [[Opposite Category]] — and the duality principle
- [[Morphism]] — endo / auto as variants; mono / epi / iso as properties
- [[Universal Properties]] — initial and final objects, products, coproducts
- [[Groupoids]] — a category in which every morphism is an isomorphism
- `example/` — [[Category Set]], [[Category Group]]

## Geometric / number-theoretic

- [[Elliptic Curve MOC]] — [[Elliptic Curve]], [[Elliptic Curves over Finite Fields]], [[Generalized Elliptic Curves]], [[Koblitz Curve]], [[Bilinear Pairings]], [[Weil Pairing over Prime Power Fields]]

## Cross-domain

- **To [[Math Properties MOC]]** — every structure definition on this page resolves there
- **From `cryptography/`** — [[Bilinear Pairings]] → pairing-based encoding; [[Field]] → every scheme over $\mathbb F_q$; [[Lattices]] → lattice assumptions
- **From `information theory/`** — [[Code Distance]] and [[Rank Metric Codes]] draw on the norm axioms
- **From `cs/`** — [[Polynomial]] and [[Lagrange Interpolation]] → `verifiable computing/relations/arithmetization/`

## References

[^1]: Thomas W. Judson, *Abstract Algebra: Theory and Applications* (2025). [PDF Link](https://twjudson.github.io/aata-files/aata-20250801.pdf)
