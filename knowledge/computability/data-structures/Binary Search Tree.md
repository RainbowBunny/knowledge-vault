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
