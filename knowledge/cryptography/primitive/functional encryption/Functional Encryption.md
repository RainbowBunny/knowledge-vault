---
aliases: [FE]
---
Reference:
- `[BSW11]` — D. Boneh, A. Sahai, B. Waters, _Functional Encryption: Definitions and Challenges_, TCC 2011: https://www.iacr.org/archive/tcc2011/65970250/65970250.pdf (also ePrint 2010/543)
- `[ABDP15]` — M. Abdalla, F. Bourse, A. De Caro, D. Pointcheval, _Simple Functional Encryption Schemes for Inner Products_, PKC 2015: https://www.iacr.org/archive/pkc2015/90200150/90200150.pdf (also ePrint 2015/017)

## Syntax

> [!definition] Parameters
> - $\lambda$: the security parameter.
> - $F: K \times X \to \{0, 1\}^*$: the functionality, described by a deterministic Turing machine. $K$: the key space; $X$: the plaintext space.
> - $\varepsilon \in K$: the empty key.
> - $\mathrm{pp}$: the public parameters; $\mathrm{mk}$: the master key.
>
> `[BSW11 Def 1]`

> [!definition] Functionality
> A functionality is a function $F: K \times X \to \{0, 1\}^*$ given by a deterministic Turing machine. The key space $K$ contains a special **empty key** $\varepsilon$: $F(\varepsilon, x)$ is all the information about $x$ that intentionally leaks from a ciphertext, such as its length. The secret key for $\varepsilon$ is empty, so anyone can compute $F(\varepsilon, x)$. `[BSW11 Def 1]`

> [!definition] Functional Encryption
> A **functional encryption scheme** for $F$ is a tuple of four PPT algorithms $(\mathsf{Setup}, \mathsf{KeyGen}, \mathsf{Enc}, \mathsf{Dec})$ — `[BSW11]` writes them in lower case, $(\mathsf{setup}, \mathsf{keygen}, \mathsf{enc}, \mathsf{dec})$:
> - $(\mathrm{pp}, \mathrm{mk}) \leftarrow \mathsf{Setup}(1^\lambda)$:
> 	- **Input**: the security parameter.
> 	- **Output**: public parameters $\mathrm{pp}$ and a master key $\mathrm{mk}$.
> - $\mathrm{sk} \leftarrow \mathsf{KeyGen}(\mathrm{mk}, k)$:
> 	- **Input**: $\mathrm{mk}$ and a key $k \in K$.
> 	- **Output**: a secret key $\mathrm{sk}$ for $k$.
> - $c \leftarrow \mathsf{Enc}(\mathrm{pp}, x)$:
> 	- **Input**: $\mathrm{pp}$ and a plaintext $x \in X$.
> 	- **Output**: a ciphertext $c$.
> - $y \leftarrow \mathsf{Dec}(\mathrm{sk}, c)$:
> 	- **Input**: a secret key and a ciphertext.
> 	- **Output**: a value $y$.
>
> `[BSW11 Def 2]`

## Property

### Correctness

> [!definition] Correctness
> For all $k \in K$ and $x \in X$, if
> - $(\mathrm{pp}, \mathrm{mk}) \leftarrow \mathsf{Setup}(1^\lambda)$,
> - $\mathrm{sk} \leftarrow \mathsf{KeyGen}(\mathrm{mk}, k)$,
> - $c \leftarrow \mathsf{Enc}(\mathrm{pp}, x)$,
> - $y \leftarrow \mathsf{Dec}(\mathrm{sk}, c)$,
>
> then $y = F(k, x)$ with probability $1$. `[BSW11 Def 2]`

## Security

### Indistinguishability

