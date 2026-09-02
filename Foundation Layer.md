# Foundation Layer — specification, drafts, filling plan

*Everything below is paste-ready or a precise spec. Provenance tagged. House notation.*

> **Link convention in this file.** `Set Operation`, `Homomorphism`, `Injectivity` and `Surjectivity` appear in `code` because they do not exist yet — they become real links as Batch A and C land. Inside the fenced drafts they are already written as wikilinks, ready to paste.


---

# Part I · The spine

One claim organizes the whole layer: **every object in the vault descends from `Set` through the Cartesian product.**

```
Set
 │
 └─ Cartesian Product  A × B
     │
     └─ Relation        R ⊆ A × B
         │
         ├─ homogeneous          R ⊆ S × S ──[relation axioms]──► Preorder → Partial Order → Total Order
         │                                                          Equivalence Relation → Quotient Relation
         │
         └─ functional + total   Function  f: A → B ──[map axioms]──► Homomorphism, Linear Map, Monotone Map
             │
             ├─ partial function        (drop totality)
             │
             └─ Operation  (many-sorted, arity-indexed)
                 │
                 └─ Binary Operation  ⋆: S × S → S ──[operation axioms]──► Magma → Semigroup → Monoid
                                                                            → Group → Abelian Group
                                                                            → Ring → Commutative Ring → Field
```

Two consequences worth stating in the vault, because both are currently invisible:

**A function is a relation.** Specifically: a relation $R \subseteq A \times B$ that is *total* (every $a$ is related to something) and *functional* (to at most one thing). Right now `Relation.md` only defines the homogeneous case $R \subseteq S \times S$, so this edge cannot be drawn — the object layer has two parallel branches with nothing joining them.

**A binary operation is a function.** Already stated correctly in `Binary Operation.md`. That edge is the one that makes the operation axioms and the map axioms siblings rather than strangers.

## The four attachment points

Each axiom family attaches at exactly one node of the spine. This is what justifies the four subfolders — they are not a taxonomy of convenience, they are indexed by *what the axioms constrain*.

| family                        | attaches to                                              | Scope line reads                        | structures produced                                      |
| ----------------------------- | -------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------- |
| `properties/operation/`       | binary operation $\star: S \times S \to S$               | "A [[Binary Operation]] $\star$ on $O$" | [[Magma]] → [[Group]] → [[Ring]] → [[Field]]             |
| `properties/relation/`        | homogeneous relation $R \subseteq S \times S$            | "A [[Relation]] $R$ on $S$"             | [[Preorder]] → [[Total Order]]; [[Equivalence Relation]] |
| `properties/map/`             | function $f: A \to B$                                    | "A [[Function]] $f: A \to B$"           | homomorphism, linear map, monotone map                   |
| `properties/norm/`, `metric/` | function $V \to \mathbb R$ or $X \times X \to \mathbb R$ | "A function $N: V \to \mathbb R$"       | normed space, [[Metric Space]]                           |

There is a pleasing regularity here that the vault can state once and reuse: **each object family has its own notion of structure-preserving map.** Algebra has homomorphisms, orders have monotone maps, metric spaces have isometries (and, loosened, continuous maps), categories have functors. That is one row per family, and it is the row `properties/map/` is currently missing.

---

# Part II · Audit

## F1 · Cartesian Product no longer exists — **critical**

`Set.md` lists $\times$ in a symbol table and never defines it. `Set Foundation.md` does not have it. Nothing in `knowledge/` defines it.

It was in the old `Set Theory.md` and was dropped when task 6.3 split that note. Recoverable verbatim from git:

```
git show f9c2c34:"knowledge/math/algebra/structures/set theory/Set Theory.md"
```

This is the most load-bearing definition in the vault. Every Scope line — $R \subseteq S \times S$, $f: A \to B$, $\star: S \times S \to S$, $\mathsf{Hom}(B,C) \times \mathsf{Hom}(A,B)$ — is written in terms of a product that is currently undefined. It is exactly what precision-skeleton rule 5 exists to catch.

**Also lost in the same split:** `Set Equality` and `Empty Set`. Same commit, same recovery.

## F2 · `Relation.md` is homogeneous-only

> "A **relation** on a set $S$ is a subset $R$ of the product $S \times S$."

