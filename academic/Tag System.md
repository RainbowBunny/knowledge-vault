# Tag System

The vault uses **two layers** of semantic markup. They serve different jobs and shouldn't be collapsed into each other.

| Layer | Lives in | Answers | Cardinality |
|---|---|---|---|
| **Inline callouts** | Body of the note | "What *parts* are in here?" | Many per note |
| **YAML frontmatter `tags`** | Top of the note | "What *is* this note?" | One set per note |

Callouts give content typing (every definition, theorem, scheme is wrapped in a styled block). Frontmatter tags give note typing (queryable via Obsidian's tag pane and Dataview's `file.tags`).

---

## Layer 1 — Inline callouts (`> [!type]`)

All callout names are **lowercase**. Capitalized variants don't get styled — the CSS selectors are case-sensitive. Styles live in `.obsidian/snippets/math-blocks.css` and `pseudocode-callout.css`.

### Mathematical content

> [!definition] callout-name `definition`
> A formal definition. The green border signals "this is the canonical statement."

> [!theorem] `theorem`, `lemma`, `corollary`, `proposition`
> Provable statements, in decreasing prominence. The four share a purple/blue/teal family so they read as one visual gradient.

> [!conjecture] `conjecture`, `axiom`
> Unproven assumptions or accepted starting points. Use sparingly — flag when something is *assumed* rather than proven.

> [!proof] `proof`
> Proof body. CSS automatically appends a QED `□` marker.

### Procedural content

> [!algorithm] `algorithm`
> High-level algorithm description in prose. "BSGS proceeds in two stages…"

> [!pseudocode] `pseudocode`
> Verbatim pseudocode in a monospace block. Styled in `pseudocode-callout.css`.

### Auxiliary

> [!example] `example`
> A concrete instance: "Take $p = 11, g = 2$…"

> [!remark] `remark` · [!question] `question` · [!principle] `principle`
> Sidebar commentary, open problems, guiding ideas.

### Crypto-flavoured (new)

> [!security] `security`
> Security claim or game. "AES-GCM is IND-CCA assuming AES is a PRP and GMAC is a PRF."

> [!construction] `construction`
> "We build X from Y" framing. "Given a PRG $G$, define a PRF $F$ by…"

> [!scheme] `scheme`
> A named scheme spec: RSA-OAEP, Schnorr signature, Kyber. Use when the callout body is the *full algorithm tuple* (key-gen, encrypt, decrypt).

> [!attack] `attack`
> An attack or break against a scheme. CRIME, Bleichenbacher, padding oracle.

> [!intuition] `intuition`
> The informal picture before the formal definition. "Think of a hash as a one-way pipe…"

### Casing

Always lowercase. If you write `[!Definition]` or `[!Theorem]`, the styles will not apply. (A `sed` pass already normalized existing notes.)

---

## Layer 2 — YAML frontmatter `tags`

Every note should ideally start with a frontmatter block. Hierarchical tags work natively (Obsidian renders `area/crypto/sig` as a nested tag in the tag pane, and Dataview can filter by prefix).

```yaml
---
tags:
  - domain/crypto
  - area/crypto/sig
  - kind/scheme
  - status/done
  - source/boneh-shoup
---
```

### Tag namespaces

**`domain/*`** — top-level subject:
`domain/crypto`, `domain/cs`, `domain/math`, `domain/security`, `domain/econ`, `domain/finance`

**`area/*`** — sub-area, hierarchical, mirrors folder layout:

- Crypto: `area/crypto/foundations`, `area/crypto/symmetric`, `area/crypto/mac`, `area/crypto/pke`, `area/crypto/sig`, `area/crypto/kex`, `area/crypto/kem`, `area/crypto/id`, `area/crypto/zk`, `area/crypto/threshold`, `area/crypto/mpc`, `area/crypto/he`, `area/crypto/ecc`, `area/crypto/pq/lattice`, `area/crypto/pq/code`, `area/crypto/assumptions/dlp`, `area/crypto/assumptions/lattice`, `area/crypto/assumptions/idealized`, `area/crypto/cryptanalysis`
- CS: `area/cs/foundations`, `area/cs/data-structures`, `area/cs/algorithms/dp`, `area/cs/algorithms/greedy`, `area/cs/graph`, `area/cs/computability`, `area/cs/complexity`, `area/cs/math`, `area/cs/problems`
- Math: `area/math/algebra`, `area/math/calculus`, `area/math/linear-algebra`, `area/math/number-theory`, `area/math/probability`

