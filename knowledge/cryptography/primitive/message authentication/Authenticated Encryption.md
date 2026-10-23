Reference:
- `[BS]` — D. Boneh, V. Shoup, _A Graduate Course in Applied Cryptography_, v0.6, 2023: https://toc.cryptobook.us/ (Ch. 9, Attack Game 9.1). `⚠️ CLAUDE – verify:` WebFetch returns only the first ~17 pages of the book, so Attack Game 9.1 could not be read; the table redraws the wording this note already had. Check it against the book.
- `⚠️ CLAUDE – verify:` — a point I could not check against the source.

## Ciphertext Integrity

> [!definition] SKE Ciphertext Integrity Advantage
> For a cipher $\mathcal E = (E, D)$ over $(\mathcal K, \mathcal M, \mathcal C)$ and an adversary $\mathcal A$:
>
> A search game: one branch. `[BS Attack Game 9.1]`
>
> | | challenger $\mathcal C$ | | adversary $\mathcal A$ |
> | --- | --- | --- | --- |
> | 1 | $k \xleftarrow{R} \mathcal K$ | | |
> | 2 | | $\xleftarrow{\ m_i\ }$ | **Encryption queries** (repeated, adaptive): sends $m_i \in \mathcal M$, for $i = 1, 2, \dots$ |
> | | $c_i \xleftarrow{R} E(k, m_i)$ | $\xrightarrow{\ c_i\ }$ | |
> | 3 | | $\xleftarrow{\ c\ }$ | outputs a candidate ciphertext $c \in \mathcal C$ |
> | 4 | $m \leftarrow D(k, c)$ | | |
>
> **Goal** — $\mathcal A$ wins iff all hold:
> - $c \notin \{c_1, c_2, \dots\}$: $c$ is not a ciphertext it was given;
> - $m \neq \text{reject}$: $c$ decrypts.
>
> Define $\text{CIadv}[\mathcal A, \mathcal E] = \Pr[\mathcal A \text{ wins}]$. $\mathcal A$ is a **$Q$-query adversary** if it issues at most $Q$ encryption queries.

> [!definition] Ciphertext Integrity
> A cipher $\mathcal E$ provides **ciphertext integrity** (CI) if $\text{CIadv}[\mathcal A, \mathcal E]$ is negligible for every efficient $\mathcal A$.

> [!definition] One-time Ciphertext Integrity
> $\mathcal E$ provides **one-time ciphertext integrity** if $\text{CIadv}[\mathcal A, \mathcal E]$ is negligible for every efficient single-query $\mathcal A$.

## Definition

> [!definition] Authenticated Encryption
> We say that a cipher $\mathcal E = (E, D)$ provides **authenticated encryption**, or is simply **AE-secure**, if $\mathcal E$ is 
> 1. Semantically secure under a [[Symmetric Key Encryption#Indistinguishability|CPA attack]].
> 2. Provides [[#Ciphertext Integrity|ciphertext integrity]].

> [!definition] One-time Authenticated Encryption
> We say that a cipher $\mathcal E = (E, D)$ provides **one-time authenticated encryption**, or is 1AE-**secure** for short, if $\mathcal E$ is semantically secure and provides one-time [[#Ciphertext Integrity|ciphertext integrity]].

> [!theorem]
> Let $\mathcal E = (E, D)$ be a cipher. If $\mathcal E$ is AE-secure, then it is CCA-secure. If $\mathcal E$ is 1AE-secure, then it is 1CCA-secure.
> 
> In particular, suppose $\mathcal A$ is a [[Symmetric Key Encryption#Indistinguishability|CCA security]] adversary for $\mathcal E$ that makes at most $Q_e$ encryption queries and $Q_d$ decryption queries. Then there exist a [[Symmetric Key Encryption#Indistinguishability|CPA security]] $\mathcal B_{cpa}$ and a [[#Ciphertext Integrity|ciphertext integrity]] $\mathcal B_{ci}$, where $\mathcal B_{cpa}$ and $\mathcal B_{ci}$ are elementary wrappers around $\mathcal A$, such that $$\text{CCAadv}[\mathcal A, \mathcal E] \leq \text{CPAadv}[\mathcal B_{cpa}, \mathcal E] + 2 Q_d \cdot \text{CIadv}[\mathcal B_{ci}, \mathcal E].$$
> Moreover, $\mathcal B_{cpa}$ and $\mathcal B_{ci}$ both make at most $Q_e$ encryption queries.
