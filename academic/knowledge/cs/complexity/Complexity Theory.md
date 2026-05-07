_What makes some problems computationally hard and others easy?_
Complexity is based on input sizes.

## Reductions

> [!definition] Reduce
> Problem $A$ **reduces** to Problem $B$, written $A \leq B$, if one can efficiently solve $A$ (with non-negligible probability), given an algorithm that efficiently solves $B$ (with non-negligible probability).

## Class NP

A **verifier** for a language $A$ is an algorithm $V$, where $$A = \{w | V \text{ accepts } \langle w, c \rangle \text{ for some string } c\}.$$
We measure the time of a verifier only in terms of the length of $w$, so a **polynomial time verifier** runs in polynomial time in the length of $w$. A language $A$ is **polynomial verifiable** if it has a polynomial time verifier.

To test the membership in $A$, the verifier uses an additional information $c$ called a **certificate**, or **proof**.

**Theorem**: A language is in $\text{NP}$ if and only if it is decided by some nondeterministic polynomial time Turing machine.

$\text{NP} = \cup_k \text{NTIME}(n^k)$. 

**Member of** $\text{NP}$:
[[Number Theory#Prime Numbers, Unique Factorization, and Finite Fields|COMPOSITES]]

Observation: $$\text{NP} \subseteq \text{EXPTIME} = \cup_k \text{TIME}(2^{n^k})$$
Separate complexity class: Complements of language in NP.
> [!question] 
> Does $\text{coNP} = \text{NP}$? Does $\text{P} = \text{NP}$?


## Class PSPACE

> [!definition] Class PSPACE 
> **PSPACE** is the class of languages that are decidable in polynomial space on a deterministic Turing machine. In other words, $$\text{PSPACE} = \cup_k \text{SPACE}(n^k).$$

## NP-Complete

> [!definition] NP-complete
> A language $B$ is **NP-complete** if it satisfies two conditions:
> 1. $B$ is in $\text{NP}$, and
> 2. every $A$ in $\text{NP}$ is polynomial time reducible to $B$.
> 
> If $B$ merely satisfies condition 2, we say that it is $\text{NP}$-hard

> [!theorem] 
> If $B$ is **NP-complete** and $B \in \text{P}$, then $\text{P} = \text{NP}$ 

> [!definition] Polynomial time computable function
> A function $f: \Sigma^{*} \rightarrow \Sigma^{*}$ is a **polynomial time computable function** if some polynomial time Turing machine $M$ exists that halts with just $f(w)$ on its tape, when started on any input $w$.

> [!definition] Polynomial time reduction
Language $A$ is **polynomial time mapping reducible**, or simply **polynomial time reducible**, to language $B$, written $A \leq_\text{P} B$, if a polynomial time computable function $f: \Sigma^* \rightarrow \Sigma^*$ exists, where for every $w$, $$w \in A \Longleftrightarrow f(w) \in B.$$
The function $f$ is called the **polynomial time reduction** of $A$ to $B$.

> [!theorem] 
> If $A \leq_\text{P} B$ and $B \in \text{P}$, then $A \in \text{P}$.

> [!theorem] Cook-Levin Theorem
 [[Satisfiability Problem|SAT]] is **NP-complete** (revisit the prove).

**Member of NP-Complete**:
$\text{CLIQUE} = \{\langle G, k \rangle | G \text{ is an undirected graph with a } k \text{-clique}\}.$
$\text{VERTEX-COVER} = \{\langle G, k \rangle | G \text{ is an undirected graph that has a } k\text{-node vertex cover}\}$  
$\text{HAMPATH} = \{\langle G, s, t \rangle | G \text{ is a directed graph with a Hamiltonian path from } s \text{ to } t\}.$
$\text{UHAMPATH} = \{\langle G, s, t \rangle | G \text{ is a undirected graph with a Hamiltonian path from } s \text{ to } t\}.$
[[Subset-Sum Problem|SUBSET-SUM]]

## PSPACE-Completeness

> [!definition] PSPACE-complete
 A language $B$ is **PSPACE-complete** if it satisfies two conditions:
> 1. $B$ is in $\text{PSPACE}$, and
> 2. every $A$ in $\text{PSPACE}$ is polynomial time reducible to $B$.
>
> If $B$ merely satisfies condition 2, we say that it is $\text{PSPACE-hard}$.

> [!theorem] 
> [[Satisfiability Problem|TQBF]] is $\text{PSPACE}$-complete.


**Member of NP-Complete**: 
**Formula game**: Player $\text{A}$ selects values for variable with $\forall$ quantifiers, player $\text{E}$ selects values for variable with $\exists$ quantifiers.
$\text{FORMULA-GAME} = \{\langle \phi \rangle | \text{Player E has a winning strategy in the formula game associated with } \phi\}.$
**Generalized geography**: Match last character of a city with the first character of the next city.
$\text{GG} =\{\langle G, b \rangle | \text{Player I has a winning strategy for the generalized geography game played on graph } G \text{ starting at node } b\}$

## Classes L and NL

When consider these classes, we consider two tape:
- A read-only input tape.
- A read/write work tape (measure this).

> [!definition] Class L
 $\text{L}$ is the class of languages that are decidable in logarithmic space on a deterministic Turing machine: $\text{L} = \text{SPACE}(log\; n)$.

> [!definition] Class NL
$\text{NL}$ is the class of languages that are decidable in logarithmic space on a nondeterministic Turing machine: $\text{NL} = \text{NSPACE}(log\;n)$.

$\text{NL} = \text{coNL}$.

>[!definition] Configuration of Turing machine with a read-only input tape
> If $M$ is a Turing machine that has a separate read-only input tape and $w$ is an input, a **configuration of $M$ on $w$** is a setting of the state, the work tape, and the positions of the two tape heads. The input $w$ is not a part of the configuration of $M$ on $w$ (because $w$ is constant).

## NL-completeness

> [!definition] Class NL-complete
> A language $B$ is $\text{NL}$-complete if
> 1. $B \in \text{NL}$, and
> 2. every $A$ in $\text{NL}$ is log space reducible to $B$.
