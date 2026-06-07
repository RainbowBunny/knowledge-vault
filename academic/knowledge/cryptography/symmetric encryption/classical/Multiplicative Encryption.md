# Multiplicative Encryption

> [!scheme] Multiplicative Encryption over $\mathbb{F}_p^{*}$
> **Setting:** large prime $p$.
>
> **Key generation.**
> Key, message, and ciphertext spaces: $$\mathcal K = \mathcal M = \mathcal C = \mathbb F_p^{*} = \{1, 2, \ldots, p - 1\}.$$
> Sample $k \in \mathcal K$.
>
> **Encryption.** Compute $c \gets k \cdot m \pmod p$.
>
> **Decryption.** Compute the modular inverse $k^{-1} \pmod p$, then $m \gets k^{-1} \cdot c \pmod p$.

## Security

Same shape as the [[One-time Pad#Multiplicative Variant|multiplicative one-time pad]]. Perfectly secure if used only once with a uniformly random key; insecure with key reuse.
