# Cryptography Layer — the setting of a scheme, party views, filling plan

*Companion to [[Foundation Layer]] for the crypto side. Everything here is either paste-ready or a precise spec. Provenance tagged. House notation.*

## Status · 2026-09-03

| thing | state |
| --- | --- |
| **slot placement** | **settled 2026-09-03** — real `###` headings under `## Scheme`, one `[!scheme]` callout each ([[Kyber PKE]]). §2.5 |
| **the setting slots themselves** | **four competing forms** — see §2.2 and **V12**. `Parameters`/`Building Block`/`Algorithms` (17) · that plus `Ring and Modulus`/`Dimensions`/`Messages` (2) · `Parameters`/`Statement`/`Scheme` (3) · the HPS bold-label form `Public Parameters`/`Plaintext Space`/`Key Creation (Alice)` (~14) |
| the `## Syntax` / `## Scheme` split | **already real and perfectly disjoint** — 28 notes use one, 22 use the other, **zero use both**. Never written down |
| the full Kyber shape (Scheme + Property + Security) | **4 notes of 40**: [[Kyber PKE]], [[Kyber KEM]], [[Keccak]], and *almost* [[Schnorr Protocol]] / [[Sum-Check Protocol]] |
| party views | one note has it — [[Multi-Party Computation]]. ~14 notes need it |
| legacy `## Encryption Scheme` form | 10 notes, all textbook-derived |

Counts from a full walk of `knowledge/cryptography/` (40 notes carrying a `[!scheme]` callout or a scheme-ish `##` heading): `## Property` 8 · `### Correctness` 5 · `## Security` 9 (4 of which are cryptanalysis prose, not a game) · `[!security]` 5 · `Link:`/`Reference:` 12 · `dg-publish` 15.

---

# Part I · Two levels, and why they get two names

## 1.1 The split you already made

You never wrote this rule, but you have followed it without a single exception:

|                            | `## Syntax`                                            | `## Scheme`                                      |
| -------------------------- | ------------------------------------------------------ | ------------------------------------------------ |
| **declares**               | the tuple of algorithms and the spaces they range over | concrete code for **one** instance of that tuple |
| **callout**                | `[!definition]`                                        | `[!scheme]`                                      |
| **who quantifies over it** | other notes — *"for every PKE scheme…"*                | nobody; it is a leaf                             |
| **proof obligation**       | none — it is a stipulation                             | correctness, **and** a security reduction        |
| **lives in**               | the primitive folder                                   | `schemes/` or `scheme/` under it                 |
| **math analogue**          | the **signature** — the `### Scope` line               | a **model** — `rings/examples/`                  |
| **Lean analogue**          | `class`                                                | `instance`                                       |

**[Vault-local]**, but principled. The reason to keep two words rather than collapsing both to `## Definition` (which is what the math side does) is that they carry *different obligations*. A `## Syntax` block hands other notes names to bind — the moment you write it, `## Security` sections elsewhere can say "for all $\text{PKE}$". A `## Scheme` block hands you code, and code owes you a correctness statement and a reduction. One glance at the heading tells a reader whether they are looking at an interface or an implementation.

> **The honest wrinkle.** `rings/examples/Polynomial Ring.md` is structurally a `## Scheme` — an instance of the `Ring` signature — and it says `## Definition`. That asymmetry is *earned*, not sloppy: a polynomial ring owes you nothing once defined, Kyber owes you a $(1-\delta)$ bound and an MLWE reduction. But it is exactly the kind of thing future-you will "fix" at 1 a.m. One line in [[North Star]] prevents that.

## 1.2 The four levels

```
Level 0   foundations/          Adversary · PPT · Negligible Function · Security Game · Indistinguishability
                                the vocabulary every game below is written in

Level 1   <Primitive>.md        ## Syntax    [!definition]   the interface
                                ## Property  ### Correctness  what ANY instance must satisfy
                                ## Security  ### <Game>       the games, as definitions of advantage

Level 2   schemes/<Name>.md     ## Scheme    [!scheme]        the code
                                ## Property  ### Correctness  THIS instance's concrete bound
                                ## Security  ### <Game>       the reduction

Level 3   assumptions/          MLWE · DDH · SIS · Factoring — where the reduction lands
```

The load-bearing sentence:

> **A Level-2 `## Security` section is a theorem whose *statement* lives at Level 1 and whose *hypothesis* lives at Level 3.**

[[Kyber PKE]] is the only note in the vault that makes this fully visible — its security callout links `[[Public-Key Encryption#Indistinguishability under Chosen-Plaintext Attacks|CPA adversary]]` (Level 1) on the left and `[[Module Learning With Error#Assumption|MLWE adversary]]` (Level 3) on the right, with the advantage inequality between them. That two-link shape is the thing to copy. Copy the links, not just the layout: a security section with no link up and no link down is a floating claim.

This is the same three-part structure as the math side — signature (`properties/` Scope), axioms (`properties/`), models (`structures/`, `examples/`) — with one difference: **the axioms are games instead of equations.** That is exactly the Tier 1 / Tier 3 distinction already in [[North Star]]. Nothing new is being invented here; the crypto side is the third tier of the same architecture.

---

# Part II · Templates, and the setting of a scheme

**§2.2 is the one that answers the question.** The rest is scaffolding around it.

## 2.1 Primitive note — `## Syntax`

