# Foundation Layer — specification, drafts, filling plan

*Everything below is paste-ready or a precise spec. Provenance tagged. House notation.*

> **Link convention in this file.** `Set Operation`, `Homomorphism`, `Injectivity` and `Surjectivity` appear in `code` because they do not exist yet — they become real links as Batch A and C land. Inside the fenced drafts they are already written as wikilinks, ready to paste.

## Status · 2026-08-29

| batch                   | state                                                                                                                                                                                                                                                                  |
| ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **0** moves             | done — `math/set theory/`, 10.2 relocations, `properties/metric/` created                                                                                                                                                                                              |
| **A** restore the floor | **A1–A4 done · A5, A6, A7 still open** — the Cartesian product is defined but [[Set Operation]] still has **zero inbound links**; union / intersection / difference / disjoint union are still undefined; the false law $A-(B-C) = (A-B) \cup C$ is still in the table |
| **B** join the spine    | done — [[Relation]] rewritten heterogeneous-first (with left/right-total, better than the draft), `Function between Sets` → **[[Function]]** restructured with a partial-function variant                                                                              |
| **C** axiom notes       | **9 of 11 done** — `Cancellativity`, `Absorption`, `Injection`, `Surjection`, `Bijection`, `Involution`, `Monotonicity` created. **Missing: `Homomorphism`** (the biggest gap) and the whole **`metric/` family** — see the revised §3.11                              |
| **D** rewire            | open                                                                                                                                                                                                                                                                   |
| **E** hygiene           | open                                                                                                                                                                                                                                                                   |

Batches B and C ran ahead of A. The floor items are three edits and about fifteen minutes; they block nothing else technically, but every Scope line in `properties/` still points at a product that no note links.



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

| family | attaches to | Scope line reads | structures produced |
| --- | --- | --- | --- |
| `properties/operation/` | binary operation $\star: S \times S \to S$ | "A [[Binary Operation]] $\star$ on $O$" | [[Magma]] → [[Group]] → [[knowledge/math/algebra/structures/rings/Ring]] → [[Field]] |
| `properties/relation/` | homogeneous relation $R \subseteq S \times S$ | "A [[Relation]] $R$ on $S$" | [[Preorder]] → [[Total Order]]; [[Equivalence Relation]] |
| `properties/map/` | function $f: A \to B$ | "A [[Function]] $f: A \to B$" | homomorphism, linear map, monotone map |
| `properties/norm/`, `metric/` | function $V \to \mathbb R$ or $X \times X \to \mathbb R$ | "A function $N: V \to \mathbb R$" | normed space, [[Metric Space]] |

There is a pleasing regularity here that the vault can state once and reuse: **each object family has its own notion of structure-preserving map.** Algebra has homomorphisms, orders have monotone maps, metric spaces have isometries (and, loosened, continuous maps), categories have functors. That is one row per family, and it is the row `properties/map/` is currently missing.

---

# Part II · Audit

## F1 · Cartesian Product no longer exists — **half-resolved**: defined in [[Set Operation]], still linked from nowhere

`Set.md` lists $\times$ in a symbol table and never defines it. `Set Foundation.md` does not have it. Nothing in `knowledge/` defines it.

It was in the old `Set Theory.md` and was dropped when task 6.3 split that note. Recoverable verbatim from git:

```
git show f9c2c34:"knowledge/math/algebra/structures/set theory/Set Theory.md"
```

This is the most load-bearing definition in the vault. Every Scope line — $R \subseteq S \times S$, $f: A \to B$, $\star: S \times S \to S$, $\mathsf{Hom}(B,C) \times \mathsf{Hom}(A,B)$ — is written in terms of a product that is currently undefined. It is exactly what precision-skeleton rule 5 exists to catch.

**Also lost in the same split:** `Set Equality` and `Empty Set`. Same commit, same recovery.

## F2 · `Relation.md` is homogeneous-only — **resolved**

> "A **relation** on a set $S$ is a subset $R$ of the product $S \times S$."

Correct as far as it goes, but it makes `Relation` unable to serve as the parent of `Function`, and it means "relation from $A$ to $B$" has no home. Fix: define the heterogeneous case first, homogeneous as the specialisation $A = B$.

## F3 · `Function.md` had two definition blocks — **merged; one sub-problem left**

The note opened with the graph $\Gamma_f$ formulation (good) and *ended* with a second definition block absorbed from the old `Function.md` in task 7.7, redefining Function, Domain, Co-domain, Range, plus odd/even functions. It now carries a single `## Definition`. Three sub-problems came out of it:
- **Range** duplicates **Image**, defined 100 lines apart with different words. — **still open**; both `### Range` and `### Image` are live.
- **Odd / even function** is analysis, not the foundation layer — it moved to [[Calculus Functions]] (it needs an additive inverse on the domain, which sets do not have). — **done** (B4).
- The bottom definition — "a set of ordered pairs no two of which have the same first member" — omits totality, so it is *literally the definition of a partial function*. It became `### Partial Function` under `## Variant` rather than a duplicate to delete. — **done**.

## F4 · Small errors in the same note

- "A function $f: A \rightarrow$ is **surjective**" — missing codomain.
- "We often **right** $f$" → write.
- `### Inversion` heading over an `[!definition] Inverse` callout.

## F5 · Injective / surjective / bijective filed as object content — **resolved**, moved to `properties/map/` as `Injection`, `Surjection`, `Bijection`

They sit in `Function.md`'s `## Property` section. By the vault's own rule they belong in `properties/map/` — their Scope is "a map $f: A \to B$", identical in shape to [[Linearity]].

The precedent is already set on the algebra side: [[Inverse Element]] states the axiom, [[Group]] holds the *theorems* about it (uniqueness, cancellation). Apply the same split here — `properties/map/Injectivity.md` states the axiom; `Function.md` keeps the theorems (injective ⟺ monomorphism, left-inverse ⟺ injective, canonical decomposition).

## F6 · `Set Foundation.md` opened with two blank lines and no `## Definition` — **half done**

The blank lines are gone and the heading exists, but `## Definition` is still **empty** — the note jumps straight to `## Cardinality`. Either fill it (the signature $\in$ plus the axiom list) or drop the heading; an empty one is worse than neither.

