Reference:
- https://eprint.iacr.org/2004/331 (Bellare–Rogaway, code-based game-playing proofs)
- https://eprint.iacr.org/2004/332 (Shoup, sequences of games)
- https://toc.cryptobook.us/ (Boneh–Shoup, the notation used vault-wide)

## Definition

> [!definition] Security Game (Experiment)
> A **security game** for a scheme $\Pi$ is a probabilistic experiment between a **challenger**, who runs $\Pi$'s algorithms honestly, and an [[Adversary]] $\mathcal A$, who may behave arbitrarily within its class. The experiment ends in a bit, and definitions are stated as probabilities of that bit over the experiment's randomness.

> [!remark] House format
> Games are written as bracketed probability arrays: outcome condition on the left, experiment steps on the right, adversary phases named ($\mathcal A_\mathsf{find}, \mathcal A_\mathsf{guess}, \dots$). See [[Soundness]] or [[Zero Knowledge]] for the shape.

## Variant

### Search Game

> [!definition] Search Game
> $\mathcal A$ must *produce* something — a forgery, a collision, a false-statement proof. The **advantage** is
> $$\mathsf{Adv}(\mathcal A) = \Pr[\text{win}]$$
> (minus the trivial win probability, when guessing can win). Instances: [[Soundness]], [[Knowledge Soundness]], collision resistance in [[Special Functions]].

### Distinguishing Game

> [!definition] Distinguishing Game
> Two experiments $G_0, G_1$ differ in one component; $\mathcal A$ outputs a guess $b$. The **advantage** is
> $$\mathsf{Adv}(\mathcal A) = \left| \Pr[b = 1 \mid G_0] - \Pr[b = 1 \mid G_1] \right|$$
> Instances: [[Indistinguishability]], [[Zero Knowledge]] (real vs simulated), pseudorandomness in [[Special Functions]].

## Property — strength of a security bound

A **security notion** fixes a game, then demands the advantage be small for a class of adversaries. Three standard strengths:

| flavour           | adversary class | required bound                             |
| ----------------- | --------------- | ------------------------------------------ |
| **perfect**       | unbounded       | $\mathsf{Adv} = 0$                         |
| **statistical**   | unbounded       | $\mathsf{Adv} \leq \mathsf{negl}(\lambda)$ |
| **computational** | [[PPT]]         | $\mathsf{Adv} \leq \mathsf{negl}(\lambda)$ |

Every security definition in the vault is a game plus a row of this table. The same game changes name by row: perfect / statistical / computational [[Zero Knowledge]]; statistical [[Soundness]] gives *proofs*, computational gives *arguments* ([[Argument Systems]]); [[Perfect Security]] is the perfect row of the encryption distinguishing game.

> [!remark] The rows trade off
> Some pairs of notions cannot both sit in an unbounded row: a commitment scheme cannot be statistically hiding **and** statistically binding — an unbounded adversary breaks at least one. Choosing rows is a design decision, not bookkeeping.

## Related

- [[Elementary Wrapper]] — how a reduction turns an adversary for one game into an adversary for another
- Hybrid argument — advantages obey the triangle inequality across a chain of games ([[Indistinguishability]])