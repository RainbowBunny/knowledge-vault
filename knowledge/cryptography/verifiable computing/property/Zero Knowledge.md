Reference:
- `[Gro16 x]` — J. Groth, _On the Size of Pairing-Based Non-Interactive Arguments_, EUROCRYPT 2016 (ePrint 2016/260), §2.2: https://eprint.iacr.org/2016/260.pdf
- `[BCI+13 x]` — N. Bitansky, A. Chiesa, Y. Ishai, R. Ostrovsky, O. Paneth, _Succinct Non-Interactive Arguments via Linear Interactive Proofs_, TCC 2013; numbers refer to the full version, ePrint 2012/718: https://eprint.iacr.org/2012/718.pdf
- `[GMNO18 x]` — R. Gennaro, M. Minelli, A. Nitulescu, M. Orrù, _Lattice-Based zk-SNARKs from Square Span Programs_, ACM CCS 2018 (ePrint 2018/275): https://eprint.iacr.org/2018/275.pdf
- `[A]` — Alinush, _Zero-Knowledge Proofs_, section "Algorithms": https://alinush.github.io/zkps
- `[ISW21 x]` — Y. Ishai, H. Su, D. J. Wu, _Shorter and Faster Post-Quantum Designated-Verifier zkSNARKs from Lattices_, ACM CCS 2021 (ePrint 2021/977): https://eprint.iacr.org/2021/977.pdf
- All five were read through a summarizer, not verbatim; check the wording before quoting.

## Definition

### Non-Interactive Proof System

