# Assignments

*Practice loop. I place the stub — location, layout, reference, and a checklist. You fill it from the source. Then say **"review assignment N"** and I mark it against the checklist and against [[Note Layouts]].*

**Rules of the game.** I do not write the content. If an item says *do not create a note*, the correct answer is a remark or a link — creating one is a wrong answer. If you disagree with a placement, say so and argue it; that counts as a correct answer if the argument holds.

---

# Assignment 1 · The RSD project

Source: your Definitions 1–6, plus https://eprint.iacr.org/2003/230 for regular words.

## 1A · Fix a bug you just shipped — [[Power Set Ring]]

**Where** `math/algebra/structures/rings/examples/Power Set Ring.md` · **Layout** Example (4)

The note says $A + B = A \amalg B$. Disjoint union is not an operation on $\mathcal P(S)$ — $A \amalg B$ does not land back in $\mathcal P(S)$ unless $A$ and $B$ are already disjoint, and there are no additive inverses.

**Must contain** the correct operation; the additive identity and the multiplicative identity; and the observation that **every element is idempotent**, which makes this a *Boolean* ring.
**I will check** that the ring axioms actually hold under what you wrote, and that you linked [[Idempotence]].

## 1B · Create — `Regular Word`

**Where** `information theory/code-based/weight/` · **Layout** Object (1) · **Reference** eprint 2003/230; your Definition 1

The support set that [[Regular Syndrome Decoding Problem]], 2-RNSD and the FSB hash all quantify over — the sibling of [[Hamming Sphere]].

**Must contain**
- the block decomposition: $K = wb$, $x = (x^{(1)}, \dots, x^{(w)})$ with $x^{(i)} \in \mathbb F_2^b$
- $\mathrm{Reg}_w := \{x : \mathsf{wt}(x^{(i)}) = 1\ \forall i\}$, and $|\mathrm{Reg}_w| = b^w$
- **2-regular words**, and the count $\left(1 + \binom b2\right)^w$
- a `### Relation to [[Hamming Sphere]]` — every regular word has weight exactly $w$, so $\mathrm{Reg}_w \subsetneq \mathcal S_w^{wb}$; say how much smaller and why that matters for encoding rate.


**I will check** the two counts, the strictness of the inclusion, and whether you noticed which of $b^w$ and $\binom{wb}{w}$ is larger — that comparison is the whole reason FSB picks one encoding over the other.

## 1C · Do **not** create a note — the support bridge

**Where** a `[!remark]` in [[Power Set Ring]] and a `### Support` in [[Hamming Weight]] · **Layout** Bridge

$\mathrm{supp} : \mathbb F_2^n \to \mathcal P([n])$ and the indicator map $T \mapsto \mathbf 1_T$ are mutually inverse, and they carry $\oplus \mapsto \triangle$ and $\circ \mapsto \cap$. So $(\mathbb F_2^n, \oplus, \circ)$ **is** the power set ring on $[n]$.

**Must contain** the isomorphism named on one side and a link back from the other; and $\mathsf{wt}(z) = |\mathrm{supp}(z)|$.
**I will check** that you wrote a remark and not a note, that only **one** side carries the statement, and that you did not restate the ring axioms.

## Review · 1A, 1B, 1C — marked 2026-09-05

| item | mark | one line |
| --- | --- | --- |
| **1A** [[Power Set Ring]] | **not done** | operation unchanged, and the error propagated |
| **1B** [[Regular Word]] | **strong** | counts correct; two real bugs, one omission |
| **1C** support bridge | **right call, thin execution** | you correctly wrote no note — but the definition does not define |

### 1A — still $A + B = A \amalg B$

$\amalg$ is coproduct / disjoint union. It is **not an operation on $\mathcal P(S)$**: $A \amalg B$ leaves $\mathcal P(S)$ unless $A \cap B = \emptyset$, and there are no additive inverses. What makes this a ring is **symmetric difference** $A \triangle B$.

And it spread — [[Hamming Weight]]`#Support` now also writes $(\mathcal P([n]), \amalg, \cap)$. **An error inside a definition propagates to every note that links it**: the argument for the precision skeleton, demonstrating itself.

