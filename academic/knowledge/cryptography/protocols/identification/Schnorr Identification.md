## Schnorr's Identification Protocol

> [!algorithm] Schnorr's Identification Protocol
> Let $\mathcal C$ be a subset of $\mathbb Z_q$. Then Schnorr's identification protocol is $\mathcal I_{sch} = (G, P, V)$, where:
> - The key generation algorithm $G$ runs as follows: $$\alpha \xleftarrow{R} \mathbb Z_q, u \leftarrow g^{\alpha}.$$ The verification key is $vk := u$, and the secret key is $sk := \alpha$.
> - The protocol between $P$ and $V$ runs as follows, where the prover $P$ is initialized with $sk = \alpha$, and the verifier $V$ is initialized with $vk = u$:
> 	1. $P$ computes $\alpha_t \xleftarrow{R} \mathbb Z_q, u_t \leftarrow g^{\alpha_t}$, and sends $u_t$ to $V$;
> 	2. $V$ computes $c \xleftarrow{R} \mathcal C$, and sends $c$ to $P$;
> 	3. $P$ computes $\alpha_z \leftarrow \alpha_t + \alpha c \in \mathbb Z_q$, and sends $\alpha_z$ to $V$;
> 	4. $V$ checks if $g^{\alpha_z} = u_t \cdot u^c$; if so $V$ outputs `accept`; otherwise, $V$ outputs `reject`.

> [!definition]
> An interaction between $P(\alpha)$ and $V(u)$ generates a **conversation** $(u_t, c, \alpha_z) \in \mathbb G \times \mathcal C \times \mathbb Z_q$. We call such a conversation an **accepting conversation for** $u$ if $V$'s check passes, i.e., if $g^{\alpha_z} = u_t \cdot u^c$. The set $\mathcal C$ is called the **challenge space**.

