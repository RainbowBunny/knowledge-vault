## Definition

> [!definition] Hamming Distance
> Let $x$ and $y$ be words of length $n$ over the alphabet $A$. The **(Hamming) distance** from $x$ to $y$, denoted by $d(x, y)$, is defined to be the number of places at which $x$ and $y$ differ. If $x = x_1 \cdots x_n$ and $y = y_1 \cdots y_n$, then 
> $$d(x, y) = d(x_1, y_1) + \cdots + d(x_n, y_n),$$ 
> where $x_i$ and $y_i$ are regarded as words of length $1$, and $$d(x_i, y_i) = \begin{cases}1 &\text{ if } x_i \neq y_i \\ 0 &\text{ if } x_i = y_i\end{cases}$$

> [!proposition]
> The Hamming distance of words of length $n$ over the alphabet $A$ satisfies:
> - [[Positive Definiteness]].
> - [[Distance Symmetry]].
> - [[Triangle Inequality]].