Still missing: the identities $\emptyset$ and $S$, and that every element is [[Idempotence|idempotent]] — which is what makes it a **Boolean ring**, not merely commutative.

### 1B — two bugs and an omission

1. **Wrong index set.** $\forall i \in [n]$ should be $\forall i \in [w]$ — there are $w$ blocks. Same slip in the 2-regular definition.
2. **The strictness claim fails at the edges.** *"As $w < n$"* is not the reason, and the conclusion is false twice: $w = 1$ gives one block of length $n$, so $\mathrm{Reg}_1 = \mathcal S_1^n$; $b = 1$ forces every block to $1$, so $\mathrm{Reg}_w = \mathcal S_n^n$. Strictness needs $w \geq 2$ **and** $b \geq 2$ — a `### Condition` line. Inclusion holds because one nonzero per block forces total weight $w$; strictness holds because a sphere element may put two ones in one block and none in another.
3. **The omission.** By Stirling $\binom{wb}{w} \approx b^w e^w / \sqrt{2\pi w}$ — the sphere is larger by about $e^w$, so it carries roughly $w \log_2 e \approx 1.44w$ more bits. **Regular encoding is chosen despite the worse rate**, for speed and for the exact 2-RNSD reduction. That trade-off is the note's reason to exist.

Correct as written: both counts, the $q$-ary generalisation, the sum-of-two-regulars proposition. Missing the `Reference:` header; and `### Relation to [[Hamming Sphere]]` sits under `## Definition` when it is a `## Property`.

### 1C — right call, then under-written

You created no note and put the statement on one side only. That was the item, and you passed it.

But the callout is `[!definition] Support` and **it never defines support** — it opens with a property of a map that has not been introduced. Add $\mathrm{supp}(z) := \{i \in [n] : z_i = 1\}$ first. Then: $\mathsf{wt}(z) = |\mathrm{supp}(z)|$ is missing — the checklist line, and the one identity tying this section to the note it lives in. The second operation is written $\cdot$ when it is the component-wise product, $\odot$ (Schur / Hadamard). And it is a bridge, so `[!remark]`, not `[!definition]`.

---

## 1D · Rebuild — [[Commitment Scheme]]

**Where** existing note · **Layout** Primitive (5) · **Reference** your Definition 2

### The rule the axes obey

You asked whether the definition should state the axes. **It should state none of them.** An axis appearing inside a `[!definition]` is a sign the definition is trying to be several definitions. Sort each axis by one test — **does it change the signature?**

| axis | changes the signature? | where it goes |
| --- | --- | --- |
| **setup** — keyless · public parameters · trusted CRS | adds one optional algorithm | `## Syntax`, as `\mathsf{Setup}`; keyless is the trivial case |
| **opening** — $o = \rho$ · $o$ arbitrary | **no** — a specialisation of one signature | a `[!remark]` under Syntax |
| **arity** — single message · **positional opening** | **yes** — new algorithms *and* a new security notion | **its own note**, `Extends: [[Commitment Scheme]]` |
| **binding strength** | no | a row of [[Security Game]]'s table, in `## Security` |
| **hiding strength** | no | same |

### Where your instinct needs one correction

Arity is **not** a property of the message. "Commit to a tuple" is free — take $\mathcal M^N$ as the message space and nothing changes. What makes a **vector commitment** a different primitive is *per-position opening*: $\mathsf{Open}(c, i) \to (m_i, o_i)$, $\mathsf{Verify}(c, i, m_i, o_i)$, and a new notion, **position binding** — no adversary opens position $i$ to two values. New algorithms plus a new game means a new note, not a mode.

### Your syntax is already the more general one

| | your note | Definition 2 |
| --- | --- | --- |
| commit | $(c, o) \leftarrow \mathsf{Com}(m)$ | $c \leftarrow \mathsf{Com}(\mathsf{PP}, x; \rho)$ |
| verify | $\mathsf{Verify}(m, c, o)$ | $\mathsf{Verif}(\mathsf{PP}, x, c, \rho)$ |

Keep $o$: for a hash commitment $o = \rho$, but **for a [[Merkle Tree]] the opening is an authentication path, not the randomness**. Definition 2 is the special case, and one remark says so.

