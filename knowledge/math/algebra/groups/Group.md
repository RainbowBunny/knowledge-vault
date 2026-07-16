
## Group

>[!definition] Group
A **group** consists of a set $G$ and a rule, which we denote by $\star$, for combining two elements $a, b \in G$ to obtain an element $a \star b \in G$. The composition operation $\star$ is required to have the following three properties: 
> - **Identity Law**, 
> - **Inverse Law**, 
> - **Associate Law**.

> [!definition] Abelian Group
If, in addition, composition satisfies the **Commutative Law** then the group is called a **commutative group** or an **abelian group**.

> [!definition] Finite Group
> If $G$ has finitely many elements, we say that $G$ is a **finite group**.

### Order of a group

> [!definition] Order of a Group
> The **order of** $G$ is the number of elements in $G$; it is denoted by $|G|$ or $\# G$.

> [!definition] Order of a group element
> Let $G$ be a group and let $a \in G$ be an element of the group. Suppose there exists a positive integer $d$ with the property that $a^d = e$. The smallest such $d$ is called the **order of** $a$. If there is no such $d$, then $a$ is said to have **infinite order**.

>[!proposition]
>Let $G$ be a finite group. Then every element of $G$ has finite order. Further, if $a \in G$ has order $d$ and if $a^k = e$, then $d \mid k$.

> [!theorem] Lagrange's Theorem
> Let $G$ be a finite group and let $a \in G$. Then the order of $a$ divides the order of $G$.
> More precisely, let $n = |G|$ be the order of $G$ and let $d$ be the order of $a$. Then
> $$a^n = e \qquad \text{and} \qquad d \mid n$$

### Example Group

> [!example]
> Each of the following is a group:
> 1. $\text{GL}_n(\mathbb R) = \{n\text{-by-}n \text{ matrices } A \text{ with real coefficients and } \det(A) \neq 0\}$ with operation $\star$ is matrix multiplication.

> [!definition] General Linear Group
> The **General Linear Group** of order $s$, denoted $\text{GL}_s(\mathbb Z_n)$, is the monoid of invertible $s \times s$ matrices containing elements from $\mathbb Z_n$ with respect to multiplication such that the determinants of the matrices and $n$ are relatively prime.

> [!theorem]
> The order of the General Linear Group $\text{GL}_2(\mathbb Z_p)$ is given by $$|\text{GL}_2(\mathbb Z_p)| = (p^2 - 1)(q^2 - 1),$$ where $p$ is a prime integer.

> [!lemma]
> Let $n = pq$ where $p$ and $q$ are distinct prime integers. If $M \in \text{GL}_2(\mathbb Z_n)$, then $M \in \text{GL}_2(\mathbb Z_p)$ and $M \in \text{GL}_2(\mathbb Z_q)$. 
 
## Subgroup

> [!definition] Additive Subgroup
> A subset $L$ of $\mathbb R^m$ is an **additive subgroup** if it is closed under addition and subtraction.

> [!definition] Discrete Additive Subgroup
> An additive subgroup is called a **discrete additive subgroup** if there is a positive constant $\epsilon > 0$ with the following property: for every $\textbf{v} \in L$, $$L \cap \{\textbf{w} \in \mathbb R^m: ||\textbf{v} - \textbf{w}|| < \epsilon\} = \{\textbf{v}\}.$$

> [!theorem] Lagrange's Theorem
> Let $H$ be a subgroup of a finite group $G$. Then $|H|$ divides $|G|$.
 
## Group Homorphism

> [!definition] Group Homorphism
> Let $G$ and $H$ be groups. A function $\phi: G \rightarrow H$ is called a **(group) homomorphism** if it satisfies $$\phi(g_1 \star g_2) = \phi(g_1) \star \phi(g_2) \forall g_1, g_2 \in G.$$

> [!proposition]
> Let $e_G$ be the identity element of $G$, let $e_H$ be the identity element of $H$, and let $g \in G$. Then $$\phi(e_G) = e_H \quad \text{and} \quad \phi(g^{-1}) = \phi(g)^{-1}.$$

> [!example]
> Each of the following maps is a group homomorphism
> 1. The map $\phi : \mathbb Z \rightarrow Z / N \mathbb Z$ that sends $a \in \mathbb Z$ to $a \mod N$ in $\mathbb Z / N \mathbb Z$.
> 2. The map $\phi : \mathbb R^* \rightarrow GL_2(\mathbb R)$ defined by $\phi(a) = \begin{pmatrix}a & 0 \\ 0 & a^{-1}\end{pmatrix}.$
