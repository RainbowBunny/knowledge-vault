## The Subset-Sum Problem

> [!definition] The Subset-Sum Problem
> Suppose that you are give a list of positive integers $(M_1, M_2, \dots, M_n)$ and another integer $S$. Find a subset of the elements in the list whose sum is $S$. (You may assume that there is at least one such subset.)

> [!remark]
> $\text{SUBSET-SUM} = \{\langle S, t \rangle | S = \{x_1, \cdots, x_k\}, \text{ and for some} \{y_1, \cdots, y_l\} \subseteq S, \text{we have } \sum y_i = t\}$ is in [[Complexity Theory#NP-Complete|NP-Complete]].

## Lattice Formulation

> [!remark] Vectors Formulation
> For the matrix $$\begin{pmatrix}
> 2 & 0 & 0 & \cdots & 0 & m_1 \\
> 0 & 2 & 0 & \cdots & 0 & m_2 \\
> 0 & 0 & 2 & \cdots & 0 & m_3 \\
> \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
> 0 & 0 & 0 & \cdots & 2 & m_n \\
> 1 & 1 & 1 & \cdots & 1 & S
> \end{pmatrix}.$$
> We have the rows vector: $$
\begin{aligned}
\mathbf{v}_1 &= (2, 0, 0, \ldots, 0, m_1), \\
\mathbf{v}_2 &= (0, 2, 0, \ldots, 0, m_2), \\
&\ \vdots \\
\mathbf{v}_n &= (0, 0, 0, \ldots, 2, m_n), \\
\mathbf{v}_{n+1} &= (1, 1, 1, \ldots, 1, S).
\end{aligned}$$

> [!remark]
> A solution $t$ has length $\sqrt{n}$, so we can use LLL to get a row with $1, -1$ except the last element is $0$.

## Super Increasing Sequence

> [!definition] Super Increasing Sequence
> A **super increasing sequence** of integers is a list of positive integers $\textbf{r} = (r_1, r_2, \dots, r_n)$ with the property that $$r_{i + 1} \geq 2 r_i \quad \forall 1 \leq i \leq n - 1.$$

> [!lemma] 
> Let $\textbf{r} = (r_1, r_2, \dots, r_n)$ be a super increasing sequence. Then $$r_k > r_{k - 1} + \dots + r_2 + r_1 \quad \forall 2 \leq k \leq n.$$ 

> [!algorithm] Fast Algorithm for Superincreasing Subset-Sum
> **Input:**  
> - A superincreasing sequence $M = (M_1, M_2, \ldots, M_n)$  
> - A target sum $S$
>
> **Output:**  
> The unique solution vector
> $$x = (x_1, x_2, \ldots, x_n) \in \{0,1\}^n$$
> such that
> $$\sum_{i=1}^n x_i M_i = S,$$
> assuming a solution exists
>
> ---
>
> 1. For $i = n, n-1, \ldots, 1$, do:
>
>    1.1. If
>    $$S \ge M_i,$$
>    then set:
>    $$x_i \gets 1$$
>    and update:
>    $$S \gets S - M_i.$$
>
>    1.2. Otherwise, set:
>    $$x_i \gets 0.$$
>
> 2. Return the vector $x$.
> ---
> **Complexity of the algorithm**: $\mathcal O(n)$.

## Collision Algorithm

> [!proposition]
> Let $\textbf{M} = (M_1, M_2, \dots, M_n)$ and let $(\textbf{M}, S)$ be a subset-sum problem. For all sets of integers $\textbf{I}$ and $\textbf{J}$ satisfying $$\textbf{I} \subset \{i : 1 \leq i \leq \frac{1}{2}n\} \quad \text{and} \quad \textbf{J} \subset \{j : \frac{1}{2} n < j \leq n\},$$
> compute and make a list of the values $$A_{\textbf{I}} = \sum_{i \in \textbf{I}} M_i \quad \text{and} \quad B_{\textbf{J}} = S - \sum_{j \in \textbf{J}} M_j.$$ Then these lists include a pair of sets $\textbf{I}_0$ and $\textbf{J}_0$ satisfying $A_{\textbf{I}_0} = B_{\textbf{J}_0}$, and the sets $\textbf{I}_0$ and $\textbf{J}_0$ give a solution to the subset-sum problem, $$S = \sum_{i \in \textbf{I}_0} M_i + \sum_{j \in \textbf{J}_0} M_j.$$ The number of entries in each list is at most $2^{n/2}$, so the running time of the algorithm is $\mathcal O(2^{n / 2 + \epsilon})$, where $\epsilon$ is some small value that accounts for sorting and comparing the lists.


## One-Way Function

$$f_{ssum}(x_1, \cdots, x_n, I) = (x_1, \cdots, x_n, \sum_{i \in I} x_i)$$
where $|x_1| = \cdots = |x_n| = n$, and $I \subseteq \{1, 2, \cdots, n\}$.

Problem: The subset sum problem is easy for special cases so $\text{NP}$-Complete can not serve as evidence to the one-wayness of $f_{ssum}$.