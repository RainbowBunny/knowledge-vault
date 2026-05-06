## Signature Scheme

> [!algorithm] Digital Signature Algorithm (DSA)
> **Participants:** Samantha (signer), Victor (verifier)
>
> **Public Parameters:**  
> - Large primes $p$ and $q$ such that $p \equiv 1 \pmod q$  
> - An element $g \in \mathbb{Z}_p^{*}$ of order $q$
>
> **Output:**  
> A valid DSA signature $(S_1, S_2)$ for a document $D$, and successful
> verification of the signature
>
> ---
>
> ### Key Creation (Samantha)
>
> 1. Choose a secret signing key:
>    $$1 \le s \le q-1.$$
>
> 2. Compute the verification key:
>    $$v \gets g^{\,s} \pmod p.$$
>
> 3. Publish the public key $v$.
>
> ---
>
> ### Signing (Samantha)
>
> **Input:** Document $D \in \mathbb{Z}_q$
>
> 1. Choose a random ephemeral key:
>    $$e \in \mathbb{Z}_q^{*}.$$
>
> 2. Compute:
>    $$S_1 \gets (g^{\,e} \bmod p) \bmod q.$$
>
> 3. Compute:
>    $$S_2 \gets (D + s S_1)e^{-1} \pmod q.$$
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
>    $$V_1 \gets D S_2^{-1} \pmod q, \qquad
>      V_2 \gets S_1 S_2^{-1} \pmod q.$$
>
> 2. Compute:
>    $$V \gets (g^{V_1} v^{V_2} \bmod p) \bmod q.$$
>
> 3. Accept the signature if and only if:
>     $$V = S_1.$$

