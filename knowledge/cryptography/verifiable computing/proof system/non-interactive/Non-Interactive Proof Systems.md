Reference:
- `[G16 §2.2]` — Groth, _On the Size of Pairing-Based Non-Interactive Arguments_, EUROCRYPT 2016 (ePrint 2016/260): https://eprint.iacr.org/2016/260.pdf
- `[N §5]` — Nitulescu, _A Gentle Introduction to SNARKs_ (survey), Definition 5.1: https://www.di.ens.fr/~nitulesc/files/Survey-SNARKs.pdf
- `[A]` — Alinush, _Zero-Knowledge Proofs_, section "Algorithms": https://alinush.github.io/zkps
- The three were read through a summarizer, not verbatim; check the wording before quoting.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Syntax

> [!definition] Parameters
> - $\lambda$: the security parameter.
> - [[Effective Relation]]: Import $(\mathcal X, \mathcal W, \mathcal R)$; $\mathcal L_\mathcal R = \{\mathbf x : \exists \mathbf w, (\mathbf x, \mathbf w) \in \mathcal R\}$ is its language.
> - [[Relation Generator]]: Import $(\mathrm{aux})$. The relation $\mathcal R$ may come from $(\mathcal R, \mathrm{aux}) \leftarrow \mathsf{RelGen}(1^\lambda)$; for a fixed relation $\mathrm{aux} = \perp$.
> - $\mathrm{crs}$: the common reference string, used by the prover. $\mathrm{st}$: the verification state, used by the verifier.

> [!definition] Non-Interactive Proof System `[G16 §2.2]` `[N Def 5.1]` `[A]`
> A **non-interactive proof system** for an [[Effective Relation]] $\mathcal R$ is a triple $\Pi_\mathsf{NIPS} = (\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify})$ of efficient algorithms. The relation generator is not one of them: it runs first.
> - $(\mathrm{crs}, \mathrm{st}) \leftarrow \mathsf{Setup}(1^\lambda, \mathcal R)$: (Randomized) Setup algorithm.
>     - **Input**: the security parameter $1^\lambda$ and the relation $\mathcal R$.
>     - **Output**: a common reference string $\mathrm{crs}$ and a verification state $\mathrm{st}$.
> - $\boldsymbol{\pi} \leftarrow \mathsf{Prove}(\mathrm{crs}, \mathbf{x}, \mathbf{w})$: (Randomized) Proving algorithm.
>     - **Input**: the common reference string $\mathrm{crs}$, a statement $\mathbf{x} \in \mathcal X$ and a witness $\mathbf{w} \in \mathcal W$. Honest provers have $(\mathbf{x}, \mathbf{w}) \in \mathcal R$.
>     - **Output**: a proof $\boldsymbol{\pi}$.
> - $b \leftarrow \mathsf{Verify}(\mathrm{st}, \mathbf{x}, \boldsymbol{\pi})$: (Possibly randomized) Verification algorithm.
>     - **Input**: the verification state $\mathrm{st}$, a statement $\mathbf{x}$ and a proof $\boldsymbol{\pi}$.
>     - **Output**: a bit $b \in \{0, 1\}$; $1$ means accept.

