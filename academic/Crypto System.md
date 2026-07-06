
# The Architecture of Modern Cryptography — A Stability Map for a Knowledge Vault

Goal: identify what in the field is **load-bearing and stable** (safe to build vault structure on) versus **volatile** (should live in leaf notes that can be replaced without touching the skeleton). The test used throughout: _has this survived since the foundational era (roughly Goldwasser–Micali 1982 → mid-1990s) without structural change?_ Almost everything below has.

---

## Layer 0 — The epistemic stance (most stable; will never change)

Modern ("provable-security") cryptography is an **axiomatic-deductive system built on unproven axioms**:

1. **Assumptions** are the axioms: precisely stated average-case hardness claims, believed but unprovable with current techniques (proving any of them unconditionally would imply P ≠ NP).
2. **Definitions** are the specifications: precise statements of what a primitive _is_ and what "secure" means for it.
3. **Reductions** are the theorems: "any adversary breaking scheme X with advantage ε yields an adversary breaking assumption Y with advantage ε′ and comparable runtime."
4. Confidence flows **upward from axioms**, calibrated **downward by cryptanalysis** (best known attacks set concrete parameters).

This stance — definitions, assumptions, reductions — is _the_ invariant of the field. Every textbook (Goldreich, Katz–Lindell, Boneh–Shoup) is organized around it. **Vault implication:** the top-level split of the vault should mirror it: `Assumptions/`, `Primitives/`, `Reductions & Theorems/`, plus `Attacks & Cryptanalysis/` as the calibration layer. This will never need restructuring.

## Layer 1 — The three kinds of objects (stable)

Everything in cryptography is one of three object kinds, each with its own definitional template:

|Object kind|What it is|Template|Examples|
|---|---|---|---|
|**Assumption**|A hard distributional problem|Parameters → Distribution → Problem → Hardness (+ Relations)|SD, QCSD, LWE, DDH, RSA, factoring|
|**Primitive**|A functionality with a security contract|Syntax → Property → Security|PKE, KEM, signatures, PRF, PRG, hash, commitment, OWF|
|**Protocol**|An interaction among ≥2 parties|Syntax → Property → Security, but security is _simulation/ideal-functionality_ based|key exchange, ZK proofs, MPC, TLS|

You already have the templates for the first two. Protocols are the third and last kind — their distinguishing feature is that security is usually defined by comparison to an ideal world (Family-3 advantage), because "what the adversary shouldn't learn" can't be captured by a single game. **No fourth kind has emerged in 40 years.** Constructions (HQC, Kyber, ElGamal) are not a fourth kind — a construction is an _edge_: it instantiates a primitive from assumptions and/or lower primitives, and lives naturally as a `Construction` section inside the primitive's note or as its own note tagged with both endpoints.

## Layer 2 — The definitional machinery (stable)

Cross-cutting machinery used by all three object kinds. Six pieces, all settled:

**2a. Security parameter λ and asymptotics.** Everything is a family indexed by λ; "efficient" = PPT in λ; "small" = negligible in λ. The concrete-security refinement ((t, ε), or (t, q, ε) with oracle-query counts) is a _rendering_ of the same definitions, not a rival framework — every asymptotic statement has a mechanical concrete translation. Vault: one foundational note; every definition written concretely with the asymptotic version as a remark (concrete is strictly more information).

**2b. The three advantage families.** Unpredictability (bare probability, baseline ≈ 0), Indistinguishability (probability difference, baseline ½), Simulation (real vs. ideal with ∃-simulator). Every security notion and every decisional/search assumption declares one. Stable since the 1980s; the general rule generating all three: _advantage = adversary's success minus the best trivial strategy's success_.

**2c. Adversary resources, orthogonal to family.** What varies across "attack models" is never the advantage shape but the resources: runtime (PPT / t-bounded / unbounded), oracle access (CPA/CCA1/CCA2; random-oracle queries; signing queries), phases (find/guess), uniformity (uniform TMs vs. circuit families), and quantum power (see Layer 5). A security notion = **functionality + advantage family + resource profile**. This three-coordinate system classifies every notion you will ever meet (IND-CCA2 = PKE + indistinguishability + decryption-oracle-both-phases).

**2d. Perfect / statistical / computational hierarchy.** Every indistinguishability-flavored statement exists at three strengths: identical distributions (Δ=0), Δ negligible against unbounded adversaries, bounded adversaries only. Computational is where nearly all of practical crypto lives; statistical/perfect appear in information-theoretic corners (one-time pad, secret sharing, statistically-hiding commitments). Stable and complete — there is no fourth rung.

**2e. Search vs. decision duality.** For assumptions: search and decision variants, related (or provably separated) case-by-case; decision has a statistical-distance ceiling; not every assumption has both forms (bijective maps → search only; residuosity-type → decision only). You have this in the template already; it is settled machinery.

