## Encryption Scheme

> [!algorithm] Goldwasser–Micali Public-Key Encryption Scheme
> **Participants:** Bob (key owner), Alice (sender)
>
> ---
>
> ### Key Creation (Bob)
> 1. Choose two secret primes $p$ and $q$.
> 2. Choose an integer $a$ such that:
>    $$\left(\frac{a}{p}\right) = \left(\frac{a}{q}\right) = -1,$$
>    where $(\tfrac{\cdot}{\cdot})$ denotes the Legendre symbol.
> 3. Compute:
>    $$N \gets pq.$$
> 4. Publish the public key $(N, a)$.
>
> ---
>
> ### Encryption (Alice)
> **Input:** Plaintext bit $m \in \{0,1\}$  
> **Public key:** $(N, a)$
>
> 1. Choose a random integer $r$ such that $1 < r < N$.
> 2. Compute the ciphertext:
>    $$c \equiv
>    \begin{cases}
>      r^2 \pmod N, & \text{if } m = 0, \\
>      a r^2 \pmod N, & \text{if } m = 1.
>    \end{cases}$$
> 3. Send the ciphertext $c$ to Bob.
>
> ---
>
> ### Decryption (Bob)
> **Input:** Ciphertext $c$
>
> 1. Compute the Jacobi symbol:
>    $$\left(\frac{c}{p}\right).$$
> 2. Output:
>    $$m =
>    \begin{cases}
>      0, & \text{if } \left(\frac{c}{p}\right) = 1, \\
>      1, & \text{if } \left(\frac{c}{p}\right) = -1.
>    \end{cases}$$

