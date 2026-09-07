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

## 2.7 Correctness vs Completeness

Both are the honest-run condition: *nobody is cheating, does the thing work?* Both belong under `## Property`, never `## Security`. So why two words, and which slot does a given note want?

The vault already answers it cleanly and disjointly — 10 notes use `### Correctness`, 11 use `Completeness`, and **the split follows a real line**, not habit.

### The rule

> **Correctness** — the honest run must reproduce **data**. $\mathsf{Dec}(sk, \mathsf{Enc}(pk, m)) = m$.
> **Completeness** — the honest run must produce a **verdict**, and there is a dual condition on the other side of a promise.

### The test: *does it have a soundness partner?*

That is the whole distinction, and it is checkable in one look.

| | correctness | completeness |
| --- | --- | --- |
| honest output | data — a message, a key, a share, a digest | a bit — accept / reject |
| quantified over | **all** inputs | only inputs satisfying a **promise** ($\mathbf x \in \mathcal L$) |
| has a dual | **no** | **yes** — [[Soundness]], on $\mathbf x \notin \mathcal L$ |
| the pair means | — | no false negatives / no false positives |
| error feeds | correctness loss $\delta$ into a CCA proof (FO) | $\varepsilon_c$ into repetition and amplification |
| examples | [[Public-Key Encryption]], [[Key Encapsulation Mechanism]], [[Commitment Scheme]], [[Keccak]], [[Threshold Secret-Sharing]] | [[Interactive Proof Systems]], [[Sigma Protocols]], [[Argument Systems]], [[Probabilistically Checkable Proofs]], [[Schnorr Protocol]] |

The promise is what does the work. Because completeness only speaks about **true** statements, there is a whole other half of the input space left unspoken for — and that space is exactly where [[Soundness]] lives. Correctness quantifies over everything, so it leaves no room for a dual and needs none.

### The asymmetry that causes the filing mistake

Completeness and soundness look like a matched pair, so they get filed together. They should not be:

- **Completeness** — both parties honest, no attacker → `## Property`
- **Soundness** — an attacker in the prover slot → `## Security`

[[Schnorr Protocol]] and [[Interactive Proof Systems]] already do this correctly. The tell is not "is it half of a pair" but "is there an $\mathcal A$ trying to break it".

> [!remark]
> [[Completeness]] writes its condition as a game with an adversary $\mathcal A_\mathsf{find}$ — but that adversary only *chooses the statement*, it does not attack. It is there to strengthen the property to adversarially-chosen valid inputs. A chooser is not an attacker, and the note still belongs under `## Property`.

### Where the name flips: [[Fiat-Shamir Transform]]

A $\Sigma$-protocol has **completeness / soundness**. The signature scheme Fiat-Shamir turns it into has **correctness / unforgeability**. Same honest-run condition, renamed — and the test explains why: in a signature every $(pk, m)$ is a legitimate statement, so there is no $\mathbf x \notin \mathcal L$ half. The promise collapses, the dual disappears, and what is left is correctness. Unforgeability is a *search* game about producing $\sigma$ without $sk$, not a soundness condition on a language.

A **Transform** renaming a property as it crosses is worth one remark on each side; it is the same two-views situation as everywhere else.

### The homonym — four senses of "complete" in this vault

Two families, and they are not the same idea:

| sense | statement | dual | where |
| --- | --- | --- | --- |
| **proof completeness** | every true statement is provable / accepted | [[Soundness]] | crypto `proof/`, and [[First-Order Logic]] (Gödel: $\models \varphi \Rightarrow\; \vdash \varphi$), [[Equational Logic]] (Birkhoff) |
| **NP-completeness** | everything in the class reduces to it | none | [[Class NP-complete]] |
| **completeness of $\mathbb R$** | every Cauchy sequence converges | none | [[Real Number]] |
| *(same shape)* | every subset has a supremum | none | order completeness |

The first row is one idea in two dresses: **crypto borrowed completeness/soundness straight from proof theory**, and the duality is identical — no false negatives / no false positives. That is a genuine [[North Star|bridge]] worth a remark in [[Completeness]], because it explains the vocabulary rather than just recording it. **[Standard]**

Rows 2–4 are a *different* word: "complete" there means **maximal — nothing of the relevant kind is missing**, and none of them has a dual. Filing them under the same idea would be a false bridge.

## 2.8 Worked review — [[Non-Interactive Linear Proofs]] and the `st` / `td` question

### The answer: `st` wears two hats, and whether they can be conflated is exactly the DV / PV split

