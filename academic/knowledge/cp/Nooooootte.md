
> [!definition] In Place
> An algorithm is **in place** if only a constant number of elements of the input array are ever sorted outside the array.

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

> [!definition] Adding two $n$-bit binary integers
> **Input**: Two sequences of $n$-bit binary integers $A = \langle a_1, a_2, \dots, a_n \rangle$ and $B = \langle b_1, b_2, \dots, b_n \rangle$.
> **Output**: The sum of the two integers stored in binary form in an $(n + 1)$-element array $C = \langle c_1, c_2, \dots, c_{n + 1} \rangle$.

## Polynomial

> [!definition] Horner's Rule
> For a polynomial $P(x) = \sum_{k = 0}^n a_k x^k$, given the coefficients $a_0, a_1, \dots, a_n$ and a value $x$: $$P(x) = a_0 + x(a_1 + x(a_2 + \cdots + x(a_{n - 1} + x a_n)\cdots)),$$ and thus we can calculate this by the code segment:
> ```
> 1. y = 0
> 2. for i = n downto 0
> 3.     y = ai + x * y
> ```

## Inversion

> [!definition] Inversions
> Let `A[1..n]` be an array of $n$ distinct numbers. If `i < j` and `A[i] > A[j]`, then the pair `(i, j)` is called an **inversion** of `A`.

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

## Matrix Multiplication

> [!definition] Square Matrix Multiplication
> **Input**: Two $n \times n$ square matrices $A = (a_{i, j})$ and $B = (b_{i, j})$ 
> **Output**: The product $C = A \cdot B$, with each entry $c_{i, j} = \sum_{k = 1}^n a_{i, k} \cdot b_{k, j}$

> [!pseudocode]
> ```
> SQUARE-MATRIX-MULTIPLY(A, B)
> 1. n = A.rows
> 2. let C be a new n * n matrix
> 3. for i = 1 to n
> 4.     for j = 1 to n
> 5.         c[i][j] = 0
> 6.         for k = 1 to n
> 7.             c[i][j] = c[i][j] + a[i][k] * b[k][j]
> 8. return C
> ```

### Strassen's Algorithm

> [!proposition]
> Partition:
> $$A = \begin{pmatrix}A_{1,1} & A_{1,2} \\ A_{2, 1} & A_{2, 2}\end{pmatrix}, \quad B = \begin{pmatrix}B_{1,1} & B_{1,2} \\ B_{2, 1} & B_{2, 2}\end{pmatrix}, \quad C = \begin{pmatrix}C_{1,1} & C_{1,2} \\ C_{2, 1} & C_{2, 2}\end{pmatrix}$$

> [!pseudocode]
> ```
> SQUARE-MATRIX-MULTIPLY-RECURSIVE(A, B)
>  1. n = A.rows
>  2. let C be a new n * n matrix
>  3. if n == 1
>  4.     return c[1][1] = a[1][1] * b[1][1]
>  5. else partition A, B, and C 
>  6.     C[1][1] = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[1][1], B[1][1])
>                 + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[1][2], B[2][1])
>  7.     C[1][2] = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[1][1], B[1][2])
>                 + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[1][2], B[2][2])
>  8.     C[2][1] = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[2][1], B[1][1])
>                 + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[2][2], B[2][1])
>  9.     C[2][2] = SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[2][1], B[1][2])
>                 + SQUARE-MATRIX-MULTIPLY-RECURSIVE(A[2][2], B[2][2])
> 10. return C
> ```