Correct as far as it goes, but it makes `Relation` unable to serve as the parent of `Function`, and it means "relation from $A$ to $B$" has no home. Fix: define the heterogeneous case first, homogeneous as the specialisation $A = B$.

## F3 · `Function between Sets.md` has two definition blocks

The note opens with `## Basic Definition` (the graph $\Gamma_f$ formulation, good) and *ends* with a second `## Definition` absorbed from the old `Function.md` in task 7.7, redefining Function, Domain, Co-domain, Range, plus odd/even functions.

Three separate problems:
- **Range** duplicates **Image**, defined 100 lines apart with different words.
- **Odd / even function** is analysis, not the foundation layer — it belongs in [[Calculus Functions]] (it needs an additive inverse on the domain, which sets do not have).
- The bottom definition — "a set of ordered pairs no two of which have the same first member" — omits totality, so it is *literally the definition of a partial function*. That is the seed for the missing partial-function note rather than a duplicate to delete.

## F4 · Small errors in the same note

- "A function $f: A \rightarrow$ is **surjective**" — missing codomain.
- "We often **right** $f$" → write.
- `### Inversion` heading over an `[!definition] Inverse` callout.

## F5 · Injective / surjective / bijective are properties filed as object content

They sit in `Function between Sets.md`'s `## Property` section. By the vault's own rule they belong in `properties/map/` — their Scope is "a map $f: A \to B$", identical in shape to [[Linearity]].

The precedent is already set on the algebra side: [[Inverse Element]] states the axiom, [[Group]] holds the *theorems* about it (uniqueness, cancellation). Apply the same split here — `properties/map/Injectivity.md` states the axiom; `Function between Sets.md` keeps the theorems (injective ⟺ monomorphism, left-inverse ⟺ injective, canonical decomposition).

## F6 · `Set Foundation.md` opens with two blank lines and no `## Basic Definition`

Cosmetic, but it is the only foundation note that breaks the section convention.

## F7 · The axiom families have gaps with existing consumers

Detailed in Part IV. The short version: **cancellativity** (3 consumers, currently a theorem in two places), **homomorphism** (4 consumers, defined inline twice), **the metric axioms** (4 consumers including [[Statistical Distance]], which *is* a metric), and **monotonicity** (the missing row of the structure-preserving-map table).

---

# Part III · Note drafts

## F0 — Primitives



### 3.2 `Set Operation.md` — NEW **[Standard]**

Carries the ~20-row laws table out of `Set.md` (task 6.3b) *and* restores the Cartesian product.

```markdown

> [!definition] Partition
> A collection of nonempty sets $A_1, A_2, \dots$ is a **partition** of $A$ if they are pairwise disjoint and their union is $A$.
> 
> Partitions of $A$ correspond exactly to [[Equivalence Relation|equivalence relations]] on $A$ — see [[Quotient Relation]].

## Property

*[the existing laws table moves here verbatim]*

> [!remark] These are instances, not new axioms
> $\cup$ and $\cap$ are [[Binary Operation|binary operations]] on $\mathcal P(S)$, and the first three rows of the table are exactly [[Commutativity]], [[Associativity]] and [[Distributivity]] for them. The rows $A \cup A = A$ and $A \cap A = A$ are [[Idempotence]]; $A \cup (A \cap B) = A$ is [[Absorption]]. With $\emptyset$ and $S$ as identities, $(\mathcal P(S), \cup, \cap)$ is the standard example of a lattice.
```

That closing remark is task 6.5, and it is the single best advertisement in the vault for why the axiom library exists: a table the reader has seen since school turns out to be five named axioms they already have notes for.

---

## F1 — Derived objects

### 3.3 `Relation.md` — REWRITE **[Standard]**

```markdown
Reference:
- https://en.wikipedia.org/wiki/Binary_relation

## Intuition

A relation is just a set of pairs that "count as related" — nothing more. Everything else in the layer is a relation with conditions bolted on: an order is a relation that is reflexive and transitive; a function is a relation where each input has exactly one output.




> [!remark] Function = left-total + functional
> A [[Function between Sets|function]] $A \to B$ is exactly a relation that is both. Dropping left-totality gives a **partial function**; dropping functionality gives a multivalued relation.
> 
> Beware the word *total*: **left-total** here (defined on all of $A$) is unrelated to [[Totality]] on a homogeneous relation ($\forall x, y:\ xRy \lor yRx$), and unrelated again to a *total* function. This vault has all three senses live — the reason [[Totality]] should be renamed **Connexity**.

```

