# Time Complexity

The canonical resource bound: how many steps does a Turing machine take?

## Time Complexity

> [!definition] Deterministic Time Complexity
> Let $M$ be a deterministic Turing machine that halts on all inputs. The **running time** or **time complexity** of $M$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the maximum number of steps that $M$ uses on any input of length $n$. If $f(n)$ is the running time of $M$, we say that $M$ runs in time $f(n)$ and that $M$ is an $f(n)$-time Turing machine. Customarily, we use $n$ to represent the length of the input.

> [!definition] Nondeterministic Time Complexity
> Let $N$ be a nondeterministic Turing machine that is a decider. The **running time** of $N$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the maximum number of steps that $N$ uses on any branch of its computation on any input of length $n$.

> [!definition] Time Complexity Class
> Let $t: \mathcal N \rightarrow \mathcal R^{+}$ be a function:
> $$\text{TIME}(t(n)) = \{L \mid L \text{ is a language decided by an } O(t(n))\text{-time deterministic Turing machine}\}.$$
> $$\text{NTIME}(t(n)) = \{L \mid L \text{ is a language decided by an } O(t(n))\text{-time nondeterministic Turing machine}\}.$$

## Class P

> [!definition] Class P
> $\text{P}$ is the class of languages that are decidable in polynomial time on a deterministic single-tape Turing machine: $$\text{P} = \bigcup_{k} \text{TIME}(n^k).$$
> Unfolded (machine form): $L \in \text{P}$ iff there exist a deterministic Turing machine $M$ and a polynomial $p(\cdot)$ such that
> - On input a string $x$, machine $M$ halts after at most $p(|x|)$ steps, and
> - $M(x) = 1$ if and only if $x \in L$.

> [!remark] Role of Class P
> 1. $\text{P}$ is invariant for all models of computation that are polynomial-equivalent to the deterministic single-tape Turing machine.
> 2. $\text{P}$ roughly corresponds to the class of problems that are realistically solvable on a computer.

> [!theorem]
> If $A \leq_\text{P} B$ and $B \in \text{P}$, then $A \in \text{P}$.

