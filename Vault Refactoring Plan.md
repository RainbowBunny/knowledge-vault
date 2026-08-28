# Vault Refactoring Plan

**Status legend** — `Open` · `Partial` · `Parked` (deliberately deferred) · `?` (needs a decision)

*Living document. Completed tasks are removed, not struck through — git holds the history, Appendix B keeps the IDs.*

*Last review: 2026-08-26, fifth pass.*

> **Housekeeping.** This file lives in the vault, so its wikilinks join your graph. Notes that **exist** are real links; notes that do not exist yet, and examples of broken links, are in `code`.

## Progress

| | 1st | 2nd | 3rd | now |
| --- | --- | --- | --- | --- |
| Notes in `knowledge/` | 501 | 505 | 505 | **518** |
| Orphans | 163 | 73 | 64 | **86** ¹ |
| Orphans in `math/` + `cryptography/` + `information theory/` | ~90 | 14 | 11 | **23** ¹ |
| Broken targets inside `knowledge/` | 16 | 13 | 13 | **6** ² |

¹ *Thirteen new notes landed this pass (quantum, physics, coding, assumptions) and none are linked from a hub yet. Of the 23, only ~8 predate this pass.*
² *Excluding `Fleeting MOC`, `Book Reference` and `PPT`, whose targets live outside `knowledge/` and resolve fine vault-wide. See task 11.3 for `PPT`.*

---

# Review — fifth pass (2026-08-26)

## The two new operation notes

[[Binary Operation]], [[Many-Sorted Operation]] and [[Binary Operation Examples]] created in `set theory/operation/`, alongside the new `function/` folder — the object layer now mirrors `relation/`. Three fixes:

| # | fix |
| --- | --- |
| G1 | `Binary Operation.md` starts with a stray comma: `,Reference:` |
| G2 | **The many-sorted section is now duplicated** — it survives as `### Many-Sorted Operation` inside [[Binary Operation]] *and* as the standalone [[Many-Sorted Operation]]. Delete the inline section; replace with one line: *"The general form is a [[Many-Sorted Operation]]; this note is the one-sort, arity-2 case."* Also reword the `## Variant` intro, which still says "many-sorted subsumes the other two" about a section that should no longer be there |
| G3 | [[Many-Sorted Operation]] predates the size discussion: add the remark that sorts are *labels* (the carrier of sort $(A,B)$ is $\mathsf{Hom}(A,B)$, objects only index), and that a [[Category]] is literally a many-sorted algebra **only when small** — for locally small categories it is an analogy. Swap the References to Birkhoff–Lipson 1970 (the founding paper) + the category article |

## Convention decided: signature-and-structure, in three tiers

The vault's architecture — objects in `set theory/`, axioms in `properties/`, structures composed by linking — is the **signature + structure** pattern of universal algebra and model theory. It is adopted vault-wide, with the honesty clause that it holds at three strengths:

| tier | Scope line is… | domains | composition behaves like |
| --- | --- | --- | --- |
| 1 | a first-order signature | algebra, orders, graphs, linear codes, automata / data types | equational or first-order logic — clean |
| 2 | a higher-order gadget (set of subsets, sup over subsets) | topology, analysis, probability, category size | the template still works; expect **Condition** clauses, not equations |
| 3 | a tuple of typed algorithms (`## Syntax`) | crypto schemes and proof systems | properties are games quantifying over adversaries; implications between them are theorems |

Practical rule: **`## Syntax` in a crypto note and `### Scope` in a math note are the same slot.** Tier 2 is why [[Field]] kept going wrong in review ("nonzero" is a condition, not an equation) and why the order table needed its own treatment — the friction was mathematical, not organisational.

### How multiple formal systems coexist (decided)

The systems do not conflict, because **the vault's medium is not a formal system**. Notes are written in informal-rigorous prose + the Scope/Condition/Property template, the way mathematics itself is written — formalizable in principle, committed to no foundation. Five rules:

