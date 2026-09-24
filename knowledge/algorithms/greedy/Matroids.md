## Matroid

> [!definition] Matroid
> A **matroid** is an ordered pair $M = (S, \mathcal I)$ satisfying the following conditions:
> 1. $S$ is a finite set.
> 2. $\mathcal I$ is a nonempty family of subsets of $S$, called the **independent** subsets of $S$, such that if $B \in \mathcal I$ and $A \subseteq B$, then $A \in \mathcal I$. We say that $\mathcal I$ is **hereditary** if it satisfies this property. Note that the empty set $\emptyset$ is necessarily a member of $\mathcal I$.
> 3. If $A \in \mathcal I, B \in \mathcal I$, and $|A| < |B|$, then there exists some element $x \in B - A$ such that $A \cup \{x\} \in \mathcal I$. We say that $M$ satisfies the **exchange property**.

> [!example] Matrix Matroid
> Let $M$ be a matrix and $S$ are rows of the given matrix, and $\mathcal I$ is the family of set of linearly independent rows. Then $(S, \mathcal I)$ form a **matrix matroid**.

> [!example] Graphic Matroid
> For a given undirected graph $G = (V, E)$:
> - The set $S_G$ is defined to be $E$, the set of edges of $G$.
> - If $A$ is a subset of $E$, then $A \in \mathcal I_G$ if and only if $A$ is acyclic. That is, a set of edges $A$ is independent if and only if the subgraph $G_A = (V, A)$ forms a forest.
> The structure $(S_G, \mathcal I_G)$ form a **graphic matroid**.

> [!definition] Extension
> Given a matroid $M = (S, \mathcal I)$, we call an element $x \in A$ an **extension** of $A \in \mathcal I$ if we can add $x$ to $A$ while preserving independence.

> [!definition] Maximal
> If $A$ is an independent subset in a matroid $M$, we say that $A$ is **maximal** if it has no extensions.

> [!theorem]
> All maximal independent subsets in a matroid have the same size.

> [!definition] Weighted Matroid
> We say that a matroid $M = (S, \mathcal I)$ is **weighted** if it is associated with a weight function $w$ that assigns a **strictly positive** weight $w(x)$ to each element $x \in S$. The weight function $w$ extends to subsets of $S$ by summation: $$w(A) = \sum_{x \in A} w(x)$$ for any $A \subseteq S$.

> [!definition] Optimal
> Given a weight matroid $M = (S, \mathcal I)$, an independent set $A \in \mathcal I$ such that $w(A)$ is maximized is an **optimal** subset of the matroid.

> [!pseudocode]
> ```
> GREEDY(M, w)
> 1. A = ∅
> 2. sort M.S into monotonically decreasing order by weight w
> 3. for each x ∈ M.S, taken in monotonically decreasing order by weight w(x)
> 4.     if A ∪ {x} ∈ M.I
> 5.         A = A ∪ {x}
> 6. return A
> ```
> Complexity: $O(n \lg n + n f(n))$.

> [!example] Dual of a Matroid
> If $(S, \mathcal I)$ is a matroid, then $(S, \mathcal I')$ is a matroid, where $$I' = \{A' : S - A' \text{ contains some maximal } A \in \mathcal I\}.$$ That is, the maximal independent sets of $(S, \mathcal I')$ are just the complements of the maximal independent sets of $(S, \mathcal I)$.

> [!example]
> Let $S$ be a finite set and let $S_1, S_2, \dots, S_k$ be a partition of $S$ into nonempty disjoint subsets. Define the structure $(S, \mathcal I)$ by the condition that $\mathcal I = \{A : |A \cup S_i| \leq 1 \forall i = 1, 2, \cdots, k \}$. Then $(S, \mathcal I)$ is a matroid.
