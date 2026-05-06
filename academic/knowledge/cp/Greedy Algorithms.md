
> [!definition] Greedy Algorithm
> A **greedy algorithm** is a solution of an optimization problems that always make the choice that looks best at the moment.

> [!remark]
> When developing greedy algorithm, we went through the following steps:
> 1. Cast the optimization problem as one in which we make a choice and are left with one subproblem to solve.
> 2. Prove that there is always an optimal solution to the original problem that makes the greedy choice, so that the greedy choice is always safe.
> 3. Demonstrate optimal substructure by showing that, having made the greedy choice, what remains is a subproblem with the property that if we combine an optimal solution to the subproblem with the greedy choice we have made, we arrive at an optimal solution to the original problem.

> [!definition] Greedy-Choice Property
> We can assemble a globally optimal solution by making locally optimal (greedy) choices. In other words, when we are considering which choice to make, we make the choice that looks best in the current problem, without considering results from subproblems.

## Activity-selection problem

> [!definition] Activity-selection problem
> Suppose we have a set $S = \{a_1, a_2, \dots, a_n\}$ of $n$ proposed **activities** that wish to use a resource, such as a lecture hall, which can serve only one activity at a time. Each activity $a_i$ has a **start time** $s_i$ and a **finish time** $f_i$, where $0 \leq s_i < f_i < \infty$. If selected, activity $a_i$ takes place during the half-open time interval $[s_i, f_i)$. Activities $a_i$ and $a_j$ are **compatible** if the intervals $[s_i, f_i)$ and $[s_j, f_j)$ do not overlap. We wish to select a maximum-size subset of mutually compatible activities.

> [!pseudocode]
> ```
> RECURSIVE-ACTIVITY-SELECTOR(s, f, k, n)
> 1. m = k + 1
> 2. while m <= n and s[m] < f[k]
> 3.     m = m + 1
> 4. if m <= n
> 5.     return {a[m]} ∪ RECURSIVE-ACTIVITY-SELECTOR(s, f, m, n)
> 6. return ∅
> ```

> [!pseudocode]
> ```
> GREEDY-ACTIVITY-SELECTOR(s, f)
> 1. n = A.length
> 2. A = {a[1]}
> 3. k = 1
> 4. for m = 2 to n
> 5.     if s[m] >= f[k]
> 6.         A = A ∪ {a[m]}
> 7.         k = m
> 8. return A
> ```

### Multiple Lecture Hall Variant

> [!definition] Multiple Lecture Hall Variant
> Now we have a large number of lecture halls, where any activity can take place in any lecture hall. We wish to schedule all the activities using as few lecture halls as possible.

> [!remark] Idea
> We keep a set of unoccupied lecture halls, and sorting the events of having activity start $s_i$ and activity finish $t_i$ (If $s_i = t_j$ then activity finish will go first). Thus, we can just greedily put activity to empty lecture hall.

### Weighted Variant

> [!definition] Weighted Variant
> Now, each activity $a_i$ has an additional value $v_i$ and thus we are not maximize the number of activities scheduled but the sum of $v$ for chosen activity.

> [!remark] Idea
> We can not use greedy for this problem but dynamic programming works. Sort activities according to the ending time and calculate `c[i, j]` is the answer for all activities that start after $a_i$ and end before $a_j$.

## Huffman Codes

> [!definition] Variable-Length Code
> Considering the problem of designing a **binary character code** (or **code**) in which each character is represented by a unique binary string (**codeword**). If every codeword has the same length then it is called **fixed-length code**, else, it is called **variable-length code**.

> [!definition] Prefix Code
> The codes such that no codeword in it is also a prefix of some other codeword is called **prefix codes**.

> [!definition] Optimal Code Problem
> Given a tree $T$ corresponding to a prefix code, we can easily compute the number of bits required to encode a file (**cost**) by the formula: $$B(T) = \sum_{c \in C} c.\text{freq} \cdot d_T(c).$$ Where, $c.\text{freq}$ is frequency of character $c$ and $d_T(c)$ is the length of the codeword for character $c$.

> [!pseudocode]
> ```
> HUFFMAN(C)
> 1. n = |C|
> 2. Q = C
> 3. for i = 1 to n - 1
> 4.     allocate a new node z
> 5.     z.left = x = EXTRACT-MIN(Q)
> 6.     z.right = y = EXTRACT-MIN(Q)
> 7.     z.freq = x.freq + y.freq
> 8.     INSERT(Q, z)
> 9. return EXTRACT-MIN(Q)
> ```

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

