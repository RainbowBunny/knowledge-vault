## Heap

### Binary Version

> [!definition] Heap
> The **(binary) heap** data structure is an array object that we can view as a nearly complete binary tree.

> [!pseudocode]
> ```
> PARENT(i)
> 1. return FLOOR(i / 2)
> 
> LEFT(i)
> 1. return 2 * i
> 
> RIGHT(i)
> 1. return 2 * i + 1
> ```

> [!definition] Heap Property
> The values in the nodes of each kinds of binary heaps satisfy a **heap property**.
> In a **max-heap**, the **max-heap property** is that for every node $i$ other than the root,
> `A[PARENT(i)] >= A[i]`,
> that is, the value of a node is at most the value of its parent. Thus, the largest element in a max-heap is stored at the root, and the subtree rooted at a node contains values no larger than that contained at the node itself. A **min-heap** is organized in the opposite way; the **min-heap property** is that for every node $i$ other than the root,
> `A[PARENT(i)] <= A[i]`.
> The smallest element in a min-heap is at the root.

> [!definition] Height
> Viewing a heap as a tree, we define the **height** of a node in a heap to be the number of edges on the longest simple downward path from the node to a leaf, and we define the height of the heap to be the height of its root.

> [!proposition]
> 1. A heap of height $h$ has at most $2^{h + 1} - 1$ elements and at least $2^h$ elements. Thus, an $n$-element heap has height $\lfloor \log n \rfloor$.
> 2. There are at most $\lceil \frac{n}{2^{h + 1}} \rceil$ nodes of height $h$ in any $n$-element heap.
> 3. The elements in the subarray `A[(FLOOR(n / 2) + 1)..n]`are all leaves of the tree.

> [!pseudocode]
> ```
> MAX-HEAPIFY(A, i)
>  1. l = LEFT(i)
>  2. r = RIGHT(i)
>  3. if l <= A.heap-size and A[l] > A[i]
>  4.     largest = l
>  5. else largest = i
>  6. if r <= A.heap-size and A[r] > A[largest]
>  7.     largest = r
>  8. if largest != i
>  9.     exchange A[i] with A[largest]
> 10.     MAX-HEAPIFY(A, largest)
> ```

> [!pseudocode]
> ```
> BUILD-MAX-HEAP(A)
> 1. A.heap-size = A.length
> 2. for i = FLOOR(A.length / 2) downto 1
> 3.     MAX-HEAPIFY(A, i)
> 
> BUILD-MAX-HEAP'(A)
> 1. A.heap-size = 1
> 2. for i = 2 to A.length
> 3.     MAX-HEAP-INSERT(A, A[i])
> ```

### $d$-ary Version

> [!pseudocode]
> ```
> d-ARY-PARENT(i)
> 1. return FLOOR((i - 2) / d + 1)
> 
> d-ARY-CHILD(i, j)
> 1. return d(i - 1) + j + 1
> ```

> [!pseudocode]
> ```
> MAX-HEAPIFY(A, i)
> 1. largest = i
> 2. for i from 1 to d
> 3.     current-child = d-ARY-CHILD(i, j)
> 4.     if A[current-child] > A[largest]
> 5.         largest = current-child
> 6. if largest != i
> 7.     exchange A[i] with A[largest]
> 8.     MAX-HEAPIFY(A, largest)
> ```

### Mergeable Heaps

> [!algorithm] Mergeable Heap
> A **mergeable heap** is any data structure that supports the following five operations, in which each element has a key:
> - `MAKE-HEAP()`: creates and returns a new heap containing no elements.
> - `INSERT(H, x)`: inserts element $x$, whose $key$ has already been filled in, into heap $H$.
> - `MINIMUM(H)`: returns a pointer to the element in the heap $H$ whose key is minimum.
> - `EXTRACT-MEAN(H)`: deletes the element from heap $H$ whose key is minimum, returning a pointer to the element.
> - `UNION(H1, H2)`: creates and returns a new heap that contains all the elements of heaps $H_1$ and $H_2$. Heaps $H_1$ and $H_2$ are "destroyed" by this operation.
> - `DECREASE-KEY(H, x, k)`: assigns to element $x$ within heap $H$ the new key value $k$, which we assume to be no greater than its current key value.
> - `DELETE(H, x)`: deletes element $x$ from heap $H$.

### Young Tableaus

> [!definition] Young Tableaus
> An $m \times n$ **Young Tableaus** is an $m \times n$ matrix such that the entries of each row are in sorted order from left to right and the entries of each column are in sorted order from top to bottom. Some of the entries of a Young Tableau may be $\infty$, which we treat as nonexistent elements. Thus, a Young tableau can be used to hold $r \leq mn$ finite numbers.

> [!pseudocode]
> ```
> YOUNGIFY(Y, i, j)
> 1. smallest = (i, j)
> 2. if i + 1 <= m and Y[i + 1, j] < Y[smallest]
> 3.     smallest = (i + 1, j)
> 4. if j + 1 <= n and Y[i, j + 1] < Y[smallest]
> 5.     smallest = (i, j + 1)
> 6. if smallest != (i, j)
> 7.     exchange Y[i, j] with Y[smallest]
> 8.     YOUNGIFY(Y, smallest)
> ```
> Complexity:
> - `YOUNGIFY`: $O(m + n)$

> [!pseudocode]
> ```
> INSERT(Y, key)
> 1. if Y[m, n] < INF
> 2.     error "tableau full"
> 3. i = m, j = n
> 4. Y[i, j] = key
> 5. while TRUE
> 6.     largest = 
> ```
