## Soundness

> [!algorithm] Soundness
> Let $\Pi = (P, V)$ be a [[Sigma Protocols|Sigma protocol]] for $\mathcal R \subseteq \mathcal X \times \mathcal Y$. For a given adversary $\mathcal A$, the attack game runs as follows:
> - The adversary chooses a statement $y^* \in \mathcal Y$ and gives this to the challenger.
> - The adversary now interacts with the verifier $V(y^*)$, where the challenger plays the role of verifier and the adversary plays the role of a possibly "cheating" prover.
> 
> We say that the adversary wins the game if $V(y^*)$ outputs $\text{accept}$ but $y^* \notin L_{\mathcal R}$. We define $\mathcal A$'s advantage with respect to $\Pi$, denoted $\text{Sndadv}[\mathcal A, \Pi]$, as the probability that $\mathcal A$ wins the game.

> [!definition] Sound
> We say that $\Pi$ is **sound** if for all efficient adversaries $\mathcal A$, the quantity $\text{Sndadv}[\mathcal A, \Pi]$ is negligible.

> [!theorem] Special Soundness implies Soundness
> Let $\Pi$ be a [[Sigma Protocols|Sigma protocol]] with a large challenge space. If $\Pi$ provides special soundness, then $\Pi$ is sound.
> 
> In particular, for every adversary $\mathcal A$, we have $$\text{Sndadv}[\mathcal A, \Pi] \leq \frac{1}{N},$$ where $N$ is the size of the challenge space.

## Special Computational HVZK

A simulator for an interactive Σ-protocol is a (different) PPT machine $\text{Sim}$ that, on input a statement $y$ and challenge $c$, outputs a transcript $(t, z)$.

> [!algorithm] Special cHVZK
> Let $\Pi = (P, V)$ be a [[Sigma Protocols|Sigma protocol]] for $\mathcal R \subseteq \mathcal X \times \mathcal Y$, with challenge space $\mathcal C$. Let $Sim$ be a simulator for $\Pi$. For a given adversary $\mathcal A$, we define two experiments, Experiment 0 and Experiment 1. In both experiments, $\mathcal A$ starts out by computing $(x, y) \in \mathcal R$ and submitting $(x, y)$ to the challenger.
> - In Experiment 0, the challenger runs the protocol between $P(x, y)$ and $V(y)$, and gives the resulting conversation $(t, c, z)$ to $\mathcal A$.
> - In Experiment 1, the challenger computes $$c \xleftarrow{R}, (t, z) \xleftarrow{R} Sim(y, c),$$ and gives the simulated conversation $(t, c, z)$ to $\mathcal A$.
> 
> At the end of the game, $\mathcal A$ computes and outputs a bit $\hat{b} \in \{0, 1\}$.
> For $b = 0, 1$, let $W_b$ be the event that $\mathcal A$ outputs 1 in Experiment $b$. We define $\mathcal A$'s **advantage** with respect to $\Pi$ and $Sim$ as $$\text{cHVZKadv}[\mathcal A, \Pi, Sim] = |P[W_0] - P[W_1]|.$$

> [!definition] Special cHVZK
> We say $\Pi$ is **special computational HVZK**, or **special cHVZK**, if there exists a simulator $Sim$ for $\Pi$, such that for every efficient adversary $\mathcal A$, the value $\text{cHVZKadv}[\mathcal A, \Pi, Sim]$ is negligible.
