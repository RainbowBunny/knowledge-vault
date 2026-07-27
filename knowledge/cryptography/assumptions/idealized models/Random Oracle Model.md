## Basic Definition

> [!definition] Random Oracle Model
> Suppose we have some type of cryptographic scheme $\mathcal S$ whose implementation makes use of a subroutine for computing a hash function $H$ defined over $(\mathcal M, \mathcal T)$. The scheme $\mathcal S$ evaluates $H$ at arbitrary points of its choice, but does not look at the internal implementation of $H$. We say that $\mathcal S$ **uses $H$ as an oracle**.
> 
> If we wish to analyze $\mathcal S$ in the random oracle model, then the attack game defining security is modified so that $H$ is effectively replaced by a **random function** $\mathcal O \in \text{Funs}[\mathcal M, \mathcal T]$, to which both the adversary and the challenger have oracle access.

> [!scheme] Usage of the Random Oracle Model
> We wish to analyze the security of $\mathcal S$. Let us assume that whatever security property we are interested in property $X$ and an arbitrary adversary $\mathcal A$. This game defines an advantage $\text{Xadv}[\mathcal A, \mathcal S]$, and security with respect to property $X$ means that this advantage should be negligible for all efficient adversaries $\mathcal A$.
> 
> The attack game then is modified as follows.
> - At the beginning of the game, the challenger chooses $\mathcal O \in \text{Funs}[\mathcal M, \mathcal T]$ at random.
> - In addition to its standard queries, the adversary $\mathcal A$ may submit **random oracle queries**: it gives $m \in \mathcal M$ to the challenger, who responds with $t = \mathcal O(m)$. The adversary may make any number of random oracle queries, arbitrarily interleaved with standard queries.
> - In processing standard queries, the challenger performs its computations using $\mathcal O$ in place of $H$.
> 
> The adversary's advantage is defined using the same rule as before, but is denoted $\text{X}^{ro}\text{adv}[\mathcal A, \mathcal S]$ to emphasize that this is an advantage **in the random oracle model**. Security **in the random oracle model** means that $\text{X}^{ro}\text{adv}[\mathcal A, \mathcal S]$ should be negligible for all efficient adversaries $\mathcal A$.