> [!definition] Indistinguishability for Functional Encryption
> ### Scope
> A functional encryption scheme $\mathcal E$ for $F$ and a PPT adversary $\mathcal A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ gets $\mathrm{pp}$ and a key oracle, before and after the challenge.
> - **Promise** — for every key $k$ whose secret key $\mathcal A$ holds, before or after the challenge,
>   $$F(k, m_0) = F(k, m_1).$$
>   Since everyone holds the key for $\varepsilon$, this includes $F(\varepsilon, m_0) = F(\varepsilon, m_1)$ — for instance, equal lengths.
> - **Quantifier** — $\forall$ PPT $\mathcal A$.
> - **Adaptivity** — key queries are adaptive; $m_0, m_1$ are chosen after the first round of keys. One challenge.
>
> ---
> ### Experiment
> Two branches that differ in row 4 only: **Game 0** and **Game 1**. `[BSW11 Def 3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{pp}, \mathrm{mk}) \leftarrow \mathsf{Setup}(1^\lambda)$ | $\xrightarrow{\ \mathrm{pp}\ }$ | |
> | 2 | | $\xleftarrow{\ k_i\ }$ | **Key queries** (repeated, adaptive): sends $k_i \in K$ |
> | | $\mathrm{sk}_i \leftarrow \mathsf{KeyGen}(\mathrm{mk}, k_i)$ | $\xrightarrow{\ \mathrm{sk}_i\ }$ | |
> | 3 | | $\xleftarrow{m_0, m_1}$ | chooses $m_0, m_1 \in X$ satisfying the Promise |
> | 4 | **Game 0**: $c^* \leftarrow \mathsf{Enc}(\mathrm{pp}, m_0)$<br>**Game 1**: $c^* \leftarrow \mathsf{Enc}(\mathrm{pp}, m_1)$ | $\xrightarrow{\ c^*\ }$ | |
> | 5 | | $\xleftarrow{\ k_i\ }$ | **Key queries** (repeated, adaptive): sends $k_i \in K$, subject to the Promise |
> | | $\mathrm{sk}_i \leftarrow \mathsf{KeyGen}(\mathrm{mk}, k_i)$ | $\xrightarrow{\ \mathrm{sk}_i\ }$ | |
> | 6 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — the bit $b'$; $W_b$ is the event $b' = 1$ in Game $b$.
> - **Measure** — how far apart $\Pr[W_0]$ and $\Pr[W_1]$ are.
>
> ---
> ### Property
> $$\mathsf{FEadv}[\mathcal E, \mathcal A](\lambda) = \big|\Pr[W_0] - \Pr[W_1]\big|.$$
> $\mathcal E$ is **secure** if $\mathsf{FEadv}[\mathcal E, \mathcal A]$ is negligible for every PPT $\mathcal A$. `[BSW11 Def 3]`

> [!remark] Other notions in the source
> `[BSW11]` also gives a simulation-based definition (Def 4, §5) and a weak simulation-based one (Def 5, §5.1). The game above generalises earlier definitions for predicate encryption.

## Variant

### Predicate encryption
Given a polynomial-time predicate $P: K \times I \to \{0, 1\}$, plaintexts are pairs $(\mathrm{ind}, m)$ of an index and a payload, and
$$F\big(k, (\mathrm{ind}, m)\big) = \begin{cases} m & \text{if } P(k, \mathrm{ind}) = 1, \\ \perp & \text{if } P(k, \mathrm{ind}) = 0. \end{cases}$$
With a **public index**, $F(\varepsilon, \cdot)$ reveals $\mathrm{ind}$; in the **anonymous** case it reveals only the length of $m$. `[BSW11 §2.1]`

| example `[BSW11 §3]` | predicate |
| --- | --- |
| identity-based encryption | $K = \{0, 1\}^* \cup \{\varepsilon\}$, $P(k, \mathrm{ind}) = 1$ iff $k = \mathrm{ind}$; public index |
| attribute-based encryption, key-policy and ciphertext-policy | public index |
| anonymous IBE, hidden vector encryption, inner-product predicate | private index |

## Related

### Descendants
- [[Inner-Product Functional Encryption]] — $K = X = \mathbb Z_p^\ell$ and $F(\mathbf x, \mathbf y) = \langle \mathbf x, \mathbf y \rangle \bmod p$ `[ABDP15]`. Not the inner-product *predicate* above: that one reveals $m$ when $\langle \mathbf x, \mathbf y \rangle = 0$; this one reveals the inner product itself.

### Siblings
- [[Public-Key Encryption Scheme]] — the case where a key returns the whole plaintext and $\varepsilon$ its length

### Prerequisites
- [[Security Game]], [[Adversary]]
