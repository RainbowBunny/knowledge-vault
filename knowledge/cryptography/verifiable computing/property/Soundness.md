Reference:
- `[Gro16 x]` — J. Groth, _On the Size of Pairing-Based Non-Interactive Arguments_, EUROCRYPT 2016 (ePrint 2016/260), §2.2: https://eprint.iacr.org/2016/260.pdf
- `[BCI+13 x]` — N. Bitansky, A. Chiesa, Y. Ishai, R. Ostrovsky, O. Paneth, _Succinct Non-Interactive Arguments via Linear Interactive Proofs_, TCC 2013; numbers refer to the full version, ePrint 2012/718: https://eprint.iacr.org/2012/718.pdf
- `[GMNO18 x]` — R. Gennaro, M. Minelli, A. Nitulescu, M. Orrù, _Lattice-Based zk-SNARKs from Square Span Programs_, ACM CCS 2018 (ePrint 2018/275): https://eprint.iacr.org/2018/275.pdf
- `[BISW17]` — D. Boneh, Y. Ishai, A. Sahai, D. J. Wu, _Lattice-Based SNARGs and Their Application to More Efficient Obfuscation_, EUROCRYPT 2017 (ePrint 2017/240): https://eprint.iacr.org/2017/240 — cited here only through `[GMNO18 Remark 6]`.
- The first three were read through a summarizer, not verbatim; check the wording before quoting.

## Definition

> [!remark] Soundness
> Soundness means false statement can not be proven.

### Non-Interactive Proof Systems Variant

