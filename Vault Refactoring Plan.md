# Vault Refactoring Plan

*Open work only — completed tasks are removed, git holds the history, Appendix B keeps the IDs.*
*Conventions live in [[North Star]]. The foundation build spec lives in [[Foundation Layer]].*
*Verified against the vault 2026-08-28.*

---

# Pipeline

## The loop

1. **You work** in Obsidian and commit as usual (obsidian-git auto-backup is fine — no special commit messages needed).
2. **You send one trigger** from the table below. That is the whole handoff.
3. **I verify against the vault itself** — `git diff` since my last pass, `scripts/vault-lint.py`, and a read of the notes the batch names. Never against status marks.
4. **I report and update this plan**, then commit it.

> [!important] You do not maintain status
> This was the main friction in the first five passes: you would finish work, the plan would go stale, and I would re-derive the truth by scanning anyway. So the division is now explicit — **you do the work, I own the bookkeeping.** Mark things if you like; I will not rely on it.

## Triggers

| you say | I do |
| --- | --- |
| `check A` — any batch letter or task id | Verify that checkpoint. Report **pass / blocking / content errors / minor**, update the plan |
| `review` | Diff everything changed since my last pass and review it, whether or not it was on the plan |
| `lint` + paste the output | Triage the report into real problems vs known noise |
| `next` | The next three things and why, given what is actually done |
| `stuck: <note>` | Read it, diagnose, hand back a paste-ready fix |
| `draft <note>` | Write a full draft in house style with a `Reference:` line |
| `done <ids>` | Fast path — mark without a full review |
| `audit` | Full scan: lint plus a read pass over a named area |

Anything conversational still works. The triggers exist so you never have to explain context.

## Ownership

| | owner |
| --- | --- |
| Everything in `knowledge/` | **you** — content is yours |
| MOCs | **me** — say the word and I write or update them |
| [[North Star]], [[Foundation Layer]], this plan | **me** |
| `scripts/vault-lint.py` | **me** |

## Before you commit

```
python scripts/vault-lint.py
```

Six checks: broken links, duplicate names, callout-title mismatch, empty notes, hollow headings, orphans. If **broken** or **dupe** went up, fix before committing — those are always real. The other four are smells, not errors; current baselines are in Appendix A.

`--full` lists everything, `--only broken` runs one check, `--all` widens past `knowledge/`.

## Two things worth telling me

- **If you renamed something.** Obsidian repairs vault links automatically; it cannot repair references in my drafts or in this plan. One line — "renamed X to Y" — and I fix them.
- **If you have not committed.** I read the working tree, so I see uncommitted work fine; but `git diff` is how I scope a review, so uncommitted work may fall outside the window I check.

---

# Now — clear Checkpoint A, finish Batch B

Two floor items plus the last of Batch B — unchanged for three passes. Paste-ready text in the checkpoint report and [[Foundation Layer]]; ~15 minutes.

| # | task |
| --- | --- |
| **A5** | **Link the Cartesian product.** [[Set Operation]] has zero inbound links — the definition is restored but unreachable, so rule 5 is still violated. Add links from [[Set]], [[Relation]], [[Binary Operation]], [[Function]] |
| **A6** | **Define union, intersection, difference, disjoint union.** They exist only as rows in a symbol table, yet the whole law table is written in them. Same bug as the missing product, one layer up |
| **B3** | Last of Batch B: **G1** stray `,Reference:` at the top of [[Binary Operation]] · **G3** [[Many-Sorted Operation]] still lacks the sorts-are-labels remark, the small / locally-small caveat, and the Birkhoff–Lipson reference |

Riding along whenever you next touch these notes: Famous Sets belongs in [[Set]] not [[Set Operation]]; Disjoint should move the other way (it uses $\cap$); the law table sits under `## Notation` but is a `## Property`; "are **equals**" → "are equal"; $P(S)$ → $\mathcal P(S)$; [[Set Foundation]]'s `## Basic Definition` is an empty heading.

---

# Queue

## Foundation — Batches C, D, E

Specification and drafts in [[Foundation Layer]]; its Status block tracks the batches.

