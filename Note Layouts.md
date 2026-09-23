---
dg-publish: true
---
# Note Layouts

*Every skeleton in one place. Pick a row, copy the block. The reasoning behind each lives in [[North Star]], [[Foundation Layer]] and [[Cryptography Layer]]; this file is the lookup.*

Insertable copies are in `templates/`, prefixed `layout-` — **Insert template** puts one at the cursor.

## Which layout?

| you are writing                                     | layout                     | lives in                                     |
| --------------------------------------------------- | -------------------------- | -------------------------------------------- |
| a typed thing — set, relation, function, operation  | **Object** (1)             | `math/set theory/`                           |
| one axiom, no carriers of its own                   | **Property** (2), a mixin  | `math/property/`                             |
| an object plus chosen axioms                        | **Structure** (3)          | `math/algebra/structures/`                   |
| a concrete model of a structure                     | **Example** (4)            | `structures/<X>/example/`                    |
| a cryptographic interface — a tuple of algorithms   | **Primitive** (5)          | `primitive/`, `verifiable computing/`        |
| one concrete instantiation of a primitive           | **Scheme** (6)             | `<primitive>/scheme/`                        |
| an interactive protocol for one language            | **Scheme** (6)             | `complexity/interactive/`                    |
| *give me an $X$, I build you a $Y$*                 | **Transform** (7)          | under the **output** primitive               |
| *these two are the same thing seen differently*     | **Bridge**                 | wherever its ends are                        |
| a worst-case computational problem                  | **Problem** (8)            | `complexity/…/problem/<subject>/`            |
| the average-case hardness claim                     | **Assumption** (9)         | `cryptography/assumptions/`                  |
| a security notion — any game                        | **Security property** (10) | `verifiable computing/property/`             |
| a named result other notes invoke                   | **Theorem** (12)           | with its subject                             |
| a machine — configurations and a step relation      | **Machine** (13)           | `computability/computing model/`             |
| a parameterised family $\mathsf{X}(f(n))$           | **Generator** (14)         | `complexity/…/complexity class/generator/`   |
| one named complexity class                          | **Complexity class** (15)  | `complexity/…/complexity class/class/`       |
| a hub                                               | **MOC** (11)               | beside what it indexes                       |

**The two tests that decide most cases.** Does it declare carriers of its own? If no, it is a Property, not a Structure. Does the theorem about it carry a multiplicative loss factor? If yes, it is a Transform, not a Bridge.

## Header fields — provenance above, relations inside

**Revised 2026-09-09.** Two kinds, and they do not belong in the same place:

- **Provenance** is about the *note* — where you read it. Goes **above the first heading**.
- **Relations** are about the *object* — they are clauses of the definition. Go **inside the definition callout**, written with `::` so Dataview still indexes them.

The vault already did this in prose: [[Integral Domain]] reads *"an integral domain is a nonzero [[Commutative Ring]] $R$ (with 1) such that…"* — the parent sits inside the definition. A structured field is that same idea made queryable, not a competing convention.

> [!warning] The field never replaces the sentence
> `Extends:: [[Monoid]]` alone does not say **what is added**. The definition still owes the delta —
> *"Extends [[Turing Machine]]; the transition function becomes …"*

Fields:

| field                 | means                                                     | example                                                        |
| --------------------- | --------------------------------------------------------- | -------------------------------------------------------------- |
| `Reference:` *header* | where it comes from                                       | a paper URL, a book and section                                |
| `Extends::`           | this **is** that one, plus a condition                    | `Extends:: [[Multitape Turing Machine]]`                       |
| `Generalizes::`       | this **widens a slot** of that one                        | `Generalizes:: [[Turing Machine]]`                             |
| `Instantiates::`      | a concrete witness of an interface                        | `Instantiates:: [[Public-Key Encryption]]`                     |
| `Requires::`          | building blocks, or a theorem's dependencies              | `Requires:: [[Hardness and Completeness]]`                     |
| `Member of::`         | this problem lies in that class                           | `Member of:: [[Class NP]]`                                     |
| `Complete for::`      | complete, **and the reduction**                           | `Complete for:: [[Class NP]] under [[Polynomial-time Karp Reducibility]]` |
| `Hard for::`          | hard, and the reduction                                   | `Hard for:: [[Class NP]] under [[Polynomial-time Karp Reducibility]]`    |
| `Import`              | parameters pulled from another note, in a `Parameters` callout | `[[Syndrome Decoding Problem]]: Import $(n, k, w)$`       |