In Groth16's NILP (eprint 2016/260) `Setup` returns `(crs, st)` and **`st` is used by two different parties**:

| role | who uses it | shows up in |
| --- | --- | --- |
| **verification state** | the verifier, via `Test` | completeness, soundness |
| **simulation trapdoor** | the simulator | zero knowledge |

In the linear model over $\mathbb F$ these are *the same vector* — the paper writes one symbol because at that layer there is only one object. **They separate on compilation.** The linear-only encoding sends `crs` into the target group; `st` then splits in two:

- the part the verifier needs becomes a **verification key** `vk` — the *image* of `st` under the encoding,
- the raw field elements stay as the **simulation trapdoor** `td` — the *preimage*, the toxic waste.

And the crucial consequence:

> **Whether `st` and `td` may be identified is precisely the designated-verifier / publicly-verifiable distinction.**
> - **Designated verifier** — [[LUNA]], whose `st = (st_LPCP, sk.S)` contains an HGSW *decryption key*. `st` is secret, `vk = st`, and conflating `st` with `td` is harmless.
> - **Publicly verifiable** — Groth16. `vk` is published, `td` is destroyed. Conflating them means **publishing the trapdoor**, which is the one mistake in this area that is fatal rather than untidy.

**Recommendation: do not introduce `td` in [[Non-Interactive Linear Proofs]].** Keep the single symbol `st`, matching the source, and add the two-hats remark. Introduce `td` one layer up, in the compiled scheme, where the split is real — and say there that `td` is the NILP's `st` and `vk` is its encoding. Two symbols that are provably equal at the layer where you write them is worse than one symbol with a documented double role.

```markdown
> [!remark] `st` wears two hats
> `st` is the verifier's checking material (used by `Test`, so it appears in completeness and
> soundness) **and** the simulator's trapdoor (so it appears in zero knowledge). In the linear
> model over $\mathbb F$ these are the same vector, which is why the source writes one symbol.
> They separate on compilation: the encoding sends `st` to a verification key $\mathrm{vk}$,
> while `st` itself stays as the simulation trapdoor $\mathrm{td}$. Whether the two may be
> identified is exactly the designated-verifier / publicly-verifiable question — see [[LUNA]]
> (DV, `st` secret) against a publicly-verifiable SNARK (`vk` public, `td` destroyed).
```

### Bugs in the two notes

**Both notes:** `$\boldsymbol\pi \leftarrow \mathsf{Prove}(\mathcal R, \mathbf x, \mathbf w)$` — but step 2 returns $\Pi\,\mathrm{crs}$. **`crs` is not an argument.** Precision rule 2: an unbound symbol in a signature. Should be $\mathsf{Prove}(\mathcal R, \mathrm{crs}, \mathbf x, \mathbf w)$. [[LUNA]] already gets this right.

Also both: `\mathbf{F}^\eta` should be `\mathbb{F}^\eta`; step 1 declares $\mathbf t$ and step 2 applies $t$.

**[[Non-Interactive Linear Proofs]]:** no `## Property`, no `## Security` — the note stops after `## Syntax`. Three properties are missing (below). No `dg-publish`.

**[[Split Non-Interactive Linear Proofs]]:** its callout is titled `Non-Interactive Linear Proof` — **the same title as the parent's** — and the body says "A NILP for $\mathcal R$", not a split one. `\mathbf{F}^{m_2}` should be `\mathbb F^{m_2}`. $\Pi \in \mathbb F^{k \times m}$ now needs $m = m_1 + m_2$ and $k = k_1 + k_2$, which are never declared. It is otherwise a **verbatim copy** of the parent — only two lines differ.

### The three properties, with the right object in each

| property | slot | who holds what |
| --- | --- | --- |
| **Completeness** | `## Property` | honest $\Pi$; probability over `Setup`'s coins |
| **Non-adaptive knowledge soundness** (affine strategies) | `## Security` | $\mathcal A$ outputs $\Pi$ **before** `Setup` runs |
| **Perfect zero knowledge** | `## Security` | the simulator gets `st`, **in its trapdoor role** |

