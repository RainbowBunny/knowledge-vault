Reference:
- `[BS]` — D. Boneh, V. Shoup, _A Graduate Course in Applied Cryptography_, v0.6, 2023: https://toc.cryptobook.us/ (§4.7, the ideal cipher model; Ch. 8, the list guessing game and the random oracle). `⚠️ CLAUDE – verify:` WebFetch returns only the first ~17 pages of the book, so neither part could be read: the tables redraw the wording this note already had.
- `⚠️ CLAUDE – verify:` — a point I could not check against the source.

## The Ideal Cipher Model

### Ideal Block Model

> [!definition] Parameters
> - $\mathcal S$: a cryptographic scheme that uses a block cipher $\mathcal E = (E, D)$, defined over $(\mathcal K, \mathcal X)$, as an oracle.
> - X: the attack game defining the security of $\mathcal S$, with its standard queries and its advantage $\text{Xadv}[\mathcal A, \mathcal S]$.
> - $\{\Pi_k\}_{k \in \mathcal K}$: the ideal cipher, one uniform permutation $\Pi_k \in \text{Perms}[\mathcal X]$ for each key.
> - $Q_s$, $Q_{ic}$: the numbers of standard queries and of ideal cipher queries.

> [!definition] Ideal Block Model
> Suppose we have some type of cryptographic scheme $\mathcal S$ whose implementation makes use of a block cipher $\mathcal E = (E, D)$ defined over $(\mathcal K, \mathcal X)$. Moreover, suppose the scheme $\mathcal S$ evaluates $E$ at various inputs $(k, a) \in \mathcal K \times \mathcal X$, and $D$ at various inputs $(k, b) \in \mathcal K \times \mathcal X$, but does not look at the internal implementation of $\mathcal E$. In this case, we say that $\mathcal S$ **uses $\mathcal E$ as an oracle**.
> 
> To analyze $\mathcal S$ in the ideal cipher model, the attack game defining security is modified so that $\mathcal E$ is effectively replaced by a family of random permutations $\{\Pi_{k}\}_{k \in \mathcal K}$ to which both the adversary and the challenger have oracle access.
>
> ### Scope
> The scheme $\mathcal S$, its attack game X and all efficient adversaries.
>
> ---
> ### Condition
> - **Access** — the standard queries of X, plus **ideal cipher queries** of two types: $\Pi$-queries and $\Pi^{-1}$-queries. The adversary may make any number of ideal cipher queries, arbitrarily interleaved with standard queries.
> - **Promise** — that of X.
> - **Quantifier** — that of X; bounds count the standard queries ($Q_s$) and the ideal cipher queries ($Q_{ic}$) separately.
> - **Adaptivity** — that of X; each ideal cipher query may depend on all earlier answers.
>
> ---
> ### Experiment
> The game X with the rows below added; its own rows, and its branches if it is a distinguishing game, stay as they are. `[BS §4.7]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 0 | at the beginning of the game, for each $k \in \mathcal K$:<br>$\Pi_k \xleftarrow{\$} \text{Perms}[\mathcal X]$ | | |
> | 1 | | $\xleftarrow{\ (k,\, a)\ }$ | **$\Pi$-queries** (repeated, adaptive, interleaved with the rows of X): sends $(k, a) \in \mathcal K \times \mathcal X$ |
> | | $b \leftarrow \Pi_k(a)$ | $\xrightarrow{\ b\ }$ | |
> | 2 | | $\xleftarrow{\ (k,\, b)\ }$ | **$\Pi^{-1}$-queries** (repeated, adaptive, interleaved with the rows of X): sends $(k, b) \in \mathcal K \times \mathcal X$ |
> | | $a \leftarrow \Pi^{-1}_k(b)$ | $\xrightarrow{\ a\ }$ | |
> | 3 | in processing the standard queries of X:<br>uses $\Pi_k(a)$ in place of $E(k, a)$<br>uses $\Pi^{-1}_k(b)$ in place of $D(k, b)$ | | |
>
> **Goal**
> - The goal of X, unchanged.
>
> ---
> ### Property
> - The adversary's advantage is defined using the same rule as in X, but is denoted $\text{X}^{ic}\text{adv}[\mathcal A, \mathcal S]$.
> - Security in the ideal cipher model means that $\text{X}^{ic}\text{adv}[\mathcal A, \mathcal S]$ is negligible for all efficient adversaries $\mathcal A$.

> [!remark]
> - Instances in [[Block Ciphers]]: $\text{BC}^{ic}\text{adv}$ ([[Block Ciphers#Secure Block Cipher|Attack Game 4.1]] in this model, for Triple-DES and $\mathcal EX$) and $\text{KR}^{ic}\text{adv}$ ([[Block Ciphers#Key Recovery|Attack Game 4.4]] in this model, for exhaustive search).

### Ideal Permutation Model

> [!algorithm] Ideal Permutation Model
> Some constructions, make use of a permutation $\pi: \mathcal X \rightarrow \mathcal X$, rather than a block cipher.

### List Guessing Advantage

> [!definition] Parameters
> - $P$: a probability distribution on a finite set $\mathcal S$; $I$: a function on $\mathcal S$, the adversary's side information — as in [[Key Derivation Problem]].
> - $Q$: the length of the list of guesses.

> [!definition] List Guessing Advantage
> ### Scope
> The pair $(P, I)$ and all efficient adversaries.
>
> ---
> ### Condition
> - **Access** — $\mathcal A$ receives $I(s)$ and nothing else.
> - **Promise** — none.
> - **Quantifier** — $\forall$ efficient $\mathcal A$ that outputs a list of at most $Q$ guesses.
> - **Adaptivity** — none: one message each way.
>
> ---
> ### Experiment
> A search game: one branch. It generalizes the [[Key Derivation Problem|guessing advantage]] game: the adversary outputs a list of guesses instead of one. `[BS Ch. 8]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $s \leftarrow P$ | $\xrightarrow{\ I(s)\ }$ | |
> | 2 | | $\xleftarrow{\ \hat s_1, \dots, \hat s_Q\ }$ | outputs a list of guesses $\hat s_1, \dots, \hat s_Q \in \mathcal S$ |
> | 3 | compares each $\hat s_i$ with $s$ | | |
>
> **Goal** — $\mathcal A$ wins iff any of:
> - $\hat s_i = s$ for some $i = 1, \dots, Q$.
>
> ---
> ### Property
> $$\text{ListGuessadv}[\mathcal A, P, I] = \Pr[\mathcal A \text{ wins}].$$
> - $\mathcal A$'s probability of winning in this game is called his **list guessing advantage**. With $Q = 1$ it is $\text{Guessadv}[\mathcal A, P, I]$ of [[Key Derivation Problem]].

> [!theorem]
> If $H$ is modeled as a random oracle, then for every distinguishing adversary $\mathcal A$ that makes at most $Q_{ro}$ random oracle queries, there exists a list guessing adversary $\mathcal B$, which is an elementary wrapper around $\mathcal A$, such that $$\text{Dist}^{ro}\text{adv}[\mathcal A, P, I, H] \leq \text{ListGuessadv}[\mathcal B, P, I]$$ and $\mathcal B$ outputs a list of size at most $Q_{ro}$. In particular, there exists a guessing adversary $\mathcal B'$, which is an elementary wrapper around $\mathcal A$, such that $$\text{Dist}^{ro}\text{adv}[\mathcal A, P, I, H] \leq Q_{ro} \cdot \text{Guessadv}[\mathcal B', P, I].$$
 
