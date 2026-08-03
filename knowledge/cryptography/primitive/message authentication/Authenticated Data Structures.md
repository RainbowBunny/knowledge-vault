
| Term                                                    | Reference                                                                        |                 |
| ------------------------------------------------------- | -------------------------------------------------------------------------------- | --------------- |
| Attack Game 8.2 (Authenticated Data Structure Security) | [[#Authenticated Data Structures Security\|secure authenticated data structure]] | $\text{ADSadv}$ |

## Basic Definition

> [!definition] Authenticated Data Structures
> An **authenticated data structure scheme** $\mathcal D = (H, \mathcal P, \mathcal V)$ defined over $(\mathcal X^n, \mathcal Y)$ is a tuple of three efficient deterministic algorithms:
> - $H$ is an algorithm that is invoked as $y \leftarrow H(T)$, where $T = (x_1, \dots, x_n) \in \mathcal X^n$ and $y \in \mathcal Y$.
> - $\mathcal P$ is an algorithm that is invoked as $\pi \leftarrow \mathcal P(i, x, T)$, where $x \in \mathcal X$ and $1 \leq i \leq n$. The algorithm outputs a proof $\pi$ that $x = x_i$, where $T = (x_1, \dots, x_n)$.
> - $\mathcal V$ is an algorithm that is invoked as $\mathcal V(i, x, y, \pi)$ and outputs $\text{accept}$ or $\text{reject}$.
> - We require that for all $T = (x_1, \dots, x_n) \in \mathcal X^n$, and all $1 \leq i \leq n$, we have that $$\mathcal V(i, x_i, H(T), \mathcal P(i, x_i, T)) = \text{accept}$$

## Security

### Authenticated Data Structures

> [!algorithm] Authenticated Data Structures Security
> For an authenticated data structure scheme $\mathcal D = (H, \mathcal P, \mathcal V)$ defined over $(\mathcal X^n, \mathcal Y)$, and a given adversary $\mathcal A$, the attack game runs as follows:
> - The adversary $\mathcal A$ outputs a $y \in \mathcal Y$, a position $i \in \{1, \dots, n\}$, and two pairs $(x, \pi)$ and $(x', \pi')$ where $x, x' \in \mathcal X$.
> 
> We say that $\mathcal A$ wins the game if $x \neq x'$ and $\mathcal V(i, x, y, \pi) = \mathcal V(i, x', y, \pi') = \text{accept}$. Define $\mathcal A$'s advantage with respect to $\mathcal D$, denoted $\text{ADSadv}[\mathcal A, \mathcal D]$, as the probability that $\mathcal A$ wins the game.

> [!definition] Secure Authenticated Data Structures
> We say that an authenticated data structure scheme $\mathcal D$ is secure if for all efficient adversaries $\mathcal A$, the value $\text{ADSadv}[\mathcal A, \mathcal D]$ is negligible.

## Case Study

### Merkle Trees

> [!algorithm] Merkle Trees
> The Merkle tree hash uses a collision resistant hash function $h$, that outputs values in a set $\mathcal Y$. The input to $h$ is either a single element in $\mathcal X$, or a pair of elements in $\mathcal Y$. The Merkle tree hash $H$, derived from $h$, is defined over $(\mathcal X^n, \mathcal Y)$:
> 
> ---
> Function $H$:
> **Input**: $x_1, \dots, x_n \in \mathcal X$, where $n$ is a power of 2.
> **Output**: $y \in \mathcal Y$.
> 
> 1. For $i = 1$ to $n$: $y_i \leftarrow h(x_i)$.
> 2. For $i = 1$ to $n - 1$: $y_{i + n} \leftarrow h(y_{2i - 1}, y_{2i})$
> 3. Output $y_{2n - 1} \in \mathcal Y$.
> 
> ---
> Function $P$:
> Find the path from element $x$ to root, the proof is the sibling of these node.
> 
> ---
> Function $V$:
>  

> [!theorem]
> Let $T \subseteq \mathcal X$ be a set of size $n$, where $n$ is a power of two. For every $1 \leq r \leq n$, and a set $L \subseteq T$ of size $r$, the Merkle proof that all the elements of $L$ are in $T$ contains at most $r \cdot \log_2(n/r)$ elements in $\mathcal Y$.

> [!theorem]
> The Merkle hash tree scheme is a secure authenticated data structure scheme, assuming the underlying hash function $h$ is collision resistant.