```markdown
---
dg-publish: true
---
Reference:
- <primary source>

## Syntax

> [!definition] <Primitive> Scheme
> A **<primitive>** $\Pi = (\text{Alg}_1, \dots, \text{Alg}_k)$ is a tuple of efficient algorithms
> with <spaces: message space $\mathcal M$, key space $\mathcal K$, …>.
> - $out \leftarrow \text{Alg}_1(in)$: <one sentence, what it takes and returns>
> - …

## Property

### Correctness

> [!definition] <Primitive> $(1 - \delta)$-Correctness
> …

## Security

### <Game name>

> [!definition] <Primitive> <Game> Advantage
> $$\mathsf{Adv}^{\text{<game>}}_\Pi(\mathcal A) = \dots$$

## Related
```

Rules for this note:
- **Every algorithm gets an arrow line.** `$out \leftarrow \text{Alg}(in)$` then a colon then one sentence. [[Public-Key Encryption]] and [[Multi-Party Computation]] both do this; copy either.
- **The syntax block declares nothing you cannot type-check.** Spaces before algorithms; no algorithm mentions a space that has not been named.
- **`## Security` here holds *definitions of advantage*, not bounds.** A number belongs at Level 2.

## 2.2 The setting of a scheme

This is the part worth being careful about. Before a scheme's algorithms mean anything you have to say what world they run in — and the vault currently says it four different ways.

### What is actually in use

| family | slots | count |
| --- | --- | --- |
| **A · modern** (your Kyber form) | `Parameters` / `Building Block` / `Algorithms` | 17 notes |
| **A′ · modern, extended** | `Parameters` / **`Ring and Modulus`** / **`Dimensions`** / **`Messages`** / `Building Block` / `Algorithms` | [[Module HGSW]], [[Private Re-randomization of MLWE Samples]] |
| **B · proof protocol** | `Parameters` / **`Statement`** / `Scheme` | [[Schnorr Protocol]], [[Sum-Check Protocol]], [[Kilian Interactive Argument of Knowledge from PCP]] |
| **C · textbook (HPS)** | **`Public Parameters`** / **`Plaintext Space`** / `Ciphertext Space` / `Key Space` / `Output` / **`Key Creation (Alice)`** / `Encryption (Bob)` / `Decryption (Alice)` — as bold labels, not headings | ~14 notes |
| **D · not a scheme at all** | `Experiment $b$`, or `Input` / `Output` | games and plain algorithms, correctly a different thing |

Raw counts: `### Parameters` 25 · `### Building Block` 26 vs `### Building Blocks` 4 · `### Algorithms` 30 vs `### Algorithm` 4 · `### Statement` 3 · `### Scheme` 3.

Families A′ and C are not noise — they are you noticing that `Parameters` was doing too much and splitting it. A′ split off the algebraic ambient (`Ring and Modulus`) and the spaces (`Messages`); C split off the spaces (`Plaintext Space`…) and the parties (`(Alice)`, `(Bob)`, `(Samantha)`, `(Victor)`). Both splits are right. They just used different words for the same two ideas.

### The categorization

Six slots. The rule that makes them non-arbitrary is that **each one points somewhere different** — so "which slot?" is answered by "where does this thing come from?", not by taste.

| slot | answers | points | example |
| --- | --- | --- | --- |
| **Parameters** | what you *choose* at setup | **nowhere** — knobs, no note owns them | $q$, $n$, $k$, $\eta$, $d_u$, $\lambda$ |
| **Setting** | what mathematical object the scheme lives *in* | **down**, into `math/` | $R_q = \mathbb Z_q[x]/(x^n + 1)$; a group $\mathbb G$ of prime order $p$; a pairing $e : \mathbb G_1 \times \mathbb G_2 \to \mathbb G_T$ |
| **Spaces** | the carriers the algorithms range over | **up**, into the primitive's `## Syntax` | $\mathcal M, \mathcal C, \mathcal K, \mathcal R$ |
| **Distribution** | where randomness is drawn from | **down**, into `math/probability/` | $\beta_\eta$, $D_{\mathbb Z, \sigma}$, uniform on $R_q^k$ |
| **Building Block** | which *other cryptographic* object it calls | **sideways**, into another crypto note | an XOF, a hash, a PRG, a KEM, a commitment |
| **Parties** | who runs which algorithm, and who talks to whom | **into the view remark** (§3) | $\mathcal P / \mathcal V$; $P_1, \dots, P_n$ and a dealer $D$; Alice / Bob |

Then `Algorithms` — the code — and, for proof systems, `Statement` — the relation $\mathcal R$ or language $\mathcal L$, which points into `relations/`.

Two consequences worth stating plainly:

- **`Setting` is the crypto version of the math side's `### Scope` line.** It is the *same slot*: name every carrier and every operation the definition below is allowed to mention. A scheme whose algorithms use $R_q$ without a Setting line has an unbound symbol, exactly like a Scope line that forgets to declare its set. That is precision rule 1 applied to crypto, and it is the argument for splitting `Setting` out of `Parameters` even though it costs a line.
- **`Parties` is the setting half of the view.** The setting says *who exists*; the [!remark] View says *what each one ends up able to compute*. That is why these two questions arrived together — they are the same question asked before and after the protocol runs.

### Write only the slots that do work

Six slots is a menu, not a checklist. Omit any slot that is empty or inherited:

- **Spaces** is usually inherited from the primitive's `## Syntax` — write it only when this scheme narrows it ($\mathcal M = \{0,1\}^{256}$ where the interface said $\mathcal M$).
- **Setting** is empty for a scheme over bit strings. [[Keccak]] does not need one; [[Kyber PKE]] does.
- **Parties** is empty for a non-interactive primitive. Encryption schemes skip it.
- **Distribution** folds into Setting when there is one, obvious, uniform distribution.

The minimum is `Parameters` + `Algorithms`. Everything else appears when it has content.

### The one fix this makes visible

