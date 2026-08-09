
## MAYO Trapdoor

> [!remark]
> A homogenous quadratic polynomial can be written as $$p(x) = x^\top P x$$ with $P$ is a matrix.

> [!algorithm] MAYO Trapdoor
> ### Parameters
> - $q$: Finite field size
> - $n$: Number of variables for each quadratic polynomial
> - $m$: Number of quadratic polynomial
> - $o$: Oil-space (hidden subspace) dimension
> - $k$: Number of vectors in the signature representation
> 
> ---
> ### Algorithms
> - $(pk, sk) \leftarrow \text{TrapGen}()$:
> 	1. Sample $O \in \mathbb F_q^{(n - o) \times o}$ uniformly at random.
> 	2. Sample $m$ homogenous quadratic polynomial $\mathcal T = (p_1, \dots, p_m)$ in $n$ variables, uniformly at random subject to the constraint that they evaluate to zero on the row-space of $\begin{pmatrix}O & 1_o\end{pmatrix}$.
> 	3. Output $(sk = O, pk = \mathcal T)$.
> - $\mathbb F_q^m \leftarrow \text{Eval}(\mathcal T, s = (s_1, \dots, s_k))$: Evaluate the Public Function
> 	1. Output $T^*(s) = \sum_{i = 1}^k E_{i, i} \mathcal T(s_i) + \sum_{i = 1}^k \sum_{j = i + 1}^k E_{i, j} \mathcal T'(s_i, s_j)$.
> - $s \leftarrow \text{SamplePre}(O, t \in \mathbb F_q^m)$: Find a Preimage
> 	1. Let $O = \text{rowspan}\begin{pmatrix}O & 1_o\end{pmatrix}$. Set $ctr = 0$.
> 	2. Sample $v = (v_1, \dots, v_k) \in \mathbb F_q^{n \times k}$ uniformly at random, deterministically based on $(O, ctr)$.
> 	3. If the linear map $A_v: O^k \rightarrow \mathbb F_q^m: o \mapsto \mathcal T^*(v + o)$ does not have rank $m$, increase the $ctr$ by 1 and go to step 1.
> 	4. Sample a solution $o$ to the linear system $\mathcal T^*(v + o) = t$ uniformly at random, deterministically based on $(O, ctr)$.
> 	5. Output $s = v + o$.


> [!algorithm] Lattice-based NIBS
> ### Parameters
> - $q$: Modulus
> - $\chi_s, \chi_e, \chi_\gamma$: Efficiently sampleable short distributions.
> - $\mathcal Y$: Nonce space.
> - $B_s, B_e, B_y, B_v, B_\Gamma, B$: public bounds.
> - $p$
> - $\alpha$
> - $\mathcal C$: Challenge space
> - $R_q$: $\mathbb Z_q[X] / (X^n + 1)$
> 
> ---
> ### Building Blocks:
> - $H_{msg}: \{0, 1\}^* \rightarrow \{0, 1\}^{256}, H_{chal}: \{0, 1\}^* \rightarrow \mathcal C$.
> - $H_{mat}: \mathcal Y \rightarrow R_q^{\ell \times \ell}$
> - $\text{TrapGen}, \text{SamplePre}$ from MAYO Trapdoor.
> - Proof Relation $\Pi_{DR} = (\text{Prove}_{DR}, \text{Verify}_{DR})$ is an argument of knowledge for the relation:
> 	- Public instance: $x = (vk, M, \Gamma)$, $vk = (A, t)$.
> 	- Witness: $\omega = (s_R, e_R, y, v, e_\Gamma)$, and thus we can calculate $pk_R = As_R + e_R, s_y = H_{mat}(y) s_R, u = As_y + v$.
> 	- Relation: 
> 		1. $y \in \mathcal Y$
> 		2. $||s_R|| \leq B_s, ||e_R|| \leq B_e, ||v|| \leq B_v, ||e_\Gamma|| \leq B_\Gamma$
> 		3. $Av = t - pk_R - Ay \pmod q$
> 		4. $\Gamma = u + e_\Gamma \pmod q$
> 		5. $\lfloor \Gamma \rceil_p = \lfloor u \rceil_p$
> 		6. $M = H_{msg}(\lfloor \Gamma \rceil_p, vk)$.
> 
> ---
> ### Algorithms
> - $\text{Setup}(1^\lambda)$
> - $(sk_S, vk_S) \leftarrow \text{Gen}_S(pp)$: Signer key generation
> 	1. $(A, T_A) \leftarrow \text{TrapGen}(1^\lambda, k, \ell, q)$
> 	2. Sample $t \leftarrow R_q^k$, and output $sk = T_A, vk = (A, t)$.
> - $(sk_R, pk_R) \leftarrow \text{Gen}_R(vk_S)$: Receiver key generation
> 	1. Sample $s_R \leftarrow \chi_s^\ell$ and $e_R \leftarrow \chi_e^k$.
> 	2. Compute $pk_R = As_R + e_R \pmod q$ and $sk_R = (s_R, e_R)$
> - $(\text{psig}, \text{nonce}) \leftarrow \text{Issue}(sk_S, vk_S, pk_R)$:
> 	1. Sample $y \in \mathcal Y$ and compute $t_{tar} = t - pk_R - Ay \pmod q$
> 	2. Using the trapdoor, sample a short preimage $v \leftarrow \text{SamplePre}(A, t_{tar})$
> 	3. Output $(\text{psig} = v, \text{nonce} = y)$
> - $(M, \sigma) \leftarrow \text{Obtain}(sk_R, vk_S, \text{psig}, \text{nonce})$
> 	1. Calculate $pk_R = A s_R + e_R$
> 	2. If $Av \neq t - pk_R - Ay \pmod q$, or if any required norm check fails, output $\perp$.
> 	3. Set $s_y = H_{mat}(y) s_R, u = As_y + v \pmod q$.
> 	4. Sample $e_\Gamma \leftarrow \chi_\Gamma^k$ until $[u + e \Gamma]_p = [u]_p$.
> 	5. Set $\Gamma = u + e \Gamma \pmod q, M = H_{msg}(\lfloor \Gamma \rceil_p, vk)$.
> 	6. Generate $\pi_{DR} = \text{Prove}_{DR}(x = (vk, M, \Gamma), \omega = (s_R, e_R, y, v, e_\Gamma))$.
> 	7. The signature is $\sigma = (\Gamma, \pi_{DR})$
> - $\text{Verify}(vk, M, \sigma)$:
> 	1. Reject if $M \neq H_{msg}(\lfloor \Gamma \rceil, vk)$
> 	2. Then accept iff $\text{Verify}_{DR}(x = (vk, M, \Gamma), \pi_{DR}) = 1$. 

