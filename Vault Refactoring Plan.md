# Vault Refactoring Plan — revised

*Scouted 2026-08-20 against `knowledge/` (483 notes) and the full vault (709 notes). Every claim below was checked against the files, not inferred from the previous plan.*

---

## Part I — Corrections to the plan you wrote

Five items are wrong or already done. Two of them would destroy content or waste an evening.

### C1. `lkdsjjfowjfdowoiwoif.md` is not junk — do not delete it

It is **6,086 bytes of real lattice content**: apprSVP, the Shortest Independent Vector Problem, Hermite's Theorem (both forms), the Hadamard ratio, Minkowski's Theorem, the ball-volume formula, the Gaussian heuristic, Babai's Closest Vertex algorithm, and the LLL-based approximate-CVP algorithm. Only the filename is garbage.

It is also the only place in the vault where those results live — `Lattices.md` (5,849 B) does not repeat them.

**Do instead:** rename to `Short Vectors in Lattices.md`, then split along the seam already present in its headings:

| new note | absorbs |
| --- | --- |
| `Lattice Problems.md` | apprSVP, SIVP, Approx-SIVP, the `SVP_γ` hardness remarks |
| `Lattice Bounds.md` | Hermite, Hadamard ratio, Minkowski, ball volume, Gaussian heuristic |
| `Babai's Algorithm.md` | Babai closest-vertex, LLL-based approximate CVP |

It also carries three empty headings — `## Blichfeldt's Theorem`, `## Pick's Theorem`, and an empty `## Property` — which are placeholders, not content. Keep them as a TODO list or drop them, but decide consciously.

Note the overlap you will inherit: `Lattice Problems.md` will restate what `cryptography/assumptions/lattice-based/SVP/{Shortest Vector Problem, Closest Vector Problem, Shortest Basis Problem}.md` already say. Those three are orphans (no inbound links). Resolve the direction once: **math states the problem, crypto states the hardness assumption.**

### C2. Most of Phase 5 is already done

Checked line by line against the notes:

| plan item | actual state |
| --- | --- |
| "add the linear oracle remark to `Linear Probabilistically Checkable Proofs.md`" | **done** — the `[!definition] Linear Oracle` callout ends with "the verifier $\mathcal V$ only has access to this response, not the proof string $\boldsymbol\pi$" |
| "add the non-adaptivity remark to LPCP" | **done** — LPCP has non-adaptive *and* adaptive soundness, and non-adaptive *and* adaptive knowledge soundness, as four separate games |
| "…and to `Non-Interactive Linear Proofs.md`" | **done** — "Every proof — honest or adversarial — is of this form: the prover chooses only the coefficient matrix, never the field elements" |
| "`Non-interactive ARGument.md` and `ARgument of Knowledge.md` still duplicate the three algorithm bullets" | **false** — both are already three-line compositional notes. NARG = NIPS + Completeness + computational Soundness; NARK = NARG with Soundness strengthened to Knowledge Soundness. No `Setup/Prove/Verify` bullets in either. |
| "Missing leaves: SNARG, SNARK, zkSNARK, zkSNARG" | **already exist**, as `###` sections inside those two notes, each defined by composition and reachable via `[[#SNARG]]`-style links |
| "adaptive/non-adaptive in `Soundness.md`" | **done** — both games are there |
| "`Split Prover.md` needs split correctness + split ZK in game form" | **done** — both are written as advantage games |
| "the leakage parameterization in `Zero Knowledge.md`" | **partly** — the leakage variant exists, but in `Linear Probabilistically Checkable Proofs.md` (`hvzk-D`), not in `Zero Knowledge.md` |

What is genuinely left in Phase 5 is different, and smaller, than what you wrote. See Phase 8.

**The judgement call this raises:** SNARG/SNARK/zkSNARK already work as headings. Promoting them to standalone notes buys you a graph node and a place to hang scheme links (`Groth16` → SNARK); it costs you four notes that will each be two lines long. My read: promote **SNARK only**, because that is the one with schemes attached and the one other notes will want to link to. Leave SNARG/zk-SNARG/zk-SNARK as headings until something needs to link to them.

### C3. Phase 1 undercounts the duplication — there are four sites, not two

| note | how the axioms appear |
| --- | --- |
| `structures/groups/Groups.md` | Identity / Inverse / Associative spelled out as three numbered bold items inside the definition callout |
| `Ring.md` | eight bold axiom names as bullets, no definitions, no links |
| `Field.md` | a six-item `[!axiom] The Field Axioms` callout naming Commutative / Associative / Distributive / Identity / Inverse again |
| `structures/Algebra Structure.md` | a six-row markdown table: Identity Law, Inverse Law, Associative Law, Commutative Law, Distributive Law, Alternative — **with the formal statements**, which the other three lack |

