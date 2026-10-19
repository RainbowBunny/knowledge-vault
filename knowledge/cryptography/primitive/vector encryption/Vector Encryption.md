Reference:
- https://eprint.iacr.org/2022/1690.pdf
- `[ISW21 x]` — Ishai, Su, Wu, _Shorter and Faster Post-Quantum Designated-Verifier zkSNARKs from Lattices_, CCS 2021 (ePrint 2021/977): https://eprint.iacr.org/2021/977.pdf. Definitions 3.3, 3.4 and 3.7 were read through a summarizer, not verbatim.
- `#supplemented` marks what I added to your text; its source is on this line. Delete the tag once you have read it.

## Syntax

> [!definition] Parameters
> - $\lambda$: the security parameter. $\ell$: the plaintext dimension, given in unary $1^\ell$.
> - $\mathbb F$: a finite field; plaintexts are vectors in $\mathbb F^\ell$.
> - $\mathrm{pp}$: the public parameters. $\mathrm{sk}$: the secret key.
> - $m$: the number of ciphertexts one $\mathsf{Add}$ combines.

> [!definition] Vector Encryption
> Let $\mathbb F$ be a finite field. A secret-key additively-homomorphic **vector encryption** scheme over a vector space $\mathbb F^\ell$ consists of a tuple of algorithms $\Pi_\mathsf{Enc} = (\mathsf{Setup}, \mathsf{Enc}, \mathsf{Add}, \mathsf{Dec})$:
> - $(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell)$: (Randomized) Setup algorithm.
>     - **Input**: the security parameter $\lambda$ and the plaintext dimension $\ell$.
>     - **Output**: public parameter $\mathrm{pp}$ and a secret key $\mathrm{sk}$.
> - $\mathbf{C} \leftarrow \mathsf{Enc}(\mathrm{sk}, \mathbf{v})$: (Randomized) Encryption algorithm.
>     - **Input**: the secret key $\mathrm{sk}$ and a vector $\mathbf{v} \in \mathbb F^\ell$.
>     - **Output**: a ciphertext $\mathbf{C}$.
> - $\mathbf{C}^* \leftarrow \mathsf{Add}(\mathrm{pp}, \{\mathbf{C}_i\}_{i \in [m]}, \{y_i\}_{i \in [m]})$: (Possibly randomized) Addition algorithm.
>     - **Input**: the public parameters, a collection of ciphertexts $\{\mathbf{C}_i\}_{i \in [m]}$ and scalars $\{y_i\} \in \mathbb F$, $i \in [m]$.
>     - **Output**: a new ciphertext $\mathbf{C}^*$.
> - $\mathbf{v} / \perp \leftarrow \mathsf{Dec}(\mathrm{sk}, \mathbf{C})$: (Deterministic) Decryption algorithm.
>     - **Input**: the secret key $\mathrm{sk}$ and a ciphertext $\mathbf{C}$.
>     - **Output**: either a vector $\mathbf{v} \in \mathbb F^\ell$ or a special symbol $\perp$.

> [!remark] Notation in the literature
> | source | algorithms | differences |
> | --- | --- | --- |
> | `[ISW21 Def 3.3]` | $(\mathsf{Setup}, \mathsf{Encrypt}, \mathsf{Decrypt}, \mathsf{Add})$ | $\mathsf{Encrypt}(\mathrm{sk}, \mathbf v) \to \mathrm{ct}$ and $\mathsf{Decrypt}(\mathrm{sk}, \mathrm{ct})$; $\mathsf{Add}(\mathrm{pp}, \{\mathrm{ct}_i\}_{i \in [n]}, \{c_i\}_{i \in [n]})$ names the scalars $c_i$ and the count $n$. |
>
> The scheme [[Module HGSW]] gives $\mathsf{Enc}$ an extra index $i$, because its ciphertexts are tied to a position. #supplemented

## Property

### Additive Homomorphism

> [!definition] Additive Homomorphism
> For any adversary $\mathcal A = (\mathcal A_\mathsf{find})$, we define the additive homomorphic advantage:
> $$\mathsf{Adv}_{\Pi_{\mathsf{Enc}}}^{\mathsf{AH}}(\mathcal A) = \Pr\!\left[ 
\begin{array}{l}
\sum_{i \in [m]} y_i v_i = m^*
\end{array} 
\;\middle |\; 
\begin{array}{l}
(\mathrm{pp}, \mathrm{sk}) \leftarrow \mathsf{Setup}(1^\lambda, 1^\ell) \\
\{\mathbf{v}_i\}_{i \in [m]}, \{y_i\}_{i \in [m]} \leftarrow \mathcal{A}_\mathsf{find}(\mathrm{pp}, \mathrm{sk}) \\
\{\mathbf{C}_i\}_{i \in [m]} \leftarrow \{\mathsf{Enc}(\mathrm{sk}, \mathbf{v}_i)\}_{i \in [m]} \\
\mathbf{C}^* \leftarrow \mathsf{Add}(\mathrm{pp}, \{\mathbf{C}_i\}_{i \in [m]}, \{y_i\}_{i \in [m]}) \\
m^* \leftarrow \mathsf{Dec}(\mathbf{sk}, \mathbf{C}^*)
\end{array} \right]$$

> [!remark]
> We say that the scheme $\Pi_\mathsf{Enc}$ is additively homomorphic with respect to a set $S \in R_p^m$ holds for all $(y_1, \dots, y_m) \in S$.

> [!remark] Correctness in the source
> `[ISW21 Eq. 3.1]` asks that $\mathsf{Dec}$ of the output of $\mathsf{Add}$ equals $\sum_i y_i \mathbf v_i$ with probability $1 - \mathsf{negl}(\lambda)$, and also defines correctness relative to a set of allowed coefficient vectors. The remark above is that relative form. #supplemented

## Related

### Instantiations
- [[Module HGSW]] — the scheme behind [[LUNA]]

### Constructions
- [[LUNA]] — compiles an LPCP through this primitive

### Properties
- [[Circuit Privacy]] — what the output of $\mathsf{Add}$ reveals about $y_i$
- [[Linear-Only Security]] — every ciphertext an adversary can make is a linear combination of the ones it was given

### Siblings
- [[Homomorphic Encryption]] — evaluates arbitrary circuits (public key); here only linear combinations (secret key)
