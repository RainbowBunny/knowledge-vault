Reference:
- `[Gro16 x]` — J. Groth, _On the Size of Pairing-Based Non-Interactive Arguments_, EUROCRYPT 2016 (ePrint 2016/260): §2.2 for knowledge soundness, §2.4 and Definition 3 for NILPs: https://eprint.iacr.org/2016/260.pdf
- `[AEAN25 x]` — M. S. Ahmadi, T. Eghlidos, B. Abdolmaleki, N. K. Nguyen, _A Lattice-based Designated Verifier zkSNARK from Standard Assumptions_ (ePrint 2025/2099): https://eprint.iacr.org/2025/2099
- `[GMNO18 x]` — R. Gennaro, M. Minelli, A. Nitulescu, M. Orrù, _Lattice-Based zk-SNARKs from Square Span Programs_, ACM CCS 2018 (ePrint 2018/275): https://eprint.iacr.org/2018/275.pdf
- `[A]` — Alinush, _Zero-Knowledge Proofs_, section "Algorithms": https://alinush.github.io/zkps
- All four were read through a summarizer, not verbatim; check the wording before quoting.

## Definition

> [!remark]
> Knowledge Soundness means to proof a statement, you need to know the witness.

### Non-Interactive Proof Systems Variant

> [!definition] Parameters
> - [[Non-Interactive Proof Systems]]: Import $(\lambda, \mathsf{Setup}, \mathsf{Verify})$, with $(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$ and $\mathsf{Verify}(\mathcal R, \mathrm{vk}, \mathbf x, \pi) \in \{0, 1\}$.
> - [[Relation Generator]] $\mathcal G$: $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$; the relation $\mathcal R$ is public, the auxiliary input $z$ goes to the adversary and to the extractor.
> - $\mathbf x$: the statement and $\pi$: the proof output by the adversary. $\mathbf w$: the witness output by the extractor.
> - $\mathcal E_\mathcal A$: the extractor, a non-uniform PPT algorithm that may depend on $\mathcal A$. $r_\mathcal A$: the random tape of $\mathcal A$.
> - $\mathbb A$: the class of non-uniform PPT [[Adversary|adversaries]].

> [!definition] Adaptive Knowledge Soundness
> ### Scope
> A [[Non-Interactive Proof Systems|non-interactive proof system]] $\Pi_\mathsf{NIPS}$, a relation generator $\mathcal G$, the adversary class $\mathbb A$ and, for each $\mathcal A$, an extractor $\mathcal E_\mathcal A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $(\mathcal R, z, \mathrm{prk})$, and $\mathrm{vk}$ when the system is publicly verifiable; never $\mathrm{td}$. No oracle. $\mathcal E_\mathcal A$ receives the same input together with the random tape $r_\mathcal A$.
> - **Promise** — none.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A\ \exists \mathcal E_\mathcal A$: the extractor is chosen after the adversary and may depend on it.
> - **Adaptivity** — adaptive: $\mathcal A$ chooses the statement $\mathbf x$ after seeing the output of $\mathsf{Setup}$.
>
> ---
> ### Experiment
> A search game with one branch; the challenger runs the extractor after $\mathcal A$ has spoken. `[Gro16 §2.2]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$<br>$(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$ | $\xrightarrow{\ \mathcal R,\, z,\, \mathrm{prk},\, \mathrm{vk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x,\, \pi\ }$ | outputs a statement $\mathbf x$ and a proof $\pi$ |
> | 3 | $\mathbf w \leftarrow \mathcal E_\mathcal A(\mathcal R, z, \mathrm{prk}, \mathrm{vk}, r_\mathcal A)$<br>$b \leftarrow \mathsf{Verify}(\mathcal R, \mathrm{vk}, \mathbf x, \pi)$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $b = 1$: the proof is accepted;
> - $(\mathbf x, \mathbf w) \notin \mathcal R$: the extracted value is not a witness.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{ks}}_{\mathsf{NIPS}}(\mathcal A, \mathcal E_\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
> - $\Pi_\mathsf{NIPS}$ is **computationally knowledge sound** if for every $\mathcal A \in \mathbb A$ there is an $\mathcal E_\mathcal A$ with $\mathsf{Adv}^{\mathsf{ks}}_{\mathsf{NIPS}}(\mathcal A, \mathcal E_\mathcal A)$ negligible in $\lambda$ `[Gro16 §2.2]`.
>
> It is a *search* game, see [[Security Game]].

> [!remark] The extractor sees what the adversary sees
> $\mathcal E_\mathcal A$ receives the input and the random tape of $\mathcal A$ `[Gro16 §2.2]`, so it can re-run $\mathcal A$ and knows the pair $(\mathbf x, \pi)$ of row 2 without being sent it; this is why row 3 gives it no $\mathbf x$. It still gets nothing $\mathcal A$ does not have: no $\mathrm{td}$, and no $\mathrm{vk}$ when $\mathrm{vk}$ is secret.
>
> Adaptivity is still a real choice: in a **non-adaptive** variant $\mathcal A$ commits to $\mathbf x$ before $\mathsf{Setup}$, as in [[Soundness#Non-Interactive Proof Systems Variant|non-adaptive soundness]]. `[AEAN25]` uses both terms, but describes the non-adaptive one in prose only.

> [!remark] Notation in the literature
> - `[Gro16 §2.2]` writes the extractor $\chi_\mathcal A$ and the experiment $((\phi, \pi); w) \leftarrow (\mathcal A \Vert \chi_\mathcal A)(R, z, \sigma)$: both run on the same input, and $\chi_\mathcal A$ also gets the random coins of $\mathcal A$. Here the pair is split into row 2 ($\mathcal A$) and row 3 ($\mathcal E_\mathcal A$), with the coins $r_\mathcal A$ as an explicit input.
> - `[A]` has the same definition with $(\mathcal A \Vert \mathcal X_\mathcal A)(\mathrm{prk}, \mathrm{vk}, R, \mathrm{aux})$, and notes that the generator must be *benign*; see [[Relation Generator]].
> - `[AEAN25 Def 6]` reverses the quantifiers: one expected-PPT extractor $E$ for every stateful PPT prover, with input $(R, \mathrm{crs}, \pi)$ and black-box access to the prover, which it may rewind; the bound is $\varepsilon(\lambda) + \mathsf{negl}(\lambda)$.
> - `[GMNO18 Def 5]` is designated-verifier: $\mathcal A$ and its extractor get $\mathrm{crs}$ and a verification oracle $V(\mathrm{vrs}, \cdot, \cdot)$ (*strong soundness*, `[GMNO18 Remark 6]`).

### Against Affine Prover Strategies Variant

> [!definition] Parameters
> - [[Non-Interactive Linear Proofs]]: Import $(\mathbb F, m, k, \mathsf{Setup}, \mathsf{Verify})$, with $(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal R)$, $\mathrm{crs} \in \mathbb F^m$ containing the entry $1$, and $\mathsf{Verify}(\mathcal R, \mathrm{crs}, \mathbf x, \pi)$.
> - [[Relation Generator]] $\mathcal G$: $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$.
> - $\boldsymbol\Pi$: the proof matrix output by the adversary; the proof is $\pi = \boldsymbol\Pi \cdot \mathrm{crs}$.
> - $\mathcal E$: the extractor, one PPT algorithm for all adversaries. $\mathbf w$: its output.
> - $\mathbb A$: all [[Adversary|adversaries]], with no bound on their running time.

> [!definition] Knowledge Soundness against Affine Prover Strategies
> ### Scope
> A [[Non-Interactive Linear Proofs|non-interactive linear proof]] $\Pi_\mathsf{NILP}$, a relation generator $\mathcal G$, the adversary class $\mathbb A$ and an extractor $\mathcal E$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $(\mathcal R, z)$ only: neither $\mathrm{crs}$ nor $\mathrm{st}$. Its proof is the fixed matrix $\boldsymbol\Pi$ applied to $\mathrm{crs}$. $\mathcal E$ receives $(\mathcal R, \mathbf x, \boldsymbol\Pi)$.
> - **Promise** — none.
> - **Quantifier** — $\exists \mathcal E\ \forall \mathcal A \in \mathbb A$: one extractor works for every adversary.
> - **Adaptivity** — none: $\mathcal A$ sees nothing that depends on $\mathsf{Setup}$.
>
> ---
> ### Experiment
> A search game with one branch. `[Gro16 Def 3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$<br>$(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal R)$ | $\xrightarrow{\ \mathcal R,\, z\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x,\, \boldsymbol\Pi\ }$ | outputs a statement $\mathbf x$ and a matrix $\boldsymbol\Pi$ |
> | 3 | $\mathbf w \leftarrow \mathcal E(\mathcal R, \mathbf x, \boldsymbol\Pi)$<br>$\pi \leftarrow \boldsymbol\Pi \cdot \mathrm{crs}$<br>$b \leftarrow \mathsf{Verify}(\mathcal R, \mathrm{crs}, \mathbf x, \pi)$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $\boldsymbol\Pi \in \mathbb F^{k \times m}$;
> - $b = 1$;
> - $(\mathbf x, \mathbf w) \notin \mathcal R$.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{ks}\text{-}\mathsf{aff}}_{\mathsf{NILP}}(\mathcal A, \mathcal E) = \Pr[\mathcal A \text{ wins}].$$
> - $\Pi_\mathsf{NILP}$ has **statistical knowledge soundness against affine prover strategies** if there is a PPT $\mathcal E$ such that $\mathsf{Adv}^{\mathsf{ks}\text{-}\mathsf{aff}}_{\mathsf{NILP}}(\mathcal A, \mathcal E)$ is negligible for every $\mathcal A \in \mathbb A$ `[Gro16 Def 3]`.
>
> It is a *search* game, see [[Security Game]].

> [!remark] Why affine, and why no $\mathrm{crs}$
> - Because $\mathrm{crs}$ contains the entry $1$, the proof $\boldsymbol\Pi \cdot \mathrm{crs}$ is an affine function of the other entries: an affine prover strategy.
> - $\mathcal A$ does not see $\mathrm{crs}$ in `[Gro16 Def 3]`: the strategy is a fixed matrix, chosen independently of the setup.
> - `[Gro16 §2.4]` writes $(\sigma, \tau) \leftarrow \mathsf{Setup}(R)$ with $\sigma \in \mathbb F^m$, $\tau \in \mathbb F^n$, and the extractor $\mathcal X$.

## Related

### Properties
- [[Soundness]] — implied: an accepted proof of $\mathbf x \notin \mathcal L_\mathcal R$ wins the game above for any extractor
- [[Linear-Only Security]], [[Strictly Linear Targeted Malleability]] — encryption properties used to compile a linear proof system into an argument; see those notes

### Prerequisites
- [[Non-Interactive Proof Systems]], [[Non-Interactive Linear Proofs]], [[Relation Generator]], [[Security Game]], [[Adversary]]
