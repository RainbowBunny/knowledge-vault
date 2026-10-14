Reference:
- `[G16 §2.2]` — Groth, _On the Size of Pairing-Based Non-Interactive Arguments_, EUROCRYPT 2016 (ePrint 2016/260): https://eprint.iacr.org/2016/260.pdf
- `[A]` — Alinush, _Zero-Knowledge Proofs_, section "Algorithms": https://alinush.github.io/zkps
- `[N §5]` — Nitulescu, _A Gentle Introduction to SNARKs_ (survey): https://www.di.ens.fr/~nitulesc/files/Survey-SNARKs.pdf
- All three were read through a summarizer, not verbatim; check the wording before quoting.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Definition

> [!definition] Parameters
> - $\lambda$: the security parameter.
> - [[Effective Relation]]: Import $(\mathcal X, \mathcal W, \mathcal R)$.
> - $\mathcal R_\lambda$: the set of relations the generator can output, all of them polynomial-time decidable.
> - $\mathrm{aux}$: auxiliary information about how $\mathcal R$ was generated.

> [!definition] Relation Generator `[G16 §2.2]` `[A]`
> A **relation generator** is a probabilistic polynomial-time algorithm that picks the relation a proof system is used for.
> - $(\mathcal R, \mathrm{aux}) \leftarrow \mathsf{RelGen}(1^\lambda)$: (Randomized) Relation-generation algorithm.
>     - **Input**: the security parameter $1^\lambda$.
>     - **Output**: an [[Effective Relation]] $\mathcal R \in \mathcal R_\lambda$ and auxiliary information $\mathrm{aux}$.

> [!remark] Role of $\mathrm{aux}$
> - In `[G16]` the auxiliary input $z$ "will be given to the adversary"; in `[A]` the adversary and the extractor both receive $\mathrm{aux}$, and for a bilinear-group scheme such as Groth16 it is natural to return the group through $\mathrm{aux}$.
> - Neither source lists $\mathrm{aux}$ as an input of $\mathsf{Setup}$, which takes the relation only. This vault does the same in [[Non-Interactive Proof Systems]].
> - `[A]` requires the generator to be **benign**, because otherwise knowledge soundness cannot be achieved. I did not find a precise definition of benign in what I read. `⚠️ CLAUDE – verify` before relying on it.

## Variant

### Fixed relation

> [!definition] Fixed relation
> A proof system for one fixed family $\{\mathcal R_\lambda\}$ uses the trivial generator $\mathsf{RelGen}(1^\lambda) = (\mathcal R_\lambda, \perp)$. `[N Def 5.1]` takes this view: $\mathcal R$ is an input of the setup algorithm, and there is no generator.

> [!remark] Notation in the literature
> The vault writes $\mathsf{RelGen}$ for the generator because $\mathcal R$ already names the relation.
>
> | source | generator | differences |
> | --- | --- | --- |
> | `[G16 §2.2]` | $(R, z) \leftarrow \mathcal R(1^\lambda)$ | the generator is called $\mathcal R$ and the relation $R$; $z$ is the auxiliary input. |
> | `[A]` | $\mathcal R(1^\lambda) \to (R, \mathsf{aux})$ | same shape; the outputs for a given $\lambda$ are written $\mathcal R_\lambda$. |
> | `[N §5]` | none | $\mathcal R$ is an input of $\mathsf G$; an auxiliary input generator $\mathcal Z(1^\lambda)$ appears only in knowledge soundness (§5.3). |

> [!remark] Context generator in [[Public-Key Encryption Scheme]]
> `⚠️ CLAUDE – verify:` the context generator $\mathcal P(1^\lambda) \to \mathrm{aux}$ of the PKE note has the same shape: it runs before key generation and its output is public. The difference is that there $\mathrm{aux}$ is an input of $\mathsf{Gen}$, while here it is adversary-side information. Treating the two as one pattern is my reading.

## Related

- [[Non-Interactive Proof Systems]] — uses $(\mathcal R, \mathrm{aux})$; [[Effective Relation]]
- [[Soundness]], [[Knowledge Soundness]], [[Zero Knowledge]] — the games where $\mathrm{aux}$ reaches the adversary
- [[Public-Key Encryption Scheme]]