## Task-scheduling Problem as a Matroid

> [!definition] Scheduling Unit-time Tasks with Deadlines and Penalties for a Single Processor
> **Input**:
> - A set $S = \{a_1, a_2, \dots, a_n\}$ of $n$ unit-time tasks;
> - A set of $n$ integer **deadlines** $d_1, d_2, \dots, d_n$, such that each $d_i$ satisfies $1 \leq d_i \leq n$ and task $a_i$ is supposed to finish by time $d_i$; and
> - A set of $n$ nonnegative weights or **penalties** $w_1, w_2, \dots, w_n$, such that we incur a penalty of $w_i$ if task $a_i$ is not finished by time $d_i$, and we incur no penalty if a task finishes by its deadline.
> 
> Find a schedule for $S$ that minimizes the total penalty incurred for missed deadlines.

> [!definition] Canonical Form
> We can always transform an arbitrary schedule into **canonical form**, in which the early tasks precede the late tasks and we schedule the early tasks in order of monotonically increasing deadlines.

> [!theorem]
> We say a set $A$ of tasks is **independent** if there exists a schedule for these tasks such that no tasks are late. Then set $S$ is a set of unit-time tasks with deadlines, and $\mathcal I$ is the set of all independent sets of tasks form a matroid.

> [!pseudocode]
> ```
> SCHEDULING-VARIATIONS(A)
>  1. let D[1..n] be a new array
>  2. for i = 1 to n
>  3.     a[i].time = a[i].deadline
>  4.     if D[a[i].deadline] != NIL
>  5.         y = FIND-SET(D[a[i].deadline])
>  6.         a[i].time = y.low - 1
>  7.     x = MAKE-SET(a[i])
>  8.     D[a[i].time] = x
>  9.     x.low = x.high = a[i].time
> 10.     if D[a[i].time - 1] != NIL
> 11.         UNION(D[a[i].time - 1], D[a[i].time])
> 12.     if D[a[i].time + 1] != NIL
> 13.         UNION(D[a[i].time + 1], D[a[i].time])
> ```

## Task scheduling to Minimize Average Completion Time

> [!definition] Task scheduling to minimize average completion time
> Suppose you are given a set $S = \{a_1, a_2, \cdots, a_n\}$ of tasks, where task $a_i$ requires $p_i$ units of processing time to complete. You have one computer on which to run these tasks, and the computer can run only one task at a time. Let $c_i$ be the **completion time** of task $a_i$, that is, the time at which task $a_i$ complete processing. Minimize the average completion time: $$\frac{1}{n} \sum_{i = 1}^n c_i.$$

### Non-preemptive Variant

> [!definition] Non-preemtive
> Once task $a_i$ starts, it must run continuously for $p_i$ units of time.

> [!proposition] 
> Greedy algorithm by sorting task by length works.

### Preemptive Variant with Release Time

> [!definition]
> Now, tasks are not all available at once. That is, each task cannot start until its **release time** $r_i$. Also, we now allow **preemption**, so that a task can be suspended and restarted at a later time.

> [!proposition]
> Now greedy need to run for every unit of time (we can reduce to only consider release time).

## Acyclic Subgraphs

> [!definition] Incidence Matrix
> The **incidence matrix** for an undirected graph $G = (V, E)$ is a $|V| \times |E|$ matrix $M$ such that $M_{ve} = 1$ if edge $e$ is incident on vertex $v$, and $M_{ve} = 0$ otherwise. 
> The **incidence matrix** for an directed graph $G = (V, E)$ with no self-loops is a $|V| \times |E|$ matrix $M$ such that $M_{ve} = -1$ if edge $e$ leaves vertex $v$, $M_{ve} = 1$ if edge $e$ enters vertex $v$, and $M_{ve} = 0$ otherwise.

> [!proposition]
> Consider the incidence matrix for an undirected graph $G = (V, E)$. A set of columns of $M$ is linearly independent over $\mathbb F_2$ if and only if the corresponding set of edges is acyclic.

> [!proposition]
> Consider the incidence matrix for a directed graph $G = (V, E)$ with no self-loops, then if a set of columns of $M$ is linearly independent, then the corresponding set of edges does not contain a directed cycle.

## Off-line chaching