`Algebra Structure.md` is the one that already does the job properly. Phase 1 is really *"extract that table into six notes and point the other three at them"* — which makes it cheaper than you budgeted, because the content already exists in written form.

A fifth site is `set theory/Set.md`, which restates Commutative / Associative / Distributive laws for $\cup$ and $\cap$. That one is legitimately separate (it is an instance, not a restatement), but it should link to the new notes once they exist.

### C4. Groupoids — the duplicate is an empty stub, and the survivor is in the wrong folder

- `set theory/Groupoids.md` — contains exactly `## Basic Definition` and nothing else. Delete.
- `groups/Groupoids.md` — 126 B, the real one: *"A [[Category]] in which every morphism is an isomorphism."*

But that definition is stated in terms of `Category`, not in terms of groups. It belongs in `algebra/category/`, not `algebra/structures/groups/`. Move it there in Phase 4, where you are already touching the category folder.

### C5. Abelian Groups has the same stub/content inversion, and you did not catch it

- `groups/special groups/Abelian Groups.md` — 21 bytes. `## Basic Definition`, empty. **The better name.**
- `groups/Commutative Groups.md` — 679 B, the real content: the definition (already correctly written as *"a [[Groups]] whose operation is [[Commutativity|Commutative]]"* — exactly the composed style Phase 1 is aiming for), the additive-notation remark, and the $g^2 = e \Rightarrow$ abelian example.

Merge into `special groups/Abelian Groups.md` and delete `Commutative Groups.md`. Everything else in the vault — `Ring.md`, the closure table, standard usage — says "abelian".

---
## Part II — What the scout turned up that the plan does not cover

### N1. The entire `groups/` subtree is unreachable — 9 orphans

Zero inbound links, from anywhere in the vault:

```
Subgroups          Normal Subgroups   Cosets          Quotient Groups
Symmetric Groups   Free Groups        Bilinear Groups Abelian Groups
Example of Subgroups
```

`Groups.md` links to none of them. Instead it carries an inline `## Subgroup` section holding *Additive Subgroup*, *Discrete Additive Subgroup*, and Lagrange's Theorem — while `subgroups/Subgroups.md` sits beside it, unread.

This is the same failure mode as Phase 1 (a hub note restating rather than composing), but it costs you more: nine notes you have written and cannot find.

**Also, a real error in `Groups.md`:** Lagrange's Theorem appears twice with two different statements. The version under `### Order` reads *"let $n = |G|$ be the order of $G$ and let $n$ be the order of $g$"* — the same symbol bound twice — and then asserts $a^k = e$ for an $a$ that was never introduced. The version under `## Subgroup` ($|H|$ divides $|G|$) is correct. Keep the second, fix or delete the first.

### N2. `Set.md` duplicates `Relations.md` and `Equivalence Relations.md` wholesale

`Set.md` has a `## Relations on Sets` section defining Relation, Equivalence Relation, Equivalence Class, and Quotient — the same four things that `relations/Relations.md` and `relations/Equivalence Relations.md` define. And `Set.md` itself is an orphan.

Worse, `Equivalence Relations.md` is already the *good* version — it is three links to Reflexivity / Symmetric / Transitivity, exactly the Phase 1 style. `Set.md` restates it longhand right next to it.

