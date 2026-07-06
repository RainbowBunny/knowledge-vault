> [!info]
> Representations and traversal are written; trees/DAGs, connectivity, and flows (sections at the bottom) are still outlines. Related material:
> - [[Graph DP]] — Optimal BST, Longest Path in DAG, Bitonic TSP
> - [[Acyclic Subgraphs]] — incidence-matrix columns vs. acyclicity (matroid view)
> - [[CP Setup]] / [[Snippet Reference]] — competitive snippet prefixes for graph algorithms

## Basic Definition

> [!definition] Sparse Graph
> A graph that has $|E|$ is much less than $|V|^2$.

> [!definition] Dense Graph
> A graph that has $|E|$ close to $|V|^2$.

> [!definition] Square
> The **square** of a directed graph $G = (V, E)$ is the graph $G^2 = (V, E^2)$ such that $(u, v) \in E^2$ if and only $G$ contains a path with at most two edges between $u$ and $v$.

> [!definition] Universal Sink
> Vertex with in-degree $|V| - 1$ and out-degree 0.

### Weighted Graph

> [!definition] Weighted Graph
> Each edge has an associated **weight**, typically given by a **weighted function** $w: E \rightarrow \mathbb R$.

## Representations of Graphs

### Adjacency-List Representation

> [!definition] Adjacency-List Representation
> The **adjacency-list representation** of a graph $G = (V, E)$ consists of an array $Adj$ of $|V|$ lists, one for each vertex in $V$. For each $u \in V$, the adjacency list $Adj[u]$ contains all the vertices adjacent to $u$ in $G$. 

### Adjacency-Matrix Representation

> [!definition] Adjacency-Matrix Representation
> Assume vertices are numbered $1, 2, \dots, |V|$ in some arbitrary manner, the adjacency-matrix representation of a graph $G$ consists of a $|V| \times |V|$ matrix $A = (a_{ij})$ such that $$a_{ij} = \begin{cases}1 &\text{if } (i, j) \in E, \\ 0 &\text{otherwise}.\end{cases}$$

> [!definition] Transpose
> The **transpose** of a directed graph $G = (V, E)$ is the graph $G^T = (V, E^T)$, where $E^T = \{(u, v) \in V \times V: (u, v) \in E\}$. Thus, $G^T$ is $G$ with all its edges reversed.

### Representing Attributes


### Incidence Matrix

> [!definition] Incidence Matrix
> The **incidence matrix** of a directed graph $G = (V, E)$ with no self-loops is a $|V| \times |E|$ matrix $B = (b_{i j})$ such that $$b_{i j} = \begin{cases}-1 &\text{if edge } j \text{ leaves vertex } i, \\ 1 &\text{if edge } j \text{ enters vertex } i, \\ 0 &\text{otherwise}\end{cases}$$

