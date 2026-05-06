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

## Priority Queues

> [!definition] Priority Queue
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

## Elementary Data Structures

### Stacks

> [!pseudocode]
> ```
> STACK-EMPTY(S)
> 1. if S.top == 0
> 2.     return TRUE
> 3. else return FALSE
> 
> PUSH(S, x)
> 1. S.top = S.top + 1
> 2. S[S.top] = x
> 
> POP(S)
> 1. if STACK-EMPTY(S)
> 2.     error "underflow"
> 3. else S.top = S.top - 1
> 4.     return S[S.top + 1]
> 
> MULTIPOP(S, k)
> 1. while not STACK-EMPTY(S) and k > 0
> 2.     POP(S)
> 3.     k = k - 1
> ```

### Queues

> [!pseudocode]
> ```
> QUEUE-EMPTY(Q)
> 1. if Q.head == Q.tail
> 2.     return TRUE
> 3. else return FALSE
> 
> QUEUE-FULL(Q)
> 1. if Q.head == Q.tail + 1 or (Q.head == 1 and Q.tail == Q.length)
> 2.     return TRUE
> 3. else return FALSE
> 
> ENQUEUE(Q, x)
> 1. if QUEUE-FULL(Q)
> 2.     error "overflow"
> 3. else
> 4.     Q[Q.tail] = x
> 5.     if Q.tail == Q.length
> 6.         Q.tail = 1
> 7.     else Q.tail = Q.tail + 1
> 
> DEQUEUE(Q)
> 1. if QUEUE-EMPTY(Q)
> 2.     error "underflow"
> 3. else
> 4.     x = Q[Q.head]
> 5.     if Q.head == Q.length
> 6.         Q.head = 1
> 7.         else Q.head = Q.head + 1
> 8.         return x
> ```

### Dequeue

> [!pseudocode]
> ```
> HEAD-ENQUEUE(Q, x)
> 1. if QUEUE-FULL(Q)
> 2.     error "overflow"
> 3. else
> 4.     if Q.head == 1
> 5.         Q.head = Q.length
> 6.     else Q.head = Q.head - 1
> 7.     Q[Q.head] = x
> 
> TAIL-ENQUEUE(Q, x)
> 1. if QUEUE-FULL(Q)
> 2.     error "overflow"
> 3. else
> 4.     Q[Q.tail] = x
> 5.     if Q.tail == Q.length
> 6.         Q.tail = 1
> 7.     else
> 8.         Q.tail = Q.tail + 1
> 
> HEAD-DEQUEUE(Q)
> 1. if QUEUE-EMPTY(Q)
> 2.     error "underflow"
> 3. else
> 4.     x = Q[Q.head]
> 5.     if Q.head == Q.length
> 6.         Q.head = 1
> 7.     else Q.head = Q.head + 1
> 8.     return x
> 
> TAIL-DEQUEUE(Q)
> 1. if QUEUE-EMPTY(Q)
> 2.     error "underflow"
> 3. else
> 4.     if Q.tail == 1
> 5.         Q.tail = Q.length
> 6.     else Q.tail = Q.tail - 1
> 7.     x = Q[Q.tail]
> 8.     return x
> ```

### Double Linked Lists

> [!pseudocode]
> ```
> LIST-SEARCH(L, k)
> 1. x = L.head
> 2. while x != NIL and x.key != k
> 3.     x = x.next
> 4. return x
> 
> LIST-INSERT(L, x)
> 1. x.next = L.head
> 2. if L.head != NIL
> 3.     L.head.prev = x
> 4. L.head = x
> 5. x.prev = NIL
> 
> LIST-DELETE(L, x)
> 1. if x.prev != NIL
> 2.     x.prev.next = x.next
> 3. else L.head = x.next
> 4. if x.next != NIL
> 5.     x.next.prev = x.prev
> ```

> [!pseudocode]
> ```
> LIST-DELETE'(L, x)
> 1. x.prev.next = x.next
> 2. x.next.prev = x.prev
> 
> LIST-SEARCH'(L, k)
> 1. x = L.nil.next
> 2. while x != L.nil and x.key != k
> 3.     x = x.next
> 4. return x
> 
> LIST-INSERT'(L, x)
> 1. x.next = L.nil.next
> 2. L.nil.next.prev = x
> 3. L.nil.next = x
> 4. x.prev = L.nil
> ```

### Single Linked Lists

> [!pseudocode]
> ```
> LIST-INSERT(L, x)
> 1. x.next = L.head
> 2. L.head = x
> ```

