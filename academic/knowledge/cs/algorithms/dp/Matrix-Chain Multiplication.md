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
