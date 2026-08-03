## Encryption Scheme

> [!algorithm] Massey–Omura Three-Pass Cryptosystem
> **Participants:** Alice (sender), Bob (receiver)
>
> **Public Parameters:**  
> A large prime $p$
>
> **Plaintext Space:**  
> $$\mathcal{M} = \mathbb{F}_p^{*}$$
>
> **Ciphertext Space:**  
> $$\mathcal{C} = \mathbb{F}_p^{*}$$
>
> **Key Space:**  
> Each user chooses a secret exponent in $\mathbb{Z}_{p-1}^{*}$
>
> **Output:**  
> Bob recovers Alice’s plaintext $m$
>
> ---
>
> ### Key Selection
>
> 1. Alice chooses a secret exponent $a \in \mathbb{Z}_{p-1}^{*}$
>    and computes its inverse
>    $$a^{-1} \pmod{p-1}.$$
>
> 2. Bob chooses a secret exponent $b \in \mathbb{Z}_{p-1}^{*}$
>    and computes its inverse
>    $$b^{-1} \pmod{p-1}.$$
>
> ---
>
> ### Message Transmission
>
> **Input:** Plaintext $m \in \mathcal{M}$
>
> 1. Alice computes
>    $$u \gets m^{a} \pmod p$$
>    and sends $u$ to Bob.
>
> 2. Bob computes
>    $$v \gets u^{b} \pmod p$$
>    and sends $v$ to Alice.
>
> 3. Alice computes
>    $$w \gets v^{a^{-1}} \pmod p$$
>    and sends $w$ to Bob.
>
> 4. Bob computes
>    $$m \gets w^{b^{-1}} \pmod p,$$
>    recovering the plaintext.

> [!remark]
> If Eve can solve [[Discrete Logarithm Problem#Discrete Logarithm Problem|DLP]], Eve can break this cryptosystem.
> If Eve can solve [[Diffie-Hellman Key Exchange#Diffie-Hellman Problem|Diffie-Hellman Problem]], Eve can break this cryptosystem.

## Elliptic Version

> [!algorithm] Elliptic-Curve Massey–Omura Three-Pass Cryptosystem
> **Participants:** Alice (sender), Bob (receiver)
>
> **Public Parameters:**  
> - A finite field $\mathbb{F}_q$  
> - An elliptic curve $E / \mathbb{F}_q$  
> - A base point $P \in E(\mathbb{F}_q)$ of prime order $n$
>
> **Plaintext Space:**  
> $$\mathcal{M} = \langle P \rangle \subset E(\mathbb{F}_q)$$
>
> **Ciphertext Space:**  
> $$\mathcal{C} = \langle P \rangle$$
>
> **Key Space:**  
> Each user chooses a secret scalar in $\mathbb{Z}_n^{*}$
>
> **Output:**  
> Bob recovers Alice’s plaintext point $M$
>
> ---
>
> ### Key Selection
>
> 1. Alice chooses a secret scalar
>    $$a \in \mathbb{Z}_n^{*}$$
>    and computes its inverse
>    $$a^{-1} \pmod n.$$
>
> 2. Bob chooses a secret scalar
>    $$b \in \mathbb{Z}_n^{*}$$
>    and computes its inverse
>    $$b^{-1} \pmod n.$$
>
> ---
>
> ### Message Transmission
>
> **Input:** Plaintext point $M \in \mathcal{M}$
>
> 1. Alice computes
>    $$U \gets a M$$
>    and sends $U$ to Bob.
>
> 2. Bob computes
>    $$V \gets b U = ab M$$
>    and sends $V$ to Alice.
>
> 3. Alice computes
>    $$W \gets a^{-1} V = b M$$
>    and sends $W$ to Bob.
>
> 4. Bob computes
>    $$M \gets b^{-1} W,$$
>    recovering the plaintext.