## Dynamic Table

> [!definition] Dynamic Table
> We do not always know in advance how many objects will we need, so the idea is that we will change the allocation based on the **load factor** $\alpha (T)$ of table defined by dividing the number of items stored with the size of the table.
> One idea is that if $\alpha (T) = 1$ then we expand the memory allocation by two-fold, and when load factor is too low ($\alpha (T) \leq \frac{1}{4}$), we halve our memory allocation.



## Hash Tables

### Direct-address Tables

> [!definition] Direct-Addressing
> Only works well when the universe $U$ of keys is reasonably small.

> [!pseudocode]
> ```
> DIRECT-ADDRESS-SEARCH(T, k)
> 1. return T[k]
> 
> DIRECT-ADDRESS-INSERT(T, x)
> 1. T[x.key] = x
> 
> DIRECT-ADDRESS-DELETE(T, x)
> 1. T[x.key] = NIL
> ```

### Hash Tables

> [!pseudocode]
> ```
> CHAINED-HASH-INSERT(T, x)
> 1. insert x at the head of list T[h(x, key)]
> 
> CHAINED-HASH-SEARCH(T, k)
> 1. search for an element with key k in list T[h(k)]
> 
> CHAINED-HASH-DELETE(T, x)
> 1. delete x from the list T[h(x.key)]
> ```

> [!definition] Simple Uniform Hashing
> Assume that any given element is equally likely to hash into any of the $m$ slots, independently of where any other element has hashed to. Meaning that if we have $n$ elements, the expected value of the longest chain is $\alpha = \frac{n}{m}$.

> [!theorem]
> In a hash table in which collisions are resolved by chaining, an unsuccessful (successful) search takes average-case time $\Theta(1 + \alpha)$, under the assumption of simple uniform hashing.

### Open Addressing

> [!definition] Open Addressing
> In **open addressing**, all elements occupy the hash table itself. That is, each table entry contains either an element of the dynamic set or `NIL`. To perform insertion using open addressing, we successively examine, or **probe**, the hash table until we find an empty slot in which to put the key.

> [!remark]
> Assume that the hash function $$h: U \times \{0, 1, \dots, m - 1\} \rightarrow \{0, 1, \dots, m - 1\}.$$ With the **probe sequence** $$\langle h(k, 0), h(k, 1), \dots, h(k, m - 1) \rangle$$ be a permutation of $\langle 0, 1, \dots, m - 1 \rangle$.

> [!pseudocode]
> ```
> HASH-INSERT(T, k)
> 1. i = 0
> 2. repeat
> 3.     j = h(k, i)
> 4.     if T[j] == NIL
> 5.         T[j] = k
> 6.         return j
> 7.     else i = i + 1
> 8. until i == m
> 9. error "hash table overflow"
> 
> HASH-SEARCH(T, k)
> 1. i = 0
> 2. repeat
> 3.     j = h(k, i)
> 4.     if T[j] == k
> 5.         return j
> 6.     i = i + 1
> 7. until T[j] == NIL or i == m
> 8. return NIL
> ```

> [!definition] Linear Probing
> Given an ordinary hash function $h': U \rightarrow \{0, 1, \dots, m - 1\}$ as the **auxiliary hash function**, the method of **linear probing** uses the hash function $$h(k, i) = (h'(k) + i) \mod m$$

> [!remark] Problem of Linear Probing
> Linear probing is easy to implement, but it suffers from a problem known as **primary clustering**. Thus, long runs increase the average search time.