That final table is the spine, stated at the node where it branches — and it makes `Relation.md` the hub of the object layer rather than a one-line stub.

---

### 3.4 `Function between Sets.md` — RESTRUCTURE **[Standard]**

Keep the graph definition, the image / restriction / composition / projections / canonical-decomposition material, and the mono/epi theorems. Six edits:


1. **Add the partial function variant** — this closes the dependency [[Binary Operation#Partial Operation]] currently dangles on:
   ```markdown
   ### Partial Function

   > [!definition] Partial Function
   > A **partial function** $f: A \rightharpoonup B$ is a functional relation that need not be left-total: each $a \in A$ has *at most* one image. Its **domain of definition** is $\mathsf{dom}(\Gamma_f) \subseteq A$.
   > 
   > Division on $\mathbb R$ is the standard example; see [[Binary Operation#Partial Operation]].
   ```
2. (F5). What stays here is the theorems: left-inverse ⟺ injective, right-inverse ⟺ surjective, bijection ⟺ two-sided inverse, injective ⟺ monomorphism, surjective ⟺ epimorphism.
3. **Add the composition remark** pointing at [[Relation#Composition]], so the two composition definitions are one concept stated once.

---

## F2 — New axioms

All follow the Scope / Condition / Property template unchanged. Each has named existing consumers; nothing speculative.

### 3.5 `properties/operation/Cancellativity.md` **[Standard]** — 3 consumers

```markdown
## Basic Definition

> [!definition] Cancellativity
> ### Scope
> A [[Binary Operation]] $\star: O \times O \rightarrow O$.
> 
> ---
> ### Property
> $\star$ is **left-cancellative** iff
> $$\forall a, x, y \in O: \quad a \star x = a \star y \implies x = y$$
> **right-cancellative** iff $x \star a = y \star a \implies x = y$, and **cancellative** iff both.

> [!remark] Axiom here, theorem there
> In a [[Group]] cancellativity is a *theorem* — compose with the [[Inverse Element|inverse]]. In a [[Monoid]] it is an independent axiom: $(\mathbb N, \times)$ is cancellative on nonzero elements, $(\mathbb Z / 6\mathbb Z, \times)$ is not, since $2 \cdot 2 = 2 \cdot 5$.
```

Consumers: [[Group]]'s `### Cancellation` proposition; [[Field]]'s "Cancellation Law for Addition / Multiplication" rows; and the payoff — **an integral domain is exactly a commutative ring whose nonzero elements are cancellative under $\star$**, which recomposes a definition [[Field]] currently states as "has no zero divisors".

---

### 3.6 `properties/operation/Absorption.md` **[Standard]** — 2 consumers

```markdown
## Basic Definition

> [!definition] Absorption
> ### Scope
> Two [[Binary Operation|binary operations]] $\oplus, \otimes$ on $O$.
> 
> ---
> ### Property
> $\oplus$ and $\otimes$ satisfy **absorption** iff for all $a, b \in O$:
> - $a \oplus (a \otimes b) = a$
> - $a \otimes (a \oplus b) = a$
```

Consumers: `Set Operation`' law table ($A \cup (A \cap B) = A$); and the order-theoretic lattice of task 2.14 — a lattice is exactly two [[Idempotence|idempotent]], [[Commutativity|commutative]], [[Associativity|associative]] operations satisfying absorption. This note is what makes [[Idempotence]] stop being an orphan.

---

### 3.7 `properties/map/Homomorphism.md` **[Standard]** — 4 consumers, the biggest gap

```markdown
Reference:
- https://en.wikipedia.org/wiki/Signature_(logic)

## Intuition

A map that respects structure: do the operation then map, or map then do the operation, and you land in the same place. Every "…-morphism" in the vault is this with a particular signature filled in.

## Basic Definition

> [!definition] Homomorphism
> ### Scope
> A [[Function between Sets|map]] $\varphi: A \rightarrow B$.
> 
> ---
> ### Condition
> $A$ and $B$ carry structures over the **same signature** — the same operation symbols with the same arities (see [[First-Order Logic]]).
> 
> ---
> ### Property
> $\varphi$ is a **homomorphism** iff it commutes with every operation of the signature: for each $n$-ary symbol $\star$,
> $$\varphi(\star_A(x_1, \dots, x_n)) = \star_B(\varphi(x_1), \dots, \varphi(x_n))$$
> for all $x_1, \dots, x_n \in A$. In particular, nullary symbols (constants such as identities) must be preserved.

> [!remark] The signature is what makes this statable
> Without a shared signature, "preserves the structure" has no referent. This is the one place the vault's [[First-Order Logic|signature]] framing is not just organisational but load-bearing.
```

Instances to rewire: [[Group Homomorphisms]] ($\varphi(g_1 \star g_2) = \varphi(g_1) \star \varphi(g_2)$), [[Ring]]'s inline ring homomorphism, [[Linear Maps]] (a homomorphism of modules — [[Linearity]] is this note's specialisation to the module signature), and [[Subgroups]], whose definition *is* "the inclusion is a group homomorphism".

---

### 3.8 `properties/map/Injectivity.md`, `Surjectivity.md` **[Standard]**

Moved out of [[Function]] (F5), verbatim apart from the missing $B$:

```markdown
> [!definition] Injectivity
> ### Scope
> A [[Function between Sets|map]] $f: A \rightarrow B$.
> 
> ---
> ### Property
> $f$ is **injective** (one-to-one) iff
> $$\forall a_1, a_2 \in A: \quad f(a_1) = f(a_2) \implies a_1 = a_2$$
> Written $f: A \hookrightarrow B$.
```

```markdown
> [!definition] Surjectivity
> ### Scope
> A [[Function between Sets|map]] $f: A \rightarrow B$.
> 
> ---
> ### Property
> $f$ is **surjective** (onto) iff
> $$\forall b \in B \; \exists a \in A: \quad f(a) = b$$
> equivalently $\mathrm{im}\, f = B$. Written $f: A \twoheadrightarrow B$.
```

**Bijectivity** stays a composed one-liner — *"a map is bijective iff it is `injective` and `surjective`"* — either as its own two-line note or as a remark in [[Function]]. Prefer the note if [[Morphism]] will link it.

---

### 3.9 `properties/map/Monotonicity.md` **[Standard]** — the missing row

```markdown
## Basic Definition

> [!definition] Monotonicity
> ### Scope
> A [[Function between Sets|map]] $f: A \rightarrow B$.
> 
> ---
> ### Condition
> $A$ and $B$ carry [[Preorder|preorders]] $\leq_A, \leq_B$.
> 
> ---
> ### Property
> $f$ is **monotone** (order-preserving, isotone) iff
> $$\forall x, y \in A: \quad x \leq_A y \implies f(x) \leq_B f(y)$$
> **Antitone** (order-reversing) iff $x \leq_A y \implies f(y) \leq_B f(x)$; **strictly monotone** iff strict inequalities are preserved.

> [!remark] One row per family
> Monotone maps are to [[Preorder|orders]] what [[Homomorphism|homomorphisms]] are to algebra and functors are to [[Category|categories]] — the structure-preserving maps of that family. Under the [[Preorder]]-as-thin-category reading, a monotone map *is* a functor.
```

Consumers: [[Calculus Functions]]' increasing / decreasing / strictly monotone definitions (which currently state the order-theoretic notion for $\mathbb R$ only); order theory generally; Galois connections if they ever arrive.

---

### 3.10 `properties/map/Involution.md` **[Standard]** — 4 consumers, cheap

```markdown
> [!definition] Involution
> ### Scope
> A [[Function between Sets|map]] $f: A \rightarrow A$.
> 
> ---
> ### Property
> $f$ is an **involution** iff $f \circ f = \mathrm{id}_A$, i.e. $\forall x \in A: f(f(x)) = x$.
> Every involution is a bijection, and is its own inverse.
```

Consumers: complex conjugation and $-(-a) = a$ in [[Field]]; matrix transpose in [[Matrix]]; $(a^{-1})^{-1} = a$ in [[Group]]; set complement in `Set Operation`.

---

### 3.11 `properties/metric/` — NEW FAMILY **[Standard]** — 4 consumers, one of them crypto

Three notes, all with Scope *"A function $d: X \times X \rightarrow \mathbb R$ on a set $X$"*:

```markdown
> [!definition] Non-negativity
> $d$ is non-negative iff $\forall x, y \in X: d(x, y) \geq 0$.
```
```markdown
> [!definition] Identity of Indiscernibles
> $d$ separates points iff $\forall x, y \in X: d(x, y) = 0 \iff x = y$.
```
```markdown
> [!definition] Distance Symmetry
> $d$ is symmetric iff $\forall x, y \in X: d(x, y) = d(y, x)$.
> 
> Distinct from relation [[Symmetry]] and from [[Map Symmetry]]: same word, third scope.
```

Plus a `### Metric Form` section appended to the existing [[Triangle Inequality]]:

```markdown
### Metric Form

> [!definition] Triangle Inequality (metric)
> ### Scope
> A function $d: X \times X \rightarrow \mathbb R$.
> 
> ---
> ### Property
> $$\forall x, y, z \in X: \quad d(x, z) \leq d(x, y) + d(y, z)$$
> 
> ### Remark
> The norm form above is the special case $d(x, y) = \lVert x - y \rVert$ on an additive group — every norm induces a metric, not conversely.
```

Consumers, and why this family is worth a folder:

| consumer | why it needs metric, not norm |
| --- | --- |
| [[Metric Space]] | fixes 5.4b — "additive group + norm" is a *normed group*; the metric axioms are the general notion |
| [[Code Distance]] | Hamming distance is a metric on $\Sigma^n$ with no vector-space norm underneath |
| [[Rank Metric Codes]] | same, rank-weight |
| [[Statistical Distance]] | **total variation distance is a metric on distributions** — the axioms are already implicit in your Δ theorems |

> **One judgment call.** Splitting [[Symmetry]] / [[Map Symmetry]] set the precedent *"different scope → different note"*, which argues for a fourth note rather than a `### Metric Form` section inside [[Triangle Inequality]]. I recommend the section anyway: the two forms are the same inequality and one implies the other, whereas relation-symmetry and form-symmetry are unrelated statements that merely share a word. Flagging it because it is a real inconsistency, decided deliberately.

---

# Part IV · Complete axiom inventory

Every axiom the vault has, needs, or should deliberately not write. **Consumer rule applied throughout** — nothing is proposed without a note that already wants it.

## `properties/operation/` — Scope: a binary operation $\star: O \times O \to O$

| axiom | status | consumers |
| --- | --- | --- |
| [[Closure]] | exists (subset reading) | [[Subgroups]] (3.6) — and *only* subgroups, once 1.12 lands |
| [[Associativity]] | exists | [[Semigroup]] onward; [[Category]]; [[Relation]] composition |
| [[Commutativity]] | exists | [[Abelian Group]], [[Commutative Ring]], `Set Operation` |
| [[Identity Element]] | exists | [[Monoid]] onward; [[Category]] |
| [[Inverse Element]] | exists | [[Group]] onward; [[Field]] |
| [[Distributivity]] | exists | [[Ring]]; `Set Operation` |
| [[Idempotence]] | exists — **currently orphaned** | `Set Operation`; lattices via `Absorption` |
| [[Alternativity]] | exists | octonions in [[Algebra Structure]] |
| **Cancellativity** | **add** | [[Group]] (thm), [[Field]] (2 rows + integral domain) |
| **Absorption** | **add** | `Set Operation`; lattice (2.14) |
| ~~Annihilator / zero element~~ | defer | a *theorem* in rings ($0 \cdot a = 0$), not an axiom |
| ~~Nilpotency, anti-commutativity~~ | defer | no consumer — needs Lie algebras or cross products |

## `properties/relation/` — Scope: a homogeneous relation $R \subseteq S \times S$

| axiom | status | consumers |
| --- | --- | --- |
| [[Reflexivity]] | exists | [[Preorder]], [[Equivalence Relation]] |
| [[Symmetry]] | exists | [[Equivalence Relation]] |
| [[Antisymmetry]] | exists | [[Partial Order]] |
| [[Transitivity]] | exists | [[Preorder]], [[Equivalence Relation]] |
| [[Totality]] | exists — **rename `Connexity`** | [[Total Order]]; the word now collides three ways (see 3.3) |
| ~~Irreflexivity, Asymmetry, Trichotomy~~ | defer | strict orders — no note wants them yet |
| ~~Well-foundedness~~ | optional | [[Proofs]]' induction principle is the one candidate |

## `properties/map/` — Scope: a map $f: A \to B$

| axiom | status | consumers |
| --- | --- | --- |
| [[Linearity]] | exists | [[Linear Maps]], [[Vector Spaces]] |
| [[Bilinearity]] | exists | [[Bilinear Pairings]], [[Split-R1CS]] |
| [[Multilinearity]] | exists | [[Bilinear Pairings]] |
| [[Map Symmetry]] | exists | [[Inner-Product Spaces]] |
| **Homomorphism** | **add** | [[Group Homomorphisms]], [[Ring]], [[Linear Maps]], [[Subgroups]] |
| **Injectivity** | **move in** | [[Function]], [[Group Homomorphisms]], [[Morphism]] |
| **Surjectivity** | **move in** | same |
| **Monotonicity** | **add** | [[Calculus Functions]]; order theory; functors |
| **Involution** | **add** | [[Field]], [[Matrix]], [[Group]], `Set Operation` |
| ~~Continuity~~ | defer (Tier 2) | analysis — when `analysis/` exists |
| ~~Isometry, Lipschitz~~ | after `metric/` | [[Calculus Functions]] has a Lipschitz-1 section already |

## `properties/norm/` and the new `properties/metric/`

| axiom | family | status | consumers |
| --- | --- | --- | --- |
| [[Triangle Inequality]] | norm + **metric section** | exists, extend | [[Metric Space]], [[Lattices]], [[Code Distance]] |
| [[Homogeneity]] | norm | exists | [[Metric Space]], [[Inner-Product Spaces]] |
| [[Positive Definiteness]] | norm | exists | same |
| **Non-negativity** | metric | **add** | [[Metric Space]], [[Code Distance]] |
| **Identity of Indiscernibles** | metric | **add** | same |
| **Distance Symmetry** | metric | **add** | [[Code Distance]], [[Statistical Distance]] |
| ~~Ultrametric, inner-product axioms~~ | defer | [[Inner-Product Spaces]] is composable from `map/` + `norm/` already — rewire rather than add |

**Totals:** 20 axiom notes exist; **11 to add or move**; 12 explicitly deferred with reasons. After this, every structure note in `math/` composes from the library with no inline restatement.

---

# Part V · Filling plan

Six batches, dependency-ordered. Times are focused-work estimates.

```
Batch 0 (moves) ─► A (restore) ─► B (spine) ─► C (axioms) ─► D (rewire) ─► E (hygiene)
                                       │                          ▲
                                       └──────────────────────────┘
                                        D's payoff is why B and C matter
```

## Batch 0 · Move once, before writing anything · ~15 min

Doing the folder moves *first* means every note created later lands in its final home. Obsidian carries the backlinks.

| #   | task                                                                                                                                                                  |      |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| 0a  | **10.1** — `algebra/structures/set theory/` → `math/set theory/`. It holds the objects every Scope line points at; they are not algebra                               | Done |
| 0b  | **10.2** — [[Matrix]], [[Vector Algebra]], [[Kronecker Product]] → `linear algebra/`; [[Metric Space]] → `calculus/` (it is analysis, and Batch D rewrites it anyway) | Done |
| 0c  | Create empty `math/properties/metric/`                                                                                                                                | Done |

## Batch A · Restore the floor · ~30 min · **blocks everything**

| #   | task                                                                                                                                    |      |
| --- | --------------------------------------------------------------------------------------------------------------------------------------- | ---- |
| A1  | Recover **Cartesian Product**, **Set Equality**, **Empty Set** from `git show f9c2c34:"…/Set Theory.md"`                                | Done |
| A2  | Create `Set Operation` (**6.3b**) — the laws table out of [[Set]], plus Cartesian Product, power set, complement, partition (draft 3.2) |      |
| A3  | [[Set]] keeps: definition, equality, empty set, famous sets, notation, universal set. Move Universal Set out of `## Representation`     |      |
| A4  | [[Set Foundation]]: strip the two leading blank lines, add `## Basic Definition`                                                        |      |

**Checkpoint:** no Scope line in the vault refers to an undefined product.

## Batch B · Join the spine · ~1.5–2 h

| #   | task                                                                                                                                                                                                |     |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --- |
| B1  | Rewrite [[Relation]] — heterogeneous first, homogeneous as specialisation, converse, composition, left-total/functional, the specialisation table (draft 3.3)                                       |     |
| B2  | Restructure [[Function]] — six edits incl. the partial-function variant and deleting the duplicate `## Definition` (draft 3.4)                                                         |     |
| B3  | **G1** stray comma; **G2** delete the duplicated many-sorted section from [[Binary Operation]]; **G3** sorts-are-labels + smallness caveat + Birkhoff–Lipson reference in [[Many-Sorted Operation]] |     |
| B4  | Move odd/even functions → [[Calculus Functions]]                                                                                                                                                    |     |

**Checkpoint:** `Set → Relation → Function → Binary Operation` is one linked chain.

## Batch C · Fill the axiom gaps · ~2 h · 11 short notes

| # | task |
| --- | --- |
| C1 | `operation/` — **Cancellativity**, **Absorption** (drafts 3.5, 3.6) |
| C2 | `map/` — **Homomorphism** (draft 3.7) — the biggest single gap |
| C3 | `map/` — move **Injectivity**, **Surjectivity** out of [[Function]]; **Bijectivity** as the composed one-liner (draft 3.8) |
| C4 | `map/` — **Monotonicity**, **Involution** (drafts 3.9, 3.10) |
| C5 | `metric/` — **Non-negativity**, **Identity of Indiscernibles**, **Distance Symmetry**, + `### Metric Form` in [[Triangle Inequality]] (draft 3.11) |

**Checkpoint:** every axiom a math note assumes exists as a note.

## Batch D · Rewire the consumers — **the payoff** · ~2–3 h

This is where the previous three batches turn into read value. Each row deletes a restatement.

| # | task |
| --- | --- |
| D1 | **1.12–1.15** — [[Magma]] / [[Semigroup]] / [[Monoid]]: one definition each, cite a [[Binary Operation]], drop the [[Closure]] links; [[Group]]'s second definition Semigroup → **Monoid** |
| D2 | [[Group]]'s Cancellation proposition → link **Cancellativity**; [[Field]]'s two cancellation rows likewise, and recompose *integral domain* as "commutative ring whose nonzero elements are cancellative" |
| D3 | [[Group Homomorphisms]], [[Ring]], [[Linear Maps]], [[Subgroups]] → link **Homomorphism**; [[Linearity]] gains "the module-signature case of `Homomorphism`" |
| D4 | **5.4 / 5.4b** — rewrite [[Metric Space]]: separate *normed group* from *metric space*, compose both from the axiom notes |
| D5 | **5.5** — [[Code Distance]], [[Rank Metric Codes]] → metric axioms; [[Statistical Distance]] → the same, since total variation *is* a metric |
| D6 | **6.5** — `Set Operation`' laws table → [[Commutativity]] / [[Associativity]] / [[Distributivity]] / [[Idempotence]] / **Absorption** as instances |
| D7 | [[Calculus Functions]]' monotonic section → **Monotonicity**; [[Inner-Product Spaces]] → [[Map Symmetry]] + [[Linearity]] + [[Positive Definiteness]] |

## Batch E · Naming and hygiene · ~45 min

| # | task |
| --- | --- |
| E1 | Rename [[Totality]] → **Connexity**, with the synonyms remark. Three live senses of "total" after B1 make this near-mandatory |
| E2 | **2.10** — the clone-and-edit slips: [[Partial Order]] body says "preorder"; [[Total Order]] title says "Partial Order"; [[Abelian Group]] "Abelian Groups"; [[Field]] callout "Fields"; plural titles in [[Equivalence Relation]], [[Quotient Relation]] |
| E3 | **9.12** — the lint script: callout title vs filename, plus broken links. Run it as the Batch-E checkpoint |
| E4 | **1.6 / 1.10** — [[Algebra Structure]]: restore the axiom index, strip the legacy frontmatter |

## Mine, after yours

- After **B**: [[Algebra MOC]] gains `Set Operation` and the reshaped `set theory/` tree; the spine diagram goes into a `Set Theory MOC` if you want one.
- After **C**: [[Math Properties MOC]] gains the `metric/` family, the new map axioms, and the "one structure-preserving map per family" row.
- After **D**: a review pass — I re-run orphan, broken-link and duplicate audits and report.

## If you only do one batch

**Batch A.** Thirty minutes, and it restores the definition every Scope line in the vault silently depends on.

**If you only do two:** A then D1 — the five-note Magma→Group chain is the vault's showcase, and it currently contains a wrong definition ([[Group]] via [[Semigroup]]) and four disagreeing closure treatments.
