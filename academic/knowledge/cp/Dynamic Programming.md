
## Element of Dynamic Programming

> [!remark]
> When developing a dynamic-programming algorithm, we follow a sequence of four steps:
> 1. Characterize the structure of an optimal solution.
> 2. Recursively define the value of an optimal solution.
> 3. Compute the value of an optimal solution, typically in a bottom-up fashion.
> 4. Construct an optimal solution from computed information.

> [!definition] Optimal Substructure
> A problem exhibits **optimal substructure** if an optimal solution to the problem contains within it optimal solutions to subproblems.

> [!remark]
> Common pattern in discovering optimal substructure:
> 1. Show that a solution to the problem consists of making a choice. Making this choice leaves one or more subproblems to be solved.
> 2. Suppose that for a given problem, you are given the choice that leads to an optimal solution. You do not concern yourself yet with how to determine this choice. You just assume that it has been given to you.
> 3. Given this choice, you determine which subproblems ensue and how to best characterize the resulting space of subproblems.
> 4. Show that the solutions to the subproblems used within an optimal solution to the problem must themselves be optimal by using a "cut-and-paste" technique. You do so by supposing that each of the subproblem solutions is not optimal and then deriving a contradiction.

> [!remark]
> Optimal substructure varies across problem domain in two ways:
> 1. How many subproblems an optimal solution to the original problem used, and
> 2. How many choices we have in determining which subproblem(s) to use in an optimal solution.

> [!definition] Overlapping Subproblems
> When a recursive algorithm revisits the same problem repeatedly, we say that the optimization problem has **overlapping subproblems**.

> [!remark] Reconstructing an optimal solution 
> As a practical matter, we often store which choice we made in each subproblem in a table so that we do not have to reconstruct this information from the costs that we stored.

## Rod cutting

> [!definition] Rod-cutting Problem
> Given a rod of length $n$ inches and a table of prices $p_i$ for $i = 1, 2, \dots, n$, determine the maximum revenue $r_n$ obtainable by cutting the rod and selling the pieces.

> [!pseudocode]
> ```
> MEMOIZED-CUR-ROD-AUX(p, n, r)
>  1. if r[n] >= 0
>  2.     return r[n]
>  3. if n == 0
>  4.     q = 0
>  5. else q = -INF
>  6.     for i = 1 to n
>  7.         (val, s) = MEMOIZED-CUT-ROD-AUX(p, n - i, r, s)
>  8.         if q < p[i] + val
>  9.             q = p[i] + val
> 10.             s[n] = i
> 11. r[n] = q
> 12. return (q, s)
> 
> MEMOIZED-CUT-ROD(p, n)
> 1. let r[0..n] and s[0..n] be new arrays
> 2. for i = 0 to n
> 3.     r[i] = -INF
> 4. (val, s) = MEMOIZED-CUT-ROD-AUX(p, n, r, s)
> 5. print "The optimal value is" val "and the cuts are at"
> 6. j = n
> 7. while j > 0
> 8.     print s[j]
> 9.     j = j - s[j]
> ```

> [!pseudocode]
> ```
> BOTTOM-UP-CUT-ROD(p, n)
> 1. let r[0..n] be a new array
> 2. r[0] = 0
> 3. for j = 1 to n
> 4.     q = -INF
> 5.     for i = 1 to j
> 6.         q = max(q, p[i] + r[j - i])
> 7.     r[j] = q
> 8. return r[n]
> ```

> [!pseudocode]
> ```
> EXTENDED-BOTTOM-UP-CUT-ROD(p, n)
>  1. let r[0..n] and s[0..n] be new arrays
>  2. r[0] = 0
>  3. for j = 1 to n
>  4.     q = -INF
>  5.     for i = 1 to j
>  6.         if q < p[i] + r[j - i]
>  7.             q = p[i] + r[j - i]
>  8.             s[j] = i
>  9.     r[j] = q
> 10. return r and s
> 
> PRINT-CUT-ROD-SOLUTION(p, n)
> 1. (r, s) = EXTENDED-BOTTOM-UP-CUT-ROD(p, n)
> 2. while n > 0
> 3.     print s[n]
> 4.     n = n - s[n]
> ```

## Fibonacci

> [!pseudocode]
> ```
> FIBONACCI(n)
> 1. let fib[0..n] be a new array
> 2. fib[0] = fib[1] = 1
> 3. for i = 2 to n
> 4.     fib[i] = fib[i - 1] + fib[i - 2]
> 5. return fib[n]
> ```

## Knapsack Problem