Separately, `Set.md` and `Set Theory.md` are two notes with no clear division: Cartesian product is defined in `Set Theory.md` and listed as an operation in `Set.md`; the empty set appears in both. Decide the split explicitly — my suggestion: `Set.md` = objects, notation, operations, algebra of sets; `Set Theory.md` = cardinality, countability, and the foundational material (Russell's paradox should move there from `Set.md`).

### N3. `Function.md` is the largest misfiling in `math/` — 12 KB in the wrong folder

It lives at `math/algebra/structures/set theory/Function.md`. Its contents, in order:

| section | actually belongs in |
| --- | --- |
| Function, domain, co-domain, range, equality, odd/even | stays (or merges with `Function between Sets.md`) |
| Natural logarithm, its properties, $\log_b$, the $P_n$ / error-term theorems | `math/calculus/` |
| Complex Logarithm, `Log z` | `math/algebra/Field.md`'s complex material (see N4) |
| Exponential function $E(x)$ | `math/calculus/` |
| Logarithmic integral $\mathrm{Li}(X)$ | `math/number theory/Prime.md` — it exists for the PNT |
| Monotonic / strictly monotonic / piecewise monotonic | `math/calculus/` |
| Convex / concave, derivative test | `math/calculus/Inequality.md` |
| **Jensen's Inequality** (stated twice, once probabilistically) | `math/probability/Probability Inequalities.md` |
| Composition, Inverse | duplicates `Function between Sets.md` — merge |
| Root, isolated root | `math/calculus/` |
| Lipschitz-1 | `math/calculus/` |
| Lambda function (Carmichael) | `math/number theory/` |
| Gamma function + Stirling | `math/calculus/` or a new `math/analysis/Special Functions.md` |
| Bessel functions, Bessel's equation | `math/calculus/Differential Equations.md` |
| Unit step, Dirac delta | `math/calculus/` (used by `Fourier Analysis.md`, also an orphan) |
| Von Mangoldt $\Lambda$ | `math/number theory/Prime.md` |

Note the collateral damage this is already causing: `Math MOC.md` lists `[[Function]]` as a *top-level* math note, but it is buried four levels deep inside `algebra/structures/set theory/`. And `Gamma` is referenced from the lattice ball-volume formula in C1, from a folder that has no reason to reach into set theory.

### N4. `Field.md` carries a complex-analysis note inside it

`Field.md` is 14.5 KB, and roughly the back half is Complex Numbers, Complex Exponentials, Complex-valued Functions (derivative, integral), the $y'' + ay' + by = 0$ characteristic-equation theorem, and DeMoivre. That is not field theory; $\mathbb C$ is one example of a field.

Split out `math/algebra/Complex Numbers.md` (the field structure: definition, conjugate, modulus, polar form, $e^{i\theta}$) and move the calculus of complex-valued functions to `math/calculus/`. What stays in `Field.md`: axioms → integral domain → characteristic → finite fields → extension fields.

The arithmetic-identity table in `Field.md` (Cancellation, Possibility of Subtraction, ~20 rows of $-(a+b) = -a-b$ etc.) is derivable-consequences, not axioms. Consider a `## Consequences` collapse or a separate `Field Arithmetic.md`, so the axioms are not buried under it.

### N5. `Cryptography MOC.md` is stale — it describes a vault you no longer have

Its folder-layout code block lists `zero-knowledge/`, `homomorphic encryption/`, `assumptions/dlp/`, and `post-quantum cryptography/code-based/`. **None of those directories exist.**

It omits, entirely: `verifiable computing/` (where nearly all your current work is), the `primitive/` wrapper level, `special functions/`, `pseudorandom/`, `identification protocols/`, `relations/`.

Consequences visible in the link graph: `[[Zero-knowledge MOC]]` is broken and linked 4 times; `[[Homomorphic Encryption MOC]]` is broken.

This is your crypto entry point and it points at a tree from before the refactor. It should be rewritten in the same pass that adds the Verifiable Computing MOC — not later.

### N6. `Algebra MOC.md` has no entry for four of its own subfolders

It covers Foundations, Linear Structures, Geometric/Number-Theoretic. It does **not** mention:

- `category/` — 3 notes + 2 examples
- `properties/` — 5 notes, the folder Phase 1 and 2 are about to triple
- `structures/set theory/` — 8 notes
- the `structures/groups/` subtree — 9 notes (see N1)

So the two closure tables Phase 1–2 produce would land in a MOC that does not currently reach the notes they summarise. The MOC needs a structure pass, not a table insertion.

### N7. Copy-paste bleed from the LPCP note into the shared property notes

Two of these are wrong, not just untidy:

- **`properties/Soundness.md`, Adaptive Soundness** — the game verifies `Verify(st, x, Q^T π*)`. $\mathbf Q$ is the LPCP *query matrix*; a `Non-Interactive Proof Systems` has no query matrix. Should be `Verify(st, x, π*)`.
- **`properties/Zero Knowledge.md`** — declares $\mathcal S = (\mathcal S_\mathsf{setup}, \mathcal S_\mathsf{prove})$, then the ideal-world game invokes `S_query(R)` and binds $\widetilde{\mathbf Q}$, which is never used. Both lines are LPCP leftovers.
- **`Non-Interactive Proof Systems.md`, the relation table** — the last row is labelled `zk-SNARG` but has Knowledge ✓, so it is `zk-SNARK`. And the first cell links `[[Non-Interactive Proof|NIP]]`, which is a broken target — the note is `Non-Interactive Proof Systems`.

That table is otherwise the single best artefact in the crypto side of the vault. It is the model for the two closure tables Phase 1–2 produce. Worth fixing precisely because so much else will point at it.

### N8. 25 broken wikilinks vault-wide

Real missing notes — decide create-or-unlink for each:

```
4  [[Complexity Theory]]           4  [[Zero-knowledge MOC]]
3  [[Non-Interactive Zero Knowledge]]  2  [[Knowledge Extractor]]
2  [[Extendable Output Function]]  1  [[Proof System]]
1  [[Interactive Zero Knowledge]]  1  [[Homomorphic Encryption MOC]]
1  [[Integer Factorization]]       1  [[Non-Abelian Group]]
1  [[Pseudorandom Number Generators]]
1  [[Foundational Math for Zero Knowledge Proofs]]
```

Accidental links — these are typos, not intent:

```
[[a]] ×3, [[b]], [[c]], [[dp]], [[greedy]], [[osint]], [[zER]]
[[Non-Interactive Proof\]]                    (malformed alias)
[[symmetric encryption/classical/]]           (folder link, not a note)
[[symmetric encryption/schemes/]]
[[\text{HighBits}(r) \neq \text{HighBits}(r + z)]]   in Dilithium.md
[[\text{Number of 1's in } h \text{ is} \leq \omega]] in Dilithium.md
[[c = H(\mu]]                                 in Dilithium.md
```

The three in `Dilithium.md` are `[[ ]]` used where `$$ $$` was meant — display math that turned into links.

### N9. `Foundations MOC` exists three times — this breaks Obsidian's shortest-path linking

```
complexity/foundations/Foundations MOC.md
cryptography/foundations/Foundations MOC.md
cs/foundations/Foundations MOC.md
```

This is why `Cryptography MOC.md` had to write out the full path `[[knowledge/cryptography/foundations/Foundations MOC]]` — an ugly link that will break the moment you move a folder. Rename to `Complexity Foundations MOC`, `Cryptography Foundations MOC`, `CS Foundations MOC`.

(`CTF Challenges` exists 11 times, once per security subfolder. Same hazard, but there it is probably deliberate — leave it unless you start linking to them.)

### N10. Frontmatter is in an unresolved half-state

Of 709 notes: 44 have `parent:`, and **all 44 are legacy fleeting notes** in `language/`, `security/`, and one stray in `math/algebra/structures/Algebra Structure.md`. 41 carry the `🪴weedy` tag. A scattered handful carry `dg-publish: true` for the digitalgarden plugin — including several verifiable-computing notes, apparently ad hoc.

Nothing in `knowledge/` uses frontmatter systematically. Your `templates/default.md` still writes `parent: "[[Fleeting MOC]]"` into every new note.

This is a decision, not a cleanup: either **(a)** adopt a minimal schema in `knowledge/` — `parent`, `status`, `dg-publish` — so MOC sections can be Dataview-generated instead of hand-maintained (you already have the dataview plugin and a `dataview-tables.css` snippet), or **(b)** drop `parent:` from the template and commit to MOCs plus links as the only structure. Both are fine. Doing half of each, which is the current state, means the graph and the folders disagree.

Given how much MOC hand-maintenance the phases below imply, **(a) is worth pricing.** A `parent:` field would make N6 self-maintaining.

### N11. Root-level debris

- `Untitled.md` — empty. Delete.
- `Characteristic.md` — a Vietnamese fleeting note about MLWE / rank-metric ciphertext malleability ($(u, v) = (u, su + e + \hat m)$). Nothing to do with field characteristic, despite sitting one search away from `Field.md#Characteristic`. Move to `daily/` or file it under `cryptography/assumptions/lattice-based/` with a real title.
- `Fleeting MOC.md` — a one-line dummy. Fine as long as the template keeps pointing at it; delete it if you choose N10(b).

### N12. Orphan clusters map exactly onto missing hub notes

157 of 470 `knowledge/` notes have zero inbound links. They are not evenly spread — they cluster in folders with no MOC:

| folder | orphans | has MOC? |
| --- | --- | --- |
| `cryptography/verifiable computing/**` | 20 | **no** |
| `math/algebra/structures/groups/**` | 9 | no |
| `cryptography/assumptions/{lattice,coding}-based/**` | 9 | parent only |
| `cryptography/special functions/**` | 6 | no |
| `complexity/complexity class/**` | 5 | no |
| `information theory/` (incl. `Entropy`, `Information Theory` itself) | 3 + 6 in `code-based/` | **no MOC at all** |
| `cryptography/threshold cryptography/secret sharing/**` | 4 | parent only |
| `math/algebra/category/example/` | 2 | no |
| `cs/arithmetization/` | 2 (QSP, SSP) | no |

`information theory/` having no MOC is notable given your stated goal of extending the vault beyond crypto — it is 20 notes with no entry point, and `Entropy.md` is unreachable.

### N13. `cs/arithmetization/` is on the wrong side of a seam

`Quadratic Arithmetic Program`, `Quadratic Span Program`, `Square Span Program`, `R1CS to QAP Reduction` live in `cs/`. `Rank-1 Constraint Statisfiability` and `Split-R1CS` live in `cryptography/verifiable computing/relations/`. `QAP-based Linear PCP` reaches across the two.

Nothing else in `cs/` uses QAP. Arithmetization exists *for* proof systems. **Move `cs/arithmetization/` to `verifiable computing/relations/arithmetization/`** and let `R1CS to QAP Reduction.md` sit next to the R1CS note it reduces from. This is also what makes the Verifiable Computing MOC complete rather than a half-index.

---
## Part III — The revised plan

Ten phases. Phases 0–3 are the spine; everything after is independently orderable.

Do all renames and moves **inside Obsidian** so backlinks follow. Commit to git between phases — you have a repo, use it as the undo button.

---

### Phase 0 — hygiene and safety · ~30 min

| #    | task                                                                                                                                                                                    | note                                 | Status                          |
| ---- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ------------------------------- |
| 0.1  | **Rename** `structures/lattices/lkdsjjfowjfdowoiwoif.md` → `Short Vectors in Lattices.md`                                                                                               | **do not delete** — see C1           | Done                            |
| 0.2  | Delete `set theory/Groupoids.md` (empty stub); keep `groups/Groupoids.md`                                                                                                               | C4                                   | Done                            |
| 0.3  | Merge `groups/Commutative Groups.md` into `special groups/Abelian Groups.md`; delete the former                                                                                         | C5                                   | Done                            |
| 0.4  | Fix the callout title in `properties/Transitivity.md` — it says "Reflexivity"                                                                                                           | verified                             | Done                            |
| 0.5  | Fix scope in `Reflexivity` / `Symmetric` / `Transitivity`: a relation is $\sim\, \subseteq S \times S$, not $\sim: S \times S \to S$                                                    | verified — all three are wrong       | Done                            |
| 0.6  | Rename `Rank-1 Constraint Statisfiability.md` → `Rank-1 Constraint Satisfiability.md`; normalise casing in `Non-interactive ARGument.md` and `Non-interactive ARgument of Knowledge.md` | 5 inbound links follow automatically | I want unnormalise for clarity? |
| 0.7  | Rename the three `Foundations MOC.md` to `Complexity/Cryptography/CS Foundations MOC.md`                                                                                                | N9                                   | Done                            |
| 0.8  | Delete `Untitled.md`; move `Characteristic.md` out of the vault root                                                                                                                    | N11                                  | Done                            |
| 0.9  | Fix the three `[[…]]`-as-display-math accidents in `Dilithium.md`                                                                                                                       | N8                                   | Done                            |
| 0.10 | Sweep the accidental links: `[[a]]`, `[[b]]`, `[[c]]`, `[[dp]]`, `[[greedy]]`, `[[osint]]`, `[[zER]]`, the two folder-links, the malformed `[[Non-Interactive Proof\]]`                 | N8                                   | Reserved                        |
| 0.11 | Fix `Verify(st, x, Q^T π*)` → `Verify(st, x, π*)` in `Soundness.md`; delete the stray `S_query` line in `Zero Knowledge.md`; relabel `zk-SNARG` → `zk-SNARK` in the NIPS table          | N7 — these are wrong, not untidy     | Done                            |
| 0.12 | Fix or delete the garbled first Lagrange's Theorem in `Groups.md`                                                                                                                       | N1                                   | Done                            |

The remaining 12 broken links (`[[Complexity Theory]]`, `[[Zero-knowledge MOC]]`, …) are **create-or-unlink decisions**, not hygiene. Park them until Phase 8.

---

### Phase 1 — operation axioms · the highest-leverage step

Create in `properties/`, using your existing **Scope / Condition / Property** template:

`Closure` · `Associativity` · `Identity Element` · `Inverse Element` · `Distributivity` · `Idempotence` (Done)

Source the formal statements from the table already in `structures/Algebra Structure.md` — do not rewrite them from scratch.

Then rewrite the four restatement sites:

| note                   | becomes                                                                                                                                                           |               |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------- |
| `Groups.md`            | *"a set with a binary operation satisfying [[Associativity]], [[Identity Element]], [[Inverse Element]]"*                                                         | Done          |
| `Ring.md`              | *"an [[Abelian Groups\|abelian group]] under $+$, a monoid under $\star$, plus [[Distributivity]]"*                                                               | Done          |
| `Field.md`             | *"a commutative [[Ring]] in which every nonzero element has an [[Inverse Element\|inverse]]"* — then delete the six-item `[!axiom]` block, which is now redundant | Done          |
| `Algebra Structure.md` | keep the table, but make each row's name a link; it becomes the axiom index rather than a fourth definition                                                       | Need checking |

**A caution on `Closure`.** In the modern formulation closure is not an axiom — it is built into "binary operation $S \times S \to S$", which is exactly how your own `Commutativity.md` already writes its Scope. Write `Closure.md` as *"a condition that is automatic once the operation is typed $S \times S \to S$; stated separately only when checking that a subset is a substructure"* — and then it earns its keep, because that is precisely how `Subgroups.md` will use it.

Add to `Algebra MOC.md`:

|               | closure | assoc | ident | inv | comm |
| ------------- | :-----: | :---: | :---: | :-: | :--: |
| magma         |    ✓    |       |       |     |      |
| semigroup     |    ✓    |   ✓   |       |     |      |
| monoid        |    ✓    |   ✓   |   ✓   |     |      |
| group         |    ✓    |   ✓   |   ✓   |  ✓  |      |
| abelian group |    ✓    |   ✓   |   ✓   |  ✓  |  ✓   |

---

### Phase 2 — relation axioms, and promoting `properties/`

There are still some small naming and wording issue in the properties part I believe.
**2.1 — Move `math/algebra/properties/` → `math/properties/`.**

Relation axioms are order theory, norm axioms are analysis, and `information theory/code-based/Code Distance.md` needs the metric axioms too. The folder outgrows `algebra/` the moment Phase 2 lands. Do the move *before* adding notes to it, so fewer backlinks have to follow.

**2.2 — Add** `Antisymmetry` and `Totality`.

**2.3 — Split into** `properties/operation/` and `properties/relation/`. `Bilinearity.md` stays put for now; it moves in Phase 5.

**2.4 — Rewrite `Equivalence Relations.md`** — actually, it is already three links. Instead, point `Set.md`'s duplicate section at it (see Phase 6) and add the equivalence-class / quotient material that `Set.md` currently monopolises.
(Maybe I should move Relation from set to properties?)
**2.5 — Second table for the MOC:**
which MOC is this

|               | reflexive | symmetric | antisymmetric | transitive | total |
| ------------- | :-------: | :-------: | :-----------: | :--------: | :---: |
| preorder      |     ✓     |           |               |     ✓      |       |
| partial order |     ✓     |           |       ✓       |     ✓      |       |
| total order   |     ✓     |           |       ✓       |     ✓      |   ✓   |
| equivalence   |     ✓     |     ✓     |               |     ✓      |       |

This table is what gives your two category examples a name — see Phase 4.

---

### Phase 3 — wire up the `groups/` subtree · **new, and I would do it third**

Nine notes you wrote and cannot reach (N1). Cheaper than Phase 1 and it makes Phase 1's payoff visible.

| #   | task                                                                                                                                                                                                                   |
| --- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 3.1 | Replace `Groups.md`'s inline `## Subgroup` section with a link to `[[Subgroups]]`; move *Additive Subgroup* and *Discrete Additive Subgroup* into `Subgroups.md` (they are used by `Lattices.md`, not by group theory) |
| 3.2 | Give `Groups.md` a `## Structure` section linking `Subgroups`, `Normal Subgroups`, `Cosets`, `Quotient Groups`                                                                                                         |
| 3.3 | Give it a `## Special Groups` section linking `Abelian Groups`, `Cyclic Groups`, `Symmetric Groups`, `Free Groups`, `Bilinear Groups`                                                                                  |
| 3.4 | Move the `GL_n` / `GL_2(\mathbb Z_n)` material out of `Groups.md`'s `## Example` into `example/Example of Subgroups.md` or a new `example/General Linear Group.md`                                                     |
| 3.5 | Add `Groups MOC.md`, or fold the above into `Algebra MOC.md` — decide once whether `groups/` is big enough to deserve its own hub (I think yes, at 14 notes)                                                           |
| 3.6 | Have `Subgroups.md` state its criterion using `[[Closure]]` and `[[Inverse Element]]` — this is where Phase 1 pays off concretely                                                                                      |

---

### Phase 4 — category folder

| # | task |
| --- | --- |
| 4.1 | Promote `Opposite Category` out of `Category.md` into its own note; state the duality principle once, there |
| 4.2 | Move `groups/Groupoids.md` → `category/Groupoids.md` (C4) and expand it: composition in a category is **partial**, which is the property groupoids are about |
| 4.3 | In `Morphisms.md`: mark endo/auto as **variants** (constrain $A = B$), mono/epi/iso as **properties** |
| 4.4 | Add the remark that mono + epi $\not\Rightarrow$ iso, with $\mathbb Z \to \mathbb Q$ in $\mathsf{Ring}$ — and cross-link `Function between Sets.md`, which already proves that in $\mathsf{Set}$ it *does* (injective ⟺ mono, surjective ⟺ epi). The contrast is the point |
| 4.5 | Fix the coproduct definition in `Universal Properties.md` — the arrows are reversed. It should read $f_A \in \mathrm{Hom}(A, Z)$, not $\mathrm{Hom}(Z, A)$ |
| 4.6 | Move the two poset examples (`Equivalence Category`, `Small Category`) out of `Category.md` into `example/Poset as Category.md` — they are one construction, and Phase 2 now gives you the word for it: a **preorder** viewed as a category |
| 4.7 | Cross-link `Category.md`'s axioms 3 and 4 to `[[Associativity]]` and `[[Identity Element]]` |
| 4.8 | Link `Category.md` → `example/Category Set.md`, `example/Category Group.md` (both orphans) |
| 4.9 | Fill or delete `Category.md`'s empty `## Property` heading |

---

### Phase 5 — map and norm axioms

`properties/map/` — `Linearity`, `Multilinearity`, `Homomorphism`. Currently assumed with no shared source by `Linear Maps.md`, `Bilinear Pairings.md`, `Kronecker Product.md`, `Group Homomorphisms.md`, and `Ring.md` (which defines ring homomorphism inline). `Bilinearity.md` moves here.

`Group Homomorphisms.md` is worth reading first — it already links `[[Morphisms#Isomorphisms]]` and `[[Morphisms#Monomorphisms]]` rather than restating them. That is the target pattern; copy it.

`properties/norm/` — `Triangle Inequality`, `Homogeneity`, `Positive-definiteness`. Source them from `Metric Space.md`, which already states all three correctly (and has a typo: *"the norm function $\mathcal N: \mathcal X \leftarrow \mathbb R$"* — arrow is backwards).

Consumers to rewire: `Metric Space.md`, `Inner-Product Spaces.md`, everything in `structures/lattices/`, and — the reason this folder leaves `algebra/` — `information theory/code-based/Code Distance.md` and `rank-metric/Rank Metric Codes.md`.

---

### Phase 6 — set theory consolidation · new

| # | task |
| --- | --- |
| 6.1 | Delete `Set.md`'s `## Relations on Sets` section; link to `[[Relations]]` and `[[Equivalence Relations]]` instead |
| 6.2 | Move equivalence class / quotient from `Set.md` into `Equivalence Relations.md` |
| 6.3 | Draw the `Set.md` / `Set Theory.md` line: **`Set.md`** = objects, notation, operations, algebra of sets; **`Set Theory.md`** = cardinality, countability, foundations. Russell's paradox moves to the latter |
| 6.4 | Merge the overlapping Composition / Inverse material in `Function.md` and `Function between Sets.md` — keep it in `Function between Sets.md`, which does it better |
| 6.5 | Link `Set.md`'s operation-laws table to the Phase 1 notes (Commutativity, Associativity, Distributivity) as *instances* |

---

### Phase 7 — split `Function.md` · new, and the biggest single cleanup in `math/`

Work the table in **N4** row by row. Suggested order, easiest first:

1. Jensen's Inequality → `Probability Inequalities.md` (it is stated twice in `Function.md`, once in probabilistic form — pick that one)
2. Von Mangoldt, Lambda, $\mathrm{Li}(X)$ → `number theory/Prime.md`
3. Convexity / concavity → `calculus/Inequality.md`
4. Log / exp / monotonicity / roots / Lipschitz → `calculus/`
5. Gamma, Bessel, Dirac delta, unit step → `calculus/Differential Equations.md` and `calculus/Fourier Analysis.md` (both under-linked; `Fourier Analysis.md` is an orphan)
6. Complex Logarithm → the new `Complex Numbers.md` from Phase 7b

What is left of `Function.md` is ~1 KB of general function vocabulary. Merge it into `Function between Sets.md` and delete it — then fix `Math MOC.md`, which currently lists `[[Function]]` as a top-level math note (N3).

**7b — split `Field.md`** (N4): extract `math/algebra/Complex Numbers.md`; move complex-valued calculus to `calculus/`; consider a `Field Arithmetic.md` for the 20-row consequences table so the axioms are not buried.

---

### Phase 8 — finish the crypto side · smaller than you thought, plus one thing you missed

Given C2, what actually remains:

| # | task |
| --- | --- |
| 8.1 | **Write `Verifiable Computing MOC.md`.** 20 orphans hang off this folder — `commitment/` (5), `encoding scheme/` (2), `proof/scheme/` (3), `proof/oracle/` (3), plus `Circuits`, `Split-R1CS`, `Split Prover`, `Groth16`, `LUNA`, `Private Information Retrieval`, `Argument Systems`, `Multi-Prover Interactive Proofs`. Include the lattice table |
| 8.2 | **Rewrite `Cryptography MOC.md`** (N5). Its folder diagram describes a tree that no longer exists and omits `verifiable computing/` entirely. This is the crypto entry point — it should not survive the refactor unchanged |
| 8.3 | Move `cs/arithmetization/` → `verifiable computing/relations/arithmetization/` (N13); link `QSP` and `SSP`, both orphans |
| 8.4 | Promote **SNARK** to its own note (see C2); hang `Groth16` and `LUNA` off it. Leave SNARG / zk-SNARG / zk-SNARK as headings |
| 8.5 | Add the leakage parameterisation to `Zero Knowledge.md` — the LPCP note has `hvzk-D` locally; the shared property note does not |
| 8.6 | Add a `reusable` variant to `Knowledge Soundness.md`. Note the existing remark there already explains why there is no *adaptive* variant (the extractor sees the prover's randomness) — good, keep it, and put the reusable variant beside it |
| 8.7 | Explain "input-independent" in the LPCP definition — the phrase carries weight and is unglossed |
| 8.8 | Work the 12 genuine broken links (N8): `[[Complexity Theory]]` ×4 probably wants to point at `Complexity MOC`; `[[Zero-knowledge MOC]]` ×4 needs a decision now that `zero-knowledge/` does not exist as a folder; `[[Knowledge Extractor]]` ×2 is a real missing note worth writing |

---

### Phase 9 — cross-domain hubs · optional, do when the orphan count annoys you

| # | task |
| --- | --- |
| 9.1 | `Information Theory MOC.md` — 20 notes, no entry point, and `Entropy.md` is unreachable. The cheapest large win outside crypto |
| 9.2 | `Special Functions MOC.md` under `cryptography/special functions/` — 6 orphans |
| 9.3 | Link `Complexity MOC` → `Class P`, `Class NP`, `Class NP-hard`, `Class NP-complete`, `Class coNP` — all five orphaned |
| 9.4 | Decide N10 (frontmatter). If you go with `parent:`, most of Phases 3/8/9's hand-maintained MOC lists become Dataview queries and stop rotting |

---

## Order, and why

**0 → 1 → 3 → 2.** Phase 0 first, always — the renames must land before anything links to the new names.

I have moved **Phase 3 (groups wiring) ahead of Phase 2**, against your ordering. Reason: Phase 3 is the cheapest phase in the plan, it recovers nine notes from invisibility, and it gives Phase 1 something to *do* — `Subgroups.md` restating its criterion via `[[Closure]]` and `[[Inverse Element]]` is the first place a reader sees why the axiom notes exist. Phase 2's payoff (the order table) is real but arrives later.

**4 depends on 1–3.** The category axioms link to Phase 1's notes; the poset examples need Phase 2's vocabulary; `Groupoids` moves in from the folder Phase 3 touches.

**5, 6, 7, 8, 9 are mutually independent.** Phase 8 is independent of all the algebra work — do it whenever the crypto side is what you are actually reading.

**If you only do one thing:** still Phase 1 — but note it is *cheaper* than you budgeted, because `Algebra Structure.md` already contains the six formal statements. It is an extract-and-link job, not a write-from-scratch job. Six short notes, and it converts four restatement sites into composed definitions.

**If you only do one thing after that:** Phase 8.2. A stale entry-point MOC quietly undoes the legibility that every other phase is buying.

---

## What is already good, and worth protecting

Naming this explicitly because the phases above are all criticism:

- **The relation table in `Non-Interactive Proof Systems.md`** is the best artefact in the vault. NIP / NARG / NARK / SNARG / SNARK / zkSNARK as a matrix over Completeness × Soundness × Knowledge × Succinct × ZK — the composition is legible at a glance. Both closure tables in Phases 1–2 are the same move applied to algebra. Keep doing this.
- **`Equivalence Relations.md`** is already three links and nothing else. That is the target shape for every definition in the vault.
- **`Group Homomorphisms.md`** links `[[Morphisms#Isomorphisms]]` instead of restating. So does `Commutative Groups.md`. The pattern is already in your hands — Phase 1 is generalising something you have done twice, not introducing something new.
- **The Scope / Condition / Property callout template** in `properties/` is a genuinely good local convention. All 12 new axiom notes should use it unchanged.
- **`Split-R1CS.md`** deriving the split form by citing `[[Bilinearity]]` is exactly the cross-domain link the algebra refactor is meant to make routine.
