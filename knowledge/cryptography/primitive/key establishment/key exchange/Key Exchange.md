
| Term                                            | Reference                                                       |                    |
| ----------------------------------------------- | --------------------------------------------------------------- | ------------------ |
| Attack Game 10.1 (Anonymous key exchange)       | [[#Anonymous Key Exchange\|anonymous key exchange]]             | $\text{AnonKEadv}$ |
| Attack Game 10.4 (Discrete logarithm)           | [[#Discrete Logarithm\|discrete logarithm]]                     | $\text{DLadv}$     |
| Attack Game 10.5 (Computational Diffie-Hellman) | [[#Computational Diffie-Hellman\|computational Diffie-Hellman]] | $\text{CDHadv}$    |
| Attack Game 10.6 (Decisional Diffie-Hellman)    | [[#Decisional Diffie-Hellman\|decisional Diffie-Hellman]]       | $\text{DDHadv}$    |

## Anonymous Key Exchange

> [!definition] Anonymous Key Exchange Problem
> Alice and Bob want to communicate online, adversary can eavesdrop their communication, thus they want to generate a **shared secret unknown to the adversary**. The anonymity in this problem is that there is no guarantee for Alice and Bob that they are talking to each other.

> [!definition] Key Exchange Protocol
> A **key exchange protocol** is a pair of probabilistic machine $(A, B)$ that take turns in sending messages to each other. At the end of the protocol, when both machine terminate, they both obtain the same value $k$.

> [!definition] Protocol Transcript
> A **protocol transcript** $T_P$ is the sequence of messages exchanged between the parties in one execution of the protocol.

> [!algorithm] Anonymous Key Exchange
> For a key exchange protocol $P = (A, B)$ and a given adversary $\mathcal A$, the attack game runs as follows:
> - The challenge runs the protocol between $A$ and $B$ to generate a shared key $k$ and transcript $T_P$. It gives $T_P$ to $\mathcal A$.
> - $\mathcal A$ outputs a guess $\hat k$ for $k$.
> 
> We define $\mathcal A$'s advantage, denoted $\text{AnonKEadv}[\mathcal A, P]$, as the probability that $\hat k = k.$

> [!proposition]
> We say that an anonymous key exchange protocol $P$ is secure against an eavesdropper if for all efficient adversaries $\mathcal A$, the quantity $\text{AnonKEadv}[\mathcal A, P]$ is negligible.

> [!remark]
> This definition is extremely weak
> - First, we assume the adversary is unable to tamper with messages.
> - Second, we only guarantee that the adversary cannot guess $k$ in its entirely. This does not rule out the possibility that the adversary cannot guess, say, half the bits of $k$. If we are to use $k$ as a secret session key, the property we would really like is that $k$ is indistinguishable from a truly random key.
> - Third, the protocol provides no assurance of the identities of the participants.

## Construction

### Based on Trapdoor Function Scheme

> [!algorithm] Key Exchange using a One-way Trapdoor Function Scheme
> - Alice computes $(pk, sk) \xleftarrow{R} G()$, and sends $pk$ to Bob.
> - Upon receiving $pk$ from Alice, Bob computes $x \xleftarrow{R} \mathcal X, y \leftarrow F(pk, x)$, and sends $y$ to Alice.
> - Upon receiving $y$ from Bob, Alice computes $x \leftarrow I(sk, y)$.

## Key Exchange

> [!algorithm] Generic Key Exchange Protocol
> The protocol makes use of two functions $E$ and $F$. Alice chooses a random secret $\alpha$, computes $E(\alpha)$, and sends $E(\alpha)$ to Bob over an insecure channel. Likewise, Bob chooses a random secret $\beta,$ computes $E(\beta),$ and sends $E(\beta)$ to Alice over an insecure channel. Alice and Bob both somehow compute a shared key $F(\alpha, \beta)$. In this high level description, $E$ and $F$ are some functions that should satisfy the following properties:
> 1. $E$ should be easy to compute;
> 2. Given $\alpha$ and $E(\beta),$ it should be easy to compute $F(\alpha, \beta)$;
> 3. Given $E(\alpha)$ and $\beta,$ it should be easy to compute $F(\alpha, \beta)$;
> 4. Given $E(\alpha)$ and $E(\beta),$ it should be hard to compute $F(\alpha, \beta)$.

### Diffie-Hellman

> [!algorithm] Diffie-Hellman Key Exchange Protocol
> We assume that the description of $\mathbb G$, including $g \in \mathbb G$ and $q$, is a system parameter that is generated once and for all at system setup time and shared by all parties involved. The protocol runs as follows:
> 1. Alice computes $\alpha \xleftarrow{R} \mathbb Z_q, u \leftarrow g^{\alpha},$ and sends $u$ to Bob.
> 2. Bob computes $\beta \xleftarrow{R} \mathbb Z_q, v \leftarrow g^{\beta},$ and sends $v$ to Alice.
> 3. Upon receiving $v$ from Bob, Alice computes $w \leftarrow v^{\alpha}$.
> 4. Upon receiving $u$ from Alice, Bob computes $w \leftarrow u^{\beta}$.
> 
> The secret shared by Alice and Bob is $$w = v^{\alpha} = g^{\alpha \beta} = u^{\beta}.$$

> [!definition] Discrete Logarithm
> For a fixed element $g \in \mathbb G,$ different from 1, the function from $\mathbb Z_q$ to $\mathbb G$ that sends $\alpha \in \mathbb Z_q$ to $g^{\alpha} \in \mathbb G$ is called the **discrete exponentiation function**. This function is one-to-one and onto, and its inverse function is called the **discrete logarithm function**, and is usually denoted $\text{Dlog}_g$; thus, for $u \in \mathbb G, \text{Dlog}_g(u)$ is the unique $\alpha \in \mathbb Z_q$ such that $u = g^{\alpha}$. The value $g$ is called the **base** of the discrete logarithm.

### Discrete Logarithm

> [!algorithm] Discrete Logarithm
> Let $\mathbb G$ be a cyclic group of prime order $q$ generated by $g \in \mathbb G$. For a given adversary $\mathcal A$, define the following attack game:
> - The challenger and the adversary $\mathcal A$ take a description of $\mathbb G$ as input. The description includes the order $q$ and a generator $g \in \mathbb G$.
> - The challenger computes $$\alpha \xleftarrow{R} \mathbb Z_q, u \leftarrow g^{\alpha},$$ and sends $u \in \mathbb G$ to the adversary.
> - The adversary outputs some $\hat{\alpha} \in \mathbb Z_q$.
> 
> We define $\mathcal A$'s **advantage in solving the discrete logarithm problem for** $\mathbb G$, denoted $\text{DLadv}[\mathcal A, \mathbb G]$, as the probability that $\hat{\alpha} = \alpha$.

> [!definition] Discrete Logarithm Assumption
> We say that the **discrete logarithm (DL) assumption** holds for $\mathbb G$ if for all efficient adversaries $\mathcal A$ the quantity $\text{DLadv}[\mathcal A, \mathbb G]$ is negligible.

> [!remark]
> We say that $g^{\alpha}$ is an **instance** of the **discrete logarithm (DL) problem (for $\mathbb G$)**, and that $\alpha$ is a solution to this problem instance. The DL assumption asserts that there is no efficient algorithm that can effectively solve the DL problem for $\mathbb G$.

### Computational Diffie-Hellman

> [!algorithm] Computational Diffie-Hellman
> Let $\mathbb G$ be a cyclic group of prime order $q$ generated by $g \in \mathbb G$. For a given adversary $\mathcal A,$ the attack game runs as follows.
> - The challenger and the adversary $\mathcal A$ takes a description of $\mathbb G$ as input. The description includes the order $q$ and a generator $g \in \mathbb G$.
> - The challenger computes $$\alpha, \beta \xleftarrow{R} \mathbb Z_q, u \leftarrow g^\alpha, v \leftarrow g^\beta, w \leftarrow g^{\alpha \beta}$$ and sends the pair $(u, v)$ to the adversary.
> - The adversary outputs some $\hat{w} \in \mathbb G$.
> 
> We define $\mathcal A$'s **advantage in solving the computational Diffie-Hellman problem for $\mathbb G$,** denoted $\text{CDHadv}[\mathcal A, \mathbb G],$ as the probability that $\hat{w} = w$.

> [!definition] Computational Diffie-Hellman Assumption
> We say that the **computational Diffie-Hellman (CDH)** assumption holds for $\mathbb G$ if for all efficient adversaries $\mathcal A$ the quantity $\text{CDHadv}[\mathcal A, \mathbb G]$ is negligible.

> [!remark]
> We say that $(g^{\alpha}, g^{\beta})$ is an **instance** of the **computational Diffie-Hellman (CDH) problem**, and that $g^{\alpha \beta}$ is a solution to this problem instance. The CDH assumption asserts that there is no efficient algorithm that can be effectively solve the CDH problem for $\mathbb G$.

### Decisional Diffie-Hellman

> [!algorithm] Decisional Diffie-Hellman
> Let $\mathbb G$ be a cyclic group of prime order $q$ generated by $g \in \mathbb G$. For a given adversary $\mathcal A$, we define two experiments.
> **Experiment** $b$ ($b = 0, 1$):
> - The challenger and the adversary $\mathcal A$ take a description of $\mathbb G$ as input.
> - The challenger computes $$\alpha, \beta, \gamma \xleftarrow{R} \mathbb Z_q, u \leftarrow g^\alpha, v \leftarrow g^\beta, w_0 \leftarrow g^{\alpha \beta}, w_1 \leftarrow g^\gamma,$$ and sends the triple $(u, v, w_b)$ to the adversary.
> - The adversary outputs a bit $\hat{b} \in \{0, 1\}$.
> 
> If $W_b$ is the event that $\mathcal A$ outputs 1 in Experiment $b$, we define $\mathcal A$'s **advantage in solving the decisional Diffie-Hellman problem for** $\mathbb G$ as $$\text{DDHadv}[\mathcal A, \mathbb G] = |P[W_0] - P[W_1]|.$$

> [!definition] Decisional Diffie-Hellman Assumption
> We say that the **decisional Diffie-Hellman (DDH)** assumption holds for $\mathbb G$ if for all efficient adversaries $\mathcal A$ the quantity $\text{DDHadv}[\mathcal A, \mathbb G]$ is negligible.

> [!remark]
> For $\alpha, \beta, \gamma \in \mathbb Z_q,$ we call $(g^\alpha, g^\beta, g^\gamma)$ a **DH-triple** if $\gamma = \alpha \beta$; otherwise, we call it a **non-DH-triple**. The DDH assumption says that there is no efficient algorithm that can effectively distinguish between random DH-triples and random triples.

### Random Self-Reducibility

> [!theorem]
> Consider a specific cyclic group $\mathbb G$ of prime order $q$ generated by $g \in \mathbb G$. Suppose $\mathcal A$ is an efficient algorithm with the following property: If $u \in \mathbb G$ is chosen at random, then $P[\mathcal A(u) = \text{Dlog}_g(u)] = \epsilon,$ where the probability is over the random choice of $u$ and the random choices made by $\mathcal A$. Then there is an efficient algorithm $\mathcal B$ with the following property: for all $u \in \mathbb G,$ algorithm $\mathcal B$ either outputs `fail` or $\text{Dlog}_g(u),$ and it outputs the latter with probability $\epsilon,$  where now the probability is only over the random choices made by $\mathcal B$.

> [!algorithm] Proof of Theorem
> Algorithm $\mathcal B$
> Input: $u \in \mathbb G$
> Output: $\text{Dlog}_g(u)$ or `fail`
> 1. $\sigma \xleftarrow R \mathbb Z_q$
> 2. $u_1 \leftarrow u \cdot g^\sigma \in \mathbb G$
> 3. $\alpha_1 \leftarrow \mathcal A(u_1)$
> 4. If $g^{\alpha_1} \neq u_1$ then `fail`, else output $\alpha \leftarrow \sigma_1 - \sigma$.

> [!remark] Importance of self reducibility
> If a problem is hard in the worst case, and we can prove self reducibility then the problem is hard on average.

