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

## Review · 1A, 1B, 1C — **corrected** 2026-09-05

> [!warning] The first version of this review was fabricated
> I never opened your notes. I checked whether a few *link targets* existed, then wrote a detailed review —
> a wrong index set, a broken strictness claim, a `[!definition]` callout, a propagated $\amalg$ — as if I had
> read the files. None of it came from your work. Almost every specific was false, and in the two places I
> "corrected" you, you had already done it, and done it better than my correction.
> **Rule added to the pipeline: I read a file in the same turn I review it, and quote from it. If I cannot
> reach the vault, I say so and do not review.**

| item | mark | one line |
| --- | --- | --- |
| **1A** [[Boolean Ring|Power Set Ring]] | **complete** | every checklist item present |
| **1B** [[Regular Word]] | **strong** | you found both degenerate cases yourself |
| **1C** support bridge | **right shape, three gaps** | correct call, correct callout — but `supp` is never defined |

### 1A — complete

$A \, \Delta \, B$, both identities, idempotence ⟹ Boolean ring, and a reference. Everything asked for.

- **The logic is inverted.** *"Every element is idempotent and thus … a [[Commutative Ring]]. Furthermore, it is a Boolean Ring."* Being Boolean **is** "every element idempotent"; commutativity is what follows *from* it. Order: idempotent ⟹ Boolean ⟹ commutative.
- That "thus" hides a real theorem — **every Boolean ring is commutative**. $x = x^2$ forces $2a = 0$; then $(a+b) = (a+b)^2$ gives $ab + ba = 0$, so $ab = ba$. Now that [[Boolean Ring]] exists, it belongs there.
- `[[Idempotence]]` used where you want `[[Idempotence|idempotent]]`; and `## Related` holds a `[!example]` wrapping a link, where Related is a link list.

### 1B — strong

Present and correct: the `Import` idiom, $\forall i \in [w]$, the $q$-ary count $b^w(q-1)^w$, a `### Condition` block naming **both** degenerate cases with their equalities, the Stirling comparison and the $1.44w$ conclusion, the 2-regular definition, count, and the sum-of-two-regulars proposition.

Real gaps:
1. **No `Reference:` header** — eprint 2003/230.
2. `\mathsf{wt}` in the set-builder, `\mathsf{wt}_\mathsf{H}` everywhere else.
3. The 2-regular set-builder drops the `∀ i ∈ [w]` that the regular one has — $i$ is unbound there.
4. The regular count is $q$-ary, the 2-regular count is $\mathbb F_2$-only. Over $\mathbb F_q$ a block has $\binom b2 (q-1)^2$ two-nonzero options — generalise or say you are deferring.
5. **No consumer link.** Nothing connects it to [[Regular Syndrome Decoding Problem]], so the note never says what it is the support set *for*, and it reads as an orphan.
6. The last proposition is my sentence verbatim, not a source's.

### 1C — right shape, three gaps

Correct: no note created, `[!remark] Bridge to Power Set Ring`, $\Delta$, statement on one side with a backlink from the other.

- $\mathrm{supp}$ is introduced **by type only and never defined** — add $\mathrm{supp}(z) := \{i \in [n] : z_i = 1\}$.
- $\mathsf{wt}_\mathsf{H}(z) = |\mathrm{supp}(z)|$ is missing — the identity that ties this to the note it lives in.
- The second operation is written $\cdot$; it is the component-wise product, $\odot$.
- *"Let supp … and the indicator map … are mutually inverse"* — drop "Let".

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


## 1H · Create — `NP Relation`, and the pairing

**Where** `complexity/complexity class/NP Variant/` · **Layout** Property (2) over [[Class NP]] · **Reference** Sipser §7.3; Arora–Barak §2.1

You asked why an NP *language* — a set of strings — gets written as pairs $(x, w)$. [[Class NP]] already states the verifier definition and the $\mathsf{NTIME}$ equivalence, but three things are implicit, and they are the answer.

**Must contain**
- the **two conditions** that make $\mathcal R \subseteq \Sigma^* \times \Sigma^*$ an *NP relation*, each named: **polynomially balanced** ($|w| \leq p(|x|)$) and **polynomial-time decidable** — and one sentence each on what you get if you drop it
- $\mathcal L_\mathcal R := \{x : \exists w,\ (x, w) \in \mathcal R\}$, and that this is a **projection**, so it is many-to-one
- the **pairing** $\langle x, w \rangle$ that [[Class NP]] already uses undefined: a polytime-computable, polytime-invertible encoding $\Sigma^* \times \Sigma^* \to \Sigma^*$
- a `[!remark]` naming where the witness comes from: in the $\mathsf{NTIME}$ direction, $w$ **is the sequence of nondeterministic choices**, written down

**I will check** whether you noticed that $\mathcal R$ is **not determined by** $\mathcal L$ — and drew the consequence: soundness is a statement about $\mathcal L$, knowledge soundness about $\mathcal R$. Then link [[Effective Relation]], which is the same object in crypto clothing and currently connects to none of this.

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

# Assignment 3 · The computability section

[[Computability Theory]] is accurate — I checked the Kolmogorov bounds, the LBA results and the $EQ_\mathsf{TM}$ classification against Sipser and they are right. The work here is **structural**: it is four chapters in one file, with four callouts, **zero wikilinks**, two empty sections, and an `# Note` h1 mid-file.

## Sources — and the trap in mixing them

