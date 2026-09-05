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
| [[North Star]], [[Foundation Layer]], [[Cryptography Layer]], this plan | **me** |
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

One floor item plus the last of Batch B — unchanged for three passes. Paste-ready text in the checkpoint report and [[Foundation Layer]]; ~15 minutes.

| # | task |
| --- | --- |
| **A5** | **Link the Cartesian product.** [[Set Operation]] has zero inbound links — the definition is restored but unreachable, so rule 5 is still violated. Add links from [[Set]], [[Relation]], [[Binary Operation]], [[Function]] |
| **B3** | Last of Batch B: **G1** stray `,Reference:` at the top of [[Binary Operation]] · **G3** [[Many-Sorted Operation]] still lacks the sorts-are-labels remark, the small / locally-small caveat, and the Birkhoff–Lipson reference |

Riding along whenever you next touch these notes: Famous Sets belongs in [[Set]] not [[Set Operation]]; Disjoint should move the other way (it uses $\cap$); the law table sits under `## Notation` but is a `## Property`; "are **equals**" → "are equal"; $P(S)$ → $\mathcal P(S)$; [[Set Foundation]]'s `## Definition` is an empty heading.

---

# Queue

## Foundation — Batches C, D, E

Specification and drafts in [[Foundation Layer]]; its Status block tracks the batches.

| #     | task                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            | est    |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------ |
| **C** | **R1 persists (third pass):** [[Positive Definiteness]] still says `d(x,x) = 0 ⟺ x = 0` — presumes a zero the Scope has not got, and quantifies over the wrong pair, so it never states that distinct points cannot be at distance 0. Should be `∀x,y: d(x,y) = 0 ⟺ x = y`; the `≥ 0` bullet is still the derivable one. Then **R2** the missing `### Norm Form` sections, and [[Monotonicity]] (0 bytes, fourth pass) | 20 min |
| **D** | **The payoff — rewire consumers.** Absorbs 1.12–1.15, 5.4, 5.4b, 5.5, 6.5: the Magma→Group chain drops its [[Closure]] links and [[Group]]'s Semigroup bug; [[Group]]/[[Field]] cancellation → `Cancellativity`; [[Group Homomorphism]]/[[knowledge/math/algebra/structures/rings/Ring]]/[[Linear Maps]]/[[Subgroup]] → `Homomorphism`; [[Metric Space]] split normed-group vs metric; [[Code Distance]], [[Rank Metric Codes]], [[Statistical Distance]] → metric axioms; [[Set Operation]] laws → the five axioms; [[Calculus Functions]] → `Monotonicity`; [[Inner-Product Spaces]] → [[Map Symmetry]] + [[Linearity]] + [[Positive Definiteness]] | 2–3 h  |
| **E** | [[Connexity]] → `Connexity` (three live senses of "total" after B1) · the clone-and-edit slips (2.10) · [[Algebra Structure]] axiom index + frontmatter (1.6, 1.10)                                                                                                                                                                                                                                                                                                                                                                                                                                             | 45 min |

## Algebra structures

