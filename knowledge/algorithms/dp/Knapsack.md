## Knapsack Problem

> [!definition] 0-1 Knapsack Problem
> A thief robbing a store finds $n$ items. The $i$th item is worth $v_i$ dollars and weighs $w_i$ pounds, where $v_i$ and $w_i$ are integers. The thief wants to take as valuable a load as possible, but he can carry at most $W$ pounds in his knapsack, for some integer $W$. Which item should he take.

> [!pseudocode]
> ```
>  1. DYNAMIC-0-1-KNAPSACK(v, w, n, W)
>  2. let c[0..n, 0..W] be new array
>  3. for w = 0 to W
>  4.     c[0, w] = 0
>  5. for i = 1 to n
>  6.     c[i, 0] = 0
>  7.     for w = 1 to W
>  8.         c[i, w] = c[i - 1, w]
>  9.         if w >= w[i]
> 10.            c[i, w] = MAX(c[i, w], c[i - 1, w - w[i]] + v[i])
> ```

> [!remark]
> Algorithm run in $O(nw)$. 
> `c[i, w]` means using the first $i$ item and total weight is $w$.

> [!remark]
> When 

### Fractional Variant

> [!definition] Fractional Knapsack Problem
> The setup is the same but instead of choosing items, the thief can have fractions of items.

> [!remark]
> A greedy solution that sort items by $\frac{v}{w}$ works.

> [!proposition] $O(n)$ Solution
> Use $k$-th order statistic to get median $m$ of $\frac{v}{w}$, then partition into three groups: $G = \{i: \frac{v_i}{w_i} > m\}$, $E = \{i: \frac{v_i}{w_i} = M\}$, $L = \{i: \frac{v_i}{w_i} < m\}$. Then we can calculate $W_G = \sum_{i \in G} w_i$ and $W_E = \sum_{i \in E}$.
> - If $W_G > W$ then recursively solve with $(G, W)$.
> - Otherwise, take all item of $G$ and as much $E$ as possible:
> 	- If $W_G + W_E \geq W$ then done.
> 	- Else solve with $(L, W - W_G - W_E)$.
> 
> Complexity: $T(n) \leq T(n / 2) + \mathcal O(n)$.

### Coin Changing

> [!definition] Coin Changing
> Consider the problem of making change for $n$ cents using the fewest number of coins. Assume that each coin's value is an integer.
> **Input**:
> - $n$ cents.
> - $d_1, d_2, \cdots, d_k$ is the coin denominations.

> [!pseudocode]
> ```
> COMPUTE-CHANGE(n, d, k)
> 1. let c[1..n] and denom[1..n] be new arrays
> 2. for j = 1 to n
> 3.     c[j] = INF
> 4.     for i = 1 to k
> 5.         if j >= d[i] and 1 + c[j - d[i]] < c[j]
> 6.             c[j] = 1 + c[j - d[i]]
> 7.             denom[j] = d[i]
> 8. return (c, denom)
> ```

> [!remark]
> Greedy solution will work if when in ascending order, $d_{i} | d_{i + 1}$.
