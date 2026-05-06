## Encryption Scheme

> [!algorithm] RSA Public-Key Encryption Scheme
> **Participants:** Bob (key owner), Alice (sender)
>
> ---
>
> ### Key Creation (Bob)
> 1. Choose two secret primes $p$ and $q$.
> 2. Choose an encryption exponent $e$ such that
>    $$\gcd(e, (p-1)(q-1)) = 1.$$
> 3. Compute:
>    $$N \gets pq.$$
> 4. Publish the public key $(N, e)$.
>
> ---
>
> ### Encryption (Alice)
> **Input:** Plaintext message $m$  
> **Public key:** $(N, e)$
>
> 1. Choose a plaintext message $m$.
> 2. Compute the ciphertext:
>    $$c \equiv m^e \pmod N.$$
> 3. Send the ciphertext $c$ to Bob.
>
> ---
>
> ### Decryption (Bob)
> **Input:** Ciphertext $c$
>
> 1. Compute the decryption exponent $d$ satisfying:
>    $$ed \equiv 1 \pmod{(p-1)(q-1)}.$$
> 2. Recover the plaintext:
>    $$m' \equiv c^d \pmod N.$$
> 3. Output $m'$, which equals the original plaintext $m$.

### Multiple Exponent Attack

> [!example] RSA Common Modulus Attack
> Suppose that Alice publishes two different encryption exponents
> $e_1$ and $e_2$ for use with her public modulus $N$, and that Bob
> encrypts a single plaintext $m$ using both of Alice’s exponents.
> If Eve intercepts the ciphertexts
> $$c_1 \equiv m^{e_1} \pmod N
> \quad \text{and} \quad
> c_2 \equiv m^{e_2} \pmod N,$$
> she can proceed as follows.
>
> Eve computes integers $u$ and $v$ satisfying
> $$e_1 u + e_2 v = \gcd(e_1, e_2).$$
>
> She then computes:
> $$\begin{aligned}
> c_1^{\,u} \cdot c_2^{\,v}
> &\equiv (m^{e_1})^{u} \cdot (m^{e_2})^{v} \\
> &\equiv m^{e_1 u + e_2 v}
> \equiv m^{\gcd(e_1, e_2)} \pmod N.
> \end{aligned}$$
>
> If $\gcd(e_1, e_2) = 1$, then Eve recovers the plaintext $m$.
>
> More generally, if Bob encrypts the same message using exponents
> $e_1, e_2, \ldots, e_r$ and
> $$\gcd(e_1, e_2, \ldots, e_r) = 1,$$
> then Eve can recover the plaintext.
>
> **Moral:** Alice should use at most one encryption exponent for a
> given modulus $N$.

### Man in the Middle Attack on RSA

> [!algorithm] Man-in-the-Middle Attack on RSA
> **Participants:** Alice (receiver), Bob (sender), Eve (attacker)
>
> **Goal:**  
> Eve learns Bob’s plaintext $m$
>
> ---
>
> 1. Alice publishes her RSA public key $(N, e)$.
>
> 2. Eve intercepts the public key and replaces it with her own
>    $$(N_E, e_E),$$
>    which she sends to Bob.
>
> 3. Bob encrypts his message:
>    $$c = m^{e_E} \pmod{N_E}$$
>    and sends $c$ to Alice.
>
> 4. Eve intercepts $c$ and decrypts it using her private key,
>    recovering $m$.
>
> 5. Eve encrypts $m$ using Alice’s real public key $(N,e)$
>    and forwards the new ciphertext to Alice.
>
> 6. Alice decrypts successfully and remains unaware of Eve.

### RSA Oracle

