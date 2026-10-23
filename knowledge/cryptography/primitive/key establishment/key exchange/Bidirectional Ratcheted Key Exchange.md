---
aliases: [BRKE]
---
Reference:
- `[PR18]` — B. Poettering, P. Rösler, _Towards Bidirectional Ratcheted Key Exchange_, CRYPTO 2018; full version ePrint 2018/296, §7 and Fig. 10: https://eprint.iacr.org/2018/296.pdf

## Syntax

> [!definition] Parameters
> - $\mathcal K$: a finite key space. $\mathcal{AD}$: an associated-data space.
> - $\mathcal S$: the state space, shared by both users. $\mathcal C$: the ciphertext space.
> - $u \in \{A, B\}$: a user; $\bar u$: its peer, so $\{u, \bar u\} = \{A, B\}$.
>
> `[PR18 §7]`

> [!definition] Bidirectional Ratcheted Key Exchange
> A **BRKE scheme** for $\mathcal K$ and $\mathcal{AD}$ is a triple $R = (\mathsf{init}, \mathsf{snd}, \mathsf{rcv})$ of algorithms, together with $\mathcal S$ and $\mathcal C$:
> - $(S_A, S_B) \leftarrow \mathsf{init}$:
> 	- **Output**: a pair of states $(S_A, S_B) \in \mathcal S \times \mathcal S$, one for each user. Randomized.
> - $(S', k, c) \leftarrow \mathsf{snd}(S, \mathrm{ad})$:
> 	- **Input**: a state $S \in \mathcal S$ and an associated-data string $\mathrm{ad} \in \mathcal{AD}$.
> 	- **Output**: an updated state $S' \in \mathcal S$, a key $k \in \mathcal K$ and a ciphertext $c \in \mathcal C$. Randomized.
> - $(S', k) / \perp \leftarrow \mathsf{rcv}(S, \mathrm{ad}, c)$:
> 	- **Input**: a state $S \in \mathcal S$, an associated-data string $\mathrm{ad} \in \mathcal{AD}$ and a ciphertext $c \in \mathcal C$.
> 	- **Output**: an updated state $S' \in \mathcal S$ and a key $k \in \mathcal K$, or $\perp$ to indicate rejection. Deterministic.
>
> `[PR18 §7]`

> [!remark] Each message is a key exchange
> Every call of $\mathsf{snd}$ establishes a fresh key $k$ with the peer and moves the state forward — the *ratchet*. Either user may send at any time, so the keys flow in both directions. There are no long-term keys: $\mathsf{init}$ produces both states. `[PR18 §7]`

## Property

### Correctness

> [!definition] Correctness
> ### Scope
> A BRKE scheme $R$ and an adversary $\mathcal A$ that schedules the users, computationally unbounded.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ makes users send and receive, and chooses what each receives; it sees the ciphertexts, not the keys or states.
> - **Promise** — none.
> - **Quantifier** — $\forall \mathcal A$.
> - **Adaptivity** — fully adaptive scheduling.
>
> ---
> ### Experiment
> The game $\mathsf{FUNC}$; a user is *in sync* while everything it has received is, in order, what its peer sent. `[PR18 Fig. 10]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $(S_A, S_B) \leftarrow \mathsf{init}$<br>for $u \in \{A, B\}$: $s_u \leftarrow 0$, $r_u \leftarrow 0$, $\mathrm{sync}_u \leftarrow \mathsf{true}$ | | |
> | 2 | | $\xleftarrow{\ u,\, \mathrm{ad}\ }$ | **Send queries** (repeated, adaptive) |
> | | $(S_u, k, c) \leftarrow \mathsf{snd}(S_u, \mathrm{ad})$<br>if $\mathrm{sync}_u$: record $(\mathrm{ad}, c)$ as message $s_u$ of $u$<br>$\mathrm{key}_u[s_u] \leftarrow k$<br>$s_u \leftarrow s_u + 1$ | $\xrightarrow{\ c\ }$ | |
> | 3 | | $\xleftarrow{\ u,\, \mathrm{ad},\, c\ }$ | **Receive queries** (repeated, adaptive) |
> | | if $(\mathrm{ad}, c)$ is not message $r_u$ of $\bar u$: $\mathrm{sync}_u \leftarrow \mathsf{false}$<br>$(S_u, k) \leftarrow \mathsf{rcv}(S_u, \mathrm{ad}, c)$, stopping on $\perp$<br>check the Goal<br>$r_u \leftarrow r_u + 1$ | | |
>
> **Goal** — $\mathcal A$ wins iff at some receive query both:
> - $\mathrm{sync}_u = \mathsf{true}$;
> - $k \neq \mathrm{key}_{\bar u}[r_u]$.
>
> ---
> ### Property
> $R$ is **correct** if $\Pr[\mathcal A \text{ wins}] = 0$ for every $\mathcal A$. `[PR18 §7]`

> [!remark] Simplified from the source
> Fig. 10 also keeps epoch counters and refuses users whose state has become $\perp$; they matter for the security games (Fig. 11), not for the winning condition, and are left out here. A user that receives something its peer did not send leaves sync for good and is no longer checked. `[PR18 Fig. 10]`

## Variant

- **Unidirectional** (URKE, `[PR18 §3]`): only $A$ sends, with separate state spaces for sender and receiver.
- **Sesquidirectional** (SRKE, `[PR18 §5–6]`).

## Related

### Siblings
- [[Key Exchange]], [[Authenticated Key Exchange]]
- [[Key Encapsulation Mechanism]] — a one-shot exchange