| # | task |
| --- | --- |
| **N1** | **Nilpotency — two new notes.** Drafts in [[Foundation Layer]] §3.12. `rings/Nilpotent Element.md` (a predicate, filed next to Unit and Zero Divisor) and `rings/special rings/Reduced Ring.md` (a mixin over [[Ring]], one axiom). **Blocked by S3** — both drafts link `[[Unit]]` and `[[Zero Divisor]]`, which are still headings inside [[Ring]] |
| **N2** | *Nilpotent ring* is **vacuous here**: [[Ring]] is unital, so $R^n = 0$ forces $1 = 0$ and $R = $ [[Zero Ring]]. The content lives on **ideals** (nil vs nilpotent) — a `###` section of `Nilpotent Element` until `Ideal.md` is promoted out of [[Ring]] |
| **N3** | Bridge: [[Operators]] already defines nilpotent for a linear operator with $N^{\dim V} = 0$. Cross-domain two-views pair — one remark each side, no restatement |
| **N4** | **`Kernel`** — draft in [[Foundation Layer]] §3.13. It is already in the vault three times and the general one is **unnamed**: [[Function]]'s `### Canonical Decomposition` *is* the kernel equivalence relation. Add `### Fibre` to [[Function]] beside `### Image` (the domain-side counterpart, general, stays inline), then one new note `set theory/function/Kernel.md` for **the partition into fibres** (Scope = a bare function, three consumers ⇒ graduates). The sub-object reading is *one distinguished fibre* and stays with each structure |
| **N5** | **The missing half of the ideal story**: [[knowledge/math/algebra/structures/rings/Ring]] defines ring homomorphisms *and* [[Ideal]]s but never says the kernel of a hom **is** an ideal, nor that every ideal is a kernel. As it stands [[Ideal]] has no stated reason to exist. **And [[Ideal]] is defined twice** — a good note at `groups/subgroups/Ideal.md` (left / right / two-sided, links [[Ring]] and [[Subgroup]]) and a weaker inline `[!definition] Ideal` in [[knowledge/math/algebra/structures/rings/Ring]]. Delete the inline one, link the note. The duplicate is *evidence* the file is misfiled: an ideal's Scope needs a **ring**, so it belongs in `rings/` — filing it under `groups/subgroups/` groups it by shape, and a reader in ring theory never finds it. Basename resolution makes the move free. Also add *“is a normal subgroup”* to [[Subgroup]]'s `### Kernel`, and a *null space = kernel* synonym line in [[Linear Maps]] |
| **N6** | Bridge remark in `Kernel.md`: readings **A** ($f^{-1}(0)$) and **B** ($f(a')=f(a'')$) agree for groups — that agreement *is* the first isomorphism theorem — and come apart for monoids. Counterexample in §3.13: $f:(\mathbb N,+)\to(\{0,1\},\max)$ has trivial kernel and is not injective. *Non-equivalent* two-views shape; do not merge. **State the criterion, not a list**: one fibre determines the congruence exactly in **$0$-regular** varieties — those with a Mal'cev term $p(x,y,z) = xy^{-1}z$. Groups, rings, modules have one; monoids, semigroups, lattices do not. Checkable rather than memorised |
| 3.2 | Give [[Group]] a `## Structure` section: [[Subgroup]], [[Normal Subgroup]], [[Cosets]], [[Quotient Group]] |
| 3.3 | Give it `## Special Groups`: [[Abelian Group]], [[Cyclic Group]], [[Symmetric Group]], [[Free Groups]], [[Bilinear Group]] |
| 3.4 | Move the $\mathrm{GL}_n$ material out of [[Group]]'s `## Example` into [[Example of Subgroups]] or a new `General Linear Group` |
| 3.6 | [[Subgroup]] states its criterion via [[Closure]] and [[Inverse Element]] — the one place [[Closure]]'s subset reading is exactly right |
| 3.7 | [[Subgroup]]' `## Property` heading is still empty (`### Image` now has content) |
| 3.8 | Stubs: [[Free Groups]] (0 bytes), [[Cosets]] (21 bytes) |
| 9.8b | The singular rename is half done in `groups/`. Renamed: [[Group]], [[Abelian Group]], [[Cyclic Group]], [[Symmetric Group]], [[Quotient Group]], [[Bilinear Group]]. Still plural: [[Free Groups]], [[Cosets]], [[Subgroup]], [[Normal Subgroup]], [[Group Homomorphism]], and the folders. Rule to settle: **singular when the note defines one object, plural when it surveys a family** |
| 7b | Split [[Field]] (14.5 KB): extract `Complex Numbers`, complex-valued calculus → `calculus/`, consider `Field Arithmetic` for the consequences table |

## Category

| # | task |
| --- | --- |
| 4.11 | **Add the partial-composition remark to [[Category]]** — composition types as $\mathsf{Hom}(A,B) \times \mathsf{Hom}(B,C) \to \mathsf{Hom}(A,C)$, one identity per object. As written, its links to [[Associativity]] and [[Identity Element]] claim more than those notes support. Fills the empty `## Property` (4.9) and carries the one-object / many-objects ladder |
| 4.1 | [[Opposite Category]] exists but does not state the duality principle |
| 4.4 | mono + epi $\not\Rightarrow$ iso, with $\mathbb Z \to \mathbb Q$ in $\mathsf{Ring}$; cross-link [[Function]], where in $\mathsf{Set}$ it *does*. Same theme, second instance: [[Group Homomorphism]] states "isomorphism iff bijection" as though definitional — it is a **theorem about groups**, false in $\mathsf{Top}$ and $\mathsf{Poset}$ |
| 4.6 | `Poset as Category` — unblocked, [[Preorder]] has content. `### Small Category` in [[Category]] is misnamed; it is this |
| 4.8 | Link [[Category]] → [[Category Set]], [[Category Group]] |
| 4.15 | The **Homomorphism ↔ Morphism bridge**: one remark per side. Morphisms are not functions (preorder-as-category has pairs as arrows); the two families coincide only in a *concrete* category — which is what licenses [[Group Homomorphism]] to import [[Morphism#Isomorphisms|iso]] |
| 4.12 | [[Morphism]]: plural headings and callout titles under a singular note name |
| 4.13 | [[Groupoids]] → `Groupoid`, and add the algebraic reading (a group with a partial operation) |
| 4.14 | [[Universal Properties]]: the Products example says "let $A, B$ be **sets**" then uses $\mathsf{Hom}_{\mathcal C}$ |

Commutative diagrams: `\begin{CD}` confirmed working, no plugin. Snippets for products and coproducts are in the conversation of 2026-08-24.

## Class / instance rollout — Batch X

The correspondence table is in [[North Star]] § *Class and instance*. The rule that keeps this cheap: **the semantics go in four header fields, not in renamed headings.** `## Definition`, `## Syntax` and `## Scheme` do not move.

| # | task | est |
| --- | --- | --- |
| **X1** | *(mine, on your word)* **Pilot on 12 notes** — add the fields to one of each shape and nothing else: [[Ring]], [[Group]], [[Field]] (`Extends:`) · [[Polynomial Ring]], [[Kyber PKE]], [[Shamir Secret Sharing]] (`Instantiates:`) · [[Associativity]], [[Cancellativity]] (mixins, no field needed — confirming they need none is the point) · [[Fujisaki-Okamoto Transformation]], [[Fiat-Shamir Transform]] (`Transforms:`) · [[Argument Systems]], [[Puncturable Pseudorandom Function]] (`Extends:` across the crypto side). You judge, then it rolls out lazily | 30 min |
| **X2** | **Backfill `Instantiates:`** across `schemes/` (~40 notes) and `structures/…/examples/` (~15). One line each, added as you touch a note. This is the field that pays first: [[Public-Key Encryption]] currently cannot list its own instances | lazy |
| **X3** | **Backfill `Extends:`** on the algebra spine and the crypto refinements. Watch for **diamonds** — [[Field]] reaches [[Ring]] two ways and nothing here will tell you. Where a diamond exists, say so in a `[!remark]`; that is the substitute for an instance resolver | lazy |
| **X4** | *(mine)* **Lint the fields**: every `Instantiates:` target has a `## Syntax` or `## Definition`; every `Requires:` bullet is a wikilink; flag a note in `properties/` whose definition introduces a carrier (it has stopped being a mixin) | 45 min |

**Scope, stated so it does not creep.** About **200 of 557** notes are structures. The other ~350 are problems ([[Closest Vector Problem]], [[Discrete Logarithm Problem]]), algorithms ([[LLL Lattice Reduction Algorithm]] and most of `cs/`), theorems, the 48 MOCs, `language/`, `security/`. **A problem is not a class.** Do not add a field to be consistent.

**Why fields and not a rewrite.** The `Basic Definition` → `Definition` pass touched 139 files and made the vault no more correct, only better named — which was the right trade there because it was one word. "Rewrite everything in class syntax" is the same trade at 200× the size, and the value is not in the words. It is in the three graphs the fields make queryable: *what extends what*, *what instantiates what*, *what depends on what*. Those you cannot get from a heading rename at any price, and you can get them from four lines added lazily.

## Cryptography — scheme form and party views

Specification, templates and the full audit in [[Cryptography Layer]]; its Status block tracks the batches. Findings are **V1–V12**, batches **K1–K6**.

**V11 settled 2026-09-03:** slots are real `###` headings under `## Scheme`, one `[!scheme]` callout each — [[Kyber PKE]] is the model, worked through in §2.5. Consequence: `[!scheme]` no longer counts schemes; the `## Scheme` heading does.

| # | task | est |
| --- | --- | --- |
| **K2b** | **Split the setting slots (V12).** Inside `[!scheme]`, `Parameters` is doing three jobs at once. Proposed slots, each pointing somewhere different: **Parameters** (nowhere — knobs) · **Setting** (down into `math/`: $R_q$, the group, the pairing) · **Spaces** (up into the primitive) · **Distribution** (down into `math/probability/`) · **Building Block** (sideways into another crypto note) · **Parties** (into the view remark) · **Statement** (into `relations/`) · **Algorithms**. You already split it twice under local names — `Ring and Modulus`/`Dimensions`/`Messages` in [[Module HGSW]], `Plaintext Space`/`Key Space` in the textbook notes. Start with [[Kyber PKE]]: $\text{Compress}_q$ and $\text{Decompress}_q$ are `Setting`, not `Building Block` | 20 min + lazy |
| **K2** | *(mine, on your word)* Mechanical: **V12** naming — `Algorithm` → `Algorithms` (4 notes), and `Building Block` ↔ `Building Blocks` once you pick one (vault leans singular 26–4, your new [[Kyber PKE]] uses plural) · **V1** rename `## Encryption Scheme`/`## Signature Scheme` → `## Scheme` and `[!algorithm]` → `[!scheme]` in 10 textbook notes · **V2** fix 9 `[!scheme]` callouts sitting under an h1 / `## Syntax` / orphan h3 · **V10** `Link:` → `Reference:`. No content touched | 15 min |
| **K7** | **Transforms (V13).** A `## Syntax` note *with* `Building Blocks` is a **transform**, not a plain primitive — its blocks are universally quantified and each owes a hypothesis in `## Security`. [[Fujisaki-Okamoto Transformation]] has four blocks and **no security section at all**; [[From Collision Resistance]] is 132 B. Also: [[Public-Key Encryption]] (17 KB) hides three transforms inside the interface note — TDF→PKE, plus the RSA and ElGamal case studies, each with its own loss factor. [[North Star]] now lists Transform as a fifth kind | 45 min |
| **K3** | **The gate.** Only **4 of 40** scheme notes carry the full Kyber shape; `## Property` appears in 8, `### Correctness` in 5, `[!security]` in 5. Walk the 40 and mark each **spec** (owes correctness + a security reduction) or **recipe** (owes nothing beyond `## Scheme`). Everything after this depends on the answer | 30 min |
| **K4** | **Party views (V7, ~16 notes).** Start with [[Interactive Proof Systems]] — it already writes $\text{View}_{\hat{\mathcal V}}$ inside its zero-knowledge definition without defining it. Then [[Secure Multi-party Computation]], then lazily. Standardise on $\mathsf{View}$ | 20 min + lazy |
| **K5** | **V4/V9 — the biggest structural distortion.** Four signature schemes hide inside encryption notes ([[RSA Public Key Cryptosystem]], [[ElGamal Public Key Cryptosystem]], [[NTRU Public Key Cryptosystem]], [[GGH Public Key Cryptosystem]]) while [[Digital Signature]] is a 240 B stub and [[Old Digital Signature]] holds 20 KB of security model. Extract four notes into `digital signatures/schemes/`; fold the security model into [[Digital Signature]] | an afternoon |
| **K6** | **V5** adopt `## Cryptanalysis` as the slot for attacks (10 places invent a heading; the four classical ciphers' `## Security` is a break, not a game) · **V6** stubs: [[Merkle Tree]] 40 B is load-bearing for [[Kilian Interactive Argument of Knowledge from PCP]] · **V8** [[Dilithium]] is one heading from complete · add `Instantiates:` lines | lazy |
| **K2c** | **[[Kyber PKE]] finish** — draft in [[Cryptography Layer]] §2.5: add a `### Setting` block **first** (it currently uses $R_q$, $\mathbb Z_q$, $\mathcal M$, $\bmod^{\pm}$, $\|\cdot\|_\infty$ without declaring any of them) · move $\text{Compress}_q$/$\text{Decompress}_q$ out of Building Blocks into Setting, leaving Building Blocks **links only** · spell the reference name $\mathsf{Kyber.PKE}$ in all three places · $\text{Adv}$ → $\mathsf{Adv}$. Two missing notes fall out: `Extendable Output Function` (broken link, also from [[Keccak]]) and `Quotient Ring` (a heading inside [[knowledge/math/algebra/structures/rings/Ring]], never promoted) | 15 min |

## Cryptography — content

| # | task |
| --- | --- |
| **V14** | **Correctness vs completeness — three mislabels.** Rule and test in [[Cryptography Layer]] §2.7: *correctness* reproduces data, *completeness* produces a verdict and has a [[Soundness]] partner across a promise. [[Puncturable Pseudorandom Function]]'s `Completeness of Puncturing` → `Correctness` · [[Secure Multi-party Computation]]'s `[!definition] Soundness` → **Correctness** (soundness is not an MPC notion) · [[Completeness]] calls a **success probability** $\mathsf{Adv}^\mathsf{cmp}$ and then names it the *error* — they are $1$ apart, and this one will bite inside a proof |
| **V15** | Add to [[Security Game]]: **$\mathsf{Adv}$ is a quantity you drive to zero** — completeness is the single place that breaks, so flag it where the convention lives. Then one `[!remark]` each in [[Completeness]] and [[Soundness]] naming the borrowing from proof theory ([[First-Order Logic]], Gödel). Do **not** bridge to [[Class NP-complete]] or [[Real Number]] — different word, no dual |
| 11.7 | [[Security Model]] still contains **only** a BRKE definition. Move it to `key establishment/key exchange/Bidirectional Ratcheted Key Exchange`; rewrite as the umbrella — a notion is syntax + [[Security Game]] + [[Adversary]] class + bound |
| 11.5 | [[Indistinguishability]] game-first: retag the game `[!algorithm]` → `[!definition]`; state perfect and statistical as rows of the [[Security Game]] table |
| 11.8 | Payoff: [[Argument Systems]] = "[[Interactive Proof Systems]] with computational [[Soundness]]"; [[Perfect Security]] links the perfect row |
| **V16** | **NILP review — `st` vs `td`.** Full writeup in [[Cryptography Layer]] §2.8. `st` has two roles (verifier's checking material / simulator's trapdoor); in the linear model they are the *same vector*, and **whether they may be identified is exactly the DV / PV split** — [[LUNA]] is DV so `st` is secret and conflating is harmless; publicly-verifiable means `vk` is published and `td` destroyed, where conflating publishes the trapdoor. **Recommendation: keep one symbol `st` in the NILP note**, add the two-hats remark, introduce `td` only in the compiled scheme |
| **V17** | **Bugs found in the same pass.** (a) Both [[Non-Interactive Linear Proofs]] and [[Split Non-Interactive Linear Proofs]]: `Prove(R, x, w)` returns $\Pi\,\mathrm{crs}$ — **`crs` is not an argument** · (b) NILP has **no `## Property` / `## Security` at all** — drafts for completeness, non-adaptive knowledge soundness against affine strategies, and perfect ZK are in §2.8 · (c) `\mathbf F` → `\mathbb F` in three places |
| **V18** | **[[Linear Probabilistically Checkable Proofs]] HVZK is ill-formed.** Both games' simulated branch generates $(\widetilde{\mathrm{st}}, \widetilde{\mathbf Q}, \mathrm{st}_\mathcal S)$ then calls $\mathcal A_\mathsf{guess}(\mathrm{st}, \mathbf Q, \widetilde{\mathbf a})$ — **`st` and `Q` are unbound there**. Must be the tilde'd pair. As written the branches are not comparable |
| **V19** | **[[Split Non-Interactive Linear Proofs]] is a verbatim copy** of its parent, callout title and all (two `[!definition] Non-Interactive Linear Proof` in the vault). Rewrite as `Extends:` + the two-line delta — §2.8 has the draft. It is the first real test of the `Extends:` field from **X1** |
| **V20** | **Factor the proof-system properties (§2.9).** A property is *game shape* × *response map $\mathcal O$* × *adaptivity* × *strength row*, and three of those already have homes. `proof/properties/<P>.md` owns the game once over an abstract $(\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify}, \mathcal O)$; a system note carries a one-line instantiation (*"[[Completeness]] with $\mathcal O(\Pi) = \Pi\,\mathrm{crs}$, $\varepsilon_c = 0$"*) — a **note link, not a heading anchor**. Factor [[Completeness]] fully · [[Soundness]]/[[Knowledge Soundness]] statement-only, games stay local (quantifier order is the content) · **do not factor [[Zero Knowledge]]** — LPCP's simulator makes its own query, NILP's is handed `st`; that gap is the content |
| **V21** | **The bridge that makes V20 possible.** LPCP's `[!definition] Linear Oracle` and NILP's `[!definition] Linear Evaluation` are **one equation with the pen in different hands**: both are a $k \times m$ matrix against an $m$-vector, but LPCP's verifier picks the matrix and the prover the vector, while NILP's prover picks the matrix and `Setup` the vector. That swap is *why* NILP soundness must be non-adaptive and why the two ZK definitions differ in shape. One `[!remark]` each side, cross-domain bridge |
| **V22** | **`Disclosure-Free NILP`** — draft in [[Cryptography Layer]] §2.10. Groth16's Definition 4 is stated for a **split** NILP, so `Extends: [[Split Non-Interactive Linear Proofs]]` and the chain is NILP → Split → Disclosure-Free (which makes **V19** load-bearing). **Blocked by V17**: Groth16's test is $t(\sigma, \pi)$, our `Test` is $\mathbf t : \mathbb F^k \to \mathbb F^\eta$ applied to $\boldsymbol\pi$ alone — the test never sees $\mathrm{crs}$, and disclosure-freeness is *entirely* about that dependence, so the property is currently **unstatable**. One `[!todo]` left in the draft: I could not get Definition 4 verbatim (eprint blocks fetch), so check equality-vs-bound against the paper |
| **V23** | **Tier-1 vs Tier-3 properties — the graduation rule differs** (§2.10). Equational properties bind by *substitution*, so theorems transfer verbatim and a note pays as soon as a second definition binds it ([[Associativity]] → generalized associativity, proved once). Game properties bind by *family resemblance*; graduate only when the difference fits a parameter slot, else keep the game local. Ranked: [[Soundness]] and [[Zero Knowledge]] earn shared notes (amplification, composition), [[Completeness]] is mostly a comparison table, disclosure-freeness stays inline. Add the rule to [[North Star]] once you have used it twice |
| **V24** | **The simulator has no quantifier (§2.11).** [[Knowledge Soundness]] correctly writes *“for any $\mathcal A$ **there exists** $\mathcal E$”*; [[Zero Knowledge]] writes *“for any $\mathcal A$ **and** simulator $\mathcal S$”*, which is $\forall\mathcal S$ and not the notion. Fix is **one sentence per game**, using [[Security Game]]'s own game/notion seam: the advantage is a function of $(\mathcal A, \mathcal S)$, the *notion* says $\exists \mathcal S\ \forall \mathcal A$. Note the orders are opposite — ZK is $\exists\mathcal S\forall\mathcal A$, knowledge soundness is $\forall\mathcal A\exists\mathcal E$, and $\forall\mathcal A\exists\mathcal E$ **is not a falsifiable game** (Naor), which is why succinct arguments need knowledge assumptions |
| **V25** | **Give $\mathcal S$ a signature**, declared above the game like `Prove`/`Verify` — with the *“receives no witness”* line stated in prose, not buried in a probability array. **Phases are derivable**: one per scheme algorithm the simulated branch fakes. Checks out on all four notes (NIPS 2, LPCP 2, NILP 1, [[Split Prover]] 1). The two shapes are **setup simulation** vs **trapdoor simulation** — the same fork as §2.8's `st`/`td`. Rename $\mathrm{st}_\mathcal S$ → $\mathrm{aux}_\mathcal S$ |
| **V26** | **The distinguisher has amnesia.** In [[Zero Knowledge]], $\mathcal A_\mathsf{find}$ sees $(\mathcal R, \mathrm{crs}, \mathrm{st})$ but $\mathcal A_\mathsf{guess}(\boldsymbol\pi)$ gets *only the proof* — no state, not even the statement. House format passes one ([[Public-Key Encryption]]'s IND game). Same gap in [[Linear Probabilistically Checkable Proofs]]. Also: [[Knowledge Soundness]] declares $\mathcal E = (\mathcal E_\mathsf{NIPS})$ then calls $\mathcal E_\mathsf{find}$; its affine variant is labelled $\mathsf{Adv}_\mathsf{NIPS}$ but is about a NILP; `\mathbf F` → `\mathbb F`; a type declaration sits in the event column |
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
| S1 | [[Ring]] has **two** `[!definition] Unit` callouts — delete the old one-liner under `### Quotient rings` |
| S2 | **Six full-path wikilinks with unique basenames** — [[Field]], [[Polynomial]], [[Division Ring]], [[Cyclic Codes]], [[Information Theory MOC]], [[Post-Quantum Cryptography MOC]]. Two render the whole path on the page. Full paths are correct *only* where the basename is ambiguous, as in `security/`'s eleven `CTF Challenges`. **Plus 8 dead `[[daily/Temp/PPT]]` links** in [[Negligible Function]], [[Puncturable Pseudorandom Function]], [[Special Functions]] (×3), [[Interactive Proof Systems]], [[Succinctness]] — the note now lives at `cryptography/foundations/PPT.md`, so these should be plain `[[PPT]]` |
| S3 | Promote **`Unit`** and **`Zero Divisor`** out of [[Ring]] into `rings/` — [[Field]] and [[Division Ring]] currently link the heading anchor `Ring#Unit`, which the linter cannot see |
| S4 | `Rings of Power Series` is **0 bytes** — fill or delete *(the two h3 headings and `Monoid Ring` are done)* |
| S5 | [[Integral Domain]] could compose from [[Cancellativity]] — *a nonzero commutative ring whose nonzero elements are cancellative* |
| 9.7 | `Pseudorandom Functionsss` duplicate; [[Universal Hash Functions]] empty; [[Special Functions]]' empty `### Prefix-Free` / `### Unpredictability` |
| 9.11 | Adopt the `## Intuition` convention (nLab *Idea*), backfilled lazily |
| 10.3 | The AHE near-duplicate pair — `Additively-Homomorphic Encryption` (information theory) vs `Additive-Homomorphic Encryption` (crypto). One letter apart, different folders |
| 10.4 | `post-quantum/lattice-based/Lattice.md` has an **empty** `## Definition` and one trapdoor lemma → rename `Lattice Trapdoors`, link [[Lattices]] |
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
| V3 | Three names for the defining slot: `## Definition` (math), `## Syntax` (crypto interface), `## Scheme` (crypto instance) | **Keep all three, narrowly.** `## Syntax` is the literature's own word for exactly this and is already consistent across 28 notes; the interface/instance obligations really do differ. But three names for one idea is how conventions quietly stop being followed — if a fourth ever appears, collapse back to `## Definition` and let the callout type carry the level. I lean this way without arguing hard |

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

Trend — orphans 163 → 73 → 64 → 89 → 94 → 97; broken 25 → 19 → 14 → 13 → **14**; duplicate names 1 → 0.

The broken count went *up* because the linter got sharper, not because the vault got worse: it used to resolve `[[daily/Temp/PPT]]` by basename and call it fine. Obsidian resolves any link containing a slash as a **path**, so `vault-lint.py` now does too. The 8 PPT links were dead all along — see **S2**.

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
**Phase 12** Batch 0 · A1–A4 · **A6** *(eight set-operation definitions)* · A7 *(false set law)* · G2 · **Batch B** (B1 [[Relation]] rewritten heterogeneous-first; B2 `Function between Sets` → [[Function]], restructured with a partial-function variant; B4 odd/even → [[Calculus Functions]]) · **Batch C**, 9 of 11 (`Cancellativity`, `Absorption`, `Injection`, `Surjection`, `Bijection`, `Involution`, `Monotonicity`, `Homomorphism`, `Distance Symmetry`, the `norm/` → `metric/` merge) · **E1** [[Connexity]] rename · **E2** `Basic Definition` → `Definition` (141 headings across 135 notes, 15 anchor links in 10 notes, two h3 promoted to h2)

**Findings closed:** C1–C5 · D1–D13 · E1 · E3–E9 · F2–F7 · N5 · N6 · N9 · N11 · N13

---

# What is worth protecting

- **The relation table in [[Non-Interactive Proof Systems]]** — composition as a matrix. Mirrored by the closure table in [[Algebra MOC]], the order table in [[Math Properties MOC]], and the strength table in [[Security Game]].
- **[[Equivalence Relation]]**, **[[Commutative Ring]]**, **[[Preorder]]** — definitions that are nothing but links.
- **[[Group Homomorphism]]** — links [[Morphism]] instead of restating it.
- **The Scope / Condition / Property template.** Twenty notes use it; every drift so far has been in the callout title, never the content.
- **[[Split-R1CS]]** citing [[Bilinearity]] — the cross-domain link this refactor exists to make routine.
