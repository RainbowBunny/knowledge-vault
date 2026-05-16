
> [!definition] Symmetric Cipher
>  Assuming that Bob and Alice share knowledge of the secret key $k$. Using that secret key, they can both encrypt and decrypt messages, so Bob and Alice have equal (or symmetric) knowledge and abilities. For this reason, ciphers of this sort are know as **symmetric ciphers**.

**Notation**:
- Key space: $\mathcal K$.
- Plaintext space: $\mathcal M$.
- Ciphertext space: $\mathcal C$.
- Encryption function $e: \mathcal K \times \mathcal M \rightarrow \mathcal C$
- Decryption function $d: \mathcal K \times \mathcal C \rightarrow \mathcal M$
Sometimes it is convenient to write dependence on $k$ as a subscript:
- Encryption function $e_k: \mathcal M \rightarrow \mathcal C$
- Decryption function $d_k: \mathcal C \rightarrow \mathcal M$
The decryption property: $d(k, e(k, m)) = m$ for all $k \in \mathcal K$ and all $m \in \mathcal M$ or $d_k(e_k(m)) = m$ for all $m \in \mathcal M$.

>[!remark] 
>Criteria for the successful cipher: 
>If $(\mathcal K, \mathcal M, \mathcal C, e, d)$ is to be a successful cipher, it must have the following properties:
>1. For any key $k \in \mathcal K$ and plaintext $m \in \mathcal M$, it must be easy to compute the ciphertext $e_k(m)$.
>2. For any key $k \in \mathcal K$ and ciphertext $c \in \mathcal C$, it must be easy to compute the plaintext $d_k(c)$.
>3. Given one or more ciphertexts $c_1, c_2, \cdots, c_n \in \mathcal C$ encrypted using the key $k \in \mathcal K$, it must be very difficult to compute any of the corresponding plaintexts $d_k(c_1), \dots, d_k(c_k)$ without knowledge of $k$.
There is a fourth property that is desirable, although it is more difficult to achieve.
>2. Given one or more pairs of plaintexts and their corresponding ciphertexts, $(m_1, c_1), (m_2, c_2), \dots, (m_n, c_n)$, it must be difficult to decrypt any ciphertext $c$ that is not in the given list without knowing $k$. This is known as security against a **chosen plaintext attack**.

## Multiplicative Encryption

> [!algorithm] Multiplicative Encryption over $\mathbb{F}_p^{*}$
> **Input:**  
> - A large prime $p$  
> - A plaintext $m \in \mathbb{F}_p^{*}$
>
> **Output:**  
> A ciphertext $c \in \mathbb{F}_p^{*}$ and correct decryption of $m$
>
> ---
>
> ### Key Generation
>
> 1. Let the key space, message space, and ciphertext space be
>    $$\mathcal{K} = \mathcal{M} = \mathcal{C} = \mathbb{F}_p^{*}
>      = \{1,2,\ldots,p-1\}.$$
>
> 2. Choose a secret key:
>    $$k \in \mathcal{K}.$$
>
> ---
>
> ### Encryption
>
> **Input:** Plaintext $m \in \mathcal{M}$
>
> 1. Compute the ciphertext:
>    $$c \gets k \cdot m \pmod p.$$
>
> ---
>
> ### Decryption
>
> **Input:** Ciphertext $c \in \mathcal{C}$
>
> 1. Compute the modular inverse:
>    $$k^{-1} \equiv k' \pmod p.$$
>
> 2. Recover the plaintext:
>    $$m \gets k' \cdot c \pmod p.$$

## Affine Cipher

> [!algorithm] Affine Cipher
> **Input:**  
> - Modulus $p$ (typically $p=26$)  
> - Plaintext symbol $m \in \mathbb{Z}_p$
>
> **Output:**  
> Ciphertext symbol $c \in \mathbb{Z}_p$
>
> ---
>
> ### Key Generation
>
> 1. Choose integers $k_1,k_2 \in \mathbb{Z}_p$ such that
>    $$\gcd(k_1,p)=1.$$
>
> ---
>
> ### Encryption
>
> 1. Compute
>    $$c \gets k_1 m + k_2 \pmod p.$$
>
> ---
>
> ### Decryption
>
> 2. Compute the inverse $k_1^{-1} \pmod p$.
>
> 3. Recover the plaintext
>    $$m \gets k_1^{-1}(c-k_2) \pmod p.$$

## Hill Cipher

> [!algorithm] Hill Cipher
> **Input:**  
> - Modulus $p$ (typically $p=26$)  
> - Plaintext vector $m \in \mathbb{Z}_p^n$
>
> **Output:**  
> Ciphertext vector $c \in \mathbb{Z}_p^n$
>
> ---
>
> ### Key Generation
>
> 1. Choose an invertible matrix
>    $$K_1 \in \mathbb{Z}_p^{n \times n}$$
>    such that
>    $$\gcd(\det K_1, p)=1$$ and a vector $K_2 \in \mathbb{Z}_p^n$
>
> ---
>
> ### Encryption
>
> 1. Compute
>    $$c \gets K_1 m + K_2 \pmod p.$$
>
> ---
>
> ### Decryption
>
> 1. Compute the inverse matrix
>    $$K_1^{-1} \pmod p.$$
>
> 2. Recover the plaintext
>    $$m \gets K_1^{-1} (c - K_2) \pmod p.$$

