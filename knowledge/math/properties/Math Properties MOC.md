# Math Properties MOC

Index for `math/properties/` — the axiom library.

Every note here states **one** property, in one place, in the same shape. Structures elsewhere in the vault are then defined by *linking* to these rather than restating them: a [[Group|group]] is a set with an operation satisfying [[Associativity]] + [[Identity Element]] + [[Inverse Element]], and nothing about associativity is written twice.

The library is deliberately **not** under `algebra/` — relation axioms are order theory, norm axioms are analysis, and `information theory/code-based/` needs the metric axioms too.

## The pattern

Every structure in the vault has the same three parts: a **carrier**, some **added data** on it, and **axioms** the data must satisfy. What differs between the four subfolders below is only the *type* of the added data — which is exactly what each note's **Scope** line records.

| structure | carrier | added data | type of the data | axiom family |
| --- | --- | --- | --- | --- |
| [[Magma]] → [[Group]] | $S$ | $\star$ | function $S \times S \to S$ | `operation/` |
| [[Preorder]] → [[Total Order]] | $S$ | $\leq$ | subset $\subseteq S \times S$ | `relation/` |
| [[Vector Spaces\|vector space]] → normed space | $V$ | $\lVert \cdot \rVert$ | function $V \to \mathbb R$ | `norm/` |
| homomorphism, pairing | $A, B$ | $f$ | function $A \to B$ | `map/` |
| [[Category]] | $\mathsf{Obj}$ | $\mathsf{Hom}, \circ$ | **partial** function | `operation/`, read per composable triple |

So an ordered set $(S, \leq)$ is the same *kind* of thing as a group $(S, \star)$ — a carrier with data and axioms. Order theory is not a different pattern; it is this pattern with a relation in the data slot instead of an operation.

> [!remark] Where a genuinely different family appears
> **Compatibility axioms.** An *ordered group* or *ordered field* carries an operation **and** an order, plus axioms linking them — $a \leq b \Rightarrow a + c \leq b + c$, and $0 \leq a, 0 \leq b \Rightarrow 0 \leq ab$. Those constrain the *interaction*, so they belong to neither `operation/` nor `relation/`. The vault already depends on them: [[Positive Definiteness]] writes $\lVert x \rVert \geq 0$ and [[Triangle Inequality]] writes $\leq$, both presupposing that $\mathbb R$ is an ordered field. A `properties/compatibility/` folder is the place for these when they are needed.

> [!remark] Where the two families merge
> An **order-theoretic lattice** is simultaneously a [[Partial Order|poset]] with meets and joins, *and* an algebraic structure with two [[Idempotence|idempotent]], [[Commutativity|commutative]], [[Associativity|associative]] operations satisfying absorption — the two definitions are equivalent. It is the cleanest demonstration that operation axioms and relation axioms describe one thing from two sides. *(Name it `Lattice (Order Theory).md` when it exists — [[Lattices]] here is the geometric object.)*

## Convention

Each note is a single `[!definition]` callout with the same three parts:

| part | holds |
| --- | --- |
| **Scope** | the typed object the property applies to |
| **Condition** | preconditions on that object, when there are any (module / vector-space structure, an identity element) — omitted otherwise |
| **Property** | the quantified statement, and nothing else |

Consequences do **not** live here. "Inverses are unique" is a theorem of associativity and belongs in [[Group]]; this library states only what is assumed.

A **property** is what an object may have; an **axiom** is a property a definition chooses to require. These notes state properties — [[Abelian Group]] is what turns [[Commutativity]] into an axiom. That is why the folder is `properties/` and not `axioms/`, and why `verifiable computing/proof/properties/` on the cryptography side follows the same shape.

## Operation axioms

Scope: a binary operation $\star: O \times O \to O$.

- [[Closure]] — a subset $A \subseteq O$ is closed under $\star$
- [[Associativity]]
- [[Commutativity]]
- [[Identity Element]]
- [[Inverse Element]]
- [[Distributivity]] — the one two-operation axiom
- [[Idempotence]]
- [[Alternativity]] — left / right alternative; weaker than associativity, satisfied by the octonions

Structures: [[Magma]] → [[Semigroup]] → [[Monoid]] → [[Group]] → [[Abelian Group]] → [[Ring]] → [[Commutative Ring]] → [[Field]]. The closure table lives in [[Algebra MOC]], with the structures it indexes.

## Relation axioms

Scope: a relation $R \subseteq O \times O$.

- [[Reflexivity]]
- [[Symmetry]]
- [[Antisymmetry]]
- [[Transitivity]]
- [[Totality]]

|  | reflexive | symmetric | antisymmetric | transitive | total |
| --- | :-: | :-: | :-: | :-: | :-: |
| [[Preorder\|preorder]] | ✓ |  |  | ✓ |  |
| [[Partial Order\|partial order]] | ✓ |  | ✓ | ✓ |  |
| [[Total Order\|total order]] | (✓) |  | ✓ | ✓ | ✓ |
| [[Equivalence Relation\|equivalence]] | ✓ | ✓ |  | ✓ |  |

> [!remark] The parenthesised tick
> [[Totality]] as stated — $\forall x, y: (x \, R \, y) \lor (y \, R \, x)$ — **implies** [[Reflexivity]]: take $y = x$. So a total order needs only totality, antisymmetry and transitivity; reflexivity comes free. The tick is kept for readability against the rows above, but it is derived, not assumed.

The structures live with the objects, in `set theory/relation/`: [[Relation]], [[Preorder]], [[Partial Order]], [[Total Order]], [[Equivalence Relation]], [[Quotient Relation]].

> [!remark] Orders as categories
> A [[Preorder|preorder]] is exactly a **thin category** — objects are the elements, and there is one morphism $a \to b$ precisely when $a \leq b$. Reflexivity gives the identity morphisms, transitivity gives composition. See `example/Poset as Category.md`.

## Map axioms

Scope: a map between structured sets.

- [[Linearity]] — preserves addition and scalar multiplication
- [[Bilinearity]] — linear in each argument separately
- [[Multilinearity]] — the $k$-argument generalisation
- [[Map Symmetry]] — $f(x, y) = f(y, x)$; the *form* sense, distinct from relation [[Symmetry]]

Consumers: [[Linear Maps]], [[Bilinear Pairings]], [[Kronecker Product]], [[Group Homomorphisms]], [[Split-R1CS]].

*Still to add: `Homomorphism` — the structure-preserving map in general. [[Ring]] and [[Group Homomorphisms]] both define their own version inline.*

## Norm axioms

Scope: a function $N: V \to \mathbb R$ on a vector space or additive group $V$.

- [[Triangle Inequality]]
- [[Homogeneity]]
- [[Positive Definiteness]]

A function satisfying all three is a **norm**; [[Metric Space]] composes them into the distance $d(x, y) = \lVert x - y \rVert$.

Consumers: [[Metric Space]], [[Inner-Product Spaces]], [[Lattices]] and everything under `structures/lattices/`, and — the reason this library is not under `algebra/` — [[Code Distance]] and [[Rank Metric Codes]], which already generalise to "an arbitrary norm $\omega$".

## Related

- [[Algebra MOC]] — the structures these axioms compose into
- [[Set]] — the algebra of $\cup$ / $\cap$ is an *instance* of [[Commutativity]], [[Associativity]], [[Distributivity]], not a restatement
- [[Category]] — its axioms are [[Associativity]] and [[Identity Element]] for a **partial** composition, one identity per object
