
> [!proposition] Cryptographically Secure
> In order to be useful for cryptography, a PRNG should have the following two properties:
> 1. If Eve knows the first $k$ bits of Alice's random bit string, she should have no better than a $50\%$ chance of predicting whenever the next bit will be a $0$ or a $1$. More precisely, there should not be a fast (e.g., polynomial time) algorithm that can predict the next bit with better than $50\%$ chance of success.
> 2. Suppose that Eve somehow learns part of Alice's random bit string, for example, suppose that she finds out the values of $R_t, R_{t + 1}, R_{t + 2}, \dots$. This should not help Eve to determine the earlier part $R_0, R_1, \dots, R_{t - 1}$ of Alice's string.
> A PRNG with these properties is said to be **cryptographically secure**.

## Dual Elliptic Curve Deterministic Random Bit Generator (DUAL_EC_DRBG)

> [!algorithm] DUAL_EC_DRBG
> **Parameters**
> - Elliptic curve $E$ over $\mathbb F_q$
> - Public points $P, Q \in E(\mathbb F_q)$
> - Truncation parameter $t$
> 
> **State**
> - Internal scalar $s_i \in \mathbb Z_n$
> 
> **Input**
> - Current state $s_i$
> 
> **Output**
> - Pseudorandom output block $r_i$
> - Updated state $s_{i + 1}$
> ---
> Algorithm
> 1. Compute next state point $$S = s_i \cdot P$$
> 2. Update internal state $$s_{i + 1} = x(S)$$
> 3. Compute output point $$R = s_{i + 1} \cdot Q$$
> 4. Extract output bits $$r_i = \text{truncate}_t(x(R))$$
> 5. Return $(r_i, s_{})$

> [!remark] Attack With Backdoor
> The idea of this attack is assume that we can find $Q = d \cdot P$, then if at some point, we can find a specific $x(s_{i + 1} \cdot Q)$, we can recover the next state $s_{i + 1} \cdot P$ and thus continue simulating the PRNG.
> Now, the security of this algorithm is the $\text{truncate}_t$ part, if we can fill the remaining bytes of $r_i$ to get $x(R)$, then we can recover PRNG.