## F7 · The axiom families have gaps with existing consumers

Detailed in Part IV. The short version: **cancellativity** (3 consumers, currently a theorem in two places), **homomorphism** (4 consumers, defined inline twice), **the metric axioms** (4 consumers including [[Statistical Distance]], which *is* a metric), and **monotonicity** (the missing row of the structure-preserving-map table).

---

# Part III · Note drafts

## F0 — Primitives

### 3.1 `Set.md` — three restorations **[Standard]**

Add to `## Definition`, after the Set callout (recovered from `f9c2c34`):

```markdown
> [!definition] Set Equality
> Two sets $A$ and $B$ are **equal**, written $A = B$, if they consist of exactly the same elements. If one contains an element the other does not, they are unequal, written $A \neq B$.

> [!definition] Empty Set
> The set with no elements, $\emptyset = \{\}$, is the **empty set** (also null set, void set). For any set $A$, $\emptyset \subseteq A$.
```

Move `### Universal Set` out of `## Representation` — it is not a notation, it is a convention about a fixed ambient set — and place it just before `## Operation`, where `complement` needs it.

Then, per 6.3b, cut everything from `## Operation` onward into the new note below, leaving `Set.md` as: what a set is, equality, empty set, famous sets, roster/comprehension, universal set, and a link out.

---

### 3.2 `Set Operation.md` — NEW **[Standard]**

Carries the ~20-row laws table out of `Set.md` (task 6.3b) *and* restores the Cartesian product.

```markdown
## Definition

### Inclusion

| Symbol | Meaning |
| --- | --- |
| $\in$ | belongs to |
| $\subseteq$ | subset |
| $\subset, \subsetneq$ | proper subset |
| $\lvert S \rvert$ | number of elements |
| $2^S$, $\mathcal P(S)$ | power set |

> [!definition] Power Set
> The **power set** of $S$, written $\mathcal P(S)$ or $2^S$, is the set of all subsets of $S$.

### Operations

| Symbol | Operation |
| --- | --- |
| $\cup$ | union |
| $\cap$ | intersection |
| $\setminus$ | difference |
| $\amalg$ | disjoint union |
| $\times$ | Cartesian product |

> [!definition] Cartesian Product
> The **Cartesian product** of sets $A$ and $B$, written $A \times B$, is the set of **ordered** pairs
> $$A \times B = \{(x, y) \mid x \in A \text{ and } y \in B\}.$$
> The $n$-fold product $A_1 \times \cdots \times A_n$ consists of $n$-tuples; $A^n$ abbreviates the $n$-fold product of $A$ with itself.

> [!remark] Why this definition carries the vault
> Every Scope line in `properties/` is written over a product: a [[Relation]] is a subset of $A \times B$, a [[Function|function]] is a special relation, a [[Binary Operation]] is a function $S \times S \to S$. Ordered pairs are taken as primitive here; the set-theoretic construction $(x,y) := \{\{x\},\{x,y\}\}$ is a foundational detail, noted in [[Foundations of Mathematics]] and used nowhere else.

> [!definition] Disjoint
> $S$ and $T$ are **disjoint** if $S \cap T = \emptyset$.

> [!definition] Complement
> The **complement** of $T$ in $S$ is $S \setminus T$ — the elements of $S$ not in $T$. Written $T^c$ when the universal set is understood.

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

## Definition

> [!definition] Relation
> A **(binary) relation** from a set $A$ to a set $B$ is a subset
> $$R \subseteq A \times B.$$
> When $(a, b) \in R$ we say $a$ and $b$ are **related by $R$** and write $a \; R \; b$.

> [!definition] Homogeneous Relation
> A relation on a single set $S$ is the case $A = B = S$, i.e. $R \subseteq S \times S$. These are the relations the [[Math Properties MOC|relation axioms]] apply to — [[Reflexivity]], [[Symmetry]], [[Antisymmetry]], [[Transitivity]], [[Totality]] all compare two elements of the *same* set.

### Associated Sets

> [!definition] Domain, Range
> $$\mathsf{dom}(R) = \{a \in A \mid \exists b: a \; R \; b\}, \qquad \mathsf{ran}(R) = \{b \in B \mid \exists a: a \; R \; b\}.$$

## Variant

### Converse

> [!definition] Converse Relation
> $R^{-1} \subseteq B \times A$ is defined by $b \; R^{-1} a \iff a \; R \; b$.

### Composition

> [!definition] Composition of Relations
> For $R \subseteq A \times B$ and $S \subseteq B \times C$:
> $$S \circ R = \{(a, c) \mid \exists b \in B: a \; R \; b \text{ and } b \; S \; c\} \subseteq A \times C.$$
> Composition of [[Function|functions]] is this operation restricted to functional relations. It is [[Associativity|associative]], and the identity relation $\{(a,a)\}$ is its [[Identity Element|identity]] — so relations on $S$ form a [[Monoid]] under $\circ$.

## Property — toward functions

> [!definition] Left-Total, Functional
> $R \subseteq A \times B$ is
> - **left-total** if every $a \in A$ is related to at least one $b$;
> - **functional** (right-unique, single-valued) if each $a$ is related to at most one $b$.

> [!remark] Function = left-total + functional
> A [[Function|function]] $A \to B$ is exactly a relation that is both. Dropping left-totality gives a **partial function**; dropping functionality gives a multivalued relation.
> 
> Beware the word *total*: **left-total** here (defined on all of $A$) is unrelated to [[Totality]] on a homogeneous relation ($\forall x, y:\ xRy \lor yRx$), and unrelated again to a *total* function. This vault has all three senses live — the reason [[Totality]] should be renamed **Connexity**.

## Specialisation

| add | get |
| --- | --- |
| [[Reflexivity]] + [[Transitivity]] | [[Preorder]] |
| + [[Antisymmetry]] | [[Partial Order]] |
| + [[Totality]] | [[Total Order]] |
| [[Reflexivity]] + [[Symmetry]] + [[Transitivity]] | [[Equivalence Relation]] |
| left-total + functional | [[Function]] |
```

