# Branching Programs

A circuit-like model that reads each input variable at most some bounded number of times.

> [!definition] Branching Program
> A **branching program** is a directed acyclic graph where all nodes are labeled by variables, except for two **output nodes** labeled $0$ or $1$. The nodes labeled by variables are called **query nodes**. Every query node has two outgoing edges: one labeled $0$ and one labeled $1$. Both output nodes have no outgoing edges. One node in a branching program is designated the **start node**.

> [!definition] Read-once Branching Program
> A **read-once branching program** is one that can query each variable at most one time on every directed path from the start node to an output node.

## Polynomial-Identity Tools

Branching programs are commonly analyzed using polynomial-identity testing techniques. Two foundational lemmas:

> [!lemma] Univariate Degree Bound
> For every $d \geq 0$, a degree-$d$ polynomial $p$ in a single variable $x$ either has at most $d$ roots, or is identically zero.

> [!lemma] Schwartz-Zippel
> Let $\mathcal F$ be a finite field with $f$ elements and let $p$ be a nonzero polynomial in variables $x_1, \dots, x_m$, where each variable has degree at most $d$. If $a_1, \dots, a_m$ are selected uniformly at random in $\mathcal F$, then $$\Pr[p(a_1, \cdots, a_m) = 0] \leq \frac{md}{f}.$$

These give a randomized polynomial-identity testing algorithm: evaluate $p$ at a random point; if it's nonzero, $p$ is nonzero; if it's zero, $p$ is likely zero. The corresponding decision problem is in [[Randomized Complexity#Class BPP|BPP]].

## Decision Tree Model

> [!definition] Decision Tree Model
> For a problem with input space $S$, a **decision tree** is a tree where each internal node tests an input bit and each leaf outputs an answer. The decision-tree complexity of a problem is the maximum depth needed.
>
> Lower bounds come from $|S| \leq \text{number of leaves}$, giving $\log_2 |S|$ as a generic lower bound.

## Related

- [[Circuit Complexity]] — the broader non-uniform world
- [[Randomized Complexity]] — Schwartz-Zippel gives randomized tests
