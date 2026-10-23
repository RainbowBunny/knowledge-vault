---
aliases: [TR, Trace and Revoke]
---
Reference:
- `[ABPSY17]` — S. Agrawal, S. Bhattacherjee, D. H. Phan, D. Stehlé, S. Yamada, _Efficient Public Trace and Revoke from Standard Assumptions_, ACM CCS 2017, pp. 2277–2293. Numbers refer to the full version, ePrint 2017/650: https://eprint.iacr.org/2017/650.pdf

## Syntax

> [!definition] Parameters
> - $\lambda$: the security parameter. $t$: the bound on the size of traitor coalitions. $r$: the bound on the number of revoked users.
> - $\mathcal{ID}$: the identity space; $\mathcal M$: the message space — implicit arguments of $\mathsf{Setup}$. $\mathcal K$: the secret-key space; $\mathcal C$: the ciphertext space — implicit public parameters output by $\mathsf{Setup}$.
> - $\mathrm{pd}$: the public directory. $p_\mathrm{id}$: the public information of user $\mathrm{id}$; it need not contain $\mathrm{id}$.
> - $R$: a set of at most $r$ revoked users, given by their $p_\mathrm{id}$. $S$: a set of at most $t$ suspect users. $D$: a pirate decoder.
>
> `[ABPSY17 Def 1]`

> [!definition] Trace-and-Revoke Scheme
> Extends:: [[Traitor Tracing Encryption Scheme]].
>
> ---
> A **dynamic identity-based trace-and-revoke scheme** $(t, r)$-$\mathcal{TR}$ in the black-box confirmation model is a tuple $\mathcal{TR} = (\mathsf{Setup}, \mathsf{KeyGen}, \mathsf{Enc}, \mathsf{Dec}, \mathsf{Trace})$ of five PPT algorithms:
> - $(\mathrm{msk}, \mathrm{pk}, \mathrm{pd}) \leftarrow \mathsf{Setup}(1^\lambda, 1^t, 1^r)$:
> 	- **Input**: the security parameter $\lambda$, the coalition bound $t$ and the revocation bound $r$.
> 	- **Output**: the master secret key $\mathrm{msk}$, the encryption key $\mathrm{pk}$, and the public directory $\mathrm{pd}$, initially empty.
> - $(\mathrm{sk}_\mathrm{id}, p_\mathrm{id}) \leftarrow \mathsf{KeyGen}(\mathrm{msk}, \mathrm{id})$:
> 	- **Input**: $\mathrm{msk}$ and an identity $\mathrm{id} \in \mathcal{ID}$.
> 	- **Output**: the secret key $\mathrm{sk}_\mathrm{id}$ and the public information $p_\mathrm{id}$; $\mathrm{pd}$ is updated to include $p_\mathrm{id}$.
> - $C \leftarrow \mathsf{Enc}(\mathrm{pk}, R, m)$:
> 	- **Input**: $\mathrm{pk}$, a set $R$ of cardinality at most $r$ containing the $p_\mathrm{id}$ of each revoked user, and a message $m \in \mathcal M$.
> 	- **Output**: a ciphertext $C \in \mathcal C$.
> - $m \leftarrow \mathsf{Dec}(\mathrm{sk}_\mathrm{id}, C)$:
> 	- **Input**: the secret key of user $\mathrm{id}$ and a ciphertext $C \in \mathcal C$.
> 	- **Output**: a message $m \in \mathcal M$.
> - $\mathrm{id} / \perp \leftarrow \mathsf{Trace}(\mathrm{pd}, R, S, \mathcal O_D)$:
> 	- **Input**: $\mathrm{pd}$, a set $R$ of at most $r$ revoked users, a set $S$ of at most $t$ suspect users, and black-box access to the pirate decoder $D$ through the oracle $\mathcal O_D$: $\mathcal O_D(C, m) = 1$ if $D(C) = m$, and $0$ otherwise.
> 	- **Output**: an identity $\mathrm{id}$, or $\perp$.
>
> `[ABPSY17 Def 1]`