> [!pseudocode]
> ```
> STRASSEN(A, B)
>  1. n = A.rows
>  2. let C be a new n * n matrix
>  3. if n == 1
>  4.     return c[1][1] = a[1][1] * b[1][1]
>  5. else partition A, B, and C
>  6.     M[1] = STRASSEN(A[1][1] + A[2][2], B[1][1] + B[2][2])
>  7.     M[2] = STRASSEN(A[2][1] + A[2][2], B[1][1])
>  8.     M[3] = STRASSEN(A[1][1], B[1][2] - B[2][2])
>  9.     M[4] = STRASSEN(A[2][2], B[2][1] - B[1][1])
> 10.     M[5] = STRASSEN(A[1][1] + A[1][2], B[2][2])
> 11.     M[6] = STRASSEN(A[2][1] - A[1][1], B[1][1] + B[1][2])
> 12.     M[7] = STRASSEN(A[1][2] - A[2][2], B[2][1] + B[2][2])
> 13.     C[1][1] = M[1] + M[4] - M[5] + M[7]
> 14.     C[1][2] = M[3] + M[5]
> 15.     C[2][1] = M[2] + M[4]
> 16.     C[2][2] = M[1] - M[2] + M[3] + M[6]
> 17. return C
> ```

## Multiplying Complex Numbers

> [!definition] Multiplying Complex Numbers
> **Input**: Two complex numbers $\langle a, b \rangle$ and $\langle c, d \rangle$.
> **Output**: The multiplication of two complex numbers $\langle ac - bd, ad + bc \rangle$

> [!proposition] Idea
> Calculate $M_1 = ac, M_2 = bd, M_3 = (a + b)(c + d)$, then:
> **Real Part**: $ac - bd = M_1 - M_2$.
> **Imaginary Part**: $ad + bc = M_3 - M_1 - M_2$.

## Monge Arrays

> [!definition] Monge Array
> An $m \times n$ array $A$ of real numbers is a **Monge array** if for all $i, j, k$ and $l$ such that $1 \leq i < k \leq m$ and $1 \leq j < l \leq n$, we have $$A[i, j] + A[k, l] \leq A[i, l] + A[k, j].$$

> [!proposition]
> 1. An array is Monge if and only if for all $i = 1, 2, \dots, m - 1$ and $j = 1, 2, \dots, n - 1$, we have $$A[i, j] + A[i + 1, j + 1] \leq A[i, j + 1] + A[i + 1, j].$$
> 2. Let $f(i)$ be the index of column containing the leftmost minimum element of row $i$, then $f(1) \leq f(2) \leq \cdots \leq f(m)$ for any $m \times n$ Monge array.

## The hiring problem

> [!pseudocode]
> ```
> HIRE-ASSISTANT(n)
> 1. best = 0
> 2. for i = 1 to n
> 3.     interview candidate i
> 4.     if candidate i is better than candidate best
> 5.         best = i
> 6.         hire candidate i
> ```

> [!lemma]
> Assuming that the candidates are presented in a random order, algorithm `HIRE-ASSISTANT` has an average-case total hiring cost of $O(c_h \ln n)$

> [!pseudocode]
> ```
> RANDOMIZED-HIRE-ASSISTANT(n)
> 1. randomly permute the list of candidates
> 2. best = 0 // candidate 0 is a least-qualified dummy candidate
> 3. for i = 1 to n
> 4.     interview candidate i
> 5.     if candidate i is better than candidate best
> 6.         best = i
> 7.         hire candidate i
> ```

> [!lemma]
> The expected hiring cost of the procedure `RANDOMIZED-HIRE-ASSISTANT` is $O(c_h \ln n)$

### Online Version

> [!definition] On-line hiring problem
> Suppose now that we do not wish to interview all the candidates in order to find the best one. We also do not wish to hire and fire as we find better and better applicants. Instead, we are willing to settle for a candidate who is close to the best, in exchange for hiring exactly once. We must obey one company requirement: after each interview we must either immediately offer the position to the applicant or immediately reject the applicant. What is the trade-off between minimizing the amount of interviewing and maximizing the quality of the candidate hired?

> [!pseudocode]
> ```
> ON-LINE-MAXIMUM(k, n)
> 1. for i = 1 to k
> 2.     if score(i) > bestscore
> 3.         bestscore = score(i)
> 4. for i = k + 1 to n
> 5.     if score(i) > bestscore
> 6.         return i
> 7. return n
> ```

