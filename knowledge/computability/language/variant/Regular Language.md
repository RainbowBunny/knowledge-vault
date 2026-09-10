Reference:
- [[Book Reference|Introduction to the Theory of Computation]] - Chapter 1: Regular Languages, Section 1.1: Finite Automata; Section 1.2: Nondeterminism; Section 1.4: Nonregular Languages.

## Definition

> [!definition] Regular Language
> A [[Language]] $\mathcal{L}$ is regular if some [[Deterministic Finite Automaton]] recognizes it.

> [!theorem]
> A language is regular if and only if some [[Regular Expression]] describes it.

## Property

> [!theorem]
> The class of regular languages is [[Closure|Closed]] under the union operation.
> 
> ---

> [!theorem]
> The class of regular languages is [[Closure|Closed]] under the concatenation operations.
> 
> ---

> [!theorem]
> The class of regular languages is [[Closure|Closed]] under the star operations.
> 
> ---

> [!theorem] Pumping Lemma
> If $A$ is a regular language, then there is a number $p$ (the pumping length) where if $s$ is any string in $A$ of **length at least** $p$, then $s$ may be divided into three pieces, $s = xyz$ such that: 
> 1. for each $i \ge 0$, $xy^{i}z \in A$,
> 2. $|y| > 0$, and
> 3. $|xy| \leq p$
>
> ---
> Idea: If $A$ is a regular language then there exist a DFA $M = (Q, \Sigma, \delta, q_0, F)$ of $A$ and we can choose $p = |Q| + 1$ so there exist a cycle in the traversal path of $s$ (this is $y$ and $|xy| \leq p$ means that we go through the cycle in the first $|Q| + 1$ vertexes).