**2f. Ideal-model heuristics.** The Random Oracle Model (and relatives: ideal cipher, generic group) — proofs where a hash is modeled as a truly random function. Methodologically contested at the margins (known artificial counterexamples) but _structurally_ stable: every proof is clearly labeled ROM or standard-model, and that label is part of the theorem statement. Vault: treat the model as a field on every theorem note, never as an afterthought. QROM (quantum-accessible random oracle) is the same slot's quantum refinement.

## Layer 3 — The dependency map of primitives (stable in shape, grows at the edges)

The known implication structure among primitives — which exists-statements imply which — is one of the deepest settled results of the field:

```
                        OWF  (one-way functions — the minimal assumption)
                         │  (⟺ PRG [HILL'99] ⟺ PRF [GGM'86] ⟺ symmetric encryption,
                         │      MACs, signatures [Rompel'90], commitments, statistical ZK arguments)
                         │
        ─────────────────┼───────────────  the "Minicrypt / Cryptomania" frontier
                         │
                    PKE / key agreement   (NOT known to follow from OWF;
                         │                 black-box separated [Impagliazzo–Rudich'89])
                         │
              trapdoor functions, KEMs, oblivious transfer → MPC,
              IBE, FHE, iO  (each strictly "higher" or incomparable; iO ≈ "crypto-complete")
```

Three stable facts to build on: (1) **OWF is the minimal assumption** — almost everything implies it, and if OWF don't exist, essentially no computational crypto exists (Impagliazzo's Pessiland/Algorithmica worlds). (2) **The symmetric world (Minicrypt) is an equivalence class**: OWF ⟺ PRG ⟺ PRF ⟺ signatures — all interconvertible, so a vault can treat "Minicrypt" as one region. (3) **Public-key crypto is a genuinely separate continent** (Cryptomania), not reachable from OWF by black-box constructions. The map _grows at the top_ (FHE, iO, and their descendants) but the lower structure hasn't changed since ~1990. **Vault implication:** maintain one canonical "implication map" note; every primitive note links to its position. New primitives attach as leaves; they never reorganize the trunk.

## Layer 4 — The assumption zoo, organized by mathematical habitat (stable taxonomy, volatile membership)

Assumptions cluster by the mathematics they live in, and the _clusters_ are stable even though individual assumptions rise and fall:

|Habitat|Core problems|Search/decision pattern|Structured variant|Post-quantum?|
|---|---|---|---|---|
|**Factoring-based**|Factoring, RSA, QR, DCR|RSA search-only; QR/DCR decision-only|—|✗ (Shor)|
|**Discrete-log groups**|DL, CDH, DDH|DL search-only; CDH/DDH separated in pairing groups|pairing groups (adds structure _and_ functionality)|✗ (Shor)|
|**Lattices**|SIS, LWE|both, equivalent; **worst-case↔average-case reductions exist** (unique selling point)|Ring/Module-LWE|✓ believed|
|**Codes**|SD/LPN, rank-SD|both, believed equivalent|QCSD (your HQC material)|✓ believed|
|**Multivariate / isogenies / symmetric-based**|MQ, isogeny problems, hash-based sigs|varies|varies|✓ believed (isogenies: bruised by SIDH break 2022 — a live example of membership volatility)|

**What's stable:** the habitat taxonomy, the per-habitat "best known attack" families that calibrate parameters (NFS/index-calculus; lattice reduction/BKW; information-set decoding; Pollard-rho), and the structured-variant pattern (every habitat trades extra algebraic structure for efficiency and accepts extra cryptanalytic risk — QC codes, ideal lattices, pairing groups are the _same design move_ in three habitats). **What's volatile:** individual assumptions' health (SIDH died in a weekend in 2022; SVP estimates shift with each lattice-reduction advance). **Vault implication:** organize `Assumptions/` by habitat; give every assumption a `status` field (unbroken / weakened / broken, with date and attack reference) instead of encoding health in the folder structure.

## Layer 5 — The settings axis (stable, and orthogonal to everything above)

Every statement in the vault silently carries four toggles; making them explicit fields prevents the most common category errors:

1. **Machine model**: uniform (PPT) vs. non-uniform (circuit families). Crypto defaults non-uniform for adversaries in many texts; complexity theory cares intensely about the difference.
2. **Classical vs. quantum adversary** — and this splits further: quantum adversary with classical oracle access, vs. superposition oracle access (QROM). Post-quantum security is a _setting toggle on existing definitions_, not a new definitional framework — SD and LWE hardness are simply asserted against QPT adversaries. This is why your existing templates need zero restructuring for PQ crypto: add a `quantum-resistance` field.
3. **Asymptotic vs. concrete** (see 2a) — a rendering choice per note, not a fork in the ontology.
4. **Proof model**: standard / ROM / QROM / generic-group (see 2f) — a field on theorems.

