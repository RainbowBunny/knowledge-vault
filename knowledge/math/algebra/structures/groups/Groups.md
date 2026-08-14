## Basic Definition

>[!definition] Group
A **group** consists of a nonempty set $G$ and a rule, which we denote by $\star$, for combining two elements $a, b \in G$ to obtain an element $a \star b \in G$. The composition operation $\star$ is required to have the following three properties: 
> 1. (**Identity Law**) 
> $$(\exists e_G \in G) (\forall g \in G): g \star e_G = g = e_G \star g$$ 
> 2. (**Inverse Law**) 
> $$(\forall g \in G) (\exists h \in G): g \star h = e_G = h \star g$$
> 3. (**Associate Law**) 
> $$(\forall g, h, k \in G): (g \star h) \star k = g \star (h \star k)$$

### Order

> [!definition] Order of a Group
> The **order of** $G$ is the number of elements in $G$; it is denoted by $|G|$ or $\# G$. We write $|G| = \inf$ if $G$ is infinite.

> [!definition] Order of a group element
> Let $G$ be a group and let $g \in G$ be an element of the group. Suppose there exists a positive integer $n$ with the property that $g^n = e$. The smallest such $n$ is called the **order of** $g$. If there is no such $n$, then $g$ is said to have **infinite order**. We denote the order of the element as $|g|$.

>[!proposition]
>Let $G$ be a finite group. Then every element of $G$ has finite order. Further, if $g \in G$ has order $n$ and if $g^k = e$, then $n \mid k$.

> [!theorem] Lagrange's Theorem
> Let $G$ be a finite group and let $g \in G$. Then the order of $g$ divides the order of $G$.
> More precisely, let $n = |G|$ be the order of $G$ and let $n$ be the order of $g$. Then
> $$a^k = e \qquad \text{and} \qquad n \mid k$$

> [!proposition]
> Let $g \in G$ be an element of finite order. Then $g^m$ has finite order $\forall m \geq 0$, and in fact
> $$|g^m| = \frac{\text{lcm}(m, |g|)}{m} = \frac{|g|}{\gcd(m, |g|)}$$

> [!proposition]
> If $gh = hg$, then $|gh|$ divides $\text{lcm}(|g|, |h|)$.





## Property

### Identity

> [!proposition] Uniqueness of Identity
> If $h \in G$ is an identity of $G$, then $h = e_G$.

### Inverse

> [!proposition] Uniqueness of Inverse
> If $h_1, h_2$ are both inverses of $g$ in $G$, then $h_1 = h_2$.

> [!proposition] Inverse of Product
> $$\forall g, h \in G, \quad (gh)^{-1} = h^{-1} g^{-1}$$

### Cancellation

> [!proposition]
> Let $G$ be a group. Then $\forall a, g, h \in G$
> $$ga = ha \Longrightarrow g = h, \quad ag = ah \Longrightarrow g = h$$

## Subgroup

> [!definition] Additive Subgroup
> A subset $L$ of $\mathbb R^m$ is an **additive subgroup** if it is closed under addition and subtraction.

> [!definition] Discrete Additive Subgroup
> An additive subgroup is called a **discrete additive subgroup** if there is a positive constant $\epsilon > 0$ with the following property: for every $\textbf{v} \in L$, $$L \cap \{\textbf{w} \in \mathbb R^m: ||\textbf{v} - \textbf{w}|| < \epsilon\} = \{\textbf{v}\}.$$

> [!theorem] Lagrange's Theorem
> Let $H$ be a subgroup of a finite group $G$. Then $|H|$ divides $|G|$.
 
## Example

> [!example]
> Each of the following is a group:
> 1. $\text{GL}_n(\mathbb R) = \{n\text{-by-}n \text{ matrices } A \text{ with real coefficients and } \det(A) \neq 0\}$ with operation $\star$ is matrix multiplication.

> [!definition] General Linear Group
> The **General Linear Group** of order $s$, denoted $\text{GL}_s(\mathbb Z_n)$, is the monoid of invertible $s \times s$ matrices containing elements from $\mathbb Z_n$ with respect to multiplication such that the determinants of the matrices and $n$ are relatively prime.

> [!theorem]
> The order of the General Linear Group $\text{GL}_2(\mathbb Z_p)$ is given by $$|\text{GL}_2(\mathbb Z_p)| = (p^2 - 1)(q^2 - 1),$$ where $p$ is a prime integer.

> [!lemma]
> Let $n = pq$ where $p$ and $q$ are distinct prime integers. If $M \in \text{GL}_2(\mathbb Z_n)$, then $M \in \text{GL}_2(\mathbb Z_p)$ and $M \in \text{GL}_2(\mathbb Z_q)$. 
 