[[Kyber PKE]]'s `### Building Block` currently holds three things:

```
- Sam                       ← an extendable output function: a crypto primitive.  Building Block. ✓
- Compress_q(x, d)          ← a rounding map Z_q → {0..2^d-1}: pure arithmetic.   Setting.
- Decompress_q(x, d)        ← its partial inverse.                                Setting.
```

`Sam` points sideways at [[Extendable Output Function]] (which is a broken link today, `x2`). `Compress`/`Decompress` point nowhere — they are defined inline, used by [[Kyber KEM]] and [[Dilithium]] too, and are the kind of thing that graduates to its own note the moment a second note needs it (which has already happened). Under this taxonomy that is visible at a glance rather than being a judgement call.

Same pattern in [[Module HGSW]] and [[Private Re-randomization of MLWE Samples]]: their `Ring and Modulus` and `Dimensions` rows are `Setting` and `Parameters` respectively, already correctly separated, just named locally.

### Naming, to settle now

`Algorithms` plural (30 vs 4) · `Setting`, `Spaces`, `Distribution`, `Parties`, `Statement`.

`Building Block` vs `Building Blocks` needs your word: the vault leans singular 26–4, but your new [[Kyber PKE]] uses **plural**, and plural is the better reading now that the block is a list of external references. I would take plural and rename the 26 — but it is one word, and the model note wins ties. Either way it is a **K2** pass.

## 2.3 Scheme note — the template

```markdown
---
dg-publish: true
---
Reference: <paper url>

## Scheme

> [!scheme] <Name>
> Reference Name: $\text{<Name>}$
> Instantiates: [[<Primitive>#Syntax|<Primitive>]]
>
> ---
> ### Parameters
> - $q$: <what it is>
>
> ---
> ### Setting
> - $R_q = \mathbb Z_q[x]/(x^n+1)$ — a [[Quotient Ring]] of the [[Polynomial Ring]] over [[Integers Modulo n]]
>
> ---
> ### Building Block
> - $\text{Sam}$: [[Extendable Output Function]]
>
> ---
> ### Algorithms
> - $(pk, sk) \leftarrow \text{Gen}()$:
> 	1. …

> [!remark] View        ← only for interactive / multi-party schemes; see §3
> …

## Property
### Correctness

## Security
### <Game name>

## Cryptanalysis        ← optional; attacks, not games

## Related
```

## 2.4 The outer slot table

| slot | holds | never holds |
| --- | --- | --- |
| `## Syntax` | the tuple, the spaces, one line per algorithm | any bound, any adversary |
| `## Scheme` | Reference Name, Instantiates, Parameters, Building Block, Algorithms | correctness, security |
| `## Property` | correctness, complexity, homomorphism, rigidity — things provable **without** an adversary | anything with $\mathcal A$ in it |
| `## Security` | games and advantage bounds — things stated **with** an adversary | attacks |
| `## Cryptanalysis` | concrete attacks, broken parameter choices, history | definitions |
| `## Related` | links out | content |

The `## Property` / `## Security` line is the same line as the math side's Definition / Property line: **`## Property` is what holds unconditionally, `## Security` is what holds against someone.** If a statement has $\mathcal A$ in it, it is Security. Correctness of Kyber is a Property even though it is probabilistic, because the probability is over the scheme's own randomness, not over an adversary's choices.

## 2.5 Worked example — [[Kyber PKE]] after the split

Your 2026-09-03 restructure lifted the slots out of the callout into real `###` headings, each wrapping its own `[!scheme]`. That answers **V11** by making it moot: the headings are now real, so they fold, they show in the outline, and `[[Kyber PKE#Algorithms]]` resolves. Three consequences follow.

### One new block, not four

The six slots in §2.2 are a menu. **A slot earns its own block at two bullets; below that it folds into its nearest neighbour** — `Distribution` into `Setting`, `Spaces` into `Setting`. Kyber needs exactly one new block, and the reason to add it is not tidiness:

The note currently uses $R_q$, $\mathbb Z_q$, $\mathcal M$, $\bmod^{\pm} q$ and $\|\cdot\|_\infty$ — **five symbols it never declares.** `### Parameters` declares $\eta, \beta_\eta, k, d_t, d_u, d_v$ and stops. That is precision rule 1 (Scope lines type-check) failing in a crypto note, and it is invisible until you try to write the Setting block and find you cannot say what $k$ is the rank *of*.

**`Setting` goes first**, before `Parameters`, because a parameter's description forward-references it: "$k$: module rank, the dimension of vectors and matrices over $R_q$" names $R_q$ before anything introduces it.

```markdown
### Setting

> [!scheme] Setting
> - $n$, $q$: degree and modulus. $R = \mathbb Z[x]/(x^n + 1)$ and $R_q = \mathbb Z_q[x]/(x^n + 1)$ — a
>   quotient of the [[Polynomial Ring]] over $\mathbb Z_q$; every vector and matrix below lives over $R_q$.
> - $x \bmod^{\pm} q$: the representative of $x$ in $(-\tfrac q2, \tfrac q2]$.
> - $\|\cdot\|_\infty$: on $R_q$, the largest $|\cdot \bmod^{\pm} q|$ over coefficients.
> - $\mathcal M = \{0,1\}^n$, identified with $R_2$ — narrows [[Public-Key Encryption]]'s $\mathcal M$.
> - $\text{Compress}_q(x, d)$: $\lceil (2^d/q)\, x \rfloor \bmod 2^d$, an element of $\{0, \dots, 2^d - 1\}$.
> - $\text{Decompress}_q(x, d)$: $\lceil (q/2^d)\, x \rfloor$, satisfying $|x' - x \bmod^{\pm} q| \leq \lceil \tfrac{q}{2^{d+1}} \rfloor$.
```