**`kind/*`** — what role the note plays:

| Tag | Meaning |
|---|---|
| `kind/moc` | MOC index file (links to others, no original content) |
| `kind/primitive` | Foundational primitive (PRF, hash, MAC) |
| `kind/scheme` | A concrete named scheme (RSA, Kyber, AES) |
| `kind/protocol` | An interactive protocol (Schnorr ID, ZK) |
| `kind/problem` | A hard problem / assumption (DLP, LWE) |
| `kind/attack` | A concrete attack (CRIME, Bleichenbacher) |
| `kind/theory` | Security definitions, models |
| `kind/notes` | Lecture-style scratch, not yet refined |

**`status/*`** — completion stage:

| Tag | Meaning |
|---|---|
| `status/stub` | Placeholder, mostly empty |
| `status/draft` | First pass, may have holes |
| `status/review` | Content present, needs second pass |
| `status/done` | Ready to reference / share |

**`source/*`** — textbook or origin:

`source/boneh-shoup`, `source/silverman`, `source/katz-lindell`, `source/clrs`, `source/sipser`, `source/own`, `source/lecture`, `source/paper`

---

## Examples

### A scheme note (e.g. `digital signatures/Dilithium.md`)

```yaml
---
tags:
  - domain/crypto
  - area/crypto/sig
  - area/crypto/pq/lattice     # cross-area: it's both a signature and PQ
  - kind/scheme
  - status/done
  - source/own
---
```

Body uses `[!definition]` for the math objects, `[!scheme]` for the key-gen/sign/verify triple, `[!theorem]` for the EUF-CMA reduction, `[!security]` for the concrete bound.

### A problem note (e.g. `assumptions/dlp/Discrete Logarithm Problem.md`)

```yaml
---
tags:
  - domain/crypto
  - area/crypto/hardproblem/dlp
  - kind/problem
  - status/done
  - source/boneh-shoup
---
```

Body uses `[!definition]` for the problem statement, `[!theorem]` for hardness results, `[!algorithm]` for solvers (BSGS, Pohlig-Hellman) if they're inlined.

### An MOC

```yaml
---
tags:
  - domain/crypto
  - kind/moc
  - status/done
---
```

---

## Querying

**Tag pane (sidebar):** click a hierarchical tag to filter notes — clicking `area/crypto` shows everything under crypto, clicking `area/crypto/sig` narrows to signatures.

**Dataview** — show every signature scheme:

````markdown
```dataview
TABLE file.tags AS Tags, file.mtime AS "Modified"
FROM #area/crypto/sig
WHERE contains(file.tags, "kind/scheme")
SORT file.name ASC
```
````

**Dataview** — show every theorem in the crypto folder:

````markdown
```dataview
TABLE WITHOUT ID file.link AS Note, length(filter(file.lists, (l) => contains(lower(l.text), "[!theorem]"))) AS Theorems
FROM "academic/knowledge/cryptography"
WHERE contains(file.text, "[!theorem]")
SORT Theorems DESC
```
````

---

## Migration plan

The tagging is opt-in. You don't need to backfill every note before it's useful. A reasonable rollout:

1. Start with MOCs: add `kind/moc` + the appropriate `domain/*` and `status/done`. ~20 files.
2. As you touch any note for refactoring or expansion, add its frontmatter then.
3. After a month or two, run a `grep` audit for notes still missing `tags:` and decide whether to bulk-tag the largest folders.

The callouts are already in place across the vault — the new types (`security`, `construction`, `scheme`, `attack`, `intuition`) just need to be used going forward; existing notes are unchanged.
