
> [!question] 1-out-of-$n$ Oblivious Transfer
> Let's call the newspaper the *sender* and call Bob the *receiver*. Bob wants a solution to the following problem:
> The sender has data $m_1, \dots, m_n \in \mathcal M$ and the receiver has an index $i \in \{1, \dots, n\}$. They want a protocol with the following property: when the protocol completes the receiver learns $m_i$ and nothing else, while the sender learns nothing about $i$.

## Construction

### From ElGamal Encryption

> [!algorithm] Secure OT from ElGamal Encryption
> The protocol uses the following ingredients:
> - A cyclic group $\mathbb G$ of prime order $q$ with generator $g \in \mathbb G$;
> - A hash function $H: \mathbb G^2 \rightarrow \mathcal K$, which will be modeled as a random oracle;
> - A semantically secure symmetric cipher $(E_s, D_s)$ with key space $\mathcal K$ and message space $\mathcal M$.
> 
> ---
> - **Step 1**: The sender chooses $\beta \xleftarrow{R} \mathbb Z_q$, computes $v \leftarrow g^{\beta} \in \mathbb G$, and sends $v$ to the receiver.
> - **Step 2**: The receiver chooses $\alpha \xleftarrow{R} \mathbb Z_q$, computes $u \leftarrow g^{\alpha} v^{-i} \in \mathbb G$, and sends $u$ to the sender,
> - **Step 3**: For $j = 1, \dots, n$ the sender computes
> 	- $u_j \leftarrow u \cdot v^j \in \mathbb G$
> 	- $w_j \leftarrow u_j^\beta$
> 	- $k_j \leftarrow H(v, w_j) \in \mathcal K$
> 	- $c_j \xleftarrow{R} E_s(k_j, m_j)$
> 	and sends the vector of ciphertexts $C = (c_1, \dots, c_n)$ to the receiver. Note that all $n$ ElGamal ciphertexts $(v, c_1), \dots, (v, c_n)$ are generated using the same encryption randomness $\beta$.
> - **Step 4**: The receiver, who has the secret key $\alpha$ for the ElGamal public-key $u_i = g^{\alpha}$, decrypts $c_i$ as follows:
> 	- Compute $w \leftarrow v^{\alpha}, k \leftarrow H(v, w)$
> 	- Output $m \leftarrow D_s(k, c_i)$

### Oblivious PRFs

> [!definition] Oblivious PRF Protocol
> Let $F$ be a [[Pseudorandom Functionsss#PRF Security|secure PRF]] defined over $(\mathcal K, \mathcal X, \mathcal Y)$. Suppose that one party, the **sender**, has the PRF key $k \in \mathcal K$. Another party, the **receiver**, has an input $x \in \mathcal X$. An **oblivious PRF protocol**, or simply an **OPRF protocol**, is a protocol that lets the receiver learn the output $y = F(k, x)$ without learning anything else about the value of the PRF at any other input; in addition, the sender learns nothing about the input $x$. Moreover, the OPRF protocol may be run many times, allowing the receiver to learn the value of $F(k, \cdot)$ for several inputs. The sender should learn nothing about any of these inputs, and the receiver should learn nothing about the value of $F(k, \cdot)$ at any other inputs. Actually, all we will really require here is that the receiver cannot learn anything about the value of $F(k, \cdot)$ at $\ell$ inputs useless it interacts with the sender $\ell$ or more times.

> [!algorithm] OPRF1
> Component: [[Pseudorandom Functionsss#Construction from CDH|CDH-based PRF]] $H'$, [[Pseudorandom Functionsss#Construction from DDH|DDH-based PRF]] $H$.
> Suppose that the sender has a key $k \in \mathbb Z_q$. In each run of the protocol, the receiver has an input $x \in \mathcal X$, and the sender and receiver interact (over a secure channel) as follows:
> - **Receiver**: Choose $\rho \xleftarrow{R} \mathbb Z_q \backslash \{\}$, compute $v \leftarrow H(x)^{\rho} \in \mathbb G$, and send $v$ to the sender.
> - **Sender**: Compute $w \leftarrow v^k \mathbb G$ and send $w$ to the receiver.
> - **Receiver**: Compute and output $y \leftarrow H'(x, w^{1/p}) \in \mathcal Y$.

> [!algorithm] OPRF2
> The protocol begins by having the sender publish the value $u = g^k$, where $k$ is the sender's secret key. In each run of the protocol, the receiver has an input $x \in \mathcal X$, and the sender and receiver interact (over a secure channel) as follows: 
> - **Receiver**: Choose $\rho \xleftarrow{R} \mathbb Z_q \backslash \{0\}, \tau \xleftarrow{R} \mathbb Z_q$, compute $v \leftarrow H(x)^\rho \cdot g^\tau \in \mathbb G$, and send $v$ to sender.
> - **Sender**: Compute $w \leftarrow v^k \in \mathbb G$ and send $w$ to the receiver.
> - **Receiver**: Compute and output $y \leftarrow H'(x, (w / u^\tau)^{1 / \rho}) \in \mathcal Y$.

## Adaptive Oblivious Transfer

