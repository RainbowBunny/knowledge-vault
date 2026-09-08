## Double Linked Lists

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

## Single Linked Lists

> [!pseudocode]
> ```
> LIST-INSERT(L, x)
> 1. x.next = L.head
> 2. L.head = x
> ```
