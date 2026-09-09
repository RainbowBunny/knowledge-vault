Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 1: The computational model —and why it doesn’t matter, Section 1.1.2: Decision problems / languages.
- [[Book Reference|Introduction to Automata Theory, Languages, and Computation]] - Chapter 1. Automata: The Methods and The Madness, Section 1.5.3: Languages; Section 1.5.4: Problems.

## Definition

> [!definition] Language
> For an alphabet $\Sigma$, a set of strings all of which are chosen from some $\Sigma^*$ is called a **language**.

### Defining Languages by Sets

> [!definition] Set-Formers as a Way to Define Languages
> It is common to describe a language using a "set-former":
> $$\{w \mid \text{something about } w\}$$

### Problem Formulated by Language

> [!definition] Problem
> Given $\Sigma$ is an alphabet, and $L$ is a language over $\Sigma$, then the problem $L$ is defined as:
> - Given $w \in \Sigma^*$, decide whether or not $w$ is in $L$.

> [!remark]
> Formulating problems by decision problems is a little bit counter-intuitive, however, if we can solve a problems, then its decision variant is easy to solve too, and thus, the decision problem will give a lower-bound on the difficulty.

## Property

### Recognizable

> [!definition] Recognizable
> A language $\mathcal{L}$ is recognizable (Turing-recognizable) if some [[Turing Machine]] recognizes it.

### Decidable

> [!definition] Decidable
> A language $\mathcal{L}$ is decidable (Turing-decidable) if some [[Turing Machine#Decider|Decider]] recognizes it.