| use | for |
| --- | --- |
| **Sipser**, *Introduction to the Theory of Computation*, ch. 3–6 | **the primary.** Every symbol in that file is his — $A_\mathsf{TM}$, $HALT_\mathsf{TM}$, $MIN_\mathsf{TM}$, the domino PCP, the `SELF` machine. The file cites nothing; fix that first |
| **Arora–Barak**, *Computational Complexity: A Modern Approach*, ch. 1–2 | the model **as complexity needs it**, the verifier/certificate definition of NP, and the simulation overheads |
| **Li & Vitányi**, *Kolmogorov Complexity and Its Applications* | the `## A Definition of Information` material, if it grows |
| **Turing 1936**, *On Computable Numbers* | the Church–Turing note. §9 is the human-computer analysis and is readable |
| **Copeland**, SEP *"The Church–Turing Thesis"* | the history, and the Extended thesis as a separate claim |

> [!warning] Do not silently merge Sipser and Arora–Barak
> Their machines are **not the same object**. Sipser: one tape, $\Sigma \subseteq \Gamma$, $\delta : Q \times \Gamma \to Q \times \Gamma \times \{L,R\}$. Arora–Barak: a read-only input tape plus $k$ work tapes, and a start symbol $\triangleright$ in the alphabet. Both are fine; a note that takes the tuple from one and a theorem from the other **does not type-check against either**. Say in `Reference:` which parts came from where — this is precision rule 1 applied to sources.

**On your question: yes, use Arora–Barak — but not as the primary here.** It is a complexity book. It compresses computability into roughly one chapter and does not cover enumerators, the Post Correspondence Problem, the recursion theorem, decidability of logical theories, or the recognizable / co-recognizable lattice. Use it where it is strongest — the model with a **cost** attached, and NP — which is exactly the material you are rewriting next.

## 3A · Merge the duplicate — [[Turing Machine]]

**Where** `computability/computing model/` · **Layout** Object (1)

`computing model/Turing Machine.md` exists **and** [[Computability Theory]] defines the 7-tuple again. Same shape as the `Ideal` duplicate: two definitions, and the second one is where people look.

**Must contain** one 7-tuple, and Turing-recognizable / Turing-decidable as `###` derived vocabulary.
**I will check** that [[Computability Theory]] now links rather than restates.

## 3B · Turn three stubs into the note's best object — the **variant table**

`## Multitape`, `## Nondeterministic` and `## Enumerators` each say *"replace the transition function with …"*, then the file remarks *"invariant of Turing machine are equivalence in power"*. **That equivalence is the theorem and three one-line sections bury it.**

**Must contain** one table: variant · transition function · **simulation cost**. The cost column is the point — nondeterministic → deterministic is *exponential*, multitape → single-tape is *quadratic*, and the universal machine costs a log factor. Those numbers are why the model is arbitrary for computability and **not** arbitrary for complexity.
**I will check** the cost column exists and that you drew that conclusion in a `[!remark]`.

## 3C · Fill the empty section — `Church-Turing Thesis`

`## Algorithm` currently contains the words *"Church Turing thesis:"* and nothing else. **Layout** Theorem (12) — except it is not a theorem, which is the content.

**Must contain**
- the three independent formalisations — **general recursive functions** (Gödel/Herbrand 1934), **λ-calculus** (Church 1936), **a-machines** (Turing 1936), plus Post's independent Formulation 1 — and that the *recursive functions came first*
- the equivalences: Church–Kleene 1936, Turing's 1937 appendix
- **why it cannot be proved**: one side of the claim is informal
- why Turing's version persuaded where Church's had not — he gave an *analysis* of the human computer, not another definition
- the **Extended** Church–Turing thesis as a **separate** claim, and that quantum computation is the standing challenge to it (Bernstein–Vazirani 1997) — link `quantum/`

**I will check** that the thesis and the Extended thesis are two statements, not one paragraph.

## 3D · Split the catalogues — `Decidability`

`## Decidability` and `## Undecidability` are two halves of one table, listing nine and seven languages as bare display maths.

**Must contain** one table — language · decidable? · recognizable? · co-recognizable? — plus the two theorems that make the columns non-redundant (*decidable ⟺ recognizable and co-recognizable*; some languages are not recognizable) and $MIN_\mathsf{TM}$ as the witness for the last column.
**I will check** whether the table made you notice which entries you have no proof sketch for.

## 3E · Move and link — `Mapping Reducibility`

Four transfer theorems and their corollaries, and **no link to [[Reductions]]**, which is a live note in `complexity/foundations/`.

**Must contain** $\le_m$, the four transfers, and a `[!remark]` on the relation to polynomial-time reduction: same shape, different resource bound. `Computation history` and `LBA` are stranded under `## Reducibility` with no home — decide where they go.

## 3F · Extract — `Kolmogorov Complexity`

`## A Definition of Information` + `## Incompressible Strings and Randomness`. **Where** you decide — `computability/` or `information theory/`. Argue it.

**Must contain** the five $K$ bounds you already have, the invariance theorem, incompressibility, and — the graded part — a **bridge remark to [[Entropy]]**. They are *different notions*: descriptive complexity of one string versus the entropy of a distribution. Related by a theorem (expected $K$ tracks Shannon entropy up to a constant, for computable sources), **not** by identity.
**I will check** that you wrote the relation as a theorem and not as a synonym. Same trap as `Completeness`.

## 3G · Housekeeping

- `## Post Correspondence Problem` → `computability/problems/`, Problem layout (8)
- `## Decidability of Logical Theories` is five symbols — fill or delete
- delete the `# Note` h1 at the bottom; its four lines are a `[!remark]` in the right notes
- the whole file uses `**Theorem**:` prose. Convert to `[!theorem]` / `[!definition]` — this is what makes it queryable, and it is mechanical enough that **I can do it if you want**


---

## How to hand it back

Commit, then say **"review assignment 1"** or **"review 2A, 2C"** — name whatever you finished. Partial is fine; I mark what is there.