> [!definition] 0-1 Knapsack Problem
> A thief robbing a store finds $n$ items. The $i$th item is worth $v_i$ dollars and weighs $w_i$ pounds, where $v_i$ and $w_i$ are integers. The thief wants to take as valuable a load as possible, but he can carry at most $W$ pounds in his knapsack, for some integer $W$. Which item should he take.

> [!pseudocode]
> ```
>  1. DYNAMIC-0-1-KNAPSACK(v, w, n, W)
>  2. let c[0..n, 0..W] be new array
>  3. for w = 0 to W
>  4.     c[0, w] = 0
>  5. for i = 1 to n
>  6.     c[i, 0] = 0
>  7.     for w = 1 to W
>  8.         c[i, w] = c[i - 1, w]
>  9.         if w >= w[i]
> 10.            c[i, w] = MAX(c[i, w], c[i - 1, w - w[i]] + v[i])
> ```

> [!remark]
> Algorithm run in $O(nw)$. 
> `c[i, w]` means using the first $i$ item and total weight is $w$.

> [!remark]
> When 

### Fractional Variant

> [!definition] Fractional Knapsack Problem
> The setup is the same but instead of choosing items, the thief can have fractions of items.

> [!remark]
> A greedy solution that sort items by $\frac{v}{w}$ works.

> [!proposition] $O(n)$ Solution
> Use $k$-th order statistic to get median $m$ of $\frac{v}{w}$, then partition into three groups: $G = \{i: \frac{v_i}{w_i} > m\}$, $E = \{i: \frac{v_i}{w_i} = M\}$, $L = \{i: \frac{v_i}{w_i} < m\}$. Then we can calculate $W_G = \sum_{i \in G} w_i$ and $W_E = \sum_{i \in E}$.
> - If $W_G > W$ then recursively solve with $(G, W)$.
> - Otherwise, take all item of $G$ and as much $E$ as possible:
> 	- If $W_G + W_E \geq W$ then done.
> 	- Else solve with $(L, W - W_G - W_E)$.
> 
> Complexity: $T(n) \leq T(n / 2) + \mathcal O(n)$.

### Coin Changing

> [!definition] Coin Changing
> Consider the problem of making change for $n$ cents using the fewest number of coins. Assume that each coin's value is an integer.
> **Input**:
> - $n$ cents.
> - $d_1, d_2, \cdots, d_k$ is the coin denominations.

> [!pseudocode]
> ```
> COMPUTE-CHANGE(n, d, k)
> 1. let c[1..n] and denom[1..n] be new arrays
> 2. for j = 1 to n
> 3.     c[j] = INF
> 4.     for i = 1 to k
> 5.         if j >= d[i] and 1 + c[j - d[i]] < c[j]
> 6.             c[j] = 1 + c[j - d[i]]
> 7.             denom[j] = d[i]
> 8. return (c, denom)
> ```

> [!remark]
> Greedy solution will work if when in ascending order, $d_{i} | d_{i + 1}$.

## Matrix-Chain Multiplication

> [!definition] Matrix-chain Multiplication Problem
> Given a chain $\langle A_1, A_2, \dots, A_n \rangle$ of $n$ matrices, where for $i = 1, 2, \dots, n$, matrix $A_i$ has dimension $p_{i - 1} \times p_i$, fully parenthesize the product $A_1 A_2 \cdots A_n$ in a way that minimizes the number of scalar multiplications.

> [!pseudocode]
> ```
> MATRIX-CHAIN-ORDER(p)
>  1. n = p.length - 1
>  2. let m[1..n, 1..n] and s[1..n - 1, 2..n] be new tables
>  3. for i = 1 to n
>  4.     m[i, i] = 0
>  5. for l = 2 to n
>  6.     for i = 1 to n - l + 1
>  7.         j = i - l + 1
>  8.         m[i, j] = INF
>  9.         for k = i to j - 1
> 10.             q = m[i, k] + m[k + 1, j] + p[i - 1] * p[k] * p[j]
> 11.             if q < m[i, j]
> 12.                 m[i, j] = q
> 13.                 s[i, j] = k
> 14. return (m, s)
> ```

> [!pseudocode]
> ```
> PRINT-OPTIMAL-PARENS(s, i, j)
> 1. if i == j
> 2.     print "A"
> 3. else print "("
> 4.      PRINT-OPTIMAL-PARENS(s, i, s[i, j])
> 5.      PRINT-OPTIMAL-PARENS(s, s[i, j] + 1, j)
> 6.      print ")"
> ```