> [!definition] Parameters
> - [[Non-Interactive Proof Systems]]: Import $(\lambda, \mathsf{Setup}, \mathsf{Verify})$, with $(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$ and $\mathsf{Verify}(\mathcal R, \mathrm{vk}, \mathbf x, \pi) \in \{0, 1\}$.
> - [[Relation Generator]] $\mathcal G$: $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$; the relation $\mathcal R$ is public, the auxiliary input $z$ goes to the adversary. $\mathcal L_\mathcal R$: the language of $\mathcal R$.
> - $\mathbf x$: the statement and $\pi$: the proof, both output by the adversary.
> - $\mathbb A$: the class of [[Adversary|adversaries]] — non-uniform PPT for computational soundness, unbounded for statistical soundness.

> [!definition] Non-Adaptive Soundness
> ### Scope
> A [[Non-Interactive Proof Systems|non-interactive proof system]] $\Pi_\mathsf{NIPS}$, a relation generator $\mathcal G$ and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $(\mathcal R, z)$, then $\mathrm{prk}$, and $\mathrm{vk}$ when the system is publicly verifiable; never $\mathrm{td}$. No oracle.
> - **Promise** — none; a true statement cannot make $\mathcal A$ win.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — non-adaptive: $\mathcal A$ commits to $\mathbf x$ before $\mathsf{Setup}$ runs, and chooses $\pi$ after seeing its output.
>
> ---
> ### Experiment
> A search game with one branch. `[BCI+13 Def 4.2]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$ | $\xrightarrow{\ \mathcal R,\, z\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x\ }$ | chooses a statement $\mathbf x$ |
> | 3 | $(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$ | $\xrightarrow{\ \mathrm{prk},\, \mathrm{vk}\ }$ | |
> | 4 | | $\xleftarrow{\ \pi\ }$ | outputs a proof $\pi$ |
> | 5 | $b \leftarrow \mathsf{Verify}(\mathcal R, \mathrm{vk}, \mathbf x, \pi)$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $\mathbf x \notin \mathcal L_\mathcal R$;
> - $b = 1$.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{snd}\text{-}\mathsf{na}}_{\mathsf{NIPS}}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
> - $\Pi_\mathsf{NIPS}$ is **non-adaptively sound** if $\mathsf{Adv}^{\mathsf{snd}\text{-}\mathsf{na}}_{\mathsf{NIPS}}(\mathcal A)$ is negligible in $\lambda$ for every $\mathcal A \in \mathbb A$ `[BCI+13 Def 4.2]`.
>
> It is a *search* game, see [[Security Game]].

> [!definition] Parameters
> - As for Non-Adaptive Soundness: $\lambda$, $\mathsf{Setup}$, $\mathsf{Verify}$, $\mathcal G$, $\mathcal R$, $z$, $\mathcal L_\mathcal R$, $\mathrm{prk}$, $\mathrm{vk}$, $\mathrm{td}$, $\mathbf x$, $\pi$, $\mathbb A$.

> [!definition] Adaptive Soundness
> ### Scope
> A [[Non-Interactive Proof Systems|non-interactive proof system]] $\Pi_\mathsf{NIPS}$, a relation generator $\mathcal G$ and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $(\mathcal R, z, \mathrm{prk})$, and $\mathrm{vk}$ when the system is publicly verifiable; never $\mathrm{td}$. No oracle.
> - **Promise** — none.
> - **Quantifier** — $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — adaptive: $\mathcal A$ chooses the statement $\mathbf x$ after seeing the output of $\mathsf{Setup}$.
>
> ---
> ### Experiment
> A search game with one branch. `[Gro16 §2.2]`, `[BCI+13 Def 4.2]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$<br>$(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$ | $\xrightarrow{\ \mathcal R,\, z,\, \mathrm{prk},\, \mathrm{vk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x,\, \pi\ }$ | outputs a statement $\mathbf x$ and a proof $\pi$ |
> | 3 | $b \leftarrow \mathsf{Verify}(\mathcal R, \mathrm{vk}, \mathbf x, \pi)$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $\mathbf x \notin \mathcal L_\mathcal R$;
> - $b = 1$.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{snd}\text{-}\mathsf{a}}_{\mathsf{NIPS}}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
> - $\Pi_\mathsf{NIPS}$ is **computationally sound** if $\mathsf{Adv}^{\mathsf{snd}\text{-}\mathsf{a}}_{\mathsf{NIPS}}(\mathcal A)$ is negligible in $\lambda$ for every non-uniform PPT $\mathcal A$ `[Gro16 §2.2]`; it is then an *argument* ([[Argument Systems]]).
> - It is **statistically sound** if the advantage is negligible for every unbounded $\mathcal A$; it is then a *proof*. See the rows of [[Security Game]].
>
> It is a *search* game, see [[Security Game]].

> [!remark] Adaptive implies non-adaptive
> An adversary for the non-adaptive game plays the adaptive game as well: it chooses $\mathbf x$ from $(\mathcal R, z)$ alone, ignores $\mathrm{prk}$ while doing so, and sends $\mathbf x$ together with its proof in row 2. So adaptive soundness implies non-adaptive soundness.

> [!remark] Notation in the literature
> - `[Gro16 §2.2]` writes $(\sigma, \tau) \leftarrow \mathsf{Setup}(R)$, $\phi$ for the statement and $\mathsf{Vfy}$ for $\mathsf{Verify}$; its adversary is $\mathcal A(R, z, \sigma)$ returning $(\phi, \pi)$. Here $\sigma$ is $(\mathrm{prk}, \mathrm{vk})$ and $\tau$ is $\mathrm{td}$.
> - `[BCI+13 Def 4.2]` has no relation generator: $(\sigma, \tau) \leftarrow G(1^\lambda, T)$ for the universal relation, with a verification state $\tau$ that may be secret and a cheating prover $P^*$. Non-adaptive soundness quantifies over every false statement $y$ and runs $P^*(\sigma, y)$; adaptive soundness runs $P^*(\sigma)$, which outputs $(y, \pi)$. Here the quantified $y$ becomes the choice of $\mathcal A$ in row 2, made after $(\mathcal R, z)$ and before $\mathsf{Setup}$; a fixed relation is the trivial generator of [[Relation Generator]].

> [!remark] Designated verifier
> When $\mathrm{vk}$ must stay secret, as in [[LUNA]], the challenger sends $\mathrm{prk}$ only: $P^*$ sees $\sigma$ and never $\tau$ in `[BCI+13 Def 4.2]`. A stronger notion also gives $\mathcal A$ a verification oracle $\mathsf{Verify}(\mathcal R, \mathrm{vk}, \cdot, \cdot)$, so that $\mathrm{vk}$ can be reused across many proofs; `[GMNO18 Remark 6]` calls it *strong soundness*, after `[BISW17]`.

## Related

### Properties
- [[Knowledge Soundness]] — stronger: an accepted proof for $\mathbf x \notin \mathcal L_\mathcal R$ is an accepted proof for which no witness can be extracted
- [[Completeness]] — the honest side

### Prerequisites
- [[Non-Interactive Proof Systems]], [[Relation Generator]], [[Security Game]], [[Adversary]]
