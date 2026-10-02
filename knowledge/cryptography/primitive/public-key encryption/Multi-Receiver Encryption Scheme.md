Reference:
- https://eprint.iacr.org/2025/2151.pdf

## Syntax

> [!definition] Parameters
> - $\lambda$: Security parameter.
> - $N = \mathsf{poly}(\lambda)$: Number of parties.
> - $\mathcal{PK}$: Public key space.
> - $\mathcal{SK}$: Secret key space.
> - $\mathcal{M}$: Message space.
> - $\mathcal{C}$: Ciphertext space.

> [!definition] Multi-Receiver Encryption Scheme
> - $\mathsf{Gen}(1^\lambda, N) \rightarrow (\mathrm{pk}, (\mathrm{sk})_{i \in [N]})$: 
> 	- **Input**: Security parameter $1^\lambda$ and the number of users $N$.
> 	- **Output**: Returns public key $\mathrm{pk}$ and secret keys $(\mathrm{sk}_i)_{i \in [N]}$ (one key for each user).
> - $\mathsf{Enc}(\mathrm{pk}, m) \rightarrow \mathrm{ct}$:
> 	- **Input**: Public key $\mathrm{pk}$ and a message $m \in \mathcal{M}$.
> 	- **Output**: Returns a ciphertext $\mathrm{ct}$.
> - $\mathsf{Dec}(\mathrm{sk}_i, \mathrm{ct}) \rightarrow m$:
> 	- **Input**: A secret key for any user $\mathrm{sk}_i$ and a ciphertext $\mathrm{ct}$.
> 	- **Output**: A decrypted message $m \in \mathcal{M}$.

## Property

> [!definition] Correctness