```markdown
> [!definition] Non-Adaptive Knowledge Soundness against Affine Strategies
> For any [[Adversary]] $\mathcal A = (\mathcal A_\mathsf{find})$ and extractor $\mathcal E$:
> $$\mathsf{Adv}^{\mathsf{ks}\mbox{-}\mathsf{aff}}_\mathsf{NILP}(\mathcal A, \mathcal E) =
\Pr\!\left[
\begin{array}{l}
\mathsf{Verify}(\mathcal R, \mathrm{st}, \mathbf x, \boldsymbol\Pi\,\mathrm{crs}) = 1 \\
(\mathbf x, \mathbf w) \notin \mathcal R
\end{array}
\;\middle|\;
\begin{array}{l}
(\mathbf x, \boldsymbol\Pi) \leftarrow \mathcal A_\mathsf{find}(\mathcal R) \\
(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal R) \\
\mathbf w \leftarrow \mathcal E(\mathcal R, \mathbf x, \boldsymbol\Pi)
\end{array} \right]$$

> [!remark] The order of the first two lines is the whole model
> $\mathcal A_\mathsf{find}$ commits to $\boldsymbol\Pi$ **before** `Setup` runs, so the probability is over
> `Setup`'s coins alone — which is why this is *statistical* and needs no assumption. Swap the two lines
> and you have stated the adaptive variant, which is a different and generally false claim. Same
> non-adaptive / adaptive pair as [[Linear Probabilistically Checkable Proofs]].

> [!remark] Why `crs` must contain $1$
> The clause "*with $1$ as an entry*" in `Setup` is not a technicality: it is what makes an **affine**
> prover strategy expressible as a **linear** one, so a single linear model covers both.
```

```markdown
> [!definition] Perfect Zero Knowledge
> For any $\mathcal A = (\mathcal A_\mathsf{choose}, \mathcal A_\mathsf{guess})$ and simulator $\mathcal S$, with
> $(\mathbf x, \mathbf w) \leftarrow \mathcal A_\mathsf{choose}(\mathcal R)$ and $(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal R)$
> shared by both branches:
> $$\mathsf{Adv}^\mathsf{zk}_\mathsf{NILP}(\mathcal A, \mathcal S) =
\left|\Pr[\,b = 1 \mid \boldsymbol\pi \leftarrow \mathsf{Prove}(\mathcal R, \mathrm{crs}, \mathbf x, \mathbf w)\,]
- \Pr[\,b = 1 \mid \boldsymbol\pi \leftarrow \mathcal S(\mathcal R, \mathrm{st}, \mathbf x)\,]\right|$$
> where $b \leftarrow \mathcal A_\mathsf{guess}(\mathrm{crs}, \mathrm{st}, \boldsymbol\pi)$ in both.
> This is where `st` acts as the **trapdoor**: $\mathcal S$ gets it, and gets no witness.
```

Note that **both branches share one `(crs, st)`** — the simulator produces only the proof. That is what makes the definition well-formed, and it is exactly what the LPCP note gets wrong below.

### The bug that actually bites: [[Linear Probabilistically Checkable Proofs]] HVZK

In **both** HVZK games the simulated branch generates $(\widetilde{\mathrm{st}}, \widetilde{\mathbf Q}, \mathrm{st}_\mathcal S)$ and then calls

$$b \leftarrow \mathcal A_\mathsf{guess}(\mathrm{st}, \mathbf Q, \widetilde{\mathbf a})$$

**`st` and `Q` are unbound in that branch** — they are never generated there. It must be $\mathcal A_\mathsf{guess}(\widetilde{\mathrm{st}}, \widetilde{\mathbf Q}, \widetilde{\mathbf a})$, and likewise $\mathcal A_\mathsf{guess}(\widetilde{\mathrm{st}}, \widetilde{\mathbf Q}, \widetilde{\mathbf a}, \widetilde{\mathbf Z}, \widetilde{\mathbf b})$ in the leakage variant. As written the two branches are not comparable and the definition says nothing.

