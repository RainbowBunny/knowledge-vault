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

## 1D · Extend — [[Commitment Scheme]] against Definition 2

**Where** existing note · **Layout** Primitive (5)

Your Definition 2 has $(\mathsf{KeyGen}, \mathsf{Com}, \mathsf{Verif})$ with public parameters $\mathsf{PP}$ and explicit randomness $\rho$; the note's syntax may not match.

**Must contain** the reconciled syntax, then **hiding and binding written as games** in house format.
**I will check** the two things that separate them: hiding is a **distinguishing** game and binding is a **search** game ([[Security Game]]), and each needs its four Condition lines — access, promise, quantifier, adaptivity ([[Note Layouts]] §10).

## 1E · Search before you write — Definitions 3 and 4

**Where** [[Soundness]], [[Knowledge Soundness]], [[Zero Knowledge]] · **Layout** Security property (10)

All three already exist. **Creating new notes here is the wrong answer.**

**Must contain** a short diff, written as a `[!remark]` in each note where the source says something the note does not:
- Definition 3's soundness is stated for **interactive** $\langle P^*, V\rangle(s)$; the notes are non-interactive. Is that a variant or a gap?
- Definition 4's HVZK is $\mathsf{Sim}_\Pi(s) \approx_c \mathsf{View}_V[\langle P(w), V\rangle(s)]$ — it uses **$\mathsf{View}$**, which [[Interactive Proof Systems]] also uses and nothing defines. Fix that here.
- Definition 3 says *"any sufficiently successful prover admits a PPT extractor"* — write out the quantifier.

**I will check** that you created nothing, and that the quantifier in the third bullet came out as $\forall \mathcal A\ \exists \mathcal E$ and not the reverse.

## 1F · Create, and justify the placement — `k-Way Parity Test`

**Where** *you decide* · **Layout** *you decide* · **Reference** your Definition 5

This is the judgement item. It is a randomised procedure with a syntax ($\phi$ in, $\sigma$ out) and a guarantee — so it is arguably a Primitive, arguably a Transform, arguably a Theorem about a test.

**Must contain** the syntax; the fibers $S_j := \phi^{-1}(j)$ and parities $\beta_j$; the parity profile $\sigma$; **and the fact that motivates it** — for $v$ a unit vector the profile is a unit vector, so the test is complete.
**I will check** your placement *argument* more than your placement, and whether you noticed that $\bigoplus_j \beta_j = \mathsf{wt}(v) \bmod 2$, which is the constraint your Definition 6 leans on when it says the last bit is determined.

## 1G · Create — `Single-Product Detector`, and read it critically

**Where** with 1F · **Layout** Security property (10) or Theorem (12) — argue which · **Reference** your Definition 6

**Before you write it, check whether the definition is satisfiable.** Take $v = 0$: every $\beta_j = 0$, so $c = \beta_i\beta_j = 0$. The all-zero profile is not a unit-vector profile, so $v = 0$ is a "non-unit violation" on which $c$ does **not** evaluate to $1$. Same for any $v$ whose $1$s all land in one fiber.

So *"evaluates to 1 on all non-unit violation profiles"* cannot hold as written.

**Must contain** either a corrected statement — most likely a **probability over the random labeling $\phi$**, which is what makes it a test rather than a predicate — or an argument that I have misread the definition.
**I will check** the corrected quantifier, and whether the guarantee ended up in the `### Property` slot as a bound rather than as an absolute claim.

---

## How to hand it back

Commit, then say **"review assignment 1"** — or name the items you finished. Partial is fine; I mark what is there.
