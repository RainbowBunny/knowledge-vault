## Optimal Binary Search Trees

> [!definition] Optimal Binary Search Tree
> Given a sequence $K = \langle k_1, k_2, \dots, k_n \rangle$ of $n$ distinct keys in sorted order ($k_1 < k_2 < \cdots < k_n$), we wish to build a binary search tree from these keys. For each key $k_i$, we have a probability $p_i$ that a search will be for $k_i$. Some searches may be for values not in $K$, and so we also have $n + 1$ "dummy keys" $d_0, d_1, d_2, \cdots, d_n$ representing values not in $K$ or $d_0 < k_1 < d_1 < k_2 < \cdots < k_n < d_n$. Also, for each $d_i$ there is a probability $q_i$.

> [!pseudocode]
> ```
> OPTIMAL-BST(p, q, n)
>  1. let e[1..n + 1, 0..n], w[1..n + 1, 0..n], and root[1..n, 1..n] be new tables
>  2. for i = 1 to n + 1
>  3.     e[i, i - 1] = q[i - 1]
>  4.     w[i, i - 1] = q[i - 1]
>  5. for l = 1 to n
>  6.     for i = 1 to n - l + 1
>  7.         j = i + l - 1
>  8.         e[i, j] = INF
>  9.         w[i, j] = w[i, j - 1] + p[j] + q[j]
> 10.         for r = root[i, j - 1] to root[i + 1, j]
> 11.             t = e[i, r - 1] + e[r + 1, j] + w[i, j]
> 12.             if t < e[i, j]
> 13.                 e[i, j] = t
> 14.                 root[i, j] = r
> 15. return (e, root)
> ```

> [!pseudocode]
> ```
> CONSTRUCT-OPTIMAL-BST(root, i, j, last)
>  1. if i == j
>  2.     return
>  3. if last == 0
>  4.     print root[i, j] + "is the root"
>  5. else if j < last
>  6.     print root[i, j] + "is the left child of" + last
>  7. else
>  8.     print root[i, j] + "is the right child of" + last
>  9. CONSTRUCT-OPTIMAL-BST(root, i, root[i, j] - 1, root[i, j])
> 10. CONSTRUCT-OPTIMAL-BST(root, root[i, j] + 1, j, root[i, j])
> ```

> [!proposition]
> There are always roots of optimal subtrees such that `root[i, j - 1] <= root[i, j] <= root[i + 1, j]` for all $1 \leq i < j \leq n$. 

## Longest Simple Path in a Directed Acyclic Graph

> [!definition] Longest Simple Path in a Directed Acyclic Graph
> Suppose that we are given a directed acyclic graph $G = (V, E)$ with real-valued edge weights and two distinguished vertices $s$ and $t$. Find a longest weighted simple path from $s$ to $t$.

> [!pseudocode]
> ```
> LONGEST-PATH-AUX(G, u, t, dist, max)
>  1. if u == t
>  2.     dist[u] = 0
>  3.     return (dist, next)
>  4. else if next[u] >= 0
>  5.     return (dist, next)
>  6. else next[u] = 0
>  7.     for each vertex v in G.Adj[u]
>  8.         (dist, next) = LONGEST-PATH-AUX(G, v, t, dist, next)
>  9.         if w(u, v) + dist[v] > dist[u]
> 10.             dist[u] = w(u, v) + dist[v]
> 11.             next[u] = v
> 12. return (dist, next)
>
> PRINT-PATH(s, t, next)
> 1. u = s
> 2. print u
> 3. while u != t
> 4.     print "🡒" next[u]
> 5.     u = next[u]
> 
> LONGEST-PATH-MAIN(G, s, t)
>  1. n = |G.v|
>  2. let dist[1..n] and next[1..n] be new arrays
>  3. for i = 1 to n
>  4.     dist[i] = -INF
>  5.     next[i] = -1
>  6. (dist, next) = LONGEST-PATH-AUX(G, s, t, dist, next)
>  7. if dist[s] == -INF
>  8.     print "no path exists"
>  9. else print "the weight of the longest path is" dist[s]
> 10.     PRINT-PATH(s, t, next)
> ```

## Bitonic Euclidean Traveling-Salesman Problem

> [!definition] Bitonic Euclidean Traveling-Salesman Problem
> We are given a set of $n$ points in the plane, we wish to find the shortest closed tour that connects all $n$ points.
> We can simplify the problem by restricting our attention to **bitonic tours**, that is, tours that start at the leftmost point, go strictly rightward to the rightmost point, and then go strictly leftward back to the starting point.

> [!pseudocode]
> ```
> EUCLIDEAN-TSP(p)
>  1. sort the points so that (p[1], p[2], p[3], ..., p[n]) are in order of increasing x-coordinate
>  2. let b[1..n, 2..n] and r[1..n - 2, 3..n] be new arrays
>  3. b[1, 2] = DISTANCE(p[1], p[2])
>  4. for j = 3 to n
>  5.     for i = 1 to j - 2
>  6.         b[i, j] = b[i, j - 1] + DISTANCE(p[j - 1], p[j])
>  7.         r[i, j] = j - 1
>  8.     b[j - 1, j] = INF
>  9.     for k = 1 to j - 2
> 10.         q = b[k, j - 1] + DISTANCE(p[k], p[j])
> 11.         if q < b[j - 1, j]
> 12.             b[j - 1, j] = q
> 13.             r[j - 1, j] = k
> 14. b[n, n] = b[n - 1, n] + DISTANCE(p[n - 1], p[n])
> 15. return (b, r)
> 
> PRINT-TOUR(r, n)
> 1. print p[n]
> 2. print p[n - 1]
> 3. k = r[n - 1, n]
> 4. PRINT-PATH(r, k, n - 1)
> 5. print p[k]
> 
> PRINT-PATH(r, i, j)
>  1. if i < j
>  2.     k = r[i, j]
>  3.     if k != i
>  4.         print p[k]
>  5.     if k > 1
>  6.         PRINT-PATH(r, i, k)
>  7. else k = r[j, i]
>  8.     if k > 1
>  9.         PRINT-PATH(r, k, j)
> 10.         print p[k]
> ```