| #     | task                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | est    |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **C** | **[[Homomorphism]] and [[Distance Symmetry]] created; `norm/` → `metric/` complete.** Remaining, all from the review of 2026-09-02: **R1** [[Positive Definiteness]] does not type-check — `d(x,x) ⟺ x = 0` is not a proposition and presumes a zero the Scope has not got · **R2** the norm forms of [[Positive Definiteness]] and [[Triangle Inequality]] vanished in the merge, so *"a norm is…"* is no longer composable — add `### Norm Form` to each · **R3–R6** [[Distance Symmetry]] "is symmetry" → "is symmetric"; [[Monotonicity]] still 0 bytes; [[Connexity]]'s body still says "total"; small wording in [[Homomorphism]] | 30 min |
| **D** | **The payoff — rewire consumers.** Absorbs 1.12–1.15, 5.4, 5.4b, 5.5, 6.5: the Magma→Group chain drops its [[Closure]] links and [[Group]]'s Semigroup bug; [[Group]]/[[Field]] cancellation → `Cancellativity`; [[Group Homomorphisms]]/[[knowledge/math/algebra/structures/rings/Ring]]/[[Linear Maps]]/[[Subgroups]] → `Homomorphism`; [[Metric Space]] split normed-group vs metric; [[Code Distance]], [[Rank Metric Codes]], [[Statistical Distance]] → metric axioms; [[Set Operation]] laws → the five axioms; [[Calculus Functions]] → `Monotonicity`; [[Inner-Product Spaces]] → [[Map Symmetry]] + [[Linearity]] + [[Positive Definiteness]] | 2–3 h  |
| **E** | [[Connexity]] → `Connexity` (three live senses of "total" after B1) · the clone-and-edit slips (2.10) · [[Algebra Structure]] axiom index + frontmatter (1.6, 1.10)                                                                                                                                                                                                                                                                                                                                                                                                                                             | 45 min |

## Algebra structures

| # | task |
| --- | --- |
| 3.2 | Give [[Group]] a `## Structure` section: [[Subgroups]], [[Normal Subgroups]], [[Cosets]], [[Quotient Group]] |
| 3.3 | Give it `## Special Groups`: [[Abelian Group]], [[Cyclic Group]], [[Symmetric Group]], [[Free Groups]], [[Bilinear Group]] |
| 3.4 | Move the $\mathrm{GL}_n$ material out of [[Group]]'s `## Example` into [[Example of Subgroups]] or a new `General Linear Group` |
| 3.6 | [[Subgroups]] states its criterion via [[Closure]] and [[Inverse Element]] — the one place [[Closure]]'s subset reading is exactly right |
| 3.7 | [[Subgroups]]' `## Property` heading is still empty (`### Image` now has content) |
| 3.8 | Stubs: [[Free Groups]] (0 bytes), [[Cosets]] (21 bytes) |
| 9.8b | The singular rename is half done in `groups/`. Renamed: [[Group]], [[Abelian Group]], [[Cyclic Group]], [[Symmetric Group]], [[Quotient Group]], [[Bilinear Group]]. Still plural: [[Free Groups]], [[Cosets]], [[Subgroups]], [[Normal Subgroups]], [[Group Homomorphisms]], and the folders. Rule to settle: **singular when the note defines one object, plural when it surveys a family** |
| 7b | Split [[Field]] (14.5 KB): extract `Complex Numbers`, complex-valued calculus → `calculus/`, consider `Field Arithmetic` for the consequences table |

## Category

