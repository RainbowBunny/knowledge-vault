## Default Version

> [!algorithm] Diffie–Hellman Key Exchange
>
> ### Public Parameter Creation
> A trusted party chooses and publishes:
> - A large prime $p$
> - A generator $g$ of large prime order in $\mathbb{F}_p^*$
>
> ---
>
> ### Private Computations
>
> | Alice | Bob |
> |------|-----|
> | Choose a secret integer $a$ | Choose a secret integer $b$ |
> | Compute $A \equiv g^a \pmod p$ | Compute $B \equiv g^b \pmod p$ |
>
> ---
>
> ### Public Exchange of Values
>
> | Alice → Bob | Bob → Alice |
> |-------------|-------------|
> | $A$ | $B$ |
>
> ---
>
> ### Further Private Computations
>
> | Alice | Bob |
> |------|-----|
> | Compute $B^a \pmod p$ | Compute $A^b \pmod p$ |
>
> The shared secret is:
> $$B^a \equiv (g^b)^a \equiv g^{ab} \equiv (g^a)^b \equiv A^b \pmod p.$$

## Diffie-Hellman Problem

> [!definition] Diffie-Hellman Problem
Let $p$ be a prime and $g$ an integer. The **Diffie-Hellman Problem (DHP)** is the problem of computing the value of $g^{ab}\pmod p$ from the known values of $g^a\pmod p$ and $g^b\pmod p$. 

> [!question]
> Suppose that Eve has an algorithm that efficiently solves the DHP, can she use it to also efficiently solve the DLP?

## Man-in-the-middle Attack

> [!example] Man-in-the-Middle Attack on Diffie–Hellman
> **Participants:** Alice, Bob, Eve (adversary)
>
> **Public parameters:** A prime $p$ and generator $g \in \mathbb{Z}_p^*$
>
> ---
>
> ### Phase 1: Key Exchange Interception
>
> 1. Alice chooses a secret exponent $a$ and computes:
>    $$A \equiv g^a \pmod p.$$
>
> 2. Bob chooses a secret exponent $b$ and computes:
>    $$B \equiv g^b \pmod p.$$
>
> 3. Eve chooses a secret exponent $e$ and computes:
>    $$E \equiv g^e \pmod p.$$
>
> 4. Eve intercepts Alice’s message and sends $E$ to Bob instead of $A$.
>
> 5. Eve intercepts Bob’s message and sends $E$ to Alice instead of $B$.
>
> ---
>
> ### Phase 2: Key Computation
>
> 1. Alice computes the shared value:
>    $$K_A \equiv E^a \equiv g^{ea} \pmod p.$$
>
> 2. Bob computes the shared value:
>    $$K_B \equiv E^b \equiv g^{eb} \pmod p.$$
>
> 3. Eve computes both shared keys:
>    $$K_{AE} \equiv A^e \equiv g^{ae} \pmod p,$$
>    $$K_{EB} \equiv B^e \equiv g^{be} \pmod p.$$
>
> ---
>
> ### Phase 3: Message Relay
>
> 1. Alice encrypts a message using key $K_A$ and sends it toward Bob.
>
> 2. Eve decrypts the message using $K_{AE}$, optionally modifies it,
>     re-encrypts it using $K_{EB}$, and forwards it to Bob.
>
> 3. Bob decrypts the message using $K_B$.
>
> ---
>
> **Result:**  
> Alice and Bob believe they share a secret key, but Eve successfully
> reads and alters all communications without being detected.

## Elliptic Version

> [!algorithm] Elliptic Curve Diffie–Hellman (ECDH) Key Exchange
> **Participants:** Alice and Bob
>
> ---
>
> ### Public Parameter Creation
>
> 1. A trusted party chooses and publishes:
>    - A large prime $p$,
>    - An elliptic curve $E$ defined over $\mathbb{F}_p$,
>    - A public point $P \in E(\mathbb{F}_p)$.
>
> ---
>
> ### Private Computations
>
> 2. Alice chooses a secret integer $n_A$ and computes:
>    $$Q_A \gets n_A P.$$
>
> 3. Bob chooses a secret integer $n_B$ and computes:
>    $$Q_B \gets n_B P.$$
>
> ---
>
> ### Public Exchange of Values
>
> 1. Alice sends $Q_A$ to Bob.
>
> 2. Bob sends $Q_B$ to Alice.
>
> ---
>
> ### Further Private Computations
>
> 1. Alice computes the shared secret:
>    $$K \gets n_A Q_B.$$
>
> 2. Bob computes the shared secret:
>    $$K \gets n_B Q_A.$$
>
> ---
>
> **Result:**  
> Both parties obtain the same shared secret:
> $$n_A Q_B = n_A (n_B P) = n_B (n_A P) = n_B Q_A.$$

> [!definition] Elliptic Curve Diffie-Hellman Problem
> Let $E(\mathbb F_p)$ be an elliptic curve over a finite field and let $P \in E(\mathbb F_p)$. The **Elliptic Curve Diffie-Hellman Problem** is the problem of computing the value of $n_1 n_2 P$ from the known values of $n_1 P$ and $n_2 P$.

## Tripartite Version

> [!algorithm] Tripartite Diffie–Hellman Using Pairings (Joux Protocol)
> **Participants:** Alice, Bob, and Carl
>
> **Public Parameters:**  
> - A finite field $\mathbb{F}_q$  
> - An elliptic curve $E / \mathbb{F}_q$  
> - A point $P \in E(\mathbb{F}_q)$ of prime order $\ell$  
> - An $\ell$-distortion map $\phi$ for $P$  
>
> **Output:**  
> A shared secret value
> $$K = \hat{e}_\ell(P, P)^{\,n_A n_B n_C}.$$
>
> ---
>
> ### Private Computations
>
> 1. Alice chooses a secret integer $n_A$ and computes:
>    $$Q_A \gets n_A P.$$
>
> 2. Bob chooses a secret integer $n_B$ and computes:
>    $$Q_B \gets n_B P.$$
>
> 3. Carl chooses a secret integer $n_C$ and computes:
>    $$Q_C \gets n_C P.$$
>
> ---
>
> ### Publication of Values
>
> 1. Alice, Bob, and Carl publish their public points
>    $$Q_A, \; Q_B, \; Q_C.$$
>
> ---
>
> ### Further Private Computations
>
> 1. Alice computes:
>    $$K \gets \hat{e}_\ell(Q_B, Q_C)^{\,n_A}.$$
>
> 2. Bob computes:
>    $$K \gets \hat{e}_\ell(Q_A, Q_C)^{\,n_B}.$$
>
> 3. Carl computes:
>    $$K \gets \hat{e}_\ell(Q_A, Q_B)^{\,n_C}.$$
>
> ---
>
> **Correctness:**  
> $$\hat{e}_\ell(Q_B, Q_C)^{n_A}
>  = \hat{e}_\ell(P, P)^{n_A n_B n_C}
>  = \hat{e}_\ell(Q_A, Q_C)^{n_B}
>  = \hat{e}_\ell(Q_A, Q_B)^{n_C}.$$

> [!remark] Security of Tripartite Diffie-Hellman key exchange
> - If Eve can solve the [[Discrete Logarithm Problem#Elliptic Curve Discrete Logarithm Problem|ECDLP]], she can recover $n_A$, $n_B$ or $n_C$ and get the shared secret $K$.
> - The distortion map $\phi$ is a mapping to $\mathbb F_q^*$ so Eve can just solve the [[Discrete Logarithm Problem#Discrete Logarithm Problem|DLP]] for a subgroup of $\mathbb F_q^*$ of order $\ell$.