> [!remark] What the name says
> - **Dynamic identity-based** — users are added one at a time by $\mathsf{KeyGen}(\mathrm{msk}, \mathrm{id})$, with identities from $\mathcal{ID}$, instead of $N$ users fixed at setup.
> - **Revoke** — $\mathsf{Enc}$ takes the set $R$ of users who must not be able to decrypt.
> - **Public traceability** — every input of $\mathsf{Trace}$ is public, so anyone can trace, not only the holder of $\mathrm{msk}$.
> - **Black-box confirmation** — $\mathsf{Trace}$ uses $D$ only through $\mathcal O_D$, and is given a suspect set $S$ that contains the traitors; it confirms one of them.

> [!remark] Why `Extends:: [[Traitor Tracing Encryption Scheme]]`
> With $R = \emptyset$ and $N$ identities created in advance, a trace-and-revoke scheme is a traitor tracing scheme whose $\mathsf{Trace}$ reads public data instead of every secret key. The base note has the static syntax $\mathsf{KeyGen}(1^\lambda, N)$; this note adds revocation, dynamic identities and public tracing.

> [!remark] Notation in the source
> `[ABPSY17]` writes the oracle as $\mathcal O_D(M, C)$ when defining it, but as $\mathcal O_D(C, m)$ in Equation (1) and in the tracing algorithm; this note uses the second order throughout. Correctness and the games write "$\mathrm{id} \notin R$" for "$p_\mathrm{id} \notin R$".

## Property

### Correctness

> [!definition] Correctness
> With overwhelming probability over the randomness of the algorithms: for every $m \in \mathcal M$, every set $R$ of at most $r$ revoked users and every $\mathrm{id} \in \mathcal{ID}$ with $\mathrm{id} \notin R$,
> $$\mathsf{Dec}(\mathrm{sk}_\mathrm{id}, \mathsf{Enc}(\mathrm{pk}, R, m)) = m.$$
> `[ABPSY17 Def 1]`

## Security

### Public Traceability

> [!definition] Parameters
> - From Syntax: $\lambda, t, r, \mathcal{ID}, \mathcal M, \mathrm{pd}$.
> - $T$: the identities whose keys the adversary obtained (the traitors). $D$: the pirate decoder it outputs. $S$: its suspect set.
> - $c > 0$: a constant.
>
> `[ABPSY17 §2.1]`

> [!definition] Useful Decoder
> A pirate decoder $D$ is **useful** for a revoked set $R$ if, for some constant $c > 0$,
> $$\Pr\Big[\mathcal O_D\big(C^{(R)}, m\big) = 1 \;\Big|\; m \leftarrow U(\mathcal M),\ C^{(R)} \leftarrow \mathsf{Enc}(\mathrm{pk}, R, m)\Big] \geq \frac{1}{|\mathcal M|} + \frac{1}{\lambda^c}: \tag{1}$$
> on an honest encryption for $R$ of a uniform message, it outputs the message noticeably more often than guessing. This probability can be estimated by querying $\mathcal O_D$ repeatedly and applying Hoeffding's inequality. `[ABPSY17 §2.1, Eq. (1)]`