> [!definition] Quadratic Probing
> **Quadratic probing** uses a hash function of the form $$h(k, i) = (h'(k) + c_1 i + c_2 i^2) \mod m$$ where $h'$ is an auxiliary hash function, $c_1$ and $c_2$ are positive auxiliary constants

> [!definition] Double Hashing
> **Double hashing** uses a has function of the form $$h(k, i) = (h_1(k) + i h_2(k)) \mod m$$ where both $h_1$ and $h_2$ are auxiliary hash functions.

> [!theorem]
> Given an open-address hash table with load factor $\alpha = n / m < 1$, the expected number of probes in an unsuccessful search is at most $1 / (1 - \alpha)$, assuming uniform hashing.

> [!corollary]
> Inserting an element into an open-address hash table with load factor $\alpha$ requires at most $1/(1 - \alpha)$ probes on average, assuming uniform hashing.

> [!theorem]
> Given an open-address hash table with load factor $\alpha < 1$, the expected number of probes in a successful search is at most $$\frac{1}{\alpha} \ln \frac{1}{1 - \alpha},$$ assuming uniform hashing and assuming that each key in the table is equally likely to be searched for.

> [!pseudocode]
> ```
> HASH-INSERT(T, k)
> 1. i = 0
> 2. repeat
> 3.     j = h(k, i)
> 4.     if T[j] == NIL or T[j] == DELETE
> 5.         T[j] = k
> 6.         return j
> 7.     else i = i + 1
> 8. until i == m
> 9. error "hash table overflow"
> 
> HASH-DELETE(T, k)
> 1. i = 0
> 2. repeat
> 3.     j = h(k, i)
> 4.     if T[j] == k
> 5.         T[j] = DELETE
> 6.         return j
> 7.     else i = i + 1
> 8. until T[j] == NIL or i == m
> 9. error "element not exist"
> ```

### Perfect Hashing

> [!definition] Perfect Hashing
> We call a hashing technique **perfect hashing** if $O(1)$ memory accesses are required to perform a search in the worst case.

> [!proposition]
> To create a perfect hashing scheme, we use two levels of hashing, with universal hashing at each level. 
> - The first level is hash $n$ keys into $m$ slots using a hash function $h$. (Class $\mathcal H_{pm}$)
> - The second level is for each slot $j$ there is a small **secondary hash table** $S_j$ with an associated hash function $h_j$. (Class $\mathcal H_{p, m_j}$)

> [!theorem]
> Suppose that we store $n$ keys in a hash table of size $m = n^2$ using a hash function $h$ randomly chosen from a universal class of hash functions. Then, the probability is less than $1/2$ that there are any collisions.

> [!theorem]
> Suppose that we store $n$ keys in a hash table of size $m = n$ using a hash function $h$ randomly chosen from a universal class of hash functions. Then, we have $$E[\sum_{j = 0}^{m - 1} n_j^2] < 2n$$ where $n_j$ is the number of keys hashing to slot $j$.

> [!corollary]
> Suppose that we store $n$ keys in a hash table of size $m = n$ using a hash function $h$ randomly chosen from a universal class of hash functions, and we set the size of each secondary hash table to $m_j = n_j^2$ for $j = 0, 1, \dots, m - 1$. Then, the expected amount of storage required for all secondary hash tables in a perfect hashing scheme is less than $2n$.

> [!corollary]
> Suppose that we store $n$ keys in a hash table of size $m = n$ using a hash function $h$ randomly chosen from a universal class of hash functions, and we set the size of each secondary hash table to $m_j = n_j^2$ for $j = 0, 1, \dots, m - 1$. Then, the probability is less than $1/2$ that the storage used for secondary hash tables equal or exceeds $4n$.

## Binary Search Tree

> [!definition] Binary Search Tree
> Binary search tree is a binary tree which each node contains a key, satellite data, its left child, right child, parent. If a child or the parent is missing then the appropriate attribute is the value `NIL`. The root node is the only node in the tree whose parent is `NIL`.

> [!proposition] Binary Search Tree Property
> The keys in a binary search tree are always stored in such a way as to satisfy the **binary-search-tree property**:
> Let $x$ be a node in a binary search tree. If $y$ is a node in the left subtree of $x$, then $y.key \leq x.key$. If $y$ is a node in the right subtree of $x$, then $y.key \geq x.key$.

> [!pseudocode]
> ```
> INORDER-TREE-WALK(x)
> 1. if x != NIL
> 2.     INORDER-TREE-WALK(x.left)
> 3.     print x.key
> 4.     INORDER-TREE-WALK(x.right)
> ```

> [!pseudocode]
> ```
> INORDER-TREE-WALK(T)
> 1. let S be an empty stack
> 2. current = T.root
> 3. while current != NIL or stack not empty
> 4.     while current != NIL
> 5.         S.push(current)
> 6.         current = current.left
> 7.     current = POP(S)
> 8.     current = current.right
> ```

> [!theorem]
> If $x$ is the root of an $n$-node subtree, then the call `INORDER-TREE-WALK(x)` takes $\Theta(n)$ time.

> [!pseudocode]
> ```
> PREORDER-TREE-WALK(x)
> 1. if x != NIL
> 2.     print x.key
> 3.     PREORDER-TREE-WALK(x.left)
> 4.     PREORDER-TREE-WALK(x.right)
> 
> POSTORDER-TREE-WALK(x)
> 1. if x != NIL
> 2.     POSTORDER-TREE-WALK(x.left)
> 3.     POSTORDER-TREE-WALK(x.right)
> 4.     print x.key
> ```

### Querying

> [!pseudocode]
> ```
> TREE-SEARCH(x, k)
> 1. if x == NIL or k == x.key
> 2.     return x
> 3. if k < x.key
> 4.     return TREE-SEARCH(x.left, k)
> 5. else return TREE-SEARCH(x.right, k)
> 
> ITERATIVE-TREE-SEARCH(x, k)
> 1. while x != NIL and k != x.key
> 2.     if k < x.key
> 3.         x = x.left
> 4.     else x = x.right
> 5. return x
> 
> TREE-MINIMUM(x)
> 1. while x.left != NIL
> 2.     x = x.left
> 3. return x
> 
> ITERATIVE-TREE-MINIMUM(x)
> 1. if x.left != NIL
> 2.     return TREE-MINIMUM(x.left)
> 3. else return x
> 
> TREE-MAXIMUM(x)
> 1. while x.right != NIL
> 2.     x = x.right
> 3. return x
> 
> ITERATIVE-TREE-MAXIMUM(x)
> 1. if x.right != NIL
> 2.     return TREE-MAXIMUM(x.right)
> 3. else return x
> ```

> [!pseudocode]
> ```
> TREE-SUCCESSOR(x)
> 1. if x.right != NIL
> 2.     return TREE-MINIMUM(x.right)
> 3. y = x.p
> 4. while y != NIL and x == y.right
> 5.     x = y
> 6.     y = y.p
> 7. return y
> 
> TREE-PREDECESSOR(x)
> 1. if x.left != NIL
> 2.     return TREE-MAXIMUM(x.left)
> 3. y = x.p
> 4. while y != NIL and x == y.left
> 5.     x = y
> 6.     y = y.p
> 7. return y
> ```

> [!theorem]
> We can implement the dynamic-set operations `SEARCH`, `MINIMUM`, `MAXIMUM`, `SUCCESSOR`, and `PREDECESSOR` so that each one runs in $O(h)$ time on a binary search tree of height $h$.

### Insertion and Deletion

> [!pseudocode]
> ```
> TREE-INSERT(T, z)
>  1. y = NIL
>  2. x = T.root
>  3. while x != NIL
>  4.     y = x
>  5.     if z.key < x.key
>  6.         x = x.left
>  7.     else x = x.right
>  8. z.p = y
>  9. if y == NIL
> 10.     T.root = z // tree T was empty
> 11. elseif z.key < y.key
> 12.     y.left = z
> 13. else y.right = z
> 
> TRANSPLANT(T, u, v)
> 1. if u.p == NIL
> 2.     T.root = v
> 3. else if u == u.p.left
> 4.     u.p.left = v
> 5. else u.p.right = v
> 6. if v != NIL
> 7.     v.p = u.p
> 
> TREE-DELETE(T, z)
>  1. if z.left == NULL
>  2.     TRANSPLANT(T, z, z.right)
>  3. elseif z.right == NIL
>  4.     TRANSPLANT(T, z, z.left)
>  5. else y = TREE-MINIMUM(z.right)
>  6.     if y.p != z
>  7.         TRANSPLANT(T, y, y.right)
>  8.         y.right = z.right
>  9.         y.right.p = y
> 10.     TRANSPLANT(T, z, y)
> 11.     y.left = z.left
> 12.     y.left.p = y
> ```

> [!theorem]
> We can implement the dynamic-set operations `INSERT` and `DELETE` so that each one runs in $O(h)$ time on a binary search tree of height $h$.

> [!theorem]
> The expected height of a randomly build binary search tree on $n$ distinct keys is $O(\log n)$.

## Red-Black Trees

> [!definition] Red-Black Trees
> A **red-black tree** is a binary search tree with one extra bit of storage per node: its **color**, which can be either `RED` or `BLACK`. By constraining the node colors on any simple path from the root to a leaf, red-black trees ensure that no such path is more than twice as long as any other, so that the tree is approximately **balanced**.

> [!proposition] Red-black Properties
> 1. Every node is either red or black.
> 2. The root is black.
> 3. Every leaf (`NIL`) is black.
> 4. If a node is red, then both its children are black.
> 5. For each node, all simple paths from the node to descendant leaves contain the same number of black nodes.

> [!lemma]
> A red-black tree with $n$ internal nodes has height at most $2\log(n + 1)$.

### Rotations

> [!pseudocode]
> ```
> LEFT-ROTATE(T, x)
>  1. y = x.right
>  2. x.right = y.left
>  3. if y.left != T.nil
>  4.     y.left.p = x
>  5. y.p = x.p
>  6. if x.p == T.nil
>  7.     T.root = y
>  8. else if x == x.p.left
>  9.     x.p.left = y
> 10. y.left = x
> 11. x.p = y
> 
> RIGHT-ROTATE(T, y)
>  1. x = y.left
>  2. y.left = x.right
>  3. if x.right != T.nil
>  4.     x.right.p = y
>  5. x.p = y.p
>  6. if y.p == T.nil
>  7.     T.root = x
>  8. else if y == y.p.right
>  9.     y.p.right = x
> 10. else y.p.left = x
> 11. x.right = y
> 12. y.p = x
> ```

### Insertion

> [!pseudocode]
> ```
> RB-INSERT-FIXUP(T, z)
>  1. while z.p.color == RED
>  2.     if z.p == z.p.p.left
>  3.         y = z.p.p.right
>  4.         if y.color == RED
>  5.             z.p.color == BLACK
>  6.             y.color = BLACK
>  7.             z.p.p.color = RED
>  8.             z = z.p.p
>  9.         else if z == z.p.right
> 10.             z = z.p
> 11.             LEFT-ROTATE(T, z)
> 12.             z.p.color = BLACK
> 13.             z.p.p.color = RED
> 14.             RIGHT-ROTATE(T, z.p.p)
> 15.     else (same as then clause with "right" and "left" exchanged)
> 16. T.root.color = BLACK
> 
> RB-INSERT(T, z)
>  1. y = T.nil
>  2. x = T.root
>  3. while x != T.nil
>  4.     y = x
>  5.     if z.key < x.key
>  6.         x = x.left
>  7.     else x = x.right
>  8. z.p = y
>  9. if y == T.nil
> 10.     T.root = z
> 11. else if z.key < y.key
> 12.     y.left = z
> 13. else y.right = z
> 14. z.left = T.nil
> 15. z.right = T.nil
> 16. z.color = RED
> 17. RB-INSERT-FIXUP(T, z)
> ```

### Deletion

> [!pseudocode]
> ```
> RB-TRANSPLANT(T, u, v)
> 1. if u.p == T.nil
> 2.     T.root = v
> 3. else if u == u.p.left
> 4.     u.p.left = v
> 5. else u.p.right == v
> 6. v.p = u.p
> 
> RB-DELETE-FIXUP(T, x)
>  1. while x != T.root and x.color == BLACK
>  2.     if x == x.p.left
>  3.         w = x.p.right
>  4.         if w.color == RED
>  5.             w.color = BLACK
>  6.             x.p.color = RED
>  7.             LEFT-ROTATE(T, x.p)
>  8.             w = x.p.right
>  9.     if w.left.color == BLACK and w.right.color == BLACK
> 10.         w.color = RED
> 11.         x = x.p
> 12.     else if w.right.color == BLACK
> 13.         w.left.color == BLACK
> 14.         w.color = RED
> 15.         RIGHT-ROTATE(T, w)
> 16.         w = x.p.right
> 17.         w.color = x.p.color
> 18.         x.p.color = BLACK
> 19.         w.right.color = BLACK
> 20.         LEFT-ROTATE(T, x.p)
> 21.         x = T.root
> 22.     else (same as then clause with "right" and "left" exchanged)
> 23. x.color = BLACK
> 
> RB-DELETE(T, z)
>  1. y = z
>  2. y-original-color = y.color
>  3. if z.left == T.nil
>  4.     x = z.right
>  5.     RB-TRANSPLANT(T, z, z.right)
>  6. else if z.right == T.nil
>  7.     x = z.left
>  8.     RB-TRANSPANT(T, z, z.left)
>  9. else y = TREE-MINIMUM(z.right)
> 10.     y-original-color = y.color
> 11.     x = y.right
> 12.     if y.p == z
> 13.         x.p = y
> 14.     else RB-TRANSPLANT(T, y, y.right)
> 15.         y.right = z.right
> 16.         y.right.p = y
> 17.     RB-TRANSPLANT(T, y, y.right)
> 18.     y.left = z.left
> 19.     y.left.p = y
> 20.     y.color = z.color
> 21. if y-original-color == BLACK
> 22.     RB-DELETE-FIXUP(T, x)
> ```

