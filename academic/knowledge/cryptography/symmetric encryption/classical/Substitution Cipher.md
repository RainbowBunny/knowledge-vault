# Substitution Cipher

> [!scheme] Substitution Cipher
> A **substitution cipher** is a Shannon cipher $\mathcal E = (E, D)$. Let $\Sigma$ be a finite alphabet of symbols. The message space $\mathcal M$ and the ciphertext space $\mathcal C$ are both sequences of symbols from $\Sigma$ of fixed length $L$: $$\mathcal M = \mathcal C = \Sigma^L.$$
> The key space $\mathcal K$ consists of all permutations on $\Sigma$ — each $k \in \mathcal K$ is a one-to-one function from $\Sigma$ onto itself.
>
> **Algorithms.**
> - Encryption: for $m \in \Sigma^L$ and $k \in \mathcal K$, $E(k, m) = (k(m[0]), \dots, k(m[L - 1])).$
> - Decryption: for $c \in \Sigma^L$ and $k \in \mathcal K$, $D(k, c) = (k^{-1}(c[0]), \dots, k^{-1}(c[L - 1])).$

## Security

Trivially broken by frequency analysis on natural-language plaintexts (each symbol's image is fixed, so letter frequencies in the ciphertext mirror those of the plaintext).

The Caesar cipher is the special case $k(\sigma) = \sigma + s \bmod |\Sigma|$ for a single shift $s$ — only $|\Sigma|$ possible keys.
