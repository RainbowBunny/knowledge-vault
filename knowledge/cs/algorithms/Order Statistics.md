## Order Statistics

> [!definition] Order Statistics
> The $i$-th order statistic of a set of $n$ numbers is the $i$-th smallest number in the set.

> [!definition] Selection Problem
> **Input**: A set $A$ of $n$ (distinct) numbers and an integer $i$, with $1 \leq i \leq n$.
> **Output**: The element $x \in A$ that is larger than exactly $i - 1$ other elements of $A$.

### Minimum and Maximum

> [!remark]
> To find minimum and maximum we need $n - 1$ comparisons, however, to find simultaneous minimum and maximum, we can split $n$ elements into pairs, then we find minimum in the smaller group and maximum from the larger group and thus the number of comparisons is at most $\lceil \frac{3n}{2} \rceil - 2$.

> [!pseudocode]
> ```
> MINIMUM(A)
> 1. min = A[1]
> 2. for i = 2 to A.length
> 3.     if min > A[i]
> 4.         min = A[i]
> 5. return min
> ```

### Selection in Expected Linear Time

> [!pseudocode]
> ```
> RANDOMIZED-SELECT(A, p, r, i)
> 1. if p == r
> 2.     return A[p]
> 3. q = RANDOMIZED-PARTITION(A, p, r)
> 4. k = q - p + 1
> 5. if i == k // the pivot value is the answer
> 6.     return A[q]
> 7. else if i < k
> 8.     return RANDOMIZED-SELECT(A, p, q - 1, i)
> 9. else return RANDOMIZED-SELECT(A, q + 1, r, i - k)
> ```

> [!pseudocode]
> ```
> ITERATIVE-RANDOMIZED-SELECT(A, p, r, i)
>  1. while true
>  2.     if p == r
>  3.         return A[p]
>  4.     q = RANDOMIZED-PARTITION(A, p, r)
>  5.     k = q - p + 1
>  6.     if i == k
>  7.         return A[q]
>  8.     if i < k
>  9.         r = q
> 10.     else
> 11.         p = q
> 12.         i = i - k
> ```

### Selection in Worst-case Linear Time
