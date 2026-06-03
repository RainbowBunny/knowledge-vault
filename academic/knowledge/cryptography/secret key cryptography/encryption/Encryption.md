
> [!question]
> Suppose Alice and Bob share a secret key $k$. Alice wants to transmit a message $m$ to Bob over a network while maintaining the secrecy of $m$ in the presence of an eavesdropping adversary.



## Shannon Cipher

> [!algorithm] Shannon Cipher
> A **Shannon cipher** is a pair $\mathcal E = (E, D)$ of functions.
> - The function $E$ (the **encryption function**) takes as input a **key** $k$ and a **message** $m$ (also called a **plaintext**), and produces as output a **ciphertext** $c$. That is, $$c = E(k, m),$$ and we say that $c$ is the **encryption of $m$ under $k$**.
> - The function $D$ (the **decryption function**) takes as input a key $m$ and a ciphertext $c$, and produces a message $m$. That is, $$m = D(k, c),$$ and we say that $m$ is the **decryption of $c$ under $k$**.
> - We require that decryption "undoes" encryption: that is, the cipher must satisfy the following **correctness property**: for all keys $k$ and all messages $m$, we have $$D(k, E(k, m)) = m.$$
> 
> To be slightly more formal, let assume $\mathcal K$ is the set of all keys (the **key space**), $\mathcal M$ is the set of all messages (the **message space**), and that $\mathcal C$ is the set of all ciphertexts (the **ciphertext space**). With this notation, we can write $$\begin{align}E: \mathcal K \times \mathcal M \rightarrow \mathcal C, \\ D: \mathcal K \times \mathcal C \rightarrow \mathcal M.\end{align}$$
> 
> Also, we shall say that $\mathcal E$ is **defined over** $(\mathcal K, \mathcal M, \mathcal C)$.

### Perfect Security

> [!definition] Perfect Security
> Let $\mathcal E = (E, D)$ be a Shannon cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. Consider a probabilistic experiment in which the random variable $K$ is uniformly distributed over $\mathcal K$. If for all $m_0, m_1 \in \mathcal K$. If for all $m_0, m_1 \in \mathcal M$, and all $c \in \mathcal C$, we have $$P[E(K, m_0) = c] = P[E(K, m_1) = c],$$ then we say that $\mathcal E$ is a **perfect secure** Shannon cipher.

> [!theorem]
> Let $\mathcal E = (E, D)$ be a Shannon cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. The following are equivalent:
> 1. $\mathcal E$ is perfectly secure.
> 2. For every $c \in \mathcal C$, there exists an integer $N_c$ (possibly depending on $c$) such that for all $m \in \mathcal M$, we have $$|\{k \in \mathcal K : E(k, m) = c\}| = N_c.$$
> 3. If the random variable $K$ is uniformly distributed over $\mathcal K$, then each of the random variables $E(K, m)$, for $m \in \mathcal M$, has the same distribution.

> [!theorem]
> Let $\mathcal E = (E, D)$ be a Shannon cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. Consider a probabilistic experiment in which $K$ is a random variable uniformly distributed over $\mathcal K$. Then $\mathcal E$ is perfectly secure if and only if for every predicate $\phi$ on $\mathcal C$, for all $m_0, m_1 \in \mathcal M$, we have $$P[\phi(E(k, m_0))] = P[\phi(E(k, m_1))].$$

> [!theorem]
> Let $\mathcal E = (E, D)$ be a Shannon cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. Consider a random experiment in which $K$ and $M$ are random variables, such that 
> - $K$ is uniformly distributed over $\mathcal K$,
> - $M$ is distributed over $\mathcal M$, and
> - $K$ and $M$ are independent.
> 
> Define the random variable $C = E(K, M)$. Then we have:
> - If $\mathcal E$ is perfectly secure, then $C$ and $M$ are independent;
> - Conversely, if $C$ and $M$ are independent, and each message in $\mathcal M$ occurs with nonzero probability, then $\mathcal E$ is perfectly secure.

> [!theorem] Shannon's theorem
> Let $\mathcal E = (E, D)$ be a Shannon cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. If $\mathcal E$ is perfect secure, then $|\mathcal K| \geq |\mathcal M|$.