That final table is the spine, stated at the node where it branches — and it makes `Relation.md` the hub of the object layer rather than a one-line stub.

---

### 3.4 `Function.md` — RESTRUCTURE **[Standard]**

Keep the graph definition, the image / restriction / composition / projections / canonical-decomposition material, and the mono/epi theorems. Six edits:

1. **Open by placing it on the spine.** Add under the existing definition:
   ```markdown
   > [!remark]
   > Equivalently: a function is a [[Relation]] $\Gamma_f \subseteq A \times B$ that is left-total and functional. The condition $(\forall a)(\exists! b)$ above says exactly that.
   ```
2. **Delete the trailing `## Definition` block**, redistributing it:
   - *Domain / Co-domain* → keep, fold into `## Definition`.
   - *Range* → delete; it duplicates **Image** (or keep as a one-line synonym remark).
   - *Function equality theorem* → keep, move up beside the definition.
   - *Odd / Even function* → **move to [[Calculus Functions]]** (needs additive inverse; not a set-theoretic notion).
   - *"a set of ordered pairs no two of which have the same first member"* → repurpose as the **partial function** definition, below.
3. **Add the partial function variant** — this closes the dependency [[Binary Operation#Partial Operation]] currently dangles on:
   ```markdown
   ### Partial Function

   > [!definition] Partial Function
   > A **partial function** $f: A \rightharpoonup B$ is a functional relation that need not be left-total: each $a \in A$ has *at most* one image. Its **domain of definition** is $\mathsf{dom}(\Gamma_f) \subseteq A$.
   > 
   > Division on $\mathbb R$ is the standard example; see [[Binary Operation#Partial Operation]].
   ```
4. **Move injective / surjective / bijective out** to `properties/map/` (F5). What stays here is the theorems: left-inverse ⟺ injective, right-inverse ⟺ surjective, bijection ⟺ two-sided inverse, injective ⟺ monomorphism, surjective ⟺ epimorphism.
5. **Fix F4**: the missing $B$ in the surjective definition, "right" → "write", `### Inversion` → `### Inverse`.
6. **Add the composition remark** pointing at [[Relation#Composition]], so the two composition definitions are one concept stated once.

---

## F2 — New axioms

All follow the Scope / Condition / Property template unchanged. Each has named existing consumers; nothing speculative.

### 3.5 `properties/operation/Cancellativity.md` **[Standard]** — 3 consumers

```markdown
## Definition

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
## Definition

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

## Definition

> [!definition] Homomorphism
> ### Scope
> A [[Function|map]] $\varphi: A \rightarrow B$.
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

Instances to rewire: [[Group Homomorphism]] ($\varphi(g_1 \star g_2) = \varphi(g_1) \star \varphi(g_2)$), [[knowledge/math/algebra/structures/rings/Ring]]'s inline ring homomorphism, [[Linear Maps]] (a homomorphism of modules — [[Linearity]] is this note's specialisation to the module signature), and [[Subgroup]], whose definition *is* "the inclusion is a group homomorphism".

---

### 3.8 `properties/map/Injectivity.md`, `Surjectivity.md` **[Standard]**

Moved out of [[Function]] (F5), verbatim apart from the missing $B$:

```markdown
> [!definition] Injectivity
> ### Scope
> A [[Function|map]] $f: A \rightarrow B$.
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
> A [[Function|map]] $f: A \rightarrow B$.
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
## Definition

> [!definition] Monotonicity
> ### Scope
> A [[Function|map]] $f: A \rightarrow B$.
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
> A [[Function|map]] $f: A \rightarrow A$.
> 
> ---
> ### Property
> $f$ is an **involution** iff $f \circ f = \mathrm{id}_A$, i.e. $\forall x \in A: f(f(x)) = x$.
> Every involution is a bijection, and is its own inverse.
```

Consumers: complex conjugation and $-(-a) = a$ in [[Field]]; matrix transpose in [[Matrix]]; $(a^{-1})^{-1} = a$ in [[Group]]; set complement in `Set Operation`.

---

### 3.11 `properties/metric/` — the family, **revised 2026-08-29** **[Standard]**

> [!warning] Correction to the earlier draft
> This section previously proposed a **Non-negativity** axiom and kept `norm/` and `metric/` as separate folders. Both were wrong. See the reasoning below.

**Merge `norm/` into `metric/`. Four notes, not six.**

Two axioms turn out to be the same axiom in two scopes, and one proposed axiom is a theorem:

| axiom | norm scope $N: V \to \mathbb R$ | metric scope $d: X \times X \to \mathbb R$ |
| --- | --- | --- |
| **Positive Definiteness** | $\lVert x \rVert = 0 \iff x = 0$ | $d(x,y) = 0 \iff x = y$ |
| **Triangle Inequality** | $\lVert x + y \rVert \leq \lVert x \rVert + \lVert y \rVert$ | $d(x,z) \leq d(x,y) + d(y,z)$ |
| **Distance Symmetry** | — *(automatic, see below)* | $d(x,y) = d(y,x)$ |
| **Homogeneity** | $\lVert \alpha x \rVert = \lvert \alpha \rvert \lVert x \rVert$ | — |

Under the induced metric $d(x,y) = \lVert x - y \rVert$, positive definiteness **is** identity of indiscernibles. So the two families share two of their axioms outright, and each contributes one of its own.

> [!danger] Non-negativity is a theorem, not an axiom — drop it
> **Metric:** identity of indiscernibles gives $d(x,x) = 0$; then triangle with $z = x$ plus symmetry gives
> $$0 = d(x,x) \leq d(x,y) + d(y,x) = 2\,d(x,y) \implies d(x,y) \geq 0.$$
> **Norm:** homogeneity at $\alpha = 0$ gives $\lVert 0 \rVert = 0$, and $\lVert -x \rVert = \lvert -1 \rvert \lVert x \rVert = \lVert x \rVert$; then
> $$0 = \lVert x + (-x) \rVert \leq \lVert x \rVert + \lVert -x \rVert = 2 \lVert x \rVert \implies \lVert x \rVert \geq 0.$$
> Writing it as an axiom violates precision rule 3 — *consequences never live inside definition callouts*. It belongs as a `[!proposition]` in [[Metric Space]].
>
> **This also means the existing [[Positive Definiteness]] note is wrong as written**: its first bullet, $\lVert x \rVert \geq 0$, is derivable and should go. Keep only the separation property.

> [!remark] Homogeneity buys symmetry
> A norm needs no symmetry axiom because it comes free: $d(y,x) = \lVert y - x \rVert = \lVert -(x-y) \rVert = \lVert x - y \rVert = d(x,y)$, using homogeneity at $\alpha = -1$. That is why the metric family has an axiom the norm family does not.

### The four notes

Folder: `properties/metric/`. Scope lines carry the precision; the folder name is navigation.

```markdown
> [!definition] Positive Definiteness
> ### Scope
> A function $d: X \times X \rightarrow \mathbb R$ on a set $X$.
> 
> ---
> ### Property
> $d$ separates points iff
> $$\forall x, y \in X: \quad d(x, y) = 0 \iff x = y$$

### Norm Form

> [!definition] Positive Definiteness (norm)
> ### Scope
> A function $N = \lVert \cdot \rVert : V \rightarrow \mathbb R$.
> 
> ---
> ### Property
> $$\forall x \in V: \quad \lVert x \rVert = 0 \iff x = 0$$
> The case $d(x,y) = \lVert x - y \rVert$ of the metric form above.
```

```markdown
> [!definition] Distance Symmetry
> ### Scope
> A function $d: X \times X \rightarrow \mathbb R$.
> 
> ---
> ### Property
> $$\forall x, y \in X: \quad d(x, y) = d(y, x)$$
> 
> ### Remark
> Distinct from relation [[Symmetry]] and from [[Map Symmetry]] — same word, third scope. Automatic for a metric induced by a norm, by [[Homogeneity]] at $\alpha = -1$.
```

`Triangle Inequality` keeps its existing norm statement and gains a `### Metric Form`; `Homogeneity` moves across unchanged.

### Why one folder, and why `metric`

- **Two folders for four notes is thin**, and two of the four would have to appear in both.
- **The tree stays at four families** — operation, relation, map, metric — matching the four attachment points on the spine. Norm and metric attach at the same one: a map into $\mathbb R$.
- **`metric` is the better name.** It is the weaker setting (needs only a set, not a vector space), it is the terminal end of the chain *inner product → norm → metric*, and more consumers are metrics-without-norms — [[Code Distance]] (Hamming), [[Rank Metric Codes]], [[Statistical Distance]] (total variation) — than the reverse, of which there are none, since every norm induces a metric.
- **The move is free.** Obsidian resolves wikilinks by basename, so relocating the three existing notes from `norm/` to `metric/` breaks nothing.


---

---

### 3.12 Nilpotency in rings — two notes **[Standard]**

**First, a correction to the request.** *"Nilpotent ring"* is a real term, but in this vault it is **vacuous**. [[Ring]] here is a [[Monoid]] under $*$, so it is unital; a nilpotent ring means $R^n = 0$ (every product of $n$ elements vanishes), and then $1 = 1^n = 0$, so $R$ is the [[Zero Ring]]. The term only has content for **rngs** (non-unital) or, usefully, for **ideals**. So the material splits three ways, and only the first two want notes:

| notion | what it is | where |
| --- | --- | --- |
| **nilpotent element** | $x^n = 0$ | `rings/Nilpotent Element.md` — a predicate on elements, next to `Unit` and `Zero Divisor` |
| **reduced ring** | no nonzero nilpotents | `rings/special rings/Reduced Ring.md` — a mixin over [[Ring]] |
| **nil / nilpotent ideal** | $I$ all-nilpotent / $I^n = 0$ | a `###` section of `Nilpotent Element` until `Ideal.md` is promoted out of [[Ring]] |

Under the class/instance vocabulary: `Reduced Ring` is `Extends: [[Ring]]` — one axiom, no new data, exactly Mathlib's `class IsReduced`. `Nilpotent Element` is a predicate, not a class, exactly Mathlib's `IsNilpotent x`. Same split, arrived at independently.

**Blocker.** Both drafts link `[[Unit]]` and `[[Zero Divisor]]`, which are still headings inside [[Ring]]. **This makes S3 a prerequisite, not a nicety** — precision rule 5, a dependency a definition uses but cannot link.

#### A · `rings/Nilpotent Element.md`

```markdown
Reference:
- Atiyah–Macdonald, *Introduction to Commutative Algebra*, Ch. 1
- Lam, *A First Course in Noncommutative Rings*, §10 — the noncommutative side

## Definition

> [!definition] Nilpotent Element
> ### Scope
> A [[Ring]] $R$, with zero $0$.
>
> ---
> ### Property
> An element $x \in R$ is **nilpotent** iff
> $$\exists n \in \mathbb Z_{\geq 1}: x^n = 0.$$
> The least such $n$ is the **index of nilpotency** of $x$.

> [!remark]
> $0$ is the only nilpotent of index $1$; every other nilpotent has index $\geq 2$.

## Property

### Nilpotents are zero divisors

> [!proposition]
> A nonzero nilpotent $x$ of index $n$ is a [[Zero Divisor]]: $x \cdot x^{n-1} = 0$, and $x^{n-1} \neq 0$ by minimality of $n$.

### Nilpotents and units

> [!proposition]
> If $x$ is nilpotent of index $n$, then $1 - x$ is a [[Unit]]:
> $$(1 - x)^{-1} = 1 + x + x^2 + \dots + x^{n-1}.$$
> No commutativity is needed — the powers of $x$ commute with each other.

> [!corollary]
> If $u$ is a unit, $x$ is nilpotent, and $ux = xu$, then $u + x$ is a unit. In a [[Commutative Ring]]: *unit $+$ nilpotent $=$ unit.*

> [!proposition]
> In a nonzero ring no nilpotent is a unit — if $x$ were invertible so would $x^n = 0$ be, forcing $1 = 0$.

### Nilpotent and idempotent

> [!proposition]
> The only element that is both nilpotent and [[Idempotence|idempotent]] is $0$: from $x^2 = x$ we get $x = x^2 = \dots = x^n = 0$.

### Sums — where commutativity is required

> [!theorem]
> Let $R$ be a [[Commutative Ring]] with $x^m = 0$ and $y^n = 0$. Then $(x + y)^{m + n - 1} = 0$.
>
> *Proof.* Expand by the binomial theorem. In each term $\binom{m+n-1}{i} x^i y^{m+n-1-i}$ either $i \geq m$ or $m+n-1-i \geq n$, so every term vanishes.

> [!remark] Commutativity is a side condition, not decoration
> In $M_2(k)$, $e_{12} = \begin{pmatrix}0&1\\0&0\end{pmatrix}$ and $e_{21} = \begin{pmatrix}0&0\\1&0\end{pmatrix}$ are nilpotent of index $2$, but
> $$e_{12} + e_{21} = \begin{pmatrix}0&1\\1&0\end{pmatrix}, \qquad (e_{12} + e_{21})^2 = I.$$
> Their sum is a unit. In a noncommutative ring the nilpotents need not be closed under addition at all.

### Nilradical

> [!definition] Nilradical
> For a [[Commutative Ring]] $R$, $\;\mathfrak N(R) = \{x \in R : x \text{ nilpotent}\}$.

> [!theorem]
> $\mathfrak N(R)$ is an ideal — closed under addition by the theorem above, and under scaling since $(rx)^m = r^m x^m = 0$. The quotient $R / \mathfrak N(R)$ is [[Reduced Ring|reduced]].

> [!theorem] Krull
> In a commutative ring with $1$, $\mathfrak N(R)$ is the intersection of all prime ideals of $R$.

### Nil and nilpotent ideals

> [!definition]
> An ideal $I \subseteq R$ is **nil** iff every element of $I$ is nilpotent, and **nilpotent** iff $I^n = 0$ for some $n$ — every product of $n$ elements of $I$ vanishes.

> [!proposition]
> Nilpotent $\Rightarrow$ nil. The converse fails: in $k[x_1, x_2, \dots]/(x_1^2, x_2^3, x_3^4, \dots)$ the ideal $(x_1, x_2, \dots)$ is nil but not nilpotent. It does hold when $I$ is finitely generated — so in a Noetherian commutative ring $\mathfrak N(R)$ is nilpotent.

> [!remark]
> A *unital* ring is never nilpotent unless it is the [[Zero Ring]]: $R^n = 0$ gives $1 = 1^n = 0$. "Nilpotent ring" is a statement about rngs and ideals, not about the objects [[Ring]] defines.

## Example

- $\mathbb Z / p^k$: the nilpotents are exactly the multiples of $p$. In $\mathbb Z/m$, $x$ is nilpotent iff every [[Prime]] dividing $m$ divides $x$.
- **Dual numbers** $k[\varepsilon]/(\varepsilon^2)$ — the smallest interesting nonzero nilpotent, and the reason non-reduced rings exist in geometry.
- Strictly upper-triangular matrices in [[Matrix|$M_n(k)$]] — nilpotent of index $\leq n$.
- [[Polynomial Ring]]: for commutative $R$, $f = \sum a_i x^i$ is nilpotent iff every $a_i$ is; and $f$ is a unit iff $a_0$ is a unit and $a_1, \dots, a_d$ are nilpotent.
- [[Integral Domain]] and [[Field]] — no nonzero nilpotents at all.

## Related

- [[Reduced Ring]] — the rings this predicate is empty in
- [[Operators]] — the same predicate for a linear operator, where $N^{\dim V} = 0$ comes for free
```

#### B · `rings/special rings/Reduced Ring.md`

```markdown
Reference: Atiyah–Macdonald Ch. 1; Mathlib `IsReduced`

## Definition

> [!definition] Reduced Ring
> ### Scope
> A [[Ring]] $R$.
>
> ---
> ### Property
> $R$ is **reduced** iff its only [[Nilpotent Element|nilpotent]] is $0$:
> $$\forall x \in R: x^2 = 0 \implies x = 0.$$

> [!remark] Index 2 is enough
> The index-$2$ condition kills every nilpotent. If $x^n = 0$ with $n \geq 2$ minimal, then $(x^{n-1})^2 = x^{2n-2} = 0$ since $2n - 2 \geq n$, so $x^{n-1} = 0$ — contradicting minimality.

## Property

> [!proposition] The chain
> [[Field]] $\Rightarrow$ [[Integral Domain]] $\Rightarrow$ reduced.
> Neither converse holds: $\mathbb Z$ is a domain and not a field; $\mathbb Z \times \mathbb Z$ is reduced and not a domain, since $(1,0)(0,1) = (0,0)$.

> [!proposition]
> $R$ is reduced iff $\mathfrak N(R) = 0$, and $R/\mathfrak N(R)$ is reduced for every commutative $R$.

## Related

- [[Nilpotent Element]] · [[Integral Domain]] · [[Commutative Ring]]
```

#### The bridge to linear algebra

[[Operators]] already defines nilpotent for an operator and proves $N^{\dim V} = 0$. That is the **same predicate in a different idiom** — a two-views pair in the [[North Star]] sense, cross-domain shape. One remark on the ring side (*"for $R = \mathcal L(V)$ this is [[Operators]]' nilpotent operator, where the index is bounded by $\dim V$"*) and one on the operator side is the whole bridge; do not restate the theory twice.


---

### 3.13 `Kernel` — one note, and three that stay put **[Standard]**

**It is already in the vault three times, and the general one is unnamed.**

| where | what it says | reading |
| --- | --- | --- |
| [[Function]] `### Canonical Decomposition` | *"$a' \sim a'' \iff f(a') = f(a'')$"* — **the kernel, never called that** | B |
| [[Subgroup]] `### Kernel` | $\ker \phi = \phi^{-1}(e_{G'})$ | A |
| [[Linear Maps]] `### Null Spaces and Ranges` | *"null space (or kernel)"*, $\{v : Tv = 0\}$ | A |
| [[knowledge/math/algebra/structures/rings/Ring]] | ring homs and [[Ideal]]s are both defined — **but never connected** | A, missing |

#### Two readings, and they are not the same concept

|  | **A · sub-object** | **B · equivalence relation** |
| --- | --- | --- |
| definition | $\ker f = f^{-1}(0)$ | $x \sim_f y \iff f(x) = f(y)$ |
| Scope needs | a zero / identity **in the codomain** | **nothing** — any [[Function]] between bare sets |
| yields | a normal subgroup, an ideal, a subspace | a partition, hence a [[Quotient Relation]] |
| categorically | equalizer of $(f, 0)$ — needs zero morphisms | the *kernel pair*, a pullback — needs nothing |

**Revised 2026-09-04 — the sub-object reading *is* general; what is not general is the choice of *which* sub-object.**

For any [[Function]] $f: A \to B$ and any $b \in B$ the **fibre** $f^{-1}(b) \subseteq A$ exists. Fibres are perfectly general. So:

> **A is one distinguished fibre. B is the whole fibre partition.**
> $\ker f$ (sub-object) is the fibre over the basepoint; $\sim_f$ (relation) is the partition into all fibres.

Reading A therefore needs exactly one extra thing: **a distinguished point in the codomain** to take the fibre over. A bare set has none. And recovering B from A needs a *second* thing — a way to translate one fibre onto the others.

They **coincide exactly for group-like structures**, because inverses give that translation: $x \sim_f y \iff xy^{-1} \in \ker f$. That coincidence *is* the first isomorphism theorem, and it is why nobody distinguishes the two readings in a group theory course.

They **come apart one step outside groups**:

> [!remark] A monoid homomorphism can have trivial kernel and not be injective
> Let $f : (\mathbb N, +) \to (\{0,1\}, \max)$ with $f(0) = 0$ and $f(n) = 1$ for $n > 0$. This is a [[Monoid]]
> homomorphism, and $f^{-1}(0) = \{0\}$ is trivial — yet $f(1) = f(2)$, so $f$ is not an [[Injection]].
> Reading **A** has lost the information; reading **B** still has it.

This is a **two-views pair of the *non-equivalent* shape** ([[North Star]]): the surviving direction and the separating example are the content. Do not merge them.

#### The criterion, not the list

The varieties where one fibre determines the whole congruence are the **$0$-regular** (ideal-determined) ones: those with a constant $0$ and a **Mal'cev term** $p(x,y,z)$ satisfying $p(x,x,z) = z$ and $p(x,z,z) = x$. For [[Group]] it is $p(x,y,z) = xy^{-1}z$; [[knowledge/math/algebra/structures/rings/Ring]] and modules inherit it from their additive group. [[Monoid]], [[Semigroup]], lattices and orders have no such term — which is precisely why the counterexample above exists. **[Standard]** — universal algebra, the same frame as [[Equational Logic]].

So the rule is checkable rather than memorised: *ask whether the structure has $xy^{-1}z$.*

#### What category theory says

| notion | needs | exists in $\mathbf{Set}$? |
| --- | --- | --- |
| **subobject** (a mono up to iso) | nothing | yes — fully general |
| **image** (subobject of the **codomain**) | an epi–mono factorization | yes |
| **kernel** = $\mathrm{eq}(f, 0)$ (subobject of the **domain**) | **zero morphisms** | **no** — $\mathbf{Set}$ has no zero object |
| **kernel pair** $A \times_B A \rightrightarrows A$ | pullbacks | yes — and it *is* $\sim_f$ |

So the asymmetry is real and it is not about sub-objects being special: on the **codomain** side the general object is a subobject ([[Function]]'s `### Image`), and on the **domain** side the general object is a *relation*. That is exactly why `Image` sits comfortably inside [[Function]] and `Kernel` does not.

#### Placement

**First, `### Fibre` goes into [[Function]]**, beside `### Image`, as the domain-side counterpart — $f^{-1}(b) = \{a \in A : f(a) = b\}$. General, derived, one line. It stays inside [[Function]] until a second note outside its parent needs it.

**Then one new note: `math/set theory/function/Kernel.md`** — reading **B**, *the partition into fibres*. It graduates by the usual rule: three notes outside its parent need to link it ([[Subgroup]], [[knowledge/math/algebra/structures/rings/Ring]], [[Linear Maps]]), and its Scope is a bare function, so it belongs beside [[Function]] rather than inside any structure.

```markdown
Reference: Aluffi, *Algebra: Chapter 0*, §I.2 (canonical decomposition)

## Definition

> [!definition] Kernel
> ### Scope
> A [[Function]] $f : A \rightarrow B$.
>
> ---
> ### Property
> The **kernel** of $f$ is the [[Equivalence Relation]] $\sim_f$ on $A$ given by
> $$a' \sim_f a'' \iff f(a') = f(a'').$$
> Equivalently: the partition of $A$ into the non-empty fibres $f^{-1}(b)$, $b \in \operatorname{im} f$.

## Property

> [!theorem] Canonical decomposition
> Every $f$ factors as $A \twoheadrightarrow A/{\sim_f} \xrightarrow{\ \tilde f\ } \operatorname{im} f \hookrightarrow B$,
> with $\tilde f([a]) = f(a)$ a bijection — the [[Quotient Relation|quotient]] by the kernel, a bijection, and an inclusion.

> [!proposition]
> $f$ is an [[Injection]] iff $\sim_f$ is the identity relation.

## Related

- [[Subgroup]] · [[knowledge/math/algebra/structures/rings/Ring]] · [[Linear Maps]] — the sub-object reading, one per structure
```

**Reading A stays with each structure.** It is not one concept: the Scopes differ and all the content is structure-specific.

| note | do |
| --- | --- |
| [[Subgroup]] | keep `### Kernel`; add *"and is a **normal subgroup**"* — currently unstated. Phrase it as *the fibre over $e_{G'}$* so the link to `Kernel.md` is visible |
| [[knowledge/math/algebra/structures/rings/Ring]] | **add** the missing link: the kernel of a ring homomorphism **is an [[Ideal]]**, and conversely every ideal is the kernel of its quotient map. Right now [[Ideal]] appears with no reason for existing — and is defined **twice**, once well at `groups/subgroups/Ideal.md` and once weakly inline here. Delete the inline copy, link the note, and move the note to `rings/` (its Scope needs a ring) |
| [[Linear Maps]] | keep; add a one-line synonym remark — *null space* and *kernel* are the same thing, and [[Subgroup]] uses the other word |

Then one `[!remark]` in `Kernel.md` carrying the A ⟷ B bridge and the monoid counterexample. That is the whole design: **one note for the reading with no Scope requirements, one section per structure for the reading that has them.**

#### Two things it surfaces

- The **dual is muddled**. Kernel's dual is image, and [[Function]] still carries both `### Range` and `### Image` (the last open piece of **F3**), while [[Linear Maps]] uses *range* to mean image. Settle that in the same pass, or `Kernel.md`'s decomposition theorem will link a word with two meanings.
- **`kernelization`** in [[Parameterized Complexity]] is a *different word* — instance compression, no relation. One disambiguation line in `Kernel.md`. The OS kernel appears only in prose (`ASM`, `security/rev`), so the bare name is free today.


# Part IV · Complete axiom inventory

Every axiom the vault has, needs, or should deliberately not write. **Consumer rule applied throughout** — nothing is proposed without a note that already wants it.

## `properties/operation/` — Scope: a binary operation $\star: O \times O \to O$

| axiom                              | status                          | consumers                                                    |
| ---------------------------------- | ------------------------------- | ------------------------------------------------------------ |
| [[Closure]]                        | exists (subset reading)         | [[Subgroup]] (3.6) — and *only* subgroups, once 1.12 lands  |
| [[Associativity]]                  | exists                          | [[Semigroup]] onward; [[Category]]; [[Relation]] composition |
| [[Commutativity]]                  | exists                          | [[Abelian Group]], [[Commutative Ring]], `Set Operation`     |
| [[Identity Element]]               | exists                          | [[Monoid]] onward; [[Category]]                              |
| [[Inverse Element]]                | exists                          | [[Group]] onward; [[Field]]                                  |
| [[Distributivity]]                 | exists                          | [[Ring]]; `Set Operation`                                    |
| [[Idempotence]]                    | exists — **currently orphaned** | `Set Operation`; lattices via `Absorption`                   |
| [[Alternativity]]                  | exists                          | octonions in [[Algebra Structure]]                           |
| **Cancellativity**                 | **add**                         | [[Group]] (thm), [[Field]] (2 rows + integral domain)        |
| **Absorption**                     | **add**                         | `Set Operation`; lattice (2.14)                              |
| ~~Annihilator / zero element~~     | defer                           | a *theorem* in rings ($0 \cdot a = 0$), not an axiom         |
| ~~Nilpotency, anti-commutativity~~ | defer                           | no consumer — needs Lie algebras or cross products           |

## `properties/relation/` — Scope: a homogeneous relation $R \subseteq S \times S$

| axiom | status | consumers |
| --- | --- | --- |
| [[Reflexivity]] | exists | [[Preorder]], [[Equivalence Relation]] |
| [[Symmetry]] | exists | [[Equivalence Relation]] |
| [[Antisymmetry]] | exists | [[Partial Order]] |
| [[Transitivity]] | exists | [[Preorder]], [[Equivalence Relation]] |
| [[Connexity]] | exists — **rename `Connexity`** | [[Total Order]]; the word now collides three ways (see 3.3) |
| ~~Irreflexivity, Asymmetry, Trichotomy~~ | defer | strict orders — no note wants them yet |
| ~~Well-foundedness~~ | optional | [[Proofs]]' induction principle is the one candidate |

## `properties/map/` — Scope: a map $f: A \to B$

| axiom | status | consumers |
| --- | --- | --- |
| [[Linearity]] | exists | [[Linear Maps]], [[Vector Spaces]] |
| [[Bilinearity]] | exists | [[Bilinear Pairings]], [[Split-R1CS]] |
| [[Multilinearity]] | exists | [[Bilinear Pairings]] |
| [[Map Symmetry]] | exists | [[Inner-Product Spaces]] |
| **Homomorphism** | **add** | [[Group Homomorphism]], [[knowledge/math/algebra/structures/rings/Ring]], [[Linear Maps]], [[Subgroup]] |
| **Injectivity** | **move in** | [[Function]], [[Group Homomorphism]], [[Morphism]] |
| **Surjectivity** | **move in** | same |
| **Monotonicity** | **add** | [[Calculus Functions]]; order theory; functors |
| **Involution** | **add** | [[Field]], [[Matrix]], [[Group]], `Set Operation` |
| ~~Continuity~~ | defer (Tier 2) | analysis — when `analysis/` exists |
| ~~Isometry, Lipschitz~~ | after `metric/` | [[Calculus Functions]] has a Lipschitz-1 section already |

## `properties/metric/` — the merged family *(revised, see §3.11)*

Scope: a function $d: X \times X \to \mathbb R$, or $N: V \to \mathbb R$ for the norm forms.

| axiom | status | consumers |
| --- | --- | --- |
| [[Triangle Inequality]] | exists in `norm/` — **move, add `### Metric Form`** | [[Metric Space]], [[Lattices]], [[Code Distance]] |
| [[Homogeneity]] | exists in `norm/` — **move** | [[Metric Space]], [[Inner-Product Spaces]] |
| [[Positive Definiteness]] | exists in `norm/` — **move, and delete its derivable first bullet** | same; doubles as metric identity-of-indiscernibles |
| **Distance Symmetry** | **add** | [[Code Distance]], [[Statistical Distance]] |
| ~~Non-negativity~~ | **withdrawn** — derivable from the other three; a `[!proposition]` in [[Metric Space]], not an axiom | — |
| ~~Ultrametric, inner-product axioms~~ | defer | [[Inner-Product Spaces]] composes from `map/` + `metric/` already |

**Totals as of 2026-08-29:** 27 axiom notes exist; **2 to add** (`Homomorphism`, `Distance Symmetry`), **3 to move** (`norm/` → `metric/`), **1 to fix** ([[Positive Definiteness]]); 13 explicitly deferred with reasons. After this, every structure note in `math/` composes from the library with no inline restatement.

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

| # | task |
| --- | --- |
| 0a | **10.1** — `algebra/structures/set theory/` → `math/set theory/`. It holds the objects every Scope line points at; they are not algebra |
| 0b | **10.2** — [[Matrix]], [[Vector Algebra]], [[Kronecker Product]] → `linear algebra/`; [[Metric Space]] → `calculus/` (it is analysis, and Batch D rewrites it anyway) |
| 0c | Create empty `math/properties/metric/` |

## Batch A · Restore the floor · ~30 min · **blocks everything**

| # | task |
| --- | --- |
| A1 | Recover **Cartesian Product**, **Set Equality**, **Empty Set** from `git show f9c2c34:"…/Set Theory.md"` |
| A2 | Create `Set Operation` (**6.3b**) — the laws table out of [[Set]], plus Cartesian Product, power set, complement, partition (draft 3.2) |
| A3 | [[Set]] keeps: definition, equality, empty set, famous sets, notation, universal set. Move Universal Set out of `## Representation` |
| A4 | [[Set Foundation]]: strip the two leading blank lines, add `## Definition` (still empty — see F6) |

**Checkpoint:** no Scope line in the vault refers to an undefined product.

## Batch B · Join the spine · ~1.5–2 h

| # | task |
| --- | --- |
| B1 | Rewrite [[Relation]] — heterogeneous first, homogeneous as specialisation, converse, composition, left-total/functional, the specialisation table (draft 3.3) |
| B2 | Restructure [[Function]] — six edits incl. the partial-function variant and deleting the duplicate `## Definition` (draft 3.4) |
| B3 | **G1** stray comma; **G2** delete the duplicated many-sorted section from [[Binary Operation]]; **G3** sorts-are-labels + smallness caveat + Birkhoff–Lipson reference in [[Many-Sorted Operation]] |
| B4 | Move odd/even functions → [[Calculus Functions]] |

**Checkpoint:** `Set → Relation → Function → Binary Operation` is one linked chain.

## Batch C · Fill the axiom gaps · ~2 h · 11 short notes

| # | task |
| --- | --- |
| C1 | `operation/` — **Cancellativity**, **Absorption** (drafts 3.5, 3.6) |
| C2 | `map/` — **Homomorphism** (draft 3.7) — the biggest single gap |
| C3 | `map/` — move **Injectivity**, **Surjectivity** out of [[Function]]; **Bijectivity** as the composed one-liner (draft 3.8) |
| C4 | `map/` — **Monotonicity**, **Involution** (drafts 3.9, 3.10) |
| C5 | `metric/` — move [[Triangle Inequality]], [[Homogeneity]], [[Positive Definiteness]] in from `norm/`; add **Distance Symmetry**; add `### Metric Form` and `### Norm Form` sections; delete the derivable bullet in [[Positive Definiteness]]; delete the empty `norm/` folder (revised draft 3.11) |

**Checkpoint:** every axiom a math note assumes exists as a note.

## Batch D · Rewire the consumers — **the payoff** · ~2–3 h

This is where the previous three batches turn into read value. Each row deletes a restatement.

| #   | task                                                                                                                                                                                                      |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| D1  | **1.12–1.15** — [[Magma]] / [[Semigroup]] / [[Monoid]]: one definition each, cite a [[Binary Operation]], drop the [[Closure]] links; [[Group]]'s second definition Semigroup → **Monoid**                |
| D2  | [[Group]]'s Cancellation proposition → link **Cancellativity**; [[Field]]'s two cancellation rows likewise, and recompose *integral domain* as "commutative ring whose nonzero elements are cancellative" |
| D3  | [[Group Homomorphism]], [[Ring]], [[Linear Maps]], [[Subgroup]] → link **Homomorphism**; [[Linearity]] gains "the module-signature case of `Homomorphism`"                                              |
| D4  | **5.4 / 5.4b** — rewrite [[Metric Space]]: separate *normed group* from *metric space*, compose both from the axiom notes                                                                                 |
| D5  | **5.5** — [[Code Distance]], [[Rank Metric Codes]] → metric axioms; [[Statistical Distance]] → the same, since total variation *is* a metric                                                              |
| D6  | **6.5** — `Set Operation`' laws table → [[Commutativity]] / [[Associativity]] / [[Distributivity]] / [[Idempotence]] / **Absorption** as instances                                                        |
| D7  | [[Calculus Functions]]' monotonic section → **Monotonicity**; [[Inner-Product Spaces]] → [[Map Symmetry]] + [[Linearity]] + [[Positive Definiteness]]                                                     |

## Batch E · Naming and hygiene · ~45 min

| #   | task                                                                                                                                                                                                                                                      |
| --- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| E1  | Rename [[Connexity]] → **Connexity**, with the synonyms remark. Three live senses of "total" after B1 make this near-mandatory                                                                                                                             |
| E2  | **2.10** — the clone-and-edit slips: [[Partial Order]] body says "preorder"; [[Total Order]] title says "Partial Order"; [[Abelian Group]] "Abelian Groups"; [[Field]] callout "Fields"; plural titles in [[Equivalence Relation]], [[Quotient Relation]] |
| E3  | **9.12** — the lint script: callout title vs filename, plus broken links. Run it as the Batch-E checkpoint                                                                                                                                                |
| E4  | **1.6 / 1.10** — [[Algebra Structure]]: restore the axiom index, strip the legacy frontmatter                                                                                                                                                             |

## Mine, after yours

- After **B**: [[Algebra MOC]] gains `Set Operation` and the reshaped `set theory/` tree; the spine diagram goes into a `Set Theory MOC` if you want one.
- After **C**: [[Math Properties MOC]] gains the `metric/` family, the new map axioms, and the "one structure-preserving map per family" row.
- After **D**: a review pass — I re-run orphan, broken-link and duplicate audits and report.

## If you only do one batch

**Batch A.** Thirty minutes, and it restores the definition every Scope line in the vault silently depends on.

**If you only do two:** A then D1 — the five-note Magma→Group chain is the vault's showcase, and it currently contains a wrong definition ([[Group]] via [[Semigroup]]) and four disagreeing closure treatments.
