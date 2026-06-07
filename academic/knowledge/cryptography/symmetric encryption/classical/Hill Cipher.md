# Hill Cipher

> [!scheme] Hill Cipher
> **Setting:** modulus $p$ (typically $p = 26$), block length $n$.
>
> **Key generation.** Choose an invertible matrix $K_1 \in \mathbb Z_p^{n \times n}$ with $\gcd(\det K_1, p) = 1$, and a shift vector $K_2 \in \mathbb Z_p^n$.
>
> **Encryption.** For a plaintext vector $m \in \mathbb Z_p^n$: $c \gets K_1 m + K_2 \pmod p$.
>
> **Decryption.** Compute $K_1^{-1} \pmod p$, then $m \gets K_1^{-1}(c - K_2) \pmod p$.

## Security

A block generalization of the [[Affine Cipher]]. Broken by known-plaintext attacks: with enough plaintext-ciphertext pairs you can solve a linear system for $K_1$ and $K_2$.
