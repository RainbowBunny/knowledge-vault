## Identification and Signatures from Sigma Protocols

> [!definition] Key Generation Algorithm
> Suppose we have a Sigma protocol $(P, V)$ for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$. In addition to $P$ and $V$, we need a **key generation algorithm for** $\mathcal R$. This is a probabilistic algorithm $G$ that generates a public-key/secret-key pair $(pk, sk)$, where $pk = y$ and $sk = (x, y)$ for some $(x, y) \in \mathcal R$.

> [!algorithm] One-way Key generation
> Let $G$ be a key generation algorithm for $\mathcal R \subseteq \mathcal X \times \mathcal Y$. For a given adversary $\mathcal A$, the attack game runs as follows:
> - The challenger runs $(pk, sk) \xleftarrow{R} G()$, and sends $pk = y$ to $\mathcal A$;
> - $\mathcal A$ output $\hat{x} \in \mathcal X$.
> 
> We say that the adversary wins the game if $(\hat{x}, y) \in \mathcal R$. We define $\mathcal A$'s advantage with respect to $G$, denoted $\text{OWadv}[\mathcal A, G]$, the quantity $\text{OWadv}[\mathcal A, G]$ is negligible.

> [!definition] One Way Key Generation
> We say that a key generation algorithm $G$ is **one way** if for all efficient adversaries $\mathcal A$, the quantity $\text{OWadv}[\mathcal A, G]$ is negligible.

> [!theorem]
> Let $(P, V)$ be a Sigma protocol for an effective relation $\mathcal R$ with a large challenge space. Let $G$ be a key generation algorithm for $\mathcal R$. If $(P, V)$ provides special soundness and $G$ is one-way, then the identification scheme $\mathcal I = (G, P, V)$ is secure against direct attacks.
> 
> In particular, suppose $\mathcal A$ is an efficient impersonating adversary attacking $\mathcal I$ via a [[#Password Protocols|direct attack]], with advantage $\epsilon = \text{ID1adv}[\mathcal A, \mathcal I]$. Then there exists an efficient adversary $\mathcal B$ attacking $G$ as in [[#Identification and Signatures from Sigma Protocols|one-way key generation]], with advantage $\epsilon' = \text{OWadv}[\mathcal B, G]$, such that $$\epsilon' \geq \epsilon^2 - \epsilon / N,$$ where $N$ is the size of the challenge space, which implies $$\epsilon \leq \frac{1}{N} + \sqrt{e'}.$$

> [!theorem]
> Let $(P, V)$ be a Sigma protocol for an effective relation $\mathcal R$. Let $G$ be a key generation algorithm for $\mathcal R$. If the identification protocol $\mathcal I = (G, P, V)$ is secure against direct attacks, and $(P, V)$ is special HVZK, then $\mathcal I$ is also secure against eavesdropping attacks.
> 
> In particular, for every impersonating adversary $\mathcal A$ that attacks $\mathcal I$ via an [[#Security Against Eavesdropping|eavesdropping attack]], there is an adversary $\mathcal B$ that attacks $\mathcal I$ via a [[#Password Protocols|direct attack]], where $\mathcal B$ is an elementary wrapper around $\mathcal A$, such that $$\text{ID2adv}[\mathcal A, \mathcal I] = \text{ID1adv}[\mathcal B, \mathcal I].$$

### The Fiat-Shamir Heuristic for Signatures

> [!algorithm] Fiat-Shamir Signature Scheme
> Building Block:
> - A Sigma protocol $(P, V)$ for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$; we assume that conversations are of the form $(t, c, z)$, where $t \in \mathcal T, c \in \mathcal C$, and $z \in \mathcal Z$;
> - A key generation algorithm $G$ for $\mathcal R$;
> - A hash function $H: \mathcal M \times \mathcal T \rightarrow \mathcal C$, which will be modeled as a random oracle; the set $\mathcal M$ will be the message space of the signature scheme.
> 
> The **Fiat-Shamir signature scheme** derived from $G$ and $(P, V)$ works as follows:
> - The key generation algorithm is $G$, so a public key is of the form $pk = y$, where $y \in \mathcal Y$, and a secret key is of the form $sk = (x, y) \in \mathcal R$.
> - To sign a message $m \in \mathcal M$ using the secret key $sk = (x, y)$, the signing algorithm runs as follows:
> 	- It starts the prover $P(x, y)$, obtaining a commitment $t \in \mathcal T$;
> 	- It computes a challenge $c \leftarrow H(m, t)$;
> 	- Finally, it feeds $c$ to the prover, obtaining a response $z$, and outputs the signature $\sigma = (t, z) \in \mathcal T \times \mathcal Z$.
> - To verify a signature $\sigma = (t, z) \in \mathcal T \times \mathcal Z$ on a message $m \in \mathcal M$ using a public key $pk = y$, the verification algorithm computes $c \leftarrow H(m, t)$, and checks that $(t, c, z)$ is an accepting conversation for $y$.

> [!definition] Unpredictable Commitments
> Let $(P, V)$ be a Sigma protocol for $\mathcal R \subseteq \mathcal X \times \mathcal Y$, and suppose that all conversations $(t, c, z)$ lie in $\mathcal T \times \mathcal C \times \mathcal Z$. We say that $(P, V)$ has **$\delta$-unpredictable commitments** if for every $(x, y) \in \mathcal R$ and $\hat{t} \in \mathcal T$, with probability at most $\delta$, an interaction between $P(x, y)$ and $V(y)$ produces a conversation $(t, c, z)$ with $t = \hat{t}$. We say that $(P, V)$ has **unpredictable commitments** if it is has $\delta$-unpredictable commitments for negligible $\delta$.

> [!theorem]
> If $H$ is modeled as a random oracle, the identification scheme $\mathcal I = (G, P, V)$ is secure against eavesdropping attacks, and $(P, V)$ has unpredictable commitments, then the Fiat Shamir signature scheme $\mathcal S$ derived from $G$ and $(P, V)$ is secure.
> 
> In particular, let $\mathcal A$ be an adversary attacking $\mathcal S$ as in the 
