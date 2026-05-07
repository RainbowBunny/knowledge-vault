
## Efficient Algorithm

> [!definition] Efficient Algorithm
> Let $A$ be an algorithm (possibly probabilistic) that takes as input a security parameter $\lambda \in \mathbb Z_{\geq 1}$, as well as other parameters encoded as a bit string $x \in \{0, 1\}^{p(\lambda)}$ for some fixed polynomial $p$. We call $A$ an **efficient algorithm** if there exist a poly-bounded function $t$ and a negligible function $\epsilon$ such that for all $\lambda \in \mathbb Z_{\geq 1}$, and all $x \in \{0, 1\}^{\leq p(\lambda)}$, the probability that the running time of $A$ on input $(\lambda, x)$ exceeds $t(\lambda)$ is at most $\epsilon(\lambda)$.

## Time Complexity

> [!definition] Deterministic Time Complexity
   Let $M$ be a deterministic Turing machine that halts on all inputs. The **running time** or **time complexity** of $M$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the maximum number of steps that $M$ uses on any input of length $n$. If $f(n)$ is the running time of $M$, we say that $M$ runs in time $f(n)$ and that $M$ is an $f(n)$ time Turing machine. Customarily, we use $n$ to represent the length of the input.

> [!definition] Nondeterministic Time Complexity
   Let $N$ be a nondeterministic Turing machine that is a decider. The **running time** of $N$ is the function $f: \mathcal N \rightarrow \mathcal N$, where $f(n)$ is the maximum number of steps that $N$ uses on any branch of its computation on any input of length $n$.

> [!definition] Time Complexity Class
> Let $t: \mathcal N \rightarrow \mathcal R^{+}$ be a function: 
   $\text{TIME}(t(n)) = \{L | L \text{ is a language decided by an } O(t(n)) \text{ time deterministic Turing machine}\}.$
   $\text{NTIME}(t(n)) = \{L | L \text{ is a language decided by an  } O(t(n)) \text{ time nondeterministic Turing machine}\}.$

### Complexity Relationships Among Models

> [!theorem]
Let $t(n)$ be a function, where $t(n) \geq n$. Then every $t(n)$ time multitape Turing machine has an equivalent $O(t^2(n))$ time single-tape Turing machine.

### Class P

> [!definition] Class P
>  $\text{P}$ is the class of languages that are decidable in polynomial time on a deterministic single-tape Turing machine. In other words, $$\text{P} = \cup_{k} \text{TIME}(n^k).$$

> [!remark] Role of Class P
> 1. $\text{P}$ is invariant for all models of computation that are polynomial equivalent to the deterministic single-tape Turing machine, and
> 2. $\text{P}$ roughly corresponds to the class of problems that are realistically solvable on a computer.

> [!example] Member of P
> - $\text{PATH} = \{\langle G, s, t \rangle | G \text{ is a directed graph that has a directed path from } s \text{ to } t\}.$
> - $\text{CONNECTED} = \{\langle G \rangle | G \text{ is a connected undirected graph}\}$.
> - $\text{TRIANGLE} = \{\langle G \rangle | G \text{ contains a triangle}\}$.
> - [[Number Theory#Divisibility and greatest common divisors|RELPRIME]]
> - Every context-free language is a member of $P$.

### Class NP


> [!definition] Class NP
> $\text{NP}$ is the class of languages that have polynomial time verifiers.



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
