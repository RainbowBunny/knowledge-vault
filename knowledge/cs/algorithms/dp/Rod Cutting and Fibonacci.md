## Rod Cutting

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