### Building Blocks as links only

Making that block **external references only** is the right target, and it turns into a checkable invariant: *every bullet in `Building Blocks` is a wikilink.* A reader sees the dependency graph at a glance; the linter can enforce it.

For Kyber the move is small — $\text{Compress}_q$ and $\text{Decompress}_q$ go to `Setting`, above. They are not cryptographic building blocks; they are rounding maps on $\mathbb Z_q$, ambient arithmetic in the same sense as $\bmod^{\pm}$. What is left is one line:

```markdown
### Building Blocks

> [!scheme] Building Blocks
> - $\text{Sam}$: [[Extendable Output Function]], expanding a seed to a uniform element of the target space.
```

That link is **broken today** ([[Keccak]] points at it too, ×2) — so purifying the block immediately surfaces a real missing note.

Writing the `Setting` block surfaces a second one. `Ring.md` has a `### Quotient rings` heading but there is no `Quotient Ring` note, so $R_q = \mathbb Z_q[x]/(x^n+1)$ has nothing to link for the construction it is built by — precision rule 5, a dependency a definition uses but cannot link. Two missing notes found by writing four lines of setting: that is the whole argument for the block.

> **Correction to what I said last turn.** I claimed $\text{Compress}_q$ / $\text{Decompress}_q$ were already used by [[Kyber KEM]] and [[Dilithium]], and that they had therefore earned their own note. They have not — `Compress` appears in exactly one scheme note, this one. Dilithium uses a different rounding family (`Power2Round`, `Decompose`, `HighBits`). So: keep them inline in `Setting` now; when Dilithium's rounding lands you will have two consumers and a `Modular Rounding` note in `math/` earns itself, with `Setting` linking out to it. That is the graduation rule working as intended, and it says *not yet*.

### Do not split `Algorithms` per algorithm

$(\text{Gen}, \text{Enc}, \text{Dec})$ is **one object** — the tuple the `## Syntax` note quantifies over. Three callouts of five lines each cost six title lines for fifteen lines of content, and they make it harder to read the tuple as a tuple or to diff Kyber against [[Lyubashevsky-Peikert-Regev Public Key Encryption]].

Split on **structure**, not on cardinality:

| split when | example |
| --- | --- |
| the protocol has **phases** | [[Secure Multi-party Computation]] — Pre-processing / Input / Evaluation / Output. A genuine division: different parties are active in each |
| **one algorithm** needs its own sub-steps or its own remark | Dilithium's `Sign` with rejection sampling |
| a **variant** replaces only part of the tuple | [[Kyber KEM]] = this scheme + FO — only `Encaps`/`Decaps` differ |

Otherwise: one `Algorithms` block per tuple.

### Two small things in the note itself

- **The reference name is spelled three ways**: `Reference Name: $\mathsf{Kyber.PKE}$`, then `$\text{Kyber.PKE}$` in the correctness callout, then bare `Kyber.PKE` inside `\text{Adv}_{Kyber.PKE}^{\text{cpa}}` — where it renders italic, as a product of variables. Pick $\mathsf{Kyber.PKE}$ everywhere. While there: [[Security Game]] writes the advantage as $\mathsf{Adv}$, this note writes $\text{Adv}$.
- **`Reference Name:`** now floats as bare prose between `## Scheme` and `### Parameters`, with two blank lines around it. It is the one untidy spot left. Either move it into the `Setting` callout as the first bullet, or keep a short `> [!scheme] Identity` block with `Reference Name` and `Instantiates`.

### What the change costs, and the fix

`[!scheme]` used to mean *one scheme* — 38 callouts, 38 schemes. Under this format Kyber alone has four, so any count or Dataview query over `[!scheme]` degrades as the format spreads.

The fix is free, because you already made it: **the `## Scheme` heading is now the countable unit, and the callout is presentation.** Say that once and nothing is lost. (Differentiating the callout types — `[!definition]` for Setting and Parameters, `[!scheme]` only for Algorithms — would also work, but three identically-styled boxes read as one visual band, which is the accessibility property you said you wanted. Not worth trading away for a count you can get from the heading.)

## 2.6 Building Blocks at the interface level

Yes — a `## Syntax` note can have `Building Blocks`, and [[Fujisaki-Okamoto Transformation]] already does: `PKE`, `SKE`, $G$, $H$. That is not an exception to the rule; **it is the signal that tells you what kind of note you are reading.** Same slot name at both levels, different quantifier, different invariant.

| | `## Scheme` — instance | `## Syntax` — interface |
| --- | --- | --- |
| holds | the components this scheme **picks** | the components the construction is **parameterized by** |
| quantifier | fixed — $\text{Sam} = $ SHAKE-128 | **universal** — "for any [[Public-Key Encryption]] scheme, any hash $H$" |
| bullets look like | a name and a wikilink | a name, a type, and a hypothesis waiting to happen |
| **invariant** | every bullet is a **wikilink** | every bullet **reappears in `## Security` carrying a hypothesis** |

The second invariant is the one that earns its keep. Building Blocks at the interface level are *exactly* the things that show up as hypotheses in the security theorem — the block doubles as a checklist for it. [[Fujisaki-Okamoto Transformation]]'s theorem has to read "if `PKE` is OW-CPA and $G, H$ are modelled as random oracles, then $\text{FO}(\text{PKE}, \text{SKE})$ is IND-CCA": four blocks, four hypotheses. **The note today has four blocks and no `## Property` or `## Security` section at all** — it stops after Algorithms. The invariant catches that in one glance, which is the argument for stating it. Filed as **V13**.

