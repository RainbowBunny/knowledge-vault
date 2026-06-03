
## Efficient Algorithm

> [!definition] Efficient Algorithm
> Let $A$ be an algorithm (possibly probabilistic) that takes as input a security parameter $\lambda \in \mathbb Z_{\geq 1}$, as well as other parameters encoded as a bit string $x \in \{0, 1\}^{p(\lambda)}$ for some fixed polynomial $p$. We call $A$ an **efficient algorithm** if there exist a poly-bounded function $t$ and a negligible function $\epsilon$ such that for all $\lambda \in \mathbb Z_{\geq 1}$, and all $x \in \{0, 1\}^{\leq p(\lambda)}$, the probability that the running time of $A$ on input $(\lambda, x)$ exceeds $t(\lambda)$ is at most $\epsilon(\lambda)$.

> [!definition] Polynomial time computable function
> A function $f: \Sigma^{*} \rightarrow \Sigma^{*}$ is a **polynomial time computable function** if some polynomial time Turing machine $M$ exists that halts with just $f(w)$ on its tape, when started on any input $w$.

## Complexity Relationships Among Models

> [!theorem]
Let $t(n)$ be a function, where $t(n) \geq n$. Then every $t(n)$ time multitape Turing machine has an equivalent $O(t^2(n))$ time single-tape Turing machine.

> [!definition] Reduce
> Problem $A$ **reduces** to Problem $B$, written $A \leq B$, if one can efficiently solve $A$ (with non-negligible probability), given an algorithm that efficiently solves $B$ (with non-negligible probability).

> [!definition] Polynomial time reduction
Language $A$ is **polynomial time mapping reducible**, or simply **polynomial time reducible**, to language $B$, written $A \leq_\text{P} B$, if a polynomial time computable function $f: \Sigma^* \rightarrow \Sigma^*$ exists, where for every $w$, $$w \in A \Longleftrightarrow f(w) \in B.$$
The function $f$ is called the **polynomial time reduction** of $A$ to $B$.

## Time Complexity

> [!definition] Deterministic Time Complexity
   Let $M$ be a deterministic Turing machine that halts on all inputs. The **running time** or **time complexity** of $M$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the maximum number of steps that $M$ uses on any input of length $n$. If $f(n)$ is the running time of $M$, we say that $M$ runs in time $f(n)$ and that $M$ is an $f(n)$ time Turing machine. Customarily, we use $n$ to represent the length of the input.

> [!definition] Nondeterministic Time Complexity
   Let $N$ be a nondeterministic Turing machine that is a decider. The **running time** of $N$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the maximum number of steps that $N$ uses on any branch of its computation on any input of length $n$.

> [!definition] Time Complexity Class
> Let $t: \mathcal N \rightarrow \mathcal R^{+}$ be a function: 
   $\text{TIME}(t(n)) = \{L | L \text{ is a language decided by an } O(t(n)) \text{ time deterministic Turing machine}\}.$
   $\text{NTIME}(t(n)) = \{L | L \text{ is a language decided by an  } O(t(n)) \text{ time nondeterministic Turing machine}\}.$


### Class P

> [!definition] Class P
>  $\text{P}$ is the class of languages that are decidable in polynomial time on a deterministic single-tape Turing machine. In other words, $$\text{P} = \cup_{k} \text{TIME}(n^k).$$

> [!remark] Role of Class P
> 1. $\text{P}$ is invariant for all models of computation that are polynomial equivalent to the deterministic single-tape Turing machine, and
> 2. $\text{P}$ roughly corresponds to the class of problems that are realistically solvable on a computer.

> [!theorem] 
> If $A \leq_\text{P} B$ and $B \in \text{P}$, then $A \in \text{P}$.

