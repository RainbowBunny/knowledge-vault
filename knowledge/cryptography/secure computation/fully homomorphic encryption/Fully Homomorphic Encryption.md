
## Syntax

> [!definition] Parameters
> - $\lambda$: Security parameter.
> - $\mathcal{SK}$: Secret key space.
> - $\mathcal{PK}$: Public key space.
> - $\mathcal{M}$: Message space.
> - $\mathcal{C}$: Ciphertext space.

> [!definition] Fully Homomorphic Encryption (FHE)
> An **fully homomorphic encryption** scheme (for $\mathcal{SK}, \mathcal{PK}, \mathcal{M}, \mathcal{C}$) consists of four algorithms:
> - $(\mathrm{pk}, \mathrm{sk}) \leftarrow \mathsf{KeyGen}(1^\lambda)$: (Randomized) Key generation algorithm:
> 	- **Input**: Takes security parameter $\lambda$. 
> 	- **Output**: Returns public key $\mathrm{pk} \in \mathcal{PK}$ and secret key $\mathrm{sk} \in \mathcal{SK}$.
> - $c \leftarrow \mathsf{Enc}(\mathrm{pk}, m)$: (Randomized) Encryption algorithm:
> 	- **Input**: Takes public key $\mathrm{pk} \in \mathcal{PK}$ and message $m \in \mathcal{M}$.
> 	- **Output**: Returns ciphertext $c \in \mathcal{C}$.
> - $m \leftarrow \mathsf{Dec}(\mathrm{sk}, c)$: (Deterministic) Decryption algorithm:
> 	- **Input**: Takes secret key $\mathrm{sk} \in \mathcal{SK}$ and ciphertext $c \in \mathcal{C}$.
> 	- **Output**: Returns message $m \in \mathcal{M}$.
> - $c \leftarrow \mathsf{Eval}(\mathrm{pk}, f, (c_1, \dots, c_k))$: (Deterministic) Evaluation algorithm:
> 	- **Input**: Takes public key $\mathrm{pk}$, a circuit $f$ and a list of ciphertext $(c_1, \dots, c_k)$ which is the encryption of input of $f$.
> 	- **Output**: Returns a ciphertext which is the encryption of the output of $f$.

## Property

### Correctness

> [!definition] Correctness
> Experiment:
> 1. $(\mathrm{pk}, \mathrm{sk}) \xleftarrow{\$} \mathsf{KeyGen}(1^\lambda)$.
> 2. Generates $f: \mathcal{M}^k \rightarrow \mathcal{M}$.
> 3. $(m_1, \dots, m_k) \xleftarrow{\$} \mathcal{M}^k$.
> 4. $c_i \leftarrow \mathsf{Enc}(\mathrm{pk}, m_i) \; \forall i \in [1, k]$.
> 
> Target: $\mathsf{Dec}(\mathrm{sk}, \mathsf{Eval}(\mathrm{pk}, f, (c_1, \dots, c_k))) = f(m_1, \dots, m_k)$.
> 

### Compactness

> [!definition] Compactness
> Element of $C$ can be stored on $\lambda^{O(1)}$ bits.

### Bootstrapping

> [!definition] Bootstrapping
> **Setup (once, by the owner of $\mathrm{sk}_1$):** 
> - $\mathrm{bk}_i \leftarrow \mathsf{Enc}(\mathrm{pk}_2, \mathrm{sk}_{1,i})$ for $i \in [1, n_{sk}]$, and $\mathrm{bk} = (\mathrm{bk}_1, \dots, \mathrm{bk}_{n_{sk}})$.
> 
> ---
> $c' \leftarrow \mathsf{Refresh}(\mathrm{pk}_2, \mathrm{bk}, c)$: (Randomized) Bootstrapping algorithm:
> - **Input**: New public key $\mathrm{pk}_2$, bootstrapping key $\mathrm{bk}$, ciphertext $c$ (of $n_c$ bits) under $\mathrm{pk}_1$.
> - **Output**: Ciphertext $c'$ under $\mathrm{pk}_2$ with $\mathsf{Dec}(\mathrm{sk}_2, c') = \mathsf{Dec}(\mathrm{sk}_1, c)$.
> - **Steps**:
> 	1. $c_j' \leftarrow \mathsf{Enc}(\mathrm{pk}_2, c_j)$ for $j \in [1, n_c]$. (randomized)
> 	2. Return $\mathsf{Eval}(\mathrm{pk}_2, f_\mathsf{Dec}, (\mathrm{bk}_1, \dots, \mathrm{bk}_{n_{sk}}, c_1', \dots, c_{n_c}'))$. (deterministic)
>
> Remark: $\mathrm{pk}_2 = \mathrm{pk}_1$ requires circular security.

> [!definition] Augmented decryption circuit
> Let $\Gamma$ be a set of gates (e.g. $\{\mathsf{NAND}\}$ or $\{\mathsf{AND}, \mathsf{XOR}\}$). For a gate $g \in \Gamma$ of arity $t$, define the circuit
> $$f_{\mathsf{Dec},g}(\mathrm{sk}, c_1, \dots, c_t) = g\big(f_\mathsf{Dec}(\mathrm{sk}, c_1), \dots, f_\mathsf{Dec}(\mathrm{sk}, c_t)\big)$$
> taking the bits of $\mathrm{sk}$ and of $c_1, \dots, c_t$ as input.

> [!definition] Bootstrappable
> A scheme is **$\Gamma$-bootstrappable** if for every $g \in \Gamma$, $\mathsf{Eval}$ is correct on $f_{\mathsf{Dec},g}$. That is, for all $(\mathrm{pk}, \mathrm{sk})$ and all ciphertexts $c_1, \dots, c_t$ that decrypt correctly,
> $$\mathsf{Dec}\Big(\mathrm{sk}, \mathsf{Eval}\big(\mathrm{pk}, f_{\mathsf{Dec},g}, (\mathrm{bk}_1, \dots, \mathrm{bk}_{n_{sk}}, c'_{1,1}, \dots, c'_{t,n_c})\big)\Big) = g\big(\mathsf{Dec}(\mathrm{sk}, c_1), \dots, \mathsf{Dec}(\mathrm{sk}, c_t)\big)$$
> where $\mathrm{bk}_i = \mathsf{Enc}(\mathrm{pk}, \mathrm{sk}_i)$ and $c'_{s,j} = \mathsf{Enc}(\mathrm{pk}, c_{s,j})$.
>
> Equivalently: the circuit class that $\mathsf{Eval}$ handles correctly contains all augmented decryption circuits $f_{\mathsf{Dec},g}$, $g \in \Gamma$.

> [!theorem] Gentry's bootstrapping theorem
> If a scheme is $\Gamma$-bootstrappable, compact, and $\Gamma$ is complete (can express any circuit), then:
> 1. **Leveled FHE** (no extra assumption): take key pairs $(\mathrm{pk}_0, \mathrm{sk}_0), \dots, (\mathrm{pk}_L, \mathrm{sk}_L)$ with $\mathrm{bk}^{(i)} = \mathsf{Enc}(\mathrm{pk}_{i+1}, \mathrm{sk}_i)$. It evaluates circuits of depth $L$, and the evaluation key size grows with $L$.
> 2. **FHE** (unbounded depth): additionally assume circular security and use $\mathrm{pk}_{i+1} = \mathrm{pk}_i$.