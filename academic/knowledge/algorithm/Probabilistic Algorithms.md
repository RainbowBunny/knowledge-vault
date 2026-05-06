
## Probabilistic Turing machine

> [!definition] Probabilistic Turing Machine
> A **probabilistic Turing machine** $M$ is a type of nondeterministic Turing machine in which each nondeterministic step is called a **coin-flip step** and has two legal next moves. We assign a probability to each branch $b$ of $M$'s computation on input $w$ as follows. Define the probability of branch $b$ to be $$\Pr[b] = 2^{-k},$$
where $k$ is the number of coin-flip steps that occur on branch $b$. Define the probability that $M$ accepts $w$ to be $$\Pr[M \text{ accepts } w] = \sum_{b \text{ is an accepting branch}} \Pr[b].$$

> [!definition] Decidable with error
> $M$ **decides language $A$ with error probability $\epsilon$** if
>1. $w \in A$ implies $\Pr[M \text{ accepts } w] \geq 1 - \epsilon$, and
>2. $w \notin A$ implies $\Pr[M \text{ rejects } w] \geq 1 - \epsilon.$

## Class BPP

> [!definition] Class BPP
$\text{BPP}$ is the class of languages that are decided by probabilistic polynomial time Turing machines with an error probability of $\frac{1}{3}$.

> [!lemma]
 Let $\epsilon$ be a fixed constant strictly between $0$ and $\frac{1}{2}$. Then for any polynomial $p(n)$, a probabilistic polynomial time Turing machine $M_1$ that operates with error probability $\epsilon$ has an equivalent probabilistic polynomial time Turing machine $M_2$ that operates with an error probability of $2^{-p(n)}$.

**Member of $\text{BPP}$:** 
$EQ_{ROBP} = \{\langle B_1, B_2 \rangle | B_1 \text{ and } B_2 \text{ are equivalent read-once branching program}\}.$

## Class RP

> [!definition] Class RP
 $\text{RP}$ is the class of languages that are decided by probabilistic polynomial time Turing machines where inputs in the language are accepted with a probability of at least $\frac{1}{2}$, and inputs not in the language are rejected with a probability of $1$.

## Monte Carlo algorithms

> [!definition] Monte Carlo Algorithm
> A **Monte Carlo** algorithm for property $A$ takes as its input both a number $m \in S$ to be tested and a randomly chosen number $r$ and returns as output either `Yes` or `No` according to the following rules:
> 1. If the algorithm returns `Yes`, then $m$ definitely has property $A$: $$\Pr(m \text{ has property } A \mid \text{ algorithm returns Yes}) = 1.$$
> 2. If $m$ has property $A$, then the algorithm returns `YES` for at least $50\%$ of the choices for $r$: $$\Pr(\text{algorithm returns Yes} \mid m \text{ has property } A) \geq \frac{1}{2}.$$

