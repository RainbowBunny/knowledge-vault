## Syntax

> [!definition] Key Encapsulation Mechanism Scheme
> A **key encapsulation scheme** $\text{KEM} = (\text{KeyGen}, \text{Encaps}, \text{Decaps})$ is a triple of efficient algorithms with a ciphertext space $\mathcal C$, a key space $\mathcal K$ and a random space $\mathcal R$.
> - $(pk, sk) \leftarrow \text{KeyGen}()$: The key-generation algorithm $\text{KeyGen}$ returns a pair $(pk, sk)$ consisting of a public key $pk$ and a secret key $sk$.
> - $(c, K) \leftarrow \text{Encaps}(pk; r)$: The encapsulation algorithm $\text{Encaps}$ takes a public key $pk$ and a random $r \in \mathcal R$ to produce a ciphertext $c \in \mathcal C$ and a key $K \in \mathcal K$.
> - $K \leftarrow \text{Decaps}(sk, c)$: The deterministic decapsulation algorithm $\text{Decaps}$ takes a secret key $sk$ and a ciphertext $c$, and outputs either a key $K \in \mathcal K$ or a special symbol $\perp$ to indicate **rejection**.

## Property

### Correctness

> [!definition] KEM $(1 - \delta)$-Correctness
> A key encapsulation scheme $\text{KEM}$ is $(1 - \delta)$-correct if $$\Pr[\text{Decaps}(sk, c) = K \; | \; (c, K) \leftarrow \text{Encaps}(pk)] \geq 1 - \delta$$ where the probability is taken over $(pk, sk) \leftarrow \text{KeyGen}$ and the random coins of $\text{Encaps}$.

## Security

### Indistinguishability under Chosen-Ciphertext Attacks

> [!security] IND-CCA
> For any adversary $A$, the following advantage is negligible: 
> $$\text{Adv}_\text{KEM}^{\text{cca}}(A) = 
> \left|\; \Pr\!\left[ b = b' \;:\; 
> \begin{array}{l}
> (pk, sk) \leftarrow \text{KeyGen}(); \\
> b \leftarrow \{0, 1\}; \\
> (c^*, K_0^*) \leftarrow \text{EncCaps}(pk); \\
> K_1^* \in \mathcal K; \\
> b' \leftarrow A(pk, c^*, K_b^*)
> \end{array} \right] 
> \;- \frac{1}{2}
> \right|.$$
> Where:
> 1. The adversary has access to the decapsulation oracle $\text{Decaps}(\cdot) = \text{Decaps}(sk, \cdot)$.
> 2. The adversary $A$ is not allowed to query $\text{Decaps}(\cdot)$ with the challenge ciphertext $c^*$.