> [!pseudocode]
> ```
> MATRIX-CHAIN-MULTIPLY(A, s, i, j)
> 1. if i == j
> 2.     return A[i]
> 3. if i + 1 == j
> 4.     return A[i] * A[j]
> 5. b = MATRIX-CHAIN-MULTIPLY(A, s, i, s[i, j])
> 6. c = MATRIX-CHAIN-MULTIPLY(A, s, s[i, j] + 1, j)
> 7. return b * c
> ```

> [!pseudocode]
> ```
> MEMOIZED-MATRIX-CHAIN(p)
> 1. n = p.length - 1
> 2. let m[1..n, 1..n] be a new table
> 3. for i = 1 to n
> 4.     for j = i to n
> 5.         m[i, j] = INF
> 6. return LOOKUP-CHAIN(m, p, 1, n)
> 
> LOOKUP-CHAIN(m, p, i, j)
> 1. if m[i, j] < INF
> 2.     return m[i, j]
> 3. if i == j
> 4.     m[i, j] = 0
> 5. else for k = i to j - 1
> 6.     q = LOOKUP-CHAIN(m, p, i, k) + LOOKUP-CHAIN(m, p, k + 1, j) + p[i - 1] * p[k] * p[j]
> 7.     if q < m[i, j]
> 8.         m[i, j] = q
> 9. return m[i, j]
> ```

## String

### Printing Neatly

> [!definition] Printing Neatly
> Consider the problem of neatly printing a paragraph with a monospaced font (all characters having the same width) on a printer. The input text is a sequence of $n$ words of length $l_1, l_2, \dots, l_n$, measured in characters. We want to print this paragraph neatly on a number of lines that hold a maximum of $M$ characters each. Our criterion of "neatness" is as follows. If a given line contains words $i$ through $j$, where $i \leq j$, and we leave exactly one space between words, the number of extra space characters at the end of the line is $M - j + i - \sum_{k = i}^j l_k$, which must be nonnegative so that the words fit on the line. We wish to minimize the sum, over all lines except the last, of the cubes of the numbers of extra space characters at the ends of lines. Give a dynamic-programming algorithm to print a paragraph of $n$ words neatly on a printer.

> [!pseudocode]
> ```
> PRINT-NEATLY(l, n, M)
>  1. let extras[1..n, 1..n], lc[1..n, 1..n], and c[0..n] be new arrays
>  2. for i = 1 to n
>  3.     extras[i, j] = M - l[i]
>  4.     for j = i + 1 to n
>  5.         extras[i, j] = extras[i, j - 1] - l[j] - 1
>  6. for i = 1 to n
>  7.     for j = i to n
>  8.         if extras[i, j] < 0
>  9.             lc[i, j] = INF
> 10.         else if j == n and extras[i, j] >= 0
> 11.             lc[i, j] = 0
> 12.         else lc[i, j] = (extras[i, j]) ** 3
> 13. c[0] = 0
> 14. for j = 1 to n
> 15.     c[j] = INF
> 16.     for i = 1 to j
> 17.         if c[i - 1] + lc[i, j] < c[i]
> 18.             c[j] = c[i - 1] + lc[i, j]
> 19.             p[j] = i
> 20. return (c, p)
> 
> GIVE-LINES(p, j)
> 1. i = p[j]
> 2. if i == 1
> 3.     k = 1
> 4. else k = GIVE-LINES(p, i - 1) + 1
> 5. print (k, i, j)
> 6. return k
> ```

### Edit Distance



## Subsequence
### Longest Common Subsequence

> [!theorem] Optimal Substructure of an LCS
> Let $X = \langle x_1, x_2, \dots, x_m \rangle$ and $Y = \langle y_1, y_2, \dots, y_n \rangle$ be sequences, and let $Z = \langle z_1, z_2, \dots, z_k \rangle$ be any LCS of $X$ and $Y$.
> 1. If $x_m = y_n$, then $z_k = x_m = y_n$ and $Z_{k - 1}$ is an LCS of $X_{m - 1}$ and $Y_{n - 1}$.
> 2. If $x_m \neq y_n$, then $z_k \neq x_m$ implies that $Z$ is an LCS of $X_{m - 1}$ and $Y$.
> 3. If $x_m \neq y_n$, then $z_k \neq y_n$ implies that $Z$ is an LCS of $X$ and $Y_{n - 1}$.

