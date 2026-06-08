
### Containment Free Function

> [!definition] Containment Free
> We say that a function $P$ from $\mathcal M$ to subsets of $\{1, \dots, n\}$ is **containment free** if for all distinct messages $m, m' \in \mathcal M$ the set $P(m)$ is not contained in the set $P(m')$.

> [!algorithm] An Efficient Containment Free Function
> **Input**: $m \in \{0, 1\}^v$
> **Output**: $P_{opt}(m) \subseteq \{1, \dots, n\}$
> $P_{opt}(m)$:
> 1. $c \leftarrow v - \text{weight}(m)$
> 2. Encode $c$ as a binary string in $\{0, 1\}^{\log_2 v + 1}$
> 3. $m' \leftarrow m || c \in \{0, 1\}^n$
> 4. Output the set $\{i \text{ s.t. } m_i' = 1\} \subseteq \{1, \dots, n\}$

> [!lemma]
> For every distinct $m_0, m_1 \in \{0, 1\}^v$ we have that $P_{opt}(m_0) \subseteq P_{opt}(m_1)$.

### Domination Free Function

> [!definition] Dominates
> Let $s, s'$ be vectors in $I^d_n$. We say that $s'$ **dominates** $s$ if $s_i' \geq s_i$ for all $i = 1, \dots, n$. We say that a function $P: \mathcal M \rightarrow I_n^d$ is **domination free** if for all distinct messages $m, m' \in \mathcal M$ the vector $P(m')$ does not dominate $P(m)$.