> [!example] RSA Oracle Attack
> Suppose that Eve is able to convince Alice to decrypt “random” RSA messages
> using her private key. This is a plausible scenario, since one way for Alice
> to authenticate her identity as the owner of the public key $(N, e)$ is to show
> that she knows how to decrypt messages. In this situation, Eve has access to an
> **RSA oracle**.
>
> Eve exploits Alice’s generosity as follows. Suppose that Eve intercepts a
> ciphertext $c$ that Bob has sent to Alice. Eve chooses a random value $k$ and
> sends Alice the message
> $$c' \equiv k^e \cdot c \pmod N.$$
>
> Alice decrypts $c'$ and returns the resulting plaintext $m'$ to Eve, where
> $$\begin{aligned}
> m' &\equiv (c')^d
>     \equiv (k^e \cdot c)^d
>     \equiv (k^e \cdot m^e)^d \\
>    &\equiv k \cdot m \pmod N.
> \end{aligned}$$
>
> Since Eve knows $k$, she immediately recovers Bob’s plaintext $m$.
>
> ---
>
> **Observations**
>
> 1. Eve decrypts Bob’s message without knowing how to factor $N$; thus, the
>    hardness of the underlying mathematical problem is irrelevant.
> 2. Because Eve masks Bob’s ciphertext using $k$, Alice has no way to detect
>    that Eve’s message is related to Bob’s original message.
>    To Alice, both $k^e \cdot c \pmod N$ and $k \cdot m \pmod N$ appear random.


## Digital Signatures Scheme

> [!algorithm] RSA Digital Signature Scheme
> **Participants:** Samantha (signer), Victor (verifier)
>
> **Output:**  
> A valid RSA digital signature $S$ for a document $D$, and successful
> verification of the signature
>
> ---
>
> ### Key Creation (Samantha)
>
> 1. Choose two large secret primes $p$ and $q$.
>
> 2. Choose a verification exponent $v$ such that:
>    $$\gcd\!\bigl(v,(p-1)(q-1)\bigr) = 1.$$
>
> 3. Compute and publish:
>    $$N \gets pq,$$
>    along with the public verification exponent $v$.
>
> ---
>
> ### Signing (Samantha)
>
> **Input:** Document $D$
>
> 1. Compute the signing exponent $s$ satisfying:
>    $$s v \equiv 1 \pmod{(p-1)(q-1)}.$$
>
> 2. Compute the signature:
>    $$S \gets D^{\,s} \pmod N.$$
>
> ---
>
> ### Verification (Victor)
>
> **Input:** Document $D$ and signature $S$
>
> 1. Compute:
>    $$S^{\,v} \pmod N.$$
>
> 2. Accept the signature if and only if:
>    $$S^{\,v} \equiv D \pmod N.$$

## Matrix Extension of RSA

> [!theorem]
> Let $n = pq$ where $p$ and $q$ are distinct prime numbers, let $M \in \text{GL}_2(\mathbb Z_n)$ be a matrix made up of nonnegative integers less than $n$, let $g_p = |\text{GL}_2(\mathbb Z_p)| = (p^2 - 1)(p^2 - p)$ and $g_q = |\text{GL}_2(\mathbb Z_q)| = (q^2 - 1)(q^2 - q)$ and define $g = g_p g_q$. Further let $e, d \in \mathbb Z^+$ such that $ed \equiv \pmod g$, and let $C = M^e \pmod n$. Then $C^d \equiv M \pmod n$.

## 1-2 Oblivious Transfer

> [!algorithm] 1-2 Oblivious Transfer
> 

## Security of RSA

> [!remark]
> The security of RSA depends on the following dichotomy:
>- **Setup**: Let $p$ and $q$ be large primes, let $N = pq$, and let $e$ and $c$ be integers.
>- **Problem**: Solve the congruence $x^e \equiv c \pmod N$ for the variable $x$.
>- **Easy**: Bob, who knows the values of $p$ and $q$, can easily solve for $x$.
>- **Hard**: Eve, who does not know the values of $p$ and $q$, can not easily find $x$.
>- **Dichotomy**: Solving $x^e \equiv c \pmod N$ is easy for a person who possesses certain extra information, but it is apparently hard for all other people.


## Tools

- [https://github.com/bbuhrow/yafu](https://github.com/bbuhrow/yafu)


