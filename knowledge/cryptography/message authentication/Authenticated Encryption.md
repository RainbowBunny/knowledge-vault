
| Term                                   | Reference                                       |                |
| -------------------------------------- | ----------------------------------------------- | -------------- |


## Basic Definition

> [!definition] Authenticated Encryption
> We say that a cipher $\mathcal E = (E, D)$ provides **authenticated encryption**, or is simply **AE-secure**, if $\mathcal E$ is 
> 1. Semantically secure under a [[Encryption#Chosen Plaintext Attack Security|CPA attack]].
> 2. Provides [[Encryption#Ciphertext Integrity|ciphertext integrity]].

> [!definition] One-time Authenticated Encryption
> We say that a cipher $\mathcal E = (E, D)$ provides **one-time authenticated encryption**, or is 1AE-**secure** for short, if $\mathcal E$ is semantically secure and provides one-time [[Encryption#Ciphertext Integrity|ciphertext integrity]].

> [!theorem]
> Let $\mathcal E = (E, D)$ be a cipher. If $\mathcal E$ is AE-secure, then it is CCA-secure. If $\mathcal E$ is 1AE-secure, then it is 1CCA-secure.
> 
> In particular, suppose $\mathcal A$ is a [[Encryption#Chosen Ciphertext Attack Security|CCA security]] adversary for $\mathcal E$ that makes at most $Q_e$ encryption queries and $Q_d$ decryption queries. Then there exist a [[Encryption#Chosen Plaintext Attack Security|CPA security]] $\mathcal B_{cpa}$ and a [[Encryption#Ciphertext Integrity|ciphertext integrity]] $\mathcal B_{ci}$, where $\mathcal B_{cpa}$ and $\mathcal B_{ci}$ are elementary wrappers around $\mathcal A$, such that $$\text{CCAadv}[\mathcal A, \mathcal E] \leq \text{CPAadv}[\mathcal B_{cpa}, \mathcal E] + 2 Q_d \cdot \text{CIadv}[\mathcal B_{ci}, \mathcal E].$$
> Moreover, $\mathcal B_{cpa}$ and $\mathcal B_{ci}$ both make at most $Q_e$ encryption queries.

