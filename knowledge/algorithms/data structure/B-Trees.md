## B-Trees

> [!definition] B-Tree
> A **B-Tree** $T$ is a rooted tree (whose root is $T.root$) having the following properties:
> 1. Every node $x$ has the following attributes:
> 	- $x.n$, the number of keys currently stored in node $x$,
> 	- The $x.n$ keys themselves, $x.key_1, x.key_2, \dots, x.key_{x.n}$, stored in nondecreasing order, so that $x.key_1 \leq x.key_2 \leq \cdots \leq x.key_{x.n}$,
> 	- $x.leaf$, a boolean value that is $\text{TRUE}$ if $x$ is a leaf and $\text{FALSE}$ if $x$ is an internal node.
> 2. Each internal node $x$ also contains $x.n + 1$ pointers $x.c_1, x.c_2, \dots, x.c_{x.n + 1}$ to its children. Leaf nodes have no children, and so their $c_i$ attributes are undefined.
> 3. The keys $x.key_i$ separate the ranges of keys stored in each subtree: if $k_i$ is any key stored in the subtree with root $x.c_i$, then $$k_1 \leq x.key_1 \leq k_2 \leq x.key_2 \leq \cdots \leq x.key_{x.n} \leq k_{x.n + 1}.$$ 
> 4. All leaves have the same depth, which is the tree's height $h$.
> 5. Nodes have lower and upper bounds on the number of keys they can contain. We express these bounds in terms of a fixed integer $t \geq 2$ called the **minimum degree** of the $B$-tree:
> 	- Every node other than the root must have at least $t - 1$ keys. Every internal node other than the root thus has at least $t$ children. If the tree is nonempty, the root must have at least one key.
> 	- Every node may contain at most $2t - 1$ keys. Therefore, an internal node may have at most $2t$ children. We say that a node is **full** if it contains exactly $2t - 1$ keys.

> [!theorem] Height of a B-tree
> If $n \geq 1$, then for any $n$-key B-tree $T$ of height $h$ and minimum degree $t \geq 2$, $h \leq \log_t \frac{n + 1}{2}$.

> [!pseudocode]
> ```
> B-TREE-SPLIT-CHILD(x, i)
>  1. z = ALLOCATE-NODE()
>  2. y = x.c[i]
>  3. z.left = y.left
>  4. z.n = t - 1
>  5. for j = 1 to t - 1
>  6.     z.key[j] = y.key[j + t]
>  7. if not y.leaf
>  8.     for j = 1 to t
>  9.         z.c[j] = y.c[j + t]
> 10. y.n = t - 1
> 11. for j = x.n + 1 downto i + 1
> 12.     x.c[j + 1] = x.c[j]
> 13. x.c[i + 1] = z
> 14. for j = x.n downto i
> 15.     x.key[j + 1] = x.key[j]
> 16. x.key[i] = y.key[t]
> 17. x.n = x.n + 1
> 18. DISK-WRITE(y)
> 19. DISK-WRITE(z)
> 20. DISK-WRITE(x)
> 
> B-TREE-INSERT(T, k)
>  1. r = T.root
>  2. if r.n == 2t - 1
>  3.     s = ALLOCATE-NODE()
>  4.     T.root = s
>  5.     s.left = FALSE
>  6.     s.n = 0
>  7.     s.c[1] = r
>  8.     B-TREE-SPLIT-CHILD(s, 1)
>  9.     B-TREE-INSERT-NONFULL(s, k)
> 10. else B-TREE-INSERT-NONFULL(r, k)
> 
> B-TREE-INSERT-NONFULL(x, k)
>  1. i = x.n
>  2. if x.leaf
>  3.     while i >= 1 and k < x.key[i]
>  4.         x.key[i + 1] = x.key[i]
>  5.         i = i - 1
>  6.     x.key[i + 1] = k
>  7.     x.n = x.n + 1
>  8. DISK-WRITE(x)
>  9. else while i >= 1 and k < x.key[i]
> 10.         i = i - 1
> 11.     i = i + 1
> 12.     DISK-READ(x.c[i])
> 13.     if x.c[i].n == 2t - 1
> 14.         B-TREE-SPLIT-CHILD(x, i)
> 15.         if k > x.key[i]
> 16.             i = i + 1
> 17.     B-TREE-INSERT-NONFULL(x.c[i], k)
> 
> B-TREE-FIND-MIN(x)
> 1. if x == NIL
> 2.     return NIL
> 3. else if x.leaf
> 4.     return x.key[1]
> 5. else
> 6.     DISK-READ(x.c[1])
> 7.     return B-TREE-FIND-MIN(x.c[1])
> 
> B-TREE-FIND-MAX(x)
> 1. if x == NIL
> 2.     return NIL
> 3. else if x.leaf
> 4.     return x.c[x.n]
> 5. else
> 6.     DISK-READ(x.c[x.n + 1])
> 7.     return B-TREE-FIND-MAX(x.c[x.n + 1])
> 
> B-TREE-FIND-PREDECESSOR(x, i)
>  1. if !x.leaf
>  2.     DISK-READ(x.c[i])
>  3.     return B-TREE-FIND-MAX(x.c[i])
>  4. else if i > 1
>  5.     return x.key[i - 1]
>  6. else
>  7.     z = x
>  8.     while TRUE
>  9.         if z.p == NIL
> 10.             return NIL
> 11.         y = z.p
> 12.         j = 1
> 13.         DISK-READ(y.c[1])
> 14.         while y.c[j] != x
> 15.             j = j + 1
> 16.             DISK-READ(y.c[j])
> 17.         if j = 1
> 18.             z = y
> 19.         else
> 20.             return y.key[j - 1]
> ```
