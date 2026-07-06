# Randomized Complexity

What changes when the Turing machine has access to fair coin flips? Randomized complexity sits at the same conceptual level as time and space — a peer resource bound, not an "advanced topic."

## Probabilistic Turing Machine

> [!definition] Probabilistic Turing Machine
> A **probabilistic Turing machine** $M$ is a type of nondeterministic Turing machine in which each nondeterministic step is called a **coin-flip step** and has two legal next moves. We assign a probability to each branch $b$ of $M$'s computation on input $w$ as follows. Define the probability of branch $b$ to be $$\Pr[b] = 2^{-k},$$
> where $k$ is the number of coin-flip steps that occur on branch $b$. Define the probability that $M$ accepts $w$ to be $$\Pr[M \text{ accepts } w] = \sum_{b \text{ is an accepting branch}} \Pr[b].$$

> [!definition] Decidable with Error
> $M$ **decides language $A$ with error probability $\epsilon$** if
> 1. $w \in A$ implies $\Pr[M \text{ accepts } w] \geq 1 - \epsilon$, and
> 2. $w \notin A$ implies $\Pr[M \text{ rejects } w] \geq 1 - \epsilon.$

## Probabilistic Polynomial Time (PPT)

Reference: [[Book Reference#Foundation of Cryptography Volume I Basic Tools|Foundation of Cryptography Volume I Basic Tools]]

> [!definition] Probabilistic Polynomial Time (PPT)
> A **PPT Turing machine** is a probabilistic Turing machine $M$ for which there exists a polynomial $p$ such that, for every input $w$ of length $n$, every branch of $M$'s computation on $w$ halts within $p(n)$ steps.
>
> A **PPT algorithm** is one computable by such a machine. Equivalently: a probabilistic algorithm whose worst-case running time (over all coin tosses, all branches) is polynomial in the input length.

> [!remark]
> PPT is the formal meaning of "efficient randomized algorithm." Every "PPT adversary" in a cryptographic security definition is just a PPT machine quantified over inputs. This is the underlying class beneath BPP, RP, and ZPP — those are PPT machines with various conditions on error probability.

## Class BPP

Reference: [[Book Reference#Foundation of Cryptography Volume I Basic Tools|Foundation of Cryptography Volume I Basic Tools]]

> [!definition] Class BPP
> $\text{BPP}$ is the class of languages decided by probabilistic polynomial-time Turing machines with an error probability of $\frac{1}{3}$. 
> Unfolded (language form): $L \in \text{BPP}$ iff there is a PPT machine $M$ such that
> 1. $w \in L$ implies $\Pr[M \text{ accepts } w] \geq \frac{2}{3}$, and
> 2. $w \notin L$ implies $\Pr[M \text{ accepts } w] \leq \frac{1}{3}$.
>
> By the amplification lemma below, the constant $\frac{1}{3}$ can be replaced by any $\epsilon \in (0, \frac 1 2)$ or even $2^{-p(n)}$ without changing the class.

> [!lemma] Amplification
> Let $\epsilon$ be a fixed constant strictly between $0$ and $\frac{1}{2}$. Then for any polynomial $p(n)$, a probabilistic polynomial-time Turing machine $M_1$ that operates with error probability $\epsilon$ has an equivalent probabilistic polynomial-time Turing machine $M_2$ that operates with an error probability of $2^{-p(n)}$.

> [!example] Member of BPP
> $EQ_{ROBP} = \{\langle B_1, B_2 \rangle \mid B_1 \text{ and } B_2 \text{ are equivalent read-once branching programs}\}$

## Class RP

> [!definition] Class RP
> $\text{RP}$ is the class of languages decided by probabilistic polynomial-time Turing machines where inputs in the language are accepted with probability at least $\frac{1}{2}$, and inputs not in the language are rejected with probability $1$. Unfolded (language form): $L \in \text{RP}$ iff there is a PPT machine $M$ such that
> 1. $w \in L$ implies $\Pr[M \text{ accepts } w] \geq \frac{1}{2}$, and
> 2. $w \notin L$ implies $\Pr[M \text{ accepts } w] = 0$.

RP is one-sided: false negatives possible (up to probability $\frac{1}{2}$), false positives impossible.

## Class ZPP

> [!definition] Class ZPP
> $\text{ZPP} = \text{RP} \cap \text{coRP}$ — languages decidable by a PPT machine that *never errs* but may "give up" (output "don't know") with probability up to $\frac{1}{2}$. Equivalently, decidable in expected polynomial time with zero error.

Las Vegas algorithms run in this class.

## Monte Carlo Algorithms

> [!definition] Monte Carlo Algorithm
> A **Monte Carlo** algorithm for property $A$ takes as input both a number $m \in S$ to be tested and a randomly chosen number $r$, and returns either `Yes` or `No` according to:
> 1. If the algorithm returns `Yes`, then $m$ definitely has property $A$: $\Pr[m \text{ has property } A \mid \text{algorithm returns Yes}] = 1.$
> 2. If $m$ has property $A$, then the algorithm returns `Yes` for at least $50\%$ of the choices for $r$: $\Pr[\text{algorithm returns Yes} \mid m \text{ has property } A] \geq \frac{1}{2}.$

The classic Monte Carlo / Las Vegas distinction:
- **Monte Carlo**: bounded running time, bounded error probability.
- **Las Vegas**: bounded expected running time, zero error.

ZPP is the class of decision problems with Las Vegas algorithms.

## Class Relationships

$$\text{P} \subseteq \text{ZPP} \subseteq \text{RP} \subseteq \text{BPP} \subseteq \text{PSPACE}.$$

Whether $\text{P} = \text{BPP}$ is the *derandomization conjecture* — widely believed but unproven. See [[Derandomization Conjecture]].

## Related

- [[Time Complexity]] / [[Space Complexity]] — deterministic resource bounds
- [[Interactive Proofs]] — IP uses probabilistic verification
- [[Circuit Complexity]] — non-uniform analog (polynomial-size circuits can simulate BPP)
- [[Derandomization Conjecture]] — P vs BPP
- The PPT definition above is what every cryptography security definition references with "PPT adversary"