> [!warning] Two ways a field silently fails
> **One colon.** `Instantiates:` is invisible to Dataview. Every relation key takes `::`.
> **A link in the key.** Dataview reads everything before `::` as the field name, so
> `[[Hardness and Completeness|Complete]] for:: [[Class NP]]` has the key
> `[[Hardness and Completeness|Complete]] for` and matches nothing.
> **The key is plain text; links belong in the value.** Put the concept link on its own
> `Requires::` line above.

### Extends or Generalizes — the direction test

> **`X Extends:: Y`** iff every X **is** a Y, once you forget X's extra axioms.
> **`X Generalizes:: Y`** iff every Y **is** an X.

Both tolerate a canonical embedding, exactly as Lean's `extends` does with a coercion — $q \mapsto \{q\}$ for DFA ↪ NFA, $\Gamma \cong \Gamma^1$ for TM ↪ Multitape.

Worked: `DFA Extends:: NFA` ✓ (a DFA is an NFA with single-valued $\delta$) · `Multitape Generalizes:: Turing Machine` ✓ (widens $\delta$'s codomain) · `Offline TM Extends:: Multitape` ✓ (adds "never writes tape 1") · `Log-Space Uniform Circuit Family Extends:: Circuit Family` ✓ (adds a generation condition).

This has been reversed three times. When unsure, say the sentence out loud with *"every … is a …"*.


---

## 1 · Object

```markdown
Reference:

## Definition

> [!definition] <Name>
> <the defining sentence; every symbol typed, every dependency a link>

### <Derived vocabulary that only exists once the object does>

## Property

## Variant

## Example

## Related
```

## 2 · Property — a mixin

```markdown
## Definition

> [!definition] <Name>
> ### Scope
> A [[Binary Operation]] $\star : O \times O \to O$.
>
> ---
> ### Condition
> <side conditions — "nonzero", "$w \mid n$". Omit when there are none>
>
> ---
> ### Property
> $\star$ is **<name>** iff
> $$\forall x \in O: \dots$$

## Property

### <theorems about the property itself — these are what inheritance buys>

## Example

### <where it holds, and the counterexample where it fails — the boundary is the point>

## Related
```

**A mixin declares no carriers.** The moment it introduces a set or an operation of its own it has become a Structure.

## 3 · Structure

```markdown
Reference:

## Definition

> [!definition] <Name>
> Extends:: [[<parent>]] + [[<the added axiom>]]
> A **<name>** is a [[<parent>]] $(S, \star)$ that additionally satisfies [[<axiom>]].

## Structure

## Property

## Variant

## Example

## Related
```

Compose by **link**. A definition that restates an axiom it could link is the one thing this vault is against.

## 4 · Example — an instance

```markdown
Reference:

## Definition

> [!definition] <Name>
> Instantiates:: [[<the structure>]]
> <the carrier and the operations, concretely>

## Property

### <what is special about this one — not what every instance has>

## Related
```

---

## 5 · Primitive — a cryptographic interface

```markdown
---
dg-publish: true
---
Reference:

## Syntax

> [!definition] <Primitive> Scheme
> A **<primitive>** $\Pi = (\mathsf{Alg}_1, \dots)$ is a tuple of efficient algorithms with
> <spaces: $\mathcal M$, $\mathcal C$, $\mathcal K$, …>.
> - $out \leftarrow \mathsf{Alg}_1(in)$: <one sentence>

> [!remark] View                        ← multi-party / interactive only
> $\mathsf{View}_i = (x_i, r_i, m_i^{(1)}, \dots)$ — and which security notion quantifies over it.

## Property

### Correctness

## Security

### <Game name>

> [!definition] <Primitive> <Game> Advantage
> $$\mathsf{Adv}^{\text{<game>}}_\Pi(\mathcal A) = \dots$$
> $\Pi$ is **<notion>** if <quantifier> such that the advantage is <bound> for every $\mathcal A \in \mathbb A$.

## Related
```

`## Security` here holds **definitions of advantage**. A number belongs one level down, in a Scheme.

## 6 · Scheme — one instantiation

```markdown
---
dg-publish: true
---
Reference:

## Scheme

Reference Name: $\mathsf{<Name>}$
Instantiates:: [[<Primitive>]]

### Setting

> [!scheme] Setting
> - <the ambient mathematics: $R_q$, a group $\mathbb G$, $\bmod^{\pm}$ — links into `math/`>

### Parameters

> [!scheme] Parameters
> - <the knobs you choose; these link nowhere>

### Building Blocks

> [!scheme] Building Blocks
> - <other cryptographic objects it calls — **every bullet is a wikilink**>

### Algorithms

> [!scheme] Algorithms
> - $out \leftarrow \mathsf{Alg}(in)$:
> 	1. …

## Property

### Correctness

> [!property] $\mathsf{<Name>}$ Correctness

## Security

### <Game name>

> [!security]
> For any [[<Primitive>#<Game>|<game> adversary]] $\mathcal A$ there is a
> [[<Assumption>#Assumption|<assumption> adversary]] $\mathcal B$ with $\dots$

## Cryptanalysis                        ← attacks, not games. `[!attack]`

## Related
```

The security callout links **up** to the primitive's game and **down** to an assumption. Without both it is a floating claim.

> [!remark] The same layout serves a complexity protocol
> An interactive protocol for one language — a Graph Non-Isomorphism protocol, [[Sum-Check Protocol]],
> [[Schnorr Protocol]] — is a Scheme whose primitive is a proof system: `Instantiates:: [[Probabilistic Interactive Proof System]]`,
> `### Setting` points **down** at the language, `### Parties` are Prover and Verifier.
> Two adjustments: `## Security` holds the **soundness error** rather than a game, and `## Cryptanalysis` is omitted.

Slot discipline: **Parameters** point nowhere · **Setting** points down into `math/` · **Spaces** point up into the primitive · **Building Blocks** point sideways · **Parties** point into the View remark. Write only the slots that have content; the minimum is Parameters + Algorithms.

## 7 · Transform

```markdown
Reference:

## Syntax

> [!definition] <Name>
> ### Building Blocks
> - $\Pi_\mathsf{in}$: any [[<input primitive>]]     ← universally quantified
> - $H$: a hash function
>
> ---
> ### Algorithms
> …

## Property
### Correctness

## Security

> [!security]
> If $\Pi_\mathsf{in}$ is <hypothesis> and $H$ is <hypothesis>, then the output is <notion>,
> with loss factor $\dots$

## Related
```

**Every Building Block must reappear in `## Security` carrying a hypothesis.** Blocks with no hypothesis mean the security section is unfinished.

---

## 8 · Problem — worst case

```markdown
Reference:

## Definition

> [!definition] Parameters
> - <or `[[<other problem>]]: Import (…)`>

> [!definition] <Name> Relation
> ### Scope
> Instance: <format>.  Solution: <format>.
>
> ---
> ### Condition
> <parameter constraints>
>
> ---
> ### Relation
> $(\text{instance}, \text{solution}) \in \mathcal R$ iff <predicate>

## Problem

### Search Variant
Given an instance, find a solution.

### Decision Variant
Is the instance in $\mathcal L_\mathcal R = \{\mathbf x : \exists \mathbf w,\ (\mathbf x, \mathbf w) \in \mathcal R\}$?

## Claim

> [!remark]
> <NP-completeness, and best known algorithms with their cost>

## Related
```

**No distribution appears here.** `### Scope` is the instance *format*; a measure on it belongs to the Assumption.

## 9 · Assumption — average case

```markdown
Reference:

## Parameters

> [!definition] Parameters
> - [[<the Problem>]]: Import $(\dots)$

## Distribution

> [!definition] <Name> Distribution
> ### Distribution
> Sampling experiment: $\mathrm{<NAME>}(\dots)$
> 1. …

## Problem

### Search Variant                      ← a **search game**

> [!definition] Search <Name> Advantage
> $$\mathsf{Adv}^\mathsf{search}(\mathcal A) = \Pr[\dots]$$

### Decision Variant                    ← a **distinguishing game**

> [!definition] Decision <Name> Advantage
> $$\mathsf{Adv}^\mathsf{decide}(\mathcal A) = \big|\Pr[\dots] - \Pr[\dots]\big|$$

## Claim

> [!remark]
> <the hardness assertion; whether search and decision are equivalent, and by which theorem>

## Related
```

Two traps. **"Decision" means membership in the Problem note and distinguishing here** — they are different questions. And **worst-case NP-completeness does not imply average-case hardness**; codes have no worst-case→average-case reduction, lattices do. Say so in `## Claim`.

## 10 · Security property — any game, not just proof systems

```markdown
## Definition

> [!definition] <Name>
> ### Scope
> A <primitive> $\Pi$; an [[Adversary]] class $\mathbb A$; auxiliary algorithms (<simulator, extractor>).
>
> ---
> ### Condition
> - **Access** — what $\mathcal A$ may query and when: the oracle set ($\mathcal O_\mathsf{find}, \mathcal O_\mathsf{guess}$),
>   or the response map $\mathcal O$ for a proof system.
> - **Promise** — what the challenger guarantees about the input ($\mathbf x \in \mathcal L$, $\mathbf x \notin \mathcal L$, $(\mathbf x, \mathbf w) \in \mathcal R$, none).
> - **Quantifier** — $\forall \mathcal A$, and where $\exists \mathcal S$ / $\exists \mathcal E$ sits relative to it.
> - **Adaptivity** — when $\mathcal A$ commits, relative to `Setup`.
>
> ---
> ### Property
> $$\mathsf{Adv}(\mathcal A) \leq \varepsilon \qquad \text{(or } \geq 1 - \varepsilon \text{ for completeness)}$$
> A **search** game ($\Pr[\text{win}]$) or a **distinguishing** game ($|\Pr[G_0] - \Pr[G_1]|$) — see [[Security Game]].

## Variant

## Related
```

**Access is the one general knob.** [[Public-Key Encryption]] already parameterises it — $\mathsf{atk} \in \{\mathsf{cpa}, \mathsf{lta}, \mathsf{cca}\}$ selects which oracles each phase gets — and a proof system's response map is the same slot under another name.

Those four Condition lines are not a wish list: **each one is a place something broke.** Access → an adversary handed the *real* state in a simulated branch. Promise → completeness confused with soundness. Quantifier → a simulator with no $\exists$. Adaptivity → a non-adaptive model written adaptively.

**Where it stops.** Correctness has no adversary; succinctness is a complexity predicate, not a game; and UC / composability is a different framework entirely (an ideal functionality and an environment, not a two-party experiment). Do not force those into this shape.

## 11 · MOC

```markdown
# <Area> MOC

<one sentence: what this area is>

## Theory
## <Concrete things>
## Related
```

## 12 · Theorem

A theorem note is a **Property note whose Scope is its hypotheses**. There is no sixth kind of note.

```markdown
Reference:

## Definition

> [!theorem] <Name>
> ### Scope
> <the hypotheses, each symbol typed and linked>
>
> ---
> ### Condition
> <side conditions the statement silently needs>
>
> ---
> ### Property
> <the conclusion, with its bound>

## Property

### <sharpness, tightness, what fails without each hypothesis>

## Example

### <the counterexample when a hypothesis is dropped>

## Related
```

**When does a theorem graduate?** When it is **invoked, not merely known** — when other notes cite its bound or check its hypotheses. A theorem that is a fact *about* one object stays as a `[!theorem]` inside that object's note.

An empirical version of the same test, which you can just run:

```
grep -rho '^> \[!\(theorem\|lemma\|proposition\|corollary\)\] .\+' --include='*.md' . \
  | sed 's/^> \[![a-z]*\] //' | sort | uniq -c | awk '$1>=2' | sort -rn
```

**A named result stated twice has already earned a note.**

> [!remark] Which note owns a two-hypothesis theorem?
> **The one it says the most about — and you find that out by sharpening it until only one hypothesis is
> doing work.** *"A Boolean integral domain is $\mathbb Z/2\mathbb Z$"* sharpens to *"in a Boolean ring every element
> but $0$ and $1$ is a zero divisor"*, which mentions domains not at all — so it belongs to [[Boolean Ring]],
> with a one-line pointer from [[Integral Domain]]. When sharpening does **not** collapse it, the two
> hypotheses genuinely fight, and what you have is a pair of mixins whose conjunction is degenerate.

> [!remark] Axiom or theorem — same layout, different consumption site
> The difference is epistemic, not structural, and it shows in *where the link comes from*: an **axiom** is
> linked from a `## Definition` (you stipulate it), a **theorem** from a `## Property` or `## Security`
> (you derive it). That keeps precision rule 3 — *definition ≠ theorem* — intact while letting both share
> the Scope / Condition / Property skeleton.

---

## 13 · Machine — a computing model

```markdown
Reference:

## Definition

> [!definition] <Name>
> Generalizes:: [[<base machine>]]        ← or Extends:: — run the direction test
>
> ---
> <the full tuple, or the delta: "rule 4 is now $\delta: \dots$">

> [!definition] <Name> (Abstract Machine Formulation)      ← optional
> - Configuration $C$ · $\mathsf{init}(w)$ · $\mathsf{acc}$
> - the step relation $\vdash$

## Property

> [!theorem]
> <equivalence with the base machine>
> ---
> <the simulation cost — this is the content>

## Variant

| variant | $\delta$ | simulation cost |

## Related
```

**Acceptance is existential.** $M$ accepts $w$ iff $\exists c \in \mathsf{acc}$ with $\mathsf{init}(w) \vdash^* c$ — in every model, including the deterministic ones. The collapsed reading ("*the* run ends in $\mathsf{acc}$") is a `[!remark]` under determinism, never the definition; writing it as the definition excludes NFA, PDA and NTM.

**The simulation-cost column is the point.** Equivalence makes the model arbitrary for computability; the cost makes it *not* arbitrary for complexity. A variant table without costs has thrown away its reason to exist.

**Resource bounds do not belong here.** A machine whose definition contains "runs in time polynomial in $|x|$" is a complexity object — see 14 and the protocol remark in 6.

## 14 · Generator — a parameterised class family

```markdown
Reference:

## Definition

> [!definition] Class <NAME>
> A [[Language]] $\mathcal L \in \mathsf{NAME}(f(n))$ if there is a constant $c$ and a
> [[<machine>]] $M$ deciding $\mathcal L$ that <resource bound with $c \cdot f(n)$>.

## Property

> [!theorem] <Name> Hierarchy Theorem
> If $f, g$ are [[Computable Function|<Time/Space>-Constructible]] and <gap condition>, then
> $$\mathsf{NAME}(f(n)) \subsetneq \mathsf{NAME}(g(n))$$

## Related
```

**Three things a generator must name and usually doesn't.**
The **machine** by link — and the right one: space generators take [[Offline Turing Machine]], because charging for the input tape makes $\mathsf{SPACE}(\log n)$ empty.
The **constructibility hypothesis** — without it the hierarchy theorems are false, not merely unproven.
**$\subsetneq$, not $\subseteq$** — a hierarchy theorem written with $\subseteq$ is trivially true and its hypothesis does no work.

## 15 · Complexity class — one named class

```markdown
Reference:

## Definition

> [!definition] Class <NAME>
> Requires:: [[Class <GENERATOR>]]
>
> ---
> $$\mathsf{NAME} = \bigcup_{c} \mathsf{GENERATOR}(n^c)$$

> [!definition] Class <NAME> (machine form)        ← optional unfolding

## Property

### Relation with Other Classes

> [!proposition]
> Requires:: [[Class <other>]]
>
> ---
> <the inclusion or equality, and the theorem that proves it>

## Member

## Related
```

**A class is defined from its generator, never from scratch.** If the definition restates a machine and a bound, it is a generator wearing a class's name.

**`## Member` is a pointer, not a list.** Membership lives on the problem note as `Member of::` / `Complete for::`, so this section is a Dataview query or a handful of links — duplicating it by hand is how `np/` and `np-complete/` came to disagree.

**Uniformity is part of the definition** for circuit classes. $\mathsf{NC}^d$ over a plain [[Circuit Family]] is the *non-uniform* class; $\mathsf{NC}^1 \subseteq \mathsf L$ needs [[Log-Space Uniform Circuit Family]]. Name which one.

---

## Slot glossary

| slot | holds | never holds |
| --- | --- | --- |
| `## Intuition` | the friendly reading, for sharing | anything the skeleton depends on |
| `## Definition` | what you must **stipulate** | consequences |
| `## Syntax` | the tuple, the spaces, one line per algorithm | any bound, any adversary |
| `## Scheme` | Setting, Parameters, Building Blocks, Algorithms | correctness, security |
| `## Property` | what holds **unconditionally** — provable without an adversary | anything with $\mathcal A$ in it |
| `## Security` | games and bounds — what holds **against someone** | attacks |
| `## Cryptanalysis` | concrete attacks, broken parameters, history | definitions |
| `## Variant` | same object, different scope | a different object |
| `## Example` | instances, **and counterexamples** | theory |
| `## Related` | links out | content |

## Callout types

`definition` · `theorem` · `proposition` · `lemma` · `corollary` · `remark` · `example` · `property` · `security` · `scheme` · `algorithm` · `pseudocode` (CLRS-style code) · `construction` · `question` · `conjecture` · `principle` · `proof` · `todo`

Two are styled and unused — start using them: **`[!intuition]`** for the `## Intuition` section, **`[!attack]`** for `## Cryptanalysis`.

## Where the reasoning lives

- [[North Star]] — the five kinds of note, the precision skeleton, two views, class/instance
- [[Foundation Layer]] — the `math/` spine, axiom inventory, note drafts
- [[Cryptography Layer]] — interface/instance, scheme settings, party views, the game properties
