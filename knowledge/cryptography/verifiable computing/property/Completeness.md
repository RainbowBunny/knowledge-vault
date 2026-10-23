Reference:
- `[Gro16 x]` — J. Groth, _On the Size of Pairing-Based Non-Interactive Arguments_, EUROCRYPT 2016 (ePrint 2016/260), §2.2: https://eprint.iacr.org/2016/260.pdf
- `[GMNO18 x]` — R. Gennaro, M. Minelli, A. Nitulescu, M. Orrù, _Lattice-Based zk-SNARKs from Square Span Programs_, ACM CCS 2018 (ePrint 2018/275): https://eprint.iacr.org/2018/275.pdf
- `[A]` — Alinush, _Zero-Knowledge Proofs_, section "Algorithms": https://alinush.github.io/zkps
- All three were read through a summarizer, not verbatim; check the wording before quoting.

## Definition

> [!remark]
> Completeness means a true statement can be proven.

### Non-Interactive Proof Systems Variant

> [!definition] Parameters
> - [[Non-Interactive Proof Systems]]: Import $(\lambda, \mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify})$, with $(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$, $\pi \leftarrow \mathsf{Prove}(\mathcal R, \mathrm{prk}, \mathbf x, \mathbf w)$ and $\mathsf{Verify}(\mathcal R, \mathrm{vk}, \mathbf x, \pi) \in \{0, 1\}$.
> - [[Relation Generator]]: Import $(\mathcal R_\lambda)$, the set of relations the generator can output; $\mathcal R \in \mathcal R_\lambda$ is public.
> - $\mathbf x$: a statement. $\mathbf w$: a witness. $\pi$: a proof.
> - $\mathbb A$: the class of [[Adversary|adversaries]]. $\varepsilon_c$: the completeness error.

> [!definition] Completeness of Non-Interactive Proof System
> ### Scope
> A [[Non-Interactive Proof Systems|non-interactive proof system]] $\Pi_\mathsf{NIPS} = (\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify})$ for the relations in $\mathcal R_\lambda$, and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathcal R$ and $\mathrm{prk}$, and $\mathrm{vk}$ when the system is publicly verifiable; never $\mathrm{td}$. No oracle. In the designated-verifier setting of `[GMNO18 Def 4]` it receives the proving key only.
> - **Promise** — none: $\mathcal A$ may send any pair, but only a pair in $\mathcal R$ can make it win.
> - **Quantifier** — $\forall \lambda$, $\forall \mathcal R \in \mathcal R_\lambda$, $\forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — $\mathcal A$ chooses $(\mathbf x, \mathbf w)$ after seeing the output of $\mathsf{Setup}$.
>
> ---
> ### Experiment
> A search game with one branch: $\mathcal A$ looks for a true statement whose honest proof is rejected. `[GMNO18 Def 4]`, with the relation quantified as in `[Gro16 §2.2]`.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$ | $\xrightarrow{\ \mathcal R,\, \mathrm{prk},\, \mathrm{vk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x,\, \mathbf w\ }$ | chooses a statement $\mathbf x$ and a witness $\mathbf w$ |
> | 3 | $\pi \leftarrow \mathsf{Prove}(\mathcal R, \mathrm{prk}, \mathbf x, \mathbf w)$<br>$b \leftarrow \mathsf{Verify}(\mathcal R, \mathrm{vk}, \mathbf x, \pi)$ | | |
>
> **Goal** — $\mathcal A$ wins iff all of:
> - $(\mathbf x, \mathbf w) \in \mathcal R$;
> - $b = 0$: the honest proof is rejected.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{cmp}}_{\mathsf{NIPS}}(\mathcal A) = \Pr[\mathcal A \text{ wins}].$$
> - $\Pi_\mathsf{NIPS}$ has **completeness error $\varepsilon_c$** if $\mathsf{Adv}^{\mathsf{cmp}}_{\mathsf{NIPS}}(\mathcal A) \leq \varepsilon_c$ for every $\mathcal A \in \mathbb A$.
> - $\Pi_\mathsf{NIPS}$ is **complete** if the advantage is negligible in $\lambda$ for every PPT $\mathcal A$ `[GMNO18 Def 4]`, and **perfectly complete** if it is $0$ for every $\mathcal A$.
>
> It is a *search* game, see [[Security Game]].

> [!remark] Notation in the literature
> - `[GMNO18 Def 4]` writes the system as $\Pi = (G, P, V)$ with $(\mathrm{crs}, \mathrm{vrs}, \mathrm{td}) \leftarrow G(1^\lambda, R)$ for a fixed relation; its adversary $\mathcal A(\mathrm{crs})$ outputs $(u, w)$, and the game returns $V(\mathrm{vrs}, u, \pi) = \mathsf{false} \wedge R(u, w)$. A fixed relation is the case $\mathcal R_\lambda = \{\mathcal R\}$ here.
> - `[Gro16 §2.2]` and `[A]` define completeness without an adversary, for every pair in the relation: the Variant below.

## Variant

### Perfect completeness for every statement

> [!definition] Perfect Completeness `[Gro16 §2.2]` `[A]`
> For every $\lambda$, every $\mathcal R \in \mathcal R_\lambda$ and every $(\mathbf x, \mathbf w) \in \mathcal R$, the experiment
> - $(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$
> - $\pi \leftarrow \mathsf{Prove}(\mathcal R, \mathrm{prk}, \mathbf x, \mathbf w)$
>
> ends with $\mathsf{Verify}(\mathcal R, \mathrm{vk}, \mathbf x, \pi) = 1$ with probability $1$.

> [!remark] It has no adversary
> The pair $(\mathbf x, \mathbf w)$ is quantified, not chosen, so this is a correctness condition and not a game ([[Note Layouts]] § Security property, "Where it stops").
> - With probability exactly $1$ it is equivalent to the game above with $\mathsf{Adv}^{\mathsf{cmp}} = 0$: every output of $\mathsf{Setup}$ then accepts every honest proof, so no choice made after seeing it can fail.
> - With an error $\varepsilon_c > 0$ the game is the stronger notion, because $\mathcal A$ picks $(\mathbf x, \mathbf w)$ after seeing $\mathrm{prk}$ and may aim at the setups where the error sits.
> - `[A]` notes that the probability $1$ may be relaxed to $1 - \mathsf{negl}(\lambda)$.

## Related

### Properties
- [[Soundness]], [[Knowledge Soundness]] — the other side: a false statement, or one without a known witness, cannot be proven

### Prerequisites
- [[Non-Interactive Proof Systems]], [[Relation Generator]], [[Security Game]], [[Adversary]]
