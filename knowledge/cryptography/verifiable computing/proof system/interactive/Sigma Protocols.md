## Syntax

> [!definition] $\Sigma$-Protocol
> Let $\mathcal R \subseteq \mathcal X \times \mathcal W$ be an [[Effective Relation#Definition|Effective Relation]]. A **Sigma protocol** for $\mathcal R$ is a pair $(\mathcal P, \mathcal V)$.
> - $\mathcal P$ is an interactive protocol algorithm called the **prover**, which takes as input a statement-witness pair $(x, w) \in \mathcal R$.
> - $\mathcal V$ is an interactive protocol algorithm called the **verifier**, which takes as input a statement $x \in \mathcal X$, and which outputs `accept` or `reject`.
> - $\mathcal P$ and $\mathcal V$ are structured so that an interaction between them always works as follows:
> 	- **Commit Phase**: To start the protocol, $\mathcal P$ computes a message $t$, called the **commitment**, and sends $t$ to $\mathcal V$;
> 	- **Challenge Phase**: Upon receiving $\mathcal P$'s commitment $t$, $\mathcal V$ chooses a **challenge** $c$ at random from a finite **challenge space** $\mathcal C$, and sends $c$ to $P$;
> 	- **Response Phase**: Upon receiving $\mathcal V$'s challenge $c$, $\mathcal P$ computes a **response** $z$, and sends $z$ to $\mathcal V$;
> - Upon receiving $\mathcal P$'s response $z$, $\mathcal V$ outputs either `accept` or `reject`, which must be computed strictly as a function of the statement $x$ and the **conversation** $(t, c, z)$. In particular, $V$ does not make any random choices other than the selection of the challenge - all other computations are completely deterministic.
> 
> We require that for all $(x, w) \in \mathcal R$, when $P(x, w)$ and $V(x)$ interact with each other, $V(x)$ always outputs `accept`.

> [!definition] Accepting Conversation
> We require that the verifier computes its output as a function of the statement $y$ and its conversation $(t, c, z)$ with the prover. If the output is `accept` we call the conversation $(t, c, z)$ an **accepting conversation for** $y$.

> [!example] Schnorr's Sigma Protocol
> It should be clear that for Schnorr's identification protocol $(G, P, V)$, the pair $(P, V)$ is an example of a Sigma protocol for the relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$, where $$\mathcal X = \mathbb Z_q, \mathcal Y, \mathbb G, \text{and } \mathcal R = \{(\alpha, u) \in \mathbb Z_q \times \mathbb G: g^{\alpha} = u\}.$$ The challenge space $\mathcal C$ is a subset of $\mathbb Z_q$. We call $(P, V)$ **Schnorr's Sigma protocol**.

## Property

### Completeness



## Security


### Special Soundness

> [!definition] Special Soundness
> Let $(P, V)$ be a Sigma protocol for $\mathcal R \subseteq \mathcal X \times \mathcal Y$. We say that $(P, V)$ provides **special soundness** if there is an efficient deterministic algorithm $\text{Ext}$, called a **witness extractor**, with the following property: whenever $\text{Ext}$ is given as input a statement $y \in \mathcal Y$, and two accepting conversations $(t, c, z)$ and $(t, c', z')$, with $c \neq c'$, algorithm $\text{Ext}$ always outputs $x \in \mathcal X$ such that $(x, y) \in \mathcal R$ (i.e., $x$ is a witness for $y$).

### Special Honest Verifier Zero Knowledge

> [!definition] Special HVZK
> Let $(P, V)$ be a Sigma protocol for $\mathcal R \subseteq \mathcal X \times \mathcal Y$ with challenge space $\mathcal C$. We say that $(P, V)$ is **special honest verifier zero knowledge**, or **special HVZK**, if there exists an efficient probabilistic algorithm $\text{Sim}$ (called a **simulation**) that takes as input $(y, c) \in \mathcal Y \times \mathcal C$, and satisfies the following properties:
> 1. For all inputs $(y, c) \in \mathcal Y \times \mathcal C$, algorithm $\text{Sim}$ always outputs a pair $(t, z)$ such that $(t, c, z)$ is an accepting conversation for $y$;
> 2. For all $(x, y) \mathcal R$, if we compute $$c \xleftarrow{R} \mathcal C, (t, z) \xleftarrow{R} \text{Sim}(y, c),$$ then $(t, c, z)$ has the same distribution as that of a transcript of a conversation between $P(x, y)$ and $V(y)$.

### Okamoto's Protocol for Representations

> [!algorithm] Okamoto's Protocol
> - Relation: $\mathcal R = \{( (\alpha, \beta), u) \in \mathbb Z_q^2 \times \mathbb G : g^{\alpha} h^{\beta} = u\}.$
> - Challenge space $\mathcal C$: Subset of $\mathbb Z_q$.
> - The protocol $(P, V)$ runs as follows, where the prover $P$ is initialized with $((\alpha, \beta), u) \in \mathbb R$ and the verifier $V$ is initialized with $g \in \mathbb G$:
> 1. $P$ computes $$\alpha_t \xleftarrow{R} \mathbb Z_q, \beta_t \xleftarrow{R} \mathbb Z_q, u \leftarrow g^{\alpha_t} h^{\beta_t},$$ and sends the commitment $u_t$ to $V$;
> 2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends the challenge $c$ to $P$;
> 3. $P$ computes $$\alpha_z \leftarrow \alpha_t + \alpha c, \beta_z \leftarrow \beta_t + \beta c \in \mathbb Z_q,$$ and sends the response $(\alpha_z, \beta_z)$ to $V$;
> 4. $V$ checks if $g^{\alpha_z} h^{\beta_z} = u_t \cdot u^c$; if so $V$ outputs `accept`; otherwise, $V$ outputs `reject`.

> [!theorem]
> Okamoto's protocol is a Sigma protocol for the relation $\mathcal R$. Moreover, it provides special soundness and is special HVZK.

### The Chaum-Pedersen Protocol for DH-Triples

> [!algorithm] Chaum-Pedersen Protocol for DH-Triples
> - Relation: $\mathcal R = \{(\beta, (u, v, w)) \in \mathbb Z_q \times \mathbb G^3 : v = g^{\beta} \text{ and } w = u^\beta\}.$
> - Challenge space $\mathcal C$: Subset of $\mathbb Z_q$.
> - The protocol $(P, V)$ runs as follows, where the prover $P$ is initialized with $(\beta, (u, v, w)) \in \mathbb R$ and the verifier $V$ is initialized with $g, u \in \mathbb G$.
> 1. $P$ computes $$\beta_t \xleftarrow{R} \mathbb Z_q, v_t \leftarrow g^{\beta_t}, w_t \leftarrow u^{\beta_t}$$ and sends the commitment $v_t, w_t$ to $V$;
> 2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends the challenge $c$ to $P$;
> 3. $P$ computes $$\beta_z \leftarrow \beta_t + \beta c$$ and sends the response $\beta_z$ to $V$;
> 4. $V$ checks if $g^{\beta_z} = v_t \cdot v^c$ and $u^{\beta_z} = w_t \cdot w^c$.

> [!theorem]
> The Chaum-Pedersen protocol is a Sigma protocol for the relation $\mathcal R$. Moreover, it provides special soundness and is special HVZK.

### A Sigma Protocol for Arbitrary Linear Relations

> [!definition] Arbitrary Linear Relations
> Let $\mathbb G$ be a cyclic group of prime order $q$ generated by $g \mathbb G$. We shall consider boolean formulas $\phi$ of the following type: $$\phi(x_1, \dots, x_n) = \{\prod_{j = 1}^n g_{1j}^{x_j} = u_1 \land \cdots \land \prod_{j = 1}^n g_{mj}^{x_j} = u_m\}.$$

> [!algorithm] Generic Linear Protocol
> - Relation: $\mathcal R = \{((\alpha_1, \dots, \alpha_n), \phi) \in \mathbb Z_q^n \times \mathcal F: \phi(\alpha_1, \dots, \alpha_n) = true\}$.
> - Challenge space $\mathcal C$: Subset of $\mathbb Z_q$.
> - The protocol $(P, V)$ runs as follows, where the prover $P$ is initialized with $((\alpha_1, \dots, \alpha_n), \phi)$ and the verifier $V$ is initialized with $g$.
> 1. $P$ computes $\alpha_{t j} \xleftarrow{R} \mathbb Z_q (j = 1, \dots, n)$, $u_{ti} \leftarrow \prod_{j = 1}^n g_{i j}^{\alpha_{i j}} (i = 1, \dots, m)$ and sends the commitment $u_{t1}, \dots, u_{tm} \in \mathbb G$ to $V$;
> 2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends the challenge $c$ to $P$;
> 3. $P$ computes $$\alpha_{z j} \leftarrow \alpha_{t j} + \alpha_{j} c \quad (j = 1, \dots, n)$$ and sends the response $\alpha_{z 1}, \dots, \alpha_{z n} \in \mathbb Z_q$ to $V$.
> 4. $V$ checks if $\prod_{j = 1}^n g_{i j}^{\alpha_{z j}} = u_{i j} \cdot u_i^c \quad (i = 1, \dots, m)$.

> [!remark]
> - Schnorr's protocol is a special case with $\phi_1(x) := \{u = g^x\}$.
> - Okamoto's protocol is a special case with $\phi_2(x, y) := \{u = g^x h^y\}$.
> - The Chaum-Pederson protocol is a special case with $\phi_3(x) := \{v = g^x \land w = u^x\}$.

> [!theorem]
> The generic linear protocol is a Sigma protocol for the relation $\mathcal R$. Moreover, it provides special soundness and is special HVZK.

### A Sigma Protocol for the Pre-Image of a Homomorphism

> [!algorithm] Pre-Image of a Homomorphism Sigma Protocol
> - Relation: $\mathcal R = \{ (\alpha, (u, \psi)) \in \mathbb H_1 \times (\mathbb H_2 \times \mathcal F) : \psi(\alpha) = u\}$ where $\mathbb H_1$ and $\mathbb H_2$ be two finite abelian groups of known order and let $\psi: \mathbb H_1 \rightarrow \mathbb H_2$ be a group homomorphism.
> - The challenge space $\mathcal C$ is $\{0, 1, \dots, N - 1\} \subseteq \mathbb Z$ for some integer $N$.
> - The protocol $(P, V)$ runs as follows, where the prover $P$ is initialized with $(\alpha, (u, \psi))$ and the verifier $V$ is initialized with $g$.
> 1. $P$ computes $\alpha_t \xleftarrow{R} \mathbb H_1, u_1 \leftarrow \psi(\alpha_t)$ and sends the commitment $u_t \in \mathbb H_2$ to $V$.
> 2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends the challenge $c$ to $P$;
> 3. $P$ computes $\alpha_z \leftarrow \alpha_t + \alpha \cdot c \in \mathbb H_1$ and sends the response $\alpha_z \in \mathbb H_1$ to $V$.
> 4. $V$ checks if $\psi(\alpha_z) = u_t \cdot u^c$.

> [!theorem]
> The homomorphism protocol above is a Sigma protocol for the relation $\mathcal R$. Moreover, it is special HVZK, and provides special soundness whenever the smallest prime factor of $|\mathbb H_1| \times |\mathbb H_2|$ is at least $|\mathcal C|$.

### A Sigma Protocol for RSA

> [!algorithm] Guillou-Quisquater (GQ) Protocol
> - Relation: $\mathcal R = \{(x, y) \in \mathbb Z_n^* \times \mathbb Z_n^* : x^e = y\}$.
> - The challenge space $\mathcal C$ is $\{0, \dots, e - 1\}$.
> - The protocols $(P, V)$ runs as follows, where prover $P$ is initialized with $(x, y)$ and the verifier $V$ is initialized with $e$.
> 1. $P$ computes $x_t \xleftarrow{R} \mathbb Z_n^*, y_t \leftarrow x_t^e$ and sends the commitment $y_t$ to $V$.
> 2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends the challenge $c$ to $P$.
> 3. $P$ computes $x_z \leftarrow x_t \cdot x^c$, and sends the response $x_z$ to $V$.
> 4. $V$ checks if $x_z^e = y_t \cdot y^c$.

> [!theorem]
> The GQ protocol is a Sigma protocol for the relation $\mathcal R$. Moreover, it provides special soundness and is special HVZK.

