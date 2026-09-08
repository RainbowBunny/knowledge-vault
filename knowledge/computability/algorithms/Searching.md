## Searching Problem

> [!definition] Searching Problem
> **Input**: A sequence of $n$ numbers $A = \langle a_1, a_2, \dots, a_n \rangle$ and a value $v$.
> **Output**: An index $i$ such that $v = A[i]$ or the special value `NIL` if $v$ does not appear in $A$.

### Linear Search

> [!pseudocode] Linear Search
> ```
> LINEAR-SEARCH(A, v)
> 1. for i = 1 to A.length
> 2.     if A[i] == v
> 3.         return i
> 4. return NIL
> ```

### Binary Search

> [!pseudocode]
> ```
> BINARY-SEARCH(A, v)
>  1. low = 1
>  2. high = A.length
>  3. while low <= high:
>  4.     mid = FLOOR((low + high) / 2)
>  5.     if a[mid] == v
>  6.         return mid
>  7.     else if a[mid] < v
>  8.         low = mid + 1
>  9.     else
> 10.         high = mid - 1
> ```
