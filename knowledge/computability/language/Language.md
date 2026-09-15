Reference:
- [[Book Reference|Computational Complexity: A Modern Approach]] - Chapter 0: Notational conventions, Section 0.2: Decision Problems/Language.
- [[Book Reference|Introduction to Automata Theory, Languages, and Computation]] - Chapter 1. Automata: The Methods and The Madness, Section 1.5.3: Languages; Section 1.5.4: Problems.
- [[Book Reference|Introduction to the Theory of Computation]] - Chapter 1: Regular Languages, Section 1.1: Finite Automata.

## Definition

> [!definition] Language
> For an alphabet $\Sigma$, a set of strings all of which are chosen from some $\Sigma^*$ is called a **language**.

> [!definition] Regular Operation on Language
> As languages are sets, we can define:
> - **Union**: $A \cup B = \{x \mid x \in A \lor x \in B\}$.
> - **Concatenation**: $A \circ B = \{xy \mid x \in A \land y \in B\}$.
> - **Star**: $A^* = \{x_1 \dots x_k \mid k \geq 0 \land x_i \in A \; \forall \; i \in [k]\}$.

> [!definition] Completement Language
> If $\mathcal{L} \subseteq \{0, 1\}^*$ is a language, then we denote by $\overline{\mathcal{L}}$ the **completement** of $\mathcal{L}$. That is:
> $$\overline{\mathcal{L}} = \{0, 1\}^* \backslash \mathcal{L}$$

### Defining Languages by Sets

> [!definition] Set-Formers as a Way to Define Languages
> It is common to describe a language using a "set-former":
> $$\{w \mid \text{something about } w\}$$

### Problem Formulated by Language

> [!definition] Problem
> Given $\Sigma$ is an alphabet, and $L$ is a language over $\Sigma$, then the problem $L$ is defined as:
> - Given $w \in \Sigma^*$, decide whether or not $w$ is in $L$.

> [!definition] Decision Problem (Boolean Function Formulation)
> We say a machine decides a language $L \subset \{0, 1\}^*$ if it computes the function $f_L: \{0, 1\}^* \rightarrow \{0, 1\}$, where $f_L(x) = 1 \iff x \in L$. 

> [!remark]
> Formulating problems by decision problems is a little bit counter-intuitive, however, if we can solve a problems, then its decision variant is easy to solve too, and thus, the decision problem will give a lower-bound on the difficulty.

## Property

> [!remark]
> [[Regular Language]] $\subsetneq$ [[Context-Free Language]] $\subsetneq$ [[Decidable Language]] $\subsetneq$ [[Recognizable Language]].
