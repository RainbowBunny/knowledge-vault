## Definition

> [!definition] Monoid Ring
> For a monoid $(M, \cdot)$ and a ring $(R, +)$, we can obtain a new ring $(R[M], +, \cdot)$:
> - Elements of the ring are $R[M] = \sum_{m \in M} a_m \cdot m$. 
> - Let $A = \sum_{m \in M} a_m \cdot m$ and $A = \sum_{m \in M} b_m \cdot m$:
> 	- $A + B = \sum_{m \in M} (a_m + b_m) \cdot m$.
> 	- $A \cdot B = \sum_{m \in M} \sum_{m_1 \cdot m_2 = m} (a_{m_1} b_{m_2}) \cdot m$.
> - The identity in $R[M]$ is $1_R \cdot 1_M$.
