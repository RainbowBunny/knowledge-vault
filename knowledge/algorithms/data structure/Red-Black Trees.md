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
