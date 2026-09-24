Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter II: Groups, first encounter, Section 1.6: Order; Exercise 1.11; Exercise 1.14; Exercise 1.15; Section 4.2: Homomorphisms and order.

## Definition

> [!definition] Order of a Group
> The **order of** [[Group]] $G$ is the number of elements in $G$; it is denoted by $|G|$ or $\# G$. We write $|G| = \inf$ if $G$ is infinite.

> [!definition] Order of a Group Element
> Let $G$ be a [[Group]] and let $g \in G$ be an element of the group. Suppose there exists a positive integer $n$ with the property that $g^n = e_G$. The smallest such $n$ is called the **order of** $g$. If there is no such $n$, then $g$ is said to have **infinite order**. We denote the order of the element as $|g|$.

## Property

>[!proposition]
>Let $G$ be a finite group. Then every element of $G$ has finite order. Further, if $g \in G$ has order $n$ and if $g^k = e_G$, then $n \mid k$.

> [!proposition]
> Let $g \in G$ be an element of finite order. Then $g^m$ has finite order $\forall m \geq 0$, and in fact
> $$|g^m| = \frac{\text{lcm}(m, |g|)}{m} = \frac{|g|}{\gcd(m, |g|)}$$

### Commute Element

> [!proposition]
> If $gh = hg$:
> - $|gh| \mid \mathsf{lcm}(|g|, |h|)$.
> - $\mathsf{gcd}(|g|, |h|) = 1 \implies |gh| = |g| |h|$.
> 
> ---
> $(gh)^o = g^o h^o$.

> [!theorem]
> $\forall g, h \in G: |gh| = |hg|$.
> 
> ---
> $\forall a, g \in G: |aga^{-1}| = |g|$ as $g^o = (a g a^{-1})^o = a g^o a^{-1}$.

> [!theorem]
> Let $G$ be an [[Abelian Group]], and $g \in G$ be an element of maximal **finite** order, that is, for all $h \in G$ has finite order, then $|h| \leq |g|$. Then:
> $$|h| < \infty \implies |h| \mid |g|.$$
> 
> ---
> Proof by contradiction: 
> Assume that $|h| > |g|$ then there exists prime $p$:
> $$|g| = p^m r \land |h| = p^n s \land \mathsf{gcd}(r; p) = \mathsf{gcd}(s, p) = 1 \land m < n.$$ 
> And thus we have the contradiction:
> $$|g^{p^m} h^s| = p^n r > p^m r = |g|.$$

### Group Homomorphism

> [!proposition]
> Let $\varphi: G \rightarrow H$ be a [[Group Homomorphism]], and let $g \in G$ be an element of finite order. Then $|\varphi(g)|$ divides $|g|$.
