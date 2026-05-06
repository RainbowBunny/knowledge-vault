
## Division Method

> [!definition] Division Method
> In the **division method** for creating hash function, we map a key $k$ into one of $m$ slots by taking the remainder of $k$ divided by $m$. That is, the hash function is $$h(k) = k \mod m.$$

## Multiplication Method

> [!definition] Multiplication Method
> The **multiplication method** for creating hash functions operates in two steps. First, we multiply the key $k$ by a constant $A$ in the range $0 < A < 1$ and extract the fractional part of $kA$. Then, we multiply this value by $m$ and take the floor of the result. In short, the hash function is $$h(k) = \lfloor m (ka \mod 1) \rfloor.$$

## Universal Hashing

> [!theorem]
> Suppose that a hash function $h$ is chosen randomly from a universal collection of hash functions and has been used to hash $n$ keys into a table $T$ of size $m$, using chaining to resolve collisions. If key $k$ is not in the table, then the expected length $E[n_{h(k)}]$ of the list that key $k$ hashed to is at most the load factor $\alpha = \frac{n}{m}$. If key $k$ is in the table, then the expected length $E[n_{h(k)}]$ of the list containing key $k$ is at most $1 + \alpha$.

> [!corollary]
> Using universal hashing and collision resolution by chaining in an initially empty table with $m$ slots, it takes expected time $\Theta(n)$ to handle any sequence of $n$ `INSERT`, `SEARCH` and `DELETE` operations containing $O(m)$ `INSERT` operations.

> [!theorem]
> The class $\mathcal H_{pm} = \{h_{ab}(k) = ((ak + b) \mod p) \mod m\}$ of hash functions is universal.

> [!definition] $\epsilon$ Universal
> Define a family $\mathcal H$ of hash functions from a finite set $U$ to a finite set $B$ to be $\epsilon$-universal if for all pairs of distinct elements $k$ and $l$ in $U$, $$P\{h(k) = h(l)\} \leq \epsilon,$$ where the probability is over the choice of the hash function $h$ drawn at random from the family $\mathcal H$. Thus, an $\epsilon$-universal family of hash functions must have $$\epsilon \geq \frac{1}{|B|} - \frac{1}{|U|}$$

> [!proposition]
> Let $U$ be the set of $n$-tuples of values drawn from $\mathbb Z_p$, and let $B = \mathbb Z_p$, where $p$ is prime. Define the hash function $h_b: U \rightarrow B$ for $b \in \mathbb Z_p$ on an input $n$-tuple $\langle a_0, a_1, \dots, a_{n - 1} \rangle$ from $U$ as $$h_b(\langle a_0, a_1, \dots, a_{n - 1} \rangle) = \sum_{j = 0}^{n - 1} a_j b^j$$ and let $\mathcal H = \{h_b: b \in \mathbb Z_p\}$. Then, $\mathcal H$ is $(\frac{n - 1}{p})$-universal according to the $\epsilon$-universal.

## MD5

> [!remark]
> MD5 suffers from a **Chosen Prefix Collision**: 
> $$\text{MD5}(A) = \text{MD5}(B) \rightarrow \text{MD5}(A + S) = \text{MD5}(S)$$
> Example of one collisions:
> ```python
> block1 = bytes.fromhex("d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70")
block2 = bytes.fromhex("d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70")
> ```
> Todo: [https://github.com/corkami/collisions](https://github.com/corkami/collisions)

