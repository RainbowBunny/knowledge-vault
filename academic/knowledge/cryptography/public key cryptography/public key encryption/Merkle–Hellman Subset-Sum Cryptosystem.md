## Encryption Scheme

> [!algorithm] Merkle–Hellman Subset-Sum Cryptosystem
> **Participants:** Alice (key owner), Bob (sender)
>
> **Output:**  
> Correct encryption and decryption of a binary plaintext vector
> $$x \in \{0,1\}^n.$$
>
> ---
>
> ### Key Creation (Alice)
>
> 1. Choose a superincreasing sequence:
>    $$r = (r_1, r_2, \ldots, r_n).$$
>
> 2. Choose integers $A$ and $B$ such that:
>    $$B > 2r_n \quad \text{and} \quad \gcd(A, B) = 1.$$
>
> 3. For $1 \le i \le n$, compute:
>    $$M_i \gets A r_i \pmod B.$$
>
> 4. Publish the public key:
>    $$M = (M_1, M_2, \ldots, M_n).$$
>
> ---
>
> ### Encryption (Bob)
>
> **Input:** Binary plaintext vector $x = (x_1, \ldots, x_n)$  
> **Public key:** $M$
>
> 1. Compute the ciphertext:
>    $$S \gets x \cdot M = \sum_{i=1}^n x_i M_i.$$
>
> 2. Send the ciphertext $S$ to Alice.
>
> ---
>
> ### Decryption (Alice)
>
> 1. Compute:
>    $$S' \gets A^{-1} S \pmod B.$$
>
> 2. Solve the subset-sum problem:
>    $$x \cdot r = S',$$
>    using the fast algorithm for superincreasing sequences.
>
> 3. Output the plaintext vector $x$.