### Three kinds of `## Syntax` note

Told apart by what is in Building Blocks:

| kind | Building Blocks | examples |
| --- | --- | --- |
| **plain primitive** | none — defined from spaces and algorithms alone | [[Public-Key Encryption]], [[Key Encapsulation Mechanism]], [[Commitment Scheme]], [[Digital Signature]], [[Sigma Protocols]] |
| **transform** | generic, universally quantified other primitives | [[Fujisaki-Okamoto Transformation]], [[Fiat-Shamir Transform]], [[From Collision Resistance]], [[Kilian Interactive Argument of Knowledge from PCP]] |
| **refinement** | none — it *extends* another interface | [[Puncturable Pseudorandom Function]] over a PRF, [[Argument Systems]] = [[Interactive Proof Systems]] with computational [[Soundness]], threshold signatures over signatures |

Refinements want an **`Extends:`** line, the same shape as `Instantiates:` — not a Building Blocks entry. The distinction is real: a transform *calls* its input as a subroutine; a refinement *is* its input with a condition added. [[Argument Systems]] does not call an interactive proof, it is one.

### Transforms are not bridges

[[North Star]] lists [[Fiat-Shamir Transform]] as an example of a **Bridge**. On reflection that is a miscategorisation worth fixing, because the two behave differently:

- A **bridge** says *these two are the same thing seen differently*. [[R1CS to QAP Reduction]], [[Statistical Distance]] ↔ [[Indistinguishability]]. Lossless, and it reads in both directions.
- A **transform** says *give me an $X$ and I will build you a $Y$*. Different object, one direction, and it **costs something**: Fiat-Shamir loses a factor $(Q_{ro} + 1)$ in soundness; FO loses in the CPA → CCA step.

**The tell is the loss factor.** If the theorem has a multiplicative constant in it, it is a transform. If it is an "if and only if", it is a bridge. A transform is a fifth kind of note, or Bridge splits into *translation* and *construction* — either way [[Fiat-Shamir Transform]] and [[Fujisaki-Okamoto Transformation]] belong together, and neither is [[R1CS to QAP Reduction]].

Where does a transform live? Not in the input's folder and not in the output's, strictly — but file it under the **output**, since that is what a reader is looking for when they need one. By that rule [[Fujisaki-Okamoto Transformation]] under `public-key encryption/` is arguable at best; it produces the CCA-secure object that [[Kyber KEM]] is built from.

### Where this bites already

[[Public-Key Encryption]] is 17 KB and contains, past its `## Syntax`: `## Construction / ### Based on a Trapdoor Function Scheme` (a transform: TDF + symmetric cipher + hash → PKE), then `## Case Study` with RSA and ElGamal (two more transforms, each with its own theorem and loss factor), then a lattice instantiation. That is one interface note carrying **three transforms and a scheme**. It is [[RSA Public Key Cryptosystem]]'s problem (**V4**) in the other direction — there, schemes hide inside schemes; here, transforms hide inside the interface.

---

# Part III · The view of a party

## 3.1 What it is — **[Standard]**

The **view** of a party in a protocol execution is everything that party could possibly compute from: its own input, its own coins, and every message it received.

$$\mathsf{View}_i^{\Pi}(x_1, \dots, x_n) = \bigl(x_i,\ r_i,\ m_i^{(1)}, \dots, m_i^{(\rho)}\bigr)$$

This is exactly what you wrote in [[Multi-Party Computation]], and it is verbatim the standard definition.

