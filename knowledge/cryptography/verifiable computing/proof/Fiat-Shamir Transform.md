## Construction

> [!algorithm] Fiat Shamir Transform
> Let $\Pi = (P, V)$ be a [[Sigma Protocols|Sigma protocol]] for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$. Assume that conversations $(t, c, z)$ for $\Pi$ belong to $\mathcal T \times \mathcal C \times \mathcal Z$. Let $H: \mathcal Y \times \mathcal T \rightarrow \mathcal C$ be a hash function. We define the Fiat-Shamir non-interactive proof system $\text{FS-}\Pi = (GenPrf, VrfyPrf)$, with proof space $\mathcal P \mathcal S = \mathcal T \times \mathcal Z$, as follows:
> - On input $(x, y)$ in $\mathcal R$, $GenPrf$ first runs $P(x, y)$ to obtain a commitment $t \in \mathcal T$; it then feeds the challenge $c = H(y, t)$ to $P(x, y)$, obtaining a response $z \in \mathcal Z$; the output is $(t, z) \in \mathcal T \times \mathcal Z$;
> - On input $(y, (t, z)) \in \mathcal Y \times (\mathcal T \times \mathcal Z)$, $VrfyPrf$ verifies that $(t, c, z)$ is an accepting conversation for $y$, where $c = H(y, t)$.

## Soundness of FS

> [!theorem] Fiat-Shamir-Based Proofs are Sound
> Let $\Pi$ be a [[Sigma Protocols|Sigma protocol]] for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$, and let $\text{FS-}\Pi$ be the Fiat-Shamir non-interactive proof system derived from $\Pi$ with hash function $H$. If $\Pi$ is sound, and if we model $H$ as a random oracle, then $\text{FS-}\Pi$ is sound.
> 
> In particular, let $\mathcal A$ be a random oracle [[Non-Interactive Zero Knowledge#Non-Interactive Soundness|non-interactive soundness]] adversary attacking the soundness of FS-$\Pi$. Moreover, assume that $\mathcal A$ issues at most $Q_{ro}$ random oracle queries. Then there exists a [[Interactive Zero Knowledge#Soundness|soundness]] adversary $\mathcal B$ that attacks the soundness of $\Pi$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$ such that $$\text{niSnd}^{ro}\text{adv}[\mathcal A, \text{FS-}\Pi] \leq (Q_{ro} + 1) \text{Sndadv}[\mathcal B, \Pi]$$

## Zero Knowledge of FS

> [!theorem] Fiat-Shamir-Based Proofs are Zero Knowledge
> Let $\Pi = (P, V)$ be a special HVZK [[Sigma Protocols|Sigma protocol]] for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$ with unpredictable commitments, and let $\text{FS-}\Pi$ be the Fiat-Shamir non-interactive proof system derived from $\Pi$ with hash function $H$. If we model $H$ as a random oracle, then $\text{FS-}\Pi$ is niZK.
> 
> In particular, there exists a [[Non-Interactive Zero Knowledge#Simulator|simulator]] $Sim$ such that if $\mathcal A$ is a [[Non-Interactive Zero Knowledge#Non-Interactive Zero Knowledge|non-interactive zero knowledge]] adversary that attacks $\text{FS-}\Pi$ and $Sim$, making at most $Q_p$ proof queries and at most $Q_{ro}$ random oracle queries, and if $\Pi$ has $\delta$-unpredictable commitments, then we have $$\text{niZKadv}[\mathcal A, \text{FS-}\Pi, Sim] \leq Q_p(Q_p + Q_{ro}) \cdot \delta.$$