### The bug to fix while you are there

$$\mathsf{Adv}^{\mathsf{Bind}}(\mathcal A) = \Pr\big[m_1 \neq m_2 \wedge c_1 = c_2 \;\big|\; (m_1, m_2) \leftarrow \mathcal A(); (c_1, o_1) \leftarrow \mathsf{Com}(m_1); (c_2, o_2) \leftarrow \mathsf{Com}(m_2)\big]$$

The **challenger** commits, so this measures collision probability of an honest $\mathsf{Com}$ — and it never calls $\mathsf{Verify}$, so a scheme whose verifier accepts everything passes. Binding says the *adversary* produces one commitment and two valid openings, which is exactly what your Definition 2 says in words.

**Must contain** the single syntax with `Setup` optional and the $o = \rho$ remark · a corrected binding game · the `[!remark]` that **statistical hiding and statistical binding cannot both hold** ([[Security Game]] already states it) · a `## Variant` pointing at the new note below.
**I will check** that hiding came out a **distinguishing** game and binding a **search** game, each with its four Condition lines ([[Note Layouts]] §10), and that no axis ended up inside a `[!definition]`.

## 1D′ · Create — `Vector Commitment`

**Where** `verifiable computing/commitment/` · **Layout** Primitive (5), with `Extends: [[Commitment Scheme]]`

**Must contain** only the delta: the positional $\mathsf{Open}$ / $\mathsf{Verify}$, and **position binding** as its own game.
**I will check** that you wrote a delta and not a second full definition, and that you then set [[Merkle Tree]] (40 bytes) to `Instantiates: [[Vector Commitment]]` — which is what that stub has been waiting for, and what MPC-in-the-head needs when it opens $n-1$ of $n$ views.

## 1E · Search before you write  *(on hold)* — Definitions 3 and 4

**Where** [[Soundness]], [[Knowledge Soundness]], [[Zero Knowledge]] · **Layout** Security property (10)

All three already exist. **Creating new notes here is the wrong answer.**

**Must contain** a short diff, written as a `[!remark]` in each note where the source says something the note does not:
- Definition 3's soundness is stated for **interactive** $\langle P^*, V\rangle(s)$; the notes are non-interactive. Is that a variant or a gap?
- Definition 4's HVZK is $\mathsf{Sim}_\Pi(s) \approx_c \mathsf{View}_V[\langle P(w), V\rangle(s)]$ — it uses **$\mathsf{View}$**, which [[Interactive Proof Systems]] also uses and nothing defines. Fix that here.
- Definition 3 says *"any sufficiently successful prover admits a PPT extractor"* — write out the quantifier.

**I will check** that you created nothing, and that the quantifier in the third bullet came out as $\forall \mathcal A\ \exists \mathcal E$ and not the reverse.

## 1F · Create, and justify the placement  *(on hold)* — `k-Way Parity Test`

**Where** *you decide* · **Layout** *you decide* · **Reference** your Definition 5

This is the judgement item. It is a randomised procedure with a syntax ($\phi$ in, $\sigma$ out) and a guarantee — so it is arguably a Primitive, arguably a Transform, arguably a Theorem about a test.

**Must contain** the syntax; the fibers $S_j := \phi^{-1}(j)$ and parities $\beta_j$; the parity profile $\sigma$; **and the fact that motivates it** — for $v$ a unit vector the profile is a unit vector, so the test is complete.
**I will check** your placement *argument* more than your placement, and whether you noticed that $\bigoplus_j \beta_j = \mathsf{wt}(v) \bmod 2$, which is the constraint your Definition 6 leans on when it says the last bit is determined.

## 1G · Create — `Single-Product Detector`  *(on hold)*, and read it critically

**Where** with 1F · **Layout** Security property (10) or Theorem (12) — argue which · **Reference** your Definition 6

**Before you write it, check whether the definition is satisfiable.** Take $v = 0$: every $\beta_j = 0$, so $c = \beta_i\beta_j = 0$. The all-zero profile is not a unit-vector profile, so $v = 0$ is a "non-unit violation" on which $c$ does **not** evaluate to $1$. Same for any $v$ whose $1$s all land in one fiber.