> [!remark] Notation in the literature
> The form above is the most general one I found. The simulator and its trapdoor are not part of the syntax; they appear in [[Zero Knowledge]].
>
> | source | algorithms | differences |
> | --- | --- | --- |
> | `[G16 §2.2]` | $(\mathsf{Setup}, \mathsf{Prove}, \mathsf{Vfy}, \mathsf{Sim})$ | $(\sigma, \tau) \leftarrow \mathsf{Setup}(R)$ outputs one string $\sigma$ and the simulation trapdoor $\tau$; $\mathsf{Prove}(R, \sigma, \phi, w)$ and $\mathsf{Vfy}(R, \sigma, \phi, \pi)$ take the relation as an argument; $\mathsf{Sim}(R, \tau, \phi)$. The relation comes from a generator $(R, z) \leftarrow \mathcal R(1^\lambda)$ and $z$ goes to the adversary. Publicly verifiable. |
> | `[N Def 5.1]` | $(\mathsf G, \mathsf P, \mathsf{Ver}, \mathsf{Sim})$ | $\mathsf G(1^\lambda, R) \to (\mathrm{crs}, \mathrm{vrs}, \mathrm{td})$; $\mathsf{vrs}$ is a secret verification state needed only for designated-verifier schemes. The survey is inconsistent about whether $\mathsf G$ outputs $\mathrm{vrs}$ (its text and its formal line differ). |
> | `[A]` | $\mathsf{ZKP}.(\mathsf{Setup}, \mathsf{Prove}, \mathsf{Verify}, \mathsf{Sim})$ | $\mathsf{Setup}(1^\lambda, R) \to (\mathsf{prk}, \mathsf{vk}, \mathsf{td})$: a proving key and a verifying key instead of $(\mathrm{crs}, \mathrm{st})$; $\mathsf{Sim}(\mathsf{td}, \mathbf x)$. |
>
> The pair $(\mathrm{crs}, \mathrm{st})$ is the form already used in [[Non-Interactive Linear Proofs]] and [[LUNA]]; `⚠️ CLAUDE – verify:` I did not check which paper it comes from.

> [!remark] Publicly verifiable or designated verifier
> If $\mathrm{st}$ can be published, the system is **publicly verifiable**: $\mathrm{st} = \mathrm{vk}$ in `[A]`, and $\sigma$ plays both roles in `[G16]`. If $\mathrm{st}$ contains a secret, only its holder can verify: [[LUNA]] decrypts with a secret key stored in $\mathrm{st}$. The triple above covers both; `[N §5.1.1]` says the same about $\mathrm{vrs}$.

> [!remark] Where the trapdoor went
> `⚠️ CLAUDE – verify:` all three sources let the setup return a simulation trapdoor. I left it out, because [[Zero Knowledge]] here gives the simulator its own setup $\mathcal S_\mathsf{setup}$ that produces $(\widetilde{\mathrm{crs}}, \widetilde{\mathrm{st}})$. The trapdoor form is the special case where $\mathcal S_\mathsf{setup}$ runs $\mathsf{Setup}$ and keeps the trapdoor. This is my reading of the property notes, not a statement from the sources.

> [!remark] Quantification over $\mathcal R$
> In `[G16 §2.2]` completeness holds for every $R \in \mathcal R_\lambda$, while soundness and knowledge soundness are stated for $(R, z)$ drawn from the generator, with $z$ given to the adversary and the extractor. `⚠️ CLAUDE – verify:` the property notes ([[Completeness]], [[Soundness]], [[Zero Knowledge]]) currently take $\mathcal R$ as given and have no $\mathrm{aux}$; adding the generator to their games is a follow-up.

## Property

The properties are separate notes; the acronyms below are combinations of them.
- [[Completeness]] — a true statement can be proven.
- [[Soundness]] — a false statement cannot be proven; [[Knowledge Soundness]] — a prover that convinces $\mathrm{Verify}$ knows a witness.
- [[Succinctness]], [[Zero Knowledge]].

## Variant

|                                        | Completeness | Soundness     | Knowledge | Succinct | ZK  |
| -------------------------------------- | ------------ | ------------- | --------- | -------- | --- |
| [[Non-Interactive Proof Systems\|NIP]] | ✓            | statistical   | —         | —        | —   |
| NARG                                   | ✓            | computational | —         | —        | —   |
| NARK                                   | ✓            | computational | ✓         | —        | —   |
| SNARG                                  | ✓            | computational | —         | ✓        | —   |
| SNARK                                  | ✓            | computational | ✓         | ✓        | —   |
| zk-SNARG                               | ✓            | computational | —         | ✓        | ✓   |
| zk-SNARK                               | ✓            | computational | ✓         | ✓        | ✓   |

## Related

- [[Effective Relation]], [[Relation Generator]]
- [[Non-interactive ARGument]], [[Non-interactive ARgument of Knowledge]] — the rows of the table
- [[Non-Interactive Linear Proofs]], [[Split Prover]], [[Groth16]], [[LUNA]]
- [[Interactive Proof Systems]], [[Argument Systems]]
