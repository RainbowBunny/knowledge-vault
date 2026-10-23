Reference:
- `[DDP25]` — T. Debris-Alazard, V. Dyseryn, D. H. Phan, _Hardness of Problems with Hints in Code-Based Cryptography and Applications to Traitor Tracing_, ePrint 2025/2151: https://eprint.iacr.org/2025/2151.pdf

## Syntax

> [!definition] Traitor Tracing Encryption Scheme
> Extends:: [[Multi-Receiver Encryption Scheme]].
> 
> ---
> The scheme is equipped with a new function:
> - $\mathsf{Trace}^{\mathcal{D}}(\mathrm{pk}, (\mathrm{sk}_i)_{i \in [N]}, S) \rightarrow i^*$:
> 	- **Input**: Takes as inputs $\mathrm{pk}$, all the secret keys $(\mathrm{sk}_i)_{i \in [N]}$, a set of suspect users $S \subset [N]$ of size $\ell$, and has oracle access to a decoder $\mathcal{D}$.
> 	- **Output**: A traitor identity $i^* \in S$ or $\perp$.

> [!remark] Notation in the literature
> Key generation is $\mathsf{KeyGen}(1^\lambda, N)$ of [[Multi-Receiver Encryption Scheme]], written $\mathsf{Gen}(1^\lambda, N)$ in `[DDP25]`; see the remark there. `⚠️ verify:` the source's name is taken from the previous version of this note; the ePrint PDF could not be opened.

## Property

### Tracing Security

> [!definition] Parameters
> - [[Multi-Receiver Encryption Scheme]]: Import $(\lambda, N)$.
> - $\ell$: the size of the suspect set, which bounds the coalition. $S \subseteq [N]$ with $\lvert S \rvert = \ell$: the suspect set.
> - $S_D \subseteq S$: the users whose keys $\mathcal A$ obtained (the traitors). $\mathcal D$: the decoder $\mathcal A$ outputs.

> [!definition] Tracing Security Against a $\ell$-Bounded Coalition
> ### Scope
> A traitor tracing scheme $(\mathsf{KeyGen}, \mathsf{Enc}, \mathsf{Dec}, \mathsf{Trace})$ for $N$ users and an [[Adversary]] $\mathcal A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pk}$ and $S$, and the secret key of each user of $S$ it asks for; no other key. $\mathsf{Trace}$ uses $\mathcal D$ only as an oracle.
> - **Promise** — key queries are for users of $S$, so $S_D \subseteq S$ and $\lvert S_D \rvert \leq \ell$.
> - **Quantifier** — $\forall \mathcal A$.
> - **Adaptivity** — key queries are adaptive, after $\mathrm{pk}$ and $S$ are seen; $\mathcal D$ comes after the last query.
>
> ---
> ### Experiment
> A search game with one branch: tracing runs in row 4. `[DDP25]`
> `⚠️ CLAUDE – verify:` not checked against `[DDP25]`, whose PDF was behind a bot check. Check in particular who chooses $S$ (here the challenger samples it) and how the advantage of $\mathcal D$ is defined.
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{pk}, (\mathrm{sk}_i)_{i \in [N]}) \leftarrow \mathsf{KeyGen}(1^\lambda, N)$<br>$S \xleftarrow{\$} \{X \subseteq [N] : \lvert X \rvert = \ell\}$<br>$S_D \leftarrow \emptyset$ | $\xrightarrow{\ \mathrm{pk},\, S\ }$ | |
> | 2 | | $\xleftarrow{\ i\ }$ | **Key queries** (repeated, adaptive, at most $\ell$ times): sends $i \in S$ |
> | | $S_D \leftarrow S_D \cup \{i\}$ | $\xrightarrow{\ \mathrm{sk}_i\ }$ | |
> | 3 | | $\xleftarrow{\ \mathcal D\ }$ | outputs a decoder $\mathcal D$ |
> | 4 | $i^* \leftarrow \mathsf{Trace}^{\mathcal D}(\mathrm{pk}, (\mathrm{sk}_i)_{i \in [N]}, S)$ | | |
>
> **Goal** — $\mathcal A$ wins iff both hold:
> - the advantage of the decoder $\mathcal D$ is non-negligible;
> - tracing fails: $i^* = \perp$ (no traitor confirmed) or $i^* \notin S_D$ (an innocent user accused).
>
> ---
> ### Property
> The scheme is **tracing secure against an $\ell$-bounded coalition** if every PPT $\mathcal A$ wins with negligible probability. A *search* game, see [[Security Game]].

### Compactness

> [!remark]
> A trivial traitor tracing scheme can be built from any [[Public-Key Encryption Scheme (Old)]]:
> - Generating $N$ keypairs $(\mathrm{pk}_i, \mathrm{sk}_i)_{i \in [N]}$.
> - The traitor tracing public key $\mathrm{pk} = (\mathrm{pk}_1, \dots, \mathrm{pk}_N)$.
> - Encryption: Encrypting separately for each user $\mathsf{Enc}(\mathrm{pk}_i, m)$.

> [!definition] Compactness
> We require the size of public key and ciphertext to be asymptotically small in $N$.




