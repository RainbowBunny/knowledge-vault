Reference:
- [[Book Reference|Algebra: Chapter 0]] - Chapter II: Groups, first encounter, Section 1.5: Commutative Groups; Exercise 1.8.
- [[Book Reference|Algebra: Chapter 0]] - Chapter III: Rings and modules, Section 5.2: The category R-Mod.

## Definition

> [!definition] Abelian Group
> A [[Group]] $(G, \star)$ is called Abelian Group if its operation $\star$ is [[Commutativity|Commutative]].

> [!remark]
> The **operation** in an abelian group $A$ is, denoted by $+$ and is called 'addition'; the **identity** is then called $0_A$; and the **inverse** of an element $a \in A$ is denoted $-a$. The 'power' notation is of course replaced by 'multiple': $0a = 0$, and for a positive integer $n$
> $$na = \underbrace{a + \dots + a}_{n \text{ times}}, \quad (-n)a = \underbrace{(-a) + \dots + (-a)}_{n \text{ times}}.$$

## Property

> [!proposition]
> Suppose that $g^2 = e_G$ for all elements $g$ of a group $G$; then $G$ is commutative.

> [!proposition]
> Let $G$ be a finite abelian group with exactly one element $f$ of order 2. Then:
> $$\prod_{g \in G} g = f.$$
> 
> ---
> Find element $a$ such that $a = a^{-1}$, or $a^2 = e_G$ because other element will cancel out. Thus:
> $$\prod_{g \in G} g = e_g \star g = g.$$

> [!proposition]
> Requires:: [[R-Module]]
> 
> ---
> Every abelian group is a $\mathbb{Z}$-module, in exactly one way.