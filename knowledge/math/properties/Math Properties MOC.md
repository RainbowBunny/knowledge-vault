# Math Properties MOC

Index for `math/properties/` — the axiom library.

Every note here states **one** property, in one place, in the same shape. Structures elsewhere in the vault are then defined by *linking* to these rather than restating them: a [[Group|group]] is a set with an operation satisfying [[Associativity]] + [[Identity Element]] + [[Inverse Element]], and nothing about associativity is written twice.

The library is deliberately **not** under `algebra/` — relation axioms are order theory, metric axioms are analysis, and `information theory/code-based/` needs the metric axioms too.

## The pattern

Every structure in the vault has the same three parts: a **carrier**, some **added data** on it, and **axioms** the data must satisfy. What differs between the four subfolders below is only the *type* of the added data — which is exactly what each note's **Scope** line records.

| structure | carrier | added data | type of the data | axiom family |
| --- | --- | --- | --- | --- |
| [[Magma]] → [[Group]] | $S$ | $\star$ | function $S \times S \to S$ | `operation/` |
| [[Preorder]] → [[Total Order]] | $S$ | $\leq$ | subset $\subseteq S \times S$ | `relation/` |
| set → metric space | $X$ | $d$ | function $X \times X \to \mathbb R$ | `metric/` |
| [[Vector Spaces\|vector space]] → normed space | $V$ | $\lVert \cdot \rVert$ | function $V \to \mathbb R$ | `metric/`, norm forms |
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
- [[Connexity]]

|  | reflexive | symmetric | antisymmetric | transitive | total |
| --- | :-: | :-: | :-: | :-: | :-: |
| [[Preorder\|preorder]] | ✓ |  |  | ✓ |  |
| [[Partial Order\|partial order]] | ✓ |  | ✓ | ✓ |  |
| [[Total Order\|total order]] | (✓) |  | ✓ | ✓ | ✓ |
| [[Equivalence Relation\|equivalence]] | ✓ | ✓ |  | ✓ |  |

> [!remark] The parenthesised tick
> [[Connexity]] as stated — $\forall x, y: (x \, R \, y) \lor (y \, R \, x)$ — **implies** [[Reflexivity]]: take $y = x$. So a total order needs only totality, antisymmetry and transitivity; reflexivity comes free. The tick is kept for readability against the rows above, but it is derived, not assumed.

The structures live with the objects, in `set theory/relation/`: [[Relation]], [[Preorder]], [[Partial Order]], [[Total Order]], [[Equivalence Relation]], [[Quotient Relation]].

> [!remark] Orders as categories
> A [[Preorder|preorder]] is exactly a **thin category** — objects are the elements, and there is one morphism $a \to b$ precisely when $a \leq b$. Reflexivity gives the identity morphisms, transitivity gives composition. See `example/Poset as Category.md`.

## Map axioms

Scope: a map between structured sets.

- [[Linearity]] — preserves addition and scalar multiplication
- [[Bilinearity]] — linear in each argument separately
- [[Multilinearity]] — the $k$-argument generalisation
- [[Map Symmetry]] — $f(x, y) = f(y, x)$; the *form* sense, distinct from relation [[Symmetry]]
- [[Homomorphism]] — preserves every operation of a shared signature; the general case that [[Linearity]] specialises
- [[Monotonicity]] — preserves order; the [[Preorder|order]] family's structure-preserving map
- [[Injection]] · [[Surjection]] · [[Bijection]] — the cardinality properties
- [[Involution]] — $f \circ f = \mathrm{id}$

Consumers: [[Linear Maps]], [[Bilinear Pairings]], [[Kronecker Product]], [[Group Homomorphisms]], [[Split-R1CS]], [[Function]], [[Subgroups]].

> [!remark] One structure-preserving map per family
> Algebra has [[Homomorphism|homomorphisms]], orders have [[Monotonicity|monotone maps]], categories have functors. A [[Morphism|morphism]] is *not* one of these: it is an arrow in an abstract [[Category]] and need not be a function at all. The two coincide only in a **concrete** category — which is what licenses [[Group Homomorphisms]] to import [[Morphism#Isomorphisms|iso]].

## Metric axioms

Scope: a function $d: X \times X \to \mathbb R$ on a set $X$ — or, for the norm forms, $N = \lVert \cdot \rVert : V \to \mathbb R$.

| axiom | metric form | norm form |
| --- | --- | --- |
| [[Positive Definiteness]] | $d(x,y) = 0 \iff x = y$ | $\lVert x \rVert = 0 \iff x = 0$ |
| [[Triangle Inequality]] | $d(x,z) \leq d(x,y) + d(y,z)$ | $\lVert x + y \rVert \leq \lVert x \rVert + \lVert y \rVert$ |
| [[Distance Symmetry]] | $d(x,y) = d(y,x)$ | — *automatic* |
| [[Homogeneity]] | — | $\lVert \alpha x \rVert = \lvert \alpha \rvert \lVert x \rVert$ |

A function satisfying the first three is a **metric**; one satisfying positive definiteness, the triangle inequality and homogeneity is a **norm**, and $d(x,y) = \lVert x - y \rVert$ makes every normed space a [[Metric Space|metric space]].

> [!remark] Homogeneity buys symmetry
> A norm needs no symmetry axiom: $d(y,x) = \lVert y - x \rVert = \lVert -(x-y) \rVert = \lVert x - y \rVert = d(x,y)$, by [[Homogeneity]] at $\alpha = -1$. That is the one axiom the metric family has and the norm family does not.

> [!remark] Non-negativity is a theorem
> $d(x,y) \geq 0$ is **not** an axiom — it follows from the other three: $0 = d(x,x) \leq d(x,y) + d(y,x) = 2\,d(x,y)$. It belongs in [[Metric Space]] as a proposition, never inside a definition callout.

Consumers: [[Metric Space]], [[Inner-Product Spaces]], [[Lattices]] and everything under `structures/lattices/`, and — the reason this library is not under `algebra/` — [[Code Distance]], [[Rank Metric Codes]], and [[Statistical Distance]], since total variation distance is itself a metric.

## Related

- [[Algebra MOC]] — the structures these axioms compose into
- [[Set]] — the algebra of $\cup$ / $\cap$ is an *instance* of [[Commutativity]], [[Associativity]], [[Distributivity]], not a restatement
- [[Category]] — its axioms are [[Associativity]] and [[Identity Element]] for a **partial** composition, one identity per object
