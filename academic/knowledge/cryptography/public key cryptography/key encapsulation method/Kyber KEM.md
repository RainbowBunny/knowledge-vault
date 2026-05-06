

## Kyber PKE

Kyber parameters (ML-KEM-768): $q = 3329, n = 256, \eta_1 = 2, \eta_2 = 2, k = 3$.

Kyber Parameters: $n, q, k, \eta_1, \eta_2$.
Key generation: 
Alice does
1. Select $A \in_R R^{k \times k}_q, s = S^R_{\eta_1}, e \in_R S^R_{\eta_1}$, compute $t = As + e \in S_\eta^k$
2. Public key is $(A, t)$, private key is $s$.

Encryption:
Bob encrypts $m \in \{0, 1\}^n$ for Alice.
1. Select $r \in S^{k}_{\eta_1}$, $e_1 \in S_{\eta_2}^k$, $e_2 \in_R S_{\eta_2}$.
2. Compute $u = A^T r + e$, $v = t^T r + e_2 + \lceil \frac{q}{2} \rceil m$

Decryption:
Compute $m = \text{Round}_q (v - s^T u)$

Notes

## Kyber KEM

Three hash functions
$G : \{0, 1\}^* \rightarrow \{0, 1\}^{512}$
$H : \{0, 1\}^* \rightarrow \{0, 1\}^{256}$
$J : \{0, 1\}^* \rightarrow \{0, 1\}^{256}$
1. Select Kyber-PKE keys $(A, t), s$
2. Select $z \in_R \{0, 1\}^{256}$
3. Public key $(A, t)$, private key $(s, z)$

Key encapsulation:
1. Selects $m \in_R \{0, 1\}^{256}$, $e_k = H(A, t)$
2. Compute $(k, R) \rightarrow G(m, e_k)$, $K \in \{0, 1\}^{256}, R \in \{0, 1\}^{256}$.
3. Use Kyber PKE to encrypt $m$ with encryption key $(A, t)$ and using $R$ to generate $e_1, e_2$ and $r$.
4. Send $c$ to Alice + set $K$ to be the shared secret key.

Key decapsulation: 
1. Use Kyber PKD to decrypt $c$ using $s$; call the plaintext $m'$.
2. Compute $(k', R') \rightarrow G(m', A, t)$
3. Use Kyber-PKE to encrypt $m'$ with encrypt key $(A, t)$, using $R'$ to generate $e_1, e_2, r$. Call the ciphertext $c'$.
4. Compute $\bar K = J(z, c)$.
5. If $c \neq c'$ then send $\bar K$. Else, `return(K)`.


