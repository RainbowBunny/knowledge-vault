Reference:
- https://eprint.iacr.org/2025/2151.pdf

## Syntax

> [!definition] Traitor Tracing Encryption Scheme
> Extends:: [[Multi-Receiver Encryption Scheme]].
> 
> ---
> The scheme is equipped with a new function:
> - $\mathsf{Trace}^{\mathcal{D}}(\mathrm{pk}, (\mathrm{sk}_i)_{i \in [N]}, S) \rightarrow i^*$:
> 	- **Input**: Takes as inputs $\mathrm{pk}$, all the secret keys $(\mathrm{sk}_i)_{i \in [N]}$, a set of suspect users $S \subset [N]$ of size $\ell$, and has oracle access to a decoder $\mathcal{D}$.
> 	- **Output**: A traitor identity $i^* \in S$ or $\perp$.

## Property

### Tracing Security

> [!definition] Tracing Security Against a $\ell$-Bounded Coalition
> For any [[Adversary]] $\mathcal{A}$, define the following games:
> Game 1:
> - Runs $(\mathrm{pk}, (\mathrm{sk}_i)_{i \in [N]}) \leftarrow \mathsf{Gen}(1^\lambda, N)$.
> - Samples $S \leftarrow \{X \subseteq [N], |X| = \ell\}$.
> - Sends $(\mathrm{pk}, S)$ to $\mathcal{A}$.
> - Samples the set $S_D$ by:
> 	- $\mathcal{A}$ adaptively queries keys for $i \in S$.
> 	- Upon this query, sends $\mathrm{sk}_i$ to $\mathcal{A}$.
> - $\mathcal{A}$ outputs a decoder $\mathcal{D}$.
> - Runs $i^* = \mathsf{Trace}^\mathcal{D}(\mathrm{pk}, (\mathrm{sk}_i)_{i \in [N]}, S)$.
> $\mathcal{A}$ loses if 
> - Either the advantage of the decoding algorithm $\mathcal{D}$ is negligible.
> - Both conditions are met:
> 	- (Confirmation) $i^* \neq \; \perp$, and;
> 	- (Soundness) $i^* \in S_D$.

### Compactness

> [!remark]
> A trivial traitor tracing scheme can be built from any [[Public-Key Encryption Scheme]]:
> - Generating $N$ keypairs $(\mathrm{pk}_i, \mathrm{sk}_i)_{i \in [N]}$.
> - The traitor tracing public key $\mathrm{pk} = (\mathrm{pk}_1, \dots, \mathrm{pk}_N)$.
> - Encryption: Encrypting separately for each user $\mathsf{Enc}(\mathrm{pk}_i, m)$.

> [!definition] Compactness
> We require the size of public key and ciphertext to be asymptotically small in $N$.




