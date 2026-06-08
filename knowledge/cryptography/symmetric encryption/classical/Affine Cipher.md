# Affine Cipher

> [!scheme] Affine Cipher
> **Setting:** modulus $p$ (typically $p = 26$).
>
> **Key generation.** Choose $k_1, k_2 \in \mathbb Z_p$ such that $\gcd(k_1, p) = 1$.
>
> **Encryption.** $c \gets k_1 m + k_2 \pmod p$.
>
> **Decryption.** Compute $k_1^{-1} \pmod p$, then $m \gets k_1^{-1}(c - k_2) \pmod p$.

## Security

Broken by frequency analysis like the Caesar / substitution cipher: each plaintext symbol still maps to a fixed ciphertext symbol. Combined with a small message space ($p = 26$), only $\varphi(p) \cdot p = 26 \cdot 12 = 312$ keys for English alphabet — brute-forceable.
