## Priority Queues

> [!algorithm] Priority Queue
> A **priority queue** is a data structure for maintaining a set $S$ of elements, each with an associated value called a **key**. A **max-priority queue** supports the following operations:
> - `INSERT(S, x)` inserts the element $x$ into the set $S$, which is equivalent to the operations $S = S \cup \{x\}$.
> - `MAXIMUM(S)` returns the elements of $S$ with the largest key.
> - `EXTRACT-MAX(S)` removes and returns the element of $S$ with the largest key.
> - `INCREASE-KEY(S, x, k)` increases the value of element $x$'s key to the new value $k$, which is assumed to be at least as large as $x$'s current key value.
> 
> Alternatively, a **min-priority queue** supports the operations `INSERT`, `MINIMUM`, `EXTRACT-MIN` and `DECREASE-KEY`.

### Heap Implementation

> [!pseudocode]
> ```
> HEAP-MAXIMUM(A)
> 1. return A[1]
> 
> HEAP-EXTRACT-MAX(A)
> 1. if A.heap-size < 1
> 2.     error "heap underflow"
> 3. max = A[1]
> 4. A[1] = A[A.heap-size]
> 5. A.heap-size = A.heap-size - 1
> 6. MAX-HEAPIFY(A, 1)
> 7. return max
> 
> HEAP-INCREASE-KEY(A, i, key)
> 1. if key < A[i]
> 2.     error "new key is smaller than current key"
> 3. while i > 1 and A[PARENT(i)] < A[i]
> 4.     A[i] = A[PARENT(i)]
> 5.     i = PARENT(i)
> 6. A[i] = key
> 
> MAX-HEAP-INSERT(A, key)
> 1. A.heap-size = A.heap-size + 1
> 2. A[A.heap-size] = -INF
> 3. HEAP-INCREASE-KEY(A, A.heap-size, key)
> 
> HEAP-DELETE(A, i)
> 1. A[i] = A[A.heap-size]
> 2. MAX-HEAPIFY(A, i)
> 3. A.heap-size = A.heap-size - 1
> ```