> [!theorem]
> Under the DL assumption for $\mathbb G$, and assuming $N := |\mathcal C|$ is super-poly, Schnorr's identification protocol is secure against direct attacks.
> 
> In particular, suppose $\mathcal A$ is an efficient impersonation adversary attacking $\mathcal I_{sch}$ via a direct attack with advantage $\epsilon := \text{ID1adv}[\mathcal A, \mathcal I_{sch}]$. Then there exists an efficient DL adversary $\mathcal B$ (whose running time is about twice that of $\mathcal A$), with advantage $\epsilon' := \text{DLadv}[\mathcal B, \mathbb G]$, such that $$\epsilon' \geq \epsilon^2 - \epsilon / N,$$ which implies $$\epsilon \leq \frac{1}{N} + \sqrt{\epsilon'}.$$

> [!lemma] Rewinding Lemma
> Let $S$ and $T$ be finite, non-empty sets, and let $f : S \times T \rightarrow \{0, 1\}$ be a function. Let $X$, $Y$ and $Y'$ be mutually independent random variables, where $X$ takes values in the set $S$, and $Y$ and $Y'$ are each uniformly distributed over $T$. Let $\epsilon := P[f(X, Y) = 1]$ and $N := |T|$. Then $$P[f(X, Y) = 1 \land f(X, Y') = 1 \land Y \neq Y'] \geq \epsilon^2 - \epsilon / N.$$

### Security Against Eavesdropping

> [!definition] Honest Verifier Zero Knowledge
> Let $\mathcal I = (G, P, V)$ be an identification protocol. We say that $\mathcal I$ is **honest verifier zero knowledge**, or **HVZK** for short, if there exists an efficient probabilistic algorithm $\text{Sim}$ (called a **simulator**) such that for all possible outputs $(vk, sk)$ of $G$, the output distribution of $\text{Sim}$ on input $vk$ is identical to the distribution of a transcript of a conversation between $P$ (on input $sk$) and $V$ (on input $vk$).

> [!theorem]
> If an identification protocol $\mathcal I$ is secure against direct attacks, and is HVZK, then it is secure against eavesdropping attacks.
> 
> In particular, if $\mathcal I$ is HVZK with simulator Sim, then for every impersonation adversary $\mathcal A$ that attacks $\mathcal I$ via an [[#Security Against Eavesdropping|eavesdropping attack]], obtaining up to $Q$ transcripts, there is an adversary $\mathcal B$ that attacks $\mathcal I$ via a [[#Password Protocols|direct attack]], where $\mathcal B$ is an elementary wrapper around $\mathcal A$ (and where $\mathcal B$ runs Sim at most $Q$ times), such that $$\text{ID2adv}[\mathcal A, \mathcal I] = \text{ID1adv}[\mathcal B, \mathcal I].$$

> [!theorem]
> Schnorr's identification protocol is HVZK.

> [!theorem]
> If Schnorr's identification protocol is secure against direct attacks, then it is also secure against eavesdropping attacks.
> 
> In particular, for every impersonation adversary $\mathcal A$ that attacks $\mathcal I_{sch}$ via an [[#Security Against Eavesdropping|eavesdropping attack]], there is an adversary $\mathcal B$ that attacks $\mathcal I_{sch}$ via a [[#Password Protocols|direct attack]], where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{ID2adv}[\mathcal A, \mathcal I_{sch}] = \text{ID1adv}[\mathcal B, \mathcal I_{sch}].$$

> [!remark]
> We still don't know if Schnorr's identification protocol is secure against [[#Security Against Active Attacks|active attacks]]: there are no known effective, active attacks, but there is also no proof that rules out such an attack under the DL assumption.

## From Identification Protocols to Signatures

> [!algorithm] Schnorr Signature Scheme
> The Schnorr signature scheme is $\mathcal S_{sch} = (G, S, V)$, where:
> - The key generation algorithm $G$ runs as follows: $$\alpha \xleftarrow{R} \mathbb Z_q, u \leftarrow g^{\alpha}.$$
> The public key is $pk := u$, and the secret key is $sk := \alpha$.
> - To sign a message $m \in \mathcal M$ using a secret key $sk = \alpha$, the signing algorithm runs as follows: $$\begin{gather}S(sk, m) := \alpha_t \xleftarrow{R} \mathbb Z_q, u_t \leftarrow u^{\alpha_t}, c \leftarrow H(m, u_t), \alpha_z \leftarrow \alpha_t + \alpha c \\ \text{output } \sigma := (u_t, \alpha_z)\end{gather}$$
> - To verify a signature $\sigma = (u_t, \alpha_z)$ on a message $m \in \mathcal M$, using the public key $pk = u$, the signature verification algorithm $V$ computes $c \leftarrow H(m, u_t)$, and outputs `accept` if $g^{\alpha_z} = u_t \cdot u^c$, and outputs `reject`, otherwise.

### Repeated Impersonating Attacks

> [!algorithm] $r$-Impersonating Eavesdropping Attacks
> For a given identification protocol $\mathcal I = (G, P, V)$, positive integer $r$, and adversary $\mathcal A$, the attack runs as follows. The key generation and eavesdropping phase is exactly the same as in [[#Security Against Eavesdropping|eavesdropping attack]].
> The only difference is that in the impersonation phase, the adversary $\mathcal A$ is allowed to interact **concurrently** with up to $r$ verifiers. The challenger plays the role of these verifiers, all of which use the same verification key as generated during the key generation phase. The adversary wins the game if it makes any of these verifiers output `accept`.
> We define $\mathcal A$'s advantage with respect to $\mathcal I$ and $r$, denoted $\text{rID2adv}[\mathcal A, \mathcal I, r]$, as the probability that $\mathcal A$ wins the game.

> [!lemma]
> Let $\mathcal I$ be an identification protocol. For every $r$-impersonation eavesdropping adversary $\mathcal A$, there exists a standard eavesdropping adversary $\mathcal B$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{rID2adv}[\mathcal A, \mathcal I, r] \leq r \cdot \text{ID2adv}[\mathcal B, \mathcal I].$$

### Security Analysis of Schnorr Signatures

> [!theorem] 
> If $H$ is modeled as a random oracle and Schnorr's identification scheme is secure against eavesdropping attacks, then Schnorr's signature scheme is also secure.
> 
> In particular, let $\mathcal A$ be an adversary attacking $\mathcal S_{sch}$ as in the random oracle version Attack Game 13.1. Moreover, assume that $\mathcal A$ issues at most $Q_s$ signing queries and $Q_{ro}$ random oracle queries. Then there exists a $(Q_{ro} + 1)$-impersonating adversary $\mathcal B$ that attacks $\mathcal I_{sch}$ via an [[#Repeated Impersonating Attacks|r-impersonation eavesdropping attack]], where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{SIG}^{\text{ro}}\text{adv}[\mathcal A, \mathcal S_{sch}] \leq Q_s (Q_s + Q_{ro} + 1) / q + \text{rID2adv}[\mathcal B, \mathcal I_{sch}, Q_{ro} + 1].$$

> [!lemma]
> Consider Schnorr's identification protocol $\mathcal I_{sch}$, defined with respect to a group $\mathbb G$ of prime order $q$ generated by $g \in \mathbb G$, and with a challenge space $\mathcal C$ of size $N$. For every efficient $r$-impersonation eavesdropping adversary $\mathcal A$ attacking $\mathcal I_{sch}$, with advantage $\epsilon := \text{rID2adv}[\mathcal A, \mathcal I, r]$, there exists an efficient DL adversary $\mathcal B$ (whose running time is about twice that of $\mathcal A$), with advantage $\epsilon' := \text{DLadv}[\mathcal B, \mathbb G]$, such that $$\epsilon' \geq \epsilon^2 / r - \epsilon / N,$$ which implies $$\epsilon \leq \frac{r}{N} + \sqrt{r \epsilon'}.$$

