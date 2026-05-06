
| Term                                              | Reference                                                           |                   |
| ------------------------------------------------- | ------------------------------------------------------------------- | ----------------- |
| Attack Game 20.1 (Soundness)                      | [[#Soundness\|soundness]]                                           | $\text{Sndadv}$   |
| Attack Game 20.2 (Non-Interactive Soundness)      | [[#Non-interactive Soundness\|non-interactive soundness]]           | $\text{niSndadv}$ |
| Attack Game 20.3 (Non-Interactive Zero Knowledge) | [[#Non-Interactive Zero Knowledge\|non-interactive zero knowledge]] | $\text{niZKadv}$  |

## Languages

> [!definition] Languages of True Statements
> Let $\mathcal R \subseteq \mathcal X \times \mathcal Y$ be an effective relation. We say a statement $y \in \mathcal Y$ is a **true statement** if $(x, y) \in \mathcal R$ for some $x \in \mathcal X$; otherwise, we say that $y \in \mathcal Y$ is a **false statement**. We define $L_{\mathcal R}$, which is called **language defined by** $\mathcal R$, to be the set of all true statements; that is, $L_{\mathcal R} = \{y \in \mathcal Y: (x, y) \in \mathcal R \text{ for some } x \in \mathcal X\}$.

### Soundness

> [!algorithm] Soundness
> Let $\Pi = (P, V)$ be a [[Identification Protocol#Sigma Protocols|Sigma protocol]] for $\mathcal R \subseteq \mathcal X \times \mathcal Y$. For a given adversary $\mathcal A$, the attack game runs as follows:
> - The adversary chooses a statement $y^* \in \mathcal Y$ and gives this to the challenger.
> - The adversary now interacts with the verifier $V(y^*)$, where the challenger plays the role of verifier and the adversary plays the role of a possibly "cheating" prover.
> 
> We say that the adversary wins the game if $V(y^*)$ outputs $\text{accept}$ but $y^* \notin L_{\mathcal R}$. We define $\mathcal A$'s advantage with respect to $\Pi$, denoted $\text{Sndadv}[\mathcal A, \Pi]$, as the probability that $\mathcal A$ wins the game.

> [!definition] Sound
> We say that $\Pi$ is **sound** if for all efficient adversaries $\mathcal A$, the quantity $\text{Sndadv}[\mathcal A, \Pi]$ is negligible.

> [!theorem] Special Soundness implies Soundness
> Let $\Pi$ be a [[Identification Protocol#Sigma Protocols|Sigma protocol]] with a large challenge space. If $\Pi$ provides special soundness, then $\Pi$ is sound.
> 
> In particular, for every adversary $\mathcal A$, we have $$\text{Sndadv}[\mathcal A, \Pi] \leq \frac{1}{N},$$ where $N$ is the size of the challenge space.

## Non-Interactive Proof Systems

> [!definition] Non-interactive Proof System
> Let $\mathcal R \subseteq \mathcal X \times \mathcal Y$ be an effective relation. A **non-interactive proof system for $\mathcal R$** is a pair of algorithms $(GenPrf, VrfyPrf)$, where:
> - $GenPrf$ is an efficient probabilistic algorithm that is invoked as $\pi \xleftarrow{R} GenPrf(x, y)$, where $(x, y) \in \mathcal R$, and $\pi$ belongs to some **proof space** $\mathcal P \mathcal S$;
> - $VrfyPrf$ is an efficient deterministic algorithm that is invoked as $VrfyPrf(y, \pi)$, where $y \in \mathcal Y$ and $\pi \in \mathcal P \mathcal S$; the output of $VrfyPrf$ is either $\text{accept}$ or $\text{reject}$. If $VrfyPrf(y, \pi) = \text{accept}$, we say $\pi$ **is a valid proof for** $y$.
> 
> We require that for all $(x, y) \in \mathcal R$, the output of $GenPrf(x, y)$ is always a valid proof for $y$.

### Simulator

> [!definition] Simulator
> Suppose that $\Phi$ makes use of a hash function $H: \mathcal U \rightarrow \mathcal C$, and that we wish to model $H$ as a random oracle. A **simulator for** $\Phi$ is an interactive machine $Sim$ that responds to a series of queries, where each query is one of two types:
> - $(\text{sim-proof-query}, y)$, where $y \in \mathcal Y$, to which $Sim$ replies with $\pi \in \mathcal P \mathcal S$;
> - $(\text{sim-oracle-query}, u)$, where $u \in \mathcal U$, to which $Sim$ replies with $c \in \mathcal C$.

### Non-Interactive Soundness

> [!algorithm] Non-Interactive Soundness
> Let $\Phi = (GenPrf, VrfyPrf)$ be a non-interactive proof system for $\mathcal R \subseteq \mathcal X \times \mathcal Y$ with proof space $\mathcal P \mathcal S$. To attack $\Phi$, an adversary $\mathcal A$ outputs a statement $y^* \in \mathcal Y$ and a proof $\pi^* \in \mathcal P \mathcal S$.
> We say that the adversary wins the game if $VrfyPrf(y^*, \pi^*) = \text{accept}$ but $y^* \notin L_{\mathcal R}$. We define $\mathcal A$'s advantage with respect to $\Phi$, denoted $\text{niSndadv}[\mathcal A, \Phi]$, as the probability that $\mathcal A$ wins the game.

> [!definition] Non-Interactive Soundness
> We say that $\Phi$ is **sound** if for all efficient adversaries $\mathcal A$, the quantity $\text{niSndadv}[\mathcal A, \Phi]$ is negligible.

### Non-Interactive Zero Knowledge

> [!algorithm] Non-Interactive Zero Knowledge
> Let $\Phi = (GenPrf, VrfyPrf)$ be a non-interactive proof system for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$ with proof space $\mathcal P \mathcal S$. Suppose that $\Phi$ makes use of a hash function $H: \mathcal U \rightarrow \mathcal C$, which is modeled as a random oracle. Let $Sim$ be a [[#Simulator|simulator]] for $\Phi$, as above. For a given adversary $\mathcal A$, we define two experiments, Experiment 0 and Experiment 1. In both experiments, the adversary makes a series of queries to the challenger, each of which is of the form:
> - *A proof query*, which is of the form $(x, y) \in \mathcal R$, and to which the challenger replies with $\pi \in \mathcal P \mathcal S$;
> - *A random oracle query*, which is of the form $u \in \mathcal U$, and to which the challenger replies with $c \in \mathcal C$.
> 
> In Experiment 0 (the "real world"), the challenger chooses $\mathcal O \in \text{Funs}[\mathcal U, \mathcal C]$ at random, answering each proof query $(x, y) \in \mathcal R$ by running $\text{GenPrf}(x, y)$, using $\mathcal O$ in place of $H$, and answering each random oracle query $u \in \mathcal U$ with $\mathcal O(u)$.
> 
> In Experiment 1 (the "simulated world"), the challenger answers each proof query $(x, y) \in \mathcal R$ by passing $(\text{sim-proof-query}, y)$ to $Sim$, and answers each random oracle query $u \in \mathcal U$ by passing $(\text{sim-oracle-query}, u)$ to $Sim$.
> 
> For $b = 0, 1$, let $W_b$ be the event that $\mathcal A$ outputs 1 in Experiment $b$. We define $\mathcal A$'s **advantage** with respect to $\Phi$ and $Sim$ as $$\text{niZKadv}[\mathcal A, \Phi, Sim] = |P[W_0] - P[W_1]|.$$

> [!definition] Non-Interactive Zero Knowledge (niZK) in the Random Oracle Model
> We say $\Phi$ provides **non-interactive zero knowledge (niZK) in the random oracle model**, if there exists an efficient simulator $Sim$ for $\Phi$, such that for every efficient adversary $\mathcal A$, the value $\text{niZKadv}[\mathcal A, \Phi, Sim]$ is negligible.

### Special Computational HVZK

> [!algorithm] Special cHVZK
> Let $\Pi = (P, V)$ be a [[Identification Protocol#Sigma Protocols|Sigma protocol]] for $\mathcal R \subseteq \mathcal X \times \mathcal Y$, with challenge space $\mathcal C$. Let $Sim$ be a [[#Simulator|simulator]] for $\Pi$. For a given adversary $\mathcal A$, we define two experiments, Experiment 0 and Experiment 1. In both experiments, $\mathcal A$ starts out by computing $(x, y) \in \mathcal R$ and submitting $(x, y)$ to the challenger.
> - In Experiment 0, the challenger runs the protocol between $P(x, y)$ and $V(y)$, and gives the resulting conversation $(t, c, z)$ to $\mathcal A$.
> - In Experiment 1, the challenger computes $$c \xleftarrow{R}, (t, z) \xleftarrow{R} Sim(y, c),$$ and gives the simulated conversation $(t, c, z)$ to $\mathcal A$.
> 
> At the end of the game, $\mathcal A$ computes and outputs a bit $\hat{b} \in \{0, 1\}$.
> For $b = 0, 1$, let $W_b$ be the event that $\mathcal A$ outputs 1 in Experiment $b$. We define $\mathcal A$'s **advantage** with respect to $\Pi$ and $Sim$ as $$\text{cHVZKadv}[\mathcal A, \Pi, Sim] = |P[W_0] - P[W_1]|.$$

> [!definition] Special cHVZK
> We say $\Pi$ is **special computational HVZK**, or **special cHVZK**, if there exists a simulator $Sim$ for $\Pi$, such that for every efficient adversary $\mathcal A$, the value $\text{cHVZKadv}[\mathcal A, \Pi, Sim]$ is negligible.

### Fiat-Shamir Transform

> [!algorithm] Fiat Shamir Transform
> Let $\Pi = (P, V)$ be a [[Identification Protocol#Sigma Protocols|Sigma protocol]] for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$. Assume that conversations $(t, c, z)$ for $\Pi$ belong to $\mathcal T \times \mathcal C \times \mathcal Z$. Let $H: \mathcal Y \times \mathcal T \rightarrow \mathcal C$ be a hash function. We define the Fiat-Shamir non-interactive proof system $\text{FS-}\Pi = (GenPrf, VrfyPrf)$, with proof space $\mathcal P \mathcal S = \mathcal T \times \mathcal Z$, as follows:
> - On input $(x, y)$ in $\mathcal R$, $GenPrf$ first runs $P(x, y)$ to obtain a commitment $t \in \mathcal T$; it then feeds the challenge $c = H(y, t)$ to $P(x, y)$, obtaining a response $z \in \mathcal Z$; the output is $(t, z) \in \mathcal T \times \mathcal Z$;
> - On input $(y, (t, z)) \in \mathcal Y \times (\mathcal T \times \mathcal Z)$, $VrfyPrf$ verifies that $(t, c, z)$ is an accepting conversation for $y$, where $c = H(y, t)$.

> [!theorem] Fiat-Shamir-Based Proofs are Sound
> Let $\Pi$ be a [[Identification Protocol#Sigma Protocols|Sigma protocol]] for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$, and let $\text{FS-}\Pi$ be the Fiat-Shamir non-interactive proof system derived from $\Pi$ with hash function $H$. If $\Pi$ is sound, and if we model $H$ as a random oracle, then $\text{FS-}\Pi$ is sound.
> 
> In particular, let $\mathcal A$ be a random oracle [[#Non-interactive Soundness|non-interactive soundness]] adversary attacking the soundness of FS-$\Pi$. Moreover, assume that $\mathcal A$ issues at most $Q_{ro}$ random oracle queries. Then there exists a [[#Soundness|soundness]] adversary $\mathcal B$ that attacks the soundness of $\Pi$, where $\mathcal B$ is an elementary wrapper around $\mathcal A$ such that $$\text{niSnd}^{ro}\text{adv}[\mathcal A, \text{FS-}\Pi] \leq (Q_{ro} + 1) \text{Sndadv}[\mathcal B, \Pi]$$

> [!theorem] Fiat-Shamir-Based Proofs are Zero Knowledge
> Let $\Pi = (P, V)$ be a special HVZK [[Identification Protocol#Sigma Protocols|Sigma protocol]] for a relation $\mathcal R \subseteq \mathcal X \times \mathcal Y$ with unpredictable commitments, and let $\text{FS-}\Pi$ be the Fiat-Shamir non-interactive proof system derived from $\Pi$ with hash function $H$. If we model $H$ as a random oracle, then $\text{FS-}\Pi$ is niZK.
> 
> In particular, there exists a [[#Simulator|simulator]] $Sim$ such that if $\mathcal A$ is a [[#Non-Interactive Zero Knowledge|non-interactive zero knowledge]] adversary that attacks $\text{FS-}\Pi$ and $Sim$, making at most $Q_p$ proof queries and at most $Q_{ro}$ random oracle queries, and if $\Pi$ has $\delta$-unpredictable commitments, then we have $$\text{niZKadv}[\mathcal A, \text{FS-}\Pi, Sim] \leq Q_p(Q_p + Q_{ro}) \cdot \delta.$$
