
Parameters $n, q, B$.
Key generation:
- Alice: 
	1. Selects $A \in_R \mathbb Z^{n \times n}_q$, $S \in_R [-B, B]^n$, $e \in_R [-B, B]^n$.
	2. Public key is $(A, b)$, Private key: $s$ (and $e$ but it is not important).
Note: Finding $s$ from $(A, b)$ is [[Learning With Error Problem#Short-Secret Learning With Error Problem|ss-LWE]].
Encryption:
- Bob encrypts $m \in \{0, 1\}$ for Alice:
	1. Select $r \in_R [-B, B]^n, z \in_R [-B, B]^n, z' \in_R [-B, B]$
	2. Compute $c_1 = A^T r + z \in \mathbb Z_q^n$ and $c_2 = b^T r + z' + \lceil \frac{q}{2} \rceil m \in \mathbb Z_q$.
	3. Send $c = (c_1, c_2)$ to Alice.
Decryption
- To decrypt $c = (c_1, c_2)$ Alice uses $s$: $m = \text{Round}_q (c_2 - s^T c_1)$.

> [!question]
> Lindner-Peikert does not secure from chosen ciphertext attack.

> [!remark]
> 1. Encryption is 1 bit at a time. Solution: Use MLWE instead of LWE.
> 2. Public key $(A, b)$ is large. Solution: Generate $A$ from seed $\in_R \{0, 1\}^256$.
> 3. Only weakly secure. Solution: Fujisaki Transform
> 4. Matrix - vector mult is slow. Solution: Use NTT.