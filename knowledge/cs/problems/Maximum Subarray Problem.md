## Maximum Subarray Problem

> [!definition] Maximum Subarray Problem
> **Input**: A sequence of $n$ numbers $A = \langle a_1, a_2, \dots, a_n \rangle$.
> **Output**: The nonempty, continuous subarray of $A$ whose values have the largest sum by the format $\langle L, R, sum \rangle$.

### Brute-force Solution

> [!pseudocode]
> ```
> MAXIMUM-SUBARRAY-BRUTE-FORCE(A)
>  1. max-so-far = -INF
>  2. for i = 1 to n
>  3.     sum = 0
>  4.     for j = i to n
>  5.         sum = sum + A[j]
>  6.         if max-so-far < sum
>  7.             max-so-far = sum
>  8.             max-left = i
>  9.             max-right = j
> 10. return (max-left, max-right, max-so-far) 
> ```

### Divide and Conquer Solution

> [!pseudocode]
> ```
>  FIND-MAX-CROSSING-SUBARRAY(A, low, mid, high)
>  1. left-sum = -INF
>  2. for i = mid downto low
>  3.     sum = sum + A[i]
>  4.     if sum > left-sum
>  5.         left-sum = sum
>  6.         max-left = i
>  7. right-sum = -INF
>  8. sum = 0
>  9. for j = mid + 1 to high
> 10.     sum = sum + A[j]
> 11.     if sum > right-sum
> 12.         right-sum = sum
> 13.         max-right = j
> 14. return (max-left, max-right, left-sum + right-sum)
> ```

> [!pseudocode]
> ```
> FIND-MAXIMUM-SUBARRAY(A, low, high)
>  1. if high == low
>  2.     return (low, high, A[low]) // base case: only one element
>  3. else mid = FLOOR((low + high) / 2)
>  4.     (left-low, left-high, left-sum) = 
>  5.         FIND-MAXIMUM-SUBARRAY(A, low, mid)
>  6.     (right-low, right-high, right-sum) =
>  7.         FIND-MAXIMUM-SUBARRAY(A, mid + 1, high)
>  8.     (cross-low, cross-high, cross-sum) =
>  9.         FIND-MAX-CROSSING-SUBARRAY(A, low, mid, high)
> 10.     if left-sum >= right-sum and left-sum >= cross-sum
> 11.         return (left-low, left-high, left-sum)
> 12.     elseif right-sum >= left-sum and right-sum >= cross-sum
> 13.         return (right-low, right-high, right-sum)
> 14.     else return (cross-low, cross-high, cross-sum)
> ```

### Linear Solution

> [!pseudocode]
> ```
> MAXIMUM-SUBARRAY-LINEAR(A)
>  1. max-sum = -INF
>  2. ending-here-sum = -INF
>  3. for j = 1 to A.length
>  4.     ending-here-high = j
>  5.     if ending-here-sum > 0
>  6.         ending-here-sum = ending-here-sum + A[j]
>  7.     else ending-here-low = j
>  8.         ending-here-sum = A[j]
>  9.     if ending-here-sum > max-sum
> 10.         max-sum = ending-here-sum
> 11.         low = ending-here-low
> 12.         high = ending-here-high
> 13. return (low, high, max-sum)
> ```