> [!definition] Public Traceability
> ### Scope
> A $(t, r)$-trace-and-revoke scheme and a PPT adversary $\mathcal A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ gets $\mathrm{pk}$ and the growing $\mathrm{pd}$; the secret key of every identity it asks for as a traitor; and the keys of the revoked users it chooses. Adding a user gives it no key.
> - **Promise**:
>     - at most $t$ traitor queries;
>     - $|R| \leq r$;
>     - $T \subseteq S$ and $|S| \leq t$.
> - **Quantifier** — $\forall$ PPT $\mathcal A$.
> - **Adaptivity** — users, traitors and $R$ are chosen adaptively, each after everything $\mathcal A$ has seen so far, including $\mathrm{pd}$.
>
> ---
> ### Experiment
> The game $\mathsf{AD}\text{-}\mathsf{TT}$, a search game with one branch. `[ABPSY17 §2.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{msk}, \mathrm{pk}, \mathrm{pd}) \leftarrow \mathsf{Setup}(1^\lambda, 1^t, 1^r)$<br>$T \leftarrow \emptyset$ | $\xrightarrow{\ \mathrm{pk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathrm{id}\ }$ | **Add users** (repeated, adaptive, polynomially many times): sends $\mathrm{id} \in \mathcal{ID}$ |
> | | $(\mathrm{sk}_\mathrm{id}, p_\mathrm{id}) \leftarrow \mathsf{KeyGen}(\mathrm{msk}, \mathrm{id})$<br>$\mathrm{pd} \leftarrow \mathrm{pd} \cup \{p_\mathrm{id}\}$<br>keeps $\mathrm{sk}_\mathrm{id}$ to itself | $\xrightarrow{\ \mathrm{pd}\ }$ | |
> | 3 | | $\xleftarrow{\ \mathrm{id}\ }$ | **Traitor key queries** (repeated, adaptive, at most $t$ times): sends $\mathrm{id} \in \mathcal{ID}$, possibly one it saw in $\mathrm{pd}$ |
> | | if $\mathrm{id}$ is new: $(\mathrm{sk}_\mathrm{id}, p_\mathrm{id}) \leftarrow \mathsf{KeyGen}(\mathrm{msk}, \mathrm{id})$ and $\mathrm{pd} \leftarrow \mathrm{pd} \cup \{p_\mathrm{id}\}$<br>$T \leftarrow T \cup \{\mathrm{id}\}$ | $\xrightarrow{\ \mathrm{sk}_\mathrm{id}\ }$ | |
> | 4 | | $\xleftarrow{\ R\ }$ | **Revocation**: sends $R \subseteq \mathrm{pd}$ with $\lvert R \rvert \leq r$ |
> | | | $\xrightarrow{\ \{\mathrm{sk}_\mathrm{id} \,:\, p_\mathrm{id} \in R\}\ }$ | |
> | 5 | | $\xleftarrow{\ D,\, S\ }$ | outputs a pirate decoder $D$ and a suspect set $S$ with $T \subseteq S$ and $\lvert S \rvert \leq t$ |
> | 6 | $\mathrm{out} \leftarrow \mathsf{Trace}(\mathrm{pd}, R, S, \mathcal O_D)$ | | |
>
> **Goal** — $\mathcal A$ wins iff both hold:
> - $D$ is useful for the $R$ that $\mathcal A$ chose: Equation (1) holds;
> - $\Pr[\mathrm{out} = \perp \,\lor\, \mathrm{out} \notin T] \geq 1/\lambda^c$, over the coins of $\mathsf{Trace}$.
>
> ---
> ### Property
> $\mathcal{TR}$ is **publicly traceable** if no PPT $\mathcal A$ wins $\mathsf{AD}\text{-}\mathsf{TT}$ with non-negligible probability. A *search* game, see [[Security Game]]. `[ABPSY17 §2.1]`

> [!remark] Both failures count
> $\mathcal A$ wins if tracing accuses nobody ($\perp$) or accuses an innocent user ($\notin T$). A useless decoder is not a win: condition (i) rules out the trivial adversary that outputs a decoder which never decrypts.

### IND-CPA

Specializes [[Indistinguishability under Chosen-Plaintext Attack]]. The source calls it *semantic security*.

> [!definition] IND-CPA for Trace-and-Revoke
> ### Scope
> A $(t, r)$-trace-and-revoke scheme $\mathcal{TR}$ and a PPT adversary $\mathcal A$.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ gets $\mathrm{pk}$, the growing $\mathrm{pd}$, and the secret keys of the revoked users; no other key.
> - **Promise**:
>     - $|R| \leq r$;
>     - $m_0, m_1 \in \mathcal M$, $|m_0| = |m_1|$.
> - **Quantifier** — $\forall$ PPT $\mathcal A$.
> - **Adaptivity** — $R$ is chosen adaptively, after $\mathrm{pd}$ is seen; $m_0, m_1$ after the revoked keys arrive. One challenge.
>
> ---
> ### Experiment
> Two branches that differ in row 5 only: **Game 0** and **Game 1**. `[ABPSY17 §2.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(\mathrm{msk}, \mathrm{pk}, \mathrm{pd}) \leftarrow \mathsf{Setup}(1^\lambda, 1^t, 1^r)$ | $\xrightarrow{\ \mathrm{pk}\ }$ | |
> | 2 | | $\xleftarrow{\ \mathrm{id}\ }$ | **Add users** (repeated, adaptive, polynomially many times): sends $\mathrm{id} \in \mathcal{ID}$ |
> | | $(\mathrm{sk}_\mathrm{id}, p_\mathrm{id}) \leftarrow \mathsf{KeyGen}(\mathrm{msk}, \mathrm{id})$<br>$\mathrm{pd} \leftarrow \mathrm{pd} \cup \{p_\mathrm{id}\}$ | $\xrightarrow{\ \mathrm{pd}\ }$ | |
> | 3 | | $\xleftarrow{\ R\ }$ | **Revocation**: sends $R \subseteq \mathrm{pd}$ with $\lvert R \rvert \leq r$ |
> | | | $\xrightarrow{\ \{\mathrm{sk}_\mathrm{id} \,:\, p_\mathrm{id} \in R\}\ }$ | |
> | 4 | | $\xleftarrow{\ m_0,\, m_1\ }$ | chooses $m_0, m_1 \in \mathcal M$ of equal length |
> | 5 | **Game 0**: $C^* \leftarrow \mathsf{Enc}(\mathrm{pk}, R, m_0)$<br>**Game 1**: $C^* \leftarrow \mathsf{Enc}(\mathrm{pk}, R, m_1)$ | $\xrightarrow{\ C^*\ }$ | |
> | 6 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^{\mathsf{ind}\text{-}\mathsf{cpa}}_{\mathcal{TR}}(\mathcal A) = \Big|\Pr\big[\mathsf{Expt}_0(\mathcal A) = 1\big] - \Pr\big[\mathsf{Expt}_1(\mathcal A) = 1\big]\Big|.$$
> $\mathcal{TR}$ is **semantically secure** (IND-CPA) if this is negligible for every PPT $\mathcal A$.

> [!remark] The source's form
> `[ABPSY17]` samples $b \leftarrow \{0, 1\}$, encrypts $m_b$, and defines the advantage as $|\Pr[b = b'] - 1/2|$; its adversary is a single machine that keeps state, as here. The difference above is twice that; see [[Indistinguishability under Chosen-Plaintext Attack#Bit-guessing form]].

## Variant

### Almost public traceability
$\mathsf{Trace}$ outputs a public information $p_\mathrm{id}$ instead of an identity, and winning is checked against the public information of the traitors. `[ABPSY17 §2.1]`

## Related

### Constructions
- From [[Inner-Product Functional Encryption]] of dimension $\ell = t + r + 1$ `[ABPSY17 §3]`: if the IPFE scheme is $r$-IND-CPA secure, the scheme is IND-CPA secure (Thm 15); if it is $(t + r)$-IND-CPA secure, the scheme is publicly traceable (Thm 16). Only the weak [[Inner-Product Functional Encryption#Random-key bounded collusion|random-key bounded-collusion]] security is needed.
- Instantiations from LWE, DDH and DCR (decision composite residuosity); the DDH one has ciphertexts and keys of size $O((r + t)\lambda)$ `[ABPSY17, abstract and §5]`.

### Properties
- [[Indistinguishability under Chosen-Plaintext Attack]] — the base game of the IND-CPA section

### Prerequisites
- [[Security Game]], [[Adversary]]