1. **One medium.** The S/C/P template + composition-by-links is the representation. Never rewrite the vault "in" FOL or type theory.
2. **Formal systems are content.** FOL, equational logic, type theory live as *notes* in `math/logic/` (task 10.8), studied like [[Group]] — created only when a consumer exists.
3. **Tiers are metadata on properties, not foundations.** "Equational / first-order / second-order / game" is a one-line classification of each axiom; it predicts behavior (clean composition, Condition clauses, adversary quantifiers) without choosing a system.
4. **Translations are first-class notes.** When one concept has two representations, state it once in its home system and write the *bridge* as its own note. The vault already does this: [[R1CS to QAP Reduction]], [[Fiat-Shamir Transform]] (interactive → non-interactive), `Poset as Category` (4.6, order → category), the lattice poset ↔ algebra equivalence (2.14), Curry–Howard when `math/logic/` exists. Never duplicate the concept in both.
5. **Conflicts are boundary remarks.** Every real conflict met so far got a one-line remark at the exact boundary: class-vs-set (Category smallness), conditional-vs-equational ([[Field]]), symbolic-vs-computational (crypto uses games). Keep resolving locally; no global policy needed.

### North star (recorded)

*Extracted to [[North Star]] at the vault root — now the digital garden home page (`dg-home` moved there from [[Tag System]], which keeps `dg-publish`). It carries the vision, the skeleton, the when-lost workflow, and the known tensions.*

The vault is a **connected reference**: when something new is learned, backlinks + MOCs surface everything already known about its objects, and the new piece enters as leaf notes plus bridge notes. Precedents for exactly this design point exist and are healthy at scale: **nLab** (concept-centric wiki; *Idea → Definition → Properties → Examples → Related concepts → References* per entry) and the **Stacks Project** (self-contained natural-language reference, navigation by hyperlinks and tags rather than chapter order). The vault is nLab's shape + Stacks' self-containment + crypto's game style, minus machine checking.

What replaces Lean's compiler is a **precision skeleton** — prose is free everywhere *except* five load-bearing places, each with a session receipt of what happens otherwise:

