## Longest Common Subsequence

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

## Longest Palindrome Subsequence

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
