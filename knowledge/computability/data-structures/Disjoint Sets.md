## Disjoint Sets

> [!definition] Disjoint-set Data Structure
> A **disjoint-set data structure** maintain a collection $S = \{S_1, S_2, \dots, S_k\}$ of disjoint dynamic sets. We identify each set by a **representative**, which is some member of the set. In some applications, it doesn't matter which member is used as the representative; we care only that if we ask for the representative of a dynamic set twice without modifying the set between the requests, we get the same answer both times. Other applications may require a prespecified rule for choosing the representative, such as choosing the smallest member in the set.

> [!algorithm] Disjoint-set Operations
> The disjoint-set data structure support these operations:
> - `MAKE-SET(x)`: creates a new set whose only member (and thus representative) is $x$. Since the sets are disjoint, we require that $x$ not already be in some other set.
> - `UNION(x, y)`: unites the dynamic sets that contain $x$ and $y$, say $S_x$ and $S_y$, into a new set that is the union of these two sets. We assume that the two sets are disjoint prior to the operation. The representative of the resulting set is any member of $S_x \cup S_y$. Since we require the sets in the collection to be disjoint, conceptually we destroy sets $S_x$ and $S_y$, removing them from the collection $S$.
> - `FIND-SET(x)`: returns a pointer to the representative of the (unique) set containing $x$.

### Linked-List Implementation

> [!remark]
> This implementation represents the set as linked-list. 

> [!pseudocode]
> ```
> MAKE-SET(x)
> 1. Create a node S
> 2. x.set = S
> 3. x.next = NIL
> 4. S.head = x
> 5. S.tail = x
> 6. S.size = 1
> 7. return S
> 
> FIND-SET(x)
> 1. return x.set.head
> 
> UNION(x, y)
>  1. S1 = x.set
>  2. S2 = y.set
>  3. S1.tail.next = S2.head
>  4. z = S2.head
>  5. while z != NIL
>  6.     z.set = S1
>  7.     z = z.next
>  8. S1.tail = S2.tail
>  9. S1.size = S1.size + S2.size
> 10. return S1
> ```

> [!proposition] Weighted-Union Heuristic
> When merging two lists, we always append the shorter list onto the longer, breaking ties arbitrary.

> [!pseudocode]
> ```
> MAKE-SET-WU(x)
> 1. L = MAKE-SET(x)
> 2. L.size = 1
> 3. return L
> 
> UNION-WU(x, y)
> 1. L1 = x.set
> 2. L2 = y.set
> 3. if L1.size >= L2.size
> 4.     L = UNION(x, y)
> 5. else UNION(y, x)
> 6. L.size = L1.size + L2.size
> 7. return L
> ```

> [!theorem]
> Using the linked-list representation of disjoint sets and the weighted-union heuristic, a sequence of $m$ `MAKE-SET`, `UNION` and `FIND-SET` operations, $n$ of which are `MAKE-SET` operations, takes $O(m + n \lg n)$ time.

### Disjoint-Set Forests

> [!remark]
> This implementation represents the set as forest by storing parent of each node.

> [!proposition] Union by Rank
> For each node, we maintain a **rank**, which is an upper bound on the height of the node. In union by rank, we make the root with smaller rank point to the root with larger rank during a `UNION` operation.

> [!proposition] Path Compresssion
> In `FIND-SET` operations to make each node on the find path point directly to the root. Path compression does not change any ranks.

> [!pseudocode]
> ```
> MAKE-SET(x)
> 1. x.p = x
> 2. x.rank = 0
> 
> UNION(x, y)
> 1. LINK(FIND-SET(x), FIND-SET(y))
> 
> LINK(x, y)
> 1. if x.rank > y.rank
> 2.     y.p = x
> 3. else x.p = y
> 4.     if x.rank == y.rank
> 5.         y.rank = y.rank + 1
> 
> FIND-SET(x)
> 1. if x != x.p
> 2.     x.p = FIND-SET(x.p)
> 3. return x.p
> ```

> [!proposition] Effect of the Heuristics on the Running Time
> For a sequence of $n$ `MAKE-SETS` operations (and hence at most $n - 1$ operations) and $f$ `FIND-SET` operations, the path-compression heuristic alone gives a worst-case running time of $\Theta(n + f \cdot (1 + \log_{2 + f/n} n))$.
> When we use both union by rank and path compression, the worst-case running time is $O(m \alpha(n))$, where $\alpha(n)$ is a very slowly growing function.

### Connected Components

> [!pseudocode]
> ```
> CONNECTED-COMPONENTS(G)
> 1. for each vertext v in G.V
> 2.     MAKE-SET(v)
> 3. for each edge (u, v) in G.E
> 4.     if FIND-SET(u) != FIND-SET(v)
> 5.         UNION(u, v)
> 
> SAME-COMPONENT(u, v)
> 1. if FIND-SET(u) == FIND-SET(v)
> 2.     return TRUE
> 3. else return FALSE
> ```