1. **Scope lines type-check** — every symbol declared with its type, links target the declared kind *(the totally-typed category composition; the circular norm Scope)*
2. **Quantifiers bound, order explicit** *(the free $e$ in Identity Element)*
3. **Definition ≠ theorem** — never state a consequence inside a definition callout *(the $\exists!$ in Inverse Element)*
4. **Side conditions in the Condition slot** *(Field's "nonzero")*
5. **Dependencies are links** — a concept a definition uses but cannot link is a *detected gap*, not a footnote *(this is how `Module`, `Homomorphism`, and `partial function` were found)*

**Intuition convention:** an optional `## Intuition` section (nLab's *Idea*) at the top of a note, always separate from the definition callouts, so sharing-friendly prose never contaminates the precision skeleton. A custom `[!intuition]` callout can reuse the existing CSS-snippet mechanism.



# Open work

---

## Phase 1 — operation axioms

| # | task | Status |
| --- | --- | --- |
| 1.6 | [[Algebra Structure]]: restore the property table as an **axiom index** of links. `## Property` is currently empty and Frobenius sits under it (F6) | Open |
| 1.10 | Strip the legacy `parent: "[[Fleeting MOC]]"` / 🪴weedy frontmatter from [[Algebra Structure]] | Open |
| 1.11 | [[Distributivity]]: "$\oplus, \otimes$ **is** distributive" → "are" | Open |
| 1.12 | Resolve the two readings of [[Closure]] (F4): [[Binary Operation]] now carries the closure-is-in-the-type remark — remaining: reword [[Magma]] / [[Semigroup]] / [[Monoid]] to cite a [[Binary Operation]] and drop their [[Closure]] links | Partial |
| 1.13 | [[Semigroup]], [[Monoid]], [[Group]]: keep **one** definition each, the incremental one; fix "that the binary operation that satisfies" (F3) | Open |
| 1.14 | **[[Group]]: "a [[Semigroup]] with [[Inverse Element]]" → "a [[Monoid]] with…"** (F2) | Open |
| 1.15 | [[Magma]]: "a set $\{g_1, g_2 \dots\}$" → "a set $S$" | Open |

---

## Phase 2 — relation axioms

| # | task | Status |
| --- | --- | --- |
| 2.10 | **Fix the clone-and-edit slips** (F1): [[Partial Order]] body says "preorder"; [[Total Order]] callout says "Partial Order"; [[Abelian Group]] says "Abelian Groups"; [[Field]] callout says "Fields"; [[Equivalence Relation]] and [[Quotient Relation]] have plural titles | Open |
| 2.11 | [[Total Order]]: mark reflexivity as implied by [[Totality]], or drop it (F5) | Open |
| 2.12 | [[Quotient Relation]]: `S / _\sim` → `S/{\sim}` | Open |
| 2.13 | Consider `properties/compatibility/` — `Translation Invariance`, `Order Compatibility`. Needed the moment you write `Ordered Field`, which [[Positive Definiteness]] and [[Triangle Inequality]] already presuppose | ? |
| 2.14 | Consider `Lattice (Order Theory).md` — the one natural consumer [[Idempotence]] has, and the place the operation and relation families provably coincide | ? |

---

## Phase 3 — the `groups/` subtree

[[Groups MOC]] makes the subtree findable. These make it readable.

| # | task | Status |
| --- | --- | --- |
| 3.2 | Give [[Group]] a `## Structure` section: [[Subgroups]], [[Normal Subgroups]], [[Cosets]], [[Quotient Group]] | Open |
| 3.3 | Give it `## Special Groups`: [[Abelian Group]], [[Cyclic Group]], [[Symmetric Group]], [[Free Groups]], [[Bilinear Group]] | Open |
| 3.4 | Move the $\mathrm{GL}_n$ material out of [[Group]]'s `## Example` into [[Example of Subgroups]] or a new `General Linear Group.md` | Open |
| 3.6 | Have [[Subgroups]] state its criterion via [[Closure]] and [[Inverse Element]] — **the one place [[Closure]]'s subset reading is exactly right** | Open |
| 3.7 | Fill [[Subgroups]]'s empty `### Image` and `## Property` headings, or delete them | Open |
| 3.8 | Fill the stubs [[Free Groups]] and [[Cosets]] | Open |

---

## Phase 4 — category folder

| # | task | Status |
| --- | --- | --- |
| 4.1 | [[Opposite Category]] exists but does not state the duality principle — the reason it has its own note | Partial |
| 4.4 | Add mono + epi $\not\Rightarrow$ iso, with $\mathbb Z \to \mathbb Q$ in $\mathsf{Ring}$; cross-link [[Function between Sets]], which proves that in $\mathsf{Set}$ it *does* | Open |
| 4.6 | `example/Poset as Category.md` — **unblocked**, [[Preorder]] has content now. A preorder is a thin category: one morphism $a \to b$ iff $a \leq b$ | Open |
| 4.8 | Link [[Category]] → [[Category Set]], [[Category Group]] | Open |
| 4.9 | Fill or delete [[Category]]'s empty `## Property` heading | Open |
| 4.11 | **Add the partial-composition remark to [[Category]]** — composition types as $\mathsf{Hom}(A,B) \times \mathsf{Hom}(B,C) \to \mathsf{Hom}(A,C)$, not $M \times M \to M$, and there is one identity per object. As written, the links to [[Associativity]] and [[Identity Element]] claim more than those notes support. This is also what [[Groupoids]] is about, and why a monoid is a one-object category | Open |
| 4.12 | [[Morphism]]: headings and callout titles still plural ("Isomorphisms", "Epimorphisms") under a singular note name | Open |
| 4.13 | [[Groupoids]] → `Groupoid.md`, for the singular convention | Open |
| 4.14 | [[Universal Properties]]: the Products example says "Let $A, B$ be **sets**" then uses $\mathsf{Hom}_{\mathcal C}$ — state it for a general category | Open |

> **Commutative diagrams — `\begin{CD}` confirmed working, no plugin.** Drop these into [[Universal Properties]]:
>
> Product:
> ```
> $$\begin{CD}
> @. Z @.\\
> @. @VV{\sigma}V @.\\
> A @<{\pi_A}<< A\times B @>{\pi_B}>> B
> \end{CD}$$
> ```
> Coproduct — the same square with every arrow reversed, which is the duality principle from 4.1 made visible:
> ```
> $$\begin{CD}
> A @>{i_A}>> A\amalg B @<{i_B}<< B\\
> @. @VV{\sigma}V @.\\
> @. Z @.
> \end{CD}$$
> ```
> `\begin{CD}` only draws horizontal and vertical arrows on a grid, so the diagonal $f_A, f_B$ have to be labelled in prose. If that becomes limiting, `obsidian-tikzjax` gives real `tikz-cd`.

---

## Phase 5 — map and norm axioms

| # | task | Status |
| --- | --- | --- |
| 5.4 | Rewire [[Metric Space]], [[Inner-Product Spaces]], `structures/lattices/*` to the norm notes — **now unblocked**, the Scope is fixed | Open |
| 5.4b | [[Metric Space]] conflates two things: "an additive group equipped with a norm" is a **normed group**. Every normed group induces a metric space, not conversely — and [[Code Distance]] will link here, where Hamming distance is a metric with no vector-space norm underneath | Open |
| 5.5 | Rewire [[Code Distance]] and [[Rank Metric Codes]] | Open |
| 5.7b | Add `### Condition` to [[Homogeneity]] ($V$ has scalar multiplication) and [[Triangle Inequality]] ($V$ has addition) (F7) | Open |
| 5.8 | Add `Homomorphism` to `properties/map/`. [[Ring]] and [[Group Homomorphisms]] each define their own inline | Open |

---

## Phase 6 — set theory

| # | task | Status |
| --- | --- | --- |
| 6.3b | Split `Set Operations.md` out of [[Set]] — 7 KB, most of it one ~20-row table. Tell me when it exists and I will add it to [[Algebra MOC]] | Open |
| 6.4 | Merge the duplicated Composition / Inverse material; keep [[Function between Sets]]'s version | Open |
| 6.5 | Link the operation-laws table to [[Commutativity]] / [[Associativity]] / [[Distributivity]] as *instances*. Lands better after 6.3b | Open |

---

## Phase 7 — the `Function.md` split

| # | task | Status |
| --- | --- | --- |
| 7.2b | [[Prime]] still has a dead `[[Function#…]]` link, orphaned when `Function.md` was deleted | Open |
| 7.3 | [[Inequality]] — convex / concave, derivative test, **and the analytic Jensen**; [[Probability Inequalities]] keeps the expectation form and links back | Open |
| 7.7b | [[Function between Sets]] absorbed the remainder; you flagged it for a pass of its own | Open |
| 7b | Split [[Field]] (14.5 KB): extract `structures/fields/Complex Numbers.md`, move complex-valued calculus to `calculus/`, consider `Field Arithmetic.md` for the consequences table. The complex logarithm is parked in [[Calculus Functions]] and moves here | Open |

---

## Phase 8 — the crypto side

| # | task | Status |
| --- | --- | --- |
| 8.4 | Promote **SNARK** to its own note; hang [[Groth16]] and [[LUNA]] off it. Capitals mark the acronym letters: `Succinct Non-interactive ARgument of Knowledge` | Open |
| 8.5 | Leakage parameterisation in [[Zero Knowledge]] — LPCP has `hvzk-D` locally, the shared note does not | Open |
| 8.6 | `reusable` variant in [[Knowledge Soundness]] | Open |
| 8.7 | Gloss "input-independent" in [[Linear Probabilistically Checkable Proofs]] | Open |
| 8.8 | Fill the lattice-construction table in [[Verifiable Computing MOC]] | Open |
| 8.9 | `Elementary Wrapper` still links a dead `Zero-knowledge MOC` → [[Verifiable Computing MOC]] | Open |
| 0.6c | Acronym-legend line in [[Non-interactive ARGument]] and [[Non-interactive ARgument of Knowledge]] | Open |

---

## Phase 9 — hubs, hygiene, decisions

| # | task | Status |
| --- | --- | --- |
| 9.5 | Frontmatter — **decided: drop it.** Remove `parent:` from `templates/default.md`, strip it from the 43 notes carrying it, delete `Fleeting MOC.md` | Open |
| 9.6 | Sub-MOC top-ups. Pre-existing orphans: [[Assumptions MOC]] — [[Closest Vector Problem]], [[Shortest Basis Problem]], [[Normal Form Short Integer Solution]], [[Short Secret Learning With Error]], [[Ideal Rank Syndrome Decoding]]; [[Linear Algebra MOC]] — [[Dual Bases]]; [[Calculus MOC]] — [[Fourier Analysis]]; [[Probability MOC]] — [[Bernoulli Distribution]]; [[Threshold MOC]] — [[Combinatorial Approach for Secret Sharing]], [[Simple n-out-of-n Scheme]] | Open |
| 9.6b | **New notes not yet linked from any hub**: [[Assumption Taxonomy]], [[Privacy Amplification]], [[Alekhnovich Encryption Scheme]], [[Identical Partly Secret Sharing]], [[Reed-Solomon]], [[Ambiguous Coding]], [[Digital Signature]], [[Additive-Homomorphic Encryption]], [[Lyubashevsky-Peikert-Regev Public Key Encryption]], plus `complexity/quantum/` and the new `physics/` folder. Say the word and I will fold them into the MOCs | Open |
| 9.7 | Merge or delete `Pseudorandom Functionsss.md`. [[Universal Hash Functions]] is empty; [[Special Functions]] has empty `### Prefix-Free` / `### Unpredictability` | Open |
| 9.8b | **The singular rename is half done in `groups/`.** Renamed: [[Group]], [[Abelian Group]], [[Cyclic Group]], [[Symmetric Group]], [[Quotient Group]], [[Bilinear Group]]. Still plural: [[Free Groups]], [[Cosets]], [[Subgroups]], [[Normal Subgroups]], [[Group Homomorphisms]], and the folders `special groups/`, `subgroups/`. Some are legitimately plural (a note *about* cosets), so decide the rule: **singular when the note defines one object, plural when it surveys a family** | ? |
| 9.12 | **Lint script** in `scripts/` (they already run Dataview JS): compare each `[!definition]` callout title against its filename, and list broken wikilinks. The clone-and-edit bug recurred three times under review — this automates the catch | Open |
| 9.13 | Decide the garden's **dependency-closure publishing** rule: [[North Star]]'s MOC links and any published composed definition need their targets published too, or they render broken to visitors. Candidates to `dg-publish`: the nine MOCs and `properties/` | ? |
| 9.11 | Adopt the `## Intuition` section convention (nLab *Idea*); optionally add an `[!intuition]` callout via a CSS snippet beside `pseudocode-callout.css`. Backfill only when touching a note anyway | Open |
| 9.10 | `physics/` has no MOC and no entry from [[Math MOC]]. Four notes so far; decide whether it is a domain or belongs under a quantum-computing heading | ? |
| 0.10 | Remaining accidental links: `a` ×3, `b`, `c` in [[Secure Multi-party Computation]]; `osint` in one CTF note | Parked |

---

## Phase 10 — reclassification (folder audit)

Ordered by leverage. The seam rules being applied: *the mathematical object lives in its home discipline; the hardness assumption lives in `cryptography/assumptions/`; a scheme lives under the primitive it instantiates.*

| # | task | Status |
| --- | --- | --- |
| 10.1 | **Promote `algebra/structures/set theory/` → `math/set theory/`.** The objects every Scope line points at — [[Set]], [[Relation]], [[Function between Sets]], [[Binary Operation]] — are the raw material of *every* domain, not of algebra; and [[Preorder]] / [[Partial Order]] are order theory, not algebra. Same argument that promoted `properties/`, same fix. Do it in Obsidian; I update the MOC prose after | Open |
| 10.2 | `math/algebra/` root strays: [[Matrix]], [[Vector Algebra]], [[Kronecker Product]] → `linear algebra/`; [[Metric Space]] is analysis, not algebra — park it in `calculus/` until an `analysis/` folder exists | Open |
| 10.3 | **The AHE near-duplicate pair**: `information theory/…/rank-metric/schemes/Additively-Homomorphic Encryption` (1.7 KB, eprint 2023/1798) vs `cryptography/…/symmetric encryption/schemes/Additive-Homomorphic Encryption` (0.8 KB). Same name modulo one letter, different folders — the Groupoids hazard again. An encryption scheme is cryptography; codes stay in information theory, schemes built *from* them do not. Merge or rename so the two are distinguishable | Open |
| 10.4 | `post-quantum cryptography/lattice-based/Lattice.md` (815 B): its `## Basic Definition` is **empty** and the content is one trapdoor lemma. Rename `Lattice Trapdoors.md`, link [[Lattices]] for the object | Open |
| 10.5 | **Lattice problems are stated in three places**: math [[Lattice Problem]] (apprSVP, SIVP), crypto `SVP/` ([[Shortest Vector Problem]], [[Closest Vector Problem]], [[Shortest Basis Problem]]), and the DLP precedent puts problems in `cs/problems/`. Pick the seam once: problem statement in math/cs, *assumption* (hardness, parameters) in crypto — then make the crypto SVP notes link math for the statement | ? |
| 10.6 | [[Unnormalized Gaussian Function]] sits in `set theory/function/` — it is lattice-smoothing material, not a structural function. Move beside [[Discrete Gaussian Distribution]] or into `lattices/` | Open |
| 10.7 | `Reviewing Paper.md` sits at the `knowledge/` root → `academic/` | Open |
| 10.8 | `math/theory/` is empty — **decided: becomes `math/logic/`** when a first consumer exists (candidates: `Formal System`, `First-Order Logic`, `Equational Logic` — the last already has two consumers: the operation axioms and the varieties remark). Formal systems enter as *content*, per the coexistence rules above | Open |
| 10.9 | `physics/` (4 quantum-optics notes: [[Calcite Crystal]], [[Pockels Cell]], [[Photo-Multiplier]], [[Polarizing Filter]]) is a fine new domain but unanchored — no MOC, no inbound links. Presumably QKD context: link from `complexity/quantum/` or a future QKD note; I can write `Physics MOC` on request | Open |
| 10.10 | `language/` root mixes languages with tools ([[Git]], [[Docker]], [[Latex]]) and hardware ([[Verilog]], [[NPU]], [[Hexagon]]) | Parked |

**Verified sound, no move needed:** `set theory/operation|relation|function/` (new object layer — right shape); `structures/` one-folder-per-family; `properties/` four families; `verifiable computing/` post-8.3; `complexity/` vs `cs/` split; `category/` under algebra is conventional, not wrong.

## Phase 11 — security foundations unification

The Adversary / Indistinguishability / Statistical Distance triangle, unified game-first. Drafts delivered as *Security Foundations Drafts.md* (chat card, 2026-08-28); provenance: Bellare–Rogaway 2004/331, Shoup 2004/332, Boneh–Shoup (already the house notation).

**The finding that forced this phase:** `Security Model.md` contains only a BRKE (ratcheted key exchange) definition — no security-model content at all — while the trichotomy (perfect / statistical / computational) is stated twice, in [[Adversary]] and [[Indistinguishability]], with neither authoritative.

| # | task | Status |
| --- | --- | --- |
| 11.1 | Create `foundations/Security Game.md` — challenger/adversary experiment; **search** vs **distinguishing** shapes; **the strength table** (perfect / statistical / computational = adversary class × bound). The crypto analogue of [[Binary Operation]]: the object all of `proof/properties/` instantiates | Open |
| 11.2 | Create `foundations/Negligible Function.md` — used everywhere, defined nowhere; closure properties are what make game hops compose | Open |
| 11.3 | Move `daily/Temp/PPT.md` → `foundations/PPT.md` **in Obsidian** (7 links follow) and fill it — supersedes 9.9 | Open |
| 11.4 | Append the **Optimal Distinguisher (game form)** corollary to [[Statistical Distance]] — $\Delta = \max_{\mathcal A} \mathsf{Adv}^{1\text{-}\mathsf{Dist}}$ over unbounded adversaries; one line from the existing Event Characterization | Open |
| 11.5 | [[Indistinguishability]]: retag the game `[!algorithm]` → `[!definition]`; restate perfect and statistical variants game-first (statistical = negligible advantage for *all* adversaries, $= \Delta$ negligible by 11.4) | Open |
| 11.6 | [[Adversary]]: fix "the different between"; delete its perfect/statistical/computational subsections (they move to 11.1's table); content becomes the adversary *classes* — unbounded, [[daily/Temp/PPT]], oracle access | Open |
| 11.7 | [[Security Model]]: move the BRKE block to `key establishment/key exchange/Bidirectional Ratcheted Key Exchange.md`; rewrite as the umbrella — notion = syntax + game + class + bound | Open |
| 11.8 | Payoff pass: [[Argument Systems]] = "[[Interactive Proof Systems]] with computational [[Soundness]]"; [[Perfect Security]] links the perfect row; ties into 8.5 (ZK variants name their rows) | Open |
| 11.9 | After 11.1–11.7 land: I rewrite [[Cryptography Foundations MOC]] around the game/notion spine | Open — mine |

---

## Order from here

**G1–G3 while the notes are fresh, then 1.12–1.15 and 2.10–2.12**. **Phase 11 is the current front** — it is self-contained, crypto-side, and 11.1's table is the same visible-payoff move as the closure table — about twenty minutes total, and F2 and F4 are wrong claims sitting in the base of the structure hierarchy.

**Then 4.11**, the partial-composition remark. It is one paragraph and it closes the only place where the axiom library's typing is quietly violated.

**Then 3.2, 3.3, 3.6** — the outbound links from [[Group]] into the subtree and the axiom library. Still the payoff Phase 1 was built for, and still the part a MOC cannot do.

**Then 5.4** — unblocked now.

**9.6b whenever you want it** — thirteen new notes are sitting unlinked; the MOCs are mine to update, so this is a one-line ask.

---

## Appendix A — broken links

Inside `knowledge/`: `Complexity Theory` ×4 (probably wants [[Complexity MOC]]) · `Non-Interactive Zero Knowledge` ×3 · `Extendable Output Function` ×2 · `Knowledge Extractor` ×2 (worth writing) · `Interactive Zero Knowledge` · `Proof System` · `Non-Abelian Group` · `Complex Hilbert Space` · `Zyalov Bound` (→ **Zyablov**) · `Function#…` in [[Prime]] · `Zero-knowledge MOC` in `Elementary Wrapper` · the `a`/`b`/`c` accidents.

Resolving outside `knowledge/` but worth knowing: `PPT` ×7 → `daily/Temp/` (task 11.3) · `Book Reference` ×5 → `academic/` · `Fleeting MOC` ×43 → vault root (task 9.5 deletes these).

## Appendix B — completed

**Phase 0** — 0.1–0.5 · 0.6a · 0.7–0.9 · 0.11 · 0.12 · 0.13. *(0.6b withdrawn: the `ARGument` casing marks the acronym.)*
**Phase 1** — 1.1–1.5 · 1.7 · 1.9.
**Phase 2** — 2.1–2.9.
**Phase 3** — 3.1 · 3.5.
**Phase 4** — 4.2 · 4.3 · 4.5 · 4.7 · 4.10 *(`\begin{CD}` works — plain MathJax, no plugin)*.
**Phase 5** — 5.1 · 5.2 · 5.3 · 5.6 · 5.7 *(E1 circular Scope fixed)*.
**Phase 6** — 6.1 · 6.2 · 6.3.
**Phase 7** — 7.1 · 7.2 · 7.4 · 7.5 · 7.6 · 7.7.
**Phase 8** — 8.1 · 8.2 · 8.3.
**Phase 9** — 9.1–9.4 · 9.8 *(singular rename done, all backlinks followed)*.

**Findings closed:** C1–C5 · D1–D13 · E1 · E3–E9 · N5 · N6 · N9 · N11 · N13.

---

## What is worth protecting

- **The relation table in [[Non-Interactive Proof Systems]]** — composition as a matrix. Mirrored now by the closure table in [[Algebra MOC]] and the order table in [[Math Properties MOC]].
- **[[Equivalence Relation]]**, **[[Commutative Ring]]**, **[[Preorder]]** — definitions that are nothing but links.
- **[[Group Homomorphisms]]** — links [[Morphism]] instead of restating it.
- **The Scope / Condition / Property template.** Sixteen notes now use it, and the four drifts have all been in the callout title, never the content.
- **[[Split-R1CS]]** citing [[Bilinearity]] — the cross-domain link this refactor exists to make routine.
