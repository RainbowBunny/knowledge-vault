Reference:
- `[HHK17]` — D. Hofheinz, K. Hövelmanns, E. Kiltz, _A Modular Analysis of the Fujisaki-Okamoto Transformation_, TCC 2017 (ePrint 2017/604): https://eprint.iacr.org/2017/604 (§2.2 KEM syntax and correctness; Definition 2.4 and Figure 4, IND-CCA).

## Syntax

> [!definition] Key Encapsulation Mechanism Scheme
> A **key encapsulation scheme** $\text{KEM} = (\mathsf{KeyGen}, \text{Encaps}, \text{Decaps})$ is a triple of efficient algorithms with a ciphertext space $\mathcal C$, a key space $\mathcal K$ and a random space $\mathcal R$.
> - $(pk, sk) \leftarrow \mathsf{KeyGen}()$: The key-generation algorithm $\mathsf{KeyGen}$ returns a pair $(pk, sk)$ consisting of a public key $pk$ and a secret key $sk$.
> - $(c, K) \leftarrow \text{Encaps}(pk; r)$: The encapsulation algorithm $\text{Encaps}$ takes a public key $pk$ and a random $r \in \mathcal R$ to produce a ciphertext $c \in \mathcal C$ and a key $K \in \mathcal K$.
> - $K \leftarrow \text{Decaps}(sk, c)$: The deterministic decapsulation algorithm $\text{Decaps}$ takes a secret key $sk$ and a ciphertext $c$, and outputs either a key $K \in \mathcal K$ or a special symbol $\perp$ to indicate **rejection**.

> [!remark] Notation in the literature
> `[HHK17 §2.2]` calls key generation $\mathsf{Gen}$, lets $\mathrm{pk}$ define the key space $\mathcal K$, and writes the output of $\mathsf{Encaps}$ in the order $(K, c)$; this note writes $(c, K)$. The vault calls key generation $\mathsf{KeyGen}$ ([[Note Layouts]] § *Game form*).

## Property

### Correctness

> [!definition] KEM $(1 - \delta)$-Correctness
> A key encapsulation scheme $\text{KEM}$ is $(1 - \delta)$-correct if $$\Pr[\text{Decaps}(sk, c) = K \; | \; (c, K) \leftarrow \text{Encaps}(pk)] \geq 1 - \delta$$ where the probability is taken over $(pk, sk) \leftarrow \mathsf{KeyGen}()$ and the random coins of $\text{Encaps}$. `[HHK17 §2.2]` states the same condition as $\Pr[\text{Decaps}(sk, c) \neq K] \leq \delta$ and calls the scheme $\delta$-correct.

## Security

### Indistinguishability under Chosen-Ciphertext Attacks

> [!definition] IND-CCA Advantage of KEM
> A distinguishing game: two branches that differ in row 1 only, **Game 0** (the real key) and **Game 1** (a uniform key). `[HHK17 Def 2.4, Fig. 4]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(pk, sk) \leftarrow \mathsf{KeyGen}()$<br>$(c^*, K_0^*) \leftarrow \text{Encaps}(pk)$<br>$K_1^* \xleftarrow{\$} \mathcal K$<br>**Game 0**: $K^* \leftarrow K_0^*$<br>**Game 1**: $K^* \leftarrow K_1^*$ | $\xrightarrow{\ pk,\, c^*,\, K^*\ }$ | |
> | 2 | | $\xleftarrow{\ c\ }$ | **Decapsulation queries** (repeated, adaptive): sends $c \in \mathcal C$ with $c \neq c^*$ |
> | | $K \leftarrow \text{Decaps}(sk, c)$ | $\xrightarrow{\ K\ }$ | |
> | 3 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are:
> $$\text{Adv}_\text{KEM}^{\text{cca}}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
>
> $\text{KEM}$ is **IND-CCA secure** if $\text{Adv}_\text{KEM}^{\text{cca}}(\mathcal A)$ is negligible for every efficient adversary $\mathcal A$. It is a *distinguishing* game, see [[Security Game]].

> [!remark] The source's form
> `[HHK17 Fig. 4]` samples $b \xleftarrow{\$} \{0, 1\}$, runs $b' \leftarrow \mathcal A^{\mathsf{Decaps}}(c^*, K_b^*)$ with an oracle that refuses $c^*$, and defines $\mathsf{Adv}^{\mathsf{IND\text{-}CCA}}_{\mathsf{KEM}}(\mathcal A) = |\Pr[b' = b] - 1/2|$. The difference above is twice that, see [[Indistinguishability under Chosen-Plaintext Attack#Bit-guessing form]]. The figure does not list $pk$ among the adversary's inputs; it is sent in row 1 here. There is no query phase before the challenge: $c^*$ and $K^*$ exist before $\mathcal A$ starts.