> [!example] Member of P
> - $\text{PATH} = \{\langle G, s, t \rangle | G \text{ is a directed graph that has a directed path from } s \text{ to } t\}.$
> - $\text{CONNECTED} = \{\langle G \rangle | G \text{ is a connected undirected graph}\}$.
> - $\text{TRIANGLE} = \{\langle G \rangle | G \text{ contains a triangle}\}$.
> - [[Number Theory#Divisibility and greatest common divisors|RELPRIME]]
> - Every context-free language is a member of $P$.

### Class NP

> [!definition] Verifier
> A **verifier** for a language $A$ is an algorithm $V$, where $$A = \{w | V \text{ accepts } \langle w, c \rangle \text{ for some string } c\}.$$
   We measure the time of a verifier only in terms of the length of $w$, so a **polynomial time verifier** runs in polynomial time in the length of $w$. A language $A$ is **polynomial verifiable** if it has a polynomial time verifier.

> [!definition] Certificate
> To test the membership in $A$, the verifier uses an additional information $c$ called a **certificate**, or **proof**.

> [!definition] Class NP
> $\text{NP}$ is the class of languages that have polynomial time verifiers.

> [!definition] Witness
> A **witness** in computer science is proof that you solved the problem correctly.

> [!theorem] 
> A language is in $\text{NP}$ if and only if it is decided by some nondeterministic polynomial time Turing machine: $$\text{NP} = \cup_k \text{NTIME}(n^k)$$

> [!example] Member of $\text{NP}$
> - [[Number Theory#Prime Numbers, Unique Factorization, and Finite Fields|COMPOSITES]]

> [!question] 
> Does $\text{coNP} = \text{NP}$? Does $\text{P} = \text{NP}$?

### Class NP-Complete

> [!definition] Class NP-complete
> A language $B$ is **NP-complete** if it satisfies two conditions:
> 1. $B$ is in $\text{NP}$, and
> 2. every $A$ in $\text{NP}$ is polynomial time reducible to $B$.
> 
> If $B$ merely satisfies condition 2, we say that it is $\text{NP}$-hard

> [!theorem] 
> If $B$ is **NP-complete** and $B \in \text{P}$, then $\text{P} = \text{NP}$ 

> [!theorem] Cook-Levin Theorem
 [[Satisfiability Problem|SAT]] is **NP-complete** (revisit the prove).

> [!example] Member of NP-Complete
> - $\text{CLIQUE} = \{\langle G, k \rangle | G \text{ is an undirected graph with a } k \text{-clique}\}.$
> - $\text{VERTEX-COVER} = \{\langle G, k \rangle | G \text{ is an undirected graph that has a } k\text{-node vertex cover}\}$  
> - $\text{HAMPATH} = \{\langle G, s, t \rangle | G \text{ is a directed graph with a Hamiltonian path from } s \text{ to } t\}.$
> - $\text{UHAMPATH} = \{\langle G, s, t \rangle | G \text{ is a undirected graph with a Hamiltonian path from } s \text{ to } t\}.$
> - [[Subset-Sum Problem|SUBSET-SUM]]

### Class Exp-time

> [!proposition] Observation
> $$\text{NP} \subseteq \text{EXPTIME} = \cup_k \text{TIME}(2^{n^k})$$

## Space Complexity

> [!definition] Deterministic Space Complexity
> Let $M$ be a deterministic Turing machine that halts on all inputs. The **space complexity** of $M$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the maximum number of tape cells that $M$ scans on any input of length $n$. If the space complexity of $M$ is $f(n)$, we also say that $M$ runs in space $f(n)$.

> [!definition] Nondeterministic Space Complexity
> If $N$ is a nondeterministic Turing machine wherein all branches halt on all inputs, we define its space complexity $f(n)$ to be the maximum number of tape cells that $N$ scans on any branch of its computation for any input of length $n$.

> [!definition] Space Complexity Class
> Let $f: \mathcal N \rightarrow \mathcal R^{+}$ be a function:
   $\text{SPACE}(f(n)) = \{L | L \text{ is a language decided by an } O(f(n)) \text{ space deterministic Turing machine}\}$
   $\text{NSPACE}(f(n)) = \{L | L \text{ is a language decided by an } O(f(n)) \text{ space nondeterministic Turing machine}\}$

> [!theorem] Savitch's theorem
For any function $f: \mathcal N \rightarrow \mathcal R^{+}$, where $f(n) \leq n$, $$\text{NSPACE}(f(n)) \subseteq \text{SPACE}(f^2(n))$$

### Class PSPACE

> [!definition] Class PSPACE 
> **PSPACE** is the class of languages that are decidable in polynomial space on a deterministic Turing machine. In other words, $$\text{PSPACE} = \cup_k \text{SPACE}(n^k),$$
> i.e., these problems might not be computational easy to solve or verify but only require a limited space to verify.

### Class PSPACE-Complete

> [!definition] Class PSPACE-complete
 A language $B$ is **PSPACE-complete** if it satisfies two conditions:
> 1. $B$ is in $\text{PSPACE}$, and
> 2. every $A$ in $\text{PSPACE}$ is polynomial time reducible to $B$.
>
> If $B$ merely satisfies condition 2, we say that it is $\text{PSPACE-hard}$.

> [!theorem] 
> [[Satisfiability Problem|TQBF]] is $\text{PSPACE}$-complete.

> [!example] Member of NP-Complete
> **Formula game**: Player $\text{A}$ selects values for variable with $\forall$ quantifiers, player $\text{E}$ selects values for variable with $\exists$ quantifiers.
$\text{FORMULA-GAME} = \{\langle \phi \rangle | \text{Player E has a winning strategy in the formula game associated with } \phi\}.$
**Generalized geography**: Match last character of a city with the first character of the next city.
$\text{GG} =\{\langle G, b \rangle | \text{Player I has a winning strategy for the generalized geography game played on graph } G \text{ starting at node } b\}$

### Classes L and NL

> [!remark]
> When consider these classes, we consider two tape:
> - A read-only input tape.
> - A read/write work tape (measure this).

> [!definition] Class L
 $\text{L}$ is the class of languages that are decidable in logarithmic space on a deterministic Turing machine: $\text{L} = \text{SPACE}(log\; n)$.

> [!definition] Class NL
$\text{NL}$ is the class of languages that are decidable in logarithmic space on a nondeterministic Turing machine: $\text{NL} = \text{NSPACE}(log\;n)$.

$\text{NL} = \text{coNL}$.

>[!definition] Configuration of Turing machine with a read-only input tape
> If $M$ is a Turing machine that has a separate read-only input tape and $w$ is an input, a **configuration of $M$ on $w$** is a setting of the state, the work tape, and the positions of the two tape heads. The input $w$ is not a part of the configuration of $M$ on $w$ (because $w$ is constant).

### Class NL-completeness

> [!definition] Class NL-complete
> A language $B$ is $\text{NL}$-complete if
> 1. $B \in \text{NL}$, and
> 2. every $A$ in $\text{NL}$ is log space reducible to $B$.
