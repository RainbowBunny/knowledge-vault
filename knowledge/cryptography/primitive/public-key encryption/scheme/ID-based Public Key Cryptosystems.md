## Encryption Scheme

> [!algorithm] Identity-Based Encryption (Boneh–Franklin Scheme)
> **Participants:** Trusted Authority (Tom), Alice (receiver), Bob (sender)
>
> **Public Parameters:**  
> - A finite field $\mathbb{F}_q$  
> - An elliptic curve $E / \mathbb{F}_q$  
> - A point $P \in E(\mathbb{F}_q)$ of prime order $\ell$  
> - An $\ell$-distortion map $\phi$ for $P$  
> - Hash functions:
>   $$H_1 : \{ID\} \to E(\mathbb{F}_q), \qquad
>     H_2 : \mathbb{F}_q^{*} \to \{0,1\}^{\ell}$$
>
> **Output:**  
> Correct encryption and decryption of a message $M$ using an identity-based
> public key
>
> ---
>
> ### Setup (Trusted Authority)
>
> 1. Tom chooses a secret master key:
>    $$s \in \mathbb{Z}_\ell.$$
>
> 2. Tom computes and publishes the public key:
>    $$P_{\text{Tom}} \gets sP \in E(\mathbb{F}_q).$$
>
> ---
>
> ### Private Key Extraction (for Alice)
>
> 1. Alice chooses an identity-based public key:
>    $$ID_{\text{Alice}}.$$
>
> 2. Tom computes:
>    $$P_{\text{Alice}} \gets H_1(ID_{\text{Alice}}) \in E(\mathbb{F}_q).$$
>
> 3. Tom computes Alice’s private key:
>    $$Q_{\text{Alice}} \gets sP_{\text{Alice}} \in E(\mathbb{F}_q).$$
>
> 4. Tom securely sends $Q_{\text{Alice}}$ to Alice.
>
> ---
>
> ### Encryption (Bob)
>
> **Input:** Plaintext message $M$ and identity $ID_{\text{Alice}}$
>
> 1. Bob chooses a random integer:
>    $$r \in \mathbb{Z}_{\ell}.$$
>
> 2. Bob computes:
>    $$P_{\text{Alice}} \gets H_1(ID_{\text{Alice}}).$$
>
> 3. Bob computes the ciphertext components:
>    $$\begin{aligned}
>    C_1 &\gets rP, \\
>    C_2 &\gets M \oplus H_2\!\left(
>      \hat{e}_\ell(P_{\text{Alice}}, P_{\text{Tom}})^{\,r}
>    \right).
>    \end{aligned}$$
>
> 4. Bob sends the ciphertext:
>     $$C = (C_1, C_2).$$
>
> ---
>
> ### Decryption (Alice)
>
> 1. Alice recovers the plaintext by computing:
>     $$M \gets C_2 \oplus H_2\!\left(
>       \hat{e}_\ell(Q_{\text{Alice}}, C_1)
>     \right).$$