| # | task |
| --- | --- |
| 4.11 | **Add the partial-composition remark to [[Category]]** — composition types as $\mathsf{Hom}(A,B) \times \mathsf{Hom}(B,C) \to \mathsf{Hom}(A,C)$, one identity per object. As written, its links to [[Associativity]] and [[Identity Element]] claim more than those notes support. Fills the empty `## Property` (4.9) and carries the one-object / many-objects ladder |
| 4.1 | [[Opposite Category]] exists but does not state the duality principle |
| 4.4 | mono + epi $\not\Rightarrow$ iso, with $\mathbb Z \to \mathbb Q$ in $\mathsf{Ring}$; cross-link [[Function]], where in $\mathsf{Set}$ it *does*. Same theme, second instance: [[Group Homomorphisms]] states "isomorphism iff bijection" as though definitional — it is a **theorem about groups**, false in $\mathsf{Top}$ and $\mathsf{Poset}$ |
| 4.6 | `Poset as Category` — unblocked, [[Preorder]] has content. `### Small Category` in [[Category]] is misnamed; it is this |
| 4.8 | Link [[Category]] → [[Category Set]], [[Category Group]] |
| 4.15 | The **Homomorphism ↔ Morphism bridge**: one remark per side. Morphisms are not functions (preorder-as-category has pairs as arrows); the two families coincide only in a *concrete* category — which is what licenses [[Group Homomorphisms]] to import [[Morphism#Isomorphisms|iso]] |
| 4.12 | [[Morphism]]: plural headings and callout titles under a singular note name |
| 4.13 | [[Groupoids]] → `Groupoid`, and add the algebraic reading (a group with a partial operation) |
| 4.14 | [[Universal Properties]]: the Products example says "let $A, B$ be **sets**" then uses $\mathsf{Hom}_{\mathcal C}$ |

Commutative diagrams: `\begin{CD}` confirmed working, no plugin. Snippets for products and coproducts are in the conversation of 2026-08-24.

## Cryptography

| # | task |
| --- | --- |
| 11.7 | [[Security Model]] still contains **only** a BRKE definition. Move it to `key establishment/key exchange/Bidirectional Ratcheted Key Exchange`; rewrite as the umbrella — a notion is syntax + [[Security Game]] + [[Adversary]] class + bound |
| 11.5 | [[Indistinguishability]] game-first: retag the game `[!algorithm]` → `[!definition]`; state perfect and statistical as rows of the [[Security Game]] table |
| 11.8 | Payoff: [[Argument Systems]] = "[[Interactive Proof Systems]] with computational [[Soundness]]"; [[Perfect Security]] links the perfect row |
| 8.4 | Promote **SNARK** to its own note; hang [[Groth16]] and [[LUNA]] off it. Capitals mark the acronym: `Succinct Non-interactive ARgument of Knowledge` |
| 8.5 | Leakage parameterisation in [[Zero Knowledge]] — LPCP has `hvzk-D` locally, the shared note does not |
| 8.6 | `reusable` variant in [[Knowledge Soundness]] |
| 8.7 | Gloss "input-independent" in [[Linear Probabilistically Checkable Proofs]] |
| 8.8 | Fill the lattice-construction table in [[Verifiable Computing MOC]] |
| 8.9 | `Elementary Wrapper` links a dead `Zero-knowledge MOC` → [[Verifiable Computing MOC]] |
| 0.6c | Acronym-legend line in [[Non-interactive ARGument]] and [[Non-interactive ARgument of Knowledge]] |
| 11.10 | **The perfect-secrecy two-view pair.** [[Perfect Security]] (adversarial: ciphertext distributions coincide) and [[Information Theory]] (information-theoretic: posterior = prior) define the same Shannon theorem in two idioms and neither links the other. [[Perfect Security]]'s *Independence Form* is already the bridge, unlabelled. Shannon's bound is stated three times. One remark per side — drafts in *two-views.md*, 2026-08-28 |
| 11.11 | Two-view candidates to check: semantic security ↔ IND-CPA in [[Symmetric Key Encryption]] (implications are stated — is the equivalence?); knowledge soundness ↔ extractability; PCP / LPCP / NILP as three oracle idioms (a table in [[Verifiable Computing MOC]], not cross-links); min-entropy ↔ guessing advantage |
| 11.9 | *(mine)* Rewrite [[Cryptography Foundations MOC]] around the game/notion spine, once 11.5–11.8 land |

## Math content

| # | task |
| --- | --- |
| 7.2b | [[Prime]] links `[[Function#Logarithmic Integral|Logarithmic Integral]]` — but $\mathrm{Li}(X)$ now lives **in [[Prime]] itself**, at its own `### Logarithmic Integral` heading. The note name resolves again after the rename, so the linter is silent, but the anchor points at a heading that no longer exists. Change it to a local reference. *(Broken **headings** are invisible to the linter — only broken notes are caught.)* |
| 7.3 | [[Inequality]] — convex / concave, derivative test, **and the analytic Jensen**; [[Probability Inequalities]] keeps the expectation form and links back |
| 6.4 | [[Function]] still has both a `### Composition` and a `### Inverse` — check whether these are the two survivors or a leftover duplicate pair from the `Function.md` absorption |

## Hubs, hygiene, moves

| # | task |
| --- | --- |
| 9.6 | Sub-MOC top-ups for pre-existing orphans: [[Assumptions MOC]] (5), [[Linear Algebra MOC]] ([[Dual Bases]]), [[Calculus MOC]] ([[Fourier Analysis]]), [[Probability MOC]] ([[Bernoulli Distribution]]), [[Threshold MOC]] (2) |
| 9.6b | *(mine, on request)* Fold the newer notes into MOCs: [[Assumption Taxonomy]], [[Privacy Amplification]], [[Alekhnovich Encryption Scheme]], [[Identical Partly Secret Sharing]], [[Reed-Solomon]], [[Ambiguous Coding]], [[Digital Signature]], [[Quantum State]], [[Quantum Circuits]], `physics/` |
| 9.5 | Frontmatter — **decided: drop.** Remove `parent:` from `templates/default.md`, strip from the notes carrying it, delete `Fleeting MOC` |
| 9.7 | `Pseudorandom Functionsss` duplicate; [[Universal Hash Functions]] empty; [[Special Functions]]' empty `### Prefix-Free` / `### Unpredictability` |
| 9.11 | Adopt the `## Intuition` convention (nLab *Idea*), backfilled lazily |
| 10.3 | The AHE near-duplicate pair — `Additively-Homomorphic Encryption` (information theory) vs `Additive-Homomorphic Encryption` (crypto). One letter apart, different folders |
| 10.4 | `post-quantum/lattice-based/Lattice.md` has an **empty** `## Basic Definition` and one trapdoor lemma → rename `Lattice Trapdoors`, link [[Lattices]] |
| 10.6 | [[Unnormalized Gaussian Function]] is lattice-smoothing material filed under `set theory/function/` |
| 10.7 | `Reviewing Paper` sits at the `knowledge/` root → `academic/` |
| 10.8 | `math/theory/` is an empty directory. The four logic notes landed at `math/` root rather than `math/logic/` — pick one and delete the empty folder |
| 10.9 | `physics/` — four quantum-optics notes, no MOC, no inbound links. Presumably QKD context |
| 0.10 | Accidental links: `a` ×3, `b`, `c` in [[Secure Multi-party Computation]] |
| 10.10 | `language/` mixes languages with tools and hardware — 50 of the 89 orphans live here | *parked* |

---

# Open decisions

| # | question | my recommendation |
| --- | --- | --- |
| 9.8b | Singular vs plural note names | Singular when the note defines one object; plural when it surveys a family. Settle before inbound links harden |
| 2.13 | A `properties/compatibility/` family — `Translation Invariance`, `Order Compatibility` | Needed the moment `Ordered Field` exists, which [[Positive Definiteness]] and [[Triangle Inequality]] already presuppose. Not before |
| 2.14 | `Lattice (Order Theory)` | Worth it — the one natural consumer [[Idempotence]] has, and where the operation and relation families provably coincide. Name it with the qualifier; [[Lattices]] is the geometric object |
| 10.5 | Lattice problems are stated in math ([[Lattice Problem]]) and crypto (`SVP/`), with [[Discrete Logarithm Problem]] setting a third precedent in `cs/problems/` | Problem statement in math or cs; *hardness assumption* in crypto. Then the crypto SVP notes link out for the statement |
| 9.13 | Garden publishing | Publish **dependency closures**, not lone notes — a composed definition renders broken to a visitor when its axiom links are unpublished. Candidates: the nine MOCs plus `properties/` |
| 9.10 | Is `physics/` a domain or a subfolder of quantum computing? | Decide before it grows past a handful of notes |

---

# Appendix A — audit snapshot

`python scripts/vault-lint.py`, 2026-09-02 · 548 notes in `knowledge/`.

```
broken=13  dupe=0  title=26  empty=38  hollow=115  orphan=95
```

**broken (13)** — all genuine, none new. `Complexity Theory` ×4 (probably wants [[Complexity MOC]]) · `Non-Interactive Zero Knowledge` ×3 · `Extendable Output Function` ×2 · `Knowledge Extractor` ×2 (worth writing) · `Complex Hilbert Space` · `Interactive Zero Knowledge` · `Proof System` · `Non-Abelian Group` · `Zyalov Bound` (→ **Zyablov**) · `Zero-knowledge MOC` (task 8.9) · the `a`/`b`/`c` accidents (0.10). The dead `Function` link in [[Prime]] is gone — resolved by the `Function between Sets` → [[Function]] rename.

**dupe (0)** — clear.

**orphan (94)** — `language/` ~50 (no MOC, task 10.10) · `cryptography/` ~17 · `math/` single digits · the rest scattered. Rising because new notes arrive faster than hubs absorb them, not decay.

**title / empty / hollow** are *smells*, not errors. Real hits: [[Security Model]] (its only definition is BRKE — task 11.7) and the 38 empty notes, a genuine stub inventory.

Trend — orphans 163 → 73 → 64 → 89 → 94; broken 25 → 19 → 14 → 13; duplicate names 1 → 0.

# Appendix B — completed

**Phase 0** 0.1–0.5 · 0.6a · 0.7–0.9 · 0.11 · 0.12 · 0.13 *(0.6b withdrawn — the `ARGument` casing marks the acronym)*
**Phase 1** 1.1–1.5 · 1.7 · 1.9 · 1.11
**Phase 2** 2.1–2.9
**Phase 3** 3.1 · 3.5
**Phase 4** 4.2 · 4.3 · 4.5 · 4.7 · 4.10 *(`\begin{CD}` works — plain MathJax)*
**Phase 5** 5.1 · 5.2 · 5.3 · 5.6 · 5.7
**Phase 6** 6.1 · 6.2 · 6.3
**Phase 7** 7.1 · 7.2 · 7.4 · 7.5 · 7.6 · 7.7
**Phase 8** 8.1 · 8.2 · 8.3
**Phase 9** 9.1–9.4 · 9.8 · 9.12 *(`scripts/vault-lint.py`)*
**Phase 10** 10.1 · 10.2
**Phase 11** 11.1 · 11.2 · 11.3 · 11.4 · 11.6
**Phase 12** Batch 0 · A1–A4 · A7 *(false set law)* · G2 · **Batch B** (B1 [[Relation]] rewritten heterogeneous-first; B2 `Function between Sets` → [[Function]], restructured with a partial-function variant; B4 odd/even → [[Calculus Functions]]) · **Batch C**, 9 of 11 (`Cancellativity`, `Absorption`, `Injection`, `Surjection`, `Bijection`, `Involution`, `Monotonicity`, `Homomorphism`, `Distance Symmetry`, the `norm/` → `metric/` merge) · **E1** [[Connexity]] rename

**Findings closed:** C1–C5 · D1–D13 · E1 · E3–E9 · F2–F7 · N5 · N6 · N9 · N11 · N13

---

# What is worth protecting

- **The relation table in [[Non-Interactive Proof Systems]]** — composition as a matrix. Mirrored by the closure table in [[Algebra MOC]], the order table in [[Math Properties MOC]], and the strength table in [[Security Game]].
- **[[Equivalence Relation]]**, **[[Commutative Ring]]**, **[[Preorder]]** — definitions that are nothing but links.
- **[[Group Homomorphisms]]** — links [[Morphism]] instead of restating it.
- **The Scope / Condition / Property template.** Twenty notes use it; every drift so far has been in the callout title, never the content.
- **[[Split-R1CS]]** citing [[Bilinearity]] — the cross-domain link this refactor exists to make routine.
