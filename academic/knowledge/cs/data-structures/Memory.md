## Object Allocation

Two equivalent allocation schemes for a linked free-list of objects.

### Pointer Representation

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

### Array Representation

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
