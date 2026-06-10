# Space Complexity

The other canonical resource bound: how many tape cells does a Turing machine read?

## Space Complexity

> [!definition] Deterministic Space Complexity
> Let $M$ be a deterministic Turing machine that halts on all inputs. The **space complexity** of $M$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the maximum number of tape cells that $M$ scans on any input of length $n$.

> [!definition] Nondeterministic Space Complexity
> If $N$ is a nondeterministic Turing machine wherein all branches halt on all inputs, we define its space complexity $f(n)$ to be the maximum number of tape cells that $N$ scans on any branch of its computation for any input of length $n$.

> [!definition] Space Complexity Class
> Let $f: \mathcal N \rightarrow \mathcal R^{+}$ be a function:
> $$\text{SPACE}(f(n)) = \{L \mid L \text{ is a language decided by an } O(f(n))\text{-space deterministic Turing machine}\}.$$
> $$\text{NSPACE}(f(n)) = \{L \mid L \text{ is a language decided by an } O(f(n))\text{-space nondeterministic Turing machine}\}.$$

## Savitch's Theorem

> [!theorem] Savitch's Theorem
> For any function $f: \mathcal N \rightarrow \mathcal R^{+}$ with $f(n) \geq n$, $$\text{NSPACE}(f(n)) \subseteq \text{SPACE}(f^2(n)).$$

This gives $\text{PSPACE} = \text{NPSPACE}$ as a corollary — a dramatic difference from the time setting, where $\text{P} = \text{NP}$ is famously open.

## Class PSPACE

> [!definition] Class PSPACE
> **PSPACE** is the class of languages that are decidable in polynomial space on a deterministic Turing machine: $$\text{PSPACE} = \bigcup_k \text{SPACE}(n^k).$$
> These problems might not be computationally easy to solve or verify but only require a limited space to verify.

## Class PSPACE-Complete

> [!definition] Class PSPACE-Complete
> A language $B$ is **PSPACE-complete** if it satisfies two conditions:
> 1. $B$ is in $\text{PSPACE}$, and
> 2. every $A$ in $\text{PSPACE}$ is polynomial-time reducible to $B$.
>
> If $B$ merely satisfies condition 2, we say that it is **PSPACE-hard**.

> [!theorem]
> [[Satisfiability Problem|TQBF]] is PSPACE-complete.

> [!example] Members of PSPACE-Complete
> **Formula game**: Player $\text{A}$ selects values for variables with $\forall$ quantifiers, player $\text{E}$ selects values for variables with $\exists$ quantifiers.
> $\text{FORMULA-GAME} = \{\langle \phi \rangle \mid \text{Player E has a winning strategy in the formula game associated with } \phi\}.$
>
> **Generalized geography**: Match the last character of a city with the first character of the next city.
> $\text{GG} = \{\langle G, b \rangle \mid \text{Player I has a winning strategy for the generalized geography game played on graph } G \text{ starting at node } b\}.$

## Classes L and NL

> [!remark]
> When considering these classes, we consider two tapes:
> - A read-only input tape.
> - A read/write work tape (whose space we measure).

> [!definition] Class L
> $\text{L}$ is the class of languages that are decidable in logarithmic space on a deterministic Turing machine: $\text{L} = \text{SPACE}(\log n)$.

> [!definition] Class NL
> $\text{NL}$ is the class of languages that are decidable in logarithmic space on a nondeterministic Turing machine: $\text{NL} = \text{NSPACE}(\log n)$.

> [!theorem] Immerman-Szelepcsényi
> $\text{NL} = \text{coNL}$.

> [!definition] Configuration of a Turing Machine with a Read-Only Input Tape
> If $M$ is a Turing machine that has a separate read-only input tape and $w$ is an input, a **configuration of $M$ on $w$** is a setting of the state, the work tape, and the positions of the two tape heads. The input $w$ is not a part of the configuration of $M$ on $w$ (because $w$ is constant).

## Class NL-completeness

> [!definition] Class NL-Complete
> A language $B$ is **NL-complete** if
> 1. $B \in \text{NL}$, and
> 2. every $A$ in $\text{NL}$ is [[Reductions#Log-Space Reductions|log-space reducible]] to $B$.

## Related

- [[Time Complexity]] — the other canonical resource bound
- [[Reductions]] — log-space reductions used for NL-completeness
- [[Hierarchy Theorems]] — strict separations $\text{L} \subset \text{PSPACE} \subset \text{EXPSPACE}$
- [[Interactive Proofs]] — $\text{IP} = \text{PSPACE}$ (Shamir's theorem)
- [[Complexity Class#Class Inclusions|Class inclusions]] — the full lattice
