
**Notation**:
- Key space: $\mathcal K$ where each element $k = (k_{priv}, k_{pub})$
- Plaintext space: $\mathcal M$
- Ciphertext space: $\mathcal C$
- Encryption function $e_{k_{pub}}: \mathcal M \rightarrow \mathcal C,$
- Decryption function $d_{k_{priv}}: \mathcal C \rightarrow \mathcal M$.
Property: If the pair $(k_{priv}, k_{pub})$ is in the key space $\mathcal K$: $$d_{k_{priv}} (e_{k_{pub}}(m)) = m \qquad \text{for all } m \in \mathcal M.$$
> [!definition] Ephemeral key
> Key that exists only for the purposes of encrypting a single message.

> [!definition] Probabilistic encryption

### Encryption Scheme

- [[A Congruential Public Key Cryptosystem]]
- [[ElGamal Public Key Cryptosystem]]
- [[Goldwasser–Micali Cryptosystem]]
- [[GGH Public Key Cryptosystem]]
- [[ID-based Public Key Cryptosystems]]
- [[Massey-Omura Three-Pass Cryptosystem]]
- [[Merkle–Hellman Subset-Sum Cryptosystem]]
- [[NTRU Public Key Cryptosystem]]
- [[RSA Public Key Cryptosystem]]

### CRT-Bases Public Key Cryptosystem

> [!algorithm] CRT-Based Public Key Cryptosystem (Insecure)
> **Participants:** Alice (receiver), Bob (sender)
>
> **Public Parameters:**  
> A composite modulus $N = pq$, where $p$ and $q$ are large secret primes
>
> **Plaintext Space:**  
> $$\mathcal{M} = \mathbb{Z}_N$$
>
> **Ciphertext Space:**  
> $$\mathcal{C} = \mathbb{Z}_N \times \mathbb{Z}_N$$
>
> **Key Space:**  
> - Public key: $(N, g_1, g_2)$  
> - Private key: $(p,q)$
>
> **Output:**  
> Bob encrypts a message $m$, and Alice correctly recovers $m$
>
> ---
>
> ### Key Creation (Alice)
>
> 1. Choose two large primes $p$ and $q$ and set
>    $$N \gets pq.$$
>
> 2. Choose random elements $g, r_1, r_2 \in \mathbb{Z}_N$.
>
> 3. Compute
>    $$g_1 \gets g^{\,r_1(p-1)} \pmod N,$$
>    $$g_2 \gets g^{\,r_2(q-1)} \pmod N.$$
>
> 4. Publish the public key $(N, g_1, g_2)$ and keep $(p,q)$ secret.
>
> ---
>
> ### Encryption (Bob)
>
> **Input:** Plaintext $m \in \mathcal{M}$
>
> 1. Choose random exponents $s_1, s_2 \in \mathbb{Z}_N$.
>
> 2. Compute the ciphertext components:
>    $$c_1 \gets m \, g_1^{s_1} \pmod N,$$
>    $$c_2 \gets m \, g_2^{s_2} \pmod N.$$
>
> 3. Send the ciphertext $(c_1, c_2)$ to Alice.
>
> ---
>
> ### Decryption (Alice)
>
> 1. Using the Chinese Remainder Theorem, compute the unique solution
>    $$x \in \mathbb{Z}_N$$
>    to the system
>    $$x \equiv c_1 \pmod p,$$
>    $$x \equiv c_2 \pmod q.$$
>
> 2. Output $x$ as the recovered plaintext.

> [!remark]
> We can calculate $\gcd(g_1, n)$ might be $p$ and $\gcd(g_2, n)$ might be $q$.