**Vault implication:** these four become frontmatter fields on every definition and theorem note. They never justify separate folders — a folder split on any of them would double the vault for no structural gain.

## Layer 6 — Reduction techniques (the proof-pattern library; stable core, growing periphery)

The reductions themselves reuse a small set of named patterns; a vault note per pattern pays off enormously because every new proof you read decomposes into them:

- **Hybrid argument** — chain of games, adjacent pairs differing by one invocation of an assumption; total advantage ≤ sum of link advantages. The workhorse (your HQC IND-CPA proof is exactly this).
- **Game hopping / code-based games** (Bellare–Rogaway, Shoup) — formal bookkeeping discipline for hybrids; includes the **difference lemma** (games identical until a bad event ⇒ advantage gap ≤ Pr[bad]).
- **Guessing/plug-in reductions** — embed the challenge instance into the adversary's view at a guessed position; source of the Q-type loss factors in your SS→CPA box.
- **Random-oracle programming** — answer RO queries with values that embed the challenge; where ROM proofs get their power.
- **Rewinding / forking lemma** — for extracting from interactive adversaries (signatures from identification schemes); notable for _breaking_ in the quantum setting, which is exactly why QROM is its own field value.
- **Simulation** — construct the ideal-world simulator; the pattern behind all Family-3 proofs.

**Stability:** the first four have been the core since the 1990s; the periphery grows (lossy trapdoors, dual-mode systems, lattice-specific techniques) but as _new leaves_, new patterns don't invalidate old proofs.

## Layer 7 — What is genuinely volatile (quarantine zone)

Keep these in leaf notes with dates, never in the skeleton: concrete parameter recommendations (bit-security estimates move with every cryptanalytic advance); the health of individual assumptions (Layer 4's `status` field); standardization outcomes (NIST selections, deprecations); performance comparisons; and the frontier of high-end primitives (iO, FHE efficiency) where constructions are replaced wholesale every few years. A vault whose structure never references any of these will never need restructuring because of them.

---

## The resulting vault skeleton (the actual deliverable)

```
00-Foundations/
    epistemic-stance.md            (Layer 0)
    security-parameter-and-concrete-security.md  (2a)
    advantage-families.md          (2b: unpredictability / indistinguishability / simulation)
    adversary-resources.md         (2c)
    perfect-statistical-computational.md  (2d)
    proof-models.md                (2f: standard / ROM / QROM / GGM)
    vocabulary-interface.md        (crypto ↔ complexity: aliases + false-friends table)
01-Assumptions/                    (template: Params → Distribution → Problem → Hardness → Relations)
    _implication-and-habitat-map.md
    codes/   lattices/   groups/   factoring/   isogenies/
02-Primitives/                     (template: Syntax → Property → Security)
    _implication-map.md            (Layer 3 diagram)
    OWF-PRG-PRF/  PKE/  KEM/  signatures/  hash/  commitments/
03-Protocols/                      (template: Syntax → Property → Simulation-Security)
04-Reductions/
    _pattern-library.md            (Layer 6)
    per-theorem notes, each with fields: model, tightness, setting-toggles
05-Constructions/                  (HQC, Kyber, ElGamal… each tagged: primitive it realizes,
                                    assumptions it consumes, reduction notes it cites)
06-Cryptanalysis/                  (attack families per habitat; parameter status; dated)
```

Frontmatter fields on every definitional/theorem note: `object-kind`, `advantage-family`, `resources`, `model`, `setting` (uniform? quantum?), `status` + `as-of` date where applicable.

**The one-paragraph justification for why this won't need to change:** Layers 0–3 and 5–6 have been structurally fixed since roughly 1995; everything that has happened since — pairings, lattice crypto, the entire post-quantum program, FHE, iO — arrived as _new entries in existing slots_ (new habitats in Layer 4, new leaves in Layer 3's map, new toggles in Layer 5, new patterns in Layer 6's periphery), never as a change to the slot structure itself. The only plausible future events that would force a restructuring are field-level earthquakes: a proof or disproof of P ≠ NP, a practical break of a whole habitat (large-scale quantum computers killing Layer 4's first two rows — which the taxonomy already anticipates), or meta-complexity maturing into a replacement foundation for Layer 0 (in which case OWF ⟺ average-case time-bounded Kolmogorov hardness becomes the new ground floor — and even that slots in as a _deepening_ of Layer 0, not a demolition).



Cryptography work can be three cases:
1. Plausibility Results: Connect two notions or providing a generic way of solving a class of problems.
2. Introduction of paradigms and techniques that may be applicable in practice: Introduce new model, tool, or technique.
3. Presentation of schemes that are suitable for practical applications.