> [!example] Members of P
> - $\text{PATH} = \{\langle G, s, t \rangle \mid G \text{ is a directed graph with a directed path from } s \text{ to } t\}$
> - $\text{CONNECTED} = \{\langle G \rangle \mid G \text{ is a connected undirected graph}\}$
> - $\text{TRIANGLE} = \{\langle G \rangle \mid G \text{ contains a triangle}\}$
> - [[Number Theory#Divisibility and greatest common divisors|RELPRIME]]
> - Every context-free language

## Class Non-Uniform Polynomial

Reference: [[Book Reference#Foundation of Cryptography Volume I Basic Tools|Foundation of Cryptography Volume I Basic Tools]]

> [!definition] P/poly
> The complexity class non-uniform polynomial time (denoted $\text{P/poly}$) is the class of languages $L$ that can be recognized by a non-uniform sequence of polynomial time "machines". Namely, $L \in \text{P/poly}$ if there exists an infinite sequence of machines $M_1, M_2, \dots$ satisfying the following:
> 1. There exists a polynomial $p(\cdot)$ such that for every $n$, the description of machine $M_n$ has length bounded above by $p(n)$.
> 2. There exists a polynomial $q(\cdot)$ such that for every $n$, the running time of machine $M_n$ on each input of length $n$ is bounded above by $q(n)$.
> 3. For every $n$ and every $x \in \{0, 1\}^n$, machine $M_n$ will accept $x$ if and only if $x \in L$.

> [!theorem]
> $\text{BPP} \subseteq \text{P/poly}$

## Class NP

> [!definition] Verifier
> A **verifier** for a language $A$ is an algorithm $V$, where $$A = \{w \mid V \text{ accepts } \langle w, c \rangle \text{ for some string } c\}.$$
> We measure the time of a verifier only in terms of the length of $w$, so a **polynomial-time verifier** runs in polynomial time in the length of $w$. A language $A$ is **polynomial verifiable** if it has a polynomial-time verifier.

> [!definition] Certificate
> To test membership in $A$, the verifier uses additional information $c$ called a **certificate**, **witness**, or **proof** — a string whose existence proves $w \in A$ and which the verifier can check in polynomial time.

> [!definition] Class NP
> $\text{NP}$ is the class of languages that have polynomial-time verifiers.
> Unfolded (machine form): $L \in \text{NP}$ if there exists a Boolean relation $R_L \subseteq \{0, 1\}^* \times \{0, 1\}^*$ and a polynomial $p(\cdot)$ such that $R_L$ can be recognized in (deterministic) polynomial time, and $x \in L$ if and only if there exists a $y$ such that $|w| \leq p(|x|)$ and $(x, w) \in R_L$. Such $w$ is called a **witness for membership** of $x \in L$.

> [!theorem]
> A language is in $\text{NP}$ if and only if it is decided by some nondeterministic polynomial-time Turing machine: $$\text{NP} = \bigcup_k \text{NTIME}(n^k).$$

> [!example] Member of NP
> - [[Number Theory#Prime Numbers, Unique Factorization, and Finite Fields|COMPOSITES]]

> [!definition] Class coNP
> $\text{coNP} = \{L \mid \overline{L} \in \text{NP}\}$ — languages whose *non*-membership has polynomial-time-verifiable certificates (see [[Complexity Class#Complexity Class|complement classes]]). E.g. $\text{TAUTOLOGY} = \{\langle \phi \rangle \mid \phi \text{ is true under every assignment}\}$.

> [!question]
> Does $\text{coNP} = \text{NP}$? Does $\text{P} = \text{NP}$? See [[P vs NP]].

## Class NP-Complete

> [!definition] Class NP-Complete
> A language $B$ is **NP-complete** if it satisfies two conditions:
> 1. $B$ is in $\text{NP}$, and
> 2. every $A$ in $\text{NP}$ is polynomial-time reducible to $B$.
>
> If $B$ merely satisfies condition 2, we say that it is **NP-hard**.

> [!theorem]
> If $B$ is NP-complete and $B \in \text{P}$, then $\text{P} = \text{NP}$.

> [!theorem] Cook-Levin Theorem
> [[Satisfiability Problem|SAT]] is NP-complete.

> [!example] Members of NP-Complete
> - $\text{CLIQUE} = \{\langle G, k \rangle \mid G \text{ is an undirected graph with a } k\text{-clique}\}$
> - $\text{VERTEX-COVER} = \{\langle G, k \rangle \mid G \text{ is an undirected graph with a } k\text{-node vertex cover}\}$
> - $\text{HAMPATH} = \{\langle G, s, t \rangle \mid G \text{ is a directed graph with a Hamiltonian path from } s \text{ to } t\}$
> - $\text{UHAMPATH} = \{\langle G, s, t \rangle \mid G \text{ is an undirected graph with a Hamiltonian path from } s \text{ to } t\}$
> - [[Subset-Sum Problem|SUBSET-SUM]]

## Class EXPTIME

> [!proposition] Observation
> $$\text{NP} \subseteq \text{EXPTIME} = \bigcup_k \text{TIME}(2^{n^k}).$$

The strict separation $\text{P} \subset \text{EXPTIME}$ follows from the [[Hierarchy Theorems#Time Hierarchy|time hierarchy theorem]].

## Sub-Exponential

> [!definition] Sub-Exponential
> A function $f(x)$ is **sub-exponential** if:
> 1. $f(x) = \Omega((\ln x)^\alpha)$ for some $\alpha > 0$.
> 2. $f(x) = \mathcal O(x^\beta)$ for every $\beta > 0$.

Sub-exponential functions sit strictly between polynomial and exponential. Used in cryptography (e.g., $L_n[1/3, c]$ notation for the [[Index Calculus|index-calculus]] running time).

## Related

- [[Space Complexity]] — the other canonical resource bound
- [[Reductions]] — how NP-completeness is defined
- [[Hierarchy Theorems]] — why P $\subset$ EXPTIME
- [[Randomized Complexity]] — what changes with random coins
- [[P vs NP]] — the famous open problem
