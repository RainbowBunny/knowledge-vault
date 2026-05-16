## Direct-address Tables

> [!definition] Direct-Addressing
> Only works well when the universe $U$ of keys is reasonably small.

> [!pseudocode]
> ```
> DIRECT-ADDRESS-SEARCH(T, k)
> 1. return T[k]
> 
> DIRECT-ADDRESS-INSERT(T, x)
> 1. T[x.key] = x
> 
> DIRECT-ADDRESS-DELETE(T, x)
> 1. T[x.key] = NIL
> ```

## Chained Hash Tables

> [!pseudocode]
> ```
> CHAINED-HASH-INSERT(T, x)
> 1. insert x at the head of list T[h(x, key)]
> 
> CHAINED-HASH-SEARCH(T, k)
> 1. search for an element with key k in list T[h(k)]
> 
> CHAINED-HASH-DELETE(T, x)
> 1. delete x from the list T[h(x.key)]
> ```

> [!definition] Simple Uniform Hashing
> Assume that any given element is equally likely to hash into any of the $m$ slots, independently of where any other element has hashed to. Meaning that if we have $n$ elements, the expected value of the longest chain is $\alpha = \frac{n}{m}$.

> [!theorem]
> In a hash table in which collisions are resolved by chaining, an unsuccessful (successful) search takes average-case time $\Theta(1 + \alpha)$, under the assumption of simple uniform hashing.

## Open Addressing

> [!definition] Open Addressing
> In **open addressing**, all elements occupy the hash table itself. That is, each table entry contains either an element of the dynamic set or `NIL`. To perform insertion using open addressing, we successively examine, or **probe**, the hash table until we find an empty slot in which to put the key.

> [!remark]
> Assume that the hash function $$h: U \times \{0, 1, \dots, m - 1\} \rightarrow \{0, 1, \dots, m - 1\}.$$ With the **probe sequence** $$\langle h(k, 0), h(k, 1), \dots, h(k, m - 1) \rangle$$ be a permutation of $\langle 0, 1, \dots, m - 1 \rangle$.

> [!pseudocode]
> ```
> HASH-INSERT(T, k)
> 1. i = 0
> 2. repeat
> 3.     j = h(k, i)
> 4.     if T[j] == NIL
> 5.         T[j] = k
> 6.         return j
> 7.     else i = i + 1
> 8. until i == m
> 9. error "hash table overflow"
> 
> HASH-SEARCH(T, k)
> 1. i = 0
> 2. repeat
> 3.     j = h(k, i)
> 4.     if T[j] == k
> 5.         return j
> 6.     i = i + 1
> 7. until T[j] == NIL or i == m
> 8. return NIL
> ```

> [!definition] Linear Probing
> Given an ordinary hash function $h': U \rightarrow \{0, 1, \dots, m - 1\}$ as the **auxiliary hash function**, the method of **linear probing** uses the hash function $$h(k, i) = (h'(k) + i) \mod m$$

> [!remark] Problem of Linear Probing
> Linear probing is easy to implement, but it suffers from a problem known as **primary clustering**. Thus, long runs increase the average search time.

> [!definition] Quadratic Probing
> **Quadratic probing** uses a hash function of the form $$h(k, i) = (h'(k) + c_1 i + c_2 i^2) \mod m$$ where $h'$ is an auxiliary hash function, $c_1$ and $c_2$ are positive auxiliary constants

> [!definition] Double Hashing
> **Double hashing** uses a has function of the form $$h(k, i) = (h_1(k) + i h_2(k)) \mod m$$ where both $h_1$ and $h_2$ are auxiliary hash functions.

> [!theorem]
> Given an open-address hash table with load factor $\alpha = n / m < 1$, the expected number of probes in an unsuccessful search is at most $1 / (1 - \alpha)$, assuming uniform hashing.

> [!corollary]
> Inserting an element into an open-address hash table with load factor $\alpha$ requires at most $1/(1 - \alpha)$ probes on average, assuming uniform hashing.

> [!theorem]
> Given an open-address hash table with load factor $\alpha < 1$, the expected number of probes in a successful search is at most $$\frac{1}{\alpha} \ln \frac{1}{1 - \alpha},$$ assuming uniform hashing and assuming that each key in the table is equally likely to be searched for.

> [!pseudocode]
> ```
> HASH-INSERT(T, k)
> 1. i = 0
> 2. repeat
> 3.     j = h(k, i)
> 4.     if T[j] == NIL or T[j] == DELETE
> 5.         T[j] = k
> 6.         return j
> 7.     else i = i + 1
> 8. until i == m
> 9. error "hash table overflow"
> 
> HASH-DELETE(T, k)
> 1. i = 0
> 2. repeat
> 3.     j = h(k, i)
> 4.     if T[j] == k
> 5.         T[j] = DELETE
> 6.         return j
> 7.     else i = i + 1
> 8. until T[j] == NIL or i == m
> 9. error "element not exist"
> ```

## Perfect Hashing

> [!definition] Perfect Hashing
> We call a hashing technique **perfect hashing** if $O(1)$ memory accesses are required to perform a search in the worst case.

> [!proposition]
> To create a perfect hashing scheme, we use two levels of hashing, with universal hashing at each level. 
> - The first level is hash $n$ keys into $m$ slots using a hash function $h$. (Class $\mathcal H_{pm}$)
> - The second level is for each slot $j$ there is a small **secondary hash table** $S_j$ with an associated hash function $h_j$. (Class $\mathcal H_{p, m_j}$)

> [!theorem]
> Suppose that we store $n$ keys in a hash table of size $m = n^2$ using a hash function $h$ randomly chosen from a universal class of hash functions. Then, the probability is less than $1/2$ that there are any collisions.

> [!theorem]
> Suppose that we store $n$ keys in a hash table of size $m = n$ using a hash function $h$ randomly chosen from a universal class of hash functions. Then, we have $$E[\sum_{j = 0}^{m - 1} n_j^2] < 2n$$ where $n_j$ is the number of keys hashing to slot $j$.

> [!corollary]
> Suppose that we store $n$ keys in a hash table of size $m = n$ using a hash function $h$ randomly chosen from a universal class of hash functions, and we set the size of each secondary hash table to $m_j = n_j^2$ for $j = 0, 1, \dots, m - 1$. Then, the expected amount of storage required for all secondary hash tables in a perfect hashing scheme is less than $2n$.

> [!corollary]
> Suppose that we store $n$ keys in a hash table of size $m = n$ using a hash function $h$ randomly chosen from a universal class of hash functions, and we set the size of each secondary hash table to $m_j = n_j^2$ for $j = 0, 1, \dots, m - 1$. Then, the probability is less than $1/2$ that the storage used for secondary hash tables equal or exceeds $4n$.

## Hash Function Constructions

> [!remark]
> The methods below produce non-cryptographic hash functions. For collision-resistant cryptographic hash functions, see [[Hash Functions]] under cryptography.

### Division Method

> [!definition] Division Method
> In the **division method** for creating hash function, we map a key $k$ into one of $m$ slots by taking the remainder of $k$ divided by $m$. That is, the hash function is $$h(k) = k \mod m.$$

### Multiplication Method

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
