---
dg-publish: true
---
Reference:
- `[DN08]` — I. Damgård, J. B. Nielsen, _Commitment Schemes and Zero-Knowledge Protocols_, lecture notes (2008), §2: https://homepages.cwi.nl/~schaffne/courses/crypto/2014/papers/ComZK08.pdf
- ePrint 2025/2099 — M. S. Ahmadi, T. Eghlidos, B. Abdolmaleki, N. K. Nguyen, _A Lattice-based Designated Verifier zkSNARK from Standard Assumptions_: https://eprint.iacr.org/2025/2099 — uses commitments; not used for the definitions below.
- `⚠️ CLAUDE – verify:` — added by me, not taken from a source.

## Intuition

> [!example] Coin Flipping by Telephone
> Suppose Alice and Bob are getting a divorce but they can not even stand facing each other, so they have to discuss over the phone how to split the furniture, the kids, etc. Since they can not agree who get which, they decide to flip a coin. To make the game fair, we can use a simple protocol:
> 1. Alice commits to a random bit $b_A$, and sends the resulting commitment $C$ to Bob.
> 2. Bob chooses a random bit $b_B$ and sends it to Alice.
> 3. Alice opens $C$ to let Bob learn $b_A$, and both parties compute the result, which is $b = b_A \oplus b_B$.

> [!remark] The box
> Committing is like putting a message in a locked box and giving the box away: having given it away, the sender cannot change what is inside (*binding*); the receiver cannot tell what is inside until the sender hands over the key (*hiding*). `[DN08 §2.1]`

## Syntax

> [!definition] Parameters
> - $\lambda$: the security parameter (`[DN08]` writes $l$).
> - $\mathcal M$: the message space; `[DN08]` commits to bits, $\mathcal M = \{0, 1\}$.
> - $\mathrm{pk}$: the public key of the scheme. $r \in \{0, 1\}^\lambda$: the randomness of a commitment.
>
> `[DN08 §2.3]`

> [!definition] Commitment Scheme
> A **commitment scheme** consists of
> - $\mathrm{pk} \leftarrow \mathsf{Setup}(1^\lambda)$: a probabilistic polynomial-time generator that outputs the public key;
> - for every $\mathrm{pk}$, a function $\mathsf{Com}_\mathrm{pk}: \{0, 1\}^\lambda \times \mathcal M \to \{0, 1\}^\lambda$.
>
> It is used in three phases:
> - **Set-up** — one party runs $\mathsf{Setup}$ and sends $\mathrm{pk}$ to the other, who checks it and accepts or rejects.
> - **Commit** — to commit to $m$, the sender chooses $r \leftarrow \{0, 1\}^\lambda$ and sends $C \leftarrow \mathsf{Com}_\mathrm{pk}(r, m)$.
> - **Open** — the sender reveals $(r, m)$, and the receiver checks that $C = \mathsf{Com}_\mathrm{pk}(r, m)$.
>
> `[DN08 §2.3]`, which calls the generator $G$ and writes $\mathsf{commit}_\mathrm{pk}(r, b)$.

> [!remark] Opening strings
> `⚠️ CLAUDE – verify:` many papers write the scheme as $(c, o) \leftarrow \mathsf{Com}(\mathrm{pp}, m)$ with an opening string $o$ and a verification algorithm $\mathsf{Verify}(\mathrm{pp}, m, c, o)$; the form above is the case $o = r$ with $\mathsf{Verify}$ recomputing the commitment.

## Property

### Correctness

> [!proposition] Correctness — an honest opening is always accepted
> The receiver recomputes $\mathsf{Com}_\mathrm{pk}(r, m)$ from the revealed $(r, m)$, so an honest opening of $C = \mathsf{Com}_\mathrm{pk}(r, m)$ always passes the check.

## Security

### Binding

> [!definition] Unconditional Binding
> If $\mathrm{pk}$ is correctly generated, then $m$ is uniquely determined by $\mathsf{Com}_\mathrm{pk}(r, m)$: even an unbounded sender cannot change its mind after committing. `[DN08 §2.3, type 1]`

