# One-time Pad

> [!scheme] One-time Pad
> A **one-time pad** is a Shannon cipher $\mathcal E = (E, D)$ where keys, messages, and ciphertexts are bit strings of the same length; that is, $\mathcal E$ is defined over $(\mathcal K, \mathcal M, \mathcal C)$ where $$\mathcal K = \mathcal M = \mathcal C = \{0, 1\}^L,$$ for some fixed parameter $L$.
>
> **Algorithms.**
> - Encryption: $E(k, m) = k \oplus m$.
> - Decryption: $D(k, c) = k \oplus c$.

> [!theorem]
> The one-time pad is a perfectly secure Shannon cipher.

## Variable-Length Variant

> [!scheme] Variable-Length One-time Pad
> A **variable-length one-time pad** is a Shannon cipher $\mathcal E = (E, D)$ where keys are bit strings of fixed length $L$ while messages and ciphertexts are variable length, at most $L$. Thus $\mathcal E$ is defined over $$\mathcal K = \{0, 1\}^L, \quad \mathcal M = \mathcal C = \{0, 1\}^{\leq L}.$$
>
> **Algorithms.**
> - Encryption: for $k \in \mathcal K$ and message $m \in \mathcal M$ of length $\ell$, $E(k, m) = k[0 \dots \ell - 1] \oplus m$.
> - Decryption: for $k \in \mathcal K$ and ciphertext $c \in \mathcal C$ of length $\ell$, $D(k, c) = k[0 \dots \ell - 1] \oplus c$.

## Additive Variant

> [!scheme] Additive One-time Pad
> $\mathcal K = \mathcal M = \mathcal C = \{0, \dots, p - 1\}$.
>
> Replace OTP encryption/decryption by $E(k, m) = m + k \bmod n$ and $D(k, c) = c - k \bmod n$.

## Multiplicative Variant

> [!scheme] Multiplicative One-time Pad
> $\mathcal K = \mathcal M = \mathcal C = \{1, \dots, p - 1\}$.
>
> Replace OTP encryption/decryption by $E(k, m) = k \cdot m \bmod p$ and $D(k, c) = k^{-1} \cdot c \bmod p$.

## Related

- The OTP is the canonical proof witness for [[Symmetric Key Encryption#Perfect Security|perfect security]] and the optimality of [[Symmetric Key Encryption#Perfect Security|Shannon's bound]] $|\mathcal K| \geq |\mathcal M|$.
- For practical encryption use [[Symmetric Key Encryption#Construction|modern CPA-secure constructions]] (counter mode, CBC), not OTP.
