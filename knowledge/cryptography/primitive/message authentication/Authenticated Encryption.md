## Ciphertext Integrity

> [!definition] SKE Ciphertext Integrity Advantage
> For an adversary $\mathcal A$:
> - The challenger chooses $k \xleftarrow{R} \mathcal K$.
> - For $i = 1, 2, \dots$, $\mathcal A$ submits $m_i \in \mathcal M$; the challenger returns $c_i \xleftarrow{R} E(k, m_i)$.
> - $\mathcal A$ eventually outputs a candidate ciphertext $c \notin \{c_1, c_2, \dots\}$.
>
> $\mathcal A$ wins if $D(k, c) \neq \text{reject}$. Define $\text{CIadv}[\mathcal A, \mathcal E] = \Pr[\mathcal A \text{ wins}]$. $\mathcal A$ is a **$Q$-query adversary** if it issues at most $Q$ encryption queries.

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