> [!pseudocode]
> ```
> LCS-LENGTH(X, Y)
>  1. m = X.length
>  2. n = Y.length
>  3. let b[1..m, 1..n] and c[0..m, 0..n] be new tables
>  4. for i = 1 to m
>  5.     c[i, 0] = 0
>  6. for j = 0 to n
>  7.     c[0, j] = 0
>  8. for i = 1 to m
>  9.     for j = 1 to n
> 10.         if x[i] == y[j]
> 11.             c[i, j] = c[i - 1, j - 1] + 1
> 12.             b[i, j] = "🡔"
> 13.         else if c[i - 1, j] >= c[i, j - 1]
> 14.             c[i, j] = c[i - 1, j]
> 15.             b[i, j] = "🡑"
> 16.         else c[i, j] = c[i, j - 1]
> 17.             b[i, j] = "🡐"
> 18. return (c, b)
> ```

> [!pseudocode]
> ```
> PRINT-LCS(b, X, i, j)
> 1. if i == 0 or j == 0
> 2.     return
> 3. if b[i, j] == "🡔"
> 4.     PRINT-LCS(b, X, i - 1, j - 1)
> 5.     print X[i]
> 6. else if b[i, j] == "🡑"
> 7.     PRINT-LCS(b, X, i - 1, j)
> 8. else PRINT-LCS(b, X, i, j - 1)
> 
> PRINT-LCS'(c, X, Y, i, j)
> 1. if c[i, j] == 0
> 2.     return
> 3. if X[i] == Y[j]
> 4.     PRINT-LCS'(c, X, Y, i - 1, j - 1)
> 5.     print X[i]
> 6. else if c[i - 1, j] > c[i, j - 1]
> 7.     PRINT-LCS'(c, X, Y, i - 1, j)
> 8. else
> 9.     PRINT-LCS'(c, X, Y, i, j - 1)
> ```

> [!pseudocode]
> ```
> MEMOIZED-LCS-LENGTH(X, Y, i, j)
> 1. if c[i, j] > -1
> 2.     return c[i, j]
> 3. if i == 0 or j == 0
> 4.     return c[i, j] = 0
> 5. if X[i] == Y[j]
> 6.     return c[i, j] = MEMOIZED-LCS-LENGTH(X, Y, i - 1, j - 1) + 1
> 7. return c[i, j] = max(MEMOIZED-LCS-LENGTH(X, Y, i - 1, j), MEMOIZED-LCS-LENGTH(X, Y, i, j - 1))
> ```

> [!pseudocode]
> ```
> LONG-MONOTONIC(S)
>  1. let B[1..n] be a new array where every value = INF
>  2. let C[1..n] be a new array
>  3. L = 1
>  4. for i = 1 to n
>  5.     if A[i] < B[i]
>  6.         B[1] = A[i]
>  7.     else
>  8.         let j be the largest index of B such that B[j] < A[i]
>  9.         B[j + 1] = A[i]
> 10.         C[j + 1] = C[j]
> 11.         INSERT(C[j + 1], A[i])
> 12.         if j + 1 > L
> 13.             L = L + 1
> 14. print C[L]
> ```

### Longest Palindrome Subsequence

> [!pseudocode]
> ```
> LONGEST-PALINDROME(X)
>  1. n = X.length
>  2. let b[1..n, 1..n] and p[0..n, 0..n] be new tables
>  3. for i = 1 to n - 1
>  4.     p[i, i] = 1
>  5.     j = i + 1
>  6.     if x[i] == x[j]
>  7.         p[i, j] = 2
>  8.         b[i, j] = "🡗"
>  9.     else p[i, j] = 1
> 10.         b[i, j] = "🡓"
> 11. p[n, n] = 1
> 12. for i = n - 2 downto 1
> 13.     for j = i + 2 to n
> 14.         if x[i] == x[j]
> 15.             p[i, j] = p[i + 1, j - 1] + 2
> 16.             b[i, j] = "🡗"
> 17.         else if p[i + 1, j] >= p[i, j - 1]
> 18.             p[i, j] = p[i + 1, j]
> 19.             b[i, j] = "🡓"
> 20.         else p[i, j] = p[i, j - 1]
> 21.             b[i, j] = "🡐"
> 22. return (p, b)
> 
> GENERATE-LPS(b, X, i, j, S)
> 1. if i > j
> 2.     return S
> 3. else if i == j
> 4.     return S || X[i]
> 5. else if b[i, j] == "🡗"
> 6.     return x[i] || GENERATE-LPS(b, X, i + 1, j - 1, S) || x[i]
> 7. else if b[i, j] == "🡓"
> 8.     return GENERATE-LPS(b, X, i + 1, j, S)
> 9. return GENERATE-LPS(b, X, i, j - 1, S)
> ```

## Graph

### Optimal Binary Search Trees

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

### Longest Simple Path in a Directed Acyclic Graph

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

### Bitonic Euclidean Traveling-Salesman Problem

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