> [!theorem] Generalize Shannon's Theorem
> Let $\mathcal E$ be a cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$. Suppose that [[Notions of Security#Semantic Security|semantic security]] advantage $\text{SSadv}[\mathcal A, \mathcal E] \leq \epsilon$ for all adversaries $\mathcal A$, even including **computationally unbounded** ones. Then, $|\mathcal K| \geq (1 - \epsilon) |\mathcal M|$.

### Encryption Chain

> [!algorithm] Encryption Chain
> ### Building Block
> Let $\mathcal E = (E, D)$ be a cipher defined over $(\mathcal K, \mathcal M, \mathcal C)$ where $\mathcal K = \mathcal M$.
> 
> ---
> ### Algorithm
> We construction a cipher $\mathcal E' = (E', D')$.
> - Encryption: $E'((k_1, k_2), m) = (E(k_1, k_2), E(k_2, m)) \in \mathcal C^2$.

> [!theorem]
> $\mathcal E$ is perfectly secure then so is $\mathcal E'$.

> [!remark]
> The important of this construction is that adding $E(k_1, k_2)$ does not reduce the security of the scheme, as we know $E(k_2, m)$ is already secure.

## One-time Pad

> [!algorithm] One-time Pad
> ### Message Space
> A **one-time pad** is a Shannon cipher $\mathcal E = (E, D)$, where the keys, messages, and ciphertexts are bit strings of the same length; that is, $\mathcal E$ is defined over $(\mathcal K, \mathcal M, \mathcal C)$, where $$\mathcal K = \mathcal M = \mathcal C = \{0, 1\}^L,$$ for some fixed parameter $L$. 
> 
> ---
> ### Algorithms
> - Encryption: For a key $k \in \{0, 1\}^L$ and a message $m \in \{0, 1\}^L$ the encryption function is defined as follows: $$E(k, m) = k \oplus m$$ 
> - Decryption: For a key $k \in \{0, 1\}^L$ and a ciphertext $c \in \{0, 1\}^L$, the decryption function is defined as follows: $$D(k, c) = k \oplus c$$

> [!theorem]
> The one-time pad is a perfect secure Shannon cipher.

### Variable Length Variant

> [!algorithm] Variable Length One-time Pad
> ### Message Space
> A **variable length one-time pad** is a Shannon cipher $\mathcal E = (E, D)$, where the keys are bit strings of some fixed length $L$, while messages and ciphertexts are variable length bit strings, of length at most $L$. Thus, $\mathcal E$ is defined over $(\mathcal K, \mathcal M, \mathcal C)$, where $$\mathcal K = \{0, 1\}^L \quad \text{and} \quad \mathcal M = \mathcal C = \{0, 1\}^{\leq L}.$$ for some parameter $L$.
> 
> ---
> ### Algorithms
> - Encryption: For a key $k \in \mathcal K$ and a message $m \in \mathcal M$ of length $\ell$, the encryption function is defined as follows: $$E(k, m) = k[0 \dots \ell - 1] \oplus m,$$  
> - Decryption: For a key $k \in \mathcal K$ and a ciphertext $c \in \mathcal C$ of length $\ell$, the decryption function is defined as follows: $$D(k, c) = k[0 \dots \ell - 1] \oplus c.$$

### Additive Variant

> [!algorithm] Additive One-time Pad
> ### Message Space
> $\mathcal K = \mathcal M = \mathcal C = \{0, \dots, p - 1\}$.
> 
> ---
> ### Algorithms
> Replace the encryption and decryption of one-time pad by $E(k, m) = m + k \mod n$ and $D(k, c) = c - k \mod n$.

### Multiplicative One-time Pad

> [!algorithm] Multiplicative One-time Pad
> ### Message Space
> $\mathcal K = \mathcal M = \mathcal C = \{1, \dots, p - 1\}$.
> 
> ---
> ### Algorithms
> Replace the encryption and decryption of one-time pad by $E(k, m) = k \cdot m \mod p$ and $D(k, c) = k^{-1} \cdot c \mod p$.

## Substitution Cipher

> [!algorithm] Substitution Cipher
> ### Message Space
> A **substitution cipher** is a Shannon cipher $\mathcal E = (E, D)$. Let $\Sigma$ be a finite alphabet of symbols. The message space $\mathcal M$ and the ciphertext space $\mathcal C$ are both sequences of symbols from $\Sigma$ of some fixed length $L$: $$\mathcal M = \mathcal C = \Sigma^L.$$ The key space $\mathcal K$ consists of all permutations on $\Sigma$; that is, each $k \mathcal K$ is a one-to-one function from $\Sigma$ onto itself.
> 
> ---
> ### Algorithms
> - Encryption: Encryption of a message $m \in \Sigma^L$ under a key $k \in \mathcal K$ is defined as: $$E(k, m) = (k(m[0]), \dots, k(m[L - 1])).$$ 
> - Decryption: Decryption of a ciphertext $c \in \Sigma^L$ under a key $k \in \mathcal K$ is defined as: $$D(k, c) = (k^{-1}(c[0]), \dots, k(c[L - 1])).$$


