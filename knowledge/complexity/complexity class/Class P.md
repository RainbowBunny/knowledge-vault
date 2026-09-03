## Definition

> [!definition] Class P
> $\text{P}$ is the class of languages that are decidable in polynomial time on a deterministic single-tape Turing machine: $$\text{P} = \bigcup_{k} \text{TIME}(n^k).$$
> Unfolded (machine form): $L \in \text{P}$ iff there exist a deterministic Turing machine $M$ and a polynomial $p(\cdot)$ such that
> - On input a string $x$, machine $M$ halts after at most $p(|x|)$ steps, and
> - $M(x) = 1$ if and only if $x \in L$.

> [!remark] Role of Class P
> 1. $\text{P}$ is invariant for all models of computation that are polynomial-equivalent to the deterministic single-tape Turing machine.
> 2. $\text{P}$ roughly corresponds to the class of problems that are realistically solvable on a computer.

## Property

> [!theorem]
> If $A \leq_\text{P} B$ and $B \in \text{P}$, then $A \in \text{P}$.

## Member

> [!example] Members of P
> - $\text{PATH} = \{\langle G, s, t \rangle \mid G \text{ is a directed graph with a directed path from } s \text{ to } t\}$
> - $\text{CONNECTED} = \{\langle G \rangle \mid G \text{ is a connected undirected graph}\}$
> - $\text{TRIANGLE} = \{\langle G \rangle \mid G \text{ contains a triangle}\}$
> - [[Number Theory#Divisibility and greatest common divisors|RELPRIME]]
> - Every context-free language