> [!remark]
> The strategy works best when $k = \frac{n}{e}$

## Random Algorithm

> [!pseudocode]
> ```
RANDOM(a, b)
>1. if a == b
>2.     return a
>3. r = RANDOM(0, 1)
>4. if r == 0
>5.     return RANDOM(a, FLOOR((a + b) / 2)))
>6. else return RANDOM(CEIL((a + b) / 2), b)   
>```

> [!pseudocode]
> ```
> UNBIASED-RANDOM()
> 1. while TRUE
> 2.     x = BIASED-RANDOM()
> 3.     y = BIASED-RANDOM()
> 4.     if x != y
> 5.         return x
> ```

### Permutation

> [!pseudocode]
> ```
> PERMUTE-BY-SORTING(A)
> 1. n = A.length
> 2. let P[1..n] be a new array
> 3. for i = 1 to n
> 4.     P[i] = RANDOM(1, n ** 3)
> 5. sort A, using P as sort keys
> ```

> [!lemma]
> Procedure `PERMUTE-BY-SORTING` produces a uniform random permutation of the input, assuming that all priorities are distinct.

> [!pseudocode]
> ```
> RANDOMIZE-IN-PLACE(A)
> 1. n = A.length
> 2. for i = 1 to n
> 3.     swap A[i] with A[RANDOM(i, n)]
> ```

> [!lemma]
> Procedure `RANDOMIZE-IN-PLACE` computes a uniform random permutation.

### Subset of Permutation

> [!pseudocode]
> ```
> RANDOM-SAMPLE(m, n)
> 1. if m == 0
> 2.     return EMPTYSET
> 3. else S = RANDOM-SAMPLE(m - 1, n - 1)
> 4.     i = RANDOM(1, n)
> 5.     if i in S
> 6.         S = UNION(S, {n})
> 7.     else S = UNION(S, {i})
> 8.     return S
> ```

## Memory

> [!pseudocode]
> ```
> ALLOCATE-OBJECT()
> 1. if free == NIL
> 2.     error "out of space"
> 3. else x = free
> 4.     free = x.next
> 5.     return x
> 
> FREE-OBJECT(x)
> 1. x.next = free
> 2. free = x
> ```

> [!pseudocode]
> ```
> ALLOCATE-OBJECT()
> 1. if free == NIL
> 2.     error "out of space"
> 3. else x = free
> 4.     free = A[x + 1]
> 5.     return x
> 
> FREE-OBJECT(x)
> 1. A[x + 1] = free
> 2. free = x
> ```

## Amortized Analysis

### Aggregate Analysis

> [!definition] Aggregate Analysis
> In **aggregate analysis**, we show that for all $n$, a sequence of $n$ operations takes wort-case time $T(n)$ in total. In the worst case, the average cost, or **amortized cost**, per operation is therefore $T(n) / n$.

### Accounting Method

> [!definition] Accounting Method
> In the **accounting method** of amortized analysis, we assign differing charges to different operations, with some operations charged more or less than they actually cost. We call the amount we charge an operation its **amortized cost**. When an operation's amortized cost exceeds its actual cost, we assign the difference to specific objects in the data structure as **credit**. Credit can help pay for later operations whose amortized cost is less than their actual cost.

> [!example]
> Increasing a $n$-bit binary number $k$ times, the cost of setting a bit is $2$ dollars. We first begin with the cost is the number of set bits and each operation will set $1$ bit from $0$ to $1$ and thus total cost is $O(n)$. The idea is that $2$ dollars cost here is for setting the bit $1$ and at some point we will set it back to $0$.

### Potential Method

> [!definition] Potential Method
> Assign potential score for each state of the structures, and thus we can calculate the amortized cost by analyzing the different potential score of two states and the actual cost of the action. Thus, if we have the potential score always increases then.


