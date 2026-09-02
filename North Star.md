---
dg-home: true
dg-publish: true
---

# North Star

*Why this vault exists, how it is built, and what to do when lost. If you are reading this in the garden: welcome — this is the map.*

## The vision

One connected reference for everything I learn. When something new arrives, the graph should surface everything already known about its objects, and the new thing should enter as a few leaf notes plus the links that place them. Like a literature review that never goes stale; like Lean's self-containment, but in natural language, for humans — no compiler, and none wanted.

## The method — signature and structure

Every piece of knowledge is one of four kinds:

| kind | what it is | lives in | examples |
| --- | --- | --- | --- |
| **Object** | the raw typed things | `math/set theory/` | [[Relation]], [[Binary Operation]], [[Function]] |
| **Property** | one axiom, stated once, in the Scope / Condition / Property shape | `math/properties/`, `proof/properties/` | [[Associativity]], [[Soundness]] |
| **Structure / scheme** | object + chosen properties, **composed by links** | `structures/`, `primitive/`, `proof/` | [[Group]], [[Non-interactive ARGument]] |
| **Bridge** | a translation between two representations | wherever its ends are | [[R1CS to QAP Reduction]], [[Fiat-Shamir Transform]] |

A definition *links* its axioms and never restates them. `## Syntax` in a crypto note and `### Scope` in a math note are the same slot. A property becomes an axiom only when a definition requires it — which is why the folder is `properties/`, not `axioms/`.

Formal systems (first-order logic, equational logic, type theory, security games) are **content, not the medium**: the vault is written in informal-rigorous prose, states each concept once in its home system, and writes bridges where representations meet. Conflicts between systems are resolved by one remark at the boundary where they bite.

## The precision skeleton

Prose is free everywhere **except five places**. These get checked; everything else is voice:

1. **Scope lines type-check** — every symbol declared with its type; every link targets the declared kind.
2. **Quantifiers bound, order explicit.**
3. **Definition ≠ theorem** — consequences never live inside definition callouts.
4. **Side conditions in the Condition slot** — "nonzero" is a condition, not an equation.
5. **Dependencies are links** — a concept a definition uses but cannot link is a *detected gap*: create the note.

## Two views

A concept with two equivalent characterizations is stated **once**, in one primary form.

- **Same domain** — the other forms follow as an `## Equivalent Characterizations` theorem in the same note. Model: [[Perfect Security]].
- **Different domains** — each side keeps its own idiom, and one carries a bridge remark naming the equivalence. Never the whole concept twice. Model: [[Statistical Distance]] → [[Indistinguishability]].
- **Not equivalent** — the surviving direction and the separating example *are* the content. Model: statistical vs computational [[Indistinguishability]].

Cryptography is dense in these, because a security notion can be phrased as what an adversary cannot do, or as what information is not there — and most foundational results are the theorem that the two coincide.

## Intuition

Notes meant for sharing open with an `## Intuition` section (nLab's *Idea*) — always outside the definition callouts, so the friendly voice never contaminates the skeleton.

## When lost

1. Enter through a hub: [[Math MOC]] · [[Cryptography MOC]] · [[Complexity MOC]] · [[CS MOC]] · [[Information Theory MOC]] · [[Security MOC]].
2. Learning something new: name its **objects** → search each → backlinks show everything already known → file what is missing as leaf notes → add one line to the right MOC → if it translates between representations, write the **bridge**.
3. Notation lives in [[Tag System]]; the object → axiom → structure spine is mapped in [[Foundation Layer]]; live work — and how to hand it back to Claude — is in [[Vault Refactoring Plan]].
4. Before committing: `python scripts/vault-lint.py`. Broken links and duplicate names are always real; the other four checks are smells.

## Known tensions

Kept here deliberately, so the vision stays honest:

- **This is a solo nLab.** Curation cost grows with the vault while my time does not; entropy is continuous (new notes arrive faster than hubs absorb them). Perfection is an asymptote — budget a recurring gardening pass and accept decay between passes.
- **Backlinks find what was linked, not everything related.** Silent relatedness — same technique, analogous proof — is invisible until a bridge note names it. Search and memory still matter.
- **Cryptography moves; the Stacks Project's subject does not.** Notes hold *concepts*; papers are references, not sources of truth; security-level claims get a date.
- **The skeleton has no compiler.** Clone-and-edit errors recurred three times *under active review*. Review rhythm, git commits, and lint scripts are the substitute — without them, drift wins.
- **The garden shows a slice.** A composed definition reads broken to a visitor if its axiom links are unpublished. Publish dependency closures, not lone notes.