> [!definition] Computational Binding
> ### Scope
> A commitment scheme and a probabilistic polynomial-time sender $\mathcal A$ (`[DN08]`: $P^*$).
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pk}$, produced by $\mathsf{Setup}(1^\lambda)$; no oracle.
> - **Promise** — none.
> - **Quantifier** — $\forall$ PPT $\mathcal A$.
> - **Adaptivity** — $\mathcal A$ speaks once, after seeing $\mathrm{pk}$.
>
> ---
> ### Experiment
> A search game with one branch. `[DN08 §2.3, type 2]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\mathrm{pk} \leftarrow \mathsf{Setup}(1^\lambda)$ | $\xrightarrow{\ \mathrm{pk}\ }$ | |
> | 2 | | $\xleftarrow{\ C,\, m,\, r,\, m',\, r'\ }$ | outputs a commitment and two openings |
>
> **Goal** — $\mathcal A$ wins iff both:
> - $m \neq m'$;
> - $\mathsf{Com}_\mathrm{pk}(r, m) = C = \mathsf{Com}_\mathrm{pk}(r', m')$.
>
> ---
> ### Property
> $$\varepsilon(\lambda) = \Pr[\mathcal A \text{ wins}],$$
> over the coins of $\mathsf{Setup}$ and $\mathcal A$. The scheme is **computationally binding** if $\varepsilon$ is negligible for every PPT $\mathcal A$. `[DN08 §2.3]`

### Hiding

> [!definition] Hiding
> ### Scope
> A commitment scheme with $\mathcal M = \{0, 1\}$ and an adversary $\mathcal A$ — polynomial-time for computational hiding, unbounded for statistical or perfect hiding.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $\mathrm{pk}$ and one commitment.
> - **Promise** — $\mathrm{pk}$ is correctly generated.
> - **Quantifier** — $\forall \mathcal A$ in the class of the Scope.
> - **Adaptivity** — none.
>
> ---
> ### Experiment
> A distinguishing game: the two branches differ in the committed bit only. `[DN08 §2.3]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $\mathrm{pk} \leftarrow \mathsf{Setup}(1^\lambda)$<br>$r \leftarrow \{0, 1\}^\lambda$<br>**Game 0**: $C \leftarrow \mathsf{Com}_\mathrm{pk}(r, 0)$<br>**Game 1**: $C \leftarrow \mathsf{Com}_\mathrm{pk}(r, 1)$ | $\xrightarrow{\ \mathrm{pk},\, C\ }$ | |
> | 2 | | $\xleftarrow{\ b'\ }$ | outputs a bit $b'$ |
>
> **Goal**
> - **Output** — $\mathsf{Expt}_b(\mathcal A)$, the bit $b'$ in Game $b$.
> - **Measure** — how far apart $\Pr[\mathsf{Expt}_0(\mathcal A) = 1]$ and $\Pr[\mathsf{Expt}_1(\mathcal A) = 1]$ are.
>
> ---
> ### Property
> $$\mathsf{Adv}^\mathsf{hide}(\mathcal A) = \big|\Pr[\mathsf{Expt}_0(\mathcal A) = 1] - \Pr[\mathsf{Expt}_1(\mathcal A) = 1]\big|.$$
> - **Computationally hiding**: negligible for every PPT $\mathcal A$, i.e. $(\mathrm{pk}, \mathsf{Com}_\mathrm{pk}(r, 0)) \sim_c (\mathrm{pk}, \mathsf{Com}_\mathrm{pk}(s, 1))$. `[DN08 §2.3, type 1]`
> - **Statistically (unconditionally) hiding**: negligible for every $\mathcal A$, i.e. $\mathsf{Com}_\mathrm{pk}(r, 0) \sim_s \mathsf{Com}_\mathrm{pk}(s, 1)$ for correctly generated $\mathrm{pk}$. `[DN08 §2.3, type 2]`
> - **Perfectly hiding**: the two distributions are identical, $\sim_p$. `[DN08 §2.3]`
>
> The relations $\sim_c, \sim_s, \sim_p$ are those of [[Indistinguishability]] `[DN08 Def 3]`.

> [!remark] Messages longer than a bit
> `⚠️ CLAUDE – verify:` for a larger $\mathcal M$ the usual game lets $\mathcal A$ choose $m_0, m_1 \in \mathcal M$ after seeing $\mathrm{pk}$ and commits to $m_b$; `[DN08]` treats bit commitments only.

## Variant

### The two types, and why not both
- **Type 1** — unconditionally binding, computationally hiding: the sender runs $\mathsf{Setup}$ and sends $\mathrm{pk}$ to the receiver, who verifies it.
- **Type 2** — computationally binding, unconditionally hiding: the receiver runs $\mathsf{Setup}$.
- Both unconditional at once is impossible between two parties, because each sees everything the other sends; it becomes possible in distributed or noisy-channel settings. `[DN08 §2.3]`

## Related

### Prerequisites
- [[Security Game]], [[Indistinguishability]], [[Adversary]]
