
Link: https://eprint.iacr.org/2017/634.pdf
## Scheme

> [!scheme] Kyber KEM
> Reference Name: $\text{Kyber.KEM}$
> ### Parameters
> 
> ---
> ### Building Block
> - $G: \{0, 1\}^* \rightarrow \{0, 1\}^{2 \times 256}$: Secure hash function.
> - $H: \{0, 1\}^* \rightarrow \{0, 1\}^{256}$: Secure hash function.
> - $\text{Kyber.PKE} = (\text{KeyGen}, \text{Enc}, \text{Dec})$: A [[Kyber PKE#Scheme|Kyber PKE]] scheme.
> 
> ---
> ### Algorithms
> - $(pk, sk) \leftarrow \text{KeyGen}()$:
> 	1. $((t, \rho), s) \leftarrow \text{Kyber.PKE.KeyGen}()$
> 	2. $z \xleftarrow{R} \{0, 1\}^{256}$
> 	3. Return $(pk = (t, rho), sk = (s, z, t, \rho))$
> - $(c, K) \leftarrow \text{Encaps}(pk = (t, \rho))$:
> 	1. $m \leftarrow \{0, 1\}^{256}$
> 	2. $(\hat K, r) \leftarrow G(H(pk), m)$
> 	3. $(u, v) \leftarrow \text{Kyber.PKE.Enc}((t, \rho), m; r)$
> 	4. $c \leftarrow (u, v)$
> 	5. $K \leftarrow H(\hat K, H(c))$
> 	6. Return $(c, K)$
> - $K \leftarrow \text{Decaps}(sk = (s, z, t, \rho), c = (u, v))$
> 	1. $m' = \text{Kyber.PKE.Dec}(s, (u, v))$
> 	2. $(\hat K', r') \leftarrow G(H(pk), m')$
> 	3. $(u', v') \leftarrow \text{Kyber.PKE.Enc}((t, \rho), m'; r')$
> 	4. Branch
> 		1. If $(u', v') = (u, v)$ then $K \leftarrow H(\hat K', H(c))$
> 		2. Else $K \leftarrow H(z, H(c))$

## Property

### Correctness

> [!property] Correctness
> If $\text{Kyber.PKE}$ is $(1 - \delta)$-correct and $G$ is a random oracle, then $\text{Kyber.KEM}$ is $(1 - \delta)$-correct.

## Security

### Indistinguishability under Chosen-Ciphertext Attacks

> [!security]
> For any classical adversary $\mathcal A$ that makes at most $q_{RO}$ many queries to random oracles $H$ and $G$, and $q_D$ queries to the decryption oracle, there exists an adversary $\mathcal B$ such that $$\text{Adv}_\text{Kyber.KEM}^\text{cca}(\mathcal A) \leq 3 \text{Adv}_\text{Kyber.PKE}^\text{cpa}(\mathcal B) + q_{RO} \cdot \delta + \frac{3 q_{RO}}{2^{256}}$$

> [!security]
> For any quantum adversary $\mathcal A$ that makes at most $q_{RO}$ many queries to quantum random oracles $H$ and $G$, and at most $q_D$ many (classical) queries to the decryption oracle, there exists a quantum adversary $\mathcal B$ such that 
> $$\text{Adv}_\text{Kyber.KEM}^\text{cca}(\mathcal A) \leq 8 q_{RO}^2 \cdot \delta + 4 q_{RO} \cdot \sqrt{\text{Adv}_\text{Kyber.PKE}^{pr}(\mathcal B)}$$