Reference:
- Goldreich, *Foundations of Cryptography* Vol. 2, §7.2.1 — the definition of a party's view and of semi-honest security.
- Lindell, *How To Simulate It* (https://eprint.iacr.org/2016/046) — the tutorial treatment; §2 is the view/simulator definition.
- Goldwasser–Micali–Rackoff 1985 — where $\mathsf{View}_{\mathcal V}$ enters zero knowledge.

## 3.2 Why it is not decoration

[[Secure Multi-party Computation]] opens with

> [!definition] Privacy
> No party learns anything about any other party's inputs (except for information that is inherently revealed by the outputs)

That sentence is not yet a definition — "learns" is not a predicate. The view is what makes it one. Writing $I \subseteq [n]$ for the corrupted set:

$$\exists\, \mathcal S \text{ efficient}: \quad \mathcal S\bigl(\{x_i\}_{i \in I},\ \{y_i\}_{i \in I}\bigr) \ \approx\ \mathsf{View}_I^{\Pi}(x_1, \dots, x_n)$$

Read it as: *whatever the corrupt parties saw, they could have made up from their own inputs and outputs alone.* The parenthetical "except for information that is inherently revealed by the outputs" is precisely the $\{y_i\}_{i \in I}$ argument to $\mathcal S$.

So the view remark is the **bridge note between the informal privacy bullet and the game**, in exactly the sense of the vault's two-views convention: same content, two idioms, and the bridge is where the translation is stated. It also unifies three notions the vault currently states three different ways —

| notion | what is simulatable | note |
| --- | --- | --- |
| **semi-honest MPC privacy** | $\mathsf{View}_I$ from $(x_I, y_I)$ | [[Secure Multi-party Computation]] |
| **zero knowledge** | $\mathsf{View}_{\mathcal V}$ from $x$ | [[Interactive Proof Systems]], [[Zero Knowledge]] |
| **garbling obliviousness** | $(F, X)$ from $f$ | [[Secure Multi-party Computation]] |

All three say *this view is simulatable from strictly less*. One remark shape covers all three, and that is a real unification, not a formatting choice.

## 3.3 The house remark — two shapes

**Shape A — the tuple.** For a two-party or fixed-round protocol, one line under `## Syntax`:

```markdown
> [!remark] View
> $\mathsf{View}_{\mathcal V} = (x, r_{\mathcal V}, a_1, \dots, a_k)$ — the statement, the verifier's coins, and the prover's messages.
> [[Zero Knowledge]] is the claim that this tuple is simulatable from $x$ alone.
```

**Shape B — the table.** When parties are asymmetric, or when the note goes on to describe phases, a three-column table earns its space:

```markdown
> [!remark] Views
>
> | party | holds | sees | learns |
> | --- | --- | --- | --- |
> | $P_1$ | $x_1, r_1$, shares $x_{11}, \dots$ | $\delta$, opened $u, v$ | $y$ |
> | $P_2$ | $x_2, r_2$, shares $x_{12}, \dots$ | $\delta$, opened $u, v$ | $y$ |
> | $D$ | the triples it generated | nothing | nothing |
>
> $\mathsf{View}_{P_1}$ must be simulatable from $(x_1, y)$ — that is the privacy claim.
```

**holds** = private input and coins. **sees** = messages received. **learns** = output. The final line is not optional: it names which security notion quantifies over this view. A view table with no such line is furniture.

**[Vault-local]** as a *format*; **[Standard]** as *content*. The three-column split is mine; the tuple, the simulator, and the quantifier are all textbook.

## 3.4 When **not** to write one — the part that keeps this honest

A view remark earns its place only when the note's security section is stated **in terms of the view**. Concretely, write one when the note has, or will have, a simulator, an obliviousness claim, or a privacy claim.

Do **not** write one when:

- **The only security notion is a search game about the output.** [[Soundness]] and [[Knowledge Soundness]] quantify over what the adversary *produces*, not what it *saw*. A view table above a soundness section adds a paragraph and clarifies nothing.
- **There is one party.** Encryption schemes, hash functions, PRGs — the "view" is the adversary's oracle transcript, which the game already spells out. [[Kyber PKE]] does not need one.
- **You would be restating the syntax.** If `## Syntax` already lists what each algorithm takes, and the protocol is one round, the view is the syntax read sideways. Skip it.

That leaves roughly fourteen notes, listed in Part IV as **V7**. If it starts appearing on encryption schemes, the convention has become a tic and should be pruned back.

---

# Part IV · Audit

Findings are ordered by how much they cost to fix, cheapest first. IDs are stable; [[Vault Refactoring Plan]] references them.

## V1 · Ten notes still use the legacy `## Encryption Scheme` / `## Signature Scheme` heading

[[RSA Public Key Cryptosystem]] · [[ElGamal Public Key Cryptosystem]] · [[NTRU Public Key Cryptosystem]] · [[GGH Public Key Cryptosystem]] · [[Massey-Omura Three-Pass Cryptosystem]] · [[Merkle–Hellman Subset-Sum Cryptosystem]] · [[Goldwasser–Micali Cryptosystem]] · [[A Congruential Public Key Cryptosystem]] · [[ID-based Public Key Cryptosystems]] · [[Digital Signature Algorithm]]

All ten also use `[!algorithm]` where the house callout is `[!scheme]`. Rename the heading to `## Scheme` and the callout to `[!scheme]`; that part is mechanical and I can do it in one pass if you want. **What is not mechanical is V4 and V5 below, and those are the real content.**

## V2 · Nine `[!scheme]` callouts sit under a non-standard heading

| note | current | should be |
| --- | --- | --- |
| [[Affine Cipher]], [[Hill Cipher]], [[Multiplicative Encryption]], [[One-time Pad]], [[Substitution Cipher]] | `# <Title>` h1, callout directly under it | drop the h1 (the filename is the title), add `## Scheme` |
| [[Additive-Homomorphic Encryption]], [[Hamming Quasi Cyclic SKE]] | `## Syntax` | `## Scheme` — these are instances, not interfaces |
| [[LUNA]] | `### Scheme` as an orphan h3 | `## Scheme` |
| [[Private Re-randomization of MLWE Samples]] | no heading at all | `## Scheme` |

The h1 titles are worth removing generally — they duplicate the filename and the linter's `title` check counts them.

## V3 · Only 4 notes of 40 carry the full shape

`## Property` 8 · `### Correctness` 5 · `[!security]` 5. So thirty-odd scheme notes assert code with **no correctness statement and no security claim at all**.

This is the finding I would act on before any renaming. A scheme note without a correctness line is not a smaller version of [[Kyber PKE]] — it is a different kind of object, a *recipe*. Deciding which of the 40 are meant to become spec notes and which are meant to stay recipes is a judgement only you can make, and it determines how much of V1 is even worth doing.

## V4 · Four notes carry two or three primitives at once

| note | also contains |
| --- | --- |
| [[RSA Public Key Cryptosystem]] | `## Digital Signatures Scheme`, `## 1-2 Oblivious Transfer`, `## Matrix Extension of RSA` |
| [[ElGamal Public Key Cryptosystem]] | `## Digital Signature Scheme`, `## Elliptic Version`, `## Menezes-Vanstone variant` |
| [[NTRU Public Key Cryptosystem]] | `## Digital Signature Scheme`, `## NTRU as a lattice cryptosystem` |
| [[GGH Public Key Cryptosystem]] | `## Signature Scheme` |

By the vault's own rule — one note, one object — `RSA Signature`, `ElGamal Signature`, `NTRU Signature` and `GGH Signature` are four notes under `digital signatures/schemes/`, each with its own `Instantiates: [[Digital Signature]]`. Right now [[Digital Signature]] is a 240-byte stub with no instances linked, while four signature schemes hide inside encryption notes. This is the single largest structural distortion on the crypto side.

The *variants* are a different call. `## Elliptic Version` of ElGamal is genuinely the same scheme over a different group — that is a `## Variant` section, not a new note, and the same judgement you already made for [[Function]]'s partial-function variant.

## V5 · Attacks have no home

Ten places invent a heading for cryptanalysis: `## Man in the Middle Attack on ElGamal`, `### Multiple Exponent Attack`, `### RSA Oracle`, `## Security of RSA`, `## Cryptanalysis` (Congruential), `## Transcript Attack`, and the four classical ciphers whose `## Security` section is prose about frequency analysis rather than a game.

Adopt `## Cryptanalysis` as the standard slot and the classical ciphers stop lying: what they have is not a security section, it is a break. There is already a `cryptanalysis/` folder for attacks big enough to be their own note.

## V6 · Stubs on the scheme side

[[Identical Partly Secret Sharing]] 11 B · [[Alekhnovich Encryption Scheme]] 36 B · [[Merkle Tree]] 40 B · [[Multi-Party Computation-in-the-Head]] 65 B · [[Groth16]] 98 B · [[From Collision Resistance]] 132 B · [[Lyubashevsky-Peikert-Regev Public Key Encryption]] 248 B · [[Lindner-Peikert Public Key Encryption]] 1060 B but no `[!scheme]` callout at all — it is a `[!question]` and a `[!remark]`.

[[Merkle Tree]] at 40 bytes is the one that surprises me; it is load-bearing for [[Kilian Interactive Argument of Knowledge from PCP]].

## V7 · Party views to add — ~16 notes

Shape B (table) — more than two parties or explicit phases:
[[Secure Multi-party Computation]] (per protocol: Beaver, garbling, 3-party) · [[Multi-Party Computation-in-the-Head]] · [[Multi-Prover Interactive Proofs]] · [[Linear Multi-Prover Interactive Proofs]] · [[Split Prover]] · [[Oblivious Transfer]]

Shape A (tuple) — two parties:
[[Interactive Proof Systems]] · [[Sigma Protocols]] · [[Schnorr Protocol]] · [[Sum-Check Protocol]] · [[Kilian Interactive Argument of Knowledge from PCP]] · [[Identification Protocol]] · [[Schnorr Identification]] · [[Security of Identification]] · [[Commitment Scheme]] · [[Private Information Retrieval]]

[[Interactive Proof Systems]] already writes $\text{View}_{\hat{\mathcal V}}(\mathcal P(x), \hat{\mathcal V}(x))$ inside its zero-knowledge definition without ever defining $\mathsf{View}$. That note is the one to do first — it turns an undefined symbol into a link.

Notation: standardise on $\mathsf{View}$ (upright sans, matching $\mathsf{Adv}$, $\mathsf{Next}_i$, $\mathsf{Out}_i$). [[Interactive Proof Systems]] currently uses `\text{View}`.

## V8 · [[Dilithium]] stops after the scheme

`## Scheme` + `[!scheme]`, then two bare `[!lemma]` callouts with no `## Property` or `## Security` heading over them. It is one heading away from the full shape.

## V9 · [[Old Digital Signature]] is 20 KB, [[Digital Signature]] is 240 B

The interface note is a stub while a legacy note holds the entire security model — unforgeability, EUF-CMA, $q$-time signatures, strong security, message-space extension. Everything in `Old Digital Signature`'s `## Security Model` belongs in [[Digital Signature]]'s `## Security`. This is the same split you already did for `Function between Sets` → [[Function]].

## V10 · Source lines and frontmatter

12 of 40 scheme notes carry `Link:` or `Reference:`; 15 of 40 carry `dg-publish`. Two spellings for the same slot. Pick one — I suggest `Reference:` everywhere (it is what the math side uses and what [[Security Game]] uses), with `Link:` retired.

## V11 · Headings inside callouts — **resolved by you, 2026-09-03**

**Settled: lift them out.** [[Kyber PKE]] now has real `###` headings under `## Scheme`, each wrapping its own `[!scheme]` callout — so they fold, they appear in the outline, and `[[Kyber PKE#Algorithms]]` resolves. That is the house form; §2.5 works it through. The 32 other notes convert in **K2b**.

*Original question, kept for the record — the three things that made the in-callout form doubtful:*

1. Do they appear in the **outline** pane?
2. Does `[[Kyber PKE#Algorithms]]` resolve?
3. Do they fold?

One consequence to record: `[!scheme]` no longer means *one scheme* — Kyber has four. **The `## Scheme` heading is the countable unit now; the callout is presentation.**

Sub-format drift to settle at the same time: `### Building Block` (Kyber) vs `### Building Blocks:` (MPC `Garble0`) vs `**Key generation.**` bold labels (the classical ciphers). Three formats for one slot.

## V12 · The setting slots drift four ways

Full breakdown in §2.2. The short version: `Parameters` is carrying three different jobs — the knobs you choose, the algebraic object you work in, and the carriers the algorithms range over — and two notes have already split it apart under local names (`Ring and Modulus`, `Dimensions`, `Messages`), while the fourteen textbook notes split it a different way (`Public Parameters`, `Plaintext Space`, `Key Space`) using bold labels instead of headings.

Proposed slots, chosen so that each one points somewhere different: **Parameters** (points nowhere) · **Setting** (down, into `math/`) · **Spaces** (up, into the primitive) · **Distribution** (down, into `math/probability/`) · **Building Block** (sideways, into another crypto note) · **Parties** (into the view remark) · **Statement** (into `relations/`) · **Algorithms**.

Naming stragglers to fix: `Building Blocks` → `Building Block` (4 notes) · `Algorithm` → `Algorithms` (4 notes).

Concrete instance: [[Kyber PKE]]'s `Building Block` mixes $\text{Sam}$ (an XOF — a genuine building block, and a broken link today) with $\text{Compress}_q$ / $\text{Decompress}_q$ (pure arithmetic — `Setting`, and used by [[Kyber KEM]] and [[Dilithium]] too, so they have already earned their own note).

## V13 · [[Fujisaki-Okamoto Transformation]] has four Building Blocks and no security section

It stops after `### Algorithms`. No `## Property`, no `## Security` — so the whole point of FO, that it lifts CPA security to CCA security, is nowhere in the note. See §2.6: at the interface level every Building Block owes a hypothesis. Four blocks (`PKE`, `SKE`, $G$, $H$), zero hypotheses.

Same shape, smaller: [[From Collision Resistance]] is 132 B — one Building Block, no algorithms, no security.

---

# Part V · Filling plan

Six batches. K1 and K2 are mine to run if you want them; the rest are yours because they need judgement about content.

| batch | work | est | who |
| --- | --- | --- | --- |
| **K1** | Write the convention down: this file + the [[North Star]] section + the plan entries. **Done** | — | me |
| **K2** | Mechanical: **V12** `Building Blocks` → `Building Block` (4) and `Algorithm` → `Algorithms` (4) · **V1** heading + callout rename (10) · **V2** heading fixes (9) · **V10** `Link:` → `Reference:`. No content touched | 15 min | me, on your word |
| **K2b** | **Split the setting slots (V12).** Judgement per note: which `Parameters` bullets are knobs, which are `Setting`, which are `Spaces`. Start with [[Kyber PKE]] (three bullets move), then the two A′ notes (already split, only renamed), then the rest as you touch them | 20 min + lazy | you |
| **K3** | **Decide V3**: walk the 40 scheme notes and mark each *spec* or *recipe*. Only spec notes owe a `## Property` / `## Security`. This gates everything after it | 30 min | you |
| **K4** | Party views. Start with [[Interactive Proof Systems]] (defines a symbol it already uses), then [[Secure Multi-party Computation]], then the rest of V7 lazily | 20 min + lazy | you |
| **K5** | V4 — extract `RSA Signature`, `ElGamal Signature`, `NTRU Signature`, `GGH Signature` into `digital signatures/schemes/`; give [[Digital Signature]] its instance list. Then V9, folding `Old Digital Signature`'s security model into [[Digital Signature]] | 1–2 h | you |
| **K6** | V5 `## Cryptanalysis` slot · V6 stubs · V8 Dilithium headings · add `Instantiates:` lines | lazy | you |

Checkpoint after K3: every note in `schemes/` is either marked a recipe or has both a correctness line and a security line with a link up to its primitive and a link down to an assumption.

---

# Part VI · Where I think this is too ideal

**Uniformity is not the goal; comparability is.** You asked to unify the scheme syntax "like Kyber PKE", and the risk is reading that as *make all forty notes look like Kyber*. [[RSA Public Key Cryptosystem]] and [[ElGamal Public Key Cryptosystem]] are Hoffstein–Pipher–Silverman pedagogy — a scheme, an attack on it, a variant, a signature spin-off, in narrative order. Forcing `### Parameters / ### Building Block / ### Algorithms` onto that fights the source and loses the narrative that makes those notes useful to re-read. The thing actually worth having is that you can put two scheme notes side by side and diff them: same slot names, same order, same callout types. A recipe note with `## Scheme` and `## Cryptanalysis` and nothing else is *already comparable*. It does not need `### Parameters` with one bullet in it.

**The `Instantiates:` line is a small bet.** I am proposing it because nothing currently links a scheme up to its interface, and that is a real hole — but it is a second place to keep a fact that a Dataview query over the folder structure could compute for free. If you find yourself forgetting to write it, delete the convention rather than half-applying it; a field that is right 60% of the time is worse than no field.

**Party views will rot into boilerplate if you let them.** §3.4 lists where not to write one, and I would rather you under-apply it. The test is whether the last line of the remark — *"this view must be simulatable from X"* — says something the security section does not already say in the next paragraph. If it does not, the table is furniture.

**K5 is bigger than it looks.** Splitting four signature schemes out of four encryption notes means re-deriving which parts of the shared setup ($N = pq$, the group, the hash) each half needs, and both halves will want the same `## Parameters`. Expect duplication you then have to decide how to factor. It is the right move, but it is an afternoon, not the hour the table claims — and it is the one item here I would be comfortable with you deferring indefinitely.

**One thing I am not sure about.** Whether `## Syntax` should exist at all, or whether it should be `## Definition` like everywhere else in the vault, with the interface/instance distinction carried entirely by the folder and the callout type (`[!definition]` vs `[!scheme]`). Arguments for keeping `## Syntax`: it is already consistent across 28 notes; the word is standard in the literature for exactly this ("the syntax of a PKE scheme"); the reader learns the level from the heading without scrolling. Argument against: the vault now has three names for the defining slot — `## Definition`, `## Syntax`, `## Scheme` — and a convention with three names for one idea is the kind of thing that quietly stops being followed. I lean toward keeping it, on the strength of the literature usage, but I would not argue hard.

---

# Related

- [[Foundation Layer]] — the same treatment for `math/`
- [[North Star]] — the four kinds of note, the precision skeleton, the two-views convention
- [[Vault Refactoring Plan]] — the queue; V-IDs and K-batches are referenced there
- [[Security Game]] — the Level-0 vocabulary every `## Security` section is written in