An LPCP simulator legitimately generates its **own** query and state (the query is part of the verifier's view being simulated) — unlike the NILP simulator, which is handed the real `st`. Both patterns are correct; the note just has to hand the adversary the *matching* one. Worth a remark saying which pattern applies and why.

Minor: three `st`-shaped symbols in one game — `st` (real), $\widetilde{\mathrm{st}}$ (simulated), $\mathrm{st}_\mathcal S$ (the simulator's own working state). Rename the third.

### The split note should stop restating the syntax

```markdown
Extends: [[Non-Interactive Linear Proofs]]
Reference: https://eprint.iacr.org/2016/260.pdf

## Syntax

> [!definition] Split NILP
> A **split NILP** is a [[Non-Interactive Linear Proofs|NILP]] with the reference string and the
> proof matrix partitioned into two independent blocks. Only two things change:
> - $\mathrm{crs} = (\mathrm{crs}_1, \mathrm{crs}_2) \in \mathbb F^{m_1} \times \mathbb F^{m_2}$, $m = m_1 + m_2$;
> - $\Pi = \begin{pmatrix}\Pi_1 & 0 \\ 0 & \Pi_2\end{pmatrix}$ with $\Pi_i \in \mathbb F^{k_i \times m_i}$, $k = k_1 + k_2$.
>
> Everything else — `Setup`, `Prove`, `Verify`, `Test`, and all three properties — is inherited unchanged.

> [!remark] What the block structure buys
> <one sentence: each block can be encoded under its own key / computed by its own party>
> — the linear-model counterpart of [[Split Prover]].
```

That is `Extends:` doing real work: the note carries the delta and nothing else, so a fix to the parent's `Prove` signature does not have to be made twice. Right now it does — both notes carry the same missing-`crs` bug.

## 2.9 Fix order, and factoring the shared properties

### The fix, in order

Signature first, because the properties quote it. Anything else and you write the games twice.

| # | do | where | min |
| --- | --- | --- | --- |
| **1** | `Prove(R, x, w)` → **`Prove(R, crs, x, w)`**; `\mathbf F` → `\mathbb F` (3×); step 1 declares $\mathbf t$, step 2 applies $t$ — pick one | [[Non-Interactive Linear Proofs]] **and** [[Split Non-Interactive Linear Proofs]] | 5 |
| **2** | Add the **two-hats remark** (§2.8). No `td` in this note | NILP | 2 |
| **3** | Rewrite as `Extends:` + the two-line delta — draft in §2.8 | Split NILP | 10 |
| **4** | Tilde the adversary's arguments in **both** HVZK games: $\mathcal A_\mathsf{guess}(\widetilde{\mathrm{st}}, \widetilde{\mathbf Q}, \dots)$. Rename $\mathrm{st}_\mathcal S$ → $\mathrm{aux}_\mathcal S$ | [[Linear Probabilistically Checkable Proofs]] | 5 |
| **5** | Factor the properties — below | `proof/properties/` | 30 |
| **6** | Introduce `td` where the split is real; say [[LUNA]] is designated-verifier, so there `vk = st` | [[LUNA]], and any PV scheme | 10 |

Do **1** before **3**: fixing the parent first means the delta note never inherits the bug. That is the point of `Extends:`.

### Why the properties can be factored: it is one equation with the pen in different hands

[[Linear Probabilistically Checkable Proofs]] has a `[!definition] Linear Oracle`; [[Non-Interactive Linear Proofs]] has a `[!definition] Linear Evaluation`. **These are the same object under two names.**

$$\text{LPCP:}\quad \mathbf a = \mathbf Q^{T}\boldsymbol\pi, \quad \mathbf Q^{T} \in \mathbb F^{k \times m},\ \boldsymbol\pi \in \mathbb F^{m}
\qquad\qquad
\text{NILP:}\quad \boldsymbol\pi = \boldsymbol\Pi\,\mathrm{crs}, \quad \boldsymbol\Pi \in \mathbb F^{k \times m},\ \mathrm{crs} \in \mathbb F^{m}$$

Same shape — a $k \times m$ matrix against an $m$-vector. What differs is **who holds the pen**:

| | chooses the matrix | chooses the vector | verifier reads |
| --- | --- | --- | --- |
| **LPCP** | the **verifier** ($\mathbf Q$) | the **prover** ($\boldsymbol\pi$) | $\mathbf Q^T \boldsymbol\pi$ |
| **NILP** | the **prover** ($\boldsymbol\Pi$) | **`Setup`** ($\mathrm{crs}$) | $\boldsymbol\Pi\,\mathrm{crs}$ |
| **NIPS** | — | the prover ($\boldsymbol\pi$) | $\boldsymbol\pi$ (identity) |

That single swap explains a lot at once. It is why NILP soundness must be **non-adaptive** — the prover commits to its side of the pairing before `Setup` reveals the other — while LPCP has both an adaptive and a non-adaptive variant. It is also why the two ZK definitions differ in shape: the LPCP simulator has to produce the verifier's side ($\widetilde{\mathbf Q}, \widetilde{\mathrm{st}}$) because the verifier chose it, and the NILP simulator does not, because `Setup` did.

Write this as one `[!remark]` in each note. It is a **bridge**, cross-domain shape: neither note restates the other.

### The factoring: property notes own the game, system notes supply the arguments

Call $\mathcal O$ the **response map** — how the verifier's input is derived from the prover's output. Then a property is

$$\textbf{game shape} \;\times\; \mathcal O \;\times\; \textbf{adaptivity} \;\times\; \textbf{strength row}$$

and three of those four already have homes: $\mathcal O$ in each system's own oracle callout, adaptivity as the named non-adaptive/adaptive pair [[Linear Probabilistically Checkable Proofs]] already uses, and the strength row in [[Security Game]]'s table.

So `proof/properties/<P>.md` holds **the game, once, over an abstract $(\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify}, \mathcal O)$**, plus a variant table. And a system note's `## Property` / `## Security` section holds a **one-line instantiation**, no formula:

```markdown
### Completeness

[[Completeness]] with $\mathcal O(\boldsymbol\Pi) = \boldsymbol\Pi\,\mathrm{crs}$ and $\varepsilon_c = 0$.
```

That is exactly what [[Group]] does with [[Associativity]] — link the axiom, supply the arguments, never restate. **And it is a note link, not a heading anchor**, so it does not break [[North Star]]'s rule; the discriminating information lives locally as parameter values.

### How far to factor — three different answers

Do **not** apply this uniformly. The three properties differ in how much is genuinely shared:

| property | shared? | do |
| --- | --- | --- |
| **[[Completeness]]** | almost entirely — honest run, verdict $1$ | **Factor fully.** One game, a variant table, one-line instantiations everywhere |
| **[[Soundness]] / [[Knowledge Soundness]]** | shape yes, adaptivity and what the extractor receives no | **Factor the statement, keep the game local.** The property note carries the shape and the comparison table; each system keeps its own formula because the quantifier order *is* the content |
| **[[Zero Knowledge]]** | **no** — LPCP's simulator makes its own $(\widetilde{\mathbf Q}, \widetilde{\mathrm{st}})$, NILP's is handed the real `st` | **Do not factor.** State both patterns side by side in [[Zero Knowledge]] and name which system uses which. The gap *is* the content — the *not equivalent* row of the two-views convention |

The failure mode to avoid: a property note that is a template with five holes, so reading it means opening three other notes. The test is whether a reader can state the property after reading **one** note. Completeness passes. Zero knowledge does not, and should not be forced to.

### What this buys immediately

The LPCP HVZK bug — the untilde'd $\mathcal A_\mathsf{guess}(\mathrm{st}, \mathbf Q, \dots)$ — is a copy-and-edit slip, the same failure mode that hit the algebra notes three times. Both games in the note carry it, because the second was cloned from the first. Factoring the shape into one place is the structural fix for that class of bug: there is one copy to get right.

## 2.10 `Disclosure-Free NILP`, and what it teaches about property design

### It extends the **split** NILP, not the plain one

Groth16's **Definition 4** is stated for a *split* NILP, not for a NILP. So in the vault:

```
Extends: [[Split Non-Interactive Linear Proofs]]
```

which makes the chain `NILP → Split NILP → Disclosure-Free NILP` — and makes **V19** (rewriting Split NILP as a delta note) load-bearing rather than cosmetic: this note inherits through it.

### Your current syntax cannot express it

Groth16's `Vfy` computes a test on **$(\sigma, \pi)$ jointly** — $t(\sigma, \pi) = 0$ — and in the split case the check is a bilinear form $[\sigma_1; \pi_1]_1^{T}\, T_i\, [\sigma_2; \pi_2]_2 = 0$. [[Non-Interactive Linear Proofs]] currently declares $\mathbf t : \mathbb F^{k} \to \mathbb F^{\eta}$ and accepts if $t(\boldsymbol\pi) = 0$ — **the test never sees $\mathrm{crs}$.**

That is not a cosmetic gap here. Disclosure-freeness is *entirely about how the test depends on $\sigma$*. With the current signature the property is **not statable**. Fix the signature (step 1 of §2.9) before writing this note.

### Draft

```markdown
Extends: [[Split Non-Interactive Linear Proofs]]
Reference:
- https://eprint.iacr.org/2016/260.pdf — Groth16, Definition 4

## Syntax

> [!definition] Disclosure-Free NILP
> A [[Split Non-Interactive Linear Proofs|split NILP]] is **disclosure-free** if the outcome of the
> verifier's tests on the real reference string is already determined by an **independently sampled**
> one — the accept/reject bit discloses nothing about which $\mathrm{crs}$ was drawn.
> $$\Pr\!\left[ t(\mathrm{crs}, \boldsymbol\Pi\,\mathrm{crs}) = 0 \;\middle|\;
> \begin{array}{l}(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal R) \\
> (\mathbf x, \boldsymbol\Pi) \leftarrow \mathcal A(\mathcal R) \\
> \mathbf t \leftarrow \mathsf{Test}(\mathcal R, \mathbf x, \mathrm{st})\end{array}\right]
> \;=\;
> \Pr\!\left[ t(\mathrm{crs}', \boldsymbol\Pi\,\mathrm{crs}') = 0 \;\middle|\;
> \begin{array}{l}\text{as above, plus} \\ (\mathrm{crs}', \mathrm{st}') \leftarrow \mathsf{Setup}(1^\lambda, \mathcal R)\end{array}\right]$$

> [!todo] Verify the quantifier against Definition 4
> Substance is right — *tests on the real $\sigma$ are predictable from an independent $\sigma'$* — but I
> could not retrieve Definition 4 verbatim (eprint blocks automated fetch; the mirror paraphrased).
> Check whether it is an equality or a statistical bound, and whether $\mathcal A$ also receives $\mathrm{crs}$.

## Intuition

The verifier's decision is a channel from $\mathrm{crs}$ back to whoever can watch it. Disclosure-freeness
says that channel is silent: you would have gotten the same verdict against a reference string drawn fresh.

## Property

### Why the condition exists

> [!remark]
> This is what lets the compiled scheme survive a verifier whose answers are observable. Without it, an
> adversary submits malformed proofs and reads accept/reject to learn the verifier's secret one bit at a
> time — the **verifier-rejection problem** of designated-verifier SNARKs. Compare [[LUNA]], which is
> designated-verifier and therefore has to care.

## Related

- [[Split Non-Interactive Linear Proofs]] — what it extends
- [[Non-Interactive Linear Proofs]] — the base model
```

### And this is the note that proves your instinct right

Look at the shape of the definition: it mentions **`Setup` twice** — once for the real reference string and once for an independent one. It is not a statement about an honest run (completeness) or an adversarial run (soundness) or a simulation (zero knowledge). It is a statement about **the setup distribution relative to the tests**.

So it does not fit the game-shape factoring of §2.9 at all, and it has exactly **one** binder. By the graduation rule it should be written where it is used — which is what you said.

### The intuition you are reaching for: two kinds of "property"

Associativity and Completeness are not the same *kind* of thing, and that is why the design feels different.

| | **Tier 1 — equational** | **Tier 3 — game** |
| --- | --- | --- |
| a property is | a formula with a hole: $\mathsf{Assoc}(\star)$ | a **script**: who moves, in what order, who sees what |
| binding is | **substitution** — plug in $\star$ | **family resemblance** — the same script with different moves |
| exactness | mechanical and total | approximate; two uses can share a script and still differ |
| theorems about the property | transfer **verbatim** to every binder | rarely exist |

[[Associativity]] earns a note because binding is substitution: *generalized associativity* — every bracketing agrees — is proved once and inherited by [[Semigroup]], [[Monoid]], [[Group]], [[Ring]], every category. Inlining it means proving it six times.

For a game property there is usually no such theorem to inherit. So the graduation test changes:

> **Tier 1**: graduate as soon as a **second definition binds it**.
> **Tier 3**: graduate only when the difference between uses **fits in a parameter slot** — same script, different named objects. If the *script* changes, keep the game local and let the shared note hold the comparison.

### The part of the payoff that is easy to miss

The one-line axiom is not what a property note is for. Three things are, in increasing order of value:

1. **Deduplication** — least important, and the usual reason people give.
2. **Inheritance of theorems** — real at Tier 1, rare at Tier 3.
3. **A home for the boundary.** [[Associativity]]'s value is that subtraction is not associative, the octonions are not, and the $A_\infty$ story starts there. [[Cancellativity]]'s value is Ore's condition and the embedding theorem. **When you meet a new object the question you actually have is "does it have $P$, and what breaks if not" — and only the property note answers it.** Inlined, the boundary scatters across the binders and is never found again.

Test (3) before creating a Tier-3 property note. Ranked by whether general theorems and a real boundary exist:

| property | general theorems? | verdict |
| --- | --- | --- |
| [[Soundness]] | yes — repetition amplifies, hybrids compose | shared note earns it |
| [[Zero Knowledge]] | yes — sequential composition | shared note earns it, but **do not** merge the game shapes (§2.9) |
| [[Completeness]] | barely — it is almost always perfect | shared note is a comparison table, little more |
| **disclosure-freeness** | none, one binder | **write it in the note that uses it** |

## 2.11 Simulators, extractors, and where the quantifier goes

### The one thing to fix: $\mathcal S$ has no quantifier

[[Knowledge Soundness]] says it correctly — *"For any adversary $\mathcal A$, **there exists** an efficient extractor $\mathcal E$"*. [[Zero Knowledge]] says *"For any adversary $\mathcal A$ **and** simulator $\mathcal S$"*, which reads as $\forall \mathcal A\, \forall \mathcal S$ and is not the notion. It must be $\exists \mathcal S\, \forall \mathcal A$.

And note they are **opposite orders**. That is not an accident:

| notion | quantifier | why |
| --- | --- | --- |
| **HVZK** | $\exists \mathcal S\ \forall \mathcal A$ | one simulator must fool *every* distinguisher; a per-distinguisher $\mathcal S$ could just be told the answer |
| **malicious-verifier ZK** | $\forall \mathcal V^*\ \exists \mathcal S$, or $\exists \mathcal S^{(\cdot)}\ \forall \mathcal V^*$ | the simulator may depend on the cheating verifier's code — **that gap is exactly the non-black-box / black-box distinction** |
| **knowledge soundness** | $\forall \mathcal A\ \exists \mathcal E$ | the extractor may depend on the prover's code |

The last row is worth a remark of its own: $\forall \mathcal A\, \exists \mathcal E$ **is not a falsifiable game** in Naor's sense — you cannot decide a winner by running an experiment, because $\mathcal E$ is quantified after $\mathcal A$. That is the formal reason knowledge assumptions sit outside the falsifiable framework, and why succinct arguments need them.

### Where to put it: the game / notion split you already have

[[Security Game]] already separates *a game* from *a notion* — "a security notion fixes a game, then demands the advantage be small for a class of adversaries." Use that seam:

- **The advantage is a function.** *"For any $\mathcal A$ and any $\mathcal S$, define $\mathsf{Adv}^\mathsf{zk}(\mathcal A, \mathcal S) = \dots$"* — correct as written, because the advantage really is a function of both.
- **The notion quantifies.** One sentence after the array:

```markdown
> $\Pi_\mathsf{NIPS}$ is **zero-knowledge** if there **exists** an efficient simulator $\mathcal S$ such that
> $\mathsf{Adv}^\mathsf{zk}_\mathsf{NIPS}(\mathcal A, \mathcal S)$ is negligible for every [[PPT]] $\mathcal A$
> — perfect if it is $0$ for every unbounded $\mathcal A$ ([[Security Game]]'s rows).
```

That is the minimal fix: **one sentence per game**, not a restructure.

### Give the simulator a signature

$\mathcal S$ is an algorithm. Declare it like `Prove` and `Verify`, above the game, instead of introducing it inside a probability array:

```markdown
> [!definition] Simulator
> A **simulator** for $\Pi_\mathsf{NIPS}$ is a pair $\mathcal S = (\mathcal S_\mathsf{setup}, \mathcal S_\mathsf{prove})$:
> - $(\widetilde{\mathrm{crs}}, \widetilde{\mathrm{st}}, \mathrm{aux}_\mathcal S) \leftarrow \mathcal S_\mathsf{setup}(1^\lambda, \mathcal R)$
> - $\widetilde{\boldsymbol\pi} \leftarrow \mathcal S_\mathsf{prove}(\mathrm{aux}_\mathcal S, \mathbf x)$
>
> $\mathcal S_\mathsf{prove}$ receives **no witness**. That is the entire content of the notion; everything
> else is bookkeeping.
```

The no-witness line is the point of the whole definition, and buried inside a probability array nobody sees it.

### The simulator's phases are derivable, not conventional

> **$\mathcal S$ has one phase per scheme algorithm that the simulated branch has to fake.**

Count the algorithms that appear in the real branch and are *replaced* in the simulated one. That rule reproduces all four of your notes with no judgement calls:

| note | faked | simulator |
| --- | --- | --- |
| [[Zero Knowledge]] (NIPS) | `Setup`, `Prove` | $\mathcal S = (\mathcal S_\mathsf{setup}, \mathcal S_\mathsf{prove})$ ✓ |
| [[Linear Probabilistically Checkable Proofs]] | `Query`, `Prove` | $\mathcal S = (\mathcal S_\mathsf{query}, \mathcal S_\mathsf{prove})$ ✓ |
| [[Non-Interactive Linear Proofs]] (§2.8 draft) | `Prove` only — `Setup` is shared | $\mathcal S$, one phase ✓ |
| [[Split Prover]] | `Setup`$_\mathsf{split}$, `Prove`$_{I}$ | $\mathcal S = (\mathcal S_\mathsf{setup})$ doing both ✓ |

So the two ZK shapes from §2.9 are not two conventions, they are two answers to one question:

- **Setup simulation** — $\mathcal S$ produces its own $(\widetilde{\mathrm{crs}}, \widetilde{\mathrm{st}})$, because the setup is part of the view. NIPS, LPCP, Split Prover.
- **Trapdoor simulation** — the setup is honest and shared; $\mathcal S$ is handed `st` in its trapdoor role. NILP.

That is the same fork as §2.8's `st` / `td`: **whether the simulator programs the setup or receives a trapdoor is whether the setup is inside or outside the view.** One remark in [[Zero Knowledge]] covers both, and then each system says which it uses.

### Naming

$\mathrm{st}_\mathcal S$ collides with the verification state. Use $\mathrm{aux}_\mathcal S$ — [[Split Prover]] already uses $\mathrm{aux}$ for exactly this kind of hand-off between phases.

### Bugs found in the same pass

- **[[Zero Knowledge]]: the distinguisher has amnesia.** $\mathcal A_\mathsf{find}$ sees $(\mathcal R, \mathrm{crs}, \mathrm{st})$ and outputs $(\mathbf x, \mathbf w)$; then $\mathcal A_\mathsf{guess}(\boldsymbol\pi)$ receives *only the proof* — not the crs, not the statement, no state. It cannot even tell which statement it is looking at. The house format passes a state: compare [[Public-Key Encryption]]'s IND game, $(m_0, m_1, s) \leftarrow \mathcal A_\mathsf{find}(pk)$ then $b' \leftarrow \mathcal A_\mathsf{guess}(s, c^*)$. Fix: $(\mathbf x, \mathbf w, s) \leftarrow \mathcal A_\mathsf{find}(\dots)$, $b \leftarrow \mathcal A_\mathsf{guess}(s, \boldsymbol\pi)$. Same gap in [[Linear Probabilistically Checkable Proofs]]' $\mathcal A_\mathsf{choose}$.
- **[[Knowledge Soundness]] declares $\mathcal E = (\mathcal E_\mathsf{NIPS})$ and then calls $\mathcal E_\mathsf{find}$** — declared with one phase name, used with another.
- The affine variant is labelled $\mathsf{Adv}^{\mathsf{ks}}_\mathsf{NIPS}$ but is about a **NILP**; `\mathbf F` should be `\mathbb F`; and `$\Pi \in \mathbf F^{k \times m}$` sits in the *event* column of the probability, where it is a type declaration, not an event — it belongs in the experiment column or in prose. $\Pi$ / $\Pi^*$ are used interchangeably.

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

## V14 · Three notes use the wrong one of the pair

| note | says | should say | why |
| --- | --- | --- | --- |
| [[Puncturable Pseudorandom Function]] | `### Completeness of Puncturing` | `### Correctness` | $\mathsf{Eval}(k, x') = \mathsf{Eval}(k_X, x')$ reproduces **data**. No verdict, no promise, no soundness partner |
| [[Secure Multi-party Computation]] | `[!definition] Soundness` — *honest parties compute correct outputs* | **Correctness** | That is the honest-run condition. MPC calls it correctness; soundness is not an MPC notion. The four other bullets there (Privacy, Input Independence, Guaranteed Output Delivery, Fairness) are fine |
| [[Completeness]] | $\mathsf{Adv}^\mathsf{cmp}_\mathsf{NIPS}(\mathcal A) = \Pr[\dots]$, *"sometimes referred to as completeness error $\varepsilon_c$"* | separate the two | The expression is a **success** probability — you want it near $1$. Every other $\mathsf{Adv}$ in the vault you want near $0$. The error is $\varepsilon_c = 1 - \mathsf{Adv}^\mathsf{cmp}$; naming them the same thing inverts the reading |

The third is the one that will bite in a proof. It is also an argument for a line in [[Security Game]]: **$\mathsf{Adv}$ means a quantity to be driven to zero** — completeness is the one place that convention breaks, so say so where the convention is defined.

## V15 · The completeness / soundness duality is borrowed and unlabelled

[[Completeness]] and [[Soundness]] each open with a one-line `[!remark]` (*"a true statement can be proven"* / *"a false statement cannot be proven"*) and then go straight to the NIPS game. Neither says where the pair comes from: it is proof theory's, unchanged — [[First-Order Logic]]'s Gödel completeness is $\models \varphi \Rightarrow\; \vdash \varphi$ and its soundness is the converse. One `[!remark]` on each side turns two isolated definitions into a bridge, and explains the vocabulary instead of just recording it. §2.7 has the four-sense table; the other three senses (NP-complete, completeness of $\mathbb R$, order completeness) are a **different word** and must not be bridged to these.

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