So *"evaluates to 1 on all non-unit violation profiles"* cannot hold as written.

**Must contain** either a corrected statement — most likely a **probability over the random labeling $\phi$**, which is what makes it a test rather than a predicate — or an argument that I have misread the definition.
**I will check** the corrected quantifier, and whether the guarantee ended up in the `### Property` slot as a bound rather than as an absolute claim.


---

# Assignment 2 · Carozza–Couteau–Joux

*Short Signatures from Regular Syndrome Decoding in the Head* — the project paper. §2 Preliminaries is the source for all of these.

## 2A · The generic support, done properly — `Syndrome Decoding under ℕ-Linear Constraints`

**Where** with [[Syndrome Decoding Problem]] · **Layout** Problem (8) · **Reference** CCJ §2.1, Definition 2

Their Definition 2 is the parameterisation we were groping toward with "admissible word set $W$" — and it is **constructive**: $W = \{x \in \{0,1\}^K : L x = \mathbf v \text{ over } \mathbb N\}$ for $L \in \mathbb N^{c \times K}$, $\mathbf v \in \mathbb N^c$.

**Must contain** all three instantiations — plain SD is $c = 1$, $L = (1, \dots, 1)$, $\mathbf v = w$; **regular** SD is $c = w$, $L$ the block-indicator rows, $\mathbf v = (1,\dots,1)^\top$; $d$-split SD is $d$ blocks of weight $w/d$ — and the **feasibility** condition: $(L, \mathbf v)$ counts only if you can sample uniformly from $W$ in $\mathrm{poly}(K)$.
**I will check** whether you made this the **Scope of the whole SD family** rather than a fourth sibling note, and whether [[Regular Word]] now links it as its defining constraint.

## 2B · Create — `Gap-HVZK`

**Where** `proof/properties/` · **Layout** Security property (10) · **Reference** CCJ §2.2; [CKY09]

Knowledge soundness where the extractor produces a witness for a **larger** language $\mathcal L' \supseteq \mathcal L$ — the extracted vector is only *close* to regular.

**Must contain** the relaxed `### Condition` line, and why the paper needs it (soundness is analysed against provers using a witness *sufficiently close* to regular).
**I will check** that you wrote it as a `## Variant` of [[Knowledge Soundness]] rather than a new notion, and that you noticed it is the same shape as lattice **soundness slack**.

## 2C · Fill the stub — [[Multi-Party Computation-in-the-Head]]

Currently 65 bytes. **Layout** **Transform** — it takes an $n$-party protocol for $f'$ and returns an HVZK argument of knowledge. **Reference** CCJ §2.3; [IKOS07]

**Must contain** `Building Blocks` (the MPC protocol, a commitment — see 1D′), the compiler steps, and the **loss**: soundness error $1/n$, because the verifier opens $n - 1$ of $n$ views.
**I will check** that every Building Block reappears in `## Security` carrying a hypothesis (§2.6 of [[Cryptography Layer]]), and that HVZK is attributed to passive security against $n-1$ corruptions rather than asserted.

## 2D · Fix — [[Knowledge Soundness]] from CCJ's $\varepsilon$-soundness

Their definition gives the concrete shape yours lacks: for every $\tilde{\mathsf P}$ with success $\tilde\varepsilon > \varepsilon$ there is a **rewindable black-box** extractor running in $\mathrm{poly}(\lambda, (\tilde\varepsilon - \varepsilon)^{-1})$ that outputs a witness with probability $\geq 1/2$.

**I will check** the quantifier order, and that the runtime bound landed in `### Condition` and not in prose.

## 2E · Notation — and do not over-create

$\odot$ (Schur / Hadamard product) and $[\![\mathbf u]\!]_T$ (additive sharing over $\mathbb Z_T^\ell$ conditioned on $\sum_i \mathbf u_i = \mathbf u$).

**One of these deserves a note and one does not.** Decide which, and write the argument in your answer — the placement reasoning is the graded part.

---

## How to hand it back

Commit, then say **"review assignment 1"** or **"review 2A, 2C"** — name whatever you finished. Partial is fine; I mark what is there.
