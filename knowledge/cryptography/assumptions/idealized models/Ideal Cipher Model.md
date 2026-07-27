## The Ideal Cipher Model

### Ideal Block Model

> [!algorithm] Ideal Block Model
> Suppose we have some type of cryptographic scheme $\mathcal S$ whose implementation makes use of a block cipher $\mathcal E = (E, D)$ defined over $(\mathcal K, \mathcal X)$. Moreover, suppose the scheme $\mathcal S$ evaluates $E$ at various inputs $(k, a) \in \mathcal K \times \mathcal X$, and $D$ at various inputs $(k, b) \in \mathcal K \times \mathcal X$, but does not look at the internal implementation of $\mathcal E$. In this case, we say that $\mathcal S$ **uses $\mathcal E$ as an oracle**.
> 
> To analyze $\mathcal S$ in the ideal cipher model, then the attack game defining security is modified so that $\mathcal E$ is effectively replaced by a family of random permutations $\{\Pi_{k}\}_{k \in \mathcal K}$ to which both the adversary and the challenger have oracle access. The game is modified as follows:
> - At the beginning of the game, the challenger chooses $\Pi_k \in \text{Perms}[\mathcal K]$ at random, for each $k \in \mathcal K$.
> - In addition to its standard queries, the adversary $\mathcal A$ may submit **ideal cipher queries**. There are two types of queries: $\Pi$-queries and $\Pi^{-1}$-queries.
> 	- For a $\Pi$-query, the adversary submits a pair $(k, a) \in \mathcal K \times \mathcal X$, to which the challenger responds with $\Pi_k(a)$.
> 	- For a $\Pi^{-1}$-query, the adversary submits a pair $(k, b) \in \mathcal K \times \mathcal X$, to which the challenger responds with $\Pi^{-1}_k(b)$.
> 
> The adversary may make any number of ideal cipher queries, arbitrarily interleaved with standard queries.
> - In processing standard queries, the challenger performs its computations using $\Pi_k(a)$ in place of $E(k, a)$ and $\Pi^{-1}_k(b)$ in place of $D(k, b)$.
> 
> The adversary's advantage is defined using the same rule as before, but is denoted $\text{X}^{ic}\text{adv}[\mathcal A, \mathcal S]$. Security in the ideal cipher model means that $\text{X}^{ic}\text{adv}[\mathcal A, \mathcal S]$ should be negligible for all efficient adversaries $\mathcal A$.

### Ideal Permutation Model

> [!algorithm] Ideal Permutation Model
> Some constructions, make use of a permutation $\pi: \mathcal X \rightarrow \mathcal X$, rather than a block cipher.

### List Guessing Advantage

> [!algorithm] List Guessing Advantage
> Generalize of [[#Key Derivation Problem|guessing advantage]] problem by output a list of guesses $\hat{s}_1, \dots, \hat{s}_Q$, where the adversary is said to win the game if $\hat{s}_i = s$ for some $i = 1, \dots, Q$. An adversary $\mathcal A$'s probability of winning in this game is called his **list guessing advantage**, denoted $\text{ListGuessadv}[\mathcal A, P, I]$.

> [!theorem]
> If $H$ is modeled as a random oracle, then for every distinguishing adversary $\mathcal A$ that makes at most $Q_{ro}$ random oracle queries, there exists a list guessing adversary $\mathcal B$, which is an elementary wrapper around $\mathcal A$, such that $$\text{Dist}^{ro}\text{adv}[\mathcal A, P, I, H] \leq \text{ListGuessadv}[\mathcal B, P, I]$$ and $\mathcal B$ outputs a list of size at most $Q_{ro}$. In particular, there exists a guessing adversary $\mathcal B'$, which is an elementary wrapper around $\mathcal A$, such that $$\text{Dist}^{ro}\text{adv}[\mathcal A, P, I, H] \leq Q_{ro} \cdot \text{Guessadv}[\mathcal B', P, I].$$
 
