## Aggregate Analysis

> [!definition] Aggregate Analysis
> In **aggregate analysis**, we show that for all $n$, a sequence of $n$ operations takes wort-case time $T(n)$ in total. In the worst case, the average cost, or **amortized cost**, per operation is therefore $T(n) / n$.

## Accounting Method

> [!definition] Accounting Method
> In the **accounting method** of amortized analysis, we assign differing charges to different operations, with some operations charged more or less than they actually cost. We call the amount we charge an operation its **amortized cost**. When an operation's amortized cost exceeds its actual cost, we assign the difference to specific objects in the data structure as **credit**. Credit can help pay for later operations whose amortized cost is less than their actual cost.

> [!example]
> Increasing a $n$-bit binary number $k$ times, the cost of setting a bit is $2$ dollars. We first begin with the cost is the number of set bits and each operation will set $1$ bit from $0$ to $1$ and thus total cost is $O(n)$. The idea is that $2$ dollars cost here is for setting the bit $1$ and at some point we will set it back to $0$.

## Potential Method

> [!definition] Potential Method
> Assign potential score for each state of the structures, and thus we can calculate the amortized cost by analyzing the different potential score of two states and the actual cost of the action. Thus, if we have the potential score always increases then.

## Application: Dynamic Table

> [!definition] Dynamic Table
> We do not always know in advance how many objects will we need, so the idea is that we will change the allocation based on the **load factor** $\alpha (T)$ of table defined by dividing the number of items stored with the size of the table.
> One idea is that if $\alpha (T) = 1$ then we expand the memory allocation by two-fold, and when load factor is too low ($\alpha (T) \leq \frac{1}{4}$), we halve our memory allocation.

> [!remark]
> The doubling/halving strategy gives $O(1)$ amortized cost per insertion/deletion — the classic showcase for all three methods above.
