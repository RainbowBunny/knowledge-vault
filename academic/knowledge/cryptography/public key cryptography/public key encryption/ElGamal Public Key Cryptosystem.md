## Encryption Scheme

> [!algorithm] ElGamal Public-Key Encryption Scheme
> **Public Parameters:** A large prime $p$ and an element $g \in \mathbb{Z}_p^*$ of large (prime) order
>
> ---
>
> ### Public Parameter Creation
> A trusted party chooses and publishes:
> - A large prime $p$
> - An element $g$ modulo $p$ of large (prime) order
>
> ---
>
> ### Key Creation (Alice)
> 1. Choose a private key $a$ such that $1 \le a \le p - 1$.
> 2. Compute the public key:
>    $$A \equiv g^a \pmod p.$$
> 3. Publish the public key $A$.
>
> ---
>
> ### Encryption (Bob)
> **Input:** Plaintext message $m$  
> **Public key:** $A$
>
> 1. Choose a plaintext message $m$.
> 2. Choose a random ephemeral key $k$.
> 3. Compute:
>    $$\begin{aligned}
>    c_1 &\equiv g^k \pmod p, \\
>    c_2 &\equiv m A^k \pmod p.
>    \end{aligned}$$
> 4. Send the ciphertext $(c_1, c_2)$ to Alice.
>
> ---
>
> ### Decryption (Alice)
> **Input:** Ciphertext $(c_1, c_2)$
>
> 1. Compute:
>    $$m \equiv (c_1^a)^{-1} \cdot c_2 \pmod p.$$
> 2. Output the plaintext $m$.

> [!proposition]
>  Fix a prime $p$ and base $g$ to use for ElGamal encryption. Suppose that Eve has access to an oracle that decrypts arbitrary ElGamal ciphertexts encrypted using arbitrary ElGamal public keys. Then, she can use the oracle to solve the [[Diffie-Hellman Key Exchange|Diffie-Hellman Problem]].

> [!remark]
> In the ElGamal cryptosystem, the plaintext is an integer $m$ between $2$ and $p - 1$, while the ciphertext consists of two integers $c_1$ and $c_2$ in the same range. So ElGamal has a 2-to-1 message expansion.

## Man in the Middle Attack on ElGamal

> [!algorithm] Man-in-the-Middle Attack on ElGamal
> **Participants:** Alice (receiver), Bob (sender), Eve (attacker)
>
> **Public Parameters:**  
> A prime $p$ and generator $g \in \mathbb{F}_p^{*}$
>
> **Goal:**  
> Eve learns Bob’s plaintext $m$ while Alice and Bob believe communication is secure
>
> ---
>
> 1. Alice publishes her public key
>    $$h = g^{a} \pmod p.$$
>
> 2. Eve intercepts $h$ and replaces it with her own key
>    $$h_E = g^{e} \pmod p,$$
>    which she sends to Bob.
>
> 3. Bob encrypts $m$ using $h_E$ and sends the ciphertext
>    $$ (c_1, c_2) = (g^{k}, m \cdot h_E^{k}) $$
>    to Alice.
>
> 4. Eve intercepts $(c_1, c_2)$ and decrypts
>    $$m = c_2 / c_1^{e} \pmod p.$$
>
> 5. Eve re-encrypts $m$ using Alice’s real public key $h$
>    and forwards a fresh ElGamal ciphertext to Alice.
>
> 6. Alice decrypts successfully and remains unaware of Eve.

## Elliptic Version

> [!algorithm] Elliptic Curve ElGamal Encryption Scheme
> **Participants:** Alice (key owner), Bob (sender)
>
> ---
>
> ### Public Parameter Creation
>
> 1. A trusted party chooses and publishes:
>    - A large prime $p$,
>    - An elliptic curve $E$ defined over $\mathbb{F}_p$,
>    - A public base point $P \in E(\mathbb{F}_p)$.
>
> ---
>
> ### Key Creation (Alice)
>
> 1. Alice chooses a private key $n_A$.
>
> 2. Alice computes her public key:
>    $$Q_A \gets n_A P \in E(\mathbb{F}_p).$$
>
> 3. Alice publishes the public key $Q_A$.
>
> ---
>
> ### Encryption (Bob)
> **Input:** A plaintext point $M \in E(\mathbb{F}_p)$  
> **Public key:** $Q_A$
>
> 1. Bob chooses a random ephemeral key $k$.
>
> 2. Bob computes:
>    $$\begin{aligned}
>    C_1 &\gets kP \in E(\mathbb{F}_p), \\
>    C_2 &\gets M + kQ_A \in E(\mathbb{F}_p).
>    \end{aligned}$$
>
> 3. Bob sends the ciphertext $(C_1, C_2)$ to Alice.
>
> ---
>
> ### Decryption (Alice)
> **Input:** Ciphertext $(C_1, C_2)$
>
> 1. Alice computes:
>    $$M \gets C_2 - n_A C_1 \in E(\mathbb{F}_p).$$
>
> ---
>
> **Correctness:**  
> $$C_2 - n_A C_1 = M + kQ_A - n_A(kP) = M.$$

