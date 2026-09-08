
> [!proposition]
> Let $n$ be a positive integer and let $k = \lfloor \log n \rfloor + 1$, which means that $2^k > n$. Then we can always write $$n = u_0 + u_1 \cdot 2 + u_2 \cdot 4 + u_3 \cdot 8 + \cdots + u_k \cdot 2^k$$
> with $u_0, u_1, \dots, u_k \in \{-1, 0, 1\}$ and at most $\frac{1}{2} k$ of the $u_i$ nonzero.

> [!proof]
> $$2^s + 2^{s + 1} + \cdots + 2^{s + t - 1} + 0 \cdot 2^{s + t} = - 2^s + 2^{s + t}$$

> [!definition] Sentinels
> A trick is that we can use an object for the `nil` object.