> [!proposition]
> $$B B^T(i, j) = \begin{cases}
> 	\text{degree of } i = \text{in-degree} + \text{out-degree} &\text{if } i = j \\
> 	-(\# \text{ of edges connecting } i \text{ and } j) &\text{if } i \neq j
> \end{cases}$$

## Traversal

### BFS

> [!pseudocode]
> ```
> BFS(G, s)
>  1. for each vertex u in G.V - {s}
>  2.     u.color = WHITE
>  3.     u.d = INF
>  4.     u.pi = NIL
>  5. s.color = GRAY
>  6. s.d = 0
>  7. s.pi = NIL
>  8. Q = EMPTYSET
>  9. ENQUEUE(Q, s)
> 10. while Q != EMPTYSET
> 11.     u = DEQUEUE(Q)
> 12.     for each v in G.Adj[u]
> 13.         if v.color == WHITE
> 14.             v.color = GRAY
> 15.             v.d = u.d + 1
> 16.             v.pi = u
> 17.             ENQUEUE(Q, v)
> 18.     u.color = BLACK
> ```

> [!definition] Breadth-First Tree
> The procedure BFS build a breadth-first tree as it searches the graph. The tree corresponds to the $\pi$ attributes. Formally, for a graph $G = (V, E)$ with source $s$, we define the **predecessor subgraph** of $G$ as $G_\pi = (V_\pi, E_\pi)$, where $$V_{\pi} = \{v \in V: v.\pi \neq NIL\} \cap \{s\}$$ and $$E_{\pi} = \{(v.\pi, v): v \in V_\pi - \{s\}\}.$$
> The predecessor subgraph $G_{\pi}$ is a **breadth-first tree** if $V_\pi$ consists of the vertices reachable from $s$ and, for all $v \in V_\pi$, the subgraph $G_\pi$ contains a unique simple path from $s$ to $v$ that is also a shortest path from $s$ to $v$ in $G$.

> [!lemma]
> When applied to a directed or undirected graph $G = (V, E)$, procedure BFS constructs $\pi$ so that the predecessor subgraph $G_\pi = (V_\pi, E_\pi)$ is a breadth-first tree.

> [!pseudocode]
> ```
> PRINT-PATH(G, s, v)
> 1. if v == s
> 2.     print s
> 3. elseif v.pi == NIL
> 4.     print "no path from" s "to" v "exists"
> 5. else PRINT-PATH(G, s, v.pi)
> 6.     print v
> ```

### DFS

> [!pseudocode]
> ```
> DFS(G)
> 1. for each vertex u in G.V
> 2.     u.color = WHITE
> 3.     u.pi = NIL
> 4. time = 0
> 5. for each vertex u in G.V
> 6.     if u.color == WHITE
> 7.         DFS-VISIT(G, u)
> 
> DFS-VISIT(G, u)
>  1. time = time + 1
>  2. u.d = time
>  3. u.color = GRAY
>  4. for each v in G.Adj[u]
>  5.     if v.color == WHITE
>  6.         v.pi = u
>  7.         DFS-VISIT(G, v)
>  8. u.color = BLACK
>  9. time = time + 1
> 10. u.f = time
> ```

> [!definition] Predecessor Subgraph
> The **predecessor subgraph** of a depth-first search slightly differently from that of a breadth-first search: we let $G_\pi = (V, E_\pi)$, where $$E_\pi = \{(v.\pi, v): v \in V \text{ and } v.\pi \neq \text{NIL}\}.$$
> The predecessor subgraph of a depth-first search forms a **depth-first forest** comprising several **depth-first trees**. The edges in $E_\pi$ are **tree edges**.

> [!theorem] Parenthesis Theorem
> In any depth-first search of a (directed or undirected) graph $G = (V, E)$, for any two vertices $u$ and $v$, exactly one of the following three conditions holds:
> - The interval $[u.d, u.f]$ and $[v.d, v.f]$ are entirely disjoint, and neither $u$ nor $v$ is a descendant of other in the depth-first forest,
> - The interval $[u.d, u.f]$ is contained entirely within the interval $[v.d, v.f]$, and $u$ is a descendant of $v$ in a depth-first tree, or
> - The interval $[v.d, v.f]$ is contained entirely within the interval $[u.d, u.f]$, and $v$ is a descendant of $u$ in a depth-first tree.

> [!corollary] Nesting of descendants' intervals
> Vertex $v$ is a proper descendant of vertex $u$ in the depth-first forest for a (directed or undirected) graph $G$ if and only if $u.d < v.d < v.f < u.f$.

> [!theorem] White-path Theorem
> In a depth-first forest of a (directed or undirected) graph $G = (V, E)$, vertex $v$ is a descendant of vertex $u$ if and only if at the time $u.d$ that the search discovers $u$, there is a path from $u$ to $v$ consisting entirely of white vertices. 

> [!definition] Classification of Edges
> We can define four edge types in terms of the depth-first forest $G_\pi$ produces by a depth-first search on $G$:
> 1. **Tree edges** are edges in the depth-first forest $G_\pi$. Edge $(u, v)$ is a tree edge if $v$ was discovered by exploring edge $(u, v)$.
> 2. **Back edges** are those edges $(u, v)$ connecting a vertex $u$ to an ancestor $v$ in a depth-first tree. We consider self-loops, which may occur in directed graphs, to be back edges.
> 3. **Forward edges** are those nontree edges $(u, v)$ connecting a vertex $u$ to a descendant $v$ in a depth-first tree.
> 4. **Cross edges** are all other edges. They can go between vertices in the same depth-first tree, as long as one vertex is not an ancestor of the other, or they can go between vertices in different depth-first trees.

> [!remark]
> The DFS algorithm has enough information to classify some edges as it encounters them. The key idea is that when we first explore an edge $(u, v)$, the color of vertex $v$ tells us something about the edge:
> 1. `WHITE` indicates a tree edge.
> 2. `GRAY` indicates a back edge, and
> 3. `BLACK` indicates a forward or cross edge.

> [!theorem]
> In a depth-first search of an undirected graph $G$, every edge of $G$ is either a tree edge or a back edge.

## Shortest Paths

### By BFS

> [!lemma]
> Let $G = (V, E)$ be a directed or undirected graph, and let $s \in V$ be an arbitrary vertex. Then, for any edge $(u, v) \in E$, $$\delta(s, v) \leq \delta(s, u) + 1.$$ 

> [!lemma]
> Let $G = (V, E)$ be a directed or undirected graph, and suppose that BFS is run on $G$ from a given source vertex $s \in V$. Then upon termination, for each vertex $v \in V$, the value $v.d$ computed by BFS satisfies $v.d \geq \delta(s, v)$.

> [!lemma]
> Suppose that during the execution of BFS on a graph $G = (V, E)$, the queue $Q$ contains the vertices $\langle v_1, v_2, \dots, v_r \rangle$, where $v_1$ is the head of $Q$ and $v_r$ is the tail. Then, $v_r.d \leq v_1.d + 1$ and $v_1.d \leq v_{i + 1}.d$ for $i = 1, 2, \dots, r - 1$. 

> [!corollary]
> Suppose that vertices $v_i$ and $v_j$ are enqueued during the execution of BFS, and that $v_i$ is enqueued before $v_j$. Then $v_i.d \leq v_j.d$ at the time that $v_j$ is enqueued.

> [!theorem] Correctness of Breadth-first Search
> Let $G = (V, E)$ be a directed or undirected graph, and suppose that BFS is run on $G$ from a given source vertex $s \in V$. Then, during its execution, BFS discovers every vertex $v \in V$ that is reachable from the source $s$, and upon termination, $v.d = \delta(s, v)$ for all $v \in V$. Moreover, for any vertex $v \neq s$ that is reachable from $s$, one of the shortest paths from $s$ to $v$ is a shortest path from $s$ to $v.\pi$ followed by the edge $(v.\pi, v)$.

## Trees & DAGs

- LCA (binary lifting)
- Euler tour
- Topological sort

## Connectivity

- DSU / Union-Find
- Kruskal MST
- Prim MST

## Flows

- Dinic's algorithm