> [!remark] Practical difficulties
> 2. There is no obvious way to attach plaintext messages to points in $E(\mathbb F_p).$ 
> 3. The elliptic ElGamal cryptosystem has 4-to-1 message expansion.

## Digital Signature Scheme

> [!algorithm] ElGamal Digital Signature Algorithm
> **Participants:** Samantha (signer), Victor (verifier)
>
> **Public Parameters:**  
> - A large prime $p$  
> - A primitive root $g \bmod p$
>
> **Output:**  
> A valid ElGamal digital signature $(S_1, S_2)$ for a document $D$,
> and successful verification of the signature
>
> ---
>
> ### Key Creation (Samantha)
>
> 1. Choose a secret signing key:
>    $$1 \le s \le p-1.$$
>
> 2. Compute the verification key:
>    $$v \gets g^s \pmod p.$$
>
> 3. Publish the public key $v$.
>
> ---
>
> ### Signing (Samantha)
>
> **Input:** Document $D \in \mathbb{Z}_p$
>
> 1. Choose a random ephemeral key:
>    $$e \in \mathbb{Z}_{p-1} \quad \text{with } \gcd(e, p-1) = 1.$$
>
> 2. Compute:
>    $$S_1 \gets g^e \pmod p.$$
>
> 3. Compute:
>    $$S_2 \gets (D - s S_1)e^{-1} \pmod{(p-1)}.$$
>
> 4. Output the signature $(S_1, S_2)$.
>
> ---
>
> ### Verification (Victor)
>
> **Input:** Document $D$ and signature $(S_1, S_2)$
>
> 1. Compute:
>    $$v^{S_1} S_1^{S_2} \pmod p.$$
>
> 2. Accept the signature if and only if:
>    $$v^{S_1} S_1^{S_2} \equiv g^D \pmod p.$$

> [!remark]
> Eve's task is as follows. Given the values of $v$ and $g^D$, Eve must find integers $x$ and $y$ satisfying $$v^x x^y \equiv g^D \pmod p.$$

## Menezes-Vanstone variant

> [!algorithm] Menezes–Vanstone Variant of ElGamal (Elliptic Curve)
> **Input**
> - A large prime $p$
> - An elliptic curve $E / \mathbb{F}_p$
> - A base point $P \in E(\mathbb{F}_p)$
> - Plaintext values $m_1, m_2 \in \mathbb{F}_p$
>
> **Output**
> - Ciphertext $(R, c_1, c_2)$
>
> ---
>
> **Public Parameter Creation**
> 1. A trusted party chooses and publishes:
>    - A large prime $p$
>    - An elliptic curve $E$ over $\mathbb{F}_p$
>    - A point $P \in E(\mathbb{F}_p)$
>
> **Key Generation (Alice)**
> 1. Choose a secret multiplier $n_A$.
> 2. Compute the public key:
>    $$
>    Q_A = n_A P
>    $$
> 3. Publish $Q_A$.
>
> **Encryption (Bob)**
> 1. Choose plaintext values $m_1, m_2 \in \mathbb{F}_p$.
> 2. Choose a random integer $k$.
> 3. Compute:
>    $$
>    R = kP
>    $$
> 4. Compute:
>    $$
>    S = kQ_A = (x_S, y_S)
>    $$
> 5. Compute ciphertext components:
>    $$
>    c_1 = x_S m_1 \bmod p
>    $$
>    $$
>    c_2 = y_S m_2 \bmod p
>    $$
> 6. Send $(R, c_1, c_2)$ to Alice.
>
> **Decryption (Alice)**
> 1. Compute:
>    $$
>    T = n_A R = (x_T, y_T)
>    $$
> 2. Recover plaintext:
>    $$
>    m_1 = x_T^{-1} c_1 \bmod p
>    $$
>    $$
>    m_2 = y_T^{-1} c_2 \bmod p
>    $$
> 3. Output $(m_1, m_2)$.
