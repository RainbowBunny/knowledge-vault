## Dynamic Table

> [!definition] Dynamic Table
> We do not always know in advance how many objects will we need, so the idea is that we will change the allocation based on the **load factor** $\alpha (T)$ of table defined by dividing the number of items stored with the size of the table.
> One idea is that if $\alpha (T) = 1$ then we expand the memory allocation by two-fold, and when load factor is too low ($\alpha (T) \leq \frac{1}{4}$), we halve our memory allocation.