> [!definition] Parameters
> - [[Non-Interactive Proof Systems]]: Import $(\lambda, \mathsf{Setup}, \mathsf{Prove})$, with $(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$ and $\pi \leftarrow \mathsf{Prove}(\mathcal R, \mathrm{prk}, \mathbf x, \mathbf w)$.
> - $\mathsf{Sim}$: the simulator, $\pi \leftarrow \mathsf{Sim}(\mathcal R, \mathrm{td}, \mathbf x)$ — a proof from the trapdoor and the statement, without a witness.
> - [[Relation Generator]] $\mathcal G$: $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$; the relation $\mathcal R$ is public, the auxiliary input $z$ goes to the adversary.
> - $\mathbf x$: the statement; $\mathbf w$: the witness. $b'$: the bit output by the adversary.
> - $\mathbb A$: the class of [[Adversary|adversaries]] — unbounded for perfect and statistical zero knowledge, PPT for computational.

> [!definition] Zero-Knowledge
> ### Scope
> A [[Non-Interactive Proof Systems|non-interactive proof system]] $\Pi_\mathsf{NIPS}$ with its simulator $\mathsf{Sim}$, a relation generator $\mathcal G$ and the adversary class $\mathbb A$ of Parameters.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $(\mathcal R, z)$; after choosing its statement it receives everything $\mathsf{Setup}$ output — $\mathrm{prk}$, $\mathrm{vk}$ **and** $\mathrm{td}$ — and the challenge proof. No oracle.
> - **Promise** — $(\mathbf x, \mathbf w) \in \mathcal R$.
> - **Quantifier** — $\exists \mathsf{Sim}\ \forall \mathcal A \in \mathbb A$: the simulator is part of the scheme, fixed before the adversary.
> - **Adaptivity** — $\mathcal A$ chooses $(\mathbf x, \mathbf w)$ after seeing $(\mathcal R, z)$ and before $\mathsf{Setup}$ runs. One statement.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in row 3 only, **Game 0** (real proof) and **Game 1** (simulated proof). `[Gro16 §2.2]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$ | $\xrightarrow{\ \mathcal R,\, z\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x,\, \mathbf w\ }$ | chooses $(\mathbf x, \mathbf w) \in \mathcal R$ |
> | 3 | $(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$<br>**Game 0**: $\pi \leftarrow \mathsf{Prove}(\mathcal R, \mathrm{prk}, \mathbf x, \mathbf w)$<br>**Game 1**: $\pi \leftarrow \mathsf{Sim}(\mathcal R, \mathrm{td}, \mathbf x)$ | $\xrightarrow{\ \mathrm{prk},\, \mathrm{vk},\, \mathrm{td},\, \pi\ }$ | |
> | 4 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$: $\mathcal A$ is the distinguisher of its view $(\mathcal R, z, \mathrm{prk}, \mathrm{vk}, \mathrm{td}, \pi)$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{zk}}_{\mathsf{NIPS}}(\mathcal A) = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
> - $\Pi_\mathsf{NIPS}$ is **perfectly zero-knowledge** if $\mathsf{Adv}^{\mathsf{zk}}_{\mathsf{NIPS}}(\mathcal A) = 0$ for every $\mathcal A$ `[Gro16 §2.2]`.
> - It is **statistically** (resp. **computationally**) zero-knowledge if the advantage is negligible in $\lambda$ for every unbounded (resp. PPT) $\mathcal A$; see the rows of [[Security Game]].
>
> It is a *distinguishing* game, see [[Security Game]].

> [!remark] Notation in the literature
> - `[Gro16 §2.2]` writes $(\sigma, \tau) \leftarrow \mathsf{Setup}(R)$ and $\mathsf{Sim}(R, \tau, \phi)$, and asks that for all $\lambda$, all $(R, z)$ output by the generator, all $(\phi, w) \in R$ and all $\mathcal A$, $\Pr[\mathcal A(R, z, \sigma, \tau, \pi) = 1]$ is the same with $\pi$ from $\mathsf{Prove}$ and from $\mathsf{Sim}$. Here the quantified pair becomes the choice of $\mathcal A$ in row 2. For perfect zero knowledge the two forms agree, since an adversary may hard-wire any pair.
> - `[A]` states the same definition with $\mathcal A(\mathrm{prk}, \mathrm{vk}, \mathrm{td}, \mathrm{aux}; \pi)$.
> - Since $\mathcal A$ receives $\mathrm{td}$, the proof hides $\mathbf w$ even from whoever knows the trapdoor.

> [!remark]
> There is a Leakage variant.

## Variant

### Adaptive statement and simulated setup

> [!definition] Parameters
> - As above: $\lambda$, $\mathsf{Setup}$, $\mathsf{Prove}$, $\mathcal G$, $\mathcal R$, $z$, $\mathbf x$, $\mathbf w$, $b'$, $\mathbb A$ (here polynomial-size).
> - $\mathcal S$: the simulator, one stateful polynomial-size algorithm called twice — first in place of $\mathsf{Setup}$, then in place of $\mathsf{Prove}$. $\mathrm{trap}$: the trapdoor it keeps.

> [!definition] Adaptive Zero-Knowledge with Simulated Setup
> ### Scope
> A [[Non-Interactive Proof Systems|non-interactive proof system]] $\Pi_\mathsf{NIPS}$, a relation generator $\mathcal G$, the adversary class $\mathbb A$ and a simulator $\mathcal S$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $(\mathcal R, z, \mathrm{prk})$, then the challenge proof; not $\mathrm{vk}$, $\mathrm{td}$ or $\mathrm{trap}$. No oracle.
> - **Promise** — $(\mathbf x, \mathbf w) \in \mathcal R$.
> - **Quantifier** — $\exists \mathcal S\ \forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — adaptive: $\mathcal A$ chooses $(\mathbf x, \mathbf w)$ after seeing $\mathrm{prk}$. One statement.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in rows 1 and 3, **Game 0** (real setup and proof) and **Game 1** (simulated setup and proof). `[BCI+13 Def 4.4]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$<br>**Game 0**: $(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$<br>**Game 1**: $(\mathrm{prk}, \mathrm{vk}, \mathrm{trap}) \leftarrow \mathcal S(\mathcal R)$ | $\xrightarrow{\ \mathcal R,\, z,\, \mathrm{prk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x,\, \mathbf w\ }$ | chooses $(\mathbf x, \mathbf w) \in \mathcal R$ |
> | 3 | **Game 0**: $\pi \leftarrow \mathsf{Prove}(\mathcal R, \mathrm{prk}, \mathbf x, \mathbf w)$<br>**Game 1**: $\pi \leftarrow \mathcal S(z, \mathrm{prk}, \mathbf x, \mathrm{trap})$ | $\xrightarrow{\ \pi\ }$ | |
> | 4 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{azk}}_{\mathsf{NIPS}}(\mathcal A, \mathcal S) = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
> - `[BCI+13 Def 4.4]` asks for $\mathsf{Adv}^{\mathsf{azk}}_{\mathsf{NIPS}}(\mathcal A, \mathcal S) = 0$ for every $\mathcal A$ (perfect zero knowledge), and notes that this can be relaxed to statistical or computational closeness.

> [!remark] Notation in the literature
> `[BCI+13 Def 4.4]` has no relation generator: $(\sigma, \tau) \leftarrow G(1^\lambda, T)$ in the real experiment and $(\sigma, \tau, \mathrm{trap}) \leftarrow S(1^\lambda, T)$ in the simulated one, with a stateful distinguisher $D(z, \sigma)$ that outputs $(y, w)$, then receives $\pi$, and $\pi \leftarrow S(z, \sigma, y, \mathrm{trap})$; the experiment counts only when $(y, w)$ is in the relation, and $D$ never sees $\tau$. The split $\mathcal S = (\mathcal S_\mathsf{setup}, \mathcal S_\mathsf{prove})$ is the same machine called twice. Here $\sigma$ is $\mathrm{prk}$, $\tau$ is $\mathrm{vk}$, and $D$ is the stateful adversary $\mathcal A$.

### Many statements: a prover oracle

> [!definition] Parameters
> - As in the Definition: $\lambda$, $\mathsf{Setup}$, $\mathsf{Prove}$, $\mathsf{Sim}$, $\mathcal G$, $\mathcal R$, $z$, $\mathbf x$, $\mathbf w$, $b'$; $\mathbb A$: PPT adversaries.

> [!definition] Zero-Knowledge with a Prover Oracle
> ### Scope
> A [[Non-Interactive Proof Systems|non-interactive proof system]] $\Pi_\mathsf{NIPS}$ with its simulator $\mathsf{Sim}$, a relation generator $\mathcal G$ and the adversary class $\mathbb A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $(\mathcal R, z, \mathrm{prk}, \mathrm{vk})$ — the verification key too, even in the designated-verifier setting — but not $\mathrm{td}$; and a prover oracle that answers $\perp$ on a pair outside $\mathcal R$.
> - **Promise** — none: the oracle enforces $(\mathbf x, \mathbf w) \in \mathcal R$.
> - **Quantifier** — $\exists \mathsf{Sim}\ \forall \mathcal A \in \mathbb A$.
> - **Adaptivity** — queries are adaptive, after $\mathrm{prk}$ and $\mathrm{vk}$ are seen; polynomially many statements.
>
> ---
> ### Experiment
> A distinguishing game: two branches that differ in the answer to each query, **Game 0** (real prover) and **Game 1** (simulator). `[GMNO18 Def 7]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathcal R, z) \leftarrow \mathcal G(1^\lambda)$<br>$(\mathrm{prk}, \mathrm{vk}, \mathrm{td}) \leftarrow \mathsf{Setup}(\mathcal R)$ | $\xrightarrow{\ \mathcal R,\, z,\, \mathrm{prk},\, \mathrm{vk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathbf x,\, \mathbf w\ }$ | **Prove queries** (repeated, adaptive, polynomially many times): sends a statement $\mathbf x$ and a witness $\mathbf w$ |
> | | if $(\mathbf x, \mathbf w) \notin \mathcal R$: $\pi \leftarrow \perp$<br>**Game 0**: otherwise $\pi \leftarrow \mathsf{Prove}(\mathcal R, \mathrm{prk}, \mathbf x, \mathbf w)$<br>**Game 1**: otherwise $\pi \leftarrow \mathsf{Sim}(\mathcal R, \mathrm{td}, \mathbf x)$ | $\xrightarrow{\ \pi\ }$ | |
> | 3 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{zk}\text{-}\mathsf{or}}_{\mathsf{NIPS}}(\mathcal A) = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
> - $\Pi_\mathsf{NIPS}$ is **zero-knowledge** in the sense of `[GMNO18 Def 7]` if this is negligible in $\lambda$ for every $\mathcal A \in \mathbb A$.

> [!remark] Notation in the literature
> `[GMNO18 Def 7]` fixes the relation, $(\mathrm{crs}, \mathrm{vrs}, \mathrm{td}) \leftarrow G(1^\lambda, R)$, draws a bit $b$ and answers queries with $P(\mathrm{crs}, u, w)$ when $b = 1$ and $\mathsf{Sim}(\mathrm{td}, u)$ when $b = 0$; the adversary $\mathcal A^{\mathsf{Prove}(\mathrm{vrs})}$ guesses $b$. Its advantage is written loosely as $\Pr[\mathsf{ZK} = \mathsf{true}] = \mathsf{negl}$; the bit-guessing margin $\lvert \Pr[b' = b] - 1/2 \rvert$ is half the difference above, see [[Indistinguishability under Chosen-Plaintext Attack#Bit-guessing form]].

## Related

### Properties
- [[Circuit Privacy]] — gives zero knowledge for designated-verifier SNARKs compiled through [[Vector Encryption]] `[ISW21 Thm 3.23]`, see that note
- [[Honest Verifier Zero Knowledge]] — a weaker notion; see also the leakage remark above
- [[Completeness]], [[Soundness]], [[Knowledge Soundness]] — the other properties of [[Non-Interactive Proof Systems]]

### Prerequisites
- [[Non-Interactive Proof Systems]], [[Relation Generator]], [[Security Game]], [[Adversary]], [[Indistinguishability]]
