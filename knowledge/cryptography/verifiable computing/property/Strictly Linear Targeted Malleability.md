---
aliases: [SLTM, Linear Targeted Malleability]
---
Reference:
- `[LUNA]` — the source you named for this notion: ePrint 2022/1690 (see [[LUNA]]): https://eprint.iacr.org/2022/1690.pdf. `⚠️ CLAUDE – verify:` I read the PDF text in three passes through a summarizer. The words "targeted malleability" did not occur in what I could read; the only related statement was *Conjecture 1 (HGSW Linear Only)*: "the construction of HGSW is strictly linear-only". The extraction ended inside Theorem 3 and may have lost parts, so this does not show that the definition is absent. Please give me the section or definition number.
- `[BCI+13]` — Bitansky, Chiesa, Ishai, Ostrovsky, Paneth, _Succinct Non-Interactive Arguments via Linear Interactive Proofs_, TCC 2013 (ePrint 2012/718): https://eprint.iacr.org/2012/718.pdf. Read through a summarizer; the excerpt stopped inside Section 5.1.
- `[BSW11]` — Boneh, Segev, Waters, _Targeted Malleability_ (ePrint 2011/311): https://eprint.iacr.org/2011/311.pdf. Cited by `[BCI+13]` as the origin of targeted malleability; not read for this note.
- `#supplemented` marks what I added to your text; its source is on this line. Delete the tag once you have read it.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Strictly Linear Targeted Malleability
> For any adversary $\mathcal A = (\mathcal A_\mathsf{find})$, we define the strictly linear targeted malleability advantage:
> $$\mathsf{Adv}_{}^\mathsf{SLTM}(\mathcal A) = 
\left|\; \Pr\!\left[
\begin{array}{l}
b = 1
\end{array}
\;\middle |\; 
\begin{array}{l}
h
\end{array} \right] 
\;- 
\Pr\!\left[
\begin{array}{l}
b = 1
\end{array}
\;\middle |\; 
\begin{array}{l}
j
\end{array} \right] 
\right|.$$

The callout above is your stub, unchanged (moved here from [[Linear-Only Security]]). It is still incomplete: $h$ and $j$ are the two worlds, and the target is not yet stated.

> [!remark] What the sources say about the notion #supplemented
> - `[BCI+13]` (abstract, §1.3.2) says security can be based on "different forms of linear targeted malleability". The linear-only encryption they describe: given $\mathrm{pk}$ and $\mathsf{Enc}(a_1), \dots, \mathsf{Enc}(a_m)$, the adversary can only produce a valid new ciphertext by evaluating an *affine* function of the given ones, and an extractor $\mathcal E$ (non-uniform in $\mathcal A$) recovers that function $\Pi$. That is the extractor form, written out as a game in [[Linear-Only Security]].
> - They also describe a weaker variant in which "the extractor is replaced by a simulator", which the paper proves secure only against non-adaptive statements. `⚠️ CLAUDE – verify:` your stub compares two worlds, $\Pr[b = 1 \mid h]$ against $\Pr[b = 1 \mid j]$, which looks like this simulator form, but I could not confirm that from the text I read.
> - "Strictly" (no constant term) does not occur in the part of `[BCI+13]` I could read; it is the vocabulary of `[ISW21 Def 3.4, Remark 3.5]`, see [[Linear-Only Security]].

> [!remark] The target of this experiment, as I read your question #supplemented
> `⚠️ CLAUDE – verify:` this is my reading of "experiments with multiple target results", not a statement from a source. Unlike [[Indistinguishability under Chosen-Plaintext Attack]], where the experiment produces one bit, here $\mathcal A$ outputs $k$ ciphertexts $\mathrm{ct}'_1, \dots, \mathrm{ct}'_k$, so the experiment has a vector of results:
>
> | | Game 0 (real) | Game 1 (simulated) |
> | --- | --- | --- |
> | who answers | the challenger decrypts with $\mathrm{sk}$ | a simulator $\mathcal S$ without $\mathrm{sk}$; what exactly it receives is the part I could not source |
> | target | $T_0 = \big(\mathsf{Dec}(\mathrm{sk}, \mathrm{ct}'_i)\big)_{i \in [k]} \in (\mathbb F^\ell \cup \{\perp\})^k$ | $T_1 = \boldsymbol\Pi \cdot [\mathbf v_1 \mid \cdots \mid \mathbf v_m]^\top$ with $\boldsymbol\Pi$ the linear map $\mathcal S$ outputs, and $\perp$ where $\mathcal S$ says the ciphertext is invalid |
>
> The property then compares the targets $T_0$ and $T_1$ (jointly with the plaintexts $\mathbf v_i$, which they depend on) as distributions, by a distinguisher; $h$ and $j$ in the stub would be these two branches and $b$ the distinguisher's output. [[Linear-Only Security]] is the search-game version, where the target is the win bit $\bigvee_i w_i$.

## Related

### Siblings
- [[Linear-Only Security]] — the extractor form, `[ISW21 Def 3.4]`; this note is its simulator-style counterpart
- [[Circuit Privacy]] — the other property asked of the same primitive

### Constructions
- [[LUNA]] — where you found the notion

### Prerequisites
- [[Vector Encryption]], [[Security Game]], [[Adversary]